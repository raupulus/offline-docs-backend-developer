---
title: DROP TEXT SEARCH CONFIGURATION
description: remove a text search configuration
source_url: https://www.postgresql.org/docs/17/sql-droptsconfig.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_tsconfig.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2620
---

DROP TEXT SEARCH CONFIGURATION

DROP TEXT SEARCH CONFIGURATION

7

SQL - Language Statements

DROP TEXT SEARCH CONFIGURATION

remove a text search configuration

DROP TEXT SEARCH CONFIGURATION \[ IF EXISTS \]

name

\[ CASCADE \| RESTRICT \]

## Description

`DROP TEXT SEARCH CONFIGURATION` drops an existing text search configuration. To execute this command you must be the owner of the configuration.

## Parameters

`IF EXISTS`  
Do not throw an error if the text search configuration does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of an existing text search configuration.

`CASCADE`  
Automatically drop objects that depend on the text search configuration, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the text search configuration if any objects depend on it. This is the default.

## Examples

Remove the text search configuration `my_english`:

    DROP TEXT SEARCH CONFIGURATION my_english;

This command will not succeed if there are any existing indexes that reference the configuration in `to_tsvector` calls. Add `CASCADE` to drop such indexes along with the text search configuration.

## Compatibility

There is no `DROP TEXT SEARCH CONFIGURATION` statement in the SQL standard.

## See Also
