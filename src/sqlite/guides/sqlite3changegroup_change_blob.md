---
title: Add a blob to a changegroup
source_url: https://www.sqlite.org/session/sqlite3changegroup_change_blob.html
source_path: session/sqlite3changegroup_change_blob.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6790
---

[](../session/intro.md)

## Session Module C Interface

## Add a blob to a changegroup

> int sqlite3changegroup_change_blob(\
>     sqlite3_changegroup\*, int, int, const void \*pVal, int nVal\
> );\

This function is similar to sqlite3changegroup_change_int64(). It configures the currently accumulated change with a blob value instead of a 64-bit integer. Parameter pVal points to a buffer containing the blob. Parameter nVal is the size of the blob in bytes.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
