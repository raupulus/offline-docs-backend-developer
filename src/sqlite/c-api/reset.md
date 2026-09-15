---
title: Reset A Prepared Statement Object
source_url: https://www.sqlite.org/c3ref/reset.html
source_path: c3ref/reset.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1690
---

> \
> int sqlite3_reset(sqlite3_stmt \*pStmt);\

The sqlite3_reset() function is called to reset a [prepared statement](../c3ref/stmt.md) object back to its initial state, ready to be re-executed. Any SQL statement variables that had values bound to them using the [sqlite3_bind\_\*() API](../c3ref/bind_blob.md) retain their values. Use [sqlite3_clear_bindings()](../c3ref/clear_bindings.md) to reset the bindings.

The [sqlite3_reset(S)](../c3ref/reset.md) interface resets the [prepared statement](../c3ref/stmt.md) S back to the beginning of its program.

The return code from [sqlite3_reset(S)](../c3ref/reset.md) indicates whether or not the previous evaluation of prepared statement S completed successfully. If [sqlite3_step(S)](../c3ref/step.md) has never before been called on S or if [sqlite3_step(S)](../c3ref/step.md) has not been called since the previous call to [sqlite3_reset(S)](../c3ref/reset.md), then [sqlite3_reset(S)](../c3ref/reset.md) will return [SQLITE_OK](../rescode.md#ok).

If the most recent call to [sqlite3_step(S)](../c3ref/step.md) for the [prepared statement](../c3ref/stmt.md) S indicated an error, then [sqlite3_reset(S)](../c3ref/reset.md) returns an appropriate [error code](../rescode.md). The [sqlite3_reset(S)](../c3ref/reset.md) interface might also return an [error code](../rescode.md) if there were no prior errors but the process of resetting the prepared statement caused a new error. For example, if an [INSERT](../lang_insert.md) statement with a [RETURNING](../lang_returning.md) clause is only stepped one time, that one call to [sqlite3_step(S)](../c3ref/step.md) might return SQLITE_ROW but the overall statement might still fail and the [sqlite3_reset(S)](../c3ref/reset.md) call might return SQLITE_BUSY if locking constraints prevent the database change from committing. Therefore, it is important that applications check the return code from [sqlite3_reset(S)](../c3ref/reset.md) even if no prior call to [sqlite3_step(S)](../c3ref/step.md) indicated a problem.

The [sqlite3_reset(S)](../c3ref/reset.md) interface does not change the values of any [bindings](../c3ref/bind_blob.md) on the [prepared statement](../c3ref/stmt.md) S.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
