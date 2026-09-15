---
title: Database Snapshot
source_url: https://www.sqlite.org/c3ref/snapshot.html
source_path: c3ref/snapshot.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1790
---

> \
> typedef struct sqlite3_snapshot {\
>   unsigned char hidden\[48\];\
> } sqlite3_snapshot;\

An instance of the snapshot object records the state of a [WAL mode](../wal.md) database for some specific point in history.

In [WAL mode](../wal.md), multiple [database connections](../c3ref/sqlite3.md) that are open on the same database file can each be reading a different historical version of the database file. When a [database connection](../c3ref/sqlite3.md) begins a read transaction, that connection sees an unchanging copy of the database as it existed for the point in time when the transaction first started. Subsequent changes to the database from other connections are not seen by the reader until a new read transaction is started.

The sqlite3_snapshot object records state information about an historical version of the database file so that it is possible to later open a new read transaction that sees that historical version of the database rather than the most recent version.

1 Constructor using this object: [sqlite3_snapshot_get()](../c3ref/snapshot_get.md)

1 Destructor using this object: [sqlite3_snapshot_free()](../c3ref/snapshot_free.md)

3 Methods using this object: [sqlite3_snapshot_cmp()](../c3ref/snapshot_cmp.md), [sqlite3_snapshot_open()](../c3ref/snapshot_open.md), [sqlite3_snapshot_recover()](../c3ref/snapshot_recover.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
