---
title: Remove Unnecessary Virtual Table Implementations
source_url: https://www.sqlite.org/c3ref/drop_modules.html
source_path: c3ref/drop_modules.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1160
---

> \
> int sqlite3_drop_modules(\
>   sqlite3 \*db,                /\* Remove modules from this connection \*/\
>   const char \*\*azKeep         /\* Except, do not remove the ones named here \*/\
> );\

The sqlite3_drop_modules(D,L) interface removes all virtual table modules from database connection D except those named on list L. The L parameter must be either NULL or a pointer to an array of pointers to strings where the array is terminated by a single NULL pointer. If the L parameter is NULL, then all virtual table modules are removed.

See also: [sqlite3_create_module()](../c3ref/create_module.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
