---
title: Start a read transaction on an historical snapshot
source_url: https://www.sqlite.org/c3ref/snapshot_open.html
source_path: c3ref/snapshot_open.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1830
---

> \
> int sqlite3_snapshot_open(\
>   sqlite3 \*db,\
>   const char \*zSchema,\
>   sqlite3_snapshot \*pSnapshot\
> );\

The [sqlite3_snapshot_open(D,S,P)](../c3ref/snapshot_open.md) interface either starts a new read transaction or upgrades an existing one for schema S of [database connection](../c3ref/sqlite3.md) D such that the read transaction refers to historical [snapshot](../c3ref/snapshot.md) P, rather than the most recent change to the database. The [sqlite3_snapshot_open()](../c3ref/snapshot_open.md) interface returns SQLITE_OK on success or an appropriate [error code](../rescode.md) if it fails.

In order to succeed, the database connection must not be in [autocommit mode](../c3ref/get_autocommit.md) when [sqlite3_snapshot_open(D,S,P)](../c3ref/snapshot_open.md) is called. If there is already a read transaction open on schema S, then the database handle must have no active statements (SELECT statements that have been passed to sqlite3_step() but not sqlite3_reset() or sqlite3_finalize()). SQLITE_ERROR is returned if either of these conditions is violated, or if schema S does not exist, or if the snapshot object is invalid.

A call to sqlite3_snapshot_open() will fail to open if the specified snapshot has been overwritten by a [checkpoint](../wal.md#ckpt). In this case SQLITE_ERROR_SNAPSHOT is returned.

If there is already a read transaction open when this function is invoked, then the same read transaction remains open (on the same database snapshot) if SQLITE_ERROR, SQLITE_BUSY or SQLITE_ERROR_SNAPSHOT is returned. If another error code - for example SQLITE_PROTOCOL or an SQLITE_IOERR error code - is returned, then the final state of the read transaction is undefined. If SQLITE_OK is returned, then the read transaction is now open on database snapshot P.

A call to [sqlite3_snapshot_open(D,S,P)](../c3ref/snapshot_open.md) will fail if the database connection D does not know that the database file for schema S is in [WAL mode](../wal.md). A database connection might not know that the database file is in [WAL mode](../wal.md) if there has been no prior I/O on that database connection, or if the database entered [WAL mode](../wal.md) after the most recent I/O on the database connection. (Hint: Run "[PRAGMA application_id](../pragma.md#pragma_application_id)" against a newly opened database connection in order to make it ready to use snapshots.)

The [sqlite3_snapshot_open()](../c3ref/snapshot_open.md) interface is only available when the [SQLITE_ENABLE_SNAPSHOT](../compile.md#enable_snapshot) compile-time option is used.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
