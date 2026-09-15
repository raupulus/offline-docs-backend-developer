---
title: A Handle To An Open BLOB
source_url: https://www.sqlite.org/c3ref/blob.html
source_path: c3ref/blob.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 310
---

> \
> typedef struct sqlite3_blob sqlite3_blob;\

An instance of this object represents an open BLOB on which [incremental BLOB I/O](../c3ref/blob_open.md) can be performed. Objects of this type are created by [sqlite3_blob_open()](../c3ref/blob_open.md) and destroyed by [sqlite3_blob_close()](../c3ref/blob_close.md). The [sqlite3_blob_read()](../c3ref/blob_read.md) and [sqlite3_blob_write()](../c3ref/blob_write.md) interfaces can be used to read or write small subsections of the BLOB. The [sqlite3_blob_bytes()](../c3ref/blob_bytes.md) interface returns the size of the BLOB in bytes.

1 Constructor using this object: [sqlite3_blob_open()](../c3ref/blob_open.md)

1 Destructor using this object: [sqlite3_blob_close()](../c3ref/blob_close.md)

4 Methods using this object: [sqlite3_blob_bytes()](../c3ref/blob_bytes.md), [sqlite3_blob_read()](../c3ref/blob_read.md), [sqlite3_blob_reopen()](../c3ref/blob_reopen.md), [sqlite3_blob_write()](../c3ref/blob_write.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
