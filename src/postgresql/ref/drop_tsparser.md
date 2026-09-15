---
title: DROP TEXT SEARCH PARSER
description: remove a text search parser
source_url: https://www.postgresql.org/docs/17/sql-droptsparser.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_tsparser.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2640
---

DROP TEXT SEARCH PARSER

DROP TEXT SEARCH PARSER

7

SQL - Language Statements

DROP TEXT SEARCH PARSER

remove a text search parser

DROP TEXT SEARCH PARSER \[ IF EXISTS \]

name

\[ CASCADE \| RESTRICT \]

## Description

`DROP TEXT SEARCH PARSER` drops an existing text search parser. You must be a superuser to use this command.

## Parameters

`IF EXISTS`  
Do not throw an error if the text search parser does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of an existing text search parser.

`CASCADE`  
Automatically drop objects that depend on the text search parser, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the text search parser if any objects depend on it. This is the default.

## Examples

Remove the text search parser `my_parser`:

    DROP TEXT SEARCH PARSER my_parser;

This command will not succeed if there are any existing text search configurations that use the parser. Add `CASCADE` to drop such configurations along with the parser.

## Compatibility

There is no `DROP TEXT SEARCH PARSER` statement in the SQL standard.

## See Also
