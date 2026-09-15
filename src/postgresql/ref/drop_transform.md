---
title: DROP TRANSFORM
description: remove a transform
source_url: https://www.postgresql.org/docs/17/sql-droptransform.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_transform.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2600
---

DROP TRANSFORM

DROP TRANSFORM

7

SQL - Language Statements

DROP TRANSFORM

remove a transform

DROP TRANSFORM \[ IF EXISTS \] FOR

type_name

LANGUAGE

lang_name

\[ CASCADE \| RESTRICT \]

## Description

`DROP TRANSFORM` removes a previously defined transform.

To be able to drop a transform, you must own the type and the language. These are the same privileges that are required to create a transform.

## Parameters

`IF EXISTS`  
Do not throw an error if the transform does not exist. A notice is issued in this case.

\<type_name\>  
The name of the data type of the transform.

\<lang_name\>  
The name of the language of the transform.

`CASCADE`  
Automatically drop objects that depend on the transform, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the transform if any objects depend on it. This is the default.

## Examples

To drop the transform for type `hstore` and language `plpython3u`:

    DROP TRANSFORM FOR hstore LANGUAGE plpython3u;

## Compatibility

This form of `DROP TRANSFORM` is a PostgreSQL extension. See [???](#sql-createtransform) for details.

## See Also
