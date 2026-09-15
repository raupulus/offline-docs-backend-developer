---
title: Record A Database Snapshot
source_url: https://www.sqlite.org/c3ref/snapshot_get.html
source_path: c3ref/snapshot_get.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1820
---

> \
> int sqlite3_snapshot_get(\
>   sqlite3 \*db,\
>   const char \*zSchema,\
>   sqlite3_snapshot \*\*ppSnapshot\
> );\

The [sqlite3_snapshot_get(D,S,P)](../c3ref/snapshot_get.md) interface attempts to make a new [sqlite3_snapshot](../c3ref/snapshot.md) object that records the current state of schema S in database connection D. On success, the [sqlite3_snapshot_get(D,S,P)](../c3ref/snapshot_get.md) interface writes a pointer to the newly created [sqlite3_snapshot](../c3ref/snapshot.md) object into \*P and returns SQLITE_OK. If there is not already a read-transaction open on schema S when this function is called, one is opened automatically.

If a read-transaction is opened by this function, then it is guaranteed that the returned snapshot object may not be invalidated by a database writer or checkpointer until after the read-transaction is closed. This is not guaranteed if a read-transaction is already open when this function is called. In that case, any subsequent write or checkpoint operation on the database may invalidate the returned snapshot handle, even while the read-transaction remains open.

The following must be true for this function to succeed. If any of the following statements are false when sqlite3_snapshot_get() is called, SQLITE_ERROR is returned. The final value of \*P is undefined in this case.

- The database handle must not be in [autocommit mode](../c3ref/get_autocommit.md).
- Schema S of [database connection](../c3ref/sqlite3.md) D must be a [WAL mode](../wal.md) database.
- There must not be a write transaction open on schema S of database connection D.
- One or more transactions must have been written to the current wal file since it was created on disk (by any connection). This means that a snapshot cannot be taken on a wal mode database with no wal file immediately after it is first opened. At least one transaction must be written to it first.

This function may also return SQLITE_NOMEM. If it is called with the database handle in autocommit mode but fails for some other reason, whether or not a read transaction is opened on schema S is undefined.

The [sqlite3_snapshot](../c3ref/snapshot.md) object returned from a successful call to [sqlite3_snapshot_get()](../c3ref/snapshot_get.md) must be freed using [sqlite3_snapshot_free()](../c3ref/snapshot_free.md) to avoid a memory leak.

The [sqlite3_snapshot_get()](../c3ref/snapshot_get.md) interface is only available when the [SQLITE_ENABLE_SNAPSHOT](../compile.md#enable_snapshot) compile-time option is used.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
