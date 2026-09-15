---
title: Flags for sqlite3_deserialize()
source_url: https://www.sqlite.org/c3ref/c_deserialize_freeonclose.html
source_path: c3ref/c_deserialize_freeonclose.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 520
---

> \
> \#define SQLITE_DESERIALIZE_FREEONCLOSE 1 /\* Call sqlite3_free() on close \*/\
> \#define SQLITE_DESERIALIZE_RESIZEABLE  2 /\* Resize using sqlite3_realloc64() \*/\
> \#define SQLITE_DESERIALIZE_READONLY    4 /\* Database is read-only \*/\

The following are allowed values for the 6th argument (the F argument) to the [sqlite3_deserialize(D,S,P,N,M,F)](../c3ref/deserialize.md) interface.

The SQLITE_DESERIALIZE_FREEONCLOSE means that the database serialization in the P argument is held in memory obtained from [sqlite3_malloc64()](../c3ref/free.md) and that SQLite should take ownership of this memory and automatically free it when it has finished using it. Without this flag, the caller is responsible for freeing any dynamically allocated memory.

The SQLITE_DESERIALIZE_RESIZEABLE flag means that SQLite is allowed to grow the size of the database using calls to [sqlite3_realloc64()](../c3ref/free.md). This flag should only be used if SQLITE_DESERIALIZE_FREEONCLOSE is also used. Without this flag, the deserialized database cannot increase in size beyond the number of bytes specified by the M parameter.

The SQLITE_DESERIALIZE_READONLY flag means that the deserialized database should be treated as read-only.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
