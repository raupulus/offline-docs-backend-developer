---
title: Enable Or Disable A Session Object
source_url: https://www.sqlite.org/session/sqlite3session_enable.html
source_path: session/sqlite3session_enable.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7130
---

[](../session/intro.md)

## Session Module C Interface

## Enable Or Disable A Session Object

> int sqlite3session_enable(sqlite3_session \*pSession, int bEnable);\

Enable or disable the recording of changes by a session object. When enabled, a session object records changes made to the database. When disabled - it does not. A newly created session object is enabled. Refer to the documentation for [sqlite3session_changeset()](../session/sqlite3session_changeset.md) for further details regarding how enabling and disabling a session object affects the eventual changesets.

Passing zero to this function disables the session. Passing a value greater than zero enables it. Passing a value less than zero is a no-op, and may be used to query the current state of the session.

The return value indicates the final state of the session object: 0 if the session is disabled, or 1 if it is enabled.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
