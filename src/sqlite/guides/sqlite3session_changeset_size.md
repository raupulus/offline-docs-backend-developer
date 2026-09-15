---
title: Return An Upper-limit For The Size Of The Changeset
source_url: https://www.sqlite.org/session/sqlite3session_changeset_size.html
source_path: session/sqlite3session_changeset_size.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7080
---

[](../session/intro.md)

## Session Module C Interface

## Return An Upper-limit For The Size Of The Changeset

> sqlite3_int64 sqlite3session_changeset_size(sqlite3_session \*pSession);\

By default, this function always returns 0. For it to return a useful result, the sqlite3_session object must have been configured to enable this API using sqlite3session_object_config() with the SQLITE_SESSION_OBJCONFIG_SIZE verb.

When enabled, this function returns an upper limit, in bytes, for the size of the changeset that might be produced if sqlite3session_changeset() were called. The final changeset size might be equal to or smaller than the size in bytes returned by this function.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
