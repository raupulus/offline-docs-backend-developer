---
title: DROP VIEW
description: remove a view
source_url: https://www.postgresql.org/docs/17/sql-dropview.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_view.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2690
---

DROP VIEW

DROP VIEW

7

SQL - Language Statements

DROP VIEW

remove a view

DROP VIEW \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP VIEW` drops an existing view. To execute this command you must be the owner of the view.

## Parameters

`IF EXISTS`  
Do not throw an error if the view does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of the view to remove.

`CASCADE`  
Automatically drop objects that depend on the view (such as other views), and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the view if any objects depend on it. This is the default.

## Examples

This command will remove the view called `kinds`:

    DROP VIEW kinds;

## Compatibility

This command conforms to the SQL standard, except that the standard only allows one view to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
