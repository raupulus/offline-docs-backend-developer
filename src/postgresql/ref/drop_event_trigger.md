---
title: DROP EVENT TRIGGER
description: remove an event trigger
source_url: https://www.postgresql.org/docs/17/sql-dropeventtrigger.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_event_trigger.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2340
---

DROP EVENT TRIGGER

DROP EVENT TRIGGER

7

SQL - Language Statements

DROP EVENT TRIGGER

remove an event trigger

DROP EVENT TRIGGER \[ IF EXISTS \]

name

\[ CASCADE \| RESTRICT \]

## Description

`DROP EVENT TRIGGER` removes an existing event trigger. To execute this command, the current user must be the owner of the event trigger.

## Parameters

`IF EXISTS`  
Do not throw an error if the event trigger does not exist. A notice is issued in this case.

\<name\>  
The name of the event trigger to remove.

`CASCADE`  
Automatically drop objects that depend on the trigger, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the trigger if any objects depend on it. This is the default.

## Examples

Destroy the trigger `snitch`:

    DROP EVENT TRIGGER snitch;

## Compatibility

There is no `DROP EVENT TRIGGER` statement in the SQL standard.

## See Also
