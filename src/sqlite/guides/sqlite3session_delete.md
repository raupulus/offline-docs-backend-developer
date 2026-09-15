---
title: Delete A Session Object
source_url: https://www.sqlite.org/session/sqlite3session_delete.html
source_path: session/sqlite3session_delete.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7110
---

[](../session/intro.md)

## Session Module C Interface

## Delete A Session Object

> void sqlite3session_delete(sqlite3_session \*pSession);\

Delete a session object previously allocated using [sqlite3session_create()](../session/sqlite3session_create.md). Once a session object has been deleted, the results of attempting to use pSession with any other session module function are undefined.

Session objects must be deleted before the database handle to which they are attached is closed. Refer to the documentation for [sqlite3session_create()](../session/sqlite3session_create.md) for details.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
