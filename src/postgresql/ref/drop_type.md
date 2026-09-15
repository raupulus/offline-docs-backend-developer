---
title: DROP TYPE
description: remove a data type
source_url: https://www.postgresql.org/docs/17/sql-droptype.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_type.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2660
---

DROP TYPE

DROP TYPE

7

SQL - Language Statements

DROP TYPE

remove a data type

DROP TYPE \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP TYPE` removes a user-defined data type. Only the owner of a type can remove it.

## Parameters

`IF EXISTS`  
Do not throw an error if the type does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of the data type to remove.

`CASCADE`  
Automatically drop objects that depend on the type (such as table columns, functions, and operators), and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the type if any objects depend on it. This is the default.

## Examples

To remove the data type `box`:

    DROP TYPE box;

## Compatibility

This command is similar to the corresponding command in the SQL standard, apart from the `IF EXISTS` option, which is a PostgreSQL extension. But note that much of the `CREATE TYPE` command and the data type extension mechanisms in PostgreSQL differ from the SQL standard.

## See Also
