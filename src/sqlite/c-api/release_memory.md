---
title: Attempt To Free Heap Memory
source_url: https://www.sqlite.org/c3ref/release_memory.html
source_path: c3ref/release_memory.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1680
---

> \
> int sqlite3_release_memory(int);\

The sqlite3_release_memory() interface attempts to free N bytes of heap memory by deallocating non-essential memory allocations held by the database library. Memory used to cache database pages to improve performance is an example of non-essential memory. sqlite3_release_memory() returns the number of bytes actually freed, which might be more or less than the amount requested. The sqlite3_release_memory() routine is a no-op returning zero if SQLite is not compiled with [SQLITE_ENABLE_MEMORY_MANAGEMENT](../compile.md#enable_memory_management).

See also: [sqlite3_db_release_memory()](../c3ref/db_release_memory.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
