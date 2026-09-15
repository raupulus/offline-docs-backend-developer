---
title: The Carray() Table-Valued Function
source_url: https://www.sqlite.org/carray.html
source_path: carray.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: tools-extensions
order: 2420
---

# 1. Overview

Carray() is a [table-valued function](vtab.md#tabfunc2) with a single column (named "value") and zero or more rows. The "value" of each row in the carray() is taken from a C-language array supplied by the application via [parameter binding](c3ref/bind_blob.md). In this way, the carray() function provides a convenient mechanism to bind C-language arrays to SQL queries.

# 2. Availability

Since SQLite version 3.51.0 (2025-11-04), the carray() extension has been built into [the amalgamation](amalgamation.md), though it is disabled by default and does not function unless SQLite is compiled with [-DSQLITE_ENABLE_CARRAY](compile.md#enable_carray). Prior to version 3.51.0, carray() was in a separate source file that needed to be compiled independently and then added to SQLite as a [loadable extension](loadext.md).

The carray() function was first added to SQLite in version 3.14 (2016-08-08). The sqlite3_carray_bind() interface and the single-argument variant of carray() was added in SQLite version 3.34.0 (2020-12-01). The ability to bind an array of `struct iovec` objects that are interpreted as BLOBs was added in SQLite version 3.41.0 (2023-02-21).

# 3. Details

The carray() function takes one, two, or three arguments. The one-argument variant is recommended. <span id="onearg"></span>

## 3.1. Single-Argument CARRAY

The single-argument form of carray() requires a special C-language interface named "sqlite3_carray_bind()" in order to attach values:

> \
>   int sqlite3_carray_bind(\
>     sqlite3_stmt \*pStmt,         /\* Statement containing the CARRAY \*/\
>     int idx,                     /\* Parameter number for CARRAY argument \*/\
>     void \*aData,                 /\* Data array \*/\
>     int nData,                   /\* Number of entries in the array \*/\
>     int mFlags,                  /\* Datatype flag \*/\
>     void (\*xDestroy)(void\*)      /\* Destructor for aData \*/\
>   );\

The mFlags parameter to sqlite3_carray_bind() must be one of:

> \
>   #define SQLITE_CARRAY_INT32   0\
>   #define SQLITE_CARRAY_INT64   1\
>   #define SQLITE_CARRAY_DOUBLE  2\
>   #define SQLITE_CARRAY_TEXT    3\
>   #define SQLITE_CARRAY_BLOB    4\

The SQLITE_CARRAY_INT32 type means that the array is an array of "int". The SQLITE_CARRAY_INT64 means the array is an array of "[sqlite3_int64](c3ref/int64.md)". The SQLITE_CARRAY_DOUBLE argument means the array is an array of "double". The SQLITE_CARRAY_TEXT means the array is an array of "char\*" where each element of the array is either a NULL pointer or a pointer to a zero-terminated string.

The SQLITE_CARRAY_BLOB argument means that the array is an array of "struct iovec" objects. The 'struct iovec' type is a standard Posix data structure, normally declared using "`#include <sys/uio.h>`". The format is:

> \
> struct iovec {\
>   void  \*iov_base; /\* Starting address \*/\
>   size_t iov_len;  /\* Number of bytes to transfer \*/\
> };\

Higher order bits of the mFlags parameter must all be zero for now, though they may be used in future enhancements.

The xDestroy argument to sqlite3_carray_bind() routine is a pointer to a function that frees the input array. SQLite will invoke this function after it has finished with the data. The xDestroy argument may optionally be one of the following constants defined in "sqlite3.h":

- [SQLITE_STATIC](c3ref/c_static.md) → This means that the application that invokes sqlite3_carray_bind() maintains ownership of the data array and that the application promises SQLite that it will not change or deallocate the data until after the prepared statement is finalized.

- [SQLITE_TRANSIENT](c3ref/c_static.md) → This special value instructs SQLite to make its own private copy of the data before the sqlite3_carray_bind() interface returns.

<span id="twoarg"></span>

## 3.2. Multi-Argument CARRAY

The original carray() design used two or three arguments. This method is still supported for backwards compatibility, however new applications are encouraged to use the single-argument carray() design described above.

For the two- and three-argument versions of carray(), the first argument is a pointer to an array. Since pointer values cannot be specified directly in SQL, the first argument must be a [parameter](lang_expr.md#varparam) that is bound to a pointer value using the [sqlite3_bind_pointer()](c3ref/bind_blob.md) interface using a pointer-type of "carray". The second argument is the number of elements in the array. The optional third argument is a string that determines the datatype of the elements in the C-language array. Allowed values for the third argument are:

1.  'int32'
2.  'int64'
3.  'double'
4.  'char\*'
5.  'struct iovec'

The default datatype is 'int32'. The 'int32' datatype is assumed if the carray() function has only two arguments.

# 4. Usage

The carray() function can be used in the FROM clause of a query. For example, to query two entries from the OBJ table using rowids taken from a C-language array at address \$PTR.

SELECT obj.\* FROM obj, carray(\$PTR) AS x\
 WHERE obj.rowid=x.value;\

This query gives the same result:

SELECT \* FROM obj WHERE rowid IN carray(\$PTR);\
