---
title: Add A Single Change To A Changegroup
source_url: https://www.sqlite.org/session/sqlite3changegroup_add_change.html
source_path: session/sqlite3changegroup_add_change.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6760
---

[](../session/intro.md)

## Session Module C Interface

## Add A Single Change To A Changegroup

> int sqlite3changegroup_add_change(\
>   sqlite3_changegroup\*,\
>   sqlite3_changeset_iter\*\
> );\

This function adds the single change currently indicated by the iterator passed as the second argument to the changegroup object. The rules for adding the change are just as described for [sqlite3changegroup_add()](../session/sqlite3changegroup_add.md).

If the change is successfully added to the changegroup, SQLITE_OK is returned. Otherwise, an SQLite error code is returned.

The iterator must point to a valid entry when this function is called. If it does not, SQLITE_ERROR is returned and no change is added to the changegroup. Additionally, the iterator must not have been opened with the SQLITE_CHANGESETAPPLY_INVERT flag. In this case SQLITE_ERROR is also returned.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
