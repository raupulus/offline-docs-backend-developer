---
title: Set the Last Insert Rowid value.
source_url: https://www.sqlite.org/c3ref/set_last_insert_rowid.html
source_path: c3ref/set_last_insert_rowid.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1760
---

> \
> void sqlite3_set_last_insert_rowid(sqlite3\*,sqlite3_int64);\

The sqlite3_set_last_insert_rowid(D, R) method allows the application to set the value returned by calling sqlite3_last_insert_rowid(D) to R without inserting a row into the database.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
