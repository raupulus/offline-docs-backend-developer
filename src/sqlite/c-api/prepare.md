---
title: Compiling An SQL Statement
source_url: https://www.sqlite.org/c3ref/prepare.html
source_path: c3ref/prepare.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1630
---

> \
> int sqlite3_prepare(\
>   sqlite3 \*db,            /\* Database handle \*/\
>   const char \*zSql,       /\* SQL statement, UTF-8 encoded \*/\
>   int nByte,              /\* Maximum length of zSql in bytes. \*/\
>   sqlite3_stmt \*\*ppStmt,  /\* OUT: Statement handle \*/\
>   const char \*\*pzTail     /\* OUT: Pointer to unused portion of zSql \*/\
> );\
> int sqlite3_prepare_v2(\
>   sqlite3 \*db,            /\* Database handle \*/\
>   const char \*zSql,       /\* SQL statement, UTF-8 encoded \*/\
>   int nByte,              /\* Maximum length of zSql in bytes. \*/\
>   sqlite3_stmt \*\*ppStmt,  /\* OUT: Statement handle \*/\
>   const char \*\*pzTail     /\* OUT: Pointer to unused portion of zSql \*/\
> );\
> int sqlite3_prepare_v3(\
>   sqlite3 \*db,            /\* Database handle \*/\
>   const char \*zSql,       /\* SQL statement, UTF-8 encoded \*/\
>   int nByte,              /\* Maximum length of zSql in bytes. \*/\
>   unsigned int prepFlags, /\* Zero or more SQLITE_PREPARE\_ flags \*/\
>   sqlite3_stmt \*\*ppStmt,  /\* OUT: Statement handle \*/\
>   const char \*\*pzTail     /\* OUT: Pointer to unused portion of zSql \*/\
> );\
> int sqlite3_prepare16(\
>   sqlite3 \*db,            /\* Database handle \*/\
>   const void \*zSql,       /\* SQL statement, UTF-16 encoded \*/\
>   int nByte,              /\* Maximum length of zSql in bytes. \*/\
>   sqlite3_stmt \*\*ppStmt,  /\* OUT: Statement handle \*/\
>   const void \*\*pzTail     /\* OUT: Pointer to unused portion of zSql \*/\
> );\
> int sqlite3_prepare16_v2(\
>   sqlite3 \*db,            /\* Database handle \*/\
>   const void \*zSql,       /\* SQL statement, UTF-16 encoded \*/\
>   int nByte,              /\* Maximum length of zSql in bytes. \*/\
>   sqlite3_stmt \*\*ppStmt,  /\* OUT: Statement handle \*/\
>   const void \*\*pzTail     /\* OUT: Pointer to unused portion of zSql \*/\
> );\
> int sqlite3_prepare16_v3(\
>   sqlite3 \*db,            /\* Database handle \*/\
>   const void \*zSql,       /\* SQL statement, UTF-16 encoded \*/\
>   int nByte,              /\* Maximum length of zSql in bytes. \*/\
>   unsigned int prepFlags, /\* Zero or more SQLITE_PREPARE\_ flags \*/\
>   sqlite3_stmt \*\*ppStmt,  /\* OUT: Statement handle \*/\
>   const void \*\*pzTail     /\* OUT: Pointer to unused portion of zSql \*/\
> );\

To execute an SQL statement, it must first be compiled into a byte-code program using one of these routines. Or, in other words, these routines are constructors for the [prepared statement](../c3ref/stmt.md) object.

The preferred routine to use is [sqlite3_prepare_v2()](../c3ref/prepare.md). The [sqlite3_prepare()](../c3ref/prepare.md) interface is legacy and should be avoided. [sqlite3_prepare_v3()](../c3ref/prepare.md) has an extra ["prepFlags" option](../c3ref/c_prepare_dont_log.md#sqlitepreparefromddl) that is sometimes needed for special purpose or to pass along security restrictions.

The use of the UTF-8 interfaces is preferred, as SQLite currently does all parsing using UTF-8. The UTF-16 interfaces are provided as a convenience. The UTF-16 interfaces work by converting the input text into UTF-8, then invoking the corresponding UTF-8 interface.

The first argument, "db", is a [database connection](../c3ref/sqlite3.md) obtained from a prior successful call to [sqlite3_open()](../c3ref/open.md), [sqlite3_open_v2()](../c3ref/open.md) or [sqlite3_open16()](../c3ref/open.md). The database connection must not have been closed.

The second argument, "zSql", is the statement to be compiled, encoded as either UTF-8 or UTF-16. The sqlite3_prepare(), sqlite3_prepare_v2(), and sqlite3_prepare_v3() interfaces use UTF-8, and sqlite3_prepare16(), sqlite3_prepare16_v2(), and sqlite3_prepare16_v3() use UTF-16.

If the nByte argument is negative, then zSql is read up to the first zero terminator. If nByte is positive, then it is the maximum number of bytes read from zSql. When nByte is positive, zSql is read up to the first zero terminator or until the nByte bytes have been read, whichever comes first. If nByte is zero, then no prepared statement is generated. If the caller knows that the supplied string is nul-terminated, then there is a small performance advantage to passing an nByte parameter that is the number of bytes in the input string *including* the nul-terminator. Note that nByte measures the length of the input in bytes, not characters, even for the UTF-16 interfaces.

If pzTail is not NULL then \*pzTail is made to point to the first byte past the end of the first SQL statement in zSql. These routines only compile the first statement in zSql, so \*pzTail is left pointing to what remains uncompiled.

\*ppStmt is left pointing to a compiled [prepared statement](../c3ref/stmt.md) that can be executed using [sqlite3_step()](../c3ref/step.md). If there is an error, \*ppStmt is set to NULL. If the input text contains no SQL (if the input is an empty string or a comment) then \*ppStmt is set to NULL. The calling procedure is responsible for deleting the compiled SQL statement using [sqlite3_finalize()](../c3ref/finalize.md) after it has finished with it. ppStmt may not be NULL.

On success, the sqlite3_prepare() family of routines return [SQLITE_OK](../rescode.md#ok); otherwise an [error code](../rescode.md) is returned.

The sqlite3_prepare_v2(), sqlite3_prepare_v3(), sqlite3_prepare16_v2(), and sqlite3_prepare16_v3() interfaces are recommended for all new programs. The older interfaces (sqlite3_prepare() and sqlite3_prepare16()) are retained for backwards compatibility, but their use is discouraged. In the "vX" interfaces, the prepared statement that is returned (the [sqlite3_stmt](../c3ref/stmt.md) object) contains a copy of the original SQL text. This causes the [sqlite3_step()](../c3ref/step.md) interface to behave differently in three ways:

If the database schema changes, instead of returning [SQLITE_SCHEMA](../rescode.md#schema) as it always used to do, [sqlite3_step()](../c3ref/step.md) will automatically recompile the SQL statement and try to run it again. As many as [SQLITE_MAX_SCHEMA_RETRY](../compile.md#max_schema_retry) retries will occur before sqlite3_step() gives up and returns an error.

When an error occurs, [sqlite3_step()](../c3ref/step.md) will return one of the detailed [error codes](../rescode.md) or [extended error codes](../rescode.md#extrc). The legacy behavior was that [sqlite3_step()](../c3ref/step.md) would only return a generic [SQLITE_ERROR](../rescode.md#error) result code and the application would have to make a second call to [sqlite3_reset()](../c3ref/reset.md) in order to find the underlying cause of the problem. With the "v2" prepare interfaces, the underlying reason for the error is returned immediately.

If the specific value bound to a [host parameter](../lang_expr.md#varparam) in the WHERE clause might influence the choice of query plan for a statement, then the statement will be automatically recompiled, as if there had been a schema change, on the first [sqlite3_step()](../c3ref/step.md) call following any change to the [bindings](../c3ref/bind_blob.md) of that [parameter](../lang_expr.md#varparam). The specific value of a WHERE-clause [parameter](../lang_expr.md#varparam) might influence the choice of query plan if the parameter is the left-hand side of a [LIKE](../lang_expr.md#like) or [GLOB](../lang_expr.md#glob) operator or if the parameter is compared to an indexed column and the [SQLITE_ENABLE_STAT4](../compile.md#enable_stat4) compile-time option is enabled.

sqlite3_prepare_v3() differs from sqlite3_prepare_v2() only in having the extra prepFlags parameter, which is a bit array consisting of zero or more of the [SQLITE_PREPARE\_\*](../c3ref/c_prepare_dont_log.md#sqlitepreparepersistent) flags. The sqlite3_prepare_v2() interface works exactly the same as sqlite3_prepare_v3() with a zero prepFlags parameter.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
