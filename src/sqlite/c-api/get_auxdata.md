---
title: Function Auxiliary Data
source_url: https://www.sqlite.org/c3ref/get_auxdata.html
source_path: c3ref/get_auxdata.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1330
---

> \
> void \*sqlite3_get_auxdata(sqlite3_context\*, int N);\
> void sqlite3_set_auxdata(sqlite3_context\*, int N, void\*, void (\*)(void\*));\

These functions may be used by (non-aggregate) SQL functions to associate auxiliary data with argument values. If the same argument value is passed to multiple invocations of the same SQL function during query execution, under some circumstances the associated auxiliary data might be preserved. An example of where this might be useful is in a regular-expression matching function. The compiled version of the regular expression can be stored as auxiliary data associated with the pattern string. Then as long as the pattern string remains the same, the compiled regular expression can be reused on multiple invocations of the same function.

The sqlite3_get_auxdata(C,N) interface returns a pointer to the auxiliary data associated by the sqlite3_set_auxdata(C,N,P,X) function with the Nth argument value to the application-defined function. N is zero for the left-most function argument. If there is no auxiliary data associated with the function argument, the sqlite3_get_auxdata(C,N) interface returns a NULL pointer.

The sqlite3_set_auxdata(C,N,P,X) interface saves P as auxiliary data for the N-th argument of the application-defined function. Subsequent calls to sqlite3_get_auxdata(C,N) return P from the most recent sqlite3_set_auxdata(C,N,P,X) call if the auxiliary data is still valid or NULL if the auxiliary data has been discarded. After each call to sqlite3_set_auxdata(C,N,P,X) where X is not NULL, SQLite will invoke the destructor function X with parameter P exactly once, when the auxiliary data is discarded. SQLite is free to discard the auxiliary data at any time, including:

- when the corresponding function parameter changes, or
- when [sqlite3_reset()](../c3ref/reset.md) or [sqlite3_finalize()](../c3ref/finalize.md) is called for the SQL statement, or
- when sqlite3_set_auxdata() is invoked again on the same parameter, or
- during the original sqlite3_set_auxdata() call when a memory allocation error occurs.
- during the original sqlite3_set_auxdata() call if the function is evaluated during query planning instead of during query execution, as sometimes happens with [SQLITE_ENABLE_STAT4](../compile.md#enable_stat4).

Note the last two bullets in particular. The destructor X in sqlite3_set_auxdata(C,N,P,X) might be called immediately, before the sqlite3_set_auxdata() interface even returns. Hence sqlite3_set_auxdata() should be called near the end of the function implementation and the function implementation should not make any use of P after sqlite3_set_auxdata() has been called. Furthermore, a call to sqlite3_get_auxdata() that occurs immediately after a corresponding call to sqlite3_set_auxdata() might still return NULL if an out-of-memory condition occurred during the sqlite3_set_auxdata() call or if the function is being evaluated during query planning rather than during query execution.

In practice, auxiliary data is preserved between function calls for function parameters that are compile-time constants, including literal values and [parameters](../lang_expr.md#varparam) and expressions composed from the same.

The value of the N parameter to these interfaces should be non-negative. Future enhancements may make use of negative N values to define new kinds of function caching behavior.

These routines must be called from the same thread in which the SQL function is running.

See also: [sqlite3_get_clientdata()](../c3ref/get_clientdata.md) and [sqlite3_set_clientdata()](../c3ref/get_clientdata.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
