---
title: Finalize A Dynamic String
source_url: https://www.sqlite.org/c3ref/str_finish.html
source_path: c3ref/str_finish.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2000
---

> \
> char \*sqlite3_str_finish(sqlite3_str\*);\
> void sqlite3_str_free(sqlite3_str\*);\

The [sqlite3_str_finish(X)](../c3ref/str_finish.md) interface destroys the sqlite3_str object X and returns a pointer to a memory buffer obtained from [sqlite3_malloc64()](../c3ref/free.md) that contains the constructed string. The calling application should pass the returned value to [sqlite3_free()](../c3ref/free.md) to avoid a memory leak. The [sqlite3_str_finish(X)](../c3ref/str_finish.md) interface may return a NULL pointer if any errors were encountered during construction of the string. The [sqlite3_str_finish(X)](../c3ref/str_finish.md) interface might also return a NULL pointer if the string in [sqlite3_str](../c3ref/str.md) object X is zero bytes long.

The [sqlite3_str_free(X)](../c3ref/str_finish.md) interface destroys both the sqlite3_str object X and the string content it contains. Calling sqlite3_str_free(X) is the equivalent of calling [sqlite3_free](../c3ref/free.md)(sqlite3_str_finish(X)).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
