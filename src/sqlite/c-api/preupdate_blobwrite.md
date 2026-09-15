---
title: The pre-update hook.
source_url: https://www.sqlite.org/c3ref/preupdate_blobwrite.html
source_path: c3ref/preupdate_blobwrite.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1640
---

> \
> \#if defined(SQLITE_ENABLE_PREUPDATE_HOOK)\
> void \*sqlite3_preupdate_hook(\
>   sqlite3 \*db,\
>   void(\*xPreUpdate)(\
>     void \*pCtx,                   /\* Copy of third arg to preupdate_hook() \*/\
>     sqlite3 \*db,                  /\* Database handle \*/\
>     int op,                       /\* SQLITE_UPDATE, DELETE or INSERT \*/\
>     char const \*zDb,              /\* Database name \*/\
>     char const \*zName,            /\* Table name \*/\
>     sqlite3_int64 iKey1,          /\* Rowid of row about to be deleted/updated \*/\
>     sqlite3_int64 iKey2           /\* New rowid value (for a rowid UPDATE) \*/\
>   ),\
>   void\*\
> );\
> int sqlite3_preupdate_old(sqlite3 \*, int, sqlite3_value \*\*);\
> int sqlite3_preupdate_count(sqlite3 \*);\
> int sqlite3_preupdate_depth(sqlite3 \*);\
> int sqlite3_preupdate_new(sqlite3 \*, int, sqlite3_value \*\*);\
> int sqlite3_preupdate_blobwrite(sqlite3 \*);\
> \#endif\

These interfaces are only available if SQLite is compiled using the [SQLITE_ENABLE_PREUPDATE_HOOK](../compile.md#enable_preupdate_hook) compile-time option.

The [sqlite3_preupdate_hook()](../c3ref/preupdate_blobwrite.md) interface registers a callback function that is invoked prior to each [INSERT](../lang_insert.md), [UPDATE](../lang_update.md), and [DELETE](../lang_delete.md) operation on a database table. At most one preupdate hook may be registered at a time on a single [database connection](../c3ref/sqlite3.md); each call to [sqlite3_preupdate_hook()](../c3ref/preupdate_blobwrite.md) overrides the previous setting. The preupdate hook is disabled by invoking [sqlite3_preupdate_hook()](../c3ref/preupdate_blobwrite.md) with a NULL pointer as the second parameter. The third parameter to [sqlite3_preupdate_hook()](../c3ref/preupdate_blobwrite.md) is passed through as the first parameter to callbacks.

The preupdate hook only fires for changes to real database tables; the preupdate hook is not invoked for changes to [virtual tables](../vtab.md) or to system tables like sqlite_sequence or sqlite_stat1.

The second parameter to the preupdate callback is a pointer to the [database connection](../c3ref/sqlite3.md) that registered the preupdate hook. The third parameter to the preupdate callback is one of the constants [SQLITE_INSERT](../c3ref/c_alter_table.md), [SQLITE_DELETE](../c3ref/c_alter_table.md), or [SQLITE_UPDATE](../c3ref/c_alter_table.md) to identify the kind of update operation that is about to occur. The fourth parameter to the preupdate callback is the name of the database within the database connection that is being modified. This will be "main" for the main database or "temp" for TEMP tables or the name given after the AS keyword in the [ATTACH](../lang_attach.md) statement for attached databases. The fifth parameter to the preupdate callback is the name of the table that is being modified.

For an UPDATE or DELETE operation on a [rowid table](../rowidtable.md), the sixth parameter passed to the preupdate callback is the initial [rowid](../lang_createtable.md#rowid) of the row being modified or deleted. For an INSERT operation on a rowid table, or any operation on a WITHOUT ROWID table, the value of the sixth parameter is undefined. For an INSERT or UPDATE on a rowid table the seventh parameter is the final rowid value of the row being inserted or updated. The value of the seventh parameter passed to the callback function is not defined for operations on WITHOUT ROWID tables, or for DELETE operations on rowid tables.

The sqlite3_preupdate_hook(D,C,P) function returns the P argument from the previous call on the same [database connection](../c3ref/sqlite3.md) D, or NULL for the first call on D.

The [sqlite3_preupdate_old()](../c3ref/preupdate_blobwrite.md), [sqlite3_preupdate_new()](../c3ref/preupdate_blobwrite.md), [sqlite3_preupdate_count()](../c3ref/preupdate_blobwrite.md), and [sqlite3_preupdate_depth()](../c3ref/preupdate_blobwrite.md) interfaces provide additional information about a preupdate event. These routines may only be called from within a preupdate callback. Invoking any of these routines from outside of a preupdate callback or with a [database connection](../c3ref/sqlite3.md) pointer that is different from the one supplied to the preupdate callback results in undefined and probably undesirable behavior.

The [sqlite3_preupdate_count(D)](../c3ref/preupdate_blobwrite.md) interface returns the number of columns in the row that is being inserted, updated, or deleted.

The [sqlite3_preupdate_old(D,N,P)](../c3ref/preupdate_blobwrite.md) interface writes into P a pointer to a [protected sqlite3_value](../c3ref/value.md) that contains the value of the Nth column of the table row before it is updated. The N parameter must be between 0 and one less than the number of columns or the behavior will be undefined. This must only be used within SQLITE_UPDATE and SQLITE_DELETE preupdate callbacks; if it is used by an SQLITE_INSERT callback then the behavior is undefined. The [sqlite3_value](../c3ref/value.md) that P points to will be destroyed when the preupdate callback returns.

The [sqlite3_preupdate_new(D,N,P)](../c3ref/preupdate_blobwrite.md) interface writes into P a pointer to a [protected sqlite3_value](../c3ref/value.md) that contains the value of the Nth column of the table row after it is updated. The N parameter must be between 0 and one less than the number of columns or the behavior will be undefined. This must only be used within SQLITE_INSERT and SQLITE_UPDATE preupdate callbacks; if it is used by an SQLITE_DELETE callback then the behavior is undefined. The [sqlite3_value](../c3ref/value.md) that P points to will be destroyed when the preupdate callback returns.

The [sqlite3_preupdate_depth(D)](../c3ref/preupdate_blobwrite.md) interface returns 0 if the preupdate callback was invoked as a result of a direct insert, update, or delete operation; or 1 for inserts, updates, or deletes invoked by top-level triggers; or 2 for changes resulting from triggers called by top-level triggers; and so forth.

When the [sqlite3_blob_write()](../c3ref/blob_write.md) API is used to update a blob column, the pre-update hook is invoked with SQLITE_DELETE, because the new values are not yet available. In this case, when a callback made with op==SQLITE_DELETE is actually a write using the sqlite3_blob_write() API, the [sqlite3_preupdate_blobwrite()](../c3ref/preupdate_blobwrite.md) returns the index of the column being written. In other cases, where the pre-update hook is being invoked for some other reason, including a regular DELETE, sqlite3_preupdate_blobwrite() returns -1.

See also: [sqlite3_update_hook()](../c3ref/update_hook.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
