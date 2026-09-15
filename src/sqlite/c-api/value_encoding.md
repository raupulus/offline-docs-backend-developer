---
title: Report the internal text encoding state of an sqlite3_value object
source_url: https://www.sqlite.org/c3ref/value_encoding.html
source_path: c3ref/value_encoding.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2200
---

> \
> int sqlite3_value_encoding(sqlite3_value\*);\

The sqlite3_value_encoding(X) interface returns one of [SQLITE_UTF8](../c3ref/c_any.md#sqliteutf8), [SQLITE_UTF16BE](../c3ref/c_any.md#sqliteutf16be), or [SQLITE_UTF16LE](../c3ref/c_any.md#sqliteutf16le) according to the current text encoding of the value X, assuming that X has type TEXT. If sqlite3_value_type(X) returns something other than SQLITE_TEXT, then the return value from sqlite3_value_encoding(X) is meaningless. Calls to [sqlite3_value_text(X)](../c3ref/value_blob.md), [sqlite3_value_text16(X)](../c3ref/value_blob.md), [sqlite3_value_text16be(X)](../c3ref/value_blob.md), [sqlite3_value_text16le(X)](../c3ref/value_blob.md), [sqlite3_value_bytes(X)](../c3ref/value_blob.md), or [sqlite3_value_bytes16(X)](../c3ref/value_blob.md) might change the encoding of the value X and thus change the return from subsequent calls to sqlite3_value_encoding(X).

This routine is intended for used by applications that test and validate the SQLite implementation. This routine is inquiring about the opaque internal state of an [sqlite3_value](../c3ref/value.md) object. Ordinary applications should not need to know what the internal state of an sqlite3_value object is and hence should not need to use this interface.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
