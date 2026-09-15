---
title: Flags for sqlite3_serialize
source_url: https://www.sqlite.org/c3ref/c_serialize_nocopy.html
source_path: c3ref/c_serialize_nocopy.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 670
---

> \
> \#define SQLITE_SERIALIZE_NOCOPY 0x001   /\* Do no memory allocations \*/\

Zero or more of the following constants can be OR-ed together for the F argument to [sqlite3_serialize(D,S,P,F)](../c3ref/serialize.md).

SQLITE_SERIALIZE_NOCOPY means that [sqlite3_serialize()](../c3ref/serialize.md) will return a pointer to contiguous in-memory database that it is currently using, without making a copy of the database. If SQLite is not currently using a contiguous in-memory database, then this option causes [sqlite3_serialize()](../c3ref/serialize.md) to return a NULL pointer. SQLite will only be using a contiguous in-memory database if it has been initialized by a prior call to [sqlite3_deserialize()](../c3ref/deserialize.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
