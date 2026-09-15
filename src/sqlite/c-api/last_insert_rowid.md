---
title: Last Insert Rowid
source_url: https://www.sqlite.org/c3ref/last_insert_rowid.html
source_path: c3ref/last_insert_rowid.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1430
---

> \
> sqlite3_int64 sqlite3_last_insert_rowid(sqlite3\*);\

Each entry in most SQLite tables (except for [WITHOUT ROWID](../withoutrowid.md) tables) has a unique 64-bit signed integer key called the ["rowid"](../lang_createtable.md#rowid). The rowid is always available as an undeclared column named ROWID, OID, or \_ROWID\_ as long as those names are not also used by explicitly declared columns. If the table has a column of type [INTEGER PRIMARY KEY](../lang_createtable.md#rowid) then that column is another alias for the rowid.

The sqlite3_last_insert_rowid(D) interface usually returns the [rowid](../lang_createtable.md#rowid) of the most recent successful [INSERT](../lang_insert.md) into a rowid table or [virtual table](../vtab.md) on database connection D. Inserts into [WITHOUT ROWID](../withoutrowid.md) tables are not recorded. If no successful [INSERT](../lang_insert.md)s into rowid tables have ever occurred on the database connection D, then sqlite3_last_insert_rowid(D) returns zero.

As well as being set automatically as rows are inserted into database tables, the value returned by this function may be set explicitly by [sqlite3_set_last_insert_rowid()](../c3ref/set_last_insert_rowid.md)

Some virtual table implementations may INSERT rows into rowid tables as part of committing a transaction (e.g. to flush data accumulated in memory to disk). In this case subsequent calls to this function return the rowid associated with these internal INSERT operations, which leads to unintuitive results. Virtual table implementations that do write to rowid tables in this way can avoid this problem by restoring the original rowid value using [sqlite3_set_last_insert_rowid()](../c3ref/set_last_insert_rowid.md) before returning control to the user.

If an [INSERT](../lang_insert.md) occurs within a trigger then this routine will return the [rowid](../lang_createtable.md#rowid) of the inserted row as long as the trigger is running. Once the trigger program ends, the value returned by this routine reverts to what it was before the trigger was fired.

An [INSERT](../lang_insert.md) that fails due to a constraint violation is not a successful [INSERT](../lang_insert.md) and does not change the value returned by this routine. Thus INSERT OR FAIL, INSERT OR IGNORE, INSERT OR ROLLBACK, and INSERT OR ABORT make no changes to the return value of this routine when their insertion fails. When INSERT OR REPLACE encounters a constraint violation, it does not fail. The INSERT continues to completion after deleting rows that caused the constraint problem so INSERT OR REPLACE will always change the return value of this interface.

For the purposes of this routine, an [INSERT](../lang_insert.md) is considered to be successful even if it is subsequently rolled back.

This function is accessible to SQL statements via the [last_insert_rowid() SQL function](../lang_corefunc.md#last_insert_rowid).

If a separate thread performs a new [INSERT](../lang_insert.md) on the same database connection while the [sqlite3_last_insert_rowid()](../c3ref/last_insert_rowid.md) function is running and thus changes the last insert [rowid](../lang_createtable.md#rowid), then the value returned by [sqlite3_last_insert_rowid()](../c3ref/last_insert_rowid.md) is unpredictable and might not equal either the old or the new last insert [rowid](../lang_createtable.md#rowid).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
