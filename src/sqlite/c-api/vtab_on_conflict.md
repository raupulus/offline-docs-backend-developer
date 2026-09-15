---
title: Determine The Virtual Table Conflict Policy
source_url: https://www.sqlite.org/c3ref/vtab_on_conflict.html
source_path: c3ref/vtab_on_conflict.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2320
---

> \
> int sqlite3_vtab_on_conflict(sqlite3 \*);\

This function may only be called from within a call to the [xUpdate](../vtab.md#xupdate) method of a [virtual table](../vtab.md) implementation for an INSERT or UPDATE operation. The value returned is one of [SQLITE_ROLLBACK](../c3ref/c_fail.md), [SQLITE_IGNORE](../c3ref/c_deny.md), [SQLITE_FAIL](../c3ref/c_fail.md), [SQLITE_ABORT](../rescode.md#abort), or [SQLITE_REPLACE](../c3ref/c_fail.md), according to the [ON CONFLICT](../lang_conflict.md) mode of the SQL statement that triggered the call to the [xUpdate](../vtab.md#xupdate) method of the [virtual table](../vtab.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
