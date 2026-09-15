---
title: Deserialize a database
source_url: https://www.sqlite.org/c3ref/deserialize.html
source_path: c3ref/deserialize.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1150
---

> \
> int sqlite3_deserialize(\
>   sqlite3 \*db,            /\* The database connection \*/\
>   const char \*zSchema,    /\* Which DB to reopen with the deserialization \*/\
>   unsigned char \*pData,   /\* The serialized database content \*/\
>   sqlite3_int64 szDb,     /\* Number of bytes in the deserialization \*/\
>   sqlite3_int64 szBuf,    /\* Total size of buffer pData\[\] \*/\
>   unsigned mFlags         /\* Zero or more SQLITE_DESERIALIZE\_\* flags \*/\
> );\

The sqlite3_deserialize(D,S,P,N,M,F) interface causes the [database connection](../c3ref/sqlite3.md) D to disconnect from database S and then reopen S as an in-memory database based on the serialization contained in P. If S is a NULL pointer, the main database is used. The serialized database P is N bytes in size. M is the size of the buffer P, which might be larger than N. If M is larger than N, and the SQLITE_DESERIALIZE_READONLY bit is not set in F, then SQLite is permitted to add content to the in-memory database as long as the total size does not exceed M bytes.

If the SQLITE_DESERIALIZE_FREEONCLOSE bit is set in F, then SQLite will invoke sqlite3_free() on the serialization buffer when the database connection closes. If the SQLITE_DESERIALIZE_RESIZEABLE bit is set, then SQLite will try to increase the buffer size using sqlite3_realloc64() if writes on the database cause it to grow larger than M bytes.

Applications must not modify the buffer P or invalidate it before the database connection D is closed.

The sqlite3_deserialize() interface will fail with SQLITE_BUSY if the database is currently in a read transaction or is involved in a backup operation.

It is not possible to deserialize into the TEMP database. If the S argument to sqlite3_deserialize(D,S,P,N,M,F) is "temp" then the function returns SQLITE_ERROR.

The deserialized database should not be in [WAL mode](../wal.md). If the database is in WAL mode, then any attempt to use the database file will result in an [SQLITE_CANTOPEN](../rescode.md#cantopen) error. The application can set the [file format version numbers](../fileformat2.md#vnums) (bytes 18 and 19) of the input database P to 0x01 prior to invoking sqlite3_deserialize(D,S,P,N,M,F) to force the database file into rollback mode and work around this limitation.

If sqlite3_deserialize(D,S,P,N,M,F) fails for any reason and if the SQLITE_DESERIALIZE_FREEONCLOSE bit is set in argument F, then [sqlite3_free()](../c3ref/free.md) is invoked on argument P prior to returning.

This interface is omitted if SQLite is compiled with the [SQLITE_OMIT_DESERIALIZE](../compile.md#omit_deserialize) option.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
