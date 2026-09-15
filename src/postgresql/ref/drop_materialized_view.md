---
title: DROP MATERIALIZED VIEW
description: remove a materialized view
source_url: https://www.postgresql.org/docs/17/sql-dropmaterializedview.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_materialized_view.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2420
---

DROP MATERIALIZED VIEW

DROP MATERIALIZED VIEW

7

SQL - Language Statements

DROP MATERIALIZED VIEW

remove a materialized view

DROP MATERIALIZED VIEW \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP MATERIALIZED VIEW` drops an existing materialized view. To execute this command you must be the owner of the materialized view.

## Parameters

`IF EXISTS`  
Do not throw an error if the materialized view does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of the materialized view to remove.

`CASCADE`  
Automatically drop objects that depend on the materialized view (such as other materialized views, or regular views), and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the materialized view if any objects depend on it. This is the default.

## Examples

This command will remove the materialized view called `order_summary`:

    DROP MATERIALIZED VIEW order_summary;

## Compatibility

`DROP MATERIALIZED VIEW` is a PostgreSQL extension.

## See Also
