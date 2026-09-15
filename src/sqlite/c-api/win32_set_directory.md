---
title: Win32 Specific Interface
source_url: https://www.sqlite.org/c3ref/win32_set_directory.html
source_path: c3ref/win32_set_directory.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2380
---

> \
> int sqlite3_win32_set_directory(\
>   unsigned long type, /\* Identifier for directory being set or reset \*/\
>   void \*zValue        /\* New value for directory being set or reset \*/\
> );\
> int sqlite3_win32_set_directory8(unsigned long type, const char \*zValue);\
> int sqlite3_win32_set_directory16(unsigned long type, const void \*zValue);\

These interfaces are available only on Windows. The [sqlite3_win32_set_directory](../c3ref/win32_set_directory.md) interface is used to set the value associated with the [sqlite3_temp_directory](../c3ref/temp_directory.md) or [sqlite3_data_directory](../c3ref/data_directory.md) variable, to zValue, depending on the value of the type parameter. The zValue parameter should be NULL to cause the previous value to be freed via [sqlite3_free](../c3ref/free.md); a non-NULL value will be copied into memory obtained from [sqlite3_malloc](../c3ref/free.md) prior to being used. The [sqlite3_win32_set_directory](../c3ref/win32_set_directory.md) interface returns [SQLITE_OK](../rescode.md#ok) to indicate success, [SQLITE_ERROR](../rescode.md#error) if the type is unsupported, or [SQLITE_NOMEM](../rescode.md#nomem) if memory could not be allocated. The value of the [sqlite3_data_directory](../c3ref/data_directory.md) variable is intended to act as a replacement for the current directory on the sub-platforms of Win32 where that concept is not present, e.g. WinRT and UWP. The [sqlite3_win32_set_directory8](../c3ref/win32_set_directory.md) and [sqlite3_win32_set_directory16](../c3ref/win32_set_directory.md) interfaces behave exactly the same as the sqlite3_win32_set_directory interface except the string parameter must be UTF-8 or UTF-16, respectively.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
