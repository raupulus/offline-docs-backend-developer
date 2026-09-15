---
title: ROLLBACK PREPARED
description: cancel a transaction that was earlier prepared for two-phase commit
source_url: https://www.postgresql.org/docs/17/sql-rollback-prepared.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/rollback_prepared.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 3230
---

ROLLBACK PREPARED

ROLLBACK PREPARED

7

SQL - Language Statements

ROLLBACK PREPARED

cancel a transaction that was earlier prepared for two-phase commit

ROLLBACK PREPARED

transaction_id

## Description

`ROLLBACK PREPARED` rolls back a transaction that is in prepared state.

## Parameters

\<transaction_id\>  
The transaction identifier of the transaction that is to be rolled back.

## Notes

To roll back a prepared transaction, you must be either the same user that executed the transaction originally, or a superuser. But you do not have to be in the same session that executed the transaction.

This command cannot be executed inside a transaction block. The prepared transaction is rolled back immediately.

All currently available prepared transactions are listed in the [pg_prepared_xacts](#view-pg-prepared-xacts) system view.

## Examples

Roll back the transaction identified by the transaction identifier `foobar`:

    ROLLBACK PREPARED 'foobar';

## Compatibility

`ROLLBACK PREPARED` is a PostgreSQL extension. It is intended for use by external transaction management systems, some of which are covered by standards (such as X/Open XA), but the SQL side of those systems is not standardized.

## See Also
