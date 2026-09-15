---
title: The SQLITE_MEMSTAT Virtual Table
source_url: https://www.sqlite.org/memstat.html
source_path: memstat.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 3560
---

# 1. Overview

The SQLITE_MEMSTAT extension implements an [eponymous-only virtual table](vtab.md#epoonlyvtab) that provides SQL access to the [sqlite3_status64()](c3ref/status.md) and [sqlite3_db_status()](c3ref/db_status.md) interfaces.

The SQLITE_STMT extension can also be loaded at run-time by compiling the extension into a shared library or DLL using the source code at <https://sqlite.org/src/file/ext/misc/memstat.c> and following the instructions for how to [compile loadable extensions](loadext.md#build).

# 2. Usage

The SQLITE_MEMSTAT virtual table is a read-only table that can be queried to determine performance characteristics (primarily the amount of memory being used) of the current instance of SQLite. The SQLITE_MEMSTATE table is essentially a wrapper around the C-language APIs [sqlite3_status64()](c3ref/status.md) and [sqlite3_db_status()](c3ref/db_status.md). If the [memstat.c](https://sqlite.org/src/file/ext/misc/memstat.c) source file is compiled with the -DSQLITE_ENABLE_ZIPVFS option, then SQLITE_MEMSTAT will also do some [file-control](c3ref/file_control.md) calls to extract memory usage information about the [ZIPVFS](https://www.hwaci.com/sw/sqlite/zipvfs.html) subsystem, if that subsystem has been licensed, installed, and is in use.

The SQLITE_MEMSTAT table appears to have the following schema:

CREATE TABLE sqlite_memstat(\
  name TEXT,\
  schema TEXT,\
  value INT,\
  hiwtr INT\
);\

Each row of the SQLITE_MEMSTAT table corresponds to a single call to one of the [sqlite3_status64()](c3ref/status.md) or [sqlite3_db_status()](c3ref/db_status.md) interfaces. The NAME column of the row identifies which "verb" was passed to those interfaces. For example, if [sqlite3_status64()](c3ref/status.md) is invoked with [SQLITE_STATUS_MEMORY_USED](c3ref/c_status_malloc_count.md#sqlitestatusmemoryused), then the NAME column is 'MEMORY_USED'. Or if [sqlite3_db_status()](c3ref/db_status.md) is invoked with [SQLITE_DBSTATUS_CACHE_USED](c3ref/c_dbstatus_options.md#sqlitedbstatuscacheused), then the NAME column is "DB_CACHE_USED".

The SCHEMA column is NULL, except for cases when the [sqlite3_file_control()](c3ref/file_control.md) interface is used to interrogate the ZIPVFS backend. As this only happens when the memstat.c module is compiled with -DSQLITE_ENABLE_ZIPVFS and when [ZIPVFS](https://www.hwaci.com/sw/sqlite/zipvfs.html) is in use, SCHEMA is usually NULL.

The VALUE and HIWTR columns report the current value of the measure and its "high-water mark". The high-water mark is the highest value ever seen for the measurement, at least since the last reset. The SQLITE_MEMSTAT virtual table does not provide a mechanism for resetting the high-water mark.

Depending on which parameter is being interrogated, one of the VALUE or HIWTR mark measurements might be undefined. For example, only the high-water mark is meaningful for [SQLITE_STATUS_MALLOC_SIZE](c3ref/c_status_malloc_count.md#sqlitestatusmallocsize), and only the current value is meaningful for [SQLITE_DBSTATUS_CACHE_USED](c3ref/c_dbstatus_options.md#sqlitedbstatuscacheused). For rows where one or the other of VALUE or HIWTR is not meaningful, that value is returned as NULL.
