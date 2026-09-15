---
title: Return The Filename For A Database Connection
source_url: https://www.sqlite.org/c3ref/db_filename.html
source_path: c3ref/db_filename.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1070
---

> \
> sqlite3_filename sqlite3_db_filename(sqlite3 \*db, const char \*zDbName);\

The sqlite3_db_filename(D,N) interface returns a pointer to the filename associated with database N of connection D. If there is no attached database N on the database connection D, or if database N is a temporary or in-memory database, then this function will return either a NULL pointer or an empty string.

The string value returned by this routine is owned and managed by the database connection. The value will be valid until the database N is [DETACH](../lang_detach.md)-ed or until the database connection closes.

The filename returned by this function is the output of the xFullPathname method of the [VFS](../vfs.md). In other words, the filename will be an absolute pathname, even if the filename used to open the database originally was a URI or relative pathname.

If the filename pointer returned by this routine is not NULL, then it can be used as the filename input parameter to these routines:

- [sqlite3_uri_parameter()](../c3ref/uri_boolean.md)
- [sqlite3_uri_boolean()](../c3ref/uri_boolean.md)
- [sqlite3_uri_int64()](../c3ref/uri_boolean.md)
- [sqlite3_filename_database()](../c3ref/filename_database.md)
- [sqlite3_filename_journal()](../c3ref/filename_database.md)
- [sqlite3_filename_wal()](../c3ref/filename_database.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
