---
title: Dynamic String Object
source_url: https://www.sqlite.org/c3ref/str.html
source_path: c3ref/str.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1970
---

> \
> typedef struct sqlite3_str sqlite3_str;\

An instance of the sqlite3_str object contains a dynamically-sized string under construction.

The lifecycle of an sqlite3_str object is as follows:

1.  The sqlite3_str object is created using [sqlite3_str_new()](../c3ref/str_new.md).
2.  Text is appended to the sqlite3_str object using various methods, such as [sqlite3_str_appendf()](../c3ref/str_append.md).
3.  The sqlite3_str object is destroyed and the string it created is returned using the [sqlite3_str_finish()](../c3ref/str_finish.md) interface.

1 Constructor using this object: [sqlite3_str_new()](../c3ref/str_new.md)

2 Destructors using this object: [sqlite3_str_finish()](../c3ref/str_finish.md), [sqlite3_str_free()](../c3ref/str_finish.md)

10 Methods using this object:

- [sqlite3_str_append](../c3ref/str_append.md)
- [sqlite3_str_appendall](../c3ref/str_append.md)
- [sqlite3_str_appendchar](../c3ref/str_append.md)
- [sqlite3_str_appendf](../c3ref/str_append.md)
- [sqlite3_str_errcode](../c3ref/str_errcode.md)
- [sqlite3_str_length](../c3ref/str_errcode.md)
- [sqlite3_str_reset](../c3ref/str_append.md)
- [sqlite3_str_truncate](../c3ref/str_append.md)
- [sqlite3_str_value](../c3ref/str_errcode.md)
- [sqlite3_str_vappendf](../c3ref/str_append.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
