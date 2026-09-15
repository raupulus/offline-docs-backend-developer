---
title: Function Flags
source_url: https://www.sqlite.org/c3ref/c_deterministic.html
source_path: c3ref/c_deterministic.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 530
---

> \
> \#define SQLITE_DETERMINISTIC    0x000000800\
> \#define SQLITE_DIRECTONLY       0x000080000\
> \#define SQLITE_SUBTYPE          0x000100000\
> \#define SQLITE_INNOCUOUS        0x000200000\
> \#define SQLITE_RESULT_SUBTYPE   0x001000000\
> \#define SQLITE_SELFORDER1       0x002000000\

These constants may be ORed together with the [preferred text encoding](../c3ref/c_any.md#sqliteutf8) as the fourth argument to [sqlite3_create_function()](../c3ref/create_function.md), [sqlite3_create_function16()](../c3ref/create_function.md), or [sqlite3_create_function_v2()](../c3ref/create_function.md).

SQLITE_DETERMINISTIC  
The SQLITE_DETERMINISTIC flag means that the new function always gives the same output when the input parameters are the same. The [abs() function](../lang_corefunc.md#abs) is deterministic, for example, but [randomblob()](../lang_corefunc.md#randomblob) is not. Functions must be deterministic in order to be used in certain contexts such as with the WHERE clause of [partial indexes](../partialindex.md) or in [generated columns](../gencol.md). SQLite might also optimize deterministic functions by factoring them out of inner loops.

SQLITE_DIRECTONLY  
The SQLITE_DIRECTONLY flag means that the function may only be invoked from top-level SQL, and cannot be used in VIEWs or TRIGGERs nor in schema structures such as [CHECK constraints](../lang_createtable.md#ckconst), [DEFAULT clauses](../lang_createtable.md#dfltval), [expression indexes](../expridx.md), [partial indexes](../partialindex.md), or [generated columns](../gencol.md).

The SQLITE_DIRECTONLY flag is recommended for any [application-defined SQL function](../appfunc.md) that has side-effects or that could potentially leak sensitive information. This will prevent attacks in which an application is tricked into using a database file that has had its schema surreptitiously modified to invoke the application-defined function in ways that are harmful.

Some people say it is good practice to set SQLITE_DIRECTONLY on all [application-defined SQL functions](../appfunc.md), regardless of whether or not they are security sensitive, as doing so prevents those functions from being used inside of the database schema, and thus ensures that the database can be inspected and modified using generic tools (such as the [CLI](../cli.md)) that do not have access to the application-defined functions.

SQLITE_INNOCUOUS  
The SQLITE_INNOCUOUS flag means that the function is unlikely to cause problems even if misused. An innocuous function should have no side effects and should not depend on any values other than its input parameters. The [abs() function](../lang_corefunc.md#abs) is an example of an innocuous function. The [load_extension() SQL function](../lang_corefunc.md#load_extension) is not innocuous because of its side effects.

SQLITE_INNOCUOUS is similar to SQLITE_DETERMINISTIC, but is not exactly the same. The [random() function](../lang_corefunc.md#random) is an example of a function that is innocuous but not deterministic.

Some heightened security settings ([SQLITE_DBCONFIG_TRUSTED_SCHEMA](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigtrustedschema) and [PRAGMA trusted_schema=OFF](../pragma.md#pragma_trusted_schema)) disable the use of SQL functions inside views and triggers and in schema structures such as [CHECK constraints](../lang_createtable.md#ckconst), [DEFAULT clauses](../lang_createtable.md#dfltval), [expression indexes](../expridx.md), [partial indexes](../partialindex.md), and [generated columns](../gencol.md) unless the function is tagged with SQLITE_INNOCUOUS. Most built-in functions are innocuous. Developers are advised to avoid using the SQLITE_INNOCUOUS flag for application-defined functions unless the function has been carefully audited and found to be free of potentially security-adverse side-effects and information-leaks.

SQLITE_SUBTYPE  
The SQLITE_SUBTYPE flag indicates to SQLite that a function might call [sqlite3_value_subtype()](../c3ref/value_subtype.md) to inspect the sub-types of its arguments. This flag instructs SQLite to omit some corner-case optimizations that might disrupt the operation of the [sqlite3_value_subtype()](../c3ref/value_subtype.md) function, causing it to return zero rather than the correct subtype(). All SQL functions that invoke [sqlite3_value_subtype()](../c3ref/value_subtype.md) should have this property. If the SQLITE_SUBTYPE property is omitted, then the return value from [sqlite3_value_subtype()](../c3ref/value_subtype.md) might sometimes be zero even though a non-zero subtype was specified by the function argument expression.

<span id="sqliteresultsubtype"></span>

SQLITE_RESULT_SUBTYPE  
The SQLITE_RESULT_SUBTYPE flag indicates to SQLite that a function might call [sqlite3_result_subtype()](../c3ref/result_subtype.md) to cause a sub-type to be associated with its result. Every function that invokes [sqlite3_result_subtype()](../c3ref/result_subtype.md) should have this property. If it does not, then the call to [sqlite3_result_subtype()](../c3ref/result_subtype.md) might become a no-op if the function is used as a term in an [expression index](../expridx.md). On the other hand, SQL functions that never invoke [sqlite3_result_subtype()](../c3ref/result_subtype.md) should avoid setting this property, as the purpose of this property is to disable certain optimizations that are incompatible with subtypes.

<span id="sqliteselforder1"></span>

SQLITE_SELFORDER1  
The SQLITE_SELFORDER1 flag indicates that the function is an aggregate that internally orders the values provided to the first argument. The ordered-set aggregate SQL notation with a single ORDER BY term can be used to invoke this function. If the ordered-set aggregate notation is used on a function that lacks this flag, then an error is raised. Note that the ordered-set aggregate syntax is only available if SQLite is built using the -DSQLITE_ENABLE_ORDERED_SET_AGGREGATES compile-time option.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
