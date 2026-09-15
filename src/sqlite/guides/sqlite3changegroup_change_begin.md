---
title: Begin adding a change to a changegroup
source_url: https://www.sqlite.org/session/sqlite3changegroup_change_begin.html
source_path: session/sqlite3changegroup_change_begin.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6780
---

[](../session/intro.md)

## Session Module C Interface

## Begin adding a change to a changegroup

> int sqlite3changegroup_change_begin(\
>   sqlite3_changegroup\*,\
>   int eOp,\
>   const char \*zTab,\
>   int bIndirect,\
>   char \*\*pzErr\
> );\

This API is used, in concert with other sqlite3changegroup_change_xxx() APIs, to add changes to a changegroup object one at a time. To add a single change, the caller must:

1\. Invoke sqlite3changegroup_change_begin() to indicate the type of change (INSERT, UPDATE or DELETE), the affected table and whether or not the change should be marked as indirect.

2\. Invoke sqlite3changegroup_change_int64() or one of the other four value functions - \_null(), \_double(), \_text() or \_blob() - one or more times to specify old.\* and new.\* values for the change being constructed.

3\. Invoke sqlite3changegroup_change_finish() to either finish adding the change to the group, or to discard the change altogether.

The first argument to this function must be a pointer to the existing changegroup object that the change will be added to. The second argument must be SQLITE_INSERT, SQLITE_UPDATE or SQLITE_DELETE. The third is the name of the table that the change affects, and the fourth is a boolean flag specifying whether the change should be marked as "indirect" (if bIndirect is non-zero) or not indirect (if bIndirect is zero).

Following a successful call to this function, this function may not be called again on the same changegroup object until after sqlite3changegroup_change_finish() has been called. Doing so is an SQLITE_MISUSE error.

The changegroup object passed as the first argument must be already configured with schema data for the specified table. It may be configured either by calling sqlite3changegroup_schema() with a database that contains the table, or sqlite3changegroup_add() with a changeset that contains the table. If the changegroup object has not been configured with a schema for the specified table when this function is called, SQLITE_ERROR is returned.

If successful, SQLITE_OK is returned. Otherwise, if an error occurs, an SQLite error code is returned. In this case, if argument pzErr is non-NULL, then (\*pzErr) may be set to point to a buffer containing a utf-8 formated, nul-terminated, English language error message. It is the responsibility of the caller to eventually free this buffer using sqlite3_free().

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
