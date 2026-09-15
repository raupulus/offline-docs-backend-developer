---
title: Binding Values To Prepared Statements
source_url: https://www.sqlite.org/c3ref/bind_blob.html
source_path: c3ref/bind_blob.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 270
---

> \
> int sqlite3_bind_blob(sqlite3_stmt\*, int, const void\*, int n, void(\*)(void\*));\
> int sqlite3_bind_blob64(sqlite3_stmt\*, int, const void\*, sqlite3_uint64,\
>                         void(\*)(void\*));\
> int sqlite3_bind_double(sqlite3_stmt\*, int, double);\
> int sqlite3_bind_int(sqlite3_stmt\*, int, int);\
> int sqlite3_bind_int64(sqlite3_stmt\*, int, sqlite3_int64);\
> int sqlite3_bind_null(sqlite3_stmt\*, int);\
> int sqlite3_bind_text(sqlite3_stmt\*,int,const char\*,int,void(\*)(void\*));\
> int sqlite3_bind_text16(sqlite3_stmt\*, int, const void\*, int, void(\*)(void\*));\
> int sqlite3_bind_text64(sqlite3_stmt\*, int, const char\*, sqlite3_uint64,\
>                          void(\*)(void\*), unsigned char encoding);\
> int sqlite3_bind_value(sqlite3_stmt\*, int, const sqlite3_value\*);\
> int sqlite3_bind_pointer(sqlite3_stmt\*, int, void\*, const char\*,void(\*)(void\*));\
> int sqlite3_bind_zeroblob(sqlite3_stmt\*, int, int n);\
> int sqlite3_bind_zeroblob64(sqlite3_stmt\*, int, sqlite3_uint64);\

In the SQL statement text input to [sqlite3_prepare_v2()](../c3ref/prepare.md) and its variants, literals may be replaced by a [parameter](../lang_expr.md#varparam) that matches one of the following templates:

- ?
- ?NNN
- :VVV
- @VVV
- \$VVV

In the templates above, NNN represents an integer literal, and VVV represents an alphanumeric identifier. The values of these parameters (also called "host parameter names" or "SQL parameters") can be set using the sqlite3_bind\_\*() routines defined here.

The first argument to the sqlite3_bind\_\*() routines is always a pointer to the [sqlite3_stmt](../c3ref/stmt.md) object returned from [sqlite3_prepare_v2()](../c3ref/prepare.md) or its variants.

The second argument is the index of the SQL parameter to be set. The leftmost SQL parameter has an index of 1. When the same named SQL parameter is used more than once, second and subsequent occurrences have the same index as the first occurrence. The index for named parameters can be looked up using the [sqlite3_bind_parameter_index()](../c3ref/bind_parameter_index.md) API if desired. The index for "?NNN" parameters is the value of NNN. The NNN value must be between 1 and the [sqlite3_limit()](../c3ref/limit.md) parameter [SQLITE_LIMIT_VARIABLE_NUMBER](../c3ref/c_limit_attached.md#sqlitelimitvariablenumber) (default value: 32766).

The third argument is the value to bind to the parameter. If the third parameter to sqlite3_bind_text() or sqlite3_bind_text16() or sqlite3_bind_blob() is a NULL pointer then the fourth parameter is ignored and the end result is the same as sqlite3_bind_null(). If the third parameter to sqlite3_bind_text() is not NULL, then it should be a pointer to well-formed UTF8 text. If the third parameter to sqlite3_bind_text16() is not NULL, then it should be a pointer to well-formed UTF16 text. If the third parameter to sqlite3_bind_text64() is not NULL, then it should be a pointer to a well-formed unicode string that is either UTF8 if the sixth parameter is SQLITE_UTF8 or SQLITE_UTF8_ZT, or UTF16 otherwise.

<span id="byteorderdeterminationrules"></span> The byte-order of UTF16 input text is determined by the byte-order mark (BOM, U+FEFF) found in the first character, which is removed, or in the absence of a BOM the byte order is the native byte order of the host machine for sqlite3_bind_text16() or the byte order specified in the 6th parameter for sqlite3_bind_text64(). If UTF16 input text contains invalid unicode characters, then SQLite might change those invalid characters into the unicode replacement character: U+FFFD.

In those routines that have a fourth argument, its value is the number of bytes in the parameter. To be clear: the value is the number of <u>bytes</u> in the value, not the number of characters. If the fourth parameter to sqlite3_bind_text() or sqlite3_bind_text16() is negative, then the length of the string is the number of bytes up to the first zero terminator. If the fourth parameter to sqlite3_bind_blob() is negative, then the behavior is undefined. If a non-negative fourth parameter is provided to sqlite3_bind_text() or sqlite3_bind_text16() or sqlite3_bind_text64() then that parameter must be the byte offset where the NUL terminator would occur assuming the string were NUL terminated. If any NUL characters occur at byte offsets less than the value of the fourth parameter then the resulting string value will contain embedded NULs. The result of expressions involving strings with embedded NULs is undefined.

The fifth argument to the BLOB and string binding interfaces controls or indicates the lifetime of the object referenced by the third parameter. These three options exist: (1) A destructor to dispose of the BLOB or string after SQLite has finished with it may be passed. It is called to dispose of the BLOB or string even if the call to the bind API fails, except the destructor is not called if the third parameter is a NULL pointer or the fourth parameter is negative. (2) The special constant, [SQLITE_STATIC](../c3ref/c_static.md), may be passed to indicate that the application remains responsible for disposing of the object. In this case, the object and the provided pointer to it must remain valid until either the prepared statement is finalized or the same SQL parameter is bound to something else, whichever occurs sooner. (3) The constant, [SQLITE_TRANSIENT](../c3ref/c_static.md), may be passed to indicate that the object is to be copied prior to the return from sqlite3_bind\_\*(). The object and pointer to it must remain valid until then. SQLite will then manage the lifetime of its private copy.

The sixth argument (the E argument) to sqlite3_bind_text64(S,K,Z,N,D,E) must be one of [SQLITE_UTF8](../c3ref/c_any.md#sqliteutf8), [SQLITE_UTF8_ZT](../c3ref/c_any.md#sqliteutf8zt), [SQLITE_UTF16](../c3ref/c_any.md#sqliteutf16), [SQLITE_UTF16BE](../c3ref/c_any.md#sqliteutf16be), or [SQLITE_UTF16LE](../c3ref/c_any.md#sqliteutf16le) to specify the encoding of the text in the third parameter, Z. The special value [SQLITE_UTF8_ZT](../c3ref/c_any.md#sqliteutf8zt) means that the string argument is both UTF-8 encoded and is zero-terminated. In other words, SQLITE_UTF8_ZT means that the Z array is allocated to hold at least N+1 bytes and that the Z\[N\] byte is zero. If the E argument to sqlite3_bind_text64(S,K,Z,N,D,E) is not one of the allowed values shown above, or if the text encoding is different from the encoding specified by the sixth parameter, then the behavior is undefined.

The sqlite3_bind_zeroblob() routine binds a BLOB of length N that is filled with zeroes. A zeroblob uses a fixed amount of memory (just an integer to hold its size) while it is being processed. Zeroblobs are intended to serve as placeholders for BLOBs whose content is later written using [incremental BLOB I/O](../c3ref/blob_open.md) routines. A negative value for the zeroblob results in a zero-length BLOB.

The sqlite3_bind_pointer(S,I,P,T,D) routine causes the I-th parameter in [prepared statement](../c3ref/stmt.md) S to have an SQL value of NULL, but to also be associated with the pointer P of type T. D is either a NULL pointer or a pointer to a destructor function for P. SQLite will invoke the destructor D with a single argument of P when it is finished using P, even if the call to sqlite3_bind_pointer() fails. Due to a historical design quirk, results are undefined if D is SQLITE_TRANSIENT. The T parameter should be a static string, preferably a string literal. The sqlite3_bind_pointer() routine is part of the [pointer passing interface](../bindptr.md) added for SQLite 3.20.0.

If any of the sqlite3_bind\_\*() routines are called with a NULL pointer for the [prepared statement](../c3ref/stmt.md) or with a prepared statement for which [sqlite3_step()](../c3ref/step.md) has been called more recently than [sqlite3_reset()](../c3ref/reset.md), then the call will return [SQLITE_MISUSE](../rescode.md#misuse). If any sqlite3_bind\_() routine is passed a [prepared statement](../c3ref/stmt.md) that has been finalized, the result is undefined and probably harmful.

Bindings are not cleared by the [sqlite3_reset()](../c3ref/reset.md) routine. Unbound parameters are interpreted as NULL.

The sqlite3_bind\_\* routines return [SQLITE_OK](../rescode.md#ok) on success or an [error code](../rescode.md) if anything goes wrong. [SQLITE_TOOBIG](../rescode.md#toobig) might be returned if the size of a string or BLOB exceeds limits imposed by [sqlite3_limit](../c3ref/limit.md)([SQLITE_LIMIT_LENGTH](../c3ref/c_limit_attached.md#sqlitelimitlength)) or [SQLITE_MAX_LENGTH](../limits.md#max_length). [SQLITE_RANGE](../rescode.md#range) is returned if the parameter index is out of range. [SQLITE_NOMEM](../rescode.md#nomem) is returned if malloc() fails.

See also: [sqlite3_bind_parameter_count()](../c3ref/bind_parameter_count.md), [sqlite3_bind_parameter_name()](../c3ref/bind_parameter_name.md), and [sqlite3_bind_parameter_index()](../c3ref/bind_parameter_index.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
