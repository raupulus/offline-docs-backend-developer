---
title: DROP TABLE
description: remove a table
source_url: https://www.postgresql.org/docs/17/sql-droptable.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_table.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2580
---

DROP TABLE

DROP TABLE

7

SQL - Language Statements

DROP TABLE

remove a table

DROP TABLE \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP TABLE` removes tables from the database. Only the table owner, the schema owner, and superuser can drop a table. To empty a table of rows without destroying the table, use [`DELETE`](#sql-delete) or [`TRUNCATE`](#sql-truncate).

`DROP TABLE` always removes any indexes, rules, triggers, and constraints that exist for the target table. However, to drop a table that is referenced by a view or a foreign-key constraint of another table, `CASCADE` must be specified. (`CASCADE` will remove a dependent view entirely, but in the foreign-key case it will only remove the foreign-key constraint, not the other table entirely.)

## Parameters

`IF EXISTS`  
Do not throw an error if the table does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of the table to drop.

`CASCADE`  
Automatically drop objects that depend on the table (such as views), and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the table if any objects depend on it. This is the default.

## Examples

To destroy two tables, `films` and `distributors`:

    DROP TABLE films, distributors;

## Compatibility

This command conforms to the SQL standard, except that the standard only allows one table to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
