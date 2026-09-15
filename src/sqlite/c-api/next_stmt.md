---
title: Find the next prepared statement
source_url: https://www.sqlite.org/c3ref/next_stmt.html
source_path: c3ref/next_stmt.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1560
---

> \
> sqlite3_stmt \*sqlite3_next_stmt(sqlite3 \*pDb, sqlite3_stmt \*pStmt);\

This interface returns a pointer to the next [prepared statement](../c3ref/stmt.md) after pStmt associated with the [database connection](../c3ref/sqlite3.md) pDb. If pStmt is NULL then this interface returns a pointer to the first prepared statement associated with the database connection pDb. If no prepared statement satisfies the conditions of this routine, it returns NULL.

The [database connection](../c3ref/sqlite3.md) pointer D in a call to [sqlite3_next_stmt(D,S)](../c3ref/next_stmt.md) must refer to an open database connection and in particular must not be a NULL pointer.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
