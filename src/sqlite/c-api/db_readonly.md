---
title: Determine if a database is read-only
source_url: https://www.sqlite.org/c3ref/db_readonly.html
source_path: c3ref/db_readonly.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1110
---

> \
> int sqlite3_db_readonly(sqlite3 \*db, const char \*zDbName);\

The sqlite3_db_readonly(D,N) interface returns 1 if the database N of connection D is read-only, 0 if it is read/write, or -1 if N is not the name of a database on connection D.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
