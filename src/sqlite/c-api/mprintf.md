---
title: Formatted String Printing Functions
source_url: https://www.sqlite.org/c3ref/mprintf.html
source_path: c3ref/mprintf.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1510
---

> \
> char \*sqlite3_mprintf(const char\*,...);\
> char \*sqlite3_vmprintf(const char\*, va_list);\
> char \*sqlite3_snprintf(int,char\*,const char\*, ...);\
> char \*sqlite3_vsnprintf(int,char\*,const char\*, va_list);\

These routines are work-alikes of the "printf()" family of functions from the standard C library. These routines understand most of the common formatting options from the standard library printf() plus some additional non-standard formats ([%q](../printf.md#percentq), [%Q](../printf.md#percentq), [%w](../printf.md#percentw), and [%z](../printf.md#percentz)). See the [built-in printf()](../printf.md) documentation for details.

The sqlite3_mprintf() and sqlite3_vmprintf() routines write their results into memory obtained from [sqlite3_malloc64()](../c3ref/free.md). The strings returned by these two routines should be released by [sqlite3_free()](../c3ref/free.md). Both routines return a NULL pointer if [sqlite3_malloc64()](../c3ref/free.md) is unable to allocate enough memory to hold the resulting string.

The sqlite3_snprintf() routine is similar to "snprintf()" from the standard C library. The result is written into the buffer supplied as the second parameter whose size is given by the first parameter. Note that the order of the first two parameters is reversed from snprintf(). This is an historical accident that cannot be fixed without breaking backwards compatibility. Note also that sqlite3_snprintf() returns a pointer to its buffer instead of the number of characters actually written into the buffer. We admit that the number of characters written would be a more useful return value but we cannot change the implementation of sqlite3_snprintf() now without breaking compatibility.

As long as the buffer size is greater than zero, sqlite3_snprintf() guarantees that the buffer is always zero-terminated. The first parameter "n" is the total size of the buffer, including space for the zero terminator. So the longest string that can be completely written will be n-1 characters.

The sqlite3_vsnprintf() routine is a varargs version of sqlite3_snprintf().

See also: [built-in printf()](../printf.md), [printf() SQL function](../lang_corefunc.md#printf)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
