---
title: DROP TRIGGER
description: remove a trigger
source_url: https://www.postgresql.org/docs/17/sql-droptrigger.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_trigger.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2610
---

DROP TRIGGER

DROP TRIGGER

7

SQL - Language Statements

DROP TRIGGER

remove a trigger

DROP TRIGGER \[ IF EXISTS \]

name

ON

table_name

\[ CASCADE \| RESTRICT \]

## Description

`DROP TRIGGER` removes an existing trigger definition. To execute this command, the current user must be the owner of the table for which the trigger is defined.

## Parameters

`IF EXISTS`  
Do not throw an error if the trigger does not exist. A notice is issued in this case.

\<name\>  
The name of the trigger to remove.

\<table_name\>  
The name (optionally schema-qualified) of the table for which the trigger is defined.

`CASCADE`  
Automatically drop objects that depend on the trigger, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the trigger if any objects depend on it. This is the default.

## Examples

Destroy the trigger `if_dist_exists` on the table `films`:

    DROP TRIGGER if_dist_exists ON films;

## Compatibility

The `DROP TRIGGER` statement in PostgreSQL is incompatible with the SQL standard. In the SQL standard, trigger names are not local to tables, so the command is simply `DROP TRIGGER name`.

## See Also
