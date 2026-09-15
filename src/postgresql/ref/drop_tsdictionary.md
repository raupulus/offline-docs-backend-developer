---
title: DROP TEXT SEARCH DICTIONARY
description: remove a text search dictionary
source_url: https://www.postgresql.org/docs/17/sql-droptsdictionary.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_tsdictionary.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2630
---

DROP TEXT SEARCH DICTIONARY

DROP TEXT SEARCH DICTIONARY

7

SQL - Language Statements

DROP TEXT SEARCH DICTIONARY

remove a text search dictionary

DROP TEXT SEARCH DICTIONARY \[ IF EXISTS \]

name

\[ CASCADE \| RESTRICT \]

## Description

`DROP TEXT SEARCH DICTIONARY` drops an existing text search dictionary. To execute this command you must be the owner of the dictionary.

## Parameters

`IF EXISTS`  
Do not throw an error if the text search dictionary does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of an existing text search dictionary.

`CASCADE`  
Automatically drop objects that depend on the text search dictionary, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the text search dictionary if any objects depend on it. This is the default.

## Examples

Remove the text search dictionary `english`:

    DROP TEXT SEARCH DICTIONARY english;

This command will not succeed if there are any existing text search configurations that use the dictionary. Add `CASCADE` to drop such configurations along with the dictionary.

## Compatibility

There is no `DROP TEXT SEARCH DICTIONARY` statement in the SQL standard.

## See Also
