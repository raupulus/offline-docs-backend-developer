---
title: String Globbing
source_url: https://www.sqlite.org/c3ref/strglob.html
source_path: c3ref/strglob.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2020
---

> \
> int sqlite3_strglob(const char \*zGlob, const char \*zStr);\

The [sqlite3_strglob(P,X)](../c3ref/strglob.md) interface returns zero if and only if string X matches the [GLOB](../lang_expr.md#glob) pattern P. The definition of [GLOB](../lang_expr.md#glob) pattern matching used in [sqlite3_strglob(P,X)](../c3ref/strglob.md) is the same as for the "X GLOB P" operator in the SQL dialect understood by SQLite. The [sqlite3_strglob(P,X)](../c3ref/strglob.md) function is case sensitive.

Note that this routine returns zero on a match and non-zero if the strings do not match, the same as [sqlite3_stricmp()](../c3ref/stricmp.md) and [sqlite3_strnicmp()](../c3ref/stricmp.md).

See also: [sqlite3_strlike()](../c3ref/strlike.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
