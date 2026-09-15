---
title: Test if a changeset has recorded any changes.
source_url: https://www.sqlite.org/session/sqlite3session_isempty.html
source_path: session/sqlite3session_isempty.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7150
---

[](../session/intro.md)

## Session Module C Interface

## Test if a changeset has recorded any changes.

> int sqlite3session_isempty(sqlite3_session \*pSession);\

Return non-zero if no changes to attached tables have been recorded by the session object passed as the first argument. Otherwise, if one or more changes have been recorded, return zero.

Even if this function returns zero, it is possible that calling [sqlite3session_changeset()](../session/sqlite3session_changeset.md) on the session handle may still return a changeset that contains no changes. This can happen when a row in an attached table is modified and then later on the original values are restored. However, if this function returns non-zero, then it is guaranteed that a call to sqlite3session_changeset() will return a changeset containing zero changes.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
