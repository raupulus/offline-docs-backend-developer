---
title: Concatenate Two Changeset Objects
source_url: https://www.sqlite.org/session/sqlite3changeset_concat.html
source_path: session/sqlite3changeset_concat.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6910
---

[](../session/intro.md)

## Session Module C Interface

## Concatenate Two Changeset Objects

> int sqlite3changeset_concat(\
>   int nA,                         /\* Number of bytes in buffer pA \*/\
>   void \*pA,                       /\* Pointer to buffer containing changeset A \*/\
>   int nB,                         /\* Number of bytes in buffer pB \*/\
>   void \*pB,                       /\* Pointer to buffer containing changeset B \*/\
>   int \*pnOut,                     /\* OUT: Number of bytes in output changeset \*/\
>   void \*\*ppOut                    /\* OUT: Buffer containing output changeset \*/\
> );\

This function is used to concatenate two changesets, A and B, into a single changeset. The result is a changeset equivalent to applying changeset A followed by changeset B.

This function combines the two input changesets using an sqlite3_changegroup object. Calling it produces similar results as the following code fragment:

\
  sqlite3_changegroup \*pGrp;\
  rc = sqlite3_changegroup_new(&pGrp);\
  if( rc==SQLITE_OK ) rc = sqlite3changegroup_add(pGrp, nA, pA);\
  if( rc==SQLITE_OK ) rc = sqlite3changegroup_add(pGrp, nB, pB);\
  if( rc==SQLITE_OK ){\
    rc = sqlite3changegroup_output(pGrp, pnOut, ppOut);\
  }else{\
    \*ppOut = 0;\
    \*pnOut = 0;\
  }\

Refer to the sqlite3_changegroup documentation below for details.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
