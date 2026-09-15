---
title: Datatypes for the CARRAY table-valued function
source_url: https://www.sqlite.org/c3ref/c_carray_blob.html
source_path: c3ref/c_carray_blob.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 460
---

> \
> \#define SQLITE_CARRAY_INT32     0    /\* Data is 32-bit signed integers \*/\
> \#define SQLITE_CARRAY_INT64     1    /\* Data is 64-bit signed integers \*/\
> \#define SQLITE_CARRAY_DOUBLE    2    /\* Data is doubles \*/\
> \#define SQLITE_CARRAY_TEXT      3    /\* Data is char\* \*/\
> \#define SQLITE_CARRAY_BLOB      4    /\* Data is struct iovec \*/\

The fifth argument to the [sqlite3_carray_bind()](../c3ref/carray_bind.md) interface musts be one of the following constants, to specify the datatype of the array that is being bound into the [carray table-valued function](../carray.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
