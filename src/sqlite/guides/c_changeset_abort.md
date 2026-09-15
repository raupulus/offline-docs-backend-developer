---
title: Constants Returned By The Conflict Handler
source_url: https://www.sqlite.org/session/c_changeset_abort.html
source_path: session/c_changeset_abort.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6610
---

[](../session/intro.md)

## Session Module C Interface

## Constants Returned By The Conflict Handler

> \#define SQLITE_CHANGESET_OMIT       0\
> \#define SQLITE_CHANGESET_REPLACE    1\
> \#define SQLITE_CHANGESET_ABORT      2\

A conflict handler callback must return one of the following three values.

SQLITE_CHANGESET_OMIT  
If a conflict handler returns this value no special action is taken. The change that caused the conflict is not applied. The session module continues to the next change in the changeset.

SQLITE_CHANGESET_REPLACE  
This value may only be returned if the second argument to the conflict handler was SQLITE_CHANGESET_DATA or SQLITE_CHANGESET_CONFLICT. If this is not the case, any changes applied so far are rolled back and the call to sqlite3changeset_apply() returns SQLITE_MISUSE.

If CHANGESET_REPLACE is returned by an SQLITE_CHANGESET_DATA conflict handler, then the conflicting row is either updated or deleted, depending on the type of change.

If CHANGESET_REPLACE is returned by an SQLITE_CHANGESET_CONFLICT conflict handler, then the conflicting row is removed from the database and a second attempt to apply the change is made. If this second attempt fails, the original row is restored to the database before continuing.

SQLITE_CHANGESET_ABORT  
If this value is returned, any changes applied so far are rolled back and the call to sqlite3changeset_apply() returns SQLITE_ABORT.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
