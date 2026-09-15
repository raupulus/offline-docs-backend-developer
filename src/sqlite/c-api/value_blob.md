---
title: Obtaining SQL Values
source_url: https://www.sqlite.org/c3ref/value_blob.html
source_path: c3ref/value_blob.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2180
---

> \
> const void \*sqlite3_value_blob(sqlite3_value\*);\
> double sqlite3_value_double(sqlite3_value\*);\
> int sqlite3_value_int(sqlite3_value\*);\
> sqlite3_int64 sqlite3_value_int64(sqlite3_value\*);\
> void \*sqlite3_value_pointer(sqlite3_value\*, const char\*);\
> const unsigned char \*sqlite3_value_text(sqlite3_value\*);\
> const void \*sqlite3_value_text16(sqlite3_value\*);\
> const void \*sqlite3_value_text16le(sqlite3_value\*);\
> const void \*sqlite3_value_text16be(sqlite3_value\*);\
> int sqlite3_value_bytes(sqlite3_value\*);\
> int sqlite3_value_bytes16(sqlite3_value\*);\
> int sqlite3_value_type(sqlite3_value\*);\
> int sqlite3_value_numeric_type(sqlite3_value\*);\
> int sqlite3_value_nochange(sqlite3_value\*);\
> int sqlite3_value_frombind(sqlite3_value\*);\

**Summary:**

> **sqlite3_value_blob**
>
> →
>
> BLOB value
>
> **sqlite3_value_double**
>
> →
>
> REAL value
>
> **sqlite3_value_int**
>
> →
>
> 32-bit INTEGER value
>
> **sqlite3_value_int64**
>
> →
>
> 64-bit INTEGER value
>
> **sqlite3_value_pointer**
>
> →
>
> Pointer value
>
> **sqlite3_value_text**
>
> →
>
> UTF-8 TEXT value
>
> **sqlite3_value_text16**
>
> →
>
> UTF-16 TEXT value in the native byteorder
>
> **sqlite3_value_text16be**
>
> →
>
> UTF-16be TEXT value
>
> **sqlite3_value_text16le**
>
> →
>
> UTF-16le TEXT value
>
>  
>
>  
>
>  
>
> **sqlite3_value_bytes**
>
> →
>
> Size of a BLOB or a UTF-8 TEXT in bytes
>
> **sqlite3_value_bytes16  **
>
> →  
>
> Size of UTF-16 TEXT in bytes
>
> **sqlite3_value_type**
>
> →
>
> Default datatype of the value
>
> **sqlite3_value_numeric_type  **
>
> →  
>
> Best numeric datatype of the value
>
> **sqlite3_value_nochange  **
>
> →  
>
> True if the column is unchanged in an UPDATE against a virtual table.
>
> **sqlite3_value_frombind  **
>
> →  
>
> True if value originated from a [bound parameter](../lang_expr.md#varparam)

**Details:**

These routines extract type, size, and content information from [protected sqlite3_value](../c3ref/value.md) objects. Protected sqlite3_value objects are used to pass parameter information into the functions that implement [application-defined SQL functions](../appfunc.md) and [virtual tables](../vtab.md).

These routines work only with [protected sqlite3_value](../c3ref/value.md) objects. Any attempt to use these routines on an [unprotected sqlite3_value](../c3ref/value.md) is not threadsafe.

These routines work just like the corresponding [column access functions](../c3ref/column_blob.md) except that these routines take a single [protected sqlite3_value](../c3ref/value.md) object pointer instead of a [sqlite3_stmt\*](../c3ref/stmt.md) pointer and an integer column number.

The sqlite3_value_text16() interface extracts a UTF-16 string in the native byte-order of the host machine. The sqlite3_value_text16be() and sqlite3_value_text16le() interfaces extract UTF-16 strings as big-endian and little-endian respectively.

If [sqlite3_value](../c3ref/value.md) object V was initialized using [sqlite3_bind_pointer(S,I,P,X,D)](../c3ref/bind_blob.md) or [sqlite3_result_pointer(C,P,X,D)](../c3ref/result_blob.md) and if X and Y are strings that compare equal according to strcmp(X,Y), then sqlite3_value_pointer(V,Y) will return the pointer P. Otherwise, sqlite3_value_pointer(V,Y) returns a NULL. The sqlite3_bind_pointer() routine is part of the [pointer passing interface](../bindptr.md) added for SQLite 3.20.0.

The sqlite3_value_type(V) interface returns the [datatype code](../c3ref/c_blob.md) for the initial datatype of the [sqlite3_value](../c3ref/value.md) object V. The returned value is one of [SQLITE_INTEGER](../c3ref/c_blob.md), [SQLITE_FLOAT](../c3ref/c_blob.md), [SQLITE_TEXT](../c3ref/c_blob.md), [SQLITE_BLOB](../c3ref/c_blob.md), or [SQLITE_NULL](../c3ref/c_blob.md). Other interfaces might change the datatype for an sqlite3_value object. For example, if the datatype is initially SQLITE_INTEGER and sqlite3_value_text(V) is called to extract a text value for that integer, then subsequent calls to sqlite3_value_type(V) might return SQLITE_TEXT. Whether or not a persistent internal datatype conversion occurs is undefined and may change from one release of SQLite to the next.

The sqlite3_value_numeric_type() interface attempts to apply numeric affinity to the value. This means that an attempt is made to convert the value to an integer or floating point. If such a conversion is possible without loss of information (in other words, if the value is a string that looks like a number) then the conversion is performed. Otherwise no conversion occurs. The [datatype](../c3ref/c_blob.md) after conversion is returned.

Within the [xUpdate](../vtab.md#xupdate) method of a [virtual table](../vtab.md), the sqlite3_value_nochange(X) interface returns true if and only if the column corresponding to X is unchanged by the UPDATE operation that the xUpdate method call was invoked to implement and if the prior [xColumn](../vtab.md#xcolumn) method call that was invoked to extract the value for that column returned without setting a result (probably because it queried [sqlite3_vtab_nochange()](../c3ref/vtab_nochange.md) and found that the column was unchanging). Within an [xUpdate](../vtab.md#xupdate) method, any value for which sqlite3_value_nochange(X) is true will in all other respects appear to be a NULL value. If sqlite3_value_nochange(X) is invoked anywhere other than within an [xUpdate](../vtab.md#xupdate) method call for an UPDATE statement, then the return value is arbitrary and meaningless.

The sqlite3_value_frombind(X) interface returns non-zero if the value X originated from one of the [sqlite3_bind()](../c3ref/bind_blob.md) interfaces. If X comes from an SQL literal value, or a table column, or an expression, then sqlite3_value_frombind(X) returns zero.

Please pay particular attention to the fact that the pointer returned from [sqlite3_value_blob()](../c3ref/value_blob.md), [sqlite3_value_text()](../c3ref/value_blob.md), or [sqlite3_value_text16()](../c3ref/value_blob.md) can be invalidated by a subsequent call to [sqlite3_value_bytes()](../c3ref/value_blob.md), [sqlite3_value_bytes16()](../c3ref/value_blob.md), [sqlite3_value_text()](../c3ref/value_blob.md), or [sqlite3_value_text16()](../c3ref/value_blob.md).

These routines must be called from the same thread as the SQL function that supplied the [sqlite3_value\*](../c3ref/value.md) parameters.

As long as the input parameter is correct, these routines can only fail if an out-of-memory error occurs while trying to do a UTF8→UTF16 or UTF16→UTF8 conversion. If an out-of-memory error occurs, then the return value from these routines is the same as if the column had contained an SQL NULL value. If the input sqlite3_value was not obtained from [sqlite3_value_dup()](../c3ref/value_dup.md), then valid SQL NULL returns can also be distinguished from out-of-memory errors after extracting the value by invoking the [sqlite3_errcode()](../c3ref/errcode.md) immediately after the suspicious return value is obtained and before any other SQLite interface is called on the same [database connection](../c3ref/sqlite3.md). If the input sqlite3_value was obtained from sqlite3_value_dup() then it is disconnected from the database connection and so sqlite3_errcode() will not work. In that case, the only way to distinguish an out-of-memory condition from a true SQL NULL is to invoke sqlite3_value_type() on the input to see if it is NULL prior to trying to extract the value.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
