---
title: Finalize A Changeset Iterator
source_url: https://www.sqlite.org/session/sqlite3changeset_finalize.html
source_path: session/sqlite3changeset_finalize.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6930
---

[](../session/intro.md)

## Session Module C Interface

## Finalize A Changeset Iterator

> int sqlite3changeset_finalize(sqlite3_changeset_iter \*pIter);\

This function is used to finalize an iterator allocated with [sqlite3changeset_start()](../session/sqlite3changeset_start.md).

This function should only be called on iterators created using the [sqlite3changeset_start()](../session/sqlite3changeset_start.md) function. If an application calls this function with an iterator passed to a conflict-handler by [sqlite3changeset_apply()](../session/sqlite3changeset_apply.md), [SQLITE_MISUSE](../rescode.md#misuse) is immediately returned and the call has no effect.

If an error was encountered within a call to an sqlite3changeset_xxx() function (for example an [SQLITE_CORRUPT](../rescode.md#corrupt) in [sqlite3changeset_next()](../session/sqlite3changeset_next.md) or an [SQLITE_NOMEM](../rescode.md#nomem) in [sqlite3changeset_new()](../session/sqlite3changeset_new.md)) then an error code corresponding to that error is returned by this function. Otherwise, SQLITE_OK is returned. This is to allow the following pattern (pseudo-code):

\
  sqlite3changeset_start();\
  while( SQLITE_ROW==sqlite3changeset_next() ){\
    // Do something with change.\
  }\
  rc = sqlite3changeset_finalize();\
  if( rc!=SQLITE_OK ){\
    // An error has occurred \
  }\

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
