---
title: Convenience Routines For Running Queries
source_url: https://www.sqlite.org/c3ref/free_table.html
source_path: c3ref/free_table.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1300
---

> \
> int sqlite3_get_table(\
>   sqlite3 \*db,          /\* An open database \*/\
>   const char \*zSql,     /\* SQL to be evaluated \*/\
>   char \*\*\*pazResult,    /\* Results of the query \*/\
>   int \*pnRow,           /\* Number of result rows written here \*/\
>   int \*pnColumn,        /\* Number of result columns written here \*/\
>   char \*\*pzErrmsg       /\* Error msg written here \*/\
> );\
> void sqlite3_free_table(char \*\*result);\

This is a legacy interface that is preserved for backwards compatibility. Use of this interface is not recommended.

Definition: A **result table** is a memory data structure created by the [sqlite3_get_table()](../c3ref/free_table.md) interface. A result table records the complete query results from one or more queries.

The table conceptually has a number of rows and columns. But these numbers are not part of the result table itself. These numbers are obtained separately. Let N be the number of rows and M be the number of columns.

A result table is an array of pointers to zero-terminated UTF-8 strings. There are (N+1)\*M elements in the array. The first M pointers point to zero-terminated strings that contain the names of the columns. The remaining entries all point to query results. NULL values result in NULL pointers. All other values are in their UTF-8 zero-terminated string representation as returned by [sqlite3_column_text()](../c3ref/column_blob.md).

A result table might consist of one or more memory allocations. It is not safe to pass a result table directly to [sqlite3_free()](../c3ref/free.md). A result table should be deallocated using [sqlite3_free_table()](../c3ref/free_table.md).

As an example of the result table format, suppose a query result is as follows:

> \
> Name        \| Age\
> -----------------------\
> Alice       \| 43\
> Bob         \| 28\
> Cindy       \| 21\

There are two columns (M==2) and three rows (N==3). Thus the result table has 8 entries. Suppose the result table is stored in an array named azResult. Then azResult holds this content:

> \
> azResult\[0\] = "Name";\
> azResult\[1\] = "Age";\
> azResult\[2\] = "Alice";\
> azResult\[3\] = "43";\
> azResult\[4\] = "Bob";\
> azResult\[5\] = "28";\
> azResult\[6\] = "Cindy";\
> azResult\[7\] = "21";\

The sqlite3_get_table() function evaluates one or more semicolon-separated SQL statements in the zero-terminated UTF-8 string of its 2nd parameter and returns a result table to the pointer given in its 3rd parameter.

After the application has finished with the result from sqlite3_get_table(), it must pass the result table pointer to sqlite3_free_table() in order to release the memory that was malloced. Because of the way the [sqlite3_malloc()](../c3ref/free.md) happens within sqlite3_get_table(), the calling function must not try to call [sqlite3_free()](../c3ref/free.md) directly. Only [sqlite3_free_table()](../c3ref/free_table.md) is able to release the memory properly and safely.

The sqlite3_get_table() interface is implemented as a wrapper around [sqlite3_exec()](../c3ref/exec.md). The sqlite3_get_table() routine does not have access to any internal data structures of SQLite. It uses only the public interface defined here. As a consequence, errors that occur in the wrapper layer outside of the internal [sqlite3_exec()](../c3ref/exec.md) call are not reflected in subsequent calls to [sqlite3_errcode()](../c3ref/errcode.md) or [sqlite3_errmsg()](../c3ref/errcode.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
