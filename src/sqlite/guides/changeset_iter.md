---
title: Changeset Iterator Handle
source_url: https://www.sqlite.org/session/changeset_iter.html
source_path: session/changeset_iter.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6680
---

[](../session/intro.md)

## Session Module C Interface

## Changeset Iterator Handle

> typedef struct sqlite3_changeset_iter sqlite3_changeset_iter;\

An instance of this object acts as a cursor for iterating over the elements of a [changeset](../sessionintro.md#changeset) or [patchset](../sessionintro.md#changeset).

Constructors: [sqlite3changeset_start()](../session/sqlite3changeset_start.md), [sqlite3changeset_start_v2()](../session/sqlite3changeset_start.md)

- [sqlite3changeset_conflict](../session/sqlite3changeset_conflict.md)
- [sqlite3changeset_finalize](../session/sqlite3changeset_finalize.md)
- [sqlite3changeset_fk_conflicts](../session/sqlite3changeset_fk_conflicts.md)
- [sqlite3changeset_new](../session/sqlite3changeset_new.md)
- [sqlite3changeset_next](../session/sqlite3changeset_next.md)
- [sqlite3changeset_old](../session/sqlite3changeset_old.md)
- [sqlite3changeset_op](../session/sqlite3changeset_op.md)
- [sqlite3changeset_pk](../session/sqlite3changeset_pk.md)

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
