---
title: ROLLBACK
description: abort the current transaction
source_url: https://www.postgresql.org/docs/17/sql-rollback.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/rollback.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 3220
---

ROLLBACK

ROLLBACK

7

SQL - Language Statements

ROLLBACK

abort the current transaction

ROLLBACK \[ WORK \| TRANSACTION \] \[ AND \[ NO \] CHAIN \]

## Description

`ROLLBACK` rolls back the current transaction and causes all the updates made by the transaction to be discarded.

## Parameters

chained transactions

`WORK`; `TRANSACTION`  
Optional key words. They have no effect.

`AND CHAIN`  
If `AND CHAIN` is specified, a new (not aborted) transaction is immediately started with the same transaction characteristics (see [???](#sql-set-transaction)) as the just finished one. Otherwise, no new transaction is started.

## Notes

Use [`COMMIT`](#sql-commit) to successfully terminate a transaction.

Issuing `ROLLBACK` outside of a transaction block emits a warning and otherwise has no effect. `ROLLBACK AND CHAIN` outside of a transaction block is an error.

## Examples

To abort all changes:

    ROLLBACK;

## Compatibility

The command `ROLLBACK` conforms to the SQL standard. The form `ROLLBACK TRANSACTION` is a PostgreSQL extension.

## See Also
