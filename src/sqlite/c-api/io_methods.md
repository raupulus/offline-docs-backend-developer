---
title: OS Interface File Virtual Methods Object
source_url: https://www.sqlite.org/c3ref/io_methods.html
source_path: c3ref/io_methods.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1410
---

> \
> typedef struct sqlite3_io_methods sqlite3_io_methods;\
> struct sqlite3_io_methods {\
>   int iVersion;\
>   int (\*xClose)(sqlite3_file\*);\
>   int (\*xRead)(sqlite3_file\*, void\*, int iAmt, sqlite3_int64 iOfst);\
>   int (\*xWrite)(sqlite3_file\*, const void\*, int iAmt, sqlite3_int64 iOfst);\
>   int (\*xTruncate)(sqlite3_file\*, sqlite3_int64 size);\
>   int (\*xSync)(sqlite3_file\*, int flags);\
>   int (\*xFileSize)(sqlite3_file\*, sqlite3_int64 \*pSize);\
>   int (\*xLock)(sqlite3_file\*, int);\
>   int (\*xUnlock)(sqlite3_file\*, int);\
>   int (\*xCheckReservedLock)(sqlite3_file\*, int \*pResOut);\
>   int (\*xFileControl)(sqlite3_file\*, int op, void \*pArg);\
>   int (\*xSectorSize)(sqlite3_file\*);\
>   int (\*xDeviceCharacteristics)(sqlite3_file\*);\
>   /\* Methods above are valid for version 1 \*/\
>   int (\*xShmMap)(sqlite3_file\*, int iPg, int pgsz, int, void volatile\*\*);\
>   int (\*xShmLock)(sqlite3_file\*, int offset, int n, int flags);\
>   void (\*xShmBarrier)(sqlite3_file\*);\
>   int (\*xShmUnmap)(sqlite3_file\*, int deleteFlag);\
>   /\* Methods above are valid for version 2 \*/\
>   int (\*xFetch)(sqlite3_file\*, sqlite3_int64 iOfst, int iAmt, void \*\*pp);\
>   int (\*xUnfetch)(sqlite3_file\*, sqlite3_int64 iOfst, void \*p);\
>   /\* Methods above are valid for version 3 \*/\
>   /\* Additional methods may be added in future releases \*/\
> };\

Every file opened by the [sqlite3_vfs.xOpen](../c3ref/vfs.md#sqlite3vfsxopen) method populates an [sqlite3_file](../c3ref/file.md) object (or, more commonly, a subclass of the [sqlite3_file](../c3ref/file.md) object) with a pointer to an instance of this object. This object defines the methods used to perform various operations against the open file represented by the [sqlite3_file](../c3ref/file.md) object.

If the [sqlite3_vfs.xOpen](../c3ref/vfs.md#sqlite3vfsxopen) method sets the sqlite3_file.pMethods element to a non-NULL pointer, then the sqlite3_io_methods.xClose method may be invoked even if the [sqlite3_vfs.xOpen](../c3ref/vfs.md#sqlite3vfsxopen) reported that it failed. The only way to prevent a call to xClose following a failed [sqlite3_vfs.xOpen](../c3ref/vfs.md#sqlite3vfsxopen) is for the [sqlite3_vfs.xOpen](../c3ref/vfs.md#sqlite3vfsxopen) to set the sqlite3_file.pMethods element to NULL.

The flags argument to xSync may be one of [SQLITE_SYNC_NORMAL](../c3ref/c_sync_dataonly.md) or [SQLITE_SYNC_FULL](../c3ref/c_sync_dataonly.md). The first choice is the normal fsync(). The second choice is a Mac OS X style fullsync. The [SQLITE_SYNC_DATAONLY](../c3ref/c_sync_dataonly.md) flag may be ORed in to indicate that only the data of the file and not its inode needs to be synced.

The integer values to xLock() and xUnlock() are one of

- [SQLITE_LOCK_NONE](../c3ref/c_lock_exclusive.md),
- [SQLITE_LOCK_SHARED](../c3ref/c_lock_exclusive.md),
- [SQLITE_LOCK_RESERVED](../c3ref/c_lock_exclusive.md),
- [SQLITE_LOCK_PENDING](../c3ref/c_lock_exclusive.md), or
- [SQLITE_LOCK_EXCLUSIVE](../c3ref/c_lock_exclusive.md).

xLock() upgrades the database file lock. In other words, xLock() moves the database file lock in the direction NONE toward EXCLUSIVE. The argument to xLock() is always one of SHARED, RESERVED, PENDING, or EXCLUSIVE, never SQLITE_LOCK_NONE. If the database file lock is already at or above the requested lock, then the call to xLock() is a no-op. xUnlock() downgrades the database file lock to either SHARED or NONE. If the lock is already at or below the requested lock state, then the call to xUnlock() is a no-op. The xCheckReservedLock() method checks whether any database connection, either in this process or in some other process, is holding a RESERVED, PENDING, or EXCLUSIVE lock on the file. It returns, via its output pointer parameter, true if such a lock exists and false otherwise.

The xFileControl() method is a generic interface that allows custom VFS implementations to directly control an open file using the [sqlite3_file_control()](../c3ref/file_control.md) interface. The second "op" argument is an integer opcode. The third argument is a generic pointer intended to point to a structure that may contain arguments or space in which to write return values. Potential uses for xFileControl() might be functions to enable blocking locks with timeouts, to change the locking strategy (for example to use dot-file locks), to inquire about the status of a lock, or to break stale locks. The SQLite core reserves all opcodes less than 100 for its own use. A [list of opcodes](../c3ref/c_fcntl_begin_atomic_write.md) less than 100 is available. Applications that define a custom xFileControl method should use opcodes greater than 100 to avoid conflicts. VFS implementations should return [SQLITE_NOTFOUND](../rescode.md#notfound) for file control opcodes that they do not recognize.

The xSectorSize() method returns the sector size of the device that underlies the file. The sector size is the minimum write that can be performed without disturbing other bytes in the file. The xDeviceCharacteristics() method returns a bit vector describing behaviors of the underlying device:

- [SQLITE_IOCAP_ATOMIC](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_ATOMIC512](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_ATOMIC1K](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_ATOMIC2K](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_ATOMIC4K](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_ATOMIC8K](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_ATOMIC16K](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_ATOMIC32K](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_ATOMIC64K](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_SAFE_APPEND](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_SEQUENTIAL](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_UNDELETABLE_WHEN_OPEN](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_POWERSAFE_OVERWRITE](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_IMMUTABLE](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_BATCH_ATOMIC](../c3ref/c_iocap_atomic.md)
- [SQLITE_IOCAP_SUBPAGE_READ](../c3ref/c_iocap_atomic.md)

The SQLITE_IOCAP_ATOMIC property means that all writes of any size are atomic. The SQLITE_IOCAP_ATOMICnnn values mean that writes of blocks that are nnn bytes in size and are aligned to an address which is an integer multiple of nnn are atomic. The SQLITE_IOCAP_SAFE_APPEND value means that when data is appended to a file, the data is appended first then the size of the file is extended, never the other way around. The SQLITE_IOCAP_SEQUENTIAL property means that information is written to disk in the same order as calls to xWrite().

If xRead() returns SQLITE_IOERR_SHORT_READ it must also fill in the unread portions of the buffer with zeros. A VFS that fails to zero-fill short reads might seem to work. However, failure to zero-fill short reads will eventually lead to database corruption.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
