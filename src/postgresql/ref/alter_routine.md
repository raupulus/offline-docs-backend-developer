---
title: ALTER ROUTINE
description: change the definition of a routine
source_url: https://www.postgresql.org/docs/17/sql-alterroutine.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_routine.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1480
---

ALTER ROUTINE

ALTER ROUTINE

7

SQL - Language Statements

ALTER ROUTINE

change the definition of a routine

ALTER ROUTINE

name

\[ ( \[ \[

argmode

\] \[

argname

\]

argtype

\[, ...\] \] ) \]

action

\[ ... \] \[ RESTRICT \] ALTER ROUTINE

name

\[ ( \[ \[

argmode

\] \[

argname

\]

argtype

\[, ...\] \] ) \] RENAME TO

new_name

ALTER ROUTINE

name

\[ ( \[ \[

argmode

\] \[

argname

\]

argtype

\[, ...\] \] ) \] OWNER TO {

new_owner

\| CURRENT_ROLE \| CURRENT_USER \| SESSION_USER } ALTER ROUTINE

name

\[ ( \[ \[

argmode

\] \[

argname

\]

argtype

\[, ...\] \] ) \] SET SCHEMA

new_schema

ALTER ROUTINE

name

\[ ( \[ \[

argmode

\] \[

argname

\]

argtype

\[, ...\] \] ) \] \[ NO \] DEPENDS ON EXTENSION

extension_name

where

action

is one of:

IMMUTABLE \| STABLE \| VOLATILE \[ NOT \] LEAKPROOF \[ EXTERNAL \] SECURITY INVOKER \| \[ EXTERNAL \] SECURITY DEFINER PARALLEL { UNSAFE \| RESTRICTED \| SAFE } COST

execution_cost

ROWS

result_rows

SET

configuration_parameter

{ TO \| = } {

value

\| DEFAULT } SET

configuration_parameter

FROM CURRENT RESET

configuration_parameter

RESET ALL

## Description

`ALTER ROUTINE` changes the definition of a routine, which can be an aggregate function, a normal function, or a procedure. See under [???](#sql-alteraggregate), [???](#sql-alterfunction), and [???](#sql-alterprocedure) for the description of the parameters, more examples, and further details.

## Examples

To rename the routine `foo` for type `integer` to `foobar`:

    ALTER ROUTINE foo(integer) RENAME TO foobar;

This command will work independent of whether `foo` is an aggregate, function, or procedure.

## Compatibility

This statement is partially compatible with the `ALTER ROUTINE` statement in the SQL standard. See under [???](#sql-alterfunction) and [???](#sql-alterprocedure) for more details. Allowing routine names to refer to aggregate functions is a PostgreSQL extension.

## See Also

Note that there is no `CREATE ROUTINE` command.
