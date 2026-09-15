---
title: Configure a Session Object
source_url: https://www.sqlite.org/session/sqlite3session_object_config.html
source_path: session/sqlite3session_object_config.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7170
---

[](../session/intro.md)

## Session Module C Interface

## Configure a Session Object

> int sqlite3session_object_config(sqlite3_session\*, int op, void \*pArg);\

This method is used to configure a session object after it has been created. At present the only valid values for the second parameter are [SQLITE_SESSION_OBJCONFIG_SIZE](../session/c_session_objconfig_rowid.md) and [SQLITE_SESSION_OBJCONFIG_ROWID](../session/c_session_objconfig_rowid.md).

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
