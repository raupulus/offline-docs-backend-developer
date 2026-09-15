---
title: Configure a changeset rebaser object.
source_url: https://www.sqlite.org/session/sqlite3rebaser_configure.html
source_path: session/sqlite3rebaser_configure.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7020
---

[](../session/intro.md)

## Session Module C Interface

## Configure a changeset rebaser object.

> int sqlite3rebaser_configure(\
>   sqlite3_rebaser\*, \
>   int nRebase, const void \*pRebase\
> ); \

**Important:** This interface is [experimental](../c3ref/experimental.md) and is subject to change without notice.

Configure the changeset rebaser object to rebase changesets according to the conflict resolutions described by buffer pRebase (size nRebase bytes), which must have been obtained from a previous call to sqlite3changeset_apply_v2().

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
