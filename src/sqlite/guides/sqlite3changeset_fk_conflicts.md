---
title: Determine The Number Of Foreign Key Constraint Violations
source_url: https://www.sqlite.org/session/sqlite3changeset_fk_conflicts.html
source_path: session/sqlite3changeset_fk_conflicts.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6940
---

[](../session/intro.md)

## Session Module C Interface

## Determine The Number Of Foreign Key Constraint Violations

> int sqlite3changeset_fk_conflicts(\
>   sqlite3_changeset_iter \*pIter,  /\* Changeset iterator \*/\
>   int \*pnOut                      /\* OUT: Number of FK violations \*/\
> );\

This function may only be called with an iterator passed to an SQLITE_CHANGESET_FOREIGN_KEY conflict handler callback. In this case it sets the output variable to the total number of known foreign key violations in the destination database and returns SQLITE_OK.

In all other cases this function returns SQLITE_MISUSE.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
