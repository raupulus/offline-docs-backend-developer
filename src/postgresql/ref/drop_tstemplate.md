---
title: DROP TEXT SEARCH TEMPLATE
description: remove a text search template
source_url: https://www.postgresql.org/docs/17/sql-droptstemplate.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_tstemplate.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2650
---

DROP TEXT SEARCH TEMPLATE

DROP TEXT SEARCH TEMPLATE

7

SQL - Language Statements

DROP TEXT SEARCH TEMPLATE

remove a text search template

DROP TEXT SEARCH TEMPLATE \[ IF EXISTS \]

name

\[ CASCADE \| RESTRICT \]

## Description

`DROP TEXT SEARCH TEMPLATE` drops an existing text search template. You must be a superuser to use this command.

## Parameters

`IF EXISTS`  
Do not throw an error if the text search template does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of an existing text search template.

`CASCADE`  
Automatically drop objects that depend on the text search template, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the text search template if any objects depend on it. This is the default.

## Examples

Remove the text search template `thesaurus`:

    DROP TEXT SEARCH TEMPLATE thesaurus;

This command will not succeed if there are any existing text search dictionaries that use the template. Add `CASCADE` to drop such dictionaries along with the template.

## Compatibility

There is no `DROP TEXT SEARCH TEMPLATE` statement in the SQL standard.

## See Also
