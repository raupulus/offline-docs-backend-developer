---
title: Determine If A Prepared Statement Has Been Reset
source_url: https://www.sqlite.org/c3ref/stmt_busy.html
source_path: c3ref/stmt_busy.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1900
---

> \
> int sqlite3_stmt_busy(sqlite3_stmt\*);\

The sqlite3_stmt_busy(S) interface returns true (non-zero) if the [prepared statement](../c3ref/stmt.md) S has been stepped at least once using [sqlite3_step(S)](../c3ref/step.md) but has neither run to completion (returned [SQLITE_DONE](../rescode.md#done) from [sqlite3_step(S)](../c3ref/step.md)) nor been reset using [sqlite3_reset(S)](../c3ref/reset.md). The sqlite3_stmt_busy(S) interface returns false if S is a NULL pointer. If S is not a NULL pointer and is not a pointer to a valid [prepared statement](../c3ref/stmt.md) object, then the behavior is undefined and probably undesirable.

This interface can be used in combination [sqlite3_next_stmt()](../c3ref/next_stmt.md) to locate all prepared statements associated with a database connection that are in need of being reset. This can be used, for example, in diagnostic routines to search for prepared statements that are holding a transaction open.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
