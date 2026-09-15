---
title: Determine the transaction state of a database
source_url: https://www.sqlite.org/c3ref/txn_state.html
source_path: c3ref/txn_state.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2120
---

> \
> int sqlite3_txn_state(sqlite3\*,const char \*zSchema);\

The sqlite3_txn_state(D,S) interface returns the current [transaction state](../c3ref/c_txn_none.md) of schema S in database connection D. If S is NULL, then the highest transaction state of any schema on database connection D is returned. Transaction states are (in order of lowest to highest):

1.  SQLITE_TXN_NONE
2.  SQLITE_TXN_READ
3.  SQLITE_TXN_WRITE

If the S argument to sqlite3_txn_state(D,S) is not the name of a valid schema, then -1 is returned.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
