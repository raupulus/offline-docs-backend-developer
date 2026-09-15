---
title: DROP TABLESPACE
description: remove a tablespace
source_url: https://www.postgresql.org/docs/17/sql-droptablespace.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_tablespace.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2590
---

DROP TABLESPACE

DROP TABLESPACE

7

SQL - Language Statements

DROP TABLESPACE

remove a tablespace

DROP TABLESPACE \[ IF EXISTS \]

name

## Description

`DROP TABLESPACE` removes a tablespace from the system.

A tablespace can only be dropped by its owner or a superuser. The tablespace must be empty of all database objects before it can be dropped. It is possible that objects in other databases might still reside in the tablespace even if no objects in the current database are using the tablespace. Also, if the tablespace is listed in the [???](#guc-temp-tablespaces) setting of any active session, the `DROP` might fail due to temporary files residing in the tablespace.

## Parameters

`IF EXISTS`  
Do not throw an error if the tablespace does not exist. A notice is issued in this case.

\<name\>  
The name of a tablespace.

## Notes

`DROP TABLESPACE` cannot be executed inside a transaction block.

## Examples

To remove tablespace `mystuff` from the system:

    DROP TABLESPACE mystuff;

## Compatibility

`DROP TABLESPACE` is a PostgreSQL extension.

## See Also
