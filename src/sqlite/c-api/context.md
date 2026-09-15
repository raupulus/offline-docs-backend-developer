---
title: SQL Function Context Object
source_url: https://www.sqlite.org/c3ref/context.html
source_path: c3ref/context.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 960
---

> \
> typedef struct sqlite3_context sqlite3_context;\

The context in which an SQL function executes is stored in an sqlite3_context object. A pointer to an sqlite3_context object is always the first parameter to [application-defined SQL functions](../appfunc.md). The application-defined SQL function implementation will pass this pointer through into calls to [sqlite3_result()](../c3ref/result_blob.md), [sqlite3_aggregate_context()](../c3ref/aggregate_context.md), [sqlite3_user_data()](../c3ref/user_data.md), [sqlite3_context_db_handle()](../c3ref/context_db_handle.md), [sqlite3_get_auxdata()](../c3ref/get_auxdata.md), and/or [sqlite3_set_auxdata()](../c3ref/get_auxdata.md).

26 Methods using this object:

- [sqlite3_aggregate_context](../c3ref/aggregate_context.md)
- [sqlite3_context_db_handle](../c3ref/context_db_handle.md)
- [sqlite3_get_auxdata](../c3ref/get_auxdata.md)
- [sqlite3_result_blob](../c3ref/result_blob.md)
- [sqlite3_result_blob64](../c3ref/result_blob.md)
- [sqlite3_result_double](../c3ref/result_blob.md)
- [sqlite3_result_error](../c3ref/result_blob.md)
- [sqlite3_result_error16](../c3ref/result_blob.md)
- [sqlite3_result_error_code](../c3ref/result_blob.md)
- [sqlite3_result_error_nomem](../c3ref/result_blob.md)
- [sqlite3_result_error_toobig](../c3ref/result_blob.md)
- [sqlite3_result_int](../c3ref/result_blob.md)
- [sqlite3_result_int64](../c3ref/result_blob.md)
- [sqlite3_result_null](../c3ref/result_blob.md)
- [sqlite3_result_pointer](../c3ref/result_blob.md)
- [sqlite3_result_subtype](../c3ref/result_subtype.md)
- [sqlite3_result_text](../c3ref/result_blob.md)
- [sqlite3_result_text16](../c3ref/result_blob.md)
- [sqlite3_result_text16be](../c3ref/result_blob.md)
- [sqlite3_result_text16le](../c3ref/result_blob.md)
- [sqlite3_result_text64](../c3ref/result_blob.md)
- [sqlite3_result_value](../c3ref/result_blob.md)
- [sqlite3_result_zeroblob](../c3ref/result_blob.md)
- [sqlite3_result_zeroblob64](../c3ref/result_blob.md)
- [sqlite3_set_auxdata](../c3ref/get_auxdata.md)
- [sqlite3_user_data](../c3ref/user_data.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
