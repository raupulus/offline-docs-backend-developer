---
title: Add an double to a changegroup
source_url: https://www.sqlite.org/session/sqlite3changegroup_change_double.html
source_path: session/sqlite3changegroup_change_double.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6800
---

[](../session/intro.md)

## Session Module C Interface

## Add an double to a changegroup

> int sqlite3changegroup_change_double(sqlite3_changegroup\*, int, int, double);\

This function is similar to sqlite3changegroup_change_int64(). Except that it configures the change currently being constructed with a real value instead of a 64-bit integer.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
