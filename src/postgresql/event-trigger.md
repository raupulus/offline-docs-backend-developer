---
title: Event Triggers
source_url: https://www.postgresql.org/docs/17/event-triggers.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: event-trigger.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 500
---

## Event Triggers

event trigger

To supplement the trigger mechanism discussed in [???](#triggers), PostgreSQL also provides event triggers. Unlike regular triggers, which are attached to a single table and capture only DML events, event triggers are global to a particular database and are capable of capturing DDL events.

Like regular triggers, event triggers can be written in any procedural language that includes event trigger support, or in C, but not in plain SQL.

## Overview of Event Trigger Behavior

An event trigger fires whenever the event with which it is associated occurs in the database in which it is defined. Currently, the only supported events are `login`, `ddl_command_start`, `ddl_command_end`, `table_rewrite` and `sql_drop`. Support for additional events may be added in future releases.

The `login` event occurs when an authenticated user logs into the system. Any bug in a trigger procedure for this event may prevent successful login to the system. Such bugs may be worked around by setting [???](#guc-event-triggers) to `false` either in a connection string or configuration file. Alternatively, you can restart the system in single-user mode (as event triggers are disabled in this mode). See the [???](#app-postgres) reference page for details about using single-user mode. The `login` event will also fire on standby servers. To prevent servers from becoming inaccessible, such triggers must avoid writing anything to the database when running on a standby. Also, it's recommended to avoid long-running queries in `login` event triggers. Note that, for instance, canceling a connection in psql will not cancel the in-progress `login` trigger.

The `ddl_command_start` event occurs just before the execution of a `CREATE`, `ALTER`, `DROP`, `SECURITY LABEL`, `COMMENT`, `GRANT` or `REVOKE` command. No check whether the affected object exists or doesn't exist is performed before the event trigger fires. As an exception, however, this event does not occur for DDL commands targeting shared objects databases, roles, and tablespaces or for commands targeting event triggers themselves. The event trigger mechanism does not support these object types. `ddl_command_start` also occurs just before the execution of a `SELECT INTO` command, since this is equivalent to `CREATE TABLE AS`.

The `ddl_command_end` event occurs just after the execution of this same set of commands. To obtain more details on the DDL operations that took place, use the set-returning function `pg_event_trigger_ddl_commands()` from the `ddl_command_end` event trigger code (see [???](#functions-event-triggers)). Note that the trigger fires after the actions have taken place (but before the transaction commits), and thus the system catalogs can be read as already changed.

The `sql_drop` event occurs just before the `ddl_command_end` event trigger for any operation that drops database objects. To list the objects that have been dropped, use the set-returning function `pg_event_trigger_dropped_objects()` from the `sql_drop` event trigger code (see [???](#functions-event-triggers)). Note that the trigger is executed after the objects have been deleted from the system catalogs, so it's not possible to look them up anymore.

The `table_rewrite` event occurs just before a table is rewritten by some actions of the commands `ALTER TABLE` and `ALTER TYPE`. While other control statements are available to rewrite a table, like `CLUSTER` and `VACUUM`, the `table_rewrite` event is not triggered by them. To find the OID of the table that was rewritten, use the function `pg_event_trigger_table_rewrite_oid()` (see [???](#functions-event-triggers)). To discover the reason(s) for the rewrite, use the function `pg_event_trigger_table_rewrite_reason()`.

Event triggers (like other functions) cannot be executed in an aborted transaction. Thus, if a DDL command fails with an error, any associated `ddl_command_end` triggers will not be executed. Conversely, if a `ddl_command_start` trigger fails with an error, no further event triggers will fire, and no attempt will be made to execute the command itself. Similarly, if a `ddl_command_end` trigger fails with an error, the effects of the DDL statement will be rolled back, just as they would be in any other case where the containing transaction aborts.

For a complete list of commands supported by the event trigger mechanism, see [Event Trigger Firing Matrix](#event-trigger-matrix).

Event triggers are created using the command [???](#sql-createeventtrigger). In order to create an event trigger, you must first create a function with the special return type `event_trigger`. This function need not (and may not) return a value; the return type serves merely as a signal that the function is to be invoked as an event trigger.

If more than one event trigger is defined for a particular event, they will fire in alphabetical order by trigger name.

A trigger definition can also specify a `WHEN` condition so that, for example, a `ddl_command_start` trigger can be fired only for particular commands which the user wishes to intercept. A common use of such triggers is to restrict the range of DDL operations which users may perform.

## Event Trigger Firing Matrix

[Event Trigger Support by Command Tag](#event-trigger-by-command-tag) lists all commands for which event triggers are supported.

| Command Tag | `ddl_​command_​start` | `ddl_​command_​end` | `sql_​drop` | `table_​rewrite` | Notes |
|----|----|----|----|----|----|
| `ALTER AGGREGATE` | `X` | `X` | `-` | `-` |  |
| `ALTER COLLATION` | `X` | `X` | `-` | `-` |  |
| `ALTER CONVERSION` | `X` | `X` | `-` | `-` |  |
| `ALTER DOMAIN` | `X` | `X` | `-` | `-` |  |
| `ALTER DEFAULT PRIVILEGES` | `X` | `X` | `-` | `-` |  |
| `ALTER EXTENSION` | `X` | `X` | `-` | `-` |  |
| `ALTER FOREIGN DATA WRAPPER` | `X` | `X` | `-` | `-` |  |
| `ALTER FOREIGN TABLE` | `X` | `X` | `X` | `-` |  |
| `ALTER FUNCTION` | `X` | `X` | `-` | `-` |  |
| `ALTER LANGUAGE` | `X` | `X` | `-` | `-` |  |
| `ALTER LARGE OBJECT` | `X` | `X` | `-` | `-` |  |
| `ALTER MATERIALIZED VIEW` | `X` | `X` | `-` | `X` |  |
| `ALTER OPERATOR` | `X` | `X` | `-` | `-` |  |
| `ALTER OPERATOR CLASS` | `X` | `X` | `-` | `-` |  |
| `ALTER OPERATOR FAMILY` | `X` | `X` | `-` | `-` |  |
| `ALTER POLICY` | `X` | `X` | `-` | `-` |  |
| `ALTER PROCEDURE` | `X` | `X` | `-` | `-` |  |
| `ALTER PUBLICATION` | `X` | `X` | `-` | `-` |  |
| `ALTER ROUTINE` | `X` | `X` | `-` | `-` |  |
| `ALTER SCHEMA` | `X` | `X` | `-` | `-` |  |
| `ALTER SEQUENCE` | `X` | `X` | `-` | `-` |  |
| `ALTER SERVER` | `X` | `X` | `-` | `-` |  |
| `ALTER STATISTICS` | `X` | `X` | `-` | `-` |  |
| `ALTER SUBSCRIPTION` | `X` | `X` | `-` | `-` |  |
| `ALTER TABLE` | `X` | `X` | `X` | `X` |  |
| `ALTER TEXT SEARCH CONFIGURATION` | `X` | `X` | `-` | `-` |  |
| `ALTER TEXT SEARCH DICTIONARY` | `X` | `X` | `-` | `-` |  |
| `ALTER TEXT SEARCH PARSER` | `X` | `X` | `-` | `-` |  |
| `ALTER TEXT SEARCH TEMPLATE` | `X` | `X` | `-` | `-` |  |
| `ALTER TRIGGER` | `X` | `X` | `-` | `-` |  |
| `ALTER TYPE` | `X` | `X` | `-` | `X` |  |
| `ALTER USER MAPPING` | `X` | `X` | `-` | `-` |  |
| `ALTER VIEW` | `X` | `X` | `-` | `-` |  |
| `COMMENT` | `X` | `X` | `-` | `-` | Only for local objects |
| `CREATE ACCESS METHOD` | `X` | `X` | `-` | `-` |  |
| `CREATE AGGREGATE` | `X` | `X` | `-` | `-` |  |
| `CREATE CAST` | `X` | `X` | `-` | `-` |  |
| `CREATE COLLATION` | `X` | `X` | `-` | `-` |  |
| `CREATE CONVERSION` | `X` | `X` | `-` | `-` |  |
| `CREATE DOMAIN` | `X` | `X` | `-` | `-` |  |
| `CREATE EXTENSION` | `X` | `X` | `-` | `-` |  |
| `CREATE FOREIGN DATA WRAPPER` | `X` | `X` | `-` | `-` |  |
| `CREATE FOREIGN TABLE` | `X` | `X` | `-` | `-` |  |
| `CREATE FUNCTION` | `X` | `X` | `-` | `-` |  |
| `CREATE INDEX` | `X` | `X` | `-` | `-` |  |
| `CREATE LANGUAGE` | `X` | `X` | `-` | `-` |  |
| `CREATE MATERIALIZED VIEW` | `X` | `X` | `-` | `-` |  |
| `CREATE OPERATOR` | `X` | `X` | `-` | `-` |  |
| `CREATE OPERATOR CLASS` | `X` | `X` | `-` | `-` |  |
| `CREATE OPERATOR FAMILY` | `X` | `X` | `-` | `-` |  |
| `CREATE POLICY` | `X` | `X` | `-` | `-` |  |
| `CREATE PROCEDURE` | `X` | `X` | `-` | `-` |  |
| `CREATE PUBLICATION` | `X` | `X` | `-` | `-` |  |
| `CREATE RULE` | `X` | `X` | `-` | `-` |  |
| `CREATE SCHEMA` | `X` | `X` | `-` | `-` |  |
| `CREATE SEQUENCE` | `X` | `X` | `-` | `-` |  |
| `CREATE SERVER` | `X` | `X` | `-` | `-` |  |
| `CREATE STATISTICS` | `X` | `X` | `-` | `-` |  |
| `CREATE SUBSCRIPTION` | `X` | `X` | `-` | `-` |  |
| `CREATE TABLE` | `X` | `X` | `-` | `-` |  |
| `CREATE TABLE AS` | `X` | `X` | `-` | `-` |  |
| `CREATE TEXT SEARCH CONFIGURATION` | `X` | `X` | `-` | `-` |  |
| `CREATE TEXT SEARCH DICTIONARY` | `X` | `X` | `-` | `-` |  |
| `CREATE TEXT SEARCH PARSER` | `X` | `X` | `-` | `-` |  |
| `CREATE TEXT SEARCH TEMPLATE` | `X` | `X` | `-` | `-` |  |
| `CREATE TRIGGER` | `X` | `X` | `-` | `-` |  |
| `CREATE TYPE` | `X` | `X` | `-` | `-` |  |
| `CREATE USER MAPPING` | `X` | `X` | `-` | `-` |  |
| `CREATE VIEW` | `X` | `X` | `-` | `-` |  |
| `DROP ACCESS METHOD` | `X` | `X` | `X` | `-` |  |
| `DROP AGGREGATE` | `X` | `X` | `X` | `-` |  |
| `DROP CAST` | `X` | `X` | `X` | `-` |  |
| `DROP COLLATION` | `X` | `X` | `X` | `-` |  |
| `DROP CONVERSION` | `X` | `X` | `X` | `-` |  |
| `DROP DOMAIN` | `X` | `X` | `X` | `-` |  |
| `DROP EXTENSION` | `X` | `X` | `X` | `-` |  |
| `DROP FOREIGN DATA WRAPPER` | `X` | `X` | `X` | `-` |  |
| `DROP FOREIGN TABLE` | `X` | `X` | `X` | `-` |  |
| `DROP FUNCTION` | `X` | `X` | `X` | `-` |  |
| `DROP INDEX` | `X` | `X` | `X` | `-` |  |
| `DROP LANGUAGE` | `X` | `X` | `X` | `-` |  |
| `DROP MATERIALIZED VIEW` | `X` | `X` | `X` | `-` |  |
| `DROP OPERATOR` | `X` | `X` | `X` | `-` |  |
| `DROP OPERATOR CLASS` | `X` | `X` | `X` | `-` |  |
| `DROP OPERATOR FAMILY` | `X` | `X` | `X` | `-` |  |
| `DROP OWNED` | `X` | `X` | `X` | `-` |  |
| `DROP POLICY` | `X` | `X` | `X` | `-` |  |
| `DROP PROCEDURE` | `X` | `X` | `X` | `-` |  |
| `DROP PUBLICATION` | `X` | `X` | `X` | `-` |  |
| `DROP ROUTINE` | `X` | `X` | `X` | `-` |  |
| `DROP RULE` | `X` | `X` | `X` | `-` |  |
| `DROP SCHEMA` | `X` | `X` | `X` | `-` |  |
| `DROP SEQUENCE` | `X` | `X` | `X` | `-` |  |
| `DROP SERVER` | `X` | `X` | `X` | `-` |  |
| `DROP STATISTICS` | `X` | `X` | `X` | `-` |  |
| `DROP SUBSCRIPTION` | `X` | `X` | `X` | `-` |  |
| `DROP TABLE` | `X` | `X` | `X` | `-` |  |
| `DROP TEXT SEARCH CONFIGURATION` | `X` | `X` | `X` | `-` |  |
| `DROP TEXT SEARCH DICTIONARY` | `X` | `X` | `X` | `-` |  |
| `DROP TEXT SEARCH PARSER` | `X` | `X` | `X` | `-` |  |
| `DROP TEXT SEARCH TEMPLATE` | `X` | `X` | `X` | `-` |  |
| `DROP TRIGGER` | `X` | `X` | `X` | `-` |  |
| `DROP TYPE` | `X` | `X` | `X` | `-` |  |
| `DROP USER MAPPING` | `X` | `X` | `X` | `-` |  |
| `DROP VIEW` | `X` | `X` | `X` | `-` |  |
| `GRANT` | `X` | `X` | `-` | `-` | Only for local objects |
| `IMPORT FOREIGN SCHEMA` | `X` | `X` | `-` | `-` |  |
| `REFRESH MATERIALIZED VIEW` | `X` | `X` | `-` | `-` |  |
| `REINDEX` | `X` | `X` | `-` | `-` |  |
| `REVOKE` | `X` | `X` | `-` | `-` | Only for local objects |
| `SECURITY LABEL` | `X` | `X` | `-` | `-` | Only for local objects |
| `SELECT INTO` | `X` | `X` | `-` | `-` |  |

Event Trigger Support by Command Tag {#event-trigger-by-command-tag}

## Writing Event Trigger Functions in C

event trigger

in C

This section describes the low-level details of the interface to an event trigger function. This information is only needed when writing event trigger functions in C. If you are using a higher-level language then these details are handled for you. In most cases you should consider using a procedural language before writing your event triggers in C. The documentation of each procedural language explains how to write an event trigger in that language.

Event trigger functions must use the “version 1” function manager interface.

When a function is called by the event trigger manager, it is not passed any normal arguments, but it is passed a “context” pointer pointing to a EventTriggerData structure. C functions can check whether they were called from the event trigger manager or not by executing the macro:

    CALLED_AS_EVENT_TRIGGER(fcinfo)

which expands to:

    ((fcinfo)->context != NULL && IsA((fcinfo)->context, EventTriggerData))

If this returns true, then it is safe to cast `fcinfo->context` to type `EventTriggerData *` and make use of the pointed-to EventTriggerData structure. The function must *not* alter the EventTriggerData structure or any of the data it points to.

struct EventTriggerData is defined in `commands/event_trigger.h`:

    typedef struct EventTriggerData
    {
        NodeTag     type;
        const char *event;      /* event name */
        Node       *parsetree;  /* parse tree */
        CommandTag  tag;        /* command tag */
    } EventTriggerData;

where the members are defined as follows:

type  
Always `T_EventTriggerData`.

event  
Describes the event for which the function is called, one of `"login"`, `"ddl_command_start"`, `"ddl_command_end"`, `"sql_drop"`, `"table_rewrite"`. See [Overview of Event Trigger Behavior](#event-trigger-definition) for the meaning of these events.

parsetree  
A pointer to the parse tree of the command. Check the PostgreSQL source code for details. The parse tree structure is subject to change without notice.

tag  
The command tag associated with the event for which the event trigger is run, for example `"CREATE FUNCTION"`.

An event trigger function must return a `NULL` pointer (*not* an SQL null value, that is, do not set `isNull` true).

## A Complete Event Trigger Example

Here is a very simple example of an event trigger function written in C. (Examples of triggers written in procedural languages can be found in the documentation of the procedural languages.)

The function `noddl` raises an exception each time it is called. The event trigger definition associated the function with the `ddl_command_start` event. The effect is that all DDL commands (with the exceptions mentioned in [Overview of Event Trigger Behavior](#event-trigger-definition)) are prevented from running.

This is the source code of the trigger function:

    #include "postgres.h"

    #include "commands/event_trigger.h"
    #include "fmgr.h"

    PG_MODULE_MAGIC;

    PG_FUNCTION_INFO_V1(noddl);

    Datum
    noddl(PG_FUNCTION_ARGS)
    {
        EventTriggerData *trigdata;

        if (!CALLED_AS_EVENT_TRIGGER(fcinfo))  /* internal error */
            elog(ERROR, "not fired by event trigger manager");

        trigdata = (EventTriggerData *) fcinfo->context;

        ereport(ERROR,
                (errcode(ERRCODE_INSUFFICIENT_PRIVILEGE),
                 errmsg("command \"%s\" denied",
                        GetCommandTagName(trigdata->tag))));

        PG_RETURN_NULL();
    }

After you have compiled the source code (see [???](#dfunc)), declare the function and the triggers:

    CREATE FUNCTION noddl() RETURNS event_trigger
        AS 'noddl' LANGUAGE C;

    CREATE EVENT TRIGGER noddl ON ddl_command_start
        EXECUTE FUNCTION noddl();

Now you can test the operation of the trigger:

    =# \dy
                         List of event triggers
     Name  |       Event       | Owner | Enabled | Function | Tags
    -------+-------------------+-------+---------+----------+------
     noddl | ddl_command_start | dim   | enabled | noddl    |
    (1 row)

    =# CREATE TABLE foo(id serial);
    ERROR:  command "CREATE TABLE" denied

In this situation, in order to be able to run some DDL commands when you need to do so, you have to either drop the event trigger or disable it. It can be convenient to disable the trigger for only the duration of a transaction:

    BEGIN;
    ALTER EVENT TRIGGER noddl DISABLE;
    CREATE TABLE foo (id serial);
    ALTER EVENT TRIGGER noddl ENABLE;
    COMMIT;

(Recall that DDL commands on event triggers themselves are not affected by event triggers.)

## A Table Rewrite Event Trigger Example

Thanks to the `table_rewrite` event, it is possible to implement a table rewriting policy only allowing the rewrite in maintenance windows.

Here's an example implementing such a policy.

    CREATE OR REPLACE FUNCTION no_rewrite()
     RETURNS event_trigger
     LANGUAGE plpgsql AS
    $$
    ---
    --- Implement local Table Rewriting policy:
    ---   public.foo is not allowed rewriting, ever
    ---   other tables are only allowed rewriting between 1am and 6am
    ---   unless they have more than 100 blocks
    ---
    DECLARE
      table_oid oid := pg_event_trigger_table_rewrite_oid();
      current_hour integer := extract('hour' from current_time);
      pages integer;
      max_pages integer := 100;
    BEGIN
      IF pg_event_trigger_table_rewrite_oid() = 'public.foo'::regclass
      THEN
            RAISE EXCEPTION 'you''re not allowed to rewrite the table %',
                            table_oid::regclass;
      END IF;

      SELECT INTO pages relpages FROM pg_class WHERE oid = table_oid;
      IF pages > max_pages
      THEN
            RAISE EXCEPTION 'rewrites only allowed for table with less than % pages',
                            max_pages;
      END IF;

      IF current_hour NOT BETWEEN 1 AND 6
      THEN
            RAISE EXCEPTION 'rewrites only allowed between 1am and 6am';
      END IF;
    END;
    $$;

    CREATE EVENT TRIGGER no_rewrite_allowed
                      ON table_rewrite
       EXECUTE FUNCTION no_rewrite();

## A Database Login Event Trigger Example

The event trigger on the `login` event can be useful for logging user logins, for verifying the connection and assigning roles according to current circumstances, or for session data initialization. It is very important that any event trigger using the `login` event checks whether or not the database is in recovery before performing any writes. Writing to a standby server will make it inaccessible.

The following example demonstrates these options.

    -- create test tables and roles
    CREATE TABLE user_login_log (
      "user" text,
      "session_start" timestamp with time zone
    );
    CREATE ROLE day_worker;
    CREATE ROLE night_worker;

    -- the example trigger function
    CREATE OR REPLACE FUNCTION init_session()
      RETURNS event_trigger SECURITY DEFINER
      LANGUAGE plpgsql AS
    $$
    DECLARE
      hour integer = EXTRACT('hour' FROM current_time at time zone 'utc');
      rec boolean;
    BEGIN
    -- 1. Forbid logging in between 2AM and 4AM.
    IF hour BETWEEN 2 AND 4 THEN
      RAISE EXCEPTION 'Login forbidden';
    END IF;

    -- The checks below cannot be performed on standby servers so
    -- ensure the database is not in recovery before we perform any
    -- operations.
    SELECT pg_is_in_recovery() INTO rec;
    IF rec THEN
      RETURN;
    END IF;

    -- 2. Assign some roles. At daytime, grant the day_worker role, else the
    -- night_worker role.
    IF hour BETWEEN 8 AND 20 THEN
      EXECUTE 'REVOKE night_worker FROM ' || quote_ident(session_user);
      EXECUTE 'GRANT day_worker TO ' || quote_ident(session_user);
    ELSE
      EXECUTE 'REVOKE day_worker FROM ' || quote_ident(session_user);
      EXECUTE 'GRANT night_worker TO ' || quote_ident(session_user);
    END IF;

    -- 3. Initialize user session data
    CREATE TEMP TABLE session_storage (x float, y integer);
    ALTER TABLE session_storage OWNER TO session_user;

    -- 4. Log the connection time
    INSERT INTO public.user_login_log VALUES (session_user, current_timestamp);

    END;
    $$;

    -- trigger definition
    CREATE EVENT TRIGGER init_session
      ON login
      EXECUTE FUNCTION init_session();
    ALTER EVENT TRIGGER init_session ENABLE ALWAYS;
