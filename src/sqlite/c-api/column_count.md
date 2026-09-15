---
title: Number Of Columns In A Result Set
source_url: https://www.sqlite.org/c3ref/column_count.html
source_path: c3ref/column_count.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 870
---

> \
> int sqlite3_column_count(sqlite3_stmt \*pStmt);\

Return the number of columns in the result set returned by the [prepared statement](../c3ref/stmt.md). If this routine returns 0, that means the [prepared statement](../c3ref/stmt.md) returns no data (for example an [UPDATE](../lang_update.md)). However, just because this routine returns a positive number does not mean that one or more rows of data will be returned. A SELECT statement will always have a positive sqlite3_column_count() but depending on the WHERE clause constraints and the table content, it might return no rows.

See also: [sqlite3_data_count()](../c3ref/data_count.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
