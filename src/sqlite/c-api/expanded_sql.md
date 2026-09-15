---
title: Retrieving Statement SQL
source_url: https://www.sqlite.org/c3ref/expanded_sql.html
source_path: c3ref/expanded_sql.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1210
---

> \
> const char \*sqlite3_sql(sqlite3_stmt \*pStmt);\
> char \*sqlite3_expanded_sql(sqlite3_stmt \*pStmt);\
> \#ifdef SQLITE_ENABLE_NORMALIZE\
> const char \*sqlite3_normalized_sql(sqlite3_stmt \*pStmt);\
> \#endif\

The sqlite3_sql(P) interface returns a pointer to a copy of the UTF-8 SQL text used to create [prepared statement](../c3ref/stmt.md) P if P was created by [sqlite3_prepare_v2()](../c3ref/prepare.md), [sqlite3_prepare_v3()](../c3ref/prepare.md), [sqlite3_prepare16_v2()](../c3ref/prepare.md), or [sqlite3_prepare16_v3()](../c3ref/prepare.md). The sqlite3_expanded_sql(P) interface returns a pointer to a UTF-8 string containing the SQL text of prepared statement P with [bound parameters](../lang_expr.md#varparam) expanded. The sqlite3_normalized_sql(P) interface returns a pointer to a UTF-8 string containing the normalized SQL text of prepared statement P. The semantics used to normalize a SQL statement are unspecified and subject to change. At a minimum, literal values will be replaced with suitable placeholders.

For example, if a prepared statement is created using the SQL text "SELECT \$abc,:xyz" and if parameter \$abc is bound to integer 2345 and parameter :xyz is unbound, then sqlite3_sql() will return the original string, "SELECT \$abc,:xyz" but sqlite3_expanded_sql() will return "SELECT 2345,NULL".

The sqlite3_expanded_sql() interface returns NULL if insufficient memory is available to hold the result, or if the result would exceed the maximum string length determined by the [SQLITE_LIMIT_LENGTH](../c3ref/c_limit_attached.md#sqlitelimitlength).

The [SQLITE_TRACE_SIZE_LIMIT](../compile.md#trace_size_limit) compile-time option limits the size of bound parameter expansions. The [SQLITE_OMIT_TRACE](../compile.md#omit_trace) compile-time option causes sqlite3_expanded_sql() to always return NULL.

The strings returned by sqlite3_sql(P) and sqlite3_normalized_sql(P) are managed by SQLite and are automatically freed when the prepared statement is finalized. The string returned by sqlite3_expanded_sql(P), on the other hand, is obtained from [sqlite3_malloc()](../c3ref/free.md) and must be freed by the application by passing it to [sqlite3_free()](../c3ref/free.md).

The sqlite3_normalized_sql() interface is only available if the [SQLITE_ENABLE_NORMALIZE](../compile.md#enable_normalize) compile-time option is defined.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
