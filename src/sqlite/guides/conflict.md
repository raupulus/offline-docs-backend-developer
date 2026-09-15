---
title: Constraint Conflict Resolution in SQLite
source_url: https://www.sqlite.org/conflict.html
source_path: conflict.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2530
---

# Constraint Conflict Resolution in SQLite

In most SQL databases, if you have a [UNIQUE](lang_createtable.md#uniqueconst), [NOT NULL](lang_createtable.md#notnullconst), or [CHECK](lang_createtable.md#ckconst) constraint on a table and you try to do an [UPDATE](lang_update.md) or [INSERT](lang_insert.md) that violates the constraint, the database will abort the operation in progress, back out any prior changes associated with the same UPDATE or INSERT statement, and return an error. This is the default behavior of SQLite, though SQLite also allows one to define alternative ways for dealing with constraint violations. This article describes those alternatives and how to use them.

## Conflict Resolution Algorithms

SQLite defines five constraint conflict resolution algorithms as follows:

**ROLLBACK**  
When a constraint violation occurs, an immediate ROLLBACK occurs, thus ending the current transaction, and the command aborts with a return code of SQLITE_CONSTRAINT. If no transaction is active (other than the implied transaction that is created on every command) then this algorithm works the same as ABORT.

**ABORT**  
When a constraint violation occurs, the command backs out any prior changes it might have made and aborts with a return code of SQLITE_CONSTRAINT. But no ROLLBACK is executed so changes from prior commands within the same transaction are preserved. This is the default behavior for SQLite.

**FAIL**  
When a constraint violation occurs, the command aborts with a return code SQLITE_CONSTRAINT. But any changes to the database that the command made prior to encountering the constraint violation are preserved and are not backed out. For example, if an UPDATE statement encountered a constraint violation on the 100th row that it attempts to update, then the first 99 row changes are preserved but change to rows 100 and beyond never occur.

**IGNORE**  
When a constraint violation occurs, the one row that contains the constraint violation is not inserted or changed. But the command continues executing normally. Other rows before and after the row that contained the constraint violation continue to be inserted or updated normally. No error is returned.

**REPLACE**  
When a UNIQUE constraint violation occurs, the pre-existing row that caused the constraint violation is removed prior to inserting or updating the current row. Thus the insert or update always occurs. The command continues executing normally. No error is returned.
