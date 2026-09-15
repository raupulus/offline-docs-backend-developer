---
title: Flags for sqlite3changeset_apply_v2
source_url: https://www.sqlite.org/session/c_changesetapply_fknoaction.html
source_path: session/c_changesetapply_fknoaction.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6630
---

[](../session/intro.md)

## Session Module C Interface

## Flags for sqlite3changeset_apply_v2

> \#define SQLITE_CHANGESETAPPLY_NOSAVEPOINT   0x0001\
> \#define SQLITE_CHANGESETAPPLY_INVERT        0x0002\
> \#define SQLITE_CHANGESETAPPLY_IGNORENOOP    0x0004\
> \#define SQLITE_CHANGESETAPPLY_FKNOACTION    0x0008\
> \#define SQLITE_CHANGESETAPPLY_NOUPDATELOOP  0x0010\

The following flags may passed via the 9th parameter to [sqlite3changeset_apply_v2](../session/sqlite3changeset_apply.md) and [sqlite3changeset_apply_v2_strm](../session/sqlite3changegroup_add_strm.md):

SQLITE_CHANGESETAPPLY_NOSAVEPOINT

Usually, the sessions module encloses all operations performed by a single call to apply_v2() or apply_v2_strm() in a [SAVEPOINT](../lang_savepoint.md). The SAVEPOINT is committed if the changeset or patchset is successfully applied, or rolled back if an error occurs. Specifying this flag causes the sessions module to omit this savepoint. In this case, if the caller has an open transaction or savepoint when apply_v2() is called, it may revert the partially applied changeset by rolling it back.

SQLITE_CHANGESETAPPLY_INVERT

Invert the changeset before applying it. This is equivalent to inverting a changeset using sqlite3changeset_invert() before applying it. It is an error to specify this flag with a patchset.

SQLITE_CHANGESETAPPLY_IGNORENOOP

Do not invoke the conflict handler callback for any changes that would not actually modify the database even if they were applied. Specifically, this means that the conflict handler is not invoked for:

- a delete change if the row being deleted cannot be found,
- an update change if the modified fields are already set to their new values in the conflicting row, or
- an insert change if all fields of the conflicting row match the row being inserted.

SQLITE_CHANGESETAPPLY_FKNOACTION

If this flag it set, then all foreign key constraints in the target database behave as if they were declared with "ON UPDATE NO ACTION ON DELETE NO ACTION", even if they are actually CASCADE, RESTRICT, SET NULL or SET DEFAULT.

SQLITE_CHANGESETAPPLY_NOUPDATELOOP

Sometimes, a changeset contains two or more update statements such that although after applying all updates the database will contain no constraint violations, no single update can be applied before the others. The simplest example of this is a pair of UPDATEs that have "swapped" two column values with a UNIQUE constraint.

Usually, sqlite3changeset_apply() and similar functions work hard to try to find a way to apply such a changeset. However, if this flag is set, then all such updates are considered CONSTRAINT conflicts.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
