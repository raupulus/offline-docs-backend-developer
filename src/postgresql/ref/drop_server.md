---
title: DROP SERVER
description: remove a foreign server descriptor
source_url: https://www.postgresql.org/docs/17/sql-dropserver.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_server.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2550
---

DROP SERVER

DROP SERVER

7

SQL - Language Statements

DROP SERVER

remove a foreign server descriptor

DROP SERVER \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP SERVER` removes an existing foreign server descriptor. To execute this command, the current user must be the owner of the server.

## Parameters

`IF EXISTS`  
Do not throw an error if the server does not exist. A notice is issued in this case.

\<name\>  
The name of an existing server.

`CASCADE`  
Automatically drop objects that depend on the server (such as user mappings), and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the server if any objects depend on it. This is the default.

## Examples

Drop a server `foo` if it exists:

    DROP SERVER IF EXISTS foo;

## Compatibility

`DROP SERVER` conforms to ISO/IEC 9075-9 (SQL/MED). The `IF EXISTS` clause is a PostgreSQL extension.

## See Also
