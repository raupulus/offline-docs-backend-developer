---
title: Recover snapshots from a wal file
source_url: https://www.sqlite.org/c3ref/snapshot_recover.html
source_path: c3ref/snapshot_recover.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1840
---

> \
> int sqlite3_snapshot_recover(sqlite3 \*db, const char \*zDb);\

If a [WAL file](../wal.md#walfile) remains on disk after all database connections close (either through the use of the [SQLITE_FCNTL_PERSIST_WAL](../c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlpersistwal) [file control](../c3ref/file_control.md) or because the last process to have the database opened exited without calling [sqlite3_close()](../c3ref/close.md)) and a new connection is subsequently opened on that database and [WAL file](../wal.md#walfile), the [sqlite3_snapshot_open()](../c3ref/snapshot_open.md) interface will only be able to open the last transaction added to the WAL file even though the WAL file contains other valid transactions.

This function attempts to scan the WAL file associated with database zDb of database handle db and make all valid snapshots available to sqlite3_snapshot_open(). It is an error if there is already a read transaction open on the database, or if the database is not a WAL mode database.

SQLITE_OK is returned if successful, or an SQLite error code otherwise.

This interface is only available if SQLite is compiled with the [SQLITE_ENABLE_SNAPSHOT](../compile.md#enable_snapshot) option.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
