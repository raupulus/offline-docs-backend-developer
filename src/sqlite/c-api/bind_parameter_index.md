---
title: Index Of A Parameter With A Given Name
source_url: https://www.sqlite.org/c3ref/bind_parameter_index.html
source_path: c3ref/bind_parameter_index.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 290
---

> \
> int sqlite3_bind_parameter_index(sqlite3_stmt\*, const char \*zName);\

Return the index of an SQL parameter given its name. The index value returned is suitable for use as the second parameter to [sqlite3_bind()](../c3ref/bind_blob.md). A zero is returned if no matching parameter is found. The parameter name must be given in UTF-8 even if the original statement was prepared from UTF-16 text using [sqlite3_prepare16_v2()](../c3ref/prepare.md) or [sqlite3_prepare16_v3()](../c3ref/prepare.md).

See also: [sqlite3_bind()](../c3ref/bind_blob.md), [sqlite3_bind_parameter_count()](../c3ref/bind_parameter_count.md), and [sqlite3_bind_parameter_name()](../c3ref/bind_parameter_name.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
