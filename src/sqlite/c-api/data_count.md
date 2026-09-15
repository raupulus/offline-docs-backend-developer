---
title: Number of columns in a result set
source_url: https://www.sqlite.org/c3ref/data_count.html
source_path: c3ref/data_count.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1020
---

> \
> int sqlite3_data_count(sqlite3_stmt \*pStmt);\

The sqlite3_data_count(P) interface returns the number of columns in the current row of the result set of [prepared statement](../c3ref/stmt.md) P. If prepared statement P does not have results ready to return (via calls to the [sqlite3_column()](../c3ref/column_blob.md) family of interfaces) then sqlite3_data_count(P) returns 0. The sqlite3_data_count(P) routine also returns 0 if P is a NULL pointer. The sqlite3_data_count(P) routine returns 0 if the previous call to [sqlite3_step](../c3ref/step.md)(P) returned [SQLITE_DONE](../rescode.md#done). The sqlite3_data_count(P) will return non-zero if previous call to [sqlite3_step](../c3ref/step.md)(P) returned [SQLITE_ROW](../rescode.md#row), except in the case of the [PRAGMA incremental_vacuum](../pragma.md#pragma_incremental_vacuum) where it always returns zero since each step of that multi-step pragma returns 0 columns of data.

See also: [sqlite3_column_count()](../c3ref/column_count.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
