---
title: DROP CAST
description: remove a cast
source_url: https://www.postgresql.org/docs/17/sql-dropcast.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_cast.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2290
---

DROP CAST

DROP CAST

7

SQL - Language Statements

DROP CAST

remove a cast

DROP CAST \[ IF EXISTS \] (

source_type

AS

target_type

) \[ CASCADE \| RESTRICT \]

## Description

`DROP CAST` removes a previously defined cast.

To be able to drop a cast, you must own the source or the target data type. These are the same privileges that are required to create a cast.

## Parameters

`IF EXISTS`  
Do not throw an error if the cast does not exist. A notice is issued in this case.

\<source_type\>  
The name of the source data type of the cast.

\<target_type\>  
The name of the target data type of the cast.

`CASCADE`; `RESTRICT`  
These key words do not have any effect, since there are no dependencies on casts.

## Examples

To drop the cast from type `text` to type `int`:

    DROP CAST (text AS int);

## Compatibility

The `DROP CAST` command conforms to the SQL standard.

## See Also
