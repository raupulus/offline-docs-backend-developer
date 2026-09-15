---
title: Find The Database Handle Of A Prepared Statement
source_url: https://www.sqlite.org/c3ref/db_handle.html
source_path: c3ref/db_handle.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1080
---

> \
> sqlite3 \*sqlite3_db_handle(sqlite3_stmt\*);\

The sqlite3_db_handle interface returns the [database connection](../c3ref/sqlite3.md) handle to which a [prepared statement](../c3ref/stmt.md) belongs. The [database connection](../c3ref/sqlite3.md) returned by sqlite3_db_handle is the same [database connection](../c3ref/sqlite3.md) that was the first argument to the [sqlite3_prepare_v2()](../c3ref/prepare.md) call (or its variants) that was used to create the statement in the first place.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
