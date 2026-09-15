---
title: Return The Size Of An Open BLOB
source_url: https://www.sqlite.org/c3ref/blob_bytes.html
source_path: c3ref/blob_bytes.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 320
---

> \
> int sqlite3_blob_bytes(sqlite3_blob \*);\

Returns the size in bytes of the BLOB accessible via the successfully opened [BLOB handle](../c3ref/blob.md) in its only argument. The incremental blob I/O routines can only read or overwrite existing blob content; they cannot change the size of a blob.

This routine only works on a [BLOB handle](../c3ref/blob.md) which has been created by a prior successful call to [sqlite3_blob_open()](../c3ref/blob_open.md) and which has not been closed by [sqlite3_blob_close()](../c3ref/blob_close.md). Passing any other pointer in to this routine results in undefined and probably undesirable behavior.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
