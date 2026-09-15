---
title: Virtual Table Interface Configuration
source_url: https://www.sqlite.org/c3ref/vtab_config.html
source_path: c3ref/vtab_config.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2260
---

> \
> int sqlite3_vtab_config(sqlite3\*, int op, ...);\

This function may be called by either the [xConnect](../vtab.md#xconnect) or [xCreate](../vtab.md#xcreate) method of a [virtual table](../vtab.md) implementation to configure various facets of the virtual table interface.

If this interface is invoked outside the context of an xConnect or xCreate virtual table method then the behavior is undefined.

In the call sqlite3_vtab_config(D,C,...) the D parameter is the [database connection](../c3ref/sqlite3.md) in which the virtual table is being created and which is passed in as the first argument to the [xConnect](../vtab.md#xconnect) or [xCreate](../vtab.md#xcreate) method that is invoking sqlite3_vtab_config(). The C parameter is one of the [virtual table configuration options](../c3ref/c_vtab_constraint_support.md). The presence and meaning of parameters after C depend on which [virtual table configuration option](../c3ref/c_vtab_constraint_support.md) is used.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
