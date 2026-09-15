---
title: Rebase a changeset
source_url: https://www.sqlite.org/session/sqlite3rebaser_rebase.html
source_path: session/sqlite3rebaser_rebase.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7050
---

[](../session/intro.md)

## Session Module C Interface

## Rebase a changeset

> int sqlite3rebaser_rebase(\
>   sqlite3_rebaser\*,\
>   int nIn, const void \*pIn, \
>   int \*pnOut, void \*\*ppOut \
> );\

**Important:** This interface is [experimental](../c3ref/experimental.md) and is subject to change without notice.

Argument pIn must point to a buffer containing a changeset nIn bytes in size. This function allocates and populates a buffer with a copy of the changeset rebased according to the configuration of the rebaser object passed as the first argument. If successful, (\*ppOut) is set to point to the new buffer containing the rebased changeset and (\*pnOut) to its size in bytes and SQLITE_OK returned. It is the responsibility of the caller to eventually free the new buffer using sqlite3_free(). Otherwise, if an error occurs, (\*ppOut) and (\*pnOut) are set to zero and an SQLite error code returned.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
