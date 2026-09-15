---
title: Status Of A Dynamic String
source_url: https://www.sqlite.org/c3ref/str_errcode.html
source_path: c3ref/str_errcode.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1990
---

> \
> int sqlite3_str_errcode(sqlite3_str\*);\
> int sqlite3_str_length(sqlite3_str\*);\
> char \*sqlite3_str_value(sqlite3_str\*);\

These interfaces return the current status of an [sqlite3_str](../c3ref/str.md) object.

If any prior errors have occurred while constructing the dynamic string in sqlite3_str X, then the [sqlite3_str_errcode(X)](../c3ref/str_errcode.md) method will return an appropriate error code. The [sqlite3_str_errcode(X)](../c3ref/str_errcode.md) method returns [SQLITE_NOMEM](../rescode.md#nomem) following any out-of-memory error, or [SQLITE_TOOBIG](../rescode.md#toobig) if the size of the dynamic string exceeds [SQLITE_MAX_LENGTH](../limits.md#max_length), or [SQLITE_OK](../rescode.md#ok) if there have been no errors.

The [sqlite3_str_length(X)](../c3ref/str_errcode.md) method returns the current length, in bytes, of the dynamic string under construction in [sqlite3_str](../c3ref/str.md) object X. The length returned by [sqlite3_str_length(X)](../c3ref/str_errcode.md) does not include the zero-termination byte.

The [sqlite3_str_value(X)](../c3ref/str_errcode.md) method returns a pointer to the current content of the dynamic string under construction in X. The value returned by [sqlite3_str_value(X)](../c3ref/str_errcode.md) is managed by the sqlite3_str object X and might be freed or altered by any subsequent method on the same [sqlite3_str](../c3ref/str.md) object. Applications must not use the pointer returned by [sqlite3_str_value(X)](../c3ref/str_errcode.md) after any subsequent method call on the same object. Applications may change the content of the string returned by [sqlite3_str_value(X)](../c3ref/str_errcode.md) as long as they do not write into any bytes outside the range of 0 to [sqlite3_str_length(X)](../c3ref/str_errcode.md) and do not read or write any byte after any subsequent sqlite3_str method call.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
