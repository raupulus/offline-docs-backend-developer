---
title: Conflict resolution modes
source_url: https://www.sqlite.org/c3ref/c_fail.html
source_path: c3ref/c_fail.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 540
---

> \
> \#define SQLITE_ROLLBACK 1\
> /\* #define SQLITE_IGNORE 2 // Also used by sqlite3_authorizer() callback \*/\
> \#define SQLITE_FAIL     3\
> /\* #define SQLITE_ABORT 4  // Also an error code \*/\
> \#define SQLITE_REPLACE  5\

These constants are returned by [sqlite3_vtab_on_conflict()](../c3ref/vtab_on_conflict.md) to inform a [virtual table](../vtab.md) implementation of the [ON CONFLICT](../lang_conflict.md) mode for the SQL statement being evaluated.

Note that the [SQLITE_IGNORE](../c3ref/c_deny.md) constant is also used as a potential return value from the [sqlite3_set_authorizer()](../c3ref/set_authorizer.md) callback and that [SQLITE_ABORT](../rescode.md#abort) is also a [result code](../rescode.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
