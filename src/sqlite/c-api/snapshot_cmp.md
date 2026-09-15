---
title: Compare the ages of two snapshot handles.
source_url: https://www.sqlite.org/c3ref/snapshot_cmp.html
source_path: c3ref/snapshot_cmp.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1800
---

> \
> int sqlite3_snapshot_cmp(\
>   sqlite3_snapshot \*p1,\
>   sqlite3_snapshot \*p2\
> );\

The sqlite3_snapshot_cmp(P1, P2) interface is used to compare the ages of two valid snapshot handles.

If the two snapshot handles are not associated with the same database file, the result of the comparison is undefined.

Additionally, the result of the comparison is only valid if both of the snapshot handles were obtained by calling sqlite3_snapshot_get() since the last time the wal file was deleted. The wal file is deleted when the database is changed back to rollback mode or when the number of database clients drops to zero. If either snapshot handle was obtained before the wal file was last deleted, the value returned by this function is undefined.

Otherwise, this API returns a negative value if P1 refers to an older snapshot than P2, zero if the two handles refer to the same database snapshot, and a positive value if P1 is a newer snapshot than P2.

This interface is only available if SQLite is compiled with the [SQLITE_ENABLE_SNAPSHOT](../compile.md#enable_snapshot) option.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
