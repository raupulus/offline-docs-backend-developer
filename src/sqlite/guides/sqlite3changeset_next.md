---
title: Advance A Changeset Iterator
source_url: https://www.sqlite.org/session/sqlite3changeset_next.html
source_path: session/sqlite3changeset_next.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6970
---

[](../session/intro.md)

## Session Module C Interface

## Advance A Changeset Iterator

> int sqlite3changeset_next(sqlite3_changeset_iter \*pIter);\

This function may only be used with iterators created by the function [sqlite3changeset_start()](../session/sqlite3changeset_start.md). If it is called on an iterator passed to a conflict-handler callback by [sqlite3changeset_apply()](../session/sqlite3changeset_apply.md), SQLITE_MISUSE is returned and the call has no effect.

Immediately after an iterator is created by sqlite3changeset_start(), it does not point to any change in the changeset. Assuming the changeset is not empty, the first call to this function advances the iterator to point to the first change in the changeset. Each subsequent call advances the iterator to point to the next change in the changeset (if any). If no error occurs and the iterator points to a valid change after a call to sqlite3changeset_next() has advanced it, SQLITE_ROW is returned. Otherwise, if all changes in the changeset have already been visited, SQLITE_DONE is returned.

If an error occurs, an SQLite error code is returned. Possible error codes include SQLITE_CORRUPT (if the changeset buffer is corrupt) or SQLITE_NOMEM.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
