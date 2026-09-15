---
title: DROP STATISTICS
description: remove extended statistics
source_url: https://www.postgresql.org/docs/17/sql-dropstatistics.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_statistics.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2560
---

DROP STATISTICS

DROP STATISTICS

7

SQL - Language Statements

DROP STATISTICS

remove extended statistics

DROP STATISTICS \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP STATISTICS` removes statistics object(s) from the database. Only the statistics object's owner, the schema owner, or a superuser can drop a statistics object.

## Parameters

`IF EXISTS`  
Do not throw an error if the statistics object does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of the statistics object to drop.

`CASCADE`; `RESTRICT`  
These key words do not have any effect, since there are no dependencies on statistics.

## Examples

To destroy two statistics objects in different schemas, without failing if they don't exist:

    DROP STATISTICS IF EXISTS
        accounting.users_uid_creation,
        public.grants_user_role;

## Compatibility

There is no `DROP STATISTICS` command in the SQL standard.

## See Also
