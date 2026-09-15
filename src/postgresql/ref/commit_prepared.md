---
title: COMMIT PREPARED
description: commit a transaction that was earlier prepared for two-phase commit
source_url: https://www.postgresql.org/docs/17/sql-commit-prepared.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/commit_prepared.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1760
---

COMMIT PREPARED

COMMIT PREPARED

7

SQL - Language Statements

COMMIT PREPARED

commit a transaction that was earlier prepared for two-phase commit

COMMIT PREPARED

transaction_id

## Description

`COMMIT PREPARED` commits a transaction that is in prepared state.

## Parameters

\<transaction_id\>  
The transaction identifier of the transaction that is to be committed.

## Notes

To commit a prepared transaction, you must be either the same user that executed the transaction originally, or a superuser. But you do not have to be in the same session that executed the transaction.

This command cannot be executed inside a transaction block. The prepared transaction is committed immediately.

All currently available prepared transactions are listed in the [pg_prepared_xacts](#view-pg-prepared-xacts) system view.

## Examples

Commit the transaction identified by the transaction identifier `foobar`:

    COMMIT PREPARED 'foobar';

## Compatibility

`COMMIT PREPARED` is a PostgreSQL extension. It is intended for use by external transaction management systems, some of which are covered by standards (such as X/Open XA), but the SQL side of those systems is not standardized.

## See Also
