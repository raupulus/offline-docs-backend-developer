---
title: CREATE MATERIALIZED VIEW
description: define a new materialized view
source_url: https://www.postgresql.org/docs/17/sql-creatematerializedview.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/create_materialized_view.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1930
---

CREATE MATERIALIZED VIEW

CREATE MATERIALIZED VIEW

7

SQL - Language Statements

CREATE MATERIALIZED VIEW

define a new materialized view

CREATE MATERIALIZED VIEW \[ IF NOT EXISTS \]

table_name

\[ (

column_name

\[, ...\] ) \] \[ USING

method

\] \[ WITH (

storage_parameter

\[=

value

\] \[, ... \] ) \] \[ TABLESPACE

tablespace_name

\] AS

query

\[ WITH \[ NO \] DATA \]

## Description

`CREATE MATERIALIZED VIEW` defines a materialized view of a query. The query is executed and used to populate the view at the time the command is issued (unless `WITH NO DATA` is used) and may be refreshed later using `REFRESH MATERIALIZED VIEW`.

`CREATE MATERIALIZED VIEW` is similar to `CREATE TABLE AS`, except that it also remembers the query used to initialize the view, so that it can be refreshed later upon demand. A materialized view has many of the same properties as a table, but there is no support for temporary materialized views.

`CREATE MATERIALIZED VIEW` requires `CREATE` privilege on the schema used for the materialized view.

## Parameters

`IF NOT EXISTS`  
Do not throw an error if a materialized view with the same name already exists. A notice is issued in this case. Note that there is no guarantee that the existing materialized view is anything like the one that would have been created.

\<table_name\>  
The name (optionally schema-qualified) of the materialized view to be created. The name must be distinct from the name of any other relation (table, sequence, index, view, materialized view, or foreign table) in the same schema.

\<column_name\>  
The name of a column in the new materialized view. If column names are not provided, they are taken from the output column names of the query.

`USING method`  
This optional clause specifies the table access method to use to store the contents for the new materialized view; the method needs be an access method of type `TABLE`. See [???](#tableam) for more information. If this option is not specified, the default table access method is chosen for the new materialized view. See [???](#guc-default-table-access-method) for more information.

`WITH ( storage_parameter [= value] [, ... ] )`  
This clause specifies optional storage parameters for the new materialized view; see [???](#sql-createtable-storage-parameters) in the [???](#sql-createtable) documentation for more information. All parameters supported for `CREATE TABLE` are also supported for `CREATE MATERIALIZED VIEW`. See [???](#sql-createtable) for more information.

`TABLESPACE tablespace_name`  
The \<tablespace_name\> is the name of the tablespace in which the new materialized view is to be created. If not specified, [???](#guc-default-tablespace) is consulted.

\<query\>  
A [`SELECT`](#sql-select), [`TABLE`](#sql-table), or [`VALUES`](#sql-values) command. This query will run within a security-restricted operation; in particular, calls to functions that themselves create temporary tables will fail. Also, while the query is running, the [???](#guc-search-path) is temporarily changed to `pg_catalog, pg_temp`.

`WITH [ NO ] DATA`  
This clause specifies whether or not the materialized view should be populated at creation time. If not, the materialized view will be flagged as unscannable and cannot be queried until `REFRESH MATERIALIZED VIEW` is used.

## Compatibility

`CREATE MATERIALIZED VIEW` is a PostgreSQL extension.

## See Also
