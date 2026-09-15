---
title: Allowed return values from sqlite3_txn_state()
source_url: https://www.sqlite.org/c3ref/c_txn_none.html
source_path: c3ref/c_txn_none.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 770
---

> \
> \#define SQLITE_TXN_NONE  0\
> \#define SQLITE_TXN_READ  1\
> \#define SQLITE_TXN_WRITE 2\

These constants define the current transaction state of a database file. The [sqlite3_txn_state(D,S)](../c3ref/txn_state.md) interface returns one of these constants in order to describe the transaction state of schema S in [database connection](../c3ref/sqlite3.md) D.

<span id="sqlitetxnnone"></span>

SQLITE_TXN_NONE

The SQLITE_TXN_NONE state means that no transaction is currently pending.

<span id="sqlitetxnread"></span>

SQLITE_TXN_READ

The SQLITE_TXN_READ state means that the database is currently in a read transaction. Content has been read from the database file but nothing in the database file has changed. The transaction state will be advanced to SQLITE_TXN_WRITE if any changes occur and there are no other conflicting concurrent write transactions. The transaction state will revert to SQLITE_TXN_NONE following a [ROLLBACK](../lang_transaction.md) or [COMMIT](../lang_transaction.md).

<span id="sqlitetxnwrite"></span>

SQLITE_TXN_WRITE

The SQLITE_TXN_WRITE state means that the database is currently in a write transaction. Content has been written to the database file but has not yet committed. The transaction state will change to SQLITE_TXN_NONE at the next [ROLLBACK](../lang_transaction.md) or [COMMIT](../lang_transaction.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
