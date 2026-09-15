---
title: Memory Allocator Statistics
source_url: https://www.sqlite.org/c3ref/memory_highwater.html
source_path: c3ref/memory_highwater.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1490
---

> \
> sqlite3_int64 sqlite3_memory_used(void);\
> sqlite3_int64 sqlite3_memory_highwater(int resetFlag);\

SQLite provides these two interfaces for reporting on the status of the [sqlite3_malloc()](../c3ref/free.md), [sqlite3_free()](../c3ref/free.md), and [sqlite3_realloc()](../c3ref/free.md) routines, which form the built-in memory allocation subsystem.

The [sqlite3_memory_used()](../c3ref/memory_highwater.md) routine returns the number of bytes of memory currently outstanding (malloced but not freed). The [sqlite3_memory_highwater()](../c3ref/memory_highwater.md) routine returns the maximum value of [sqlite3_memory_used()](../c3ref/memory_highwater.md) since the high-water mark was last reset. The values returned by [sqlite3_memory_used()](../c3ref/memory_highwater.md) and [sqlite3_memory_highwater()](../c3ref/memory_highwater.md) include any overhead added by SQLite in its implementation of [sqlite3_malloc()](../c3ref/free.md), but not overhead added by any underlying system library routines that [sqlite3_malloc()](../c3ref/free.md) may call.

The memory high-water mark is reset to the current value of [sqlite3_memory_used()](../c3ref/memory_highwater.md) if and only if the parameter to [sqlite3_memory_highwater()](../c3ref/memory_highwater.md) is true. The value returned by [sqlite3_memory_highwater(1)](../c3ref/memory_highwater.md) is the high-water mark prior to the reset.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
