---
title: Write Data Into A BLOB Incrementally
source_url: https://www.sqlite.org/c3ref/blob_write.html
source_path: c3ref/blob_write.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 370
---

> \
> int sqlite3_blob_write(sqlite3_blob \*, const void \*z, int n, int iOffset);\

This function is used to write data into an open [BLOB handle](../c3ref/blob.md) from a caller-supplied buffer. N bytes of data are copied from the buffer Z into the open BLOB, starting at offset iOffset.

On success, sqlite3_blob_write() returns SQLITE_OK. Otherwise, an [error code](../rescode.md) or an [extended error code](../rescode.md#extrc) is returned. Unless SQLITE_MISUSE is returned, this function sets the [database connection](../c3ref/sqlite3.md) error code and message accessible via [sqlite3_errcode()](../c3ref/errcode.md) and [sqlite3_errmsg()](../c3ref/errcode.md) and related functions.

If the [BLOB handle](../c3ref/blob.md) passed as the first argument was not opened for writing (the flags parameter to [sqlite3_blob_open()](../c3ref/blob_open.md) was zero), this function returns [SQLITE_READONLY](../rescode.md#readonly).

This function may only modify the contents of the BLOB; it is not possible to increase the size of a BLOB using this API. If offset iOffset is less than N bytes from the end of the BLOB, [SQLITE_ERROR](../rescode.md#error) is returned and no data is written. The size of the BLOB (and hence the maximum value of N+iOffset) can be determined using the [sqlite3_blob_bytes()](../c3ref/blob_bytes.md) interface. If N or iOffset are less than zero [SQLITE_ERROR](../rescode.md#error) is returned and no data is written.

An attempt to write to an expired [BLOB handle](../c3ref/blob.md) fails with an error code of [SQLITE_ABORT](../rescode.md#abort). Writes to the BLOB that occurred before the [BLOB handle](../c3ref/blob.md) expired are not rolled back by the expiration of the handle, though of course those changes might have been overwritten by the statement that expired the BLOB handle or by other independent statements.

This routine only works on a [BLOB handle](../c3ref/blob.md) which has been created by a prior successful call to [sqlite3_blob_open()](../c3ref/blob_open.md) and which has not been closed by [sqlite3_blob_close()](../c3ref/blob_close.md). Passing any other pointer in to this routine results in undefined and probably undesirable behavior.

See also: [sqlite3_blob_read()](../c3ref/blob_read.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
