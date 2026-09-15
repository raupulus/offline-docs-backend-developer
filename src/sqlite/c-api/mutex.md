---
title: Mutex Handle
source_url: https://www.sqlite.org/c3ref/mutex.html
source_path: c3ref/mutex.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1520
---

> \
> typedef struct sqlite3_mutex sqlite3_mutex;\

The mutex module within SQLite defines [sqlite3_mutex](../c3ref/mutex.md) to be an abstract type for a mutex object. The SQLite core never looks at the internal representation of an [sqlite3_mutex](../c3ref/mutex.md). It only deals with pointers to the [sqlite3_mutex](../c3ref/mutex.md) object.

Mutexes are created using [sqlite3_mutex_alloc()](../c3ref/mutex_alloc.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
