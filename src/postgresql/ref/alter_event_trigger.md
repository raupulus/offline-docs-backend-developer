---
title: ALTER EVENT TRIGGER
description: change the definition of an event trigger
source_url: https://www.postgresql.org/docs/17/sql-altereventtrigger.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_event_trigger.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1310
---

ALTER EVENT TRIGGER

ALTER EVENT TRIGGER

7

SQL - Language Statements

ALTER EVENT TRIGGER

change the definition of an event trigger

ALTER EVENT TRIGGER

name

DISABLE ALTER EVENT TRIGGER

name

ENABLE \[ REPLICA \| ALWAYS \] ALTER EVENT TRIGGER

name

OWNER TO {

new_owner

\| CURRENT_ROLE \| CURRENT_USER \| SESSION_USER } ALTER EVENT TRIGGER

name

RENAME TO

new_name

## Description

`ALTER EVENT TRIGGER` changes properties of an existing event trigger.

You must be superuser to alter an event trigger.

## Parameters

\<name\>  
The name of an existing trigger to alter.

\<new_owner\>  
The user name of the new owner of the event trigger.

\<new_name\>  
The new name of the event trigger.

`DISABLE`/`ENABLE [ REPLICA | ALWAYS ]`  
These forms configure the firing of event triggers. A disabled trigger is still known to the system, but is not executed when its triggering event occurs. See also [???](#guc-session-replication-role).

## Compatibility

There is no `ALTER EVENT TRIGGER` statement in the SQL standard.

## See Also
