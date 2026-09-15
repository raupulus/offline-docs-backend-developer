---
title: ABORT
description: abort the current transaction
source_url: https://www.postgresql.org/docs/17/sql-abort.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/abort.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1240
---

ABORT

ABORT

7

SQL - Language Statements

ABORT

abort the current transaction

ABORT \[ WORK \| TRANSACTION \] \[ AND \[ NO \] CHAIN \]

## Description

`ABORT` rolls back the current transaction and causes all the updates made by the transaction to be discarded. This command is identical in behavior to the standard SQL command [`ROLLBACK`](#sql-rollback), and is present only for historical reasons.

## Parameters

`WORK`; `TRANSACTION`  
Optional key words. They have no effect.

`AND CHAIN`  
If `AND CHAIN` is specified, a new transaction is immediately started with the same transaction characteristics (see [`SET TRANSACTION`](#sql-set-transaction)) as the just finished one. Otherwise, no new transaction is started.

## Notes

Use [`COMMIT`](#sql-commit) to successfully terminate a transaction.

Issuing `ABORT` outside of a transaction block emits a warning and otherwise has no effect.

## Examples

To abort all changes:

    ABORT;

## Compatibility

This command is a PostgreSQL extension present for historical reasons. `ROLLBACK` is the equivalent standard SQL command.

## See Also
