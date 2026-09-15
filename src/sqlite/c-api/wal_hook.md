---
title: Write-Ahead Log Commit Hook
source_url: https://www.sqlite.org/c3ref/wal_hook.html
source_path: c3ref/wal_hook.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2370
---

> \
> void \*sqlite3_wal_hook(\
>   sqlite3\*,\
>   int(\*)(void \*,sqlite3\*,const char\*,int),\
>   void\*\
> );\

The [sqlite3_wal_hook()](../c3ref/wal_hook.md) function is used to register a callback that is invoked each time data is committed to a database in wal mode.

The callback is invoked by SQLite after the commit has taken place and the associated write-lock on the database released, so the implementation may read, write or [checkpoint](../wal.md#ckpt) the database as required.

The first parameter passed to the callback function when it is invoked is a copy of the third parameter passed to sqlite3_wal_hook() when registering the callback. The second is a copy of the database handle. The third parameter is the name of the database that was written to - either "main" or the name of an [ATTACH](../lang_attach.md)-ed database. The fourth parameter is the number of pages currently in the write-ahead log file, including those that were just committed.

The callback function should normally return [SQLITE_OK](../rescode.md#ok). If an error code is returned, that error will propagate back up through the SQLite code base to cause the statement that provoked the callback to report an error, though the commit will have still occurred. If the callback returns [SQLITE_ROW](../rescode.md#row) or [SQLITE_DONE](../rescode.md#done), or if it returns a value that does not correspond to any valid SQLite error code, the results are undefined.

A single database handle may have at most a single write-ahead log callback registered at one time. Calling [sqlite3_wal_hook()](../c3ref/wal_hook.md) replaces the default behavior or previously registered write-ahead log callback.

The return value is a copy of the third parameter from the previous call, if any, or 0.

The [sqlite3_wal_autocheckpoint()](../c3ref/wal_autocheckpoint.md) interface and the [wal_autocheckpoint pragma](../pragma.md#pragma_wal_autocheckpoint) both invoke [sqlite3_wal_hook()](../c3ref/wal_hook.md) and will overwrite any prior [sqlite3_wal_hook()](../c3ref/wal_hook.md) settings.

If a write-ahead log callback is set using this function then [sqlite3_wal_checkpoint_v2()](../c3ref/wal_checkpoint_v2.md) or [PRAGMA wal_checkpoint](../pragma.md#pragma_wal_checkpoint) should be invoked periodically to keep the write-ahead log file from growing without bound.

Passing a NULL pointer for the callback disables automatic checkpointing entirely. To re-enable the default behavior, call sqlite3_wal_autocheckpoint(db,1000) or use [PRAGMA wal_checkpoint](../pragma.md#pragma_wal_checkpoint).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
