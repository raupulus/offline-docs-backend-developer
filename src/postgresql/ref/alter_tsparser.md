---
title: ALTER TEXT SEARCH PARSER
description: change the definition of a text search parser
source_url: https://www.postgresql.org/docs/17/sql-altertsparser.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_tsparser.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1610
---

ALTER TEXT SEARCH PARSER

ALTER TEXT SEARCH PARSER

7

SQL - Language Statements

ALTER TEXT SEARCH PARSER

change the definition of a text search parser

ALTER TEXT SEARCH PARSER

name

RENAME TO

new_name

ALTER TEXT SEARCH PARSER

name

SET SCHEMA

new_schema

## Description

`ALTER TEXT SEARCH PARSER` changes the definition of a text search parser. Currently, the only supported functionality is to change the parser's name.

You must be a superuser to use `ALTER TEXT SEARCH PARSER`.

## Parameters

\<name\>  
The name (optionally schema-qualified) of an existing text search parser.

\<new_name\>  
The new name of the text search parser.

\<new_schema\>  
The new schema for the text search parser.

## Compatibility

There is no `ALTER TEXT SEARCH PARSER` statement in the SQL standard.

## See Also
