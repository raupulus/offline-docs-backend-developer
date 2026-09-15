---
title: Create A New Changegroup Object
source_url: https://www.sqlite.org/session/sqlite3changegroup_new.html
source_path: session/sqlite3changegroup_new.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6870
---

[](../session/intro.md)

## Session Module C Interface

## Create A New Changegroup Object

> int sqlite3changegroup_new(sqlite3_changegroup \*\*pp);\

An sqlite3_changegroup object is used to combine two or more changesets (or patchsets) into a single changeset (or patchset). A single changegroup object may combine changesets or patchsets, but not both. The output is always in the same format as the input.

If successful, this function returns SQLITE_OK and populates (\*pp) with a pointer to a new sqlite3_changegroup object before returning. The caller should eventually free the returned object using a call to sqlite3changegroup_delete(). If an error occurs, an SQLite error code (i.e. SQLITE_NOMEM) is returned and \*pp is set to NULL.

The usual usage pattern for an sqlite3_changegroup object is as follows:

- It is created using a call to sqlite3changegroup_new().
- Zero or more changesets (or patchsets) are added to the object by calling sqlite3changegroup_add().
- The result of combining all input changesets together is obtained by the application via a call to sqlite3changegroup_output().
- The object is deleted using a call to sqlite3changegroup_delete().

Any number of calls to add() and output() may be made between the calls to new() and delete(), and in any order.

As well as the regular sqlite3changegroup_add() and sqlite3changegroup_output() functions, also available are the streaming versions sqlite3changegroup_add_strm() and sqlite3changegroup_output_strm().

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
