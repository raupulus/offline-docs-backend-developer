---
title: Retrieve the mutex for a database connection
source_url: https://www.sqlite.org/c3ref/db_mutex.html
source_path: c3ref/db_mutex.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1090
---

> \
> sqlite3_mutex \*sqlite3_db_mutex(sqlite3\*);\

This interface returns a pointer to the [sqlite3_mutex](../c3ref/mutex.md) object that serializes access to the [database connection](../c3ref/sqlite3.md) given in the argument when the [threading mode](../threadsafe.md) is Serialized. If the [threading mode](../threadsafe.md) is Single-thread or Multi-thread then this routine returns a NULL pointer.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
