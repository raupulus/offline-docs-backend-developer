---
title: Destroy a snapshot
source_url: https://www.sqlite.org/c3ref/snapshot_free.html
source_path: c3ref/snapshot_free.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1810
---

> \
> void sqlite3_snapshot_free(sqlite3_snapshot\*);\

The [sqlite3_snapshot_free(P)](../c3ref/snapshot_free.md) interface destroys [sqlite3_snapshot](../c3ref/snapshot.md) P. The application must eventually free every [sqlite3_snapshot](../c3ref/snapshot.md) object using this routine to avoid a memory leak.

The [sqlite3_snapshot_free()](../c3ref/snapshot_free.md) interface is only available when the [SQLITE_ENABLE_SNAPSHOT](../compile.md#enable_snapshot) compile-time option is used.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
