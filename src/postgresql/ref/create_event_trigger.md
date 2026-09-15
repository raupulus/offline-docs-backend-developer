---
title: CREATE EVENT TRIGGER
description: define a new event trigger
source_url: https://www.postgresql.org/docs/17/sql-createeventtrigger.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/create_event_trigger.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1850
---

CREATE EVENT TRIGGER

CREATE EVENT TRIGGER

7

SQL - Language Statements

CREATE EVENT TRIGGER

define a new event trigger

CREATE EVENT TRIGGER

name

ON

event

\[ WHEN

filter_variable

IN (

filter_value

\[, ... \]) \[ AND ... \] \] EXECUTE { FUNCTION \| PROCEDURE }

function_name

()

## Description

`CREATE EVENT TRIGGER` creates a new event trigger. Whenever the designated event occurs and the `WHEN` condition associated with the trigger, if any, is satisfied, the trigger function will be executed. For a general introduction to event triggers, see [???](#event-triggers). The user who creates an event trigger becomes its owner.

## Parameters

\<name\>  
The name to give the new trigger. This name must be unique within the database.

\<event\>  
The name of the event that triggers a call to the given function. See [???](#event-trigger-definition) for more information on event names.

\<filter_variable\>  
The name of a variable used to filter events. This makes it possible to restrict the firing of the trigger to a subset of the cases in which it is supported. Currently the only supported \<filter_variable\> is `TAG`.

\<filter_value\>  
A list of values for the associated \<filter_variable\> for which the trigger should fire. For `TAG`, this means a list of command tags (e.g., `'DROP FUNCTION'`).

\<function_name\>  
A user-supplied function that is declared as taking no argument and returning type `event_trigger`.

In the syntax of `CREATE EVENT TRIGGER`, the keywords `FUNCTION` and `PROCEDURE` are equivalent, but the referenced function must in any case be a function, not a procedure. The use of the keyword `PROCEDURE` here is historical and deprecated.

## Notes

Only superusers can create event triggers.

Event triggers are disabled in single-user mode (see [???](#app-postgres)) as well as when [???](#guc-event-triggers) is set to `false`. If an erroneous event trigger disables the database so much that you can't even drop the trigger, restart with [???](#guc-event-triggers) set to `false` to temporarily disable event triggers, or in single-user mode, and you'll be able to do that.

## Examples

Forbid the execution of any [DDL](#ddl) command:

    CREATE OR REPLACE FUNCTION abort_any_command()
      RETURNS event_trigger
     LANGUAGE plpgsql
      AS $$
    BEGIN
      RAISE EXCEPTION 'command % is disabled', tg_tag;
    END;
    $$;

    CREATE EVENT TRIGGER abort_ddl ON ddl_command_start
       EXECUTE FUNCTION abort_any_command();

## Compatibility

There is no `CREATE EVENT TRIGGER` statement in the SQL standard.

## See Also
