---
title: Text Encodings
source_url: https://www.sqlite.org/c3ref/c_any.html
source_path: c3ref/c_any.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 440
---

> \
> \#define SQLITE_UTF8           1    /\* IMP: R-37514-35566 \*/\
> \#define SQLITE_UTF16LE        2    /\* IMP: R-03371-37637 \*/\
> \#define SQLITE_UTF16BE        3    /\* IMP: R-51971-34154 \*/\
> \#define SQLITE_UTF16          4    /\* Use native byte order \*/\
> \#define SQLITE_ANY            5    /\* Deprecated \*/\
> \#define SQLITE_UTF16_ALIGNED  8    /\* sqlite3_create_collation only \*/\
> \#define SQLITE_UTF8_ZT       16    /\* Zero-terminated UTF8 \*/\

These constants define integer codes that represent the various text encodings supported by SQLite.

SQLITE_UTF8  
Text is encoding as UTF-8

SQLITE_UTF16LE  
Text is encoding as UTF-16 with each code point being expressed "little endian" - the least significant byte first. This is the usual encoding, for example on Windows.

SQLITE_UTF16BE  
Text is encoding as UTF-16 with each code point being expressed "big endian" - the most significant byte first. This encoding is less common, but is still sometimes seen, specially on older systems.

<span id="sqliteutf16"></span>

SQLITE_UTF16  
Text is encoding as UTF-16 with each code point being expressed either little endian or as big endian, according to the native endianness of the host computer.

<span id="sqliteany"></span>

SQLITE_ANY  
This encoding value may only be used to declare the preferred text for [application-defined SQL functions](../appfunc.md) created using [sqlite3_create_function()](../c3ref/create_function.md) and similar. If the preferred encoding (the 4th parameter to sqlite3_create_function() - the eTextRep parameter) is SQLITE_ANY, that indicates that the function does not have a preference regarding the text encoding of its parameters and can take any text encoding that the SQLite core find convenient to supply. This option is deprecated. Please do not use it in new applications.

<span id="sqliteutf16aligned"></span>

SQLITE_UTF16_ALIGNED  
This encoding value may be used as the 3rd parameter (the eTextRep parameter) to [sqlite3_create_collation()](../c3ref/create_collation.md) and similar. This encoding value means that the application-defined collating sequence created expects its input strings to be in UTF16 in native byte order, and that the start of the strings must be aligned to a 2-byte boundary.

<span id="sqliteutf8zt"></span>

SQLITE_UTF8_ZT  
This option can only be used to specify the text encoding to strings input to [sqlite3_result_text64()](../c3ref/result_blob.md) and [sqlite3_bind_text64()](../c3ref/bind_blob.md). The SQLITE_UTF8_ZT encoding means that the input string (call it "z") is UTF-8 encoded and that it is zero-terminated. If the length parameter (call it "n") is non-negative, this encoding option means that the caller guarantees that z array contains at least n+1 bytes and that the z\[n\] byte has a value of zero. This option gives the same output as SQLITE_UTF8, but can be more efficient by avoiding the need to make a copy of the input string, in some cases. However, if z is allocated to hold fewer than n+1 bytes or if the z\[n\] byte is not zero, undefined behavior may result.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
