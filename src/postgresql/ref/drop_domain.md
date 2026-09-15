---
title: DROP DOMAIN
description: remove a domain
source_url: https://www.postgresql.org/docs/17/sql-dropdomain.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_domain.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2330
---

DROP DOMAIN

DROP DOMAIN

7

SQL - Language Statements

DROP DOMAIN

remove a domain

DROP DOMAIN \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP DOMAIN` removes a domain. Only the owner of a domain can remove it.

## Parameters

`IF EXISTS`  
Do not throw an error if the domain does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of an existing domain.

`CASCADE`  
Automatically drop objects that depend on the domain (such as table columns), and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the domain if any objects depend on it. This is the default.

## Examples

To remove the domain `box`:

    DROP DOMAIN box;

## Compatibility

This command conforms to the SQL standard, except for the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
