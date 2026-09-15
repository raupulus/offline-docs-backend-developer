---
title: Translate filenames
source_url: https://www.sqlite.org/c3ref/filename_database.html
source_path: c3ref/filename_database.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1270
---

> \
> const char \*sqlite3_filename_database(sqlite3_filename);\
> const char \*sqlite3_filename_journal(sqlite3_filename);\
> const char \*sqlite3_filename_wal(sqlite3_filename);\

These routines are available to [custom VFS implementations](../vfs.md) for translating filenames between the main database file, the journal file, and the WAL file.

If F is the name of an sqlite database file, journal file, or WAL file passed by the SQLite core into the VFS, then sqlite3_filename_database(F) returns the name of the corresponding database file.

If F is the name of an sqlite database file, journal file, or WAL file passed by the SQLite core into the VFS, or if F is a database filename obtained from [sqlite3_db_filename()](../c3ref/db_filename.md), then sqlite3_filename_journal(F) returns the name of the corresponding rollback journal file.

If F is the name of an sqlite database file, journal file, or WAL file that was passed by the SQLite core into the VFS, or if F is a database filename obtained from [sqlite3_db_filename()](../c3ref/db_filename.md), then sqlite3_filename_wal(F) returns the name of the corresponding WAL file.

In all of the above, if F is not the name of a database, journal or WAL filename passed into the VFS from the SQLite core and F is not the return value from [sqlite3_db_filename()](../c3ref/db_filename.md), then the result is undefined and is likely a memory access violation.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
