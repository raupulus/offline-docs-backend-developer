---
title: Total Number Of Rows Modified
source_url: https://www.sqlite.org/c3ref/total_changes.html
source_path: c3ref/total_changes.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2100
---

> \
> int sqlite3_total_changes(sqlite3\*);\
> sqlite3_int64 sqlite3_total_changes64(sqlite3\*);\

These functions return the total number of rows inserted, modified or deleted by all [INSERT](../lang_insert.md), [UPDATE](../lang_update.md) or [DELETE](../lang_delete.md) statements completed since the database connection was opened, including those executed as part of trigger programs. The two functions are identical except for the type of the return value and that if the number of rows modified by the connection exceeds the maximum value supported by type "int", then the return value of sqlite3_total_changes() is undefined. Executing any other type of SQL statement does not affect the value returned by sqlite3_total_changes().

Changes made as part of [foreign key actions](../foreignkeys.md#fk_actions) are included in the count, but those made as part of REPLACE constraint resolution are not. Changes to a view that are intercepted by INSTEAD OF triggers are not counted.

The [sqlite3_total_changes(D)](../c3ref/total_changes.md) interface only reports the number of rows that changed due to SQL statement run against database connection D. Any changes by other database connections are ignored. To detect changes against a database file from other database connections use the [PRAGMA data_version](../pragma.md#pragma_data_version) command or the [SQLITE_FCNTL_DATA_VERSION](../c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntldataversion) [file control](../c3ref/file_control.md).

If a separate thread makes changes on the same database connection while [sqlite3_total_changes()](../c3ref/total_changes.md) is running then the value returned is unpredictable and not meaningful.

See also:

- the [sqlite3_changes()](../c3ref/changes.md) interface
- the [count_changes pragma](../pragma.md#pragma_count_changes)
- the [changes() SQL function](../lang_corefunc.md#changes)
- the [data_version pragma](../pragma.md#pragma_data_version)
- the [SQLITE_FCNTL_DATA_VERSION](../c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntldataversion) [file control](../c3ref/file_control.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
