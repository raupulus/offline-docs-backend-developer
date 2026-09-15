---
title: DROP PUBLICATION
description: remove a publication
source_url: https://www.postgresql.org/docs/17/sql-droppublication.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_publication.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2490
---

DROP PUBLICATION

DROP PUBLICATION

7

SQL - Language Statements

DROP PUBLICATION

remove a publication

DROP PUBLICATION \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP PUBLICATION` removes an existing publication from the database.

A publication can only be dropped by its owner or a superuser.

## Parameters

`IF EXISTS`  
Do not throw an error if the publication does not exist. A notice is issued in this case.

\<name\>  
The name of an existing publication.

`CASCADE`; `RESTRICT`  
These key words do not have any effect, since there are no dependencies on publications.

## Examples

Drop a publication:

    DROP PUBLICATION mypublication;

## Compatibility

`DROP PUBLICATION` is a PostgreSQL extension.

## See Also
