---
title: Status Parameters
source_url: https://www.sqlite.org/c3ref/c_status_malloc_count.html
source_path: c3ref/c_status_malloc_count.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 720
---

> \
> \#define SQLITE_STATUS_MEMORY_USED          0\
> \#define SQLITE_STATUS_PAGECACHE_USED       1\
> \#define SQLITE_STATUS_PAGECACHE_OVERFLOW   2\
> \#define SQLITE_STATUS_SCRATCH_USED         3  /\* NOT USED \*/\
> \#define SQLITE_STATUS_SCRATCH_OVERFLOW     4  /\* NOT USED \*/\
> \#define SQLITE_STATUS_MALLOC_SIZE          5\
> \#define SQLITE_STATUS_PARSER_STACK         6\
> \#define SQLITE_STATUS_PAGECACHE_SIZE       7\
> \#define SQLITE_STATUS_SCRATCH_SIZE         8  /\* NOT USED \*/\
> \#define SQLITE_STATUS_MALLOC_COUNT         9\

These integer constants designate various run-time status parameters that can be returned by [sqlite3_status()](../c3ref/status.md).

SQLITE_STATUS_MEMORY_USED  
This parameter is the current amount of memory checked out using [sqlite3_malloc()](../c3ref/free.md), either directly or indirectly. The figure includes calls made to [sqlite3_malloc()](../c3ref/free.md) by the application and internal memory usage by the SQLite library. Auxiliary page-cache memory controlled by [SQLITE_CONFIG_PAGECACHE](../c3ref/c_config_covering_index_scan.md#sqliteconfigpagecache) is not included in this parameter. The amount returned is the sum of the allocation sizes as reported by the xSize method in [sqlite3_mem_methods](../c3ref/mem_methods.md).

SQLITE_STATUS_MALLOC_SIZE  
This parameter records the largest memory allocation request handed to [sqlite3_malloc()](../c3ref/free.md) or [sqlite3_realloc()](../c3ref/free.md) (or their internal equivalents). Only the value returned in the \*pHighwater parameter to [sqlite3_status()](../c3ref/status.md) is of interest. The value written into the \*pCurrent parameter is undefined.

SQLITE_STATUS_MALLOC_COUNT  
This parameter records the number of separate memory allocations currently checked out.

SQLITE_STATUS_PAGECACHE_USED  
This parameter returns the number of pages used out of the [pagecache memory allocator](../malloc.md#pagecache) that was configured using [SQLITE_CONFIG_PAGECACHE](../c3ref/c_config_covering_index_scan.md#sqliteconfigpagecache). The value returned is in pages, not in bytes.

SQLITE_STATUS_PAGECACHE_OVERFLOW  
This parameter returns the number of bytes of page cache allocation which could not be satisfied by the [SQLITE_CONFIG_PAGECACHE](../c3ref/c_config_covering_index_scan.md#sqliteconfigpagecache) buffer and where forced to overflow to [sqlite3_malloc()](../c3ref/free.md). The returned value includes allocations that overflowed because they were too large (they were larger than the "sz" parameter to [SQLITE_CONFIG_PAGECACHE](../c3ref/c_config_covering_index_scan.md#sqliteconfigpagecache)) and allocations that overflowed because no space was left in the page cache.

SQLITE_STATUS_PAGECACHE_SIZE  
This parameter records the largest memory allocation request handed to the [pagecache memory allocator](../malloc.md#pagecache). Only the value returned in the \*pHighwater parameter to [sqlite3_status()](../c3ref/status.md) is of interest. The value written into the \*pCurrent parameter is undefined.

SQLITE_STATUS_SCRATCH_USED  
No longer used.

SQLITE_STATUS_SCRATCH_OVERFLOW  
No longer used.

SQLITE_STATUS_SCRATCH_SIZE  
No longer used.

SQLITE_STATUS_PARSER_STACK  
The \*pHighwater parameter records the deepest parser stack. The \*pCurrent value is undefined. The \*pHighwater value is only meaningful if SQLite is compiled with [YYTRACKMAXSTACKDEPTH](../compile.md#yytrackmaxstackdepth).

New status parameters may be added from time to time.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
