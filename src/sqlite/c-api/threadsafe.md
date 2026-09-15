---
title: Test To See If The Library Is Threadsafe
source_url: https://www.sqlite.org/c3ref/threadsafe.html
source_path: c3ref/threadsafe.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2090
---

> \
> int sqlite3_threadsafe(void);\

The sqlite3_threadsafe() function returns zero if and only if SQLite was compiled with mutexing code omitted due to the [SQLITE_THREADSAFE](../compile.md#threadsafe) compile-time option being set to 0.

SQLite can be compiled with or without mutexes. When the [SQLITE_THREADSAFE](../compile.md#threadsafe) C preprocessor macro is 1 or 2, mutexes are enabled and SQLite is threadsafe. When the [SQLITE_THREADSAFE](../compile.md#threadsafe) macro is 0, the mutexes are omitted. Without the mutexes, it is not safe to use SQLite concurrently from more than one thread.

Enabling mutexes incurs a measurable performance penalty. So if speed is of utmost importance, it makes sense to disable the mutexes. But for maximum safety, mutexes should be enabled. The default behavior is for mutexes to be enabled.

This interface can be used by an application to make sure that the version of SQLite that it is linking against was compiled with the desired setting of the [SQLITE_THREADSAFE](../compile.md#threadsafe) macro.

This interface only reports on the compile-time mutex setting of the [SQLITE_THREADSAFE](../compile.md#threadsafe) flag. If SQLite is compiled with SQLITE_THREADSAFE=1 or =2 then mutexes are enabled by default but can be fully or partially disabled using a call to [sqlite3_config()](../c3ref/config.md) with the verbs [SQLITE_CONFIG_SINGLETHREAD](../c3ref/c_config_covering_index_scan.md#sqliteconfigsinglethread), [SQLITE_CONFIG_MULTITHREAD](../c3ref/c_config_covering_index_scan.md#sqliteconfigmultithread), or [SQLITE_CONFIG_SERIALIZED](../c3ref/c_config_covering_index_scan.md#sqliteconfigserialized). The return value of the sqlite3_threadsafe() function shows only the compile-time setting of thread safety, not any run-time changes to that setting made by sqlite3_config(). In other words, the return value from sqlite3_threadsafe() is unchanged by calls to sqlite3_config().

See the [threading mode](../threadsafe.md) documentation for additional information.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
