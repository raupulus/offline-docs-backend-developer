---
title: Add a text value to a changegroup
source_url: https://www.sqlite.org/session/sqlite3changegroup_change_text.html
source_path: session/sqlite3changegroup_change_text.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6840
---

[](../session/intro.md)

## Session Module C Interface

## Add a text value to a changegroup

> int sqlite3changegroup_change_text(\
>   sqlite3_changegroup\*, int, int, const char \*pVal, int nVal\
> );\

This function is similar to sqlite3changegroup_change_int64(). It configures the currently accumulated change with a text value instead of a 64-bit integer. Parameter pVal points to a buffer containing the text encoded using utf-8. Parameter nVal may either be the size of the text value in bytes, or else a negative value, in which case the buffer pVal points to is assumed to be nul-terminated.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
