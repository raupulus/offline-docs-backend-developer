---
title: DROP ACCESS METHOD
description: remove an access method
source_url: https://www.postgresql.org/docs/17/sql-drop-access-method.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_access_method.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2270
---

DROP ACCESS METHOD

DROP ACCESS METHOD

7

SQL - Language Statements

DROP ACCESS METHOD

remove an access method

DROP ACCESS METHOD \[ IF EXISTS \]

name

\[ CASCADE \| RESTRICT \]

## Description

`DROP ACCESS METHOD` removes an existing access method. Only superusers can drop access methods.

## Parameters

`IF EXISTS`  
Do not throw an error if the access method does not exist. A notice is issued in this case.

\<name\>  
The name of an existing access method.

`CASCADE`  
Automatically drop objects that depend on the access method (such as operator classes, operator families, and indexes), and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the access method if any objects depend on it. This is the default.

## Examples

Drop the access method `heptree`:

    DROP ACCESS METHOD heptree;

## Compatibility

`DROP ACCESS METHOD` is a PostgreSQL extension.

## See Also
