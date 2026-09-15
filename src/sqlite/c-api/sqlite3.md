---
title: Database Connection Handle
source_url: https://www.sqlite.org/c3ref/sqlite3.html
source_path: c3ref/sqlite3.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1860
---

> \
> typedef struct sqlite3 sqlite3;\

Each open SQLite database is represented by a pointer to an instance of the opaque structure named "sqlite3". It is useful to think of an sqlite3 pointer as an object. The [sqlite3_open()](../c3ref/open.md), [sqlite3_open16()](../c3ref/open.md), and [sqlite3_open_v2()](../c3ref/open.md) interfaces are its constructors, and [sqlite3_close()](../c3ref/close.md) and [sqlite3_close_v2()](../c3ref/close.md) are its destructors. There are many other interfaces (such as [sqlite3_prepare_v2()](../c3ref/prepare.md), [sqlite3_create_function()](../c3ref/create_function.md), and [sqlite3_busy_timeout()](../c3ref/busy_timeout.md) to name but three) that are methods on an sqlite3 object.

3 Constructors using this object: [sqlite3_open()](../c3ref/open.md), [sqlite3_open16()](../c3ref/open.md), [sqlite3_open_v2()](../c3ref/open.md)

2 Destructors using this object: [sqlite3_close()](../c3ref/close.md), [sqlite3_close_v2()](../c3ref/close.md)

80 Methods using this object:

- [sqlite3_autovacuum_pages](../c3ref/autovacuum_pages.md)
- [sqlite3_blob_open](../c3ref/blob_open.md)
- [sqlite3_busy_handler](../c3ref/busy_handler.md)
- [sqlite3_busy_timeout](../c3ref/busy_timeout.md)
- [sqlite3_changes](../c3ref/changes.md)
- [sqlite3_changes64](../c3ref/changes.md)
- [sqlite3_collation_needed](../c3ref/collation_needed.md)
- [sqlite3_collation_needed16](../c3ref/collation_needed.md)
- [sqlite3_commit_hook](../c3ref/commit_hook.md)
- [sqlite3_create_collation](../c3ref/create_collation.md)
- [sqlite3_create_collation16](../c3ref/create_collation.md)
- [sqlite3_create_collation_v2](../c3ref/create_collation.md)
- [sqlite3_create_function](../c3ref/create_function.md)
- [sqlite3_create_function16](../c3ref/create_function.md)
- [sqlite3_create_function_v2](../c3ref/create_function.md)
- [sqlite3_create_module](../c3ref/create_module.md)
- [sqlite3_create_module_v2](../c3ref/create_module.md)
- [sqlite3_create_window_function](../c3ref/create_function.md)
- [sqlite3_db_cacheflush](../c3ref/db_cacheflush.md)
- [sqlite3_db_config](../c3ref/db_config.md)
- [sqlite3_db_filename](../c3ref/db_filename.md)
- [sqlite3_db_mutex](../c3ref/db_mutex.md)
- [sqlite3_db_name](../c3ref/db_name.md)
- [sqlite3_db_readonly](../c3ref/db_readonly.md)
- [sqlite3_db_release_memory](../c3ref/db_release_memory.md)
- [sqlite3_db_status](../c3ref/db_status.md)
- [sqlite3_db_status64](../c3ref/db_status.md)
- [sqlite3_drop_modules](../c3ref/drop_modules.md)
- [sqlite3_enable_load_extension](../c3ref/enable_load_extension.md)
- [sqlite3_errcode](../c3ref/errcode.md)
- [sqlite3_errmsg](../c3ref/errcode.md)
- [sqlite3_errmsg16](../c3ref/errcode.md)
- [sqlite3_error_offset](../c3ref/errcode.md)
- [sqlite3_errstr](../c3ref/errcode.md)
- [sqlite3_exec](../c3ref/exec.md)
- [sqlite3_extended_errcode](../c3ref/errcode.md)
- [sqlite3_extended_result_codes](../c3ref/extended_result_codes.md)
- [sqlite3_file_control](../c3ref/file_control.md)
- [sqlite3_free_table](../c3ref/free_table.md)
- [sqlite3_get_autocommit](../c3ref/get_autocommit.md)
- [sqlite3_get_clientdata](../c3ref/get_clientdata.md)
- [sqlite3_get_table](../c3ref/free_table.md)
- [sqlite3_interrupt](../c3ref/interrupt.md)
- [sqlite3_is_interrupted](../c3ref/interrupt.md)
- [sqlite3_last_insert_rowid](../c3ref/last_insert_rowid.md)
- [sqlite3_limit](../c3ref/limit.md)
- [sqlite3_load_extension](../c3ref/load_extension.md)
- [sqlite3_next_stmt](../c3ref/next_stmt.md)
- [sqlite3_overload_function](../c3ref/overload_function.md)
- [sqlite3_prepare](../c3ref/prepare.md)
- [sqlite3_prepare16](../c3ref/prepare.md)
- [sqlite3_prepare16_v2](../c3ref/prepare.md)
- [sqlite3_prepare16_v3](../c3ref/prepare.md)
- [sqlite3_prepare_v2](../c3ref/prepare.md)
- [sqlite3_prepare_v3](../c3ref/prepare.md)
- [sqlite3_preupdate_blobwrite](../c3ref/preupdate_blobwrite.md)
- [sqlite3_preupdate_count](../c3ref/preupdate_blobwrite.md)
- [sqlite3_preupdate_depth](../c3ref/preupdate_blobwrite.md)
- [sqlite3_preupdate_hook](../c3ref/preupdate_blobwrite.md)
- [sqlite3_preupdate_new](../c3ref/preupdate_blobwrite.md)
- [sqlite3_preupdate_old](../c3ref/preupdate_blobwrite.md)
- [sqlite3_progress_handler](../c3ref/progress_handler.md)
- [sqlite3_rollback_hook](../c3ref/commit_hook.md)
- [sqlite3_set_authorizer](../c3ref/set_authorizer.md)
- [sqlite3_set_clientdata](../c3ref/get_clientdata.md)
- [sqlite3_set_errmsg](../c3ref/set_errmsg.md)
- [sqlite3_set_last_insert_rowid](../c3ref/set_last_insert_rowid.md)
- [sqlite3_setlk_timeout](../c3ref/setlk_timeout.md)
- [sqlite3_system_errno](../c3ref/system_errno.md)
- [sqlite3_table_column_metadata](../c3ref/table_column_metadata.md)
- [sqlite3_total_changes](../c3ref/total_changes.md)
- [sqlite3_total_changes64](../c3ref/total_changes.md)
- [sqlite3_trace_v2](../c3ref/trace_v2.md)
- [sqlite3_txn_state](../c3ref/txn_state.md)
- [sqlite3_unlock_notify](../c3ref/unlock_notify.md)
- [sqlite3_update_hook](../c3ref/update_hook.md)
- [sqlite3_wal_autocheckpoint](../c3ref/wal_autocheckpoint.md)
- [sqlite3_wal_checkpoint](../c3ref/wal_checkpoint.md)
- [sqlite3_wal_checkpoint_v2](../c3ref/wal_checkpoint_v2.md)
- [sqlite3_wal_hook](../c3ref/wal_hook.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
