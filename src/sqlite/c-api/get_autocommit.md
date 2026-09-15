---
title: Test For Auto-Commit Mode
source_url: https://www.sqlite.org/c3ref/get_autocommit.html
source_path: c3ref/get_autocommit.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1320
---

> \
> int sqlite3_get_autocommit(sqlite3\*);\

The sqlite3_get_autocommit() interface returns non-zero or zero if the given database connection is or is not in autocommit mode, respectively. Autocommit mode is on by default. Autocommit mode is disabled by a [BEGIN](../lang_transaction.md) statement. Autocommit mode is re-enabled by a [COMMIT](../lang_transaction.md) or [ROLLBACK](../lang_transaction.md).

If certain kinds of errors occur on a statement within a multi-statement transaction (errors including [SQLITE_FULL](../rescode.md#full), [SQLITE_IOERR](../rescode.md#ioerr), [SQLITE_NOMEM](../rescode.md#nomem), [SQLITE_BUSY](../rescode.md#busy), and [SQLITE_INTERRUPT](../rescode.md#interrupt)) then the transaction might be rolled back automatically. The only way to find out whether SQLite automatically rolled back the transaction after an error is to use this function.

If another thread changes the autocommit status of the database connection while this routine is running, then the return value is undefined.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
