---
title: Virtual Table Configuration Options
source_url: https://www.sqlite.org/c3ref/c_vtab_constraint_support.html
source_path: c3ref/c_vtab_constraint_support.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 780
---

> \
> \#define SQLITE_VTAB_CONSTRAINT_SUPPORT 1\
> \#define SQLITE_VTAB_INNOCUOUS          2\
> \#define SQLITE_VTAB_DIRECTONLY         3\
> \#define SQLITE_VTAB_USES_ALL_SCHEMAS   4\

These macros define the various options to the [sqlite3_vtab_config()](../c3ref/vtab_config.md) interface that [virtual table](../vtab.md) implementations can use to customize and optimize their behavior.

SQLITE_VTAB_CONSTRAINT_SUPPORT  
Calls of the form [sqlite3_vtab_config](../c3ref/vtab_config.md)(db,SQLITE_VTAB_CONSTRAINT_SUPPORT,X) are supported, where X is an integer. If X is zero, then the [virtual table](../vtab.md) whose [xCreate](../vtab.md#xcreate) or [xConnect](../vtab.md#xconnect) method invoked [sqlite3_vtab_config()](../c3ref/vtab_config.md) does not support constraints. In this configuration (which is the default) if a call to the [xUpdate](../vtab.md#xupdate) method returns [SQLITE_CONSTRAINT](../rescode.md#constraint), then the entire statement is rolled back as if [OR ABORT](../lang_conflict.md) had been specified as part of the user's SQL statement, regardless of the actual ON CONFLICT mode specified.

If X is non-zero, then the virtual table implementation guarantees that if [xUpdate](../vtab.md#xupdate) returns [SQLITE_CONSTRAINT](../rescode.md#constraint), it will do so before any modifications to internal or persistent data structures have been made. If the [ON CONFLICT](../lang_conflict.md) mode is ABORT, FAIL, IGNORE or ROLLBACK, SQLite is able to roll back a statement or database transaction, and abandon or continue processing the current SQL statement as appropriate. If the ON CONFLICT mode is REPLACE and the [xUpdate](../vtab.md#xupdate) method returns [SQLITE_CONSTRAINT](../rescode.md#constraint), SQLite handles this as if the ON CONFLICT mode had been ABORT.

Virtual table implementations that are required to handle OR REPLACE must do so within the [xUpdate](../vtab.md#xupdate) method. If a call to the [sqlite3_vtab_on_conflict()](../c3ref/vtab_on_conflict.md) function indicates that the current ON CONFLICT policy is REPLACE, the virtual table implementation should silently replace the appropriate rows within the xUpdate callback and return SQLITE_OK. Or, if this is not possible, it may return SQLITE_CONSTRAINT, in which case SQLite falls back to OR ABORT constraint handling.

SQLITE_VTAB_DIRECTONLY  
Calls of the form [sqlite3_vtab_config](../c3ref/vtab_config.md)(db,SQLITE_VTAB_DIRECTONLY) from within the the [xConnect](../vtab.md#xconnect) or [xCreate](../vtab.md#xcreate) methods of a [virtual table](../vtab.md) implementation prohibits that virtual table from being used from within triggers and views.

SQLITE_VTAB_INNOCUOUS  
Calls of the form [sqlite3_vtab_config](../c3ref/vtab_config.md)(db,SQLITE_VTAB_INNOCUOUS) from within the [xConnect](../vtab.md#xconnect) or [xCreate](../vtab.md#xcreate) methods of a [virtual table](../vtab.md) implementation identify that virtual table as being safe to use from within triggers and views. Conceptually, the SQLITE_VTAB_INNOCUOUS tag means that the virtual table can do no serious harm even if it is controlled by a malicious hacker. Developers should avoid setting the SQLITE_VTAB_INNOCUOUS flag unless absolutely necessary.

SQLITE_VTAB_USES_ALL_SCHEMAS  
Calls of the form [sqlite3_vtab_config](../c3ref/vtab_config.md)(db,SQLITE_VTAB_USES_ALL_SCHEMA) from within the the [xConnect](../vtab.md#xconnect) or [xCreate](../vtab.md#xcreate) methods of a [virtual table](../vtab.md) implementation instruct the query planner to begin at least a read transaction on all schemas ("main", "temp", and any ATTACH-ed databases) whenever the virtual table is used.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
