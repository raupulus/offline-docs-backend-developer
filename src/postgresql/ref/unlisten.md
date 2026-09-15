---
title: UNLISTEN
description: stop listening for a notification
source_url: https://www.postgresql.org/docs/17/sql-unlisten.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/unlisten.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 3370
---

UNLISTEN

UNLISTEN

7

SQL - Language Statements

UNLISTEN

stop listening for a notification

UNLISTEN {

channel

\| \* }

## Description

`UNLISTEN` is used to remove an existing registration for `NOTIFY` events. `UNLISTEN` cancels any existing registration of the current PostgreSQL session as a listener on the notification channel named \<channel\>. The special wildcard `*` cancels all listener registrations for the current session.

[???](#sql-notify) contains a more extensive discussion of the use of `LISTEN` and `NOTIFY`.

## Parameters

\<channel\>  
Name of a notification channel (any identifier).

`*`  
All current listen registrations for this session are cleared.

## Notes

You can unlisten something you were not listening for; no warning or error will appear.

At the end of each session, `UNLISTEN *` is automatically executed.

A transaction that has executed `UNLISTEN` cannot be prepared for two-phase commit.

## Examples

To make a registration:

    LISTEN virtual;
    NOTIFY virtual;
    Asynchronous notification "virtual" received from server process with PID 8448.

Once `UNLISTEN` has been executed, further `NOTIFY` messages will be ignored:

    UNLISTEN virtual;
    NOTIFY virtual;
    -- no NOTIFY event is received

## Compatibility

There is no `UNLISTEN` command in the SQL standard.

## See Also
