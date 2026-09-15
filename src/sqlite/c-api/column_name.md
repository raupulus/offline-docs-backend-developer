---
title: Column Names In A Result Set
source_url: https://www.sqlite.org/c3ref/column_name.html
source_path: c3ref/column_name.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 900
---

> \
> const char \*sqlite3_column_name(sqlite3_stmt\*, int N);\
> const void \*sqlite3_column_name16(sqlite3_stmt\*, int N);\

These routines return the name assigned to a particular column in the result set of a [SELECT](../lang_select.md) statement. The sqlite3_column_name() interface returns a pointer to a zero-terminated UTF-8 string and sqlite3_column_name16() returns a pointer to a zero-terminated UTF-16 string. The first parameter is the [prepared statement](../c3ref/stmt.md) that implements the [SELECT](../lang_select.md) statement. The second parameter is the column number. The leftmost column is number 0.

The returned string pointer is valid until either the [prepared statement](../c3ref/stmt.md) is destroyed by [sqlite3_finalize()](../c3ref/finalize.md) or until the statement is automatically reprepared by the first call to [sqlite3_step()](../c3ref/step.md) for a particular run or until the next call to sqlite3_column_name() or sqlite3_column_name16() on the same column.

If sqlite3_malloc() fails during the processing of either routine (for example during a conversion from UTF-8 to UTF-16) then a NULL pointer is returned.

The name of a result column is the value of the "AS" clause for that column, if there is an AS clause. If there is no AS clause then the name of the column is unspecified and may change from one release of SQLite to the next.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
