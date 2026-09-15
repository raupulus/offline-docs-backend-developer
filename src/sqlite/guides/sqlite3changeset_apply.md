---
title: Apply A Changeset To A Database
source_url: https://www.sqlite.org/session/sqlite3changeset_apply.html
source_path: session/sqlite3changeset_apply.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6900
---

[](../session/intro.md)

## Session Module C Interface

## Apply A Changeset To A Database

> int sqlite3changeset_apply(\
>   sqlite3 \*db,                    /\* Apply change to "main" db of this handle \*/\
>   int nChangeset,                 /\* Size of changeset in bytes \*/\
>   void \*pChangeset,               /\* Changeset blob \*/\
>   int(\*xFilter)(\
>     void \*pCtx,                   /\* Copy of sixth arg to \_apply() \*/\
>     const char \*zTab              /\* Table name \*/\
>   ),\
>   int(\*xConflict)(\
>     void \*pCtx,                   /\* Copy of sixth arg to \_apply() \*/\
>     int eConflict,                /\* DATA, MISSING, CONFLICT, CONSTRAINT \*/\
>     sqlite3_changeset_iter \*p     /\* Handle describing change and conflict \*/\
>   ),\
>   void \*pCtx                      /\* First argument passed to xConflict \*/\
> );\
> int sqlite3changeset_apply_v2(\
>   sqlite3 \*db,                    /\* Apply change to "main" db of this handle \*/\
>   int nChangeset,                 /\* Size of changeset in bytes \*/\
>   void \*pChangeset,               /\* Changeset blob \*/\
>   int(\*xFilter)(\
>     void \*pCtx,                   /\* Copy of sixth arg to \_apply() \*/\
>     const char \*zTab              /\* Table name \*/\
>   ),\
>   int(\*xConflict)(\
>     void \*pCtx,                   /\* Copy of sixth arg to \_apply() \*/\
>     int eConflict,                /\* DATA, MISSING, CONFLICT, CONSTRAINT \*/\
>     sqlite3_changeset_iter \*p     /\* Handle describing change and conflict \*/\
>   ),\
>   void \*pCtx,                     /\* First argument passed to xConflict \*/\
>   void \*\*ppRebase, int \*pnRebase, /\* OUT: Rebase data \*/\
>   int flags                       /\* SESSION_CHANGESETAPPLY\_\* flags \*/\
> );\
> int sqlite3changeset_apply_v3(\
>   sqlite3 \*db,                    /\* Apply change to "main" db of this handle \*/\
>   int nChangeset,                 /\* Size of changeset in bytes \*/\
>   void \*pChangeset,               /\* Changeset blob \*/\
>   int(\*xFilter)(\
>     void \*pCtx,                   /\* Copy of sixth arg to \_apply() \*/\
>     sqlite3_changeset_iter \*p     /\* Handle describing change \*/\
>   ),\
>   int(\*xConflict)(\
>     void \*pCtx,                   /\* Copy of sixth arg to \_apply() \*/\
>     int eConflict,                /\* DATA, MISSING, CONFLICT, CONSTRAINT \*/\
>     sqlite3_changeset_iter \*p     /\* Handle describing change and conflict \*/\
>   ),\
>   void \*pCtx,                     /\* First argument passed to xConflict \*/\
>   void \*\*ppRebase, int \*pnRebase, /\* OUT: Rebase data \*/\
>   int flags                       /\* SESSION_CHANGESETAPPLY\_\* flags \*/\
> );\

Apply a changeset or patchset to a database. These functions attempt to update the "main" database attached to handle db with the changes found in the changeset passed via the second and third arguments.

All changes made by these functions are enclosed in a savepoint transaction. If any other error (aside from a constraint failure when attempting to write to the target database) occurs, then the savepoint transaction is rolled back, restoring the target database to its original state, and an SQLite error code returned. Additionally, starting with version 3.51.0, an error code and error message that may be accessed using the [sqlite3_errcode()](../c3ref/errcode.md) and [sqlite3_errmsg()](../c3ref/errcode.md) APIs are left in the database handle.

The fourth argument (xFilter) passed to these functions is the "filter callback". This may be passed NULL, in which case all changes in the changeset are applied to the database. For sqlite3changeset_apply() and sqlite3_changeset_apply_v2(), if it is not NULL, then it is invoked once for each table affected by at least one change in the changeset. In this case the table name is passed as the second argument, and a copy of the context pointer passed as the sixth argument to apply() or apply_v2() as the first. If the "filter callback" returns zero, then no attempt is made to apply any changes to the table. Otherwise, if the return value is non-zero, all changes related to the table are attempted.

For sqlite3_changeset_apply_v3(), the xFilter callback is invoked once per change. The second argument in this case is an sqlite3_changeset_iter that may be queried using the usual APIs for the details of the current change. If the "filter callback" returns zero in this case, then no attempt is made to apply the current change. If it returns non-zero, the change is applied.

For each table that is not excluded by the filter callback, this function tests that the target database contains a compatible table. A table is considered compatible if all of the following are true:

- The table has the same name as the name recorded in the changeset, and
- The table has at least as many columns as recorded in the changeset, and
- The table has primary key columns in the same position as recorded in the changeset.

If there is no compatible table, it is not an error, but none of the changes associated with the table are applied. A warning message is issued via the sqlite3_log() mechanism with the error code SQLITE_SCHEMA. At most one such warning is issued for each table in the changeset.

For each change for which there is a compatible table, an attempt is made to modify the table contents according to each UPDATE, INSERT or DELETE change that is not excluded by a filter callback. If a change cannot be applied cleanly, the conflict handler function passed as the fifth argument to sqlite3changeset_apply() may be invoked. A description of exactly when the conflict handler is invoked for each type of change is below.

Unlike the xFilter argument, xConflict may not be passed NULL. The results of passing anything other than a valid function pointer as the xConflict argument are undefined.

Each time the conflict handler function is invoked, it must return one of [SQLITE_CHANGESET_OMIT](../session/c_changeset_abort.md), [SQLITE_CHANGESET_ABORT](../session/c_changeset_abort.md) or [SQLITE_CHANGESET_REPLACE](../session/c_changeset_abort.md). SQLITE_CHANGESET_REPLACE may only be returned if the second argument passed to the conflict handler is either SQLITE_CHANGESET_DATA or SQLITE_CHANGESET_CONFLICT. If the conflict-handler returns an illegal value, any changes already made are rolled back and the call to sqlite3changeset_apply() returns SQLITE_MISUSE. Different actions are taken by sqlite3changeset_apply() depending on the value returned by each invocation of the conflict-handler function. Refer to the documentation for the three [available return values](../session/c_changeset_abort.md) for details.

DELETE Changes  
For each DELETE change, the function checks if the target database contains a row with the same primary key value (or values) as the original row values stored in the changeset. If it does, and the values stored in all non-primary key columns also match the values stored in the changeset the row is deleted from the target database.

If a row with matching primary key values is found, but one or more of the non-primary key fields contains a value different from the original row value stored in the changeset, the conflict-handler function is invoked with [SQLITE_CHANGESET_DATA](../session/c_changeset_conflict.md) as the second argument. If the database table has more columns than are recorded in the changeset, only the values of those non-primary key fields are compared against the current database contents - any trailing database table columns are ignored.

If no row with matching primary key values is found in the database, the conflict-handler function is invoked with [SQLITE_CHANGESET_NOTFOUND](../session/c_changeset_conflict.md) passed as the second argument.

If the DELETE operation is attempted, but SQLite returns SQLITE_CONSTRAINT (which can only happen if a foreign key constraint is violated), the conflict-handler function is invoked with [SQLITE_CHANGESET_CONSTRAINT](../session/c_changeset_conflict.md) passed as the second argument. This includes the case where the DELETE operation is attempted because an earlier call to the conflict handler function returned [SQLITE_CHANGESET_REPLACE](../session/c_changeset_abort.md).

INSERT Changes  
For each INSERT change, an attempt is made to insert the new row into the database. If the changeset row contains fewer fields than the database table, the trailing fields are populated with their default values.

If the attempt to insert the row fails because the database already contains a row with the same primary key values, the conflict handler function is invoked with the second argument set to [SQLITE_CHANGESET_CONFLICT](../session/c_changeset_conflict.md).

If the attempt to insert the row fails because of some other constraint violation (e.g. NOT NULL or UNIQUE), the conflict handler function is invoked with the second argument set to [SQLITE_CHANGESET_CONSTRAINT](../session/c_changeset_conflict.md). This includes the case where the INSERT operation is re-attempted because an earlier call to the conflict handler function returned [SQLITE_CHANGESET_REPLACE](../session/c_changeset_abort.md).

UPDATE Changes  
For each UPDATE change, the function checks if the target database contains a row with the same primary key value (or values) as the original row values stored in the changeset. If it does, and the values stored in all modified non-primary key columns also match the values stored in the changeset the row is updated within the target database.

If a row with matching primary key values is found, but one or more of the modified non-primary key fields contains a value different from an original row value stored in the changeset, the conflict-handler function is invoked with [SQLITE_CHANGESET_DATA](../session/c_changeset_conflict.md) as the second argument. Since UPDATE changes only contain values for non-primary key fields that are to be modified, only those fields need to match the original values to avoid the SQLITE_CHANGESET_DATA conflict-handler callback.

If no row with matching primary key values is found in the database, the conflict-handler function is invoked with [SQLITE_CHANGESET_NOTFOUND](../session/c_changeset_conflict.md) passed as the second argument.

If the UPDATE operation is attempted, but SQLite returns SQLITE_CONSTRAINT, the conflict-handler function is invoked with [SQLITE_CHANGESET_CONSTRAINT](../session/c_changeset_conflict.md) passed as the second argument. This includes the case where the UPDATE operation is attempted after an earlier call to the conflict handler function returned [SQLITE_CHANGESET_REPLACE](../session/c_changeset_abort.md).

It is safe to execute SQL statements, including those that write to the table that the callback related to, from within the xConflict callback. This can be used to further customize the application's conflict resolution strategy.

If the output parameters (ppRebase) and (pnRebase) are non-NULL and the input is a changeset (not a patchset), then sqlite3changeset_apply_v2() may set (\*ppRebase) to point to a "rebase" that may be used with the sqlite3_rebaser APIs buffer before returning. In this case (\*pnRebase) is set to the size of the buffer in bytes. It is the responsibility of the caller to eventually free any such buffer using sqlite3_free(). The buffer is only allocated and populated if one or more conflicts were encountered while applying the patchset. See comments surrounding the sqlite3_rebaser APIs for further details.

The behavior of sqlite3changeset_apply_v2() and its streaming equivalent may be modified by passing a combination of [supported flags](../session/c_changesetapply_fknoaction.md) as the 9th parameter.

Note that the sqlite3changeset_apply_v2() API is still **experimental** and therefore subject to change.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
