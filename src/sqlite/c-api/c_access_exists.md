---
title: Flags for the xAccess VFS method
source_url: https://www.sqlite.org/c3ref/c_access_exists.html
source_path: c3ref/c_access_exists.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 420
---

> \
> \#define SQLITE_ACCESS_EXISTS    0\
> \#define SQLITE_ACCESS_READWRITE 1   /\* Used by PRAGMA temp_store_directory \*/\
> \#define SQLITE_ACCESS_READ      2   /\* Unused \*/\

These integer constants can be used as the third parameter to the xAccess method of an [sqlite3_vfs](../c3ref/vfs.md) object. They determine what kind of permissions the xAccess method is looking for. With SQLITE_ACCESS_EXISTS, the xAccess method simply checks whether the file exists. With SQLITE_ACCESS_READWRITE, the xAccess method checks whether the named directory is both readable and writable (in other words, if files can be added, removed, and renamed within the directory). The SQLITE_ACCESS_READWRITE constant is currently used only by the [temp_store_directory pragma](../pragma.md#pragma_temp_store_directory), though this could change in a future release of SQLite. With SQLITE_ACCESS_READ, the xAccess method checks whether the file is readable. The SQLITE_ACCESS_READ constant is currently unused, though it might be used in a future release of SQLite.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
