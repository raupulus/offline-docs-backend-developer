---
title: Collation Needed Callbacks
source_url: https://www.sqlite.org/c3ref/collation_needed.html
source_path: c3ref/collation_needed.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 850
---

> \
> int sqlite3_collation_needed(\
>   sqlite3\*,\
>   void\*,\
>   void(\*)(void\*,sqlite3\*,int eTextRep,const char\*)\
> );\
> int sqlite3_collation_needed16(\
>   sqlite3\*,\
>   void\*,\
>   void(\*)(void\*,sqlite3\*,int eTextRep,const void\*)\
> );\

To avoid having to register all collation sequences before a database can be used, a single callback function may be registered with the [database connection](../c3ref/sqlite3.md) to be invoked whenever an undefined collation sequence is required.

If the function is registered using the sqlite3_collation_needed() API, then it is passed the names of undefined collation sequences as strings encoded in UTF-8. If sqlite3_collation_needed16() is used, the names are passed as UTF-16 in machine native byte order. A call to either function replaces the existing collation-needed callback.

When the callback is invoked, the first argument passed is a copy of the second argument to sqlite3_collation_needed() or sqlite3_collation_needed16(). The second argument is the database connection. The third argument is one of [SQLITE_UTF8](../c3ref/c_any.md#sqliteutf8), [SQLITE_UTF16BE](../c3ref/c_any.md#sqliteutf16be), or [SQLITE_UTF16LE](../c3ref/c_any.md#sqliteutf16le), indicating the most desirable form of the collation sequence function required. The fourth parameter is the name of the required collation sequence.

The callback function should register the desired collation using [sqlite3_create_collation()](../c3ref/create_collation.md), [sqlite3_create_collation16()](../c3ref/create_collation.md), or [sqlite3_create_collation_v2()](../c3ref/create_collation.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
