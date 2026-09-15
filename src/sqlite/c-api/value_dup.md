---
title: Copy And Free SQL Values
source_url: https://www.sqlite.org/c3ref/value_dup.html
source_path: c3ref/value_dup.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2190
---

> \
> sqlite3_value \*sqlite3_value_dup(const sqlite3_value\*);\
> void sqlite3_value_free(sqlite3_value\*);\

The sqlite3_value_dup(V) interface makes a copy of the [sqlite3_value](../c3ref/value.md) object V and returns a pointer to that copy. The [sqlite3_value](../c3ref/value.md) returned is a [protected sqlite3_value](../c3ref/value.md) object even if the input is not. The sqlite3_value_dup(V) interface returns NULL if V is NULL or if a memory allocation fails. If V is a [pointer value](../bindptr.md), then the result of sqlite3_value_dup(V) is a NULL value.

The sqlite3_value_free(V) interface frees an [sqlite3_value](../c3ref/value.md) object previously obtained from [sqlite3_value_dup()](../c3ref/value_dup.md). If V is a NULL pointer then sqlite3_value_free(V) is a harmless no-op.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
