---
title: Name Of A Host Parameter
source_url: https://www.sqlite.org/c3ref/bind_parameter_name.html
source_path: c3ref/bind_parameter_name.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 300
---

> \
> const char \*sqlite3_bind_parameter_name(sqlite3_stmt\*, int);\

The sqlite3_bind_parameter_name(P,N) interface returns the name of the N-th [SQL parameter](../c3ref/bind_blob.md) in the [prepared statement](../c3ref/stmt.md) P. SQL parameters of the form "?NNN" or ":AAA" or "@AAA" or "\$AAA" have a name which is the string "?NNN" or ":AAA" or "@AAA" or "\$AAA" respectively. In other words, the initial ":" or "\$" or "@" or "?" is included as part of the name. Parameters of the form "?" without a following integer have no name and are referred to as "nameless" or "anonymous parameters".

The first host parameter has an index of 1, not 0.

If the value N is out of range or if the N-th parameter is nameless, then NULL is returned. The returned string is always in UTF-8 encoding even if the named parameter was originally specified as UTF-16 in [sqlite3_prepare16()](../c3ref/prepare.md), [sqlite3_prepare16_v2()](../c3ref/prepare.md), or [sqlite3_prepare16_v3()](../c3ref/prepare.md).

See also: [sqlite3_bind()](../c3ref/bind_blob.md), [sqlite3_bind_parameter_count()](../c3ref/bind_parameter_count.md), and [sqlite3_bind_parameter_index()](../c3ref/bind_parameter_index.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
