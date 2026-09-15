---
title: Delete a changeset rebaser object.
source_url: https://www.sqlite.org/session/sqlite3rebaser_delete.html
source_path: session/sqlite3rebaser_delete.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7040
---

[](../session/intro.md)

## Session Module C Interface

## Delete a changeset rebaser object.

> void sqlite3rebaser_delete(sqlite3_rebaser \*p); \

**Important:** This interface is [experimental](../c3ref/experimental.md) and is subject to change without notice.

Delete the changeset rebaser object and all associated resources. There should be one call to this function for each successful invocation of sqlite3rebaser_create().

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
