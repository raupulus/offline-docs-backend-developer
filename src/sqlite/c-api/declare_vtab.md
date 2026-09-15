---
title: Declare The Schema Of A Virtual Table
source_url: https://www.sqlite.org/c3ref/declare_vtab.html
source_path: c3ref/declare_vtab.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1140
---

> \
> int sqlite3_declare_vtab(sqlite3\*, const char \*zSQL);\

The [xCreate](../vtab.md#xcreate) and [xConnect](../vtab.md#xconnect) methods of a [virtual table module](../c3ref/module.md) call this interface to declare the format (the names and datatypes of the columns) of the virtual tables they implement.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
