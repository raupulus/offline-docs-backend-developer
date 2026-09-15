---
title: Application-Defined SQL Functions
source_url: https://www.sqlite.org/appfunc.html
source_path: appfunc.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 90
---

# 1. Executive Summary

Applications that use SQLite can define custom SQL functions that call back into application code to compute their results. The custom SQL function implementations can be embedded in the application code itself, or can be [loadable extensions](loadext.md).

Application-defined or custom SQL functions are created using the [sqlite3_create_function()](c3ref/create_function.md) family of interfaces. Custom SQL functions can be scalar functions, aggregate functions, or [window functions](windowfunctions.md). Custom SQL functions can have any number of arguments from 0 up to [SQLITE_MAX_FUNCTION_ARG](limits.md#max_function_arg). The [sqlite3_create_function()](c3ref/create_function.md) interface specifies callbacks that are invoked to carry out the processing for the new SQL function.

SQLite also supports custom [table-valued functions](vtab.md#tabfunc2), but they are implemented by a different mechanism that is not covered in this document.

# 2. Defining New SQL Functions

The [sqlite3_create_function()](c3ref/create_function.md) family of interfaces is used to create new custom SQL functions. Each member of this family is a wrapper around a common core. All family members accomplish the same thing; they merely have different calling signatures.

- **[sqlite3_create_function()](c3ref/create_function.md)** → The original version of sqlite3_create_function() allows the application to create a single new SQL function that can be either a scalar or an aggregate. The name of the function is specified using UTF8.

- **[sqlite3_create_function16()](c3ref/create_function.md)** → This variant works exactly like the sqlite3_create_function() original except that the name of the function itself is specified as a UTF16 string rather than as a UTF8 string.

- **[sqlite3_create_function_v2()](c3ref/create_function.md)** → This variant works like the original sqlite3_create_function() except that it includes an additional parameter that is a pointer to a destructor for the [sqlite3_user_data()](c3ref/user_data.md) pointer that is passed in as the 5th argument to all of the sqlite3_create_function() variants. That destructor function (if it is non-NULL) is called when the custom function is deleted - usually when the database connection is closing.

- **[sqlite3_create_window_function()](c3ref/create_function.md)** → This variant works like the original sqlite3_create_function() except that it accepts a different set of callback pointers - the callback pointers used by [window function](windowfunctions.md) definitions.

## 2.1. Common Parameters

Many of the parameters passed to the [sqlite3_create_function()](c3ref/create_function.md) family of interfaces are common across the entire family.

1.  **db** → The 1st parameter is always a pointer to the [database connection](c3ref/sqlite3.md) on which the custom SQL function will work. Custom SQL functions are created separately for each database connection. There is no short-hand mechanism for creating SQL functions that work across all database connections.

2.  **zFunctionName** → The 2nd parameter is the name of the SQL function that is being created. The name is usually in UTF8, except that the name should be in UTF16 in the native byte order for [sqlite3_create_function16()](c3ref/create_function.md).

    The maximum length of a SQL function name is 255 bytes of UTF8. Any attempt to create a function with a longer name will result in an [SQLITE_MISUSE](rescode.md#misuse) error.

    The SQL function creation interfaces may be called multiple times with the same function name. If two calls have the same function number but a different number of arguments, for example, then two variants of the SQL function will be registered, each taking a different number of arguments.

3.  **nArg** → The 3rd parameter is always the number of arguments that the function accepts. The value must be an integer between -1 and [SQLITE_MAX_FUNCTION_ARG](limits.md#max_function_arg) (default value: 127). A value of -1 means that the SQL function is a variadic function that can take any number of arguments between 0 and [SQLITE_MAX_FUNCTION_ARG](limits.md#max_function_arg).

4.  **eTextRep** → The 4th parameter is a 32-bit integer flag whose bits convey various properties about the new function. The original purpose of this parameter was to specify the preferred text encoding for the function, using one of the following constants:

    - [SQLITE_UTF8](c3ref/c_any.md#sqliteutf8)
    - [SQLITE_UTF16BE](c3ref/c_any.md#sqliteutf16be)
    - [SQLITE_UTF16LE](c3ref/c_any.md#sqliteutf16le)

    All custom SQL functions will accept text in any encoding. Encoding conversions will happen automatically. The preferred encoding merely specifies the encoding for which the function implementation is optimized. It is possible to specify multiple functions with the same name and the same number of arguments, but different preferred encodings and different callbacks used to implement the function, and SQLite will choose the set of callbacks for which the input encodings most closely match the preferred encoding.

    The preferred text encoding flag may be OR-ed together with zero or more of the following property flags:

    - [SQLITE_DETERMINISTIC](c3ref/c_deterministic.md#sqlitedeterministic)
    - [SQLITE_DIRECTONLY](c3ref/c_deterministic.md#sqlitedirectonly)
    - [SQLITE_INNOCUOUS](c3ref/c_deterministic.md#sqliteinnocuous)
    - [SQLITE_SUBTYPE](c3ref/c_deterministic.md#sqlitesubtype)

    Additional function property flags bits may be added in future versions of SQLite.

5.  **pApp** → The 5th parameter is an arbitrary pointer that is passed through into the callback routines. SQLite itself does nothing with this pointer, except to make it available to the callbacks, and to pass it into the destructor when the function is unregistered.

## 2.2. Multiple Calls To sqlite3_create_function() For The Same Function

It is common for an application to invoke sqlite3_create_function() multiple times for the same SQL function. For example, if an SQL function can take either 2 or 3 arguments, then sqlite3_create_function() would be invoked once for the 2-argument version and a second time for the 3-argument version. The underlying implementation (the callbacks) can be different for both variants.

An application can also register multiple SQL functions with the same name and same number of arguments, but a different preferred text encoding. In that case, SQLite will invoke the function using the callbacks for the version whose preferred text encoding most closely matches the database text encoding. In this way, multiple implementations of the same function can be provided that are optimized for UTF8 or UTF16.

If multiple calls to sqlite3_create_function() specify the same function name, and the same number of arguments, and the same preferred text encoding, then the callbacks and other parameters of the second call overwrite the first, and the destructor callback from the first call (if it exists) is invoked.

## 2.3. Callbacks

SQLite evaluates an SQL function by invoking callback routines.

### 2.3.1. The Scalar Function Callback

Scalar SQL functions are implemented by a single callback in the **xFunc** parameter to sqlite3_create_function(). The following code demonstrates the implementation of a "noop(X)" scalar SQL function that merely returns its argument:

static void noopfunc(\
  sqlite3_context \*context,\
  int argc,\
  sqlite3_value \*\*argv\
){\
  assert( argc==1 );\
  sqlite3_result_value(context, argv\[0\]);\
}\

The 1st parameter, **context**, is a pointer to an opaque object that describes the content from which the SQL function was invoked. This context pointer becomes the first parameter to many other routines that the function implementation might want to invoke, including:

- [sqlite3_aggregate_context](c3ref/aggregate_context.md)
- [sqlite3_context_db_handle](c3ref/context_db_handle.md)
- [sqlite3_get_auxdata](c3ref/get_auxdata.md)
- [sqlite3_result_blob](c3ref/result_blob.md)
- [sqlite3_result_blob64](c3ref/result_blob.md)
- [sqlite3_result_double](c3ref/result_blob.md)
- [sqlite3_result_error](c3ref/result_blob.md)
- [sqlite3_result_error16](c3ref/result_blob.md)
- [sqlite3_result_error_code](c3ref/result_blob.md)
- [sqlite3_result_error_nomem](c3ref/result_blob.md)
- [sqlite3_result_error_toobig](c3ref/result_blob.md)
- [sqlite3_result_int](c3ref/result_blob.md)
- [sqlite3_result_int64](c3ref/result_blob.md)
- [sqlite3_result_null](c3ref/result_blob.md)
- [sqlite3_result_pointer](c3ref/result_blob.md)
- [sqlite3_result_subtype](c3ref/result_subtype.md)
- [sqlite3_result_text](c3ref/result_blob.md)
- [sqlite3_result_text16](c3ref/result_blob.md)
- [sqlite3_result_text16be](c3ref/result_blob.md)
- [sqlite3_result_text16le](c3ref/result_blob.md)
- [sqlite3_result_text64](c3ref/result_blob.md)
- [sqlite3_result_value](c3ref/result_blob.md)
- [sqlite3_result_zeroblob](c3ref/result_blob.md)
- [sqlite3_result_zeroblob64](c3ref/result_blob.md)
- [sqlite3_set_auxdata](c3ref/get_auxdata.md)
- [sqlite3_user_data](c3ref/user_data.md)

The [sqlite3_result() family of functions](c3ref/result_blob.md) are used to specify the result of the scalar SQL function. One or more of these should be invoked by the callback to set the function return value. If none of these routines are invoked for a specific callback, then the return value will be NULL.

The [sqlite3_user_data()](c3ref/user_data.md) routine returns a copy of the **pArg** pointer that was given to [sqlite3_create_function()](c3ref/create_function.md) when the SQL function was created.

The [sqlite3_context_db_handle()](c3ref/context_db_handle.md) routine returns a pointer to the [database connection](c3ref/sqlite3.md) object.

The [sqlite3_aggregate_context()](c3ref/aggregate_context.md) routine is used only in the implementations of aggregate and window functions. Scalar functions may not use [sqlite3_aggregate_context()](c3ref/aggregate_context.md). The [sqlite3_aggregate_context()](c3ref/aggregate_context.md) function is included in the interface list only for completeness.

The 2nd and 3rd arguments to the scalar SQL function implementation, **argc** and **argv**, are the number of arguments to the SQL function itself and the values for each argument of the SQL function. Argument values can be of any datatype and are thus stored in instances of the [sqlite3_value](c3ref/value.md) object. Specific C-language values can be extracted from this object using the [sqlite3_value() family of interfaces](c3ref/value_blob.md).

### 2.3.2. The Aggregate Function Callbacks

Aggregate SQL functions are implemented by using two callback functions, **xStep** and **xFinal**. The xStep() function is called for each row of the aggregate and the xFinal() function is invoked to compute the final answer at the end. The following (slightly simplified) version of the built-in count() function illustrates:

typedef struct CountCtx CountCtx;\
struct CountCtx {\
  i64 n;\
};\
static void countStep(sqlite3_context \*context, int argc, sqlite3_value \*\*argv){\
  CountCtx \*p;\
  p = sqlite3_aggregate_context(context, sizeof(\*p));\
  if( (argc==0 \|\| SQLITE_NULL!=sqlite3_value_type(argv\[0\])) && p ){\
    p-\>n++;\
  }\
}   \
static void countFinalize(sqlite3_context \*context){\
  CountCtx \*p;\
  p = sqlite3_aggregate_context(context, 0);\
  sqlite3_result_int64(context, p ? p-\>n : 0);\
}\

Recall that there are two versions of the count() aggregate. With zero arguments, count() returns a count of the number of rows. With one argument, count() returns the number of times that the argument was non-NULL.

The countStep() callback is invoked once for each row in the aggregate. As you can see, the count is incremented if either there are no arguments, or if the one argument is not NULL.

The step function for an aggregate should always begin with a call to the [sqlite3_aggregate_context()](c3ref/aggregate_context.md) routine to fetch the persistent state of the aggregate function. On the first invocation of the step() function, the aggregate context is initialized to a block of memory that is N bytes in size, where N is the second parameter to sqlite3_aggregate_context() and that memory is zeroed. On all subsequent calls to the step() function, the same block of memory is returned. Except, sqlite3_aggregate_context() might return NULL in the case of an out-of-memory error, so aggregate functions should be prepared to deal with that case.

After all rows are processed the countFinalize() routine is called exactly once. This routine computes the final result and invokes one of the [sqlite3_result()](c3ref/result_blob.md) family of functions to set the final result. The aggregate context will be freed automatically by SQLite, though the xFinalize() routine must clean up any substructure associated with the aggregate context before it returns. If the xStep() method is called one or more times, then SQLite guarantees that the xFinal() method will be called at once, even if the query aborts.

### 2.3.3. The Window Function Callbacks

[Window functions](windowfunctions.md) use the same xStep() and xFinal() callbacks that aggregate functions use, plus two others: **xValue** and **xInverse**. See the documentation on [application-defined window functions](windowfunctions.md#udfwinfunc) for further details.

### 2.3.4. Examples

There are dozens and dozens of SQL function implementations scattered throughout the SQLite source code that can be used as example applications. The built-in SQL functions use the same interface as application-defined SQL functions, so built-in functions can be used as examples too. Search for "sqlite3_context" in the SQLite source code to find examples. <span id="sec"></span>

# 3. Security Implications

Application-defined SQL functions can become security vulnerabilities if not carefully managed. Suppose, for example, an application defines a new "system(X)" SQL function that runs its argument X as a command and returns the integer result code. Perhaps the implementation is like this:

static void systemFunc(\
  sqlite3_context \*context,\
  int argc,\
  sqlite3_value \*\*argv\
){\
  const char \*zCmd = (const char\*)sqlite3_value_text(argv\[0\]);\
  if( zCmd!=0 ){\
    int rc = system(zCmd);\
    sqlite3_result_int(context, rc);\
  }\
}\

This is a function with powerful side-effects. Most programmers would be naturally cautious about using it, but probably would not see the harm in merely having it available. But there is great risk in merely defining such a function, even if the application itself never invokes it!

Suppose the application normally does a query against table TAB1 when it starts up. If an attacker can gain access to the database file and modify the schema like this:

ALTER TABLE tab1 RENAME TO tab1_real;\
CREATE VIEW tab1 AS\
   SELECT \* FROM tab1_real\
    WHERE system('rm -rf \*') IS NOT NULL;\

Then, when the application attempts to open the database, register the system() function, then run an innocent query against the "tab1" table, it instead deletes all the files in its working directory. Yikes!

To prevent this kind of mischief, applications that create their own custom SQL functions should take one or more of the following safety precautions. The more precautions taken the better:

1.  Invoke [sqlite3_db_config](c3ref/db_config.md)(db,[SQLITE_DBCONFIG_TRUSTED_SCHEMA](c3ref/c_dbconfig_defensive.md#sqlitedbconfigtrustedschema),0,0) on each [database connection](c3ref/sqlite3.md) as soon as it is opened. This prevents application-defined functions from being used in places where an attacker might be able to surreptiously invoke them by modifying a database schema:

    - In VIEWs.
    - In TRIGGERs.
    - In CHECK constraints of a table definition.
    - In DEFAULT constraints of a table definition.
    - In the definitions of generated columns.
    - In the expression part of an index on an expression.
    - In the WHERE clause of a partial index.

    To put it another way, this setting requires that application-defined functions only be run directly by top-level SQL invoked from the application itself, not as a consequence of doing some other innocent-looking query.

2.  Use the [PRAGMA trusted_schema=OFF](pragma.md#pragma_trusted_schema) SQL statement to disable trusted schema. This has the same effect as the previous bullet, but does not require the use of C-code and hence can be performed in programs written in another programming language and that do not have access to SQLite C-language APIs.

3.  Compile SQLite using the [-DSQLITE_TRUSTED_SCHEMA=0](compile.md#trusted_schema) compile-time option. This makes SQLite distrust application-defined functions inside of the schema by default.

4.  If any application-defined SQL functions have potentially dangerous side-effects, or if they could potentially leak sensitive information to an attacker if misused, then tag those functions using the [SQLITE_DIRECTONLY](c3ref/c_deterministic.md#sqlitedirectonly) option on the "enc" parameter. This means that the function can never be run from schema-code even if the trusted-schema option is on.

5.  Never tag an application-defined SQL function with [SQLITE_INNOCUOUS](c3ref/c_deterministic.md#sqliteinnocuous) unless you really need to and you have checked the implementation closely and are certain that it can do no harm even if it falls under the control of an attacker.
