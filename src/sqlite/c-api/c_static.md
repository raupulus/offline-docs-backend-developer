---
title: Constants Defining Special Destructor Behavior
source_url: https://www.sqlite.org/c3ref/c_static.html
source_path: c3ref/c_static.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 710
---

> \
> typedef void (\*sqlite3_destructor_type)(void\*);\
> \#define SQLITE_STATIC      ((sqlite3_destructor_type)0)\
> \#define SQLITE_TRANSIENT   ((sqlite3_destructor_type)-1)\

These are special values for the destructor that is passed in as the final argument to routines like [sqlite3_result_blob()](../c3ref/result_blob.md). If the destructor argument is SQLITE_STATIC, it means that the content pointer is constant and will never change. It does not need to be destroyed. The SQLITE_TRANSIENT value means that the content will likely change in the near future and that SQLite should make its own private copy of the content before returning.

The typedef is necessary to work around problems in certain C++ compilers.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
