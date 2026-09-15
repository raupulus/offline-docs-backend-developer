---
title: Open A BLOB For Incremental I/O
source_url: https://www.sqlite.org/c3ref/blob_open.html
source_path: c3ref/blob_open.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 340
---

> \
> int sqlite3_blob_open(\
>   sqlite3\*,\
>   const char \*zDb,\
>   const char \*zTable,\
>   const char \*zColumn,\
>   sqlite3_int64 iRow,\
>   int flags,\
>   sqlite3_blob \*\*ppBlob\
> );\

This interfaces opens a [handle](../c3ref/blob.md) to the BLOB located in row iRow, column zColumn, table zTable in database zDb; in other words, the same BLOB that would be selected by:

\
SELECT zColumn FROM zDb.zTable WHERE [rowid](../lang_createtable.md#rowid) = iRow;\

Parameter zDb is not the filename that contains the database, but rather the symbolic name of the database. For attached databases, this is the name that appears after the AS keyword in the [ATTACH](../lang_attach.md) statement. For the main database file, the database name is "main". For TEMP tables, the database name is "temp".

If the flags parameter is non-zero, then the BLOB is opened for read and write access. If the flags parameter is zero, the BLOB is opened for read-only access.

On success, [SQLITE_OK](../rescode.md#ok) is returned and the new [BLOB handle](../c3ref/blob.md) is stored in \*ppBlob. Otherwise an [error code](../rescode.md) is returned and, unless the error code is SQLITE_MISUSE, \*ppBlob is set to NULL. This means that, provided the API is not misused, it is always safe to call [sqlite3_blob_close()](../c3ref/blob_close.md) on \*ppBlob after this function returns.

This function fails with SQLITE_ERROR if any of the following are true:

- Database zDb does not exist,
- Table zTable does not exist within database zDb,
- Table zTable is a WITHOUT ROWID table,
- Column zColumn does not exist,
- Row iRow is not present in the table,
- The specified column of row iRow contains a value that is not a TEXT or BLOB value,
- Column zColumn is part of an index, PRIMARY KEY or UNIQUE constraint and the blob is being opened for read/write access,
- [Foreign key constraints](../foreignkeys.md) are enabled, column zColumn is part of a [child key](../foreignkeys.md#parentchild) definition and the blob is being opened for read/write access.

Unless it returns SQLITE_MISUSE, this function sets the [database connection](../c3ref/sqlite3.md) error code and message accessible via [sqlite3_errcode()](../c3ref/errcode.md) and [sqlite3_errmsg()](../c3ref/errcode.md) and related functions.

A BLOB referenced by sqlite3_blob_open() may be read using the [sqlite3_blob_read()](../c3ref/blob_read.md) interface and modified by using [sqlite3_blob_write()](../c3ref/blob_write.md). The [BLOB handle](../c3ref/blob.md) can be moved to a different row of the same table using the [sqlite3_blob_reopen()](../c3ref/blob_reopen.md) interface. However, the column, table, or database of a [BLOB handle](../c3ref/blob.md) cannot be changed after the [BLOB handle](../c3ref/blob.md) is opened.

If the row that a BLOB handle points to is modified by an [UPDATE](../lang_update.md), [DELETE](../lang_delete.md), or by [ON CONFLICT](../lang_conflict.md) side-effects then the BLOB handle is marked as "expired". This is true if any column of the row is changed, even a column other than the one the BLOB handle is open on. Calls to [sqlite3_blob_read()](../c3ref/blob_read.md) and [sqlite3_blob_write()](../c3ref/blob_write.md) for an expired BLOB handle fail with a return code of [SQLITE_ABORT](../rescode.md#abort). Changes written into a BLOB prior to the BLOB expiring are not rolled back by the expiration of the BLOB. Such changes will eventually commit if the transaction continues to completion.

Use the [sqlite3_blob_bytes()](../c3ref/blob_bytes.md) interface to determine the size of the opened blob. The size of a blob may not be changed by this interface. Use the [UPDATE](../lang_update.md) SQL command to change the size of a blob.

The [sqlite3_bind_zeroblob()](../c3ref/bind_blob.md) and [sqlite3_result_zeroblob()](../c3ref/result_blob.md) interfaces and the built-in [zeroblob](../lang_corefunc.md#zeroblob) SQL function may be used to create a zero-filled blob to read or write using the incremental-blob interface.

To avoid a resource leak, every open [BLOB handle](../c3ref/blob.md) should eventually be released by a call to [sqlite3_blob_close()](../c3ref/blob_close.md).

See also: [sqlite3_blob_close()](../c3ref/blob_close.md), [sqlite3_blob_reopen()](../c3ref/blob_reopen.md), [sqlite3_blob_read()](../c3ref/blob_read.md), [sqlite3_blob_bytes()](../c3ref/blob_bytes.md), [sqlite3_blob_write()](../c3ref/blob_write.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
