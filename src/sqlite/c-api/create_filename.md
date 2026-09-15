---
title: Create and Destroy VFS Filenames
source_url: https://www.sqlite.org/c3ref/create_filename.html
source_path: c3ref/create_filename.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 990
---

> \
> sqlite3_filename sqlite3_create_filename(\
>   const char \*zDatabase,\
>   const char \*zJournal,\
>   const char \*zWal,\
>   int nParam,\
>   const char \*\*azParam\
> );\
> void sqlite3_free_filename(sqlite3_filename);\

These interfaces are provided for use by [VFS shim](../vfs.md#shim) implementations and are not useful outside of that context.

The sqlite3_create_filename(D,J,W,N,P) allocates memory to hold a version of database filename D with corresponding journal file J and WAL file W and an array P of N URI Key/Value pairs. The result from sqlite3_create_filename(D,J,W,N,P) is a pointer to a database filename that is safe to pass to routines like:

- [sqlite3_uri_parameter()](../c3ref/uri_boolean.md),
- [sqlite3_uri_boolean()](../c3ref/uri_boolean.md),
- [sqlite3_uri_int64()](../c3ref/uri_boolean.md),
- [sqlite3_uri_key()](../c3ref/uri_boolean.md),
- [sqlite3_filename_database()](../c3ref/filename_database.md),
- [sqlite3_filename_journal()](../c3ref/filename_database.md), or
- [sqlite3_filename_wal()](../c3ref/filename_database.md).

If a memory allocation error occurs, sqlite3_create_filename() might return a NULL pointer. The memory obtained from sqlite3_create_filename(X) must be released by a corresponding call to sqlite3_free_filename(Y).

The P parameter in sqlite3_create_filename(D,J,W,N,P) should be an array of 2\*N pointers to strings. Each pair of pointers in this array corresponds to a key and value for a query parameter. The P parameter may be a NULL pointer if N is zero. None of the 2\*N pointers in the P array may be NULL pointers and key pointers should not be empty strings. None of the D, J, or W parameters to sqlite3_create_filename(D,J,W,N,P) may be NULL pointers, though they can be empty strings.

The sqlite3_free_filename(Y) routine releases a memory allocation previously obtained from sqlite3_create_filename(). Invoking sqlite3_free_filename(Y) where Y is a NULL pointer is a harmless no-op.

If the Y parameter to sqlite3_free_filename(Y) is anything other than a NULL pointer or a pointer previously acquired from sqlite3_create_filename(), then bad things such as heap corruption or segfaults may occur. The value Y should not be used again after sqlite3_free_filename(Y) has been called. This means that if the [sqlite3_vfs.xOpen()](../c3ref/vfs.md#sqlite3vfsxopen) method of a VFS has been called using Y, then the corresponding \[sqlite3_module.xClose() method should also be invoked prior to calling sqlite3_free_filename(Y).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
