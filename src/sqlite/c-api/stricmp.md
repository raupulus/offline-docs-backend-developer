---
title: String Comparison
source_url: https://www.sqlite.org/c3ref/stricmp.html
source_path: c3ref/stricmp.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2030
---

> \
> int sqlite3_stricmp(const char \*, const char \*);\
> int sqlite3_strnicmp(const char \*, const char \*, int);\

The [sqlite3_stricmp()](../c3ref/stricmp.md) and [sqlite3_strnicmp()](../c3ref/stricmp.md) APIs allow applications and extensions to compare the contents of two buffers containing UTF-8 strings in a case-independent fashion, using the same definition of "case independence" that SQLite uses internally when comparing identifiers.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
