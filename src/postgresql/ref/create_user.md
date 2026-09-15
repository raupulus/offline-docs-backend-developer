---
title: CREATE USER
description: define a new database role
source_url: https://www.postgresql.org/docs/17/sql-createuser.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/create_user.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2170
---

CREATE USER

CREATE USER

7

SQL - Language Statements

CREATE USER

define a new database role

CREATE USER

name

\[ \[ WITH \]

option

\[ ... \] \]

where

option

can be:

SUPERUSER \| NOSUPERUSER \| CREATEDB \| NOCREATEDB \| CREATEROLE \| NOCREATEROLE \| INHERIT \| NOINHERIT \| LOGIN \| NOLOGIN \| REPLICATION \| NOREPLICATION \| BYPASSRLS \| NOBYPASSRLS \| CONNECTION LIMIT

connlimit

\| \[ ENCRYPTED \] PASSWORD '

password

' \| PASSWORD NULL \| VALID UNTIL '

timestamp

' \| IN ROLE

role_name

\[, ...\] \| IN GROUP

role_name

\[, ...\] \| ROLE

role_name

\[, ...\] \| ADMIN

role_name

\[, ...\] \| USER

role_name

\[, ...\] \| SYSID

uid

## Description

`CREATE USER` is now an alias for [`CREATE ROLE`](#sql-createrole). The only difference is that when the command is spelled `CREATE USER`, `LOGIN` is assumed by default, whereas `NOLOGIN` is assumed when the command is spelled `CREATE ROLE`.

## Compatibility

The `CREATE USER` statement is a PostgreSQL extension. The SQL standard leaves the definition of users to the implementation.

## See Also
