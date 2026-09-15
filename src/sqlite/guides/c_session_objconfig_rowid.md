---
title: Options for sqlite3session_object_config
source_url: https://www.sqlite.org/session/c_session_objconfig_rowid.html
source_path: session/c_session_objconfig_rowid.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6660
---

[](../session/intro.md)

## Session Module C Interface

## Options for sqlite3session_object_config

> \#define SQLITE_SESSION_OBJCONFIG_SIZE  1\
> \#define SQLITE_SESSION_OBJCONFIG_ROWID 2\

The following values may passed as the the 2nd parameter to sqlite3session_object_config().

SQLITE_SESSION_OBJCONFIG_SIZE

This option is used to set, clear or query the flag that enables the [sqlite3session_changeset_size()](../session/sqlite3session_changeset_size.md) API. Because it imposes some computational overhead, this API is disabled by default. Argument pArg must point to a value of type (int). If the value is initially 0, then the sqlite3session_changeset_size() API is disabled. If it is greater than 0, then the same API is enabled. Or, if the initial value is less than zero, no change is made. In all cases the (int) variable is set to 1 if the sqlite3session_changeset_size() API is enabled following the current call, or 0 otherwise.

It is an error (SQLITE_MISUSE) to attempt to modify this setting after the first table has been attached to the session object.

SQLITE_SESSION_OBJCONFIG_ROWID

This option is used to set, clear or query the flag that enables collection of data for tables with no explicit PRIMARY KEY.

Normally, tables with no explicit PRIMARY KEY are simply ignored by the sessions module. However, if this flag is set, it behaves as if such tables have a column "\_rowid\_ INTEGER PRIMARY KEY" inserted as their leftmost columns.

It is an error (SQLITE_MISUSE) to attempt to modify this setting after the first table has been attached to the session object.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
