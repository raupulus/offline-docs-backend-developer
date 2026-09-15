---
title: Database Connection For Functions
source_url: https://www.sqlite.org/c3ref/context_db_handle.html
source_path: c3ref/context_db_handle.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 970
---

> \
> sqlite3 \*sqlite3_context_db_handle(sqlite3_context\*);\

The sqlite3_context_db_handle() interface returns a copy of the pointer to the [database connection](../c3ref/sqlite3.md) (the 1st parameter) of the [sqlite3_create_function()](../c3ref/create_function.md) and [sqlite3_create_function16()](../c3ref/create_function.md) routines that originally registered the application defined function.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
