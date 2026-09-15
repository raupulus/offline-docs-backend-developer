---
title: Enable Or Disable Shared Pager Cache
source_url: https://www.sqlite.org/c3ref/enable_shared_cache.html
source_path: c3ref/enable_shared_cache.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1180
---

> \
> int sqlite3_enable_shared_cache(int);\

This routine enables or disables the sharing of the database cache and schema data structures between [connections](../c3ref/sqlite3.md) to the same database. Sharing is enabled if the argument is true and disabled if the argument is false.

This interface is omitted if SQLite is compiled with [-DSQLITE_OMIT_SHARED_CACHE](../compile.md#omit_shared_cache). The [-DSQLITE_OMIT_SHARED_CACHE](../compile.md#omit_shared_cache) compile-time option is recommended because the [use of shared cache mode is discouraged](../sharedcache.md#dontuse).

Cache sharing is enabled and disabled for an entire process. This is a change as of SQLite [version 3.5.0](../releaselog/3_5_0.md) (2007-09-04). In prior versions of SQLite, sharing was enabled or disabled for each thread separately.

The cache sharing mode set by this interface effects all subsequent calls to [sqlite3_open()](../c3ref/open.md), [sqlite3_open_v2()](../c3ref/open.md), and [sqlite3_open16()](../c3ref/open.md). Existing database connections continue to use the sharing mode that was in effect at the time they were opened.

This routine returns [SQLITE_OK](../rescode.md#ok) if shared cache was enabled or disabled successfully. An [error code](../rescode.md) is returned otherwise.

Shared cache is disabled by default. It is recommended that it stay that way. In other words, do not use this routine. This interface continues to be provided for historical compatibility, but its use is discouraged. Any use of shared cache is discouraged. If shared cache must be used, it is recommended that shared cache only be enabled for individual database connections using the [sqlite3_open_v2()](../c3ref/open.md) interface with the [SQLITE_OPEN_SHAREDCACHE](../c3ref/c_open_autoproxy.md) flag.

Note: This method is disabled on MacOS X 10.7 and iOS version 5.0 and will always return SQLITE_MISUSE. On those systems, shared cache mode should be enabled per-database connection via [sqlite3_open_v2()](../c3ref/open.md) with [SQLITE_OPEN_SHAREDCACHE](../c3ref/c_open_autoproxy.md).

This interface is threadsafe on processors where writing a 32-bit integer is atomic.

See Also: [SQLite Shared-Cache Mode](../sharedcache.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
