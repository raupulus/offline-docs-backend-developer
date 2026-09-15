---
title: ALTER CONVERSION
description: change the definition of a conversion
source_url: https://www.postgresql.org/docs/17/sql-alterconversion.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_conversion.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1270
---

ALTER CONVERSION

ALTER CONVERSION

7

SQL - Language Statements

ALTER CONVERSION

change the definition of a conversion

ALTER CONVERSION

name

RENAME TO

new_name

ALTER CONVERSION

name

OWNER TO {

new_owner

\| CURRENT_ROLE \| CURRENT_USER \| SESSION_USER } ALTER CONVERSION

name

SET SCHEMA

new_schema

## Description

`ALTER CONVERSION` changes the definition of a conversion.

You must own the conversion to use `ALTER CONVERSION`. To alter the owner, you must be able to `SET ROLE` to the new owning role, and that role must have `CREATE` privilege on the conversion's schema. (These restrictions enforce that altering the owner doesn't do anything you couldn't do by dropping and recreating the conversion. However, a superuser can alter ownership of any conversion anyway.)

## Parameters

\<name\>  
The name (optionally schema-qualified) of an existing conversion.

\<new_name\>  
The new name of the conversion.

\<new_owner\>  
The new owner of the conversion.

\<new_schema\>  
The new schema for the conversion.

## Examples

To rename the conversion `iso_8859_1_to_utf8` to `latin1_to_unicode`:

    ALTER CONVERSION iso_8859_1_to_utf8 RENAME TO latin1_to_unicode;

To change the owner of the conversion `iso_8859_1_to_utf8` to `joe`:

    ALTER CONVERSION iso_8859_1_to_utf8 OWNER TO joe;

## Compatibility

There is no `ALTER CONVERSION` statement in the SQL standard.

## See Also
