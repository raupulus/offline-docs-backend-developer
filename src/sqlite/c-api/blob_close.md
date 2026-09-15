---
title: Close A BLOB Handle
source_url: https://www.sqlite.org/c3ref/blob_close.html
source_path: c3ref/blob_close.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 330
---

> \
> int sqlite3_blob_close(sqlite3_blob \*);\

This function closes an open [BLOB handle](../c3ref/blob.md). The BLOB handle is closed unconditionally. Even if this routine returns an error code, the handle is still closed.

If the blob handle being closed was opened for read-write access, and if the database is in auto-commit mode and there are no other open read-write blob handles or active write statements, the current transaction is committed. If an error occurs while committing the transaction, an error code is returned and the transaction rolled back.

Calling this function with an argument that is not a NULL pointer or an open blob handle results in undefined behavior. Calling this routine with a null pointer (such as would be returned by a failed call to [sqlite3_blob_open()](../c3ref/blob_open.md)) is a harmless no-op. Otherwise, if this function is passed a valid open blob handle, the values returned by the sqlite3_errcode() and sqlite3_errmsg() functions are set before returning.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
