---
title: File Name
source_url: https://www.sqlite.org/c3ref/filename.html
source_path: c3ref/filename.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1260
---

> \
> typedef const char \*sqlite3_filename;\

Type [sqlite3_filename](../c3ref/filename.md) is used by SQLite to pass filenames to the xOpen method of a [VFS](../vfs.md). It may be cast to (const char\*) and treated as a normal, nul-terminated, UTF-8 buffer containing the filename, but may also be passed to special APIs such as:

- sqlite3_filename_database()
- sqlite3_filename_journal()
- sqlite3_filename_wal()
- sqlite3_uri_parameter()
- sqlite3_uri_boolean()
- sqlite3_uri_int64()
- sqlite3_uri_key()

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
