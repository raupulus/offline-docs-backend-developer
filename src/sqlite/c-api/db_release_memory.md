---
title: Free Memory Used By A Database Connection
source_url: https://www.sqlite.org/c3ref/db_release_memory.html
source_path: c3ref/db_release_memory.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1120
---

> \
> int sqlite3_db_release_memory(sqlite3\*);\

The sqlite3_db_release_memory(D) interface attempts to free as much heap memory as possible from database connection D. Unlike the [sqlite3_release_memory()](../c3ref/release_memory.md) interface, this interface is in effect even when the [SQLITE_ENABLE_MEMORY_MANAGEMENT](../compile.md#enable_memory_management) compile-time option is omitted.

See also: [sqlite3_release_memory()](../c3ref/release_memory.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
