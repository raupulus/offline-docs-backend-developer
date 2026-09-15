---
title: Checkpoint Mode Values
source_url: https://www.sqlite.org/c3ref/c_checkpoint_full.html
source_path: c3ref/c_checkpoint_full.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 470
---

> \
> \#define SQLITE_CHECKPOINT_NOOP    -1  /\* Do no work at all \*/\
> \#define SQLITE_CHECKPOINT_PASSIVE  0  /\* Do as much as possible w/o blocking \*/\
> \#define SQLITE_CHECKPOINT_FULL     1  /\* Wait for writers, then checkpoint \*/\
> \#define SQLITE_CHECKPOINT_RESTART  2  /\* Like FULL but wait for readers \*/\
> \#define SQLITE_CHECKPOINT_TRUNCATE 3  /\* Like RESTART but also truncate WAL \*/\

These constants define all valid values for the "checkpoint mode" passed as the third parameter to the [sqlite3_wal_checkpoint_v2()](../c3ref/wal_checkpoint_v2.md) interface. See the [sqlite3_wal_checkpoint_v2()](../c3ref/wal_checkpoint_v2.md) documentation for details on the meaning of each of these checkpoint modes.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
