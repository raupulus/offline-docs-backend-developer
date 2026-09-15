---
title: CREATE GROUP
description: define a new database role
source_url: https://www.postgresql.org/docs/17/sql-creategroup.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/create_group.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1900
---

CREATE GROUP

CREATE GROUP

7

SQL - Language Statements

CREATE GROUP

define a new database role

CREATE GROUP

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

`CREATE GROUP` is now an alias for [???](#sql-createrole).

## Compatibility

There is no `CREATE GROUP` statement in the SQL standard.

## See Also
