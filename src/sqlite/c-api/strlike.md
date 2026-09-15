---
title: String LIKE Matching
source_url: https://www.sqlite.org/c3ref/strlike.html
source_path: c3ref/strlike.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2040
---

> \
> int sqlite3_strlike(const char \*zGlob, const char \*zStr, unsigned int cEsc);\

The [sqlite3_strlike(P,X,E)](../c3ref/strlike.md) interface returns zero if and only if string X matches the [LIKE](../lang_expr.md#like) pattern P with escape character E. The definition of [LIKE](../lang_expr.md#like) pattern matching used in [sqlite3_strlike(P,X,E)](../c3ref/strlike.md) is the same as for the "X LIKE P ESCAPE E" operator in the SQL dialect understood by SQLite. For "X LIKE P" without the ESCAPE clause, set the E parameter of [sqlite3_strlike(P,X,E)](../c3ref/strlike.md) to 0. As with the LIKE operator, the [sqlite3_strlike(P,X,E)](../c3ref/strlike.md) function is case insensitive - equivalent upper and lower case ASCII characters match one another.

The [sqlite3_strlike(P,X,E)](../c3ref/strlike.md) function matches Unicode characters, though only ASCII characters are case folded.

Note that this routine returns zero on a match and non-zero if the strings do not match, the same as [sqlite3_stricmp()](../c3ref/stricmp.md) and [sqlite3_strnicmp()](../c3ref/stricmp.md).

See also: [sqlite3_strglob()](../c3ref/strglob.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
