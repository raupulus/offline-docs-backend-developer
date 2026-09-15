---
title: DROP FOREIGN DATA WRAPPER
description: remove a foreign-data wrapper
source_url: https://www.postgresql.org/docs/17/sql-dropforeigndatawrapper.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_foreign_data_wrapper.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2360
---

DROP FOREIGN DATA WRAPPER

DROP FOREIGN DATA WRAPPER

7

SQL - Language Statements

DROP FOREIGN DATA WRAPPER

remove a foreign-data wrapper

DROP FOREIGN DATA WRAPPER \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP FOREIGN DATA WRAPPER` removes an existing foreign-data wrapper. To execute this command, the current user must be the owner of the foreign-data wrapper.

## Parameters

`IF EXISTS`  
Do not throw an error if the foreign-data wrapper does not exist. A notice is issued in this case.

\<name\>  
The name of an existing foreign-data wrapper.

`CASCADE`  
Automatically drop objects that depend on the foreign-data wrapper (such as foreign tables and servers), and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the foreign-data wrapper if any objects depend on it. This is the default.

## Examples

Drop the foreign-data wrapper `dbi`:

    DROP FOREIGN DATA WRAPPER dbi;

## Compatibility

`DROP FOREIGN DATA WRAPPER` conforms to ISO/IEC 9075-9 (SQL/MED). The `IF EXISTS` clause is a PostgreSQL extension.

## See Also
