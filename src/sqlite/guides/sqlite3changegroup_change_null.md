---
title: Add a NULL to a changegroup
source_url: https://www.sqlite.org/session/sqlite3changegroup_change_null.html
source_path: session/sqlite3changegroup_change_null.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6830
---

[](../session/intro.md)

## Session Module C Interface

## Add a NULL to a changegroup

> int sqlite3changegroup_change_null(sqlite3_changegroup\*, int, int);\

This function is similar to sqlite3changegroup_change_int64(). Except that it configures the change currently under construction with a NULL value instead of a 64-bit integer.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
