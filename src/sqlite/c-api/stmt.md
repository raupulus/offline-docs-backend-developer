---
title: Prepared Statement Object
source_url: https://www.sqlite.org/c3ref/stmt.html
source_path: c3ref/stmt.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1890
---

> \
> typedef struct sqlite3_stmt sqlite3_stmt;\

An instance of this object represents a single SQL statement that has been compiled into binary form and is ready to be evaluated.

Think of each SQL statement as a separate computer program. The original SQL text is source code. A prepared statement object is the compiled object code. All SQL must be converted into a prepared statement before it can be run.

The life-cycle of a prepared statement object usually goes like this:

1.  Create the prepared statement object using [sqlite3_prepare_v2()](../c3ref/prepare.md).
2.  Bind values to [parameters](../lang_expr.md#varparam) using the sqlite3_bind\_\*() interfaces.
3.  Run the SQL by calling [sqlite3_step()](../c3ref/step.md) one or more times.
4.  Reset the prepared statement using [sqlite3_reset()](../c3ref/reset.md) then go back to step 2. Do this zero or more times.
5.  Destroy the object using [sqlite3_finalize()](../c3ref/finalize.md).

6 Constructors using this object:

- [sqlite3_prepare](../c3ref/prepare.md)
- [sqlite3_prepare16](../c3ref/prepare.md)
- [sqlite3_prepare16_v2](../c3ref/prepare.md)
- [sqlite3_prepare16_v3](../c3ref/prepare.md)
- [sqlite3_prepare_v2](../c3ref/prepare.md)
- [sqlite3_prepare_v3](../c3ref/prepare.md)

1 Destructor using this object: [sqlite3_finalize()](../c3ref/finalize.md)

53 Methods using this object:

- [sqlite3_bind_blob](../c3ref/bind_blob.md)
- [sqlite3_bind_blob64](../c3ref/bind_blob.md)
- [sqlite3_bind_double](../c3ref/bind_blob.md)
- [sqlite3_bind_int](../c3ref/bind_blob.md)
- [sqlite3_bind_int64](../c3ref/bind_blob.md)
- [sqlite3_bind_null](../c3ref/bind_blob.md)
- [sqlite3_bind_parameter_count](../c3ref/bind_parameter_count.md)
- [sqlite3_bind_parameter_index](../c3ref/bind_parameter_index.md)
- [sqlite3_bind_parameter_name](../c3ref/bind_parameter_name.md)
- [sqlite3_bind_pointer](../c3ref/bind_blob.md)
- [sqlite3_bind_text](../c3ref/bind_blob.md)
- [sqlite3_bind_text16](../c3ref/bind_blob.md)
- [sqlite3_bind_text64](../c3ref/bind_blob.md)
- [sqlite3_bind_value](../c3ref/bind_blob.md)
- [sqlite3_bind_zeroblob](../c3ref/bind_blob.md)
- [sqlite3_bind_zeroblob64](../c3ref/bind_blob.md)
- [sqlite3_clear_bindings](../c3ref/clear_bindings.md)
- [sqlite3_column_blob](../c3ref/column_blob.md)
- [sqlite3_column_bytes](../c3ref/column_blob.md)
- [sqlite3_column_bytes16](../c3ref/column_blob.md)
- [sqlite3_column_count](../c3ref/column_count.md)
- [sqlite3_column_database_name](../c3ref/column_database_name.md)
- [sqlite3_column_database_name16](../c3ref/column_database_name.md)
- [sqlite3_column_decltype](../c3ref/column_decltype.md)
- [sqlite3_column_decltype16](../c3ref/column_decltype.md)
- [sqlite3_column_double](../c3ref/column_blob.md)
- [sqlite3_column_int](../c3ref/column_blob.md)
- [sqlite3_column_int64](../c3ref/column_blob.md)
- [sqlite3_column_name](../c3ref/column_name.md)
- [sqlite3_column_name16](../c3ref/column_name.md)
- [sqlite3_column_origin_name](../c3ref/column_database_name.md)
- [sqlite3_column_origin_name16](../c3ref/column_database_name.md)
- [sqlite3_column_table_name](../c3ref/column_database_name.md)
- [sqlite3_column_table_name16](../c3ref/column_database_name.md)
- [sqlite3_column_text](../c3ref/column_blob.md)
- [sqlite3_column_text16](../c3ref/column_blob.md)
- [sqlite3_column_type](../c3ref/column_blob.md)
- [sqlite3_column_value](../c3ref/column_blob.md)
- [sqlite3_data_count](../c3ref/data_count.md)
- [sqlite3_db_handle](../c3ref/db_handle.md)
- [sqlite3_expanded_sql](../c3ref/expanded_sql.md)
- [sqlite3_normalized_sql](../c3ref/expanded_sql.md)
- [sqlite3_reset](../c3ref/reset.md)
- [sqlite3_sql](../c3ref/expanded_sql.md)
- [sqlite3_step](../c3ref/step.md)
- [sqlite3_stmt_busy](../c3ref/stmt_busy.md)
- [sqlite3_stmt_explain](../c3ref/stmt_explain.md)
- [sqlite3_stmt_isexplain](../c3ref/stmt_isexplain.md)
- [sqlite3_stmt_readonly](../c3ref/stmt_readonly.md)
- [sqlite3_stmt_scanstatus](../c3ref/stmt_scanstatus.md)
- [sqlite3_stmt_scanstatus_reset](../c3ref/stmt_scanstatus_reset.md)
- [sqlite3_stmt_scanstatus_v2](../c3ref/stmt_scanstatus.md)
- [sqlite3_stmt_status](../c3ref/stmt_status.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
