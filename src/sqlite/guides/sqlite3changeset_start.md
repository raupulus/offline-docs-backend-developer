---
title: Create An Iterator To Traverse A Changeset
source_url: https://www.sqlite.org/session/sqlite3changeset_start.html
source_path: session/sqlite3changeset_start.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7010
---

[](../session/intro.md)

## Session Module C Interface

## Create An Iterator To Traverse A Changeset

> int sqlite3changeset_start(\
>   sqlite3_changeset_iter \*\*pp,    /\* OUT: New changeset iterator handle \*/\
>   int nChangeset,                 /\* Size of changeset blob in bytes \*/\
>   void \*pChangeset                /\* Pointer to blob containing changeset \*/\
> );\
> int sqlite3changeset_start_v2(\
>   sqlite3_changeset_iter \*\*pp,    /\* OUT: New changeset iterator handle \*/\
>   int nChangeset,                 /\* Size of changeset blob in bytes \*/\
>   void \*pChangeset,               /\* Pointer to blob containing changeset \*/\
>   int flags                       /\* SESSION_CHANGESETSTART\_\* flags \*/\
> );\

Create an iterator used to iterate through the contents of a changeset. If successful, \*pp is set to point to the iterator handle and SQLITE_OK is returned. Otherwise, if an error occurs, \*pp is set to zero and an SQLite error code is returned.

The following functions can be used to advance and query a changeset iterator created by this function:

- [sqlite3changeset_next()](../session/sqlite3changeset_next.md)
- [sqlite3changeset_op()](../session/sqlite3changeset_op.md)
- [sqlite3changeset_new()](../session/sqlite3changeset_new.md)
- [sqlite3changeset_old()](../session/sqlite3changeset_old.md)

It is the responsibility of the caller to eventually destroy the iterator by passing it to [sqlite3changeset_finalize()](../session/sqlite3changeset_finalize.md). The buffer containing the changeset (pChangeset) must remain valid until after the iterator is destroyed.

Assuming the changeset blob was created by one of the [sqlite3session_changeset()](../session/sqlite3session_changeset.md), [sqlite3changeset_concat()](../session/sqlite3changeset_concat.md) or [sqlite3changeset_invert()](../session/sqlite3changeset_invert.md) functions, all changes within the changeset that apply to a single table are grouped together. This means that when an application iterates through a changeset using an iterator created by this function, all changes that relate to a single table are visited consecutively. There is no chance that the iterator will visit a change the applies to table X, then one for table Y, and then later on visit another change for table X.

The behavior of sqlite3changeset_start_v2() and its streaming equivalent may be modified by passing a combination of [supported flags](../session/c_changesetstart_invert.md) as the 4th parameter.

Note that the sqlite3changeset_start_v2() API is still **experimental** and therefore subject to change.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
