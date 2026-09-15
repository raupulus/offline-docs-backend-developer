---
title: Data Change Notification Callbacks
source_url: https://www.sqlite.org/c3ref/update_hook.html
source_path: c3ref/update_hook.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2140
---

> \
> void \*sqlite3_update_hook(\
>   sqlite3\*,\
>   void(\*)(void \*,int ,char const \*,char const \*,sqlite3_int64),\
>   void\*\
> );\

The sqlite3_update_hook() interface registers a callback function with the [database connection](../c3ref/sqlite3.md) identified by the first argument to be invoked whenever a row is updated, inserted or deleted in a [rowid table](../rowidtable.md). Any callback set by a previous call to this function for the same database connection is overridden.

The second argument is a pointer to the function to invoke when a row is updated, inserted or deleted in a rowid table. The update hook is disabled by invoking sqlite3_update_hook() with a NULL pointer as the second parameter. The first argument to the callback is a copy of the third argument to sqlite3_update_hook(). The second callback argument is one of [SQLITE_INSERT](../c3ref/c_alter_table.md), [SQLITE_DELETE](../c3ref/c_alter_table.md), or [SQLITE_UPDATE](../c3ref/c_alter_table.md), depending on the operation that caused the callback to be invoked. The third and fourth arguments to the callback contain pointers to the database and table name containing the affected row. The final callback parameter is the [rowid](../lang_createtable.md#rowid) of the row. In the case of an update, this is the [rowid](../lang_createtable.md#rowid) after the update takes place.

The update hook is not invoked when internal system tables are modified (i.e. sqlite_sequence). The update hook is not invoked when [WITHOUT ROWID](../withoutrowid.md) tables are modified.

In the current implementation, the update hook is not invoked when conflicting rows are deleted because of an [ON CONFLICT REPLACE](../lang_conflict.md) clause. Nor is the update hook invoked when rows are deleted using the [truncate optimization](../lang_delete.md#truncateopt). The exceptions defined in this paragraph might change in a future release of SQLite.

Whether the update hook is invoked before or after the corresponding change is currently unspecified and may differ depending on the type of change. Do not rely on the order of the hook call with regards to the final result of the operation which triggers the hook.

The update hook implementation must not do anything that will modify the database connection that invoked the update hook. Any actions to modify the database connection must be deferred until after the completion of the [sqlite3_step()](../c3ref/step.md) call that triggered the update hook. Note that [sqlite3_prepare_v2()](../c3ref/prepare.md) and [sqlite3_step()](../c3ref/step.md) both modify their database connections for the meaning of "modify" in this paragraph.

The sqlite3_update_hook(D,C,P) function returns the P argument from the previous call on the same [database connection](../c3ref/sqlite3.md) D, or NULL for the first call on D.

See also the [sqlite3_commit_hook()](../c3ref/commit_hook.md), [sqlite3_rollback_hook()](../c3ref/commit_hook.md), and [sqlite3_preupdate_hook()](../c3ref/preupdate_blobwrite.md) interfaces.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
