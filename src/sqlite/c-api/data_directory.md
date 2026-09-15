---
title: Name Of The Folder Holding Database Files
source_url: https://www.sqlite.org/c3ref/data_directory.html
source_path: c3ref/data_directory.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1030
---

> \
> SQLITE_EXTERN char \*sqlite3_data_directory;\

If this global variable is made to point to a string which is the name of a folder (a.k.a. directory), then all database files specified with a relative pathname and created or accessed by SQLite when using a built-in windows [VFS](../c3ref/vfs.md) will be assumed to be relative to that directory. If this variable is a NULL pointer, then SQLite assumes that all database files specified with a relative pathname are relative to the current directory for the process. Only the windows VFS makes use of this global variable; it is ignored by the unix VFS.

Changing the value of this variable while a database connection is open can result in a corrupt database.

It is not safe to read or modify this variable in more than one thread at a time. It is not safe to read or modify this variable if a [database connection](../c3ref/sqlite3.md) is being used at the same time in a separate thread. It is intended that this variable be set once as part of process initialization and before any SQLite interface routines have been called and that this variable remain unchanged thereafter.

The [data_store_directory pragma](../pragma.md#pragma_data_store_directory) may modify this variable and cause it to point to memory obtained from [sqlite3_malloc](../c3ref/free.md). Furthermore, the [data_store_directory pragma](../pragma.md#pragma_data_store_directory) always assumes that any string that this variable points to is held in memory obtained from [sqlite3_malloc](../c3ref/free.md) and the pragma may attempt to free that memory using [sqlite3_free](../c3ref/free.md). Hence, if this variable is modified directly, either it should be made NULL or made to point to memory obtained from [sqlite3_malloc](../c3ref/free.md) or else the use of the [data_store_directory pragma](../pragma.md#pragma_data_store_directory) should be avoided.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
