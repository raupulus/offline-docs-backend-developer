---
title: Change The EXPLAIN Setting For A Prepared Statement
source_url: https://www.sqlite.org/c3ref/stmt_explain.html
source_path: c3ref/stmt_explain.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1910
---

> \
> int sqlite3_stmt_explain(sqlite3_stmt \*pStmt, int eMode);\

The sqlite3_stmt_explain(S,E) interface changes the EXPLAIN setting for [prepared statement](../c3ref/stmt.md) S. If E is zero, then S becomes a normal prepared statement. If E is 1, then S behaves as if its SQL text began with "[EXPLAIN](../lang_explain.md)". If E is 2, then S behaves as if its SQL text began with "[EXPLAIN QUERY PLAN](../eqp.md)".

Calling sqlite3_stmt_explain(S,E) might cause S to be reprepared. SQLite tries to avoid a reprepare, but a reprepare might be necessary on the first transition into EXPLAIN or EXPLAIN QUERY PLAN mode.

Because of the potential need to reprepare, a call to sqlite3_stmt_explain(S,E) will fail with SQLITE_ERROR if S cannot be reprepared because it was created using [sqlite3_prepare()](../c3ref/prepare.md) instead of the newer [sqlite3_prepare_v2()](../c3ref/prepare.md) or [sqlite3_prepare_v3()](../c3ref/prepare.md) interfaces and hence has no saved SQL text with which to reprepare.

Changing the explain setting for a prepared statement does not change the original SQL text for the statement. Hence, if the SQL text originally began with EXPLAIN or EXPLAIN QUERY PLAN, but sqlite3_stmt_explain(S,0) is called to convert the statement into an ordinary statement, the EXPLAIN or EXPLAIN QUERY PLAN keywords will still appear in the sqlite3_sql(S) output, even though the statement now acts like a normal SQL statement.

This routine returns SQLITE_OK if the explain mode is successfully changed, or an error code if the explain mode could not be changed. The explain mode cannot be changed while a statement is active. Hence, it is good practice to call [sqlite3_reset(S)](../c3ref/reset.md) immediately prior to calling sqlite3_stmt_explain(S,E).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
