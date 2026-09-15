---
title: Configure an auto-checkpoint
source_url: https://www.sqlite.org/c3ref/wal_autocheckpoint.html
source_path: c3ref/wal_autocheckpoint.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2340
---

> \
> int sqlite3_wal_autocheckpoint(sqlite3 \*db, int N);\

The [sqlite3_wal_autocheckpoint(D,N)](../c3ref/wal_autocheckpoint.md) is a wrapper around [sqlite3_wal_hook()](../c3ref/wal_hook.md) that causes any database on [database connection](../c3ref/sqlite3.md) D to automatically [checkpoint](../wal.md#ckpt) after committing a transaction if there are N or more frames in the [write-ahead log](../wal.md) file. Passing zero or a negative value as the N parameter disables automatic checkpoints entirely.

The callback registered by this function replaces any existing callback registered using [sqlite3_wal_hook()](../c3ref/wal_hook.md). Likewise, registering a callback using [sqlite3_wal_hook()](../c3ref/wal_hook.md) disables the automatic checkpoint mechanism configured by this function.

The [wal_autocheckpoint pragma](../pragma.md#pragma_wal_autocheckpoint) can be used to invoke this interface from SQL.

Checkpoints initiated by this mechanism are [PASSIVE](../c3ref/wal_checkpoint_v2.md).

Every new [database connection](../c3ref/sqlite3.md) defaults to having the auto-checkpoint enabled with a threshold of 1000 or [SQLITE_DEFAULT_WAL_AUTOCHECKPOINT](../compile.md#default_wal_autocheckpoint) pages.

The use of this interface is only necessary if the default setting is found to be suboptimal for a particular application.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
