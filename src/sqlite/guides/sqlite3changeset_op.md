---
title: Obtain The Current Operation From A Changeset Iterator
source_url: https://www.sqlite.org/session/sqlite3changeset_op.html
source_path: session/sqlite3changeset_op.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6990
---

[](../session/intro.md)

## Session Module C Interface

## Obtain The Current Operation From A Changeset Iterator

> int sqlite3changeset_op(\
>   sqlite3_changeset_iter \*pIter,  /\* Iterator object \*/\
>   const char \*\*pzTab,             /\* OUT: Pointer to table name \*/\
>   int \*pnCol,                     /\* OUT: Number of columns in table \*/\
>   int \*pOp,                       /\* OUT: SQLITE_INSERT, DELETE or UPDATE \*/\
>   int \*pbIndirect                 /\* OUT: True for an 'indirect' change \*/\
> );\

The pIter argument passed to this function may either be an iterator passed to a conflict-handler by [sqlite3changeset_apply()](../session/sqlite3changeset_apply.md), or an iterator created by [sqlite3changeset_start()](../session/sqlite3changeset_start.md). In the latter case, the most recent call to [sqlite3changeset_next()](../session/sqlite3changeset_next.md) must have returned [SQLITE_ROW](../rescode.md#row). If this is not the case, this function returns [SQLITE_MISUSE](../rescode.md#misuse).

Arguments pOp, pnCol and pzTab may not be NULL. Upon return, three outputs are set through these pointers:

\*pOp is set to one of [SQLITE_INSERT](../c3ref/c_alter_table.md), [SQLITE_DELETE](../c3ref/c_alter_table.md) or [SQLITE_UPDATE](../c3ref/c_alter_table.md), depending on the type of change that the iterator currently points to;

\*pnCol is set to the number of columns in the table affected by the change; and

\*pzTab is set to point to a nul-terminated utf-8 encoded string containing the name of the table affected by the current change. The buffer remains valid until either sqlite3changeset_next() is called on the iterator or until the conflict-handler function returns.

If pbIndirect is not NULL, then \*pbIndirect is set to true (1) if the change is an indirect change, or false (0) otherwise. See the documentation for [sqlite3session_indirect()](../session/sqlite3session_indirect.md) for a description of direct and indirect changes.

If no error occurs, SQLITE_OK is returned. If an error does occur, an SQLite error code is returned. The values of the output variables may not be trusted in this case.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
