---
title: MOVE
description: position a cursor
source_url: https://www.postgresql.org/docs/17/sql-move.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/move.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2850
---

MOVE

cursor

MOVE

MOVE

7

SQL - Language Statements

MOVE

position a cursor

MOVE \[

direction

\] \[ FROM \| IN \]

cursor_name

where

direction

can be one of:

NEXT PRIOR FIRST LAST ABSOLUTE

count

RELATIVE

count

count

ALL FORWARD FORWARD

count

FORWARD ALL BACKWARD BACKWARD

count

BACKWARD ALL

## Description

`MOVE` repositions a cursor without retrieving any data. `MOVE` works exactly like the `FETCH` command, except it only positions the cursor and does not return rows.

The parameters for the `MOVE` command are identical to those of the `FETCH` command; refer to [???](#sql-fetch) for details on syntax and usage.

## Outputs

On successful completion, a `MOVE` command returns a command tag of the form

    MOVE count

The \<count\> is the number of rows that a `FETCH` command with the same parameters would have returned (possibly zero).

## Examples

    BEGIN WORK;
    DECLARE liahona CURSOR FOR SELECT * FROM films;

    -- Skip the first 5 rows:
    MOVE FORWARD 5 IN liahona;
    MOVE 5

    -- Fetch the 6th row from the cursor liahona:
    FETCH 1 FROM liahona;
     code  | title  | did | date_prod  |  kind  |  len
    -------+--------+-----+------------+--------+-------
     P_303 | 48 Hrs | 103 | 1982-10-22 | Action | 01:37
    (1 row)

    -- Close the cursor liahona and end the transaction:
    CLOSE liahona;
    COMMIT WORK;

## Compatibility

There is no `MOVE` statement in the SQL standard.

## See Also
