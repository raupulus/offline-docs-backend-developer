---
title: Online Backup API.
source_url: https://www.sqlite.org/c3ref/backup_finish.html
source_path: c3ref/backup_finish.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 260
---

> \
> sqlite3_backup \*sqlite3_backup_init(\
>   sqlite3 \*pDest,                        /\* Destination database handle \*/\
>   const char \*zDestName,                 /\* Destination database name \*/\
>   sqlite3 \*pSource,                      /\* Source database handle \*/\
>   const char \*zSourceName                /\* Source database name \*/\
> );\
> int sqlite3_backup_step(sqlite3_backup \*p, int nPage);\
> int sqlite3_backup_finish(sqlite3_backup \*p);\
> int sqlite3_backup_remaining(sqlite3_backup \*p);\
> int sqlite3_backup_pagecount(sqlite3_backup \*p);\

The backup API copies the content of one database into another. It is useful either for creating backups of databases or for copying in-memory databases to or from persistent files.

See Also: [Using the SQLite Online Backup API](../backup.md)

SQLite holds a write transaction open on the destination database file for the duration of the backup operation. The source database is read-locked only while it is being read; it is not locked continuously for the entire backup operation. Thus, the backup may be performed on a live source database without preventing other database connections from reading or writing to the source database while the backup is underway.

To perform a backup operation:

1.  **sqlite3_backup_init()** is called once to initialize the backup,
2.  **sqlite3_backup_step()** is called one or more times to transfer the data between the two databases, and finally
3.  **sqlite3_backup_finish()** is called to release all resources associated with the backup operation.

There should be exactly one call to sqlite3_backup_finish() for each successful call to sqlite3_backup_init().

<span id="sqlite3backupinit"></span> **sqlite3_backup_init()**

The D and N arguments to sqlite3_backup_init(D,N,S,M) are the [database connection](../c3ref/sqlite3.md) associated with the destination database and the database name, respectively. The database name is "main" for the main database, "temp" for the temporary database, or the name specified after the AS keyword in an [ATTACH](../lang_attach.md) statement for an attached database. The S and M arguments passed to sqlite3_backup_init(D,N,S,M) identify the [database connection](../c3ref/sqlite3.md) and database name of the source database, respectively. The source and destination [database connections](../c3ref/sqlite3.md) (parameters S and D) must be different or else sqlite3_backup_init(D,N,S,M) will fail with an error.

A call to sqlite3_backup_init() will fail, returning NULL, if there is already a read or read-write transaction open on the destination database.

If an error occurs within sqlite3_backup_init(D,N,S,M), then NULL is returned and an error code and error message are stored in the destination [database connection](../c3ref/sqlite3.md) D. The error code and message for the failed call to sqlite3_backup_init() can be retrieved using the [sqlite3_errcode()](../c3ref/errcode.md), [sqlite3_errmsg()](../c3ref/errcode.md), and/or [sqlite3_errmsg16()](../c3ref/errcode.md) functions. A successful call to sqlite3_backup_init() returns a pointer to an [sqlite3_backup](../c3ref/backup.md) object. The [sqlite3_backup](../c3ref/backup.md) object may be used with the sqlite3_backup_step() and sqlite3_backup_finish() functions to perform the specified backup operation.

<span id="sqlite3backupstep"></span> **sqlite3_backup_step()**

Function sqlite3_backup_step(B,N) will copy up to N pages between the source and destination databases specified by [sqlite3_backup](../c3ref/backup.md) object B. If N is negative, all remaining source pages are copied. If sqlite3_backup_step(B,N) successfully copies N pages and there are still more pages to be copied, then the function returns [SQLITE_OK](../rescode.md#ok). If sqlite3_backup_step(B,N) successfully finishes copying all pages from source to destination, then it returns [SQLITE_DONE](../rescode.md#done). If an error occurs while running sqlite3_backup_step(B,N), then an [error code](../rescode.md) is returned. As well as [SQLITE_OK](../rescode.md#ok) and [SQLITE_DONE](../rescode.md#done), a call to sqlite3_backup_step() may return [SQLITE_READONLY](../rescode.md#readonly), [SQLITE_NOMEM](../rescode.md#nomem), [SQLITE_BUSY](../rescode.md#busy), [SQLITE_LOCKED](../rescode.md#locked), or an [SQLITE_IOERR_XXX](../rescode.md#ioerr_access) extended error code.

The sqlite3_backup_step() might return [SQLITE_READONLY](../rescode.md#readonly) if

1.  the destination database was opened read-only, or
2.  the destination database is using write-ahead-log journaling and the destination and source page sizes differ, or
3.  the destination database is an in-memory database and the destination and source page sizes differ.

If sqlite3_backup_step() cannot obtain a required file-system lock, then the [busy-handler function](../c3ref/busy_handler.md) is invoked (if one is specified). If the busy-handler returns non-zero before the lock is available, then [SQLITE_BUSY](../rescode.md#busy) is returned to the caller. In this case the call to sqlite3_backup_step() can be retried later. If the source [database connection](../c3ref/sqlite3.md) is being used to write to the source database when sqlite3_backup_step() is called, then [SQLITE_LOCKED](../rescode.md#locked) is returned immediately. Again, in this case the call to sqlite3_backup_step() can be retried later on. If [SQLITE_IOERR_XXX](../rescode.md#ioerr_access), [SQLITE_NOMEM](../rescode.md#nomem), or [SQLITE_READONLY](../rescode.md#readonly) is returned, then there is no point in retrying the call to sqlite3_backup_step(). These errors are considered fatal. The application must accept that the backup operation has failed and pass the backup operation handle to the sqlite3_backup_finish() to release associated resources.

The first call to sqlite3_backup_step() obtains an exclusive lock on the destination file. The exclusive lock is not released until either sqlite3_backup_finish() is called or the backup operation is complete and sqlite3_backup_step() returns [SQLITE_DONE](../rescode.md#done). Every call to sqlite3_backup_step() obtains a [shared lock](../lockingv3.md#shared_lock) on the source database that lasts for the duration of the sqlite3_backup_step() call. Because the source database is not locked between calls to sqlite3_backup_step(), the source database may be modified mid-way through the backup process. If the source database is modified by an external process or via a database connection other than the one being used by the backup operation, then the backup will be automatically restarted by the next call to sqlite3_backup_step(). If the source database is modified by using the same database connection as is used by the backup operation, then the backup database is automatically updated at the same time.

<span id="sqlite3backupfinish"></span> **sqlite3_backup_finish()**

When sqlite3_backup_step() has returned [SQLITE_DONE](../rescode.md#done), or when the application wishes to abandon the backup operation, the application should destroy the [sqlite3_backup](../c3ref/backup.md) by passing it to sqlite3_backup_finish(). The sqlite3_backup_finish() interfaces releases all resources associated with the [sqlite3_backup](../c3ref/backup.md) object. If sqlite3_backup_step() has not yet returned [SQLITE_DONE](../rescode.md#done), then any active write-transaction on the destination database is rolled back. The [sqlite3_backup](../c3ref/backup.md) object is invalid and may not be used following a call to sqlite3_backup_finish().

The value returned by sqlite3_backup_finish is [SQLITE_OK](../rescode.md#ok) if no sqlite3_backup_step() errors occurred, regardless of whether or not sqlite3_backup_step() completed. If an out-of-memory condition or IO error occurred during any prior sqlite3_backup_step() call on the same [sqlite3_backup](../c3ref/backup.md) object, then sqlite3_backup_finish() returns the corresponding [error code](../rescode.md).

A return of [SQLITE_BUSY](../rescode.md#busy) or [SQLITE_LOCKED](../rescode.md#locked) from sqlite3_backup_step() is not a permanent error and does not affect the return value of sqlite3_backup_finish().

<span id="sqlite3backupremaining"></span> <span id="sqlite3backuppagecount"></span> **sqlite3_backup_remaining() and sqlite3_backup_pagecount()**

The sqlite3_backup_remaining() routine returns the number of pages still to be backed up at the conclusion of the most recent sqlite3_backup_step(). The sqlite3_backup_pagecount() routine returns the total number of pages in the source database at the conclusion of the most recent sqlite3_backup_step(). The values returned by these functions are only updated by sqlite3_backup_step(). If the source database is modified in a way that changes the size of the source database or the number of pages remaining, those changes are not reflected in the output of sqlite3_backup_pagecount() and sqlite3_backup_remaining() until after the next sqlite3_backup_step().

**Concurrent Usage of Database Handles**

The source [database connection](../c3ref/sqlite3.md) may be used by the application for other purposes while a backup operation is underway or being initialized. If SQLite is compiled and configured to support threadsafe database connections, then the source database connection may be used concurrently from within other threads.

However, the application must guarantee that the destination [database connection](../c3ref/sqlite3.md) is not passed to any other API (by any thread) after sqlite3_backup_init() is called and before the corresponding call to sqlite3_backup_finish(). SQLite does not currently check to see if the application incorrectly accesses the destination [database connection](../c3ref/sqlite3.md) and so no error code is reported, but the operations may malfunction nevertheless. Use of the destination database connection while a backup is in progress might also cause a mutex deadlock.

If running in [shared cache mode](../sharedcache.md), the application must guarantee that the shared cache used by the destination database is not accessed while the backup is running. In practice this means that the application must guarantee that the disk file being backed up to is not accessed by any connection within the process, not just the specific connection that was passed to sqlite3_backup_init().

The [sqlite3_backup](../c3ref/backup.md) object itself is partially threadsafe. Multiple threads may safely make multiple concurrent calls to sqlite3_backup_step(). However, the sqlite3_backup_remaining() and sqlite3_backup_pagecount() APIs are not strictly speaking threadsafe. If they are invoked at the same time as another thread is invoking sqlite3_backup_step() it is possible that they return invalid values.

**Alternatives To Using The Backup API**

Other techniques for safely creating a consistent backup of an SQLite database include:

- The [VACUUM INTO](../lang_vacuum.md#vacuuminto) command.
- The [sqlite3_rsync](../rsync.md) utility program.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
