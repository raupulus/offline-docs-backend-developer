---
title: Obtain new.* Values From A Changeset Iterator
source_url: https://www.sqlite.org/session/sqlite3changeset_new.html
source_path: session/sqlite3changeset_new.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6960
---

[](../session/intro.md)

## Session Module C Interface

## Obtain new.\* Values From A Changeset Iterator

> int sqlite3changeset_new(\
>   sqlite3_changeset_iter \*pIter,  /\* Changeset iterator \*/\
>   int iVal,                       /\* Column number \*/\
>   sqlite3_value \*\*ppValue         /\* OUT: New value (or NULL pointer) \*/\
> );\

The pIter argument passed to this function may either be an iterator passed to a conflict-handler by [sqlite3changeset_apply()](../session/sqlite3changeset_apply.md), or an iterator created by [sqlite3changeset_start()](../session/sqlite3changeset_start.md). In the latter case, the most recent call to [sqlite3changeset_next()](../session/sqlite3changeset_next.md) must have returned SQLITE_ROW. Furthermore, it may only be called if the type of change that the iterator currently points to is either [SQLITE_UPDATE](../c3ref/c_alter_table.md) or [SQLITE_INSERT](../c3ref/c_alter_table.md). Otherwise, this function returns [SQLITE_MISUSE](../rescode.md#misuse) and sets \*ppValue to NULL.

Argument iVal must be greater than or equal to 0, and less than the number of columns in the table affected by the current change. Otherwise, [SQLITE_RANGE](../rescode.md#range) is returned and \*ppValue is set to NULL.

If successful, this function sets \*ppValue to point to a protected sqlite3_value object containing the iVal'th value from the vector of new row values stored as part of the UPDATE or INSERT change and returns SQLITE_OK. If the change is an UPDATE and does not include a new value for the requested column, \*ppValue is set to NULL and SQLITE_OK returned. The name of the function comes from the fact that this is similar to the "new.\*" columns available to update or delete triggers.

If some other error occurs (e.g. an OOM condition), an SQLite error code is returned and \*ppValue is set to NULL.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
