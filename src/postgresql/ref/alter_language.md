---
title: ALTER LANGUAGE
description: change the definition of a procedural language
source_url: https://www.postgresql.org/docs/17/sql-alterlanguage.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_language.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1380
---

ALTER LANGUAGE

ALTER LANGUAGE

7

SQL - Language Statements

ALTER LANGUAGE

change the definition of a procedural language

ALTER \[ PROCEDURAL \] LANGUAGE

name

RENAME TO

new_name

ALTER \[ PROCEDURAL \] LANGUAGE

name

OWNER TO {

new_owner

\| CURRENT_ROLE \| CURRENT_USER \| SESSION_USER }

## Description

`ALTER LANGUAGE` changes the definition of a procedural language. The only functionality is to rename the language or assign a new owner. You must be superuser or owner of the language to use `ALTER LANGUAGE`.

## Parameters

\<name\>  
Name of a language

\<new_name\>  
The new name of the language

\<new_owner\>  
The new owner of the language

## Compatibility

There is no `ALTER LANGUAGE` statement in the SQL standard.

## See Also
