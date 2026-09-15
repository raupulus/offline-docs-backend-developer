---
title: Query The EXPLAIN Setting For A Prepared Statement
source_url: https://www.sqlite.org/c3ref/stmt_isexplain.html
source_path: c3ref/stmt_isexplain.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1920
---

> \
> int sqlite3_stmt_isexplain(sqlite3_stmt \*pStmt);\

The sqlite3_stmt_isexplain(S) interface returns 1 if the prepared statement S is an EXPLAIN statement, or 2 if the statement S is an EXPLAIN QUERY PLAN. The sqlite3_stmt_isexplain(S) interface returns 0 if S is an ordinary statement or a NULL pointer.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
