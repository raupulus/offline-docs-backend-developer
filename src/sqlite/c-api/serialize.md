---
title: Serialize a database
source_url: https://www.sqlite.org/c3ref/serialize.html
source_path: c3ref/serialize.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1730
---

> \
> unsigned char \*sqlite3_serialize(\
>   sqlite3 \*db,           /\* The database connection \*/\
>   const char \*zSchema,   /\* Which DB to serialize. ex: "main", "temp", ... \*/\
>   sqlite3_int64 \*piSize, /\* Write size of the DB here, if not NULL \*/\
>   unsigned int mFlags    /\* Zero or more SQLITE_SERIALIZE\_\* flags \*/\
> );\

The sqlite3_serialize(D,S,P,F) interface returns a pointer to memory that is a serialization of the S database on [database connection](../c3ref/sqlite3.md) D. If S is a NULL pointer, the main database is used. If P is not a NULL pointer, then the size of the database in bytes is written into \*P.

For an ordinary on-disk database file, the serialization is just a copy of the disk file. For an in-memory database or a "TEMP" database, the serialization is the same sequence of bytes which would be written to disk if that database were backed up to disk.

The usual case is that sqlite3_serialize() copies the serialization of the database into memory obtained from [sqlite3_malloc64()](../c3ref/free.md) and returns a pointer to that memory. The caller is responsible for freeing the returned value to avoid a memory leak. However, if the F argument contains the SQLITE_SERIALIZE_NOCOPY bit, then no memory allocations are made, and the sqlite3_serialize() function will return a pointer to the contiguous memory representation of the database that SQLite is currently using for that database, or NULL if no such contiguous memory representation of the database exists. A contiguous memory representation of the database will usually only exist if there has been a prior call to [sqlite3_deserialize(D,S,...)](../c3ref/deserialize.md) with the same values of D and S. The size of the database is written into \*P even if the SQLITE_SERIALIZE_NOCOPY bit is set but no contiguous copy of the database exists.

After the call, if the SQLITE_SERIALIZE_NOCOPY bit had been set, the returned buffer content will remain accessible and unchanged until either the next write operation on the connection or when the connection is closed, and applications must not modify the buffer. If the bit had been clear, the returned buffer will not be accessed by SQLite after the call.

A call to sqlite3_serialize(D,S,P,F) might return NULL even if the SQLITE_SERIALIZE_NOCOPY bit is omitted from argument F if a memory allocation error occurs.

This interface is omitted if SQLite is compiled with the [SQLITE_OMIT_DESERIALIZE](../compile.md#omit_deserialize) option.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
