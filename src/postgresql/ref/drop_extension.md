---
title: DROP EXTENSION
description: remove an extension
source_url: https://www.postgresql.org/docs/17/sql-dropextension.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_extension.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2350
---

DROP EXTENSION

DROP EXTENSION

7

SQL - Language Statements

DROP EXTENSION

remove an extension

DROP EXTENSION \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP EXTENSION` removes extensions from the database. Dropping an extension causes its member objects, and other explicitly dependent routines (see [???](#sql-alterroutine), the `DEPENDS ON EXTENSION extension_name` action), to be dropped as well.

You must own the extension to use `DROP EXTENSION`.

## Parameters

`IF EXISTS`  
Do not throw an error if the extension does not exist. A notice is issued in this case.

\<name\>  
The name of an installed extension.

`CASCADE`  
Automatically drop objects that depend on the extension, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
This option prevents the specified extensions from being dropped if other objects, besides these extensions, their members, and their explicitly dependent routines, depend on them. This is the default.

## Examples

To remove the extension `hstore` from the current database:

    DROP EXTENSION hstore;

This command will fail if any of `hstore`'s objects are in use in the database, for example if any tables have columns of the `hstore` type. Add the `CASCADE` option to forcibly remove those dependent objects as well.

## Compatibility

`DROP EXTENSION` is a PostgreSQL extension.

## See Also
