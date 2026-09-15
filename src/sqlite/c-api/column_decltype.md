---
title: Declared Datatype Of A Query Result
source_url: https://www.sqlite.org/c3ref/column_decltype.html
source_path: c3ref/column_decltype.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 890
---

> \
> const char \*sqlite3_column_decltype(sqlite3_stmt\*,int);\
> const void \*sqlite3_column_decltype16(sqlite3_stmt\*,int);\

The first parameter is a [prepared statement](../c3ref/stmt.md). If this statement is a [SELECT](../lang_select.md) statement and the Nth column of the returned result set of that [SELECT](../lang_select.md) is a table column (not an expression or subquery) then the declared type of the table column is returned. If the Nth column of the result set is an expression or subquery, then a NULL pointer is returned. The returned string is always UTF-8 encoded.

For example, given the database schema:

CREATE TABLE t1(c1 VARIANT);

and the following statement to be compiled:

SELECT c1 + 1, c1 FROM t1;

this routine would return the string "VARIANT" for the second result column (i==1), and a NULL pointer for the first result column (i==0).

SQLite uses dynamic run-time typing. So just because a column is declared to contain a particular type does not mean that the data stored in that column is of the declared type. SQLite is strongly typed, but the typing is dynamic not static. Type is associated with individual values, not with the containers used to hold those values.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
