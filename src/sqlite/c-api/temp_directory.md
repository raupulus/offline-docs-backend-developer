---
title: Name Of The Folder Holding Temporary Files
source_url: https://www.sqlite.org/c3ref/temp_directory.html
source_path: c3ref/temp_directory.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2070
---

> \
> SQLITE_EXTERN char \*sqlite3_temp_directory;\

If this global variable is made to point to a string which is the name of a folder (a.k.a. directory), then all temporary files created by SQLite when using a built-in [VFS](../c3ref/vfs.md) will be placed in that directory. If this variable is a NULL pointer, then SQLite performs a search for an appropriate temporary file directory.

Applications are strongly discouraged from using this global variable. It is required to set a temporary folder on Windows Runtime (WinRT). But for all other platforms, it is highly recommended that applications neither read nor write this variable. This global variable is a relic that exists for backwards compatibility of legacy applications and should be avoided in new projects.

It is not safe to read or modify this variable in more than one thread at a time. It is not safe to read or modify this variable if a [database connection](../c3ref/sqlite3.md) is being used at the same time in a separate thread. It is intended that this variable be set once as part of process initialization and before any SQLite interface routines have been called and that this variable remain unchanged thereafter.

The [temp_store_directory pragma](../pragma.md#pragma_temp_store_directory) may modify this variable and cause it to point to memory obtained from [sqlite3_malloc](../c3ref/free.md). Furthermore, the [temp_store_directory pragma](../pragma.md#pragma_temp_store_directory) always assumes that any string that this variable points to is held in memory obtained from [sqlite3_malloc](../c3ref/free.md) and the pragma may attempt to free that memory using [sqlite3_free](../c3ref/free.md). Hence, if this variable is modified directly, either it should be made NULL or made to point to memory obtained from [sqlite3_malloc](../c3ref/free.md) or else the use of the [temp_store_directory pragma](../pragma.md#pragma_temp_store_directory) should be avoided. Except when requested by the [temp_store_directory pragma](../pragma.md#pragma_temp_store_directory), SQLite does not free the memory that sqlite3_temp_directory points to. If the application wants that memory to be freed, it must do so itself, taking care to only do so after all [database connection](../c3ref/sqlite3.md) objects have been destroyed.

**Note to Windows Runtime users:** The temporary directory must be set prior to calling [sqlite3_open](../c3ref/open.md) or [sqlite3_open_v2](../c3ref/open.md). Otherwise, various features that require the use of temporary files may fail. Here is an example of how to do this using C++ with the Windows Runtime:

> \
> LPCWSTR zPath = Windows::Storage::ApplicationData::Current-\>\
>       TemporaryFolder-\>Path-\>Data();\
> char zPathBuf\[MAX_PATH + 1\];\
> memset(zPathBuf, 0, sizeof(zPathBuf));\
> WideCharToMultiByte(CP_UTF8, 0, zPath, -1, zPathBuf, sizeof(zPathBuf),\
>       NULL, NULL);\
> sqlite3_temp_directory = sqlite3_mprintf("%s", zPathBuf);\

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
