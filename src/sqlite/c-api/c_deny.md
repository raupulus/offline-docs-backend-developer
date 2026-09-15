---
title: Authorizer Return Codes
source_url: https://www.sqlite.org/c3ref/c_deny.html
source_path: c3ref/c_deny.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 510
---

> \
> \#define SQLITE_DENY   1   /\* Abort the SQL statement with an error \*/\
> \#define SQLITE_IGNORE 2   /\* Don't allow access, but don't generate an error \*/\

The [authorizer callback function](../c3ref/set_authorizer.md) must return either [SQLITE_OK](../rescode.md#ok) or one of these two constants in order to signal SQLite whether or not the action is permitted. See the [authorizer documentation](../c3ref/set_authorizer.md) for additional information.

Note that SQLITE_IGNORE is also used as a [conflict resolution mode](../c3ref/c_fail.md) returned from the [sqlite3_vtab_on_conflict()](../c3ref/vtab_on_conflict.md) interface.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
