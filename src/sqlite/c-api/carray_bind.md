---
title: Bind array values to the CARRAY table-valued function
source_url: https://www.sqlite.org/c3ref/carray_bind.html
source_path: c3ref/carray_bind.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 810
---

> \
> int sqlite3_carray_bind_v2(\
>   sqlite3_stmt \*pStmt,        /\* Statement to be bound \*/\
>   int i,                      /\* Parameter index \*/\
>   void \*aData,                /\* Pointer to array data \*/\
>   int nData,                  /\* Number of data elements \*/\
>   int mFlags,                 /\* CARRAY flags \*/\
>   void (\*xDel)(void\*),        /\* Destructor for aData \*/\
>   void \*pDel                  /\* Optional argument to xDel() \*/\
> );\
> int sqlite3_carray_bind(\
>   sqlite3_stmt \*pStmt,        /\* Statement to be bound \*/\
>   int i,                      /\* Parameter index \*/\
>   void \*aData,                /\* Pointer to array data \*/\
>   int nData,                  /\* Number of data elements \*/\
>   int mFlags,                 /\* CARRAY flags \*/\
>   void (\*xDel)(void\*)         /\* Destructor for aData \*/\
> );\

The sqlite3_carray_bind_v2(S,I,P,N,F,X,D) interface binds an array value to parameter that is the first argument of the [carray() table-valued function](../carray.md). The S parameter is a pointer to the [prepared statement](../c3ref/stmt.md) that uses the carray() functions. I is the parameter index to be bound. I must be the index of the parameter that is the first argument to the carray() table-valued function. P is a pointer to the array to be bound, and N is the number of elements in the array. The F argument is one of constants [SQLITE_CARRAY_INT32](../c3ref/c_carray_blob.md), [SQLITE_CARRAY_INT64](../c3ref/c_carray_blob.md), [SQLITE_CARRAY_DOUBLE](../c3ref/c_carray_blob.md), [SQLITE_CARRAY_TEXT](../c3ref/c_carray_blob.md), or [SQLITE_CARRAY_BLOB](../c3ref/c_carray_blob.md) to indicate the datatype of the array P.

If the X argument is not a NULL pointer or one of the special values [SQLITE_STATIC](../c3ref/c_static.md) or [SQLITE_TRANSIENT](../c3ref/c_static.md), then SQLite will invoke the function X with argument D when it is finished using the data in P. The call to X(D) is a destructor for the array P. The destructor X(D) is invoked even if the call to sqlite3_carray_bind_v2() fails. If the X parameter is the special-case value [SQLITE_STATIC](../c3ref/c_static.md), then SQLite assumes that the data static and the destructor is never invoked. If the X parameter is the special-case value [SQLITE_TRANSIENT](../c3ref/c_static.md), then sqlite3_carray_bind_v2() makes its own private copy of the data prior to returning and never invokes the destructor X.

The sqlite3_carray_bind() function works the same as sqlite3_carray_bind_v2() with a D parameter set to P. In other words, sqlite3_carray_bind(S,I,P,N,F,X) is same as sqlite3_carray_bind_v2(S,I,P,N,F,X,P).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
