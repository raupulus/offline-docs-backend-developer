---
title: COMMIT
description: commit the current transaction
source_url: https://www.postgresql.org/docs/17/sql-commit.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/commit.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1750
---

COMMIT

COMMIT

7

SQL - Language Statements

COMMIT

commit the current transaction

COMMIT \[ WORK \| TRANSACTION \] \[ AND \[ NO \] CHAIN \]

## Description

`COMMIT` commits the current transaction. All changes made by the transaction become visible to others and are guaranteed to be durable if a crash occurs.

## Parameters

chained transactions

`WORK`; `TRANSACTION`  
Optional key words. They have no effect.

`AND CHAIN`  
If `AND CHAIN` is specified, a new transaction is immediately started with the same transaction characteristics (see [???](#sql-set-transaction)) as the just finished one. Otherwise, no new transaction is started.

## Notes

Use [???](#sql-rollback) to abort a transaction.

Issuing `COMMIT` when not inside a transaction does no harm, but it will provoke a warning message. `COMMIT AND CHAIN` when not inside a transaction is an error.

## Examples

To commit the current transaction and make all changes permanent:

    COMMIT;

## Compatibility

The command `COMMIT` conforms to the SQL standard. The form `COMMIT TRANSACTION` is a PostgreSQL extension.

## See Also
