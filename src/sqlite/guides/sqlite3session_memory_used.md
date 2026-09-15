---
title: Query for the amount of heap memory used by a session object.
source_url: https://www.sqlite.org/session/sqlite3session_memory_used.html
source_path: session/sqlite3session_memory_used.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7160
---

[](../session/intro.md)

## Session Module C Interface

## Query for the amount of heap memory used by a session object.

> sqlite3_int64 sqlite3session_memory_used(sqlite3_session \*pSession);\

This API returns the total amount of heap memory in bytes currently used by the session object passed as the only argument.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
