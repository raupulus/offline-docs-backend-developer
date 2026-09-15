---
title: ROLLBACK TO SAVEPOINT
description: roll back to a savepoint
source_url: https://www.postgresql.org/docs/17/sql-rollback-to.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/rollback_to.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 3240
---

ROLLBACK TO SAVEPOINT

savepoints

rolling back

ROLLBACK TO SAVEPOINT

7

SQL - Language Statements

ROLLBACK TO SAVEPOINT

roll back to a savepoint

ROLLBACK \[ WORK \| TRANSACTION \] TO \[ SAVEPOINT \]

savepoint_name

## Description

Roll back all commands that were executed after the savepoint was established and then start a new subtransaction at the same transaction level. The savepoint remains valid and can be rolled back to again later, if needed.

`ROLLBACK TO SAVEPOINT` implicitly destroys all savepoints that were established after the named savepoint.

## Parameters

\<savepoint_name\>  
The savepoint to roll back to.

## Notes

Use [`RELEASE SAVEPOINT`](#sql-release-savepoint) to destroy a savepoint without discarding the effects of commands executed after it was established.

Specifying a savepoint name that has not been established is an error.

Cursors have somewhat non-transactional behavior with respect to savepoints. Any cursor that is opened inside a savepoint will be closed when the savepoint is rolled back. If a previously opened cursor is affected by a `FETCH` or `MOVE` command inside a savepoint that is later rolled back, the cursor remains at the position that `FETCH` left it pointing to (that is, the cursor motion caused by `FETCH` is not rolled back). Closing a cursor is not undone by rolling back, either. However, other side-effects caused by the cursor's query (such as side-effects of volatile functions called by the query) *are* rolled back if they occur during a savepoint that is later rolled back. A cursor whose execution causes a transaction to abort is put in a cannot-execute state, so while the transaction can be restored using `ROLLBACK TO SAVEPOINT`, the cursor can no longer be used.

## Examples

To undo the effects of the commands executed after `my_savepoint` was established:

    ROLLBACK TO SAVEPOINT my_savepoint;

Cursor positions are not affected by savepoint rollback:

    BEGIN;

    DECLARE foo CURSOR FOR SELECT 1 UNION SELECT 2;

    SAVEPOINT foo;

    FETCH 1 FROM foo;
     ?column?
    ----------
            1

    ROLLBACK TO SAVEPOINT foo;

    FETCH 1 FROM foo;
     ?column?
    ----------
            2

    COMMIT;

## Compatibility

The SQL standard specifies that the key word `SAVEPOINT` is mandatory, but PostgreSQL and Oracle allow it to be omitted. SQL allows only `WORK`, not `TRANSACTION`, as a noise word after `ROLLBACK`. Also, SQL has an optional clause `AND [ NO ] CHAIN` which is not currently supported by PostgreSQL. Otherwise, this command conforms to the SQL standard.

## See Also
