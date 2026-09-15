---
title: Database File Corresponding To A Journal
source_url: https://www.sqlite.org/c3ref/database_file_object.html
source_path: c3ref/database_file_object.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1040
---

> \
> sqlite3_file \*sqlite3_database_file_object(const char\*);\

If X is the name of a rollback or WAL-mode journal file that is passed into the xOpen method of [sqlite3_vfs](../c3ref/vfs.md), then sqlite3_database_file_object(X) returns a pointer to the [sqlite3_file](../c3ref/file.md) object that represents the main database file.

This routine is intended for use in custom [VFS](../vfs.md) implementations only. It is not a general-purpose interface. The argument sqlite3_file_object(X) must be a filename pointer that has been passed into [sqlite3_vfs](../c3ref/vfs.md).xOpen method where the flags parameter to xOpen contains one of the bits [SQLITE_OPEN_MAIN_JOURNAL](../c3ref/c_open_autoproxy.md) or [SQLITE_OPEN_WAL](../c3ref/c_open_autoproxy.md). Any other use of this routine results in undefined and probably undesirable behavior.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
