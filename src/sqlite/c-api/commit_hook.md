---
title: Commit And Rollback Notification Callbacks
source_url: https://www.sqlite.org/c3ref/commit_hook.html
source_path: c3ref/commit_hook.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 910
---

> \
> void \*sqlite3_commit_hook(sqlite3\*, int(\*)(void\*), void\*);\
> void \*sqlite3_rollback_hook(sqlite3\*, void(\*)(void \*), void\*);\

The sqlite3_commit_hook() interface registers a callback function to be invoked whenever a transaction is [committed](../lang_transaction.md). Any callback set by a previous call to sqlite3_commit_hook() for the same database connection is overridden. The sqlite3_rollback_hook() interface registers a callback function to be invoked whenever a transaction is [rolled back](../lang_transaction.md). Any callback set by a previous call to sqlite3_rollback_hook() for the same database connection is overridden. The pArg argument is passed through to the callback. If the callback on a commit hook function returns non-zero, then the commit is converted into a rollback.

The sqlite3_commit_hook(D,C,P) and sqlite3_rollback_hook(D,C,P) functions return the P argument from the previous call of the same function on the same [database connection](../c3ref/sqlite3.md) D, or NULL for the first call for each function on D.

The commit and rollback hook callbacks are not reentrant. The callback implementation must not do anything that will modify the database connection that invoked the callback. Any actions to modify the database connection must be deferred until after the completion of the [sqlite3_step()](../c3ref/step.md) call that triggered the commit or rollback hook in the first place. Note that running any other SQL statements, including SELECT statements, or merely calling [sqlite3_prepare_v2()](../c3ref/prepare.md) and [sqlite3_step()](../c3ref/step.md) will modify the database connections for the meaning of "modify" in this paragraph.

Registering a NULL function disables the callback.

When the commit hook callback routine returns zero, the [COMMIT](../lang_transaction.md) operation is allowed to continue normally. If the commit hook returns non-zero, then the [COMMIT](../lang_transaction.md) is converted into a [ROLLBACK](../lang_transaction.md). The rollback hook is invoked on a rollback that results from a commit hook returning non-zero, just as it would be with any other rollback.

For the purposes of this API, a transaction is said to have been rolled back if an explicit "ROLLBACK" statement is executed, or an error or constraint causes an implicit rollback to occur. The rollback callback is not invoked if a transaction is automatically rolled back because the database connection is closed.

See also the [sqlite3_update_hook()](../c3ref/update_hook.md) interface.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
