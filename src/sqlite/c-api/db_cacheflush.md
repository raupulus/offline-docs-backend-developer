---
title: Flush caches to disk mid-transaction
source_url: https://www.sqlite.org/c3ref/db_cacheflush.html
source_path: c3ref/db_cacheflush.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1050
---

> \
> int sqlite3_db_cacheflush(sqlite3\*);\

If a write-transaction is open on [database connection](../c3ref/sqlite3.md) D when the [sqlite3_db_cacheflush(D)](../c3ref/db_cacheflush.md) interface is invoked, any dirty pages in the pager-cache that are not currently in use are written out to disk. A dirty page may be in use if a database cursor created by an active SQL statement is reading from it, or if it is page 1 of a database file (page 1 is always "in use"). The [sqlite3_db_cacheflush(D)](../c3ref/db_cacheflush.md) interface flushes caches for all schemas - "main", "temp", and any [attached](../lang_attach.md) databases.

If this function needs to obtain extra database locks before dirty pages can be flushed to disk, it does so. If those locks cannot be obtained immediately and there is a busy-handler callback configured, it is invoked in the usual manner. If the required lock still cannot be obtained, then the database is skipped and an attempt made to flush any dirty pages belonging to the next (if any) database. If any databases are skipped because locks cannot be obtained, but no other error occurs, this function returns SQLITE_BUSY.

If any other error occurs while flushing dirty pages to disk (for example an IO error or out-of-memory condition), then processing is abandoned and an SQLite [error code](../rescode.md) is returned to the caller immediately.

Otherwise, if no error occurs, [sqlite3_db_cacheflush()](../c3ref/db_cacheflush.md) returns SQLITE_OK.

This function does not set the database handle error code or message returned by the [sqlite3_errcode()](../c3ref/errcode.md) and [sqlite3_errmsg()](../c3ref/errcode.md) functions.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
