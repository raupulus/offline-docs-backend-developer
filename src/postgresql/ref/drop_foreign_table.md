---
title: DROP FOREIGN TABLE
description: remove a foreign table
source_url: https://www.postgresql.org/docs/17/sql-dropforeigntable.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_foreign_table.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2370
---

DROP FOREIGN TABLE

DROP FOREIGN TABLE

7

SQL - Language Statements

DROP FOREIGN TABLE

remove a foreign table

DROP FOREIGN TABLE \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP FOREIGN TABLE` removes a foreign table. Only the owner of a foreign table can remove it.

## Parameters

`IF EXISTS`  
Do not throw an error if the foreign table does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of the foreign table to drop.

`CASCADE`  
Automatically drop objects that depend on the foreign table (such as views), and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the foreign table if any objects depend on it. This is the default.

## Examples

To destroy two foreign tables, `films` and `distributors`:

    DROP FOREIGN TABLE films, distributors;

## Compatibility

This command conforms to ISO/IEC 9075-9 (SQL/MED), except that the standard only allows one foreign table to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
