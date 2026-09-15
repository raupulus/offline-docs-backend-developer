---
title: Checkpoint a database
source_url: https://www.sqlite.org/c3ref/wal_checkpoint.html
source_path: c3ref/wal_checkpoint.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2350
---

> \
> int sqlite3_wal_checkpoint(sqlite3 \*db, const char \*zDb);\

The sqlite3_wal_checkpoint(D,X) is equivalent to [sqlite3_wal_checkpoint_v2](../c3ref/wal_checkpoint_v2.md)(D,X,[SQLITE_CHECKPOINT_PASSIVE](../c3ref/c_checkpoint_full.md),0,0).

In brief, sqlite3_wal_checkpoint(D,X) causes the content in the [write-ahead log](../wal.md) for database X on [database connection](../c3ref/sqlite3.md) D to be transferred into the database file and for the write-ahead log to be reset. See the [checkpointing](../wal.md#ckpt) documentation for addition information.

This interface used to be the only way to cause a checkpoint to occur. But then the newer and more powerful [sqlite3_wal_checkpoint_v2()](../c3ref/wal_checkpoint_v2.md) interface was added. This interface is retained for backwards compatibility and as a convenience for applications that need to manually start a callback but which do not need the full power (and corresponding complication) of [sqlite3_wal_checkpoint_v2()](../c3ref/wal_checkpoint_v2.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
