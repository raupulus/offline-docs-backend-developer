---
title: Create A New Dynamic String Object
source_url: https://www.sqlite.org/c3ref/str_new.html
source_path: c3ref/str_new.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2010
---

> \
> sqlite3_str \*sqlite3_str_new(sqlite3\*);\

The [sqlite3_str_new(D)](../c3ref/str_new.md) interface allocates and initializes a new [sqlite3_str](../c3ref/str.md) object. To avoid memory leaks, the object returned by [sqlite3_str_new()](../c3ref/str_new.md) must be freed by a subsequent call to [sqlite3_str_finish(X)](../c3ref/str_finish.md).

The [sqlite3_str_new(D)](../c3ref/str_new.md) interface always returns a pointer to a valid [sqlite3_str](../c3ref/str.md) object, though in the event of an out-of-memory error the returned object might be a special singleton that will silently reject new text, always return SQLITE_NOMEM from [sqlite3_str_errcode()](../c3ref/str_errcode.md), always return 0 for [sqlite3_str_length()](../c3ref/str_errcode.md), and always return NULL from [sqlite3_str_finish(X)](../c3ref/str_finish.md). It is always safe to use the value returned by [sqlite3_str_new(D)](../c3ref/str_new.md) as the sqlite3_str parameter to any of the other [sqlite3_str](../c3ref/str.md) methods.

The D parameter to [sqlite3_str_new(D)](../c3ref/str_new.md) may be NULL. If the D parameter in [sqlite3_str_new(D)](../c3ref/str_new.md) is not NULL, then the maximum length of the string contained in the [sqlite3_str](../c3ref/str.md) object will be the value set for [sqlite3_limit](../c3ref/limit.md)(D,[SQLITE_LIMIT_LENGTH](../c3ref/c_limit_attached.md#sqlitelimitlength)) instead of [SQLITE_MAX_LENGTH](../limits.md#max_length).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
