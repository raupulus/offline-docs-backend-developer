---
title: Obtain Conflicting Row Values From A Changeset Iterator
source_url: https://www.sqlite.org/session/sqlite3changeset_conflict.html
source_path: session/sqlite3changeset_conflict.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6920
---

[](../session/intro.md)

## Session Module C Interface

## Obtain Conflicting Row Values From A Changeset Iterator

> int sqlite3changeset_conflict(\
>   sqlite3_changeset_iter \*pIter,  /\* Changeset iterator \*/\
>   int iVal,                       /\* Column number \*/\
>   sqlite3_value \*\*ppValue         /\* OUT: Value from conflicting row \*/\
> );\

This function should only be used with iterator objects passed to a conflict-handler callback by [sqlite3changeset_apply()](../session/sqlite3changeset_apply.md) with either [SQLITE_CHANGESET_DATA](../session/c_changeset_conflict.md) or [SQLITE_CHANGESET_CONFLICT](../session/c_changeset_conflict.md). If this function is called on any other iterator, [SQLITE_MISUSE](../rescode.md#misuse) is returned and \*ppValue is set to NULL.

Argument iVal must be greater than or equal to 0, and less than the number of columns in the table affected by the current change. Otherwise, [SQLITE_RANGE](../rescode.md#range) is returned and \*ppValue is set to NULL.

If successful, this function sets \*ppValue to point to a protected sqlite3_value object containing the iVal'th value from the "conflicting row" associated with the current conflict-handler callback and returns SQLITE_OK.

If some other error occurs (e.g. an OOM condition), an SQLite error code is returned and \*ppValue is set to NULL.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
