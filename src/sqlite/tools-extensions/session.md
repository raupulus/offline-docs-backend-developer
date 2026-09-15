---
title: Session Object Handle
source_url: https://www.sqlite.org/session/session.html
source_path: session/session.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: tools-extensions
order: 6740
---

[](../session/intro.md)

## Session Module C Interface

## Session Object Handle

> typedef struct sqlite3_session sqlite3_session;\

An instance of this object is a [session](../sessionintro.md) that can be used to record changes to a database.

Constructor: [sqlite3session_create()](../session/sqlite3session_create.md)

Destructor: [sqlite3session_delete()](../session/sqlite3session_delete.md)

- [sqlite3session_attach](../session/sqlite3session_attach.md)
- [sqlite3session_changeset](../session/sqlite3session_changeset.md)
- [sqlite3session_changeset_size](../session/sqlite3session_changeset_size.md)
- [sqlite3session_diff](../session/sqlite3session_diff.md)
- [sqlite3session_enable](../session/sqlite3session_enable.md)
- [sqlite3session_indirect](../session/sqlite3session_indirect.md)
- [sqlite3session_object_config](../session/sqlite3session_object_config.md)
- [sqlite3session_patchset](../session/sqlite3session_patchset.md)
- [sqlite3session_table_filter](../session/sqlite3session_table_filter.md)

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
