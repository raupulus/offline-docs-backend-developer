---
title: DROP COLLATION
description: remove a collation
source_url: https://www.postgresql.org/docs/17/sql-dropcollation.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_collation.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2300
---

DROP COLLATION

DROP COLLATION

7

SQL - Language Statements

DROP COLLATION

remove a collation

DROP COLLATION \[ IF EXISTS \]

name

\[ CASCADE \| RESTRICT \]

## Description

`DROP COLLATION` removes a previously defined collation. To be able to drop a collation, you must own the collation.

## Parameters

`IF EXISTS`  
Do not throw an error if the collation does not exist. A notice is issued in this case.

\<name\>  
The name of the collation. The collation name can be schema-qualified.

`CASCADE`  
Automatically drop objects that depend on the collation, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the collation if any objects depend on it. This is the default.

## Examples

To drop the collation named `german`:

    DROP COLLATION german;

## Compatibility

The `DROP COLLATION` command conforms to the SQL standard, apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
