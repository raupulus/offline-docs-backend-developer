---
title: DEALLOCATE
description: deallocate a prepared statement
source_url: https://www.postgresql.org/docs/17/sql-deallocate.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/deallocate.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2220
---

DEALLOCATE

prepared statements

removing

DEALLOCATE

7

SQL - Language Statements

DEALLOCATE

deallocate a prepared statement

DEALLOCATE \[ PREPARE \] {

name

\| ALL }

## Description

`DEALLOCATE` is used to deallocate a previously prepared SQL statement. If you do not explicitly deallocate a prepared statement, it is deallocated when the session ends.

For more information on prepared statements, see [???](#sql-prepare).

## Parameters

`PREPARE`  
This key word is ignored.

\<name\>  
The name of the prepared statement to deallocate.

`ALL`  
Deallocate all prepared statements.

## Compatibility

The SQL standard includes a `DEALLOCATE` statement, but it is only for use in embedded SQL.

## See Also
