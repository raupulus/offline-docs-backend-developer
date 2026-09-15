---
title: How To Corrupt An SQLite Database File
source_url: https://www.sqlite.org/howtocorrupt.html
source_path: howtocorrupt.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 3020
---

## Overview

An SQLite database is highly resistant to corruption. If an application crash, or an operating-system crash, or even a power failure occurs in the middle of a transaction, the partially written transaction should be automatically rolled back the next time the database file is accessed. The recovery process is fully automatic and does not require any action on the part of the user or the application.

Though SQLite is resistant to database corruption, it is not immune. This document describes the various ways that an SQLite database might go corrupt.

# 1.  File overwrite by a rogue thread or process

SQLite database files are ordinary disk files. That means that any process can open the file and overwrite it with garbage. There is nothing that the SQLite library can do to defend against this.

<span id="stalefd"></span>

## 1.1.  Continuing to use a file descriptor after it has been closed

We have seen multiple cases where a file descriptor was open on a file, then that file descriptor was closed and reopened on an SQLite database. Later, some other thread continued to write into the old file descriptor, not realizing that the original file had been closed already. But because the file descriptor had been reopened by SQLite, the information that was intended to go into the original file ended up overwriting parts of the SQLite database, leading to corruption of the database.

One example of this occurred circa 2013-08-30 on the canonical repository for the [Fossil DVCS](http://www.fossil-scm.org/). In that event, file descriptor 2 (standard error) was being erroneously closed (by [stunnel](http://www.stunnel.org/), we suspect) prior to [sqlite3_open_v2()](c3ref/open.md) so that the file descriptor used for the repository database file was 2. Later, an application bug caused an assert() statement to emit an error message by invoking write(2,...). But since file descriptor 2 was now connected to a database file, the error message overwrote part of the database. To guard against this kind of problem, SQLite [version 3.8.1](releaselog/3_8_1.md) (2013-10-17) and later refuse to use low-numbered file descriptors for database files. (See [SQLITE_MINIMUM_FILE_DESCRIPTOR](compile.md#minimum_file_descriptor) for additional information.)

Another example of corruption caused by using a closed file descriptor was [reported by facebook engineers](https://code.facebook.com/posts/313033472212144/debugging-file-corruption-on-ios/) in a blog post on 2014-08-12.

Another example of this error was reported against [Fossil](https://fossil-scm.org/) on 2019-07-11. A file descriptor would be opened for debugging output, but then closed and reopened by SQLite. But the debugging logic continued to write into the original file descriptor. See the [forum discussion](https://fossil-scm.org/forum/forumpost/c51b9a1169) for the bug report and a link to the fix.

## 1.2.  Backup or restore while a transaction is active

Systems that run automatic backups in the background might try to make a backup copy of an SQLite database file while it is in the middle of a transaction. The backup copy then might contain some old and some new content, and thus be corrupt.

There are multiple safe approaches to making backup copies of SQLite databases - safe in the sense that they are generate a correct, uncorrupted backup. In no particular order:

1.  The [sqlite3_rsync](rsync.md) utility program (available beginning with SQLite 3.47.0 (2024-10-21) and later) will make a copy of a live SQLite over SSH using a bandwidth-efficient protocol.

2.  The [VACUUM INTO *filename*](lang_vacuum.md#vacuuminto) command copies out the current state of an SQLite database into a separate file.

3.  The [backup API](backup.md) is a C-language interface that can make a consistent copy of an SQLite database.

Any of the above approaches will work even on a live database. It is also safe to make a copy of an SQLite database file as long as there are no transactions in progress while the copy is taking place. If the previous write transaction failed, then it is important that any rollback journal (the `*-journal` file) or write-ahead log (the `*-wal` file) be copied together with the database file itself.

<span id="delhotjrnl"></span>

## 1.3.  Deleting a hot journal

SQLite normally stores all content in a single disk file. However, while performing a transaction, information necessary to recover the database following a crash or power failure is stored in auxiliary journal files. Such journal files are described as ["hot"](fileformat2.md#hotjrnl). The journal files have the same name as the original database file with the addition of `-journal` or `-wal` suffix.

SQLite must see the journal files in order to recover from a crash or power failure. If the [hot journal files](fileformat2.md#hotjrnl) are moved, deleted, or renamed after a crash or power failure, then automatic recovery will not work and the database may go corrupt.

Another manifestation of this problem is [database corruption caused by inconsistent use of 8+3 filenames](shortnames.md#db83corrupt).

<span id="roguejrnl"></span>

## 1.4.  Mispairing database files and hot journals

The previous example is a specific case of a more general problem: The state of an SQLite database is controlled by both the database file and the journal file. In a quiescent state, the journal file does not exist and only the database file matters. But if the journal file does exist, it must be kept together with the database to avoid corruption. The following actions are all likely to lead to corruption:

- Swapping journal files between two different databases.
- Overwriting a journal file with a different journal file.
- Moving a journal file from one database to another.
- Copying a database file without also copying its journal.
- Overwriting a database file with another without also deleting any hot journal associated with the original database.

# 2.  File locking problems

SQLite uses file locks on the database file, and on the [write-ahead log](wal.md) or [WAL](wal.md) file, to coordinate access between concurrent processes. Without coordination, two threads or processes might try to make incompatible changes to a database file at the same time, resulting in database corruption.

## 2.1.  Filesystems with broken or missing lock implementations

SQLite depends on the underlying filesystem to do locking as the documentation says it will. But some filesystems contain bugs in their locking logic such that the locks do not always behave as advertised. This is especially true of network filesystems and NFS in particular. If SQLite is used on a filesystem where the locking primitives contain bugs, and if two or more threads or processes try to access the same database at the same time, then database corruption might result.

<span id="posix_close_bug"></span>

## 2.2.  Posix advisory locks canceled by a separate thread doing close()

The default locking mechanism used by SQLite on unix platforms is POSIX advisory locking. Unfortunately, POSIX advisory locking has design quirks that make it prone to misuse and failure. In particular, any thread in the same process with a file descriptor that is holding a POSIX advisory lock can override that lock using a different file descriptor. One particularly pernicious problem is that the `close()` system call will cancel all POSIX advisory locks on the same file for all threads and all file descriptors in the process.

So, for example, suppose a multi-thread process has two or more threads with separate SQLite database connections to the same database file. Then a third thread comes along and wants to read something out of that same database file on its own, without using the SQLite library. Maybe the third thread wants to make a backup copy of the database. Or maybe the third thread is just trying to identify the file type and hences tries to read the first 16 bytes to determine if it really is an SQLite database. Regardless of the reason, the third thread does an `open()`, a `read()` and then a `close()`. One would think this would be harmless. But the `close()` system call caused the locks held on the database by all the other threads to be dropped. Those other threads have no way of knowing that their locks have just been trashed (POSIX does not provide any mechanism to determine this) and so they keep on running under the assumption that their locks are still valid. This can lead to two or more threads or processes trying to write to the database at the same time, resulting in database corruption.

Note that it is perfectly safe for two or more threads to access the same SQLite database file using the SQLite library. The unix drivers for SQLite know about the POSIX advisory locking quirks and work around them. This problem only arises when a thread tries to bypass the SQLite library and read the database file directly.

Beginning with SQLite version 3.51.0 (2025-11-04), SQLite implements additional defenses to try to avoid problems caused by locks that are broken by `close()`. These new defenses help when the database is in [WAL mode](wal.md) and is being accessed from multiple processes. But they are not a cure-all. To avoid corruptions, developers should be careful to never use `close()` on an SQLite database file while one or more database connections are open, even in other threads.

## 2.3. Multiple copies of SQLite linked into the same application

As pointed out in the previous section, SQLite takes steps to work around the quirks of POSIX advisory locking. Part of that work-around involves keeping a global list (mutex protected) of open SQLite database files. But, if multiple copies of SQLite are linked into the same application, then there will be multiple instances of this global list. Database connections opened using one copy of the SQLite library will be unaware of database connections opened using the other copy, and will be unable to work around the POSIX advisory locking quirks. A `close()` operation on one connection might unknowingly clear the locks on a different database connection, leading to database corruption.

The scenario above sounds far-fetched. But the SQLite developers are aware of at least one commercial product that was released with exactly this bug. The vendor came to the SQLite developers seeking help in tracking down some infrequent database corruption issues they were seeing on Linux and Mac. The problem was eventually traced to the fact that the application was linking against two separate copies of SQLite. The solution was to change the application build procedures to link against just one copy of SQLite instead of two.

## 2.4.  Two processes using different locking protocols

The default locking mechanism used by SQLite on unix platforms is POSIX advisory locking, but there are other options. By selecting an alternative [sqlite3_vfs](c3ref/vfs.md) using the [sqlite3_open_v2()](c3ref/open.md) interface, an application can make use of other locking protocols that might be more appropriate to certain filesystems. For example, dot-file locking might be selected for use in an application that has to run on an NFS filesystem that does not support POSIX advisory locking.

It is important that all connections to the same database file use the same locking protocol. If one application is using POSIX advisory locks and another application is using dot-file locking, then the two applications will not see each other's locks and will not be able to coordinate database access, possibly leading to database corruption.

<span id="unlink"></span>

## 2.5.  Unlinking or renaming a database file while in use

If two processes have open connections to the same database file and one process closes its connection, unlinks the file, then creates a new database file in its place with the same name and reopens the new file, then the two processes will be talking to different database files with the same name. (Note that this is only possible on Posix and Posix-like systems that permit a file to be unlinked while it is still open for reading and writing. Windows does not allow this to occur.) Since rollback journals and WAL files are based on the name of the database file, the two different database files will share the same rollback journal or WAL file. A rollback or recovery for one of the databases might use content from the other database, resulting in corruption. A similar problem occurs if a database file is renamed while it is opened and a new file is created with the old name.

In other words, unlinking or renaming an open database file results in behavior that is undefined and probably undesirable.

Beginning with SQLite [version 3.7.17](releaselog/3_7_17.md) (2013-05-20), the unix OS interface will send SQLITE_WARNING messages to the [error log](errlog.md) if a database file is unlinked while it is still in use.

<span id="alias"></span>

## 2.6.  Multiple links to the same file

If a single database file has multiple links (either hard or soft links) then that is just another way of saying that the file has multiple names. If two or more processes open the database using different names, then they will use different rollback journals and WAL files. That means that if one process crashes, the other process will be unable to recover the transaction in progress because it will be looking in the wrong place for the appropriate journal.

In other words, opening and using a database file that has two or more names results in behavior that is undefined and probably undesirable.

Beginning with SQLite [version 3.7.17](releaselog/3_7_17.md) (2013-05-20), the unix OS interface will send SQLITE_WARNING messages to the [error log](errlog.md) if a database file has multiple hard links.

Beginning with SQLite [version 3.10.0](releaselog/3_10_0.md) (2016-01-06), the unix OS interface will attempt to resolve symbolic links and open the database file by its canonical name. Prior to version 3.10.0, opening a database file through a symbolic link was similar to opening a database file that had multiple hard links and resulted in undefined behavior.

<span id="fork"></span>

## 2.7.  Carrying an open database connection across a fork()

Do not open an SQLite database connection, then fork(), then try to use that database connection in the child process. All kinds of locking problems will result and you can easily end up with a corrupt database. SQLite is not designed to support that kind of behavior. Any database connection that is used in a child process must be opened in the child process, not inherited from the parent.

Do not even call [sqlite3_close()](c3ref/close.md) on a database connection from a child process if the connection was opened in the parent. It is safe to close the underlying file descriptor, but the [sqlite3_close()](c3ref/close.md) interface might invoke cleanup activities that will delete content out from under the parent, leading to errors and perhaps even database corruption.

# 3.  Failure to sync

In order to guarantee that database files are always consistent, SQLite will occasionally ask the operating system to flush all pending writes to persistent storage then wait for that flush to complete. This is accomplished using the `fsync()` system call under unix and `FlushFileBuffers()` under Windows. We call this flush of pending writes a "sync".

Actually, if one is only concerned with atomic and consistent writes and is willing to forego durable writes, the sync operation does not need to wait until the content is completely stored on persistent media. Instead, the sync operation can be thought of as an I/O barrier. As long as all writes that occur before the sync are completed before any write that happens after the sync, no database corruption will occur. If sync is operating as an I/O barrier and not as a true sync, then a power failure or system crash might cause one or more previously committed transactions to roll back (in violation of the "durable" property of "ACID") but the database will at least continue to be consistent, and that is what most people care about.

## 3.1.  Disk drives that do not honor sync requests

Unfortunately, most consumer-grade mass storage devices lie about syncing. Disk drives will report that content is safely on persistent media as soon as it reaches the track buffer and before actually being written to oxide. This makes the disk drives seem to operate faster (which is vitally important to the manufacturer so that they can show good benchmark numbers in trade magazines). And in fairness, the lie normally causes no harm, as long as there is no power loss or hard reset prior to the track buffer actually being written to oxide. But if a power loss or hard reset does occur, and if that results in content that was written after a sync reaching oxide while content written before the sync is still in a track buffer, then database corruption can occur.

USB flash memory sticks seem to be especially pernicious liars regarding sync requests. One can easily see this by committing a large transaction to an SQLite database on a USB memory stick. The COMMIT command will return relatively quickly, indicating that the memory stick has told the operating system and the operating system has told SQLite that all content is safely in persistent storage, and yet the LED on the end of the memory stick will continue flashing for several more seconds. Pulling out the memory stick while the LED is still flashing will frequently result in database corruption.

Note that SQLite must believe whatever the operating system and hardware tell it about the status of sync requests. There is no way for SQLite to detect that either is lying and that writes might be occurring out-of-order. However, SQLite in [WAL mode](wal.md) is far more forgiving of out-of-order writes than in the default rollback journal modes. In WAL mode, the only time that a failed sync operation can cause database corruption is during a [checkpoint](wal.md#ckpt) operation. A sync failure during a COMMIT might result in loss of durability but not in a corrupt database file. Hence, one line of defense against database corruption due to failed sync operations is to use SQLite in WAL mode and to checkpoint as infrequently as possible.

## 3.2.  Disabling sync using PRAGMAs

The sync operations that SQLite performs to help ensure integrity can be disabled at run-time using the [synchronous pragma](pragma.md#pragma_synchronous). By setting PRAGMA synchronous=OFF, all sync operations are omitted. This makes SQLite seem to run faster, but it also allows the operating system to freely reorder writes, which could result in database corruption if a power failure or hard reset occurs prior to all content reaching persistent storage.

For maximum reliability and for robustness against database corruption, SQLite should always be run with its default synchronous setting of FULL.

<span id="hardwarefault"></span>

# 4.  Disk Drive and Flash Memory Failures

An SQLite database can become corrupt if the file content changes due to a disk drive or flash memory failure. It is very rare, but disks will occasionally flip a bit in the middle of a sector.

## 4.1.  Non-powersafe flash memory controllers

We are told that in some flash memory controllers the wear-leveling logic can cause random filesystem damage if power is interrupted during a write. This can manifest, for example, as random changes in the middle of a file that was not even open at the time of the power loss. So, for example, a device would be writing content into an MP3 file in flash memory when a power loss occurs, and that could result in an SQLite database being corrupted even though the database was not even in use at the time of the power loss.

<span id="fakeusb"></span>

## 4.2.  Fake capacity USB sticks

There are many fraudulent USB sticks in circulation that report to have a high capacity (ex: 8GB) but are really only capable of storing a much smaller amount (ex: 1GB). Attempts to write on these devices will often result in unrelated files being overwritten. Any use of a fraudulent flash memory device can easily lead to database corruption, therefore. Internet searches such as "fake capacity usb" will turn up lots of disturbing information about this problem.

# 5.  Memory corruption

SQLite is a C-library that runs in the same address space as the application that it serves. That means that stray pointers, buffer overruns, heap corruption, or other malfunctions in the application can corrupt internal SQLite data structure and ultimately result in a corrupt database file. Normally these kinds of problems manifest themselves as segfaults prior to any database corruption occurring, but there have been instances where application code errors have caused SQLite to malfunction subtly so as to corrupt the database file rather than panicking.

The memory corruption problem becomes more acute when using [memory-mapped I/O](mmap.md). When all or part of the database file is mapped into the application's address space, then a stray pointer that overwrites any part of that mapped space will immediately corrupt the database file, without requiring the application to do a subsequent write() system call.

# 6.  Other operating system problems

Sometimes operating systems will exhibit non-standard behavior which can lead to problems. Sometimes this non-standard behavior is deliberate, and sometimes it is a mistake in the implementation. But in any event, if the operating performs differently from they way SQLite expects it to perform, the possibility of database corruption exists.

## 6.1.  Linux Threads

Some older versions of Linux used the LinuxThreads library for thread support. LinuxThreads is similar to Pthreads, but is subtly different with respect to handling of POSIX advisory locks. SQLite versions 2.2.3 through 3.6.23 recognized that LinuxThreads were being used at runtime and took appropriate action to work around the non-standard behavior of LinuxThreads. But most modern Linux implementations make use of the newer, and correct, NPTL implementation of Pthreads. Beginning with SQLite [version 3.7.0](releaselog/3_7_0.md) (2010-07-21), the use of NPTL is assumed. No checks are made. Hence, recent versions of SQLite will subtly malfunction and may corrupt database files if used in multi-threaded application that run on older linux systems that make use of LinuxThreads.

## 6.2.  Failures of mmap() on QNX

There exists some subtle problem with mmap() on QNX such that making a second mmap() call against a single file descriptor can cause the memory obtained from the first mmap() call to be zeroed. SQLite on unix uses mmap() to create a shared memory region for transaction coordination in [WAL mode](wal.md), and it will call mmap() multiple times for large transactions. The QNX mmap() has been demonstrated to corrupt database file under that scenario. QNX engineers are aware of this problem and are working on a solution; the problem may have already been fixed by the time you read this.

When running on QNX, it is recommended that [memory-mapped I/O](mmap.md) never be used. Furthermore, to use [WAL mode](wal.md), it is recommended that applications employ the [exclusive locking mode](pragma.md#pragma_locking_mode) in order to use [WAL without shared memory](wal.md#noshm). <span id="fscorruption"></span>

## 6.3.  Filesystem Corruption

Since SQLite databases are ordinary disk files, any malfunction in the filesystem can corrupt the database. Filesystems in modern operating systems are very reliable, but errors do still occur. For example, on 2013-10-01 the SQLite database that holds the [Wiki for Tcl/Tk](http://wiki.tcl-lang.org/) went corrupt a few days after the host computer was moved to a dodgy build of the (linux) kernel that had issues in the filesystem layer. In that event, the filesystem eventually became so badly corrupted that the machine was unusable, but the earliest symptom of trouble was the corrupted SQLite database.

<span id="cfgerr"></span>

# 7. SQLite Configuration Errors

SQLite has many built-in protections against database corruption. But many of these protections can be disabled by configuration options. If protections are disabled, database corruption may occur.

The following are examples of disabling the built-in protection mechanisms of SQLite:

- Setting [PRAGMA synchronous=OFF](pragma.md#pragma_synchronous) can cause the database to go corrupt if there is an operating-system crash or power failure, though this setting is safe from damage due to application crashes.

- Changing the [PRAGMA schema_version](pragma.md#pragma_schema_version) while other database connections are open.

- Using [PRAGMA journal_mode=OFF](pragma.md#pragma_journal_mode) or [PRAGMA journal_mode=MEMORY](pragma.md#pragma_journal_mode) and taking an application crash in the middle of a write transaction.

- Setting [PRAGMA writable_schema=ON](pragma.md#pragma_writable_schema) and then changing the database schema using DML statements can render the database completely unreadable, if not done carefully.

# 8.  Bugs in SQLite

SQLite is [very carefully tested](testing.md) to help ensure that it is as bug-free as possible. Among the many tests that are carried out for every SQLite version are tests that simulate power failures, I/O errors, and out-of-memory (OOM) errors to verify that no database corruption occurs during any of these events. SQLite is also field-proven with approximately two billion active deployments with no serious problems.

Nevertheless, no software is 100% perfect. There have been a few historical bugs in SQLite (now fixed) that could cause database corruption. And there may be yet a few more that remain undiscovered. Because of the extensive testing and widespread use of SQLite, bugs that result in database corruption tend to be very obscure. The likelihood of an application encountering an SQLite bug is small. To illustrate this, an account is given below of all database-corruption bugs found in SQLite during the four-year period from 2009-04-01 to 2013-04-15. This account should give the reader an intuitive sense of the kinds of bugs in SQLite that manage to slip through testing procedures and make it into a release.

## 8.1.  Race condition when writing to a WAL-mode database.

When there are two or more database connections in separate threads or processes, both open on the same [WAL-mode](wal.md) database, and if both connections try to write or run checkpoint at the same time, then there is a race condition that might corrupt the database file. This is the [WAL-reset bug](wal.md#walresetbug). It existed in all versions of SQLite from 3.7.0 through 3.51.2. See the [WAL-reset bug](wal.md#walresetbug) documentation for details.

## 8.2.  Stale expression indexes

An "expression index" is an index that references an expression or a [VIRTUAL generated column](gencol.md#vgc*). Expression indexes are suppose to use only [deterministic functions](deterministic.md). However, when moving an database across different platforms, or when changing SQLite versions, sometimes one of these supposely deterministic functions will change its output slightly. This can cause the index to appear to be corrupt. See the [stale expression index](staleexpridx.md) documentation for further details.

## 8.3.  False corruption reports due to database shrinkage

If a database is written by SQLite version 3.7.0 or later and then written again by SQLite version 3.6.23 or earlier in such a way as to make the size of the database file decrease, then the next time that SQLite version 3.7.0 accesses the database file, it might report that the database file is corrupt. The database file is not really corrupt, however. Version 3.7.0 was simply being overly zealous in its corruption detection.

The problem was fixed on 2011-02-20. The fix first appears in SQLite [version 3.7.6](releaselog/3_7_6.md) (2011-04-12).

## 8.4.  Corruption following switches between rollback and WAL modes

Repeatedly switching an SQLite database in and out of [WAL mode](wal.md) and running the [VACUUM](lang_vacuum.md) command in between switches, in one process or thread, can cause another process or thread that has the database file open to miss the fact that the database has changed. That second process or thread might then try to modify the database using a stale cache and cause database corruption.

This problem was discovered during internal testing and has never been observed in the wild. The problem was fixed on 2011-01-27 and in version 3.7.5.

## 8.5.  I/O error while obtaining a lock leads to corruption

If the operating system returns an I/O error while attempting to obtain a certain lock on shared memory in [WAL mode](wal.md) then SQLite might fail to reset its cache, which could lead to database corruption if subsequent writes are attempted.

Note that this problem only occurs if the attempt to acquire the lock resulted in an I/O error. If the lock is simply not granted (because some other thread or process is already holding a conflicting lock) then no corruption will ever occur. We are not aware of any operating systems that will fail with an I/O error while attempting to get a file lock on shared memory. So this is a theoretical problem rather than a real problem. Needless to say, this problem has never been observed in the wild. The problem was discovered while doing stress testing of SQLite in a test harness that simulates I/O errors.

This problem was fixed on 2010-09-20 for SQLite version 3.7.3.

## 8.6.  Database pages leak from the free page list

When content is deleted from an SQLite database, pages that are no longer used are added to a free list and are reused to hold content added by subsequent inserts. A bug in SQLite that was present in version 3.6.16 through 3.7.2 might cause pages to go missing out of the free list when [incremental_vacuum](pragma.md#pragma_incremental_vacuum) was used. This would not cause data loss. But it would result in the database file being larger than necessary. And it would cause the [integrity_check pragma](pragma.md#pragma_integrity_check) to report pages missing from the free list.

This problem was fixed on 2010-08-23 for SQLite version 3.7.2.

## 8.7.  Corruption following alternating writes from 3.6 and 3.7

SQLite version 3.7.0 introduced a number of new enhancements to the SQLite database file format (such as but not limited to [WAL](wal.md)). The 3.7.0 release was a shake-out release for these new features. We expected to find problems and were not disappointed.

If a database were originally created using SQLite version 3.7.0, then written by SQLite version 3.6.23.1 such that the size of the database file increased, then written again by SQLite version 3.7.0, the database file could go corrupt.

This problem was fixed on 2010-08-04 for SQLite version 3.7.1.

## 8.8.  Race condition in recovery on Windows systems

SQLite version 3.7.16.2 fixes a subtle race condition in the locking logic on Windows systems. When a database file is in need of recovery because the previous process writing to it crashed in the middle of a transaction and two or more processes try to open the that database at the same time, then the race condition might cause one of those processes to get a false indication that the recovery has already completed, allowing that process to continue using the database file without running recovery first. If that process writes to the file, then the file might go corrupt. This race condition had apparently existed in all prior versions of SQLite for Windows going back to 2004. But the race was very tight. Practically speaking, you need a fast multi-core machine in which you launch two processes to run recovery at the same moment on two separate cores. This defect was on Windows systems only and did not affect the posix OS interface.

<span id="svptbug"></span>

## 8.9.  Boundary value error in the secondary journals used by nested transactions

When a nested transaction is started using [SAVEPOINT](lang_savepoint.md), SQLite uses a secondary rollback journal to track the changes for the nested transaction, in case the inner transaction needs to be rolled back. Secondary journals are not involved in protecting the database from corruption due to program crashes or power outages. The secondary journals only come into play when rolling back an inner transaction of a nested transaction.

These secondary journals can be held either in memory or as temporary files on disk. The default behavior is to store them on disk. But that can be changed using the [-DSQLITE_TEMP_STORE](compile.md#temp_store) compile-time option, or at run-time using the [PRAGMA temp_store](pragma.md#pragma_temp_store) statement. The bug only arises when secondary journals are held in memory.

In SQLite [version 3.35.0](releaselog/3_35_0.md) (2021-03-12), a new optimization was added so that when SQLite is holding secondary journals in memory, less memory will be used. Unfortunately, a boundary check in the new logic was coded incorrectly. What should have been a "\<" operator was coded as "\<=". This error might cause the secondary journal to enter an inconsistent state if it is ever rolled back. If additional changes are made and the outer transaction eventually commits, the database might be left in an inconsistent state.

This problem was discovered by an [independent researcher](https://sqlite.org/forum/forumpost/b03d86f9516cb3a2) who was attempting to find bugs in SQLite using a fuzzer. The fuzzer found a failure in an [assert() statement](assert.md) that is used to help verify the internal state of the secondary journal. The bug was a sufficiently obscure corner-case that it might have gone unnoticed for many years, had it not been for the intensive use of assert() statements in SQLite, the persistence and tenacity of the security researchers, and their customized state-of-the-art fuzzer.

This problem was [fixed](https://sqlite.org/src/info/73c2b50211d3ae26) in [version 3.37.2](releaselog/3_37_2.md) (2022-01-06).
