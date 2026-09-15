---
title: ALTER SCHEMA
description: change the definition of a schema
source_url: https://www.postgresql.org/docs/17/sql-alterschema.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_schema.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1500
---

ALTER SCHEMA

ALTER SCHEMA

7

SQL - Language Statements

ALTER SCHEMA

change the definition of a schema

ALTER SCHEMA

name

RENAME TO

new_name

ALTER SCHEMA

name

OWNER TO {

new_owner

\| CURRENT_ROLE \| CURRENT_USER \| SESSION_USER }

## Description

`ALTER SCHEMA` changes the definition of a schema.

You must own the schema to use `ALTER SCHEMA`. To rename a schema you must also have the `CREATE` privilege for the database. To alter the owner, you must be able to `SET ROLE` to the new owning role, and that role must have the `CREATE` privilege for the database. (Note that superusers have all these privileges automatically.)

## Parameters

\<name\>  
The name of an existing schema.

\<new_name\>  
The new name of the schema. The new name cannot begin with `pg_`, as such names are reserved for system schemas.

\<new_owner\>  
The new owner of the schema.

## Compatibility

There is no `ALTER SCHEMA` statement in the SQL standard.

## See Also
