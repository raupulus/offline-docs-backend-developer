---
title: Create a changeset rebaser object.
source_url: https://www.sqlite.org/session/sqlite3rebaser_create.html
source_path: session/sqlite3rebaser_create.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7030
---

[](../session/intro.md)

## Session Module C Interface

## Create a changeset rebaser object.

> int sqlite3rebaser_create(sqlite3_rebaser \*\*ppNew);\

**Important:** This interface is [experimental](../c3ref/experimental.md) and is subject to change without notice.

Allocate a new changeset rebaser object. If successful, set (\*ppNew) to point to the new object and return SQLITE_OK. Otherwise, if an error occurs, return an SQLite error code (e.g. SQLITE_NOMEM) and set (\*ppNew) to NULL.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
