---
title: Changegroup Handle
source_url: https://www.sqlite.org/session/changegroup.html
source_path: session/changegroup.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6670
---

[](../session/intro.md)

## Session Module C Interface

## Changegroup Handle

> typedef struct sqlite3_changegroup sqlite3_changegroup;\

A changegroup is an object used to combine two or more [changesets](../sessionintro.md#changeset) or [patchsets](../sessionintro.md#changeset)

Constructor: [sqlite3changegroup_new()](../session/sqlite3changegroup_new.md)

Destructor: [sqlite3changegroup_delete()](../session/sqlite3changegroup_delete.md)

Methods: [sqlite3changegroup_add()](../session/sqlite3changegroup_add.md), [sqlite3changegroup_add_change()](../session/sqlite3changegroup_add_change.md), [sqlite3changegroup_output()](../session/sqlite3changegroup_output.md)

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
