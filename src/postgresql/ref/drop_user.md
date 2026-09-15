---
title: DROP USER
description: remove a database role
source_url: https://www.postgresql.org/docs/17/sql-dropuser.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_user.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2670
---

DROP USER

DROP USER

7

SQL - Language Statements

DROP USER

remove a database role

DROP USER \[ IF EXISTS \]

name

\[, ...\]

## Description

`DROP USER` is simply an alternate spelling of [`DROP ROLE`](#sql-droprole).

## Compatibility

The `DROP USER` statement is a PostgreSQL extension. The SQL standard leaves the definition of users to the implementation.

## See Also
