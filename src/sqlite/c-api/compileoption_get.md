---
title: Run-Time Library Compilation Options Diagnostics
source_url: https://www.sqlite.org/c3ref/compileoption_get.html
source_path: c3ref/compileoption_get.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 920
---

> \
> \#ifndef SQLITE_OMIT_COMPILEOPTION_DIAGS\
> int sqlite3_compileoption_used(const char \*zOptName);\
> const char \*sqlite3_compileoption_get(int N);\
> \#else\
> \# define sqlite3_compileoption_used(X) 0\
> \# define sqlite3_compileoption_get(X)  ((void\*)0)\
> \#endif\

The sqlite3_compileoption_used() function returns 0 or 1 indicating whether the specified option was defined at compile time. The SQLITE\_ prefix may be omitted from the option name passed to sqlite3_compileoption_used().

The sqlite3_compileoption_get() function allows iterating over the list of options that were defined at compile time by returning the N-th compile time option string. If N is out of range, sqlite3_compileoption_get() returns a NULL pointer. The SQLITE\_ prefix is omitted from any strings returned by sqlite3_compileoption_get().

Support for the diagnostic functions sqlite3_compileoption_used() and sqlite3_compileoption_get() may be omitted by specifying the [SQLITE_OMIT_COMPILEOPTION_DIAGS](../compile.md#omit_compileoption_diags) option at compile time.

See also: SQL functions [sqlite_compileoption_used()](../lang_corefunc.md#sqlite_compileoption_used) and [sqlite_compileoption_get()](../lang_corefunc.md#sqlite_compileoption_get) and the [compile_options pragma](../pragma.md#pragma_compile_options).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
