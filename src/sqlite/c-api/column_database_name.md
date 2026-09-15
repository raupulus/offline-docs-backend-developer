---
title: Source Of Data In A Query Result
source_url: https://www.sqlite.org/c3ref/column_database_name.html
source_path: c3ref/column_database_name.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 880
---

> \
> const char \*sqlite3_column_database_name(sqlite3_stmt\*,int);\
> const void \*sqlite3_column_database_name16(sqlite3_stmt\*,int);\
> const char \*sqlite3_column_table_name(sqlite3_stmt\*,int);\
> const void \*sqlite3_column_table_name16(sqlite3_stmt\*,int);\
> const char \*sqlite3_column_origin_name(sqlite3_stmt\*,int);\
> const void \*sqlite3_column_origin_name16(sqlite3_stmt\*,int);\

These routines provide a means to determine the database, table, and table column that is the origin of a particular result column in a [SELECT](../lang_select.md) statement. The name of the database or table or column can be returned as either a UTF-8 or UTF-16 string. The \_database\_ routines return the database name, the \_table\_ routines return the table name, and the origin\_ routines return the column name. The returned string is valid until the [prepared statement](../c3ref/stmt.md) is destroyed using [sqlite3_finalize()](../c3ref/finalize.md) or until the statement is automatically reprepared by the first call to [sqlite3_step()](../c3ref/step.md) for a particular run or until the same information is requested again in a different encoding.

The names returned are the original un-aliased names of the database, table, and column.

The first argument to these interfaces is a [prepared statement](../c3ref/stmt.md). These functions return information about the Nth result column returned by the statement, where N is the second function argument. The left-most column is column 0 for these routines.

If the Nth column returned by the statement is an expression or subquery and is not a column value, then all of these functions return NULL. These routines might also return NULL if a memory allocation error occurs. Otherwise, they return the name of the attached database, table, or column that query result column was extracted from.

As with all other SQLite APIs, those whose names end with "16" return UTF-16 encoded strings and the other functions return UTF-8.

These APIs are only available if the library was compiled with the [SQLITE_ENABLE_COLUMN_METADATA](../compile.md#enable_column_metadata) C-preprocessor symbol.

If two or more threads call one or more [column metadata interfaces](../c3ref/column_database_name.md) for the same [prepared statement](../c3ref/stmt.md) and result column at the same time then the results are undefined.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
