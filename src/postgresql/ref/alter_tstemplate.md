---
title: ALTER TEXT SEARCH TEMPLATE
description: change the definition of a text search template
source_url: https://www.postgresql.org/docs/17/sql-altertstemplate.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_tstemplate.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1620
---

ALTER TEXT SEARCH TEMPLATE

ALTER TEXT SEARCH TEMPLATE

7

SQL - Language Statements

ALTER TEXT SEARCH TEMPLATE

change the definition of a text search template

ALTER TEXT SEARCH TEMPLATE

name

RENAME TO

new_name

ALTER TEXT SEARCH TEMPLATE

name

SET SCHEMA

new_schema

## Description

`ALTER TEXT SEARCH TEMPLATE` changes the definition of a text search template. Currently, the only supported functionality is to change the template's name.

You must be a superuser to use `ALTER TEXT SEARCH TEMPLATE`.

## Parameters

\<name\>  
The name (optionally schema-qualified) of an existing text search template.

\<new_name\>  
The new name of the text search template.

\<new_schema\>  
The new schema for the text search template.

## Compatibility

There is no `ALTER TEXT SEARCH TEMPLATE` statement in the SQL standard.

## See Also
