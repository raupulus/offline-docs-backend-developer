---
title: Low-Level Control Of Database Files
source_url: https://www.sqlite.org/c3ref/file_control.html
source_path: c3ref/file_control.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1250
---

> \
> int sqlite3_file_control(sqlite3\*, const char \*zDbName, int op, void\*);\

The [sqlite3_file_control()](../c3ref/file_control.md) interface makes a direct call to the xFileControl method for the [sqlite3_io_methods](../c3ref/io_methods.md) object associated with a particular database identified by the second argument. The name of the database is "main" for the main database or "temp" for the TEMP database, or the name that appears after the AS keyword for databases that are added using the [ATTACH](../lang_attach.md) SQL command. A NULL pointer can be used in place of "main" to refer to the main database file. The third and fourth parameters to this routine are passed directly through to the second and third parameters of the xFileControl method. The return value of the xFileControl method becomes the return value of this routine.

A few opcodes for [sqlite3_file_control()](../c3ref/file_control.md) are handled directly by the SQLite core and never invoke the sqlite3_io_methods.xFileControl method. The [SQLITE_FCNTL_FILE_POINTER](../c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlfilepointer) value for the op parameter causes a pointer to the underlying [sqlite3_file](../c3ref/file.md) object to be written into the space pointed to by the 4th parameter. The [SQLITE_FCNTL_JOURNAL_POINTER](../c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntljournalpointer) works similarly except that it returns the [sqlite3_file](../c3ref/file.md) object associated with the journal file instead of the main database. The [SQLITE_FCNTL_VFS_POINTER](../c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlvfspointer) opcode returns a pointer to the underlying [sqlite3_vfs](../c3ref/vfs.md) object for the file. The [SQLITE_FCNTL_DATA_VERSION](../c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntldataversion) returns the data version counter from the pager.

If the second parameter (zDbName) does not match the name of any open database file, then SQLITE_ERROR is returned. This error code is not remembered and will not be recalled by [sqlite3_errcode()](../c3ref/errcode.md) or [sqlite3_errmsg()](../c3ref/errcode.md). The underlying xFileControl method might also return SQLITE_ERROR. There is no way to distinguish between an incorrect zDbName and an SQLITE_ERROR return from the underlying xFileControl method.

See also: [file control opcodes](../c3ref/c_fcntl_begin_atomic_write.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
