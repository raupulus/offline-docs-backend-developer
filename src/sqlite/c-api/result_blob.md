---
title: Setting The Result Of An SQL Function
source_url: https://www.sqlite.org/c3ref/result_blob.html
source_path: c3ref/result_blob.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1710
---

> \
> void sqlite3_result_blob(sqlite3_context\*, const void\*, int, void(\*)(void\*));\
> void sqlite3_result_blob64(sqlite3_context\*,const void\*,\
>                            sqlite3_uint64,void(\*)(void\*));\
> void sqlite3_result_double(sqlite3_context\*, double);\
> void sqlite3_result_error(sqlite3_context\*, const char\*, int);\
> void sqlite3_result_error16(sqlite3_context\*, const void\*, int);\
> void sqlite3_result_error_toobig(sqlite3_context\*);\
> void sqlite3_result_error_nomem(sqlite3_context\*);\
> void sqlite3_result_error_code(sqlite3_context\*, int);\
> void sqlite3_result_int(sqlite3_context\*, int);\
> void sqlite3_result_int64(sqlite3_context\*, sqlite3_int64);\
> void sqlite3_result_null(sqlite3_context\*);\
> void sqlite3_result_text(sqlite3_context\*, const char\*, int, void(\*)(void\*));\
> void sqlite3_result_text64(sqlite3_context\*, const char \*z, sqlite3_uint64 n,\
>                            void(\*)(void\*), unsigned char encoding);\
> void sqlite3_result_text16(sqlite3_context\*, const void\*, int, void(\*)(void\*));\
> void sqlite3_result_text16le(sqlite3_context\*, const void\*, int,void(\*)(void\*));\
> void sqlite3_result_text16be(sqlite3_context\*, const void\*, int,void(\*)(void\*));\
> void sqlite3_result_value(sqlite3_context\*, sqlite3_value\*);\
> void sqlite3_result_pointer(sqlite3_context\*, void\*,const char\*,void(\*)(void\*));\
> void sqlite3_result_zeroblob(sqlite3_context\*, int n);\
> int sqlite3_result_zeroblob64(sqlite3_context\*, sqlite3_uint64 n);\

These routines are used by the xFunc or xFinal callbacks that implement SQL functions and aggregates. See [sqlite3_create_function()](../c3ref/create_function.md) and [sqlite3_create_function16()](../c3ref/create_function.md) for additional information.

These functions work very much like the [parameter binding](../c3ref/bind_blob.md) family of functions used to bind values to host parameters in prepared statements. Refer to the [SQL parameter](../c3ref/bind_blob.md) documentation for additional information.

The sqlite3_result_blob() interface sets the result from an application-defined function to be the BLOB whose content is pointed to by the second parameter and which is N bytes long where N is the third parameter.

The sqlite3_result_zeroblob(C,N) and sqlite3_result_zeroblob64(C,N) interfaces set the result of the application-defined function to be a BLOB containing all zero bytes and N bytes in size.

The sqlite3_result_double() interface sets the result from an application-defined function to be a floating point value specified by its 2nd argument.

The sqlite3_result_error() and sqlite3_result_error16() functions cause the implemented SQL function to throw an exception. SQLite uses the string pointed to by the 2nd parameter of sqlite3_result_error() or sqlite3_result_error16() as the text of an error message. SQLite interprets the error message string from sqlite3_result_error() as UTF-8. SQLite interprets the string from sqlite3_result_error16() as UTF-16 using the same [byte-order determination rules](../c3ref/bind_blob.md#byteorderdeterminationrules) as [sqlite3_bind_text16()](../c3ref/bind_blob.md). If the third parameter to sqlite3_result_error() or sqlite3_result_error16() is negative then SQLite takes as the error message all text up through the first zero character. If the third parameter to sqlite3_result_error() or sqlite3_result_error16() is non-negative then SQLite takes that many bytes (not characters) from the 2nd parameter as the error message. The sqlite3_result_error() and sqlite3_result_error16() routines make a private copy of the error message text before they return. Hence, the calling function can deallocate or modify the text after they return without harm. The sqlite3_result_error_code() function changes the error code returned by SQLite as a result of an error in a function. By default, the error code is SQLITE_ERROR. A subsequent call to sqlite3_result_error() or sqlite3_result_error16() resets the error code to SQLITE_ERROR.

The sqlite3_result_error_toobig() interface causes SQLite to throw an error indicating that a string or BLOB is too long to represent.

The sqlite3_result_error_nomem() interface causes SQLite to throw an error indicating that a memory allocation failed.

The sqlite3_result_int() interface sets the return value of the application-defined function to be the 32-bit signed integer value given in the 2nd argument. The sqlite3_result_int64() interface sets the return value of the application-defined function to be the 64-bit signed integer value given in the 2nd argument.

The sqlite3_result_null() interface sets the return value of the application-defined function to be NULL.

The sqlite3_result_text(), sqlite3_result_text16(), sqlite3_result_text16le(), and sqlite3_result_text16be() interfaces set the return value of the application-defined function to be a text string which is represented as UTF-8, UTF-16 native byte order, UTF-16 little endian, or UTF-16 big endian, respectively. The sqlite3_result_text64(C,Z,N,D,E) interface sets the return value of an application-defined function to be a text string in an encoding specified the E parameter, which must be one of [SQLITE_UTF8](../c3ref/c_any.md#sqliteutf8), [SQLITE_UTF8_ZT](../c3ref/c_any.md#sqliteutf8zt), [SQLITE_UTF16](../c3ref/c_any.md#sqliteutf16), [SQLITE_UTF16BE](../c3ref/c_any.md#sqliteutf16be), or [SQLITE_UTF16LE](../c3ref/c_any.md#sqliteutf16le). The special value [SQLITE_UTF8_ZT](../c3ref/c_any.md#sqliteutf8zt) means that the result text is both UTF-8 and zero-terminated. In other words, SQLITE_UTF8_ZT means that the Z array holds at least N+1 bytes and that the Z\[N\] is zero. SQLite takes the text result from the application from the 2nd parameter of the sqlite3_result_text\* interfaces. If the 3rd parameter to any of the sqlite3_result_text\* interfaces other than sqlite3_result_text64() is negative, then SQLite computes the string length itself by searching the 2nd parameter for the first zero character. If the 3rd parameter to the sqlite3_result_text\* interfaces is non-negative, then as many bytes (not characters) of the text pointed to by the 2nd parameter are taken as the application-defined function result. If the 3rd parameter is non-negative, then it must be the byte offset into the string where the NUL terminator would appear if the string were NUL terminated. If any NUL characters occur in the string at a byte offset that is less than the value of the 3rd parameter, then the resulting string will contain embedded NULs and the result of expressions operating on strings with embedded NULs is undefined. If the 4th parameter to the sqlite3_result_text\* interfaces or sqlite3_result_blob is a non-NULL pointer, then SQLite calls that function as the destructor on the text or BLOB result when it has finished using that result. If the 4th parameter to the sqlite3_result_text\* interfaces or to sqlite3_result_blob is the special constant SQLITE_STATIC, then SQLite assumes that the text or BLOB result is in constant space and does not copy the content of the parameter nor call a destructor on the content when it has finished using that result. If the 4th parameter to the sqlite3_result_text\* interfaces or sqlite3_result_blob is the special constant SQLITE_TRANSIENT then SQLite makes a copy of the result into space obtained from [sqlite3_malloc()](../c3ref/free.md) before it returns.

For the sqlite3_result_text16(), sqlite3_result_text16le(), and sqlite3_result_text16be() routines, and for sqlite3_result_text64() when the encoding is not UTF8, if the input UTF16 begins with a byte-order mark (BOM, U+FEFF) then the BOM is removed from the string and the rest of the string is interpreted according to the byte-order specified by the BOM. The byte-order specified by the BOM at the beginning of the text overrides the byte-order specified by the interface procedure. So, for example, if sqlite3_result_text16le() is invoked with text that begins with bytes 0xfe, 0xff (a big-endian byte-order mark) then the first two bytes of input are skipped and the remaining input is interpreted as UTF16BE text.

For UTF16 input text to the sqlite3_result_text16(), sqlite3_result_text16be(), sqlite3_result_text16le(), and sqlite3_result_text64() routines, if the text contains invalid UTF16 characters, the invalid characters might be converted into the unicode replacement character, U+FFFD.

The sqlite3_result_value() interface sets the result of the application-defined function to be a copy of the [unprotected sqlite3_value](../c3ref/value.md) object specified by the 2nd parameter. The sqlite3_result_value() interface makes a copy of the [sqlite3_value](../c3ref/value.md) so that the [sqlite3_value](../c3ref/value.md) specified in the parameter may change or be deallocated after sqlite3_result_value() returns without harm. A [protected sqlite3_value](../c3ref/value.md) object may always be used where an [unprotected sqlite3_value](../c3ref/value.md) object is required, so either kind of [sqlite3_value](../c3ref/value.md) object can be used with this interface.

The sqlite3_result_pointer(C,P,T,D) interface sets the result to an SQL NULL value, just like [sqlite3_result_null(C)](../c3ref/result_blob.md), except that it also associates the host-language pointer P or type T with that NULL value such that the pointer can be retrieved within an [application-defined SQL function](../appfunc.md) using [sqlite3_value_pointer()](../c3ref/value_blob.md). If the D parameter is not NULL, then it is a pointer to a destructor for the P parameter. SQLite invokes D with P as its only argument when SQLite is finished with P. The T parameter should be a static string and preferably a string literal. The sqlite3_result_pointer() routine is part of the [pointer passing interface](../bindptr.md) added for SQLite 3.20.0.

If these routines are called from within a different thread than the one containing the application-defined function that received the [sqlite3_context](../c3ref/context.md) pointer, the results are undefined.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
