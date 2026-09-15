---
title: Add Content To A Dynamic String
source_url: https://www.sqlite.org/c3ref/str_append.html
source_path: c3ref/str_append.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1980
---

> \
> void sqlite3_str_appendf(sqlite3_str\*, const char \*zFormat, ...);\
> void sqlite3_str_vappendf(sqlite3_str\*, const char \*zFormat, va_list);\
> void sqlite3_str_append(sqlite3_str\*, const char \*zIn, int N);\
> void sqlite3_str_appendall(sqlite3_str\*, const char \*zIn);\
> void sqlite3_str_appendchar(sqlite3_str\*, int N, char C);\
> void sqlite3_str_reset(sqlite3_str\*);\
> void sqlite3_str_truncate(sqlite3_str\*,int N);\

These interfaces add or remove content to an sqlite3_str object previously obtained from [sqlite3_str_new()](../c3ref/str_new.md).

The [sqlite3_str_appendf(X,F,...)](../c3ref/str_append.md) and [sqlite3_str_vappendf(X,F,V)](../c3ref/str_append.md) interfaces uses the [built-in printf](../printf.md) functionality of SQLite to append formatted text onto the end of [sqlite3_str](../c3ref/str.md) object X.

The [sqlite3_str_append(X,S,N)](../c3ref/str_append.md) method appends exactly N bytes from string S onto the end of the [sqlite3_str](../c3ref/str.md) object X. N must be non-negative. S must contain at least N non-zero bytes of content. To append a zero-terminated string in its entirety, use the [sqlite3_str_appendall()](../c3ref/str_append.md) method instead.

The [sqlite3_str_appendall(X,S)](../c3ref/str_append.md) method appends the complete content of zero-terminated string S onto the end of [sqlite3_str](../c3ref/str.md) object X.

The [sqlite3_str_appendchar(X,N,C)](../c3ref/str_append.md) method appends N copies of the single-byte character C onto the end of [sqlite3_str](../c3ref/str.md) object X. This method can be used, for example, to add whitespace indentation.

The [sqlite3_str_reset(X)](../c3ref/str_append.md) method resets the string under construction inside [sqlite3_str](../c3ref/str.md) object X back to zero bytes in length.

The [sqlite3_str_truncate(X,N)](../c3ref/str_append.md) method changes the length of the string under construction to be N bytes or less. This routine is a no-op if N is negative or if the string is already N bytes or smaller in size.

These methods do not return a result code. If an error occurs, that fact is recorded in the [sqlite3_str](../c3ref/str.md) object and can be recovered by a subsequent call to [sqlite3_str_errcode(X)](../c3ref/str_errcode.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
