---
title: File Locking Levels
source_url: https://www.sqlite.org/c3ref/c_lock_exclusive.html
source_path: c3ref/c_lock_exclusive.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 600
---

> \
> \#define SQLITE_LOCK_NONE          0       /\* xUnlock() only \*/\
> \#define SQLITE_LOCK_SHARED        1       /\* xLock() or xUnlock() \*/\
> \#define SQLITE_LOCK_RESERVED      2       /\* xLock() only \*/\
> \#define SQLITE_LOCK_PENDING       3       /\* xLock() only \*/\
> \#define SQLITE_LOCK_EXCLUSIVE     4       /\* xLock() only \*/\

SQLite uses one of these integer values as the second argument to calls it makes to the xLock() and xUnlock() methods of an [sqlite3_io_methods](../c3ref/io_methods.md) object. These values are ordered from least restrictive to most restrictive.

The argument to xLock() is always SHARED or higher. The argument to xUnlock is either SHARED or NONE.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
