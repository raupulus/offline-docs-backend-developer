---
title: Return The Schema Name For A Database Connection
source_url: https://www.sqlite.org/c3ref/db_name.html
source_path: c3ref/db_name.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1100
---

> \
> const char \*sqlite3_db_name(sqlite3 \*db, int N);\

The sqlite3_db_name(D,N) interface returns a pointer to the schema name for the N-th database on database connection D, or a NULL pointer if N is out of range. An N value of 0 means the main database file. An N of 1 is the "temp" schema. Larger values of N correspond to various ATTACH-ed databases.

Space to hold the string that is returned by sqlite3_db_name() is managed by SQLite itself. The string might be deallocated by any operation that changes the schema, including [ATTACH](../lang_attach.md) or [DETACH](../lang_detach.md) or calls to [sqlite3_serialize()](../c3ref/serialize.md) or [sqlite3_deserialize()](../c3ref/deserialize.md), even operations that occur on a different thread. Applications that need to remember the string long-term should make their own copy. Applications that are accessing the same database connection simultaneously on multiple threads should mutex-protect calls to this API and should make their own private copy of the result prior to releasing the mutex.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
