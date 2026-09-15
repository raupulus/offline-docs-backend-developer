---
title: Determine If Virtual Table Column Access Is For UPDATE
source_url: https://www.sqlite.org/c3ref/vtab_nochange.html
source_path: c3ref/vtab_nochange.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2310
---

> \
> int sqlite3_vtab_nochange(sqlite3_context\*);\

If the sqlite3_vtab_nochange(X) routine is called within the [xColumn](../vtab.md#xcolumn) method of a [virtual table](../vtab.md), then it might return true if the column is being fetched as part of an UPDATE operation during which the column value will not change. The virtual table implementation can use this hint as permission to substitute a return value that is less expensive to compute and that the corresponding [xUpdate](../vtab.md#xupdate) method understands as a "no-change" value.

If the [xColumn](../vtab.md#xcolumn) method calls sqlite3_vtab_nochange() and finds that the column is not changed by the UPDATE statement, then the xColumn method can optionally return without setting a result, without calling any of the [sqlite3_result_xxxxx() interfaces](../c3ref/result_blob.md). In that case, [sqlite3_value_nochange(X)](../c3ref/value_blob.md) will return true for the same column in the [xUpdate](../vtab.md#xupdate) method.

The sqlite3_vtab_nochange() routine is an optimization. Virtual table implementations should continue to give a correct answer even if the sqlite3_vtab_nochange() interface were to always return false. In the current implementation, the sqlite3_vtab_nochange() interface does always returns false for the enhanced [UPDATE FROM](../lang_update.md#upfrom) statement.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
