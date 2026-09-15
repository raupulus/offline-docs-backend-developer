---
title: Result Values From A Query
source_url: https://www.sqlite.org/c3ref/column_blob.html
source_path: c3ref/column_blob.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 860
---

> \
> const void \*sqlite3_column_blob(sqlite3_stmt\*, int iCol);\
> double sqlite3_column_double(sqlite3_stmt\*, int iCol);\
> int sqlite3_column_int(sqlite3_stmt\*, int iCol);\
> sqlite3_int64 sqlite3_column_int64(sqlite3_stmt\*, int iCol);\
> const unsigned char \*sqlite3_column_text(sqlite3_stmt\*, int iCol);\
> const void \*sqlite3_column_text16(sqlite3_stmt\*, int iCol);\
> sqlite3_value \*sqlite3_column_value(sqlite3_stmt\*, int iCol);\
> int sqlite3_column_bytes(sqlite3_stmt\*, int iCol);\
> int sqlite3_column_bytes16(sqlite3_stmt\*, int iCol);\
> int sqlite3_column_type(sqlite3_stmt\*, int iCol);\

**Summary:**

> **sqlite3_column_blob**
>
> →
>
> BLOB result
>
> **sqlite3_column_double**
>
> →
>
> REAL result
>
> **sqlite3_column_int**
>
> →
>
> 32-bit INTEGER result
>
> **sqlite3_column_int64**
>
> →
>
> 64-bit INTEGER result
>
> **sqlite3_column_text**
>
> →
>
> UTF-8 TEXT result
>
> **sqlite3_column_text16**
>
> →
>
> UTF-16 TEXT result
>
> **sqlite3_column_value**
>
> →
>
> The result as an [unprotected sqlite3_value](../c3ref/value.md) object.
>
>  
>
>  
>
>  
>
> **sqlite3_column_bytes**
>
> →
>
> Size of a BLOB or a UTF-8 TEXT result in bytes
>
> **sqlite3_column_bytes16  **
>
> →  
>
> Size of UTF-16 TEXT in bytes
>
> **sqlite3_column_type**
>
> →
>
> Default datatype of the result

**Details:**

These routines return information about a single column of the current result row of a query. In every case the first argument is a pointer to the [prepared statement](../c3ref/stmt.md) that is being evaluated (the [sqlite3_stmt\*](../c3ref/stmt.md) that was returned from [sqlite3_prepare_v2()](../c3ref/prepare.md) or one of its variants) and the second argument is the index of the column for which information should be returned. The leftmost column of the result set has the index 0. The number of columns in the result can be determined using [sqlite3_column_count()](../c3ref/column_count.md).

If the SQL statement does not currently point to a valid row, or if the column index is out of range, the result is undefined. These routines may only be called when the most recent call to [sqlite3_step()](../c3ref/step.md) has returned [SQLITE_ROW](../rescode.md#row) and neither [sqlite3_reset()](../c3ref/reset.md) nor [sqlite3_finalize()](../c3ref/finalize.md) have been called subsequently. If any of these routines are called after [sqlite3_reset()](../c3ref/reset.md) or [sqlite3_finalize()](../c3ref/finalize.md) or after [sqlite3_step()](../c3ref/step.md) has returned something other than [SQLITE_ROW](../rescode.md#row), the results are undefined. If [sqlite3_step()](../c3ref/step.md) or [sqlite3_reset()](../c3ref/reset.md) or [sqlite3_finalize()](../c3ref/finalize.md) are called from a different thread while any of these routines are pending, then the results are undefined.

The first six interfaces (\_blob, \_double, \_int, \_int64, \_text, and \_text16) each return the value of a result column in a specific data format. If the result column is not initially in the requested format (for example, if the query returns an integer but the sqlite3_column_text() interface is used to extract the value) then an automatic type conversion is performed.

The sqlite3_column_type() routine returns the [datatype code](../c3ref/c_blob.md) for the initial data type of the result column. The returned value is one of [SQLITE_INTEGER](../c3ref/c_blob.md), [SQLITE_FLOAT](../c3ref/c_blob.md), [SQLITE_TEXT](../c3ref/c_blob.md), [SQLITE_BLOB](../c3ref/c_blob.md), or [SQLITE_NULL](../c3ref/c_blob.md). The return value of sqlite3_column_type() can be used to decide which of the first six interface should be used to extract the column value. The value returned by sqlite3_column_type() is only meaningful if no automatic type conversions have occurred for the value in question. After a type conversion, the result of calling sqlite3_column_type() is undefined, though harmless. Future versions of SQLite may change the behavior of sqlite3_column_type() following a type conversion.

If the result is a BLOB or a TEXT string, then the sqlite3_column_bytes() or sqlite3_column_bytes16() interfaces can be used to determine the size of that BLOB or string.

If the result is a BLOB or UTF-8 string then the sqlite3_column_bytes() routine returns the number of bytes in that BLOB or string. If the result is a UTF-16 string, then sqlite3_column_bytes() converts the string to UTF-8 and then returns the number of bytes. If the result is a numeric value then sqlite3_column_bytes() uses [sqlite3_snprintf()](../c3ref/mprintf.md) to convert that value to a UTF-8 string and returns the number of bytes in that string. If the result is NULL, then sqlite3_column_bytes() returns zero.

If the result is a BLOB or UTF-16 string then the sqlite3_column_bytes16() routine returns the number of bytes in that BLOB or string. If the result is a UTF-8 string, then sqlite3_column_bytes16() converts the string to UTF-16 and then returns the number of bytes. If the result is a numeric value then sqlite3_column_bytes16() uses [sqlite3_snprintf()](../c3ref/mprintf.md) to convert that value to a UTF-16 string and returns the number of bytes in that string. If the result is NULL, then sqlite3_column_bytes16() returns zero.

The values returned by [sqlite3_column_bytes()](../c3ref/column_blob.md) and [sqlite3_column_bytes16()](../c3ref/column_blob.md) do not include the zero terminators at the end of the string. For clarity: the values returned by [sqlite3_column_bytes()](../c3ref/column_blob.md) and [sqlite3_column_bytes16()](../c3ref/column_blob.md) are the number of bytes in the string, not the number of characters.

Strings returned by sqlite3_column_text() and sqlite3_column_text16(), even empty strings, are always zero-terminated. The return value from sqlite3_column_blob() for a zero-length BLOB is a NULL pointer.

Strings returned by sqlite3_column_text16() always have the endianness which is native to the platform, regardless of the text encoding set for the database.

**Warning:** The object returned by [sqlite3_column_value()](../c3ref/column_blob.md) is an [unprotected sqlite3_value](../c3ref/value.md) object. In a multithreaded environment, an unprotected sqlite3_value object may only be used safely with [sqlite3_bind_value()](../c3ref/bind_blob.md) and [sqlite3_result_value()](../c3ref/result_blob.md). If the [unprotected sqlite3_value](../c3ref/value.md) object returned by [sqlite3_column_value()](../c3ref/column_blob.md) is used in any other way, including calls to routines like [sqlite3_value_int()](../c3ref/value_blob.md), [sqlite3_value_text()](../c3ref/value_blob.md), or [sqlite3_value_bytes()](../c3ref/value_blob.md), the behavior is not threadsafe. Hence, the sqlite3_column_value() interface is normally only useful within the implementation of [application-defined SQL functions](../appfunc.md) or [virtual tables](../vtab.md), not within top-level application code.

These routines may attempt to convert the datatype of the result. For example, if the internal representation is FLOAT and a text result is requested, [sqlite3_snprintf()](../c3ref/mprintf.md) is used internally to perform the conversion automatically. The following table details the conversions that are applied:

> Internal\
> Type
>
> Requested\
> Type
>
> Conversion
>
> NULL
>
> INTEGER
>
> Result is 0
>
> NULL
>
> FLOAT
>
> Result is 0.0
>
> NULL
>
> TEXT
>
> Result is a NULL pointer
>
> NULL
>
> BLOB
>
> Result is a NULL pointer
>
> INTEGER
>
> FLOAT
>
> Convert from integer to float
>
> INTEGER
>
> TEXT
>
> ASCII rendering of the integer
>
> INTEGER
>
> BLOB
>
> Same as INTEGER-\>TEXT
>
> FLOAT
>
> INTEGER
>
> [CAST](../lang_expr.md#castexpr) to INTEGER
>
> FLOAT
>
> TEXT
>
> ASCII rendering of the float
>
> FLOAT
>
> BLOB
>
> [CAST](../lang_expr.md#castexpr) to BLOB
>
> TEXT
>
> INTEGER
>
> [CAST](../lang_expr.md#castexpr) to INTEGER
>
> TEXT
>
> FLOAT
>
> [CAST](../lang_expr.md#castexpr) to REAL
>
> TEXT
>
> BLOB
>
> No change
>
> BLOB
>
> INTEGER
>
> [CAST](../lang_expr.md#castexpr) to INTEGER
>
> BLOB
>
> FLOAT
>
> [CAST](../lang_expr.md#castexpr) to REAL
>
> BLOB
>
> TEXT
>
> [CAST](../lang_expr.md#castexpr) to TEXT, ensure zero terminator

Note that when type conversions occur, pointers returned by prior calls to sqlite3_column_blob(), sqlite3_column_text(), and/or sqlite3_column_text16() may be invalidated. Type conversions and pointer invalidations might occur in the following cases:

- The initial content is a BLOB and sqlite3_column_text() or sqlite3_column_text16() is called. A zero-terminator might need to be added to the string.
- The initial content is UTF-8 text and sqlite3_column_bytes16() or sqlite3_column_text16() is called. The content must be converted to UTF-16.
- The initial content is UTF-16 text and sqlite3_column_bytes() or sqlite3_column_text() is called. The content must be converted to UTF-8.

Conversions between UTF-16be and UTF-16le are always done in place and do not invalidate a prior pointer, though of course the content of the buffer that the prior pointer references will have been modified. Other kinds of conversion are done in place when it is possible, but sometimes they are not possible and in those cases prior pointers are invalidated.

The safest policy is to invoke these routines in one of the following ways:

- sqlite3_column_text() followed by sqlite3_column_bytes()
- sqlite3_column_blob() followed by sqlite3_column_bytes()
- sqlite3_column_text16() followed by sqlite3_column_bytes16()

In other words, you should call sqlite3_column_text(), sqlite3_column_blob(), or sqlite3_column_text16() first to force the result into the desired format, then invoke sqlite3_column_bytes() or sqlite3_column_bytes16() to find the size of the result. Do not mix calls to sqlite3_column_text() or sqlite3_column_blob() with calls to sqlite3_column_bytes16(), and do not mix calls to sqlite3_column_text16() with calls to sqlite3_column_bytes().

The pointers returned are valid until a type conversion occurs as described above, or until [sqlite3_step()](../c3ref/step.md) or [sqlite3_reset()](../c3ref/reset.md) or [sqlite3_finalize()](../c3ref/finalize.md) is called. The memory space used to hold strings and BLOBs is freed automatically. Do not pass the pointers returned from [sqlite3_column_blob()](../c3ref/column_blob.md), [sqlite3_column_text()](../c3ref/column_blob.md), etc. into [sqlite3_free()](../c3ref/free.md).

As long as the input parameters are correct, these routines will only fail if an out-of-memory error occurs during a format conversion. Only the following subset of interfaces are subject to out-of-memory errors:

- sqlite3_column_blob()
- sqlite3_column_text()
- sqlite3_column_text16()
- sqlite3_column_bytes()
- sqlite3_column_bytes16()

If an out-of-memory error occurs, then the return value from these routines is the same as if the column had contained an SQL NULL value. Valid SQL NULL returns can be distinguished from out-of-memory errors by invoking the [sqlite3_errcode()](../c3ref/errcode.md) immediately after the suspect return value is obtained and before any other SQLite interface is called on the same [database connection](../c3ref/sqlite3.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
