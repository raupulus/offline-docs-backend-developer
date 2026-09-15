---
title: Read Data From A BLOB Incrementally
source_url: https://www.sqlite.org/c3ref/blob_read.html
source_path: c3ref/blob_read.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 350
---

> \
> int sqlite3_blob_read(sqlite3_blob \*, void \*Z, int N, int iOffset);\

This function is used to read data from an open [BLOB handle](../c3ref/blob.md) into a caller-supplied buffer. N bytes of data are copied into buffer Z from the open BLOB, starting at offset iOffset.

If offset iOffset is less than N bytes from the end of the BLOB, [SQLITE_ERROR](../rescode.md#error) is returned and no data is read. If N or iOffset is less than zero, [SQLITE_ERROR](../rescode.md#error) is returned and no data is read. The size of the blob (and hence the maximum value of N+iOffset) can be determined using the [sqlite3_blob_bytes()](../c3ref/blob_bytes.md) interface.

An attempt to read from an expired [BLOB handle](../c3ref/blob.md) fails with an error code of [SQLITE_ABORT](../rescode.md#abort).

On success, sqlite3_blob_read() returns SQLITE_OK. Otherwise, an [error code](../rescode.md) or an [extended error code](../rescode.md#extrc) is returned.

This routine only works on a [BLOB handle](../c3ref/blob.md) which has been created by a prior successful call to [sqlite3_blob_open()](../c3ref/blob_open.md) and which has not been closed by [sqlite3_blob_close()](../c3ref/blob_close.md). Passing any other pointer in to this routine results in undefined and probably undesirable behavior.

See also: [sqlite3_blob_write()](../c3ref/blob_write.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
