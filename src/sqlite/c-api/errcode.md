---
title: Error Codes And Messages
source_url: https://www.sqlite.org/c3ref/errcode.html
source_path: c3ref/errcode.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1190
---

> \
> int sqlite3_errcode(sqlite3 \*db);\
> int sqlite3_extended_errcode(sqlite3 \*db);\
> const char \*sqlite3_errmsg(sqlite3\*);\
> const void \*sqlite3_errmsg16(sqlite3\*);\
> const char \*sqlite3_errstr(int);\
> int sqlite3_error_offset(sqlite3 \*db);\

If the most recent sqlite3\_\* API call associated with [database connection](../c3ref/sqlite3.md) D failed, then the sqlite3_errcode(D) interface returns the numeric [result code](../rescode.md) or [extended result code](../rescode.md#extrc) for that API call. The sqlite3_extended_errcode() interface is the same except that it always returns the [extended result code](../rescode.md#extrc) even when extended result codes are disabled.

The values returned by sqlite3_errcode() and/or sqlite3_extended_errcode() might change with each API call. Except, there are some interfaces that are guaranteed to never change the value of the error code. The error-code preserving interfaces include the following:

- sqlite3_errcode()
- sqlite3_extended_errcode()
- sqlite3_errmsg()
- sqlite3_errmsg16()
- sqlite3_error_offset()
- sqlite3_db_handle()

The sqlite3_errmsg() and sqlite3_errmsg16() return English-language text that describes the error, as either UTF-8 or UTF-16 respectively, or NULL if no error message is available. (See how SQLite handles [invalid UTF](../invalidutf.md) for exceptions to this rule.) Memory to hold the error message string is managed internally. The application does not need to worry about freeing the result. However, the error string might be overwritten or deallocated by subsequent calls to other SQLite interface functions.

The sqlite3_errstr(E) interface returns the English-language text that describes the [result code](../rescode.md) E, as UTF-8, or NULL if E is not a result code for which a text error message is available. Memory to hold the error message string is managed internally and must not be freed by the application.

If the most recent error references a specific token in the input SQL, the sqlite3_error_offset() interface returns the byte offset of the start of that token. The byte offset returned by sqlite3_error_offset() assumes that the input SQL is UTF-8. If the most recent error does not reference a specific token in the input SQL, then the sqlite3_error_offset() function returns -1.

When the serialized [threading mode](../threadsafe.md) is in use, it might be the case that a second error occurs on a separate thread in between the time of the first error and the call to these interfaces. When that happens, the second error will be reported since these interfaces always report the most recent result. To avoid this, each thread can obtain exclusive use of the [database connection](../c3ref/sqlite3.md) D by invoking [sqlite3_mutex_enter](../c3ref/mutex_alloc.md)([sqlite3_db_mutex](../c3ref/db_mutex.md)(D)) before beginning to use D and invoking [sqlite3_mutex_leave](../c3ref/mutex_alloc.md)([sqlite3_db_mutex](../c3ref/db_mutex.md)(D)) after all calls to the interfaces listed here are completed.

If an interface fails with SQLITE_MISUSE, that means the interface was invoked incorrectly by the application. In that case, the error code and message may or may not be set.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
