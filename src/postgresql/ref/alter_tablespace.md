---
title: ALTER TABLESPACE
description: change the definition of a tablespace
source_url: https://www.postgresql.org/docs/17/sql-altertablespace.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_tablespace.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1570
---

ALTER TABLESPACE

ALTER TABLESPACE

7

SQL - Language Statements

ALTER TABLESPACE

change the definition of a tablespace

ALTER TABLESPACE

name

RENAME TO

new_name

ALTER TABLESPACE

name

OWNER TO {

new_owner

\| CURRENT_ROLE \| CURRENT_USER \| SESSION_USER } ALTER TABLESPACE

name

SET (

tablespace_option

=

value

\[, ... \] ) ALTER TABLESPACE

name

RESET (

tablespace_option

\[, ... \] )

## Description

`ALTER TABLESPACE` can be used to change the definition of a tablespace.

You must own the tablespace to change the definition of a tablespace. To alter the owner, you must also be able to `SET ROLE` to the new owning role. (Note that superusers have these privileges automatically.)

## Parameters

\<name\>  
The name of an existing tablespace.

\<new_name\>  
The new name of the tablespace. The new name cannot begin with `pg_`, as such names are reserved for system tablespaces.

\<new_owner\>  
The new owner of the tablespace.

\<tablespace_option\>  
A tablespace parameter to be set or reset. Currently, the only available parameters are `seq_page_cost`, `random_page_cost`, `effective_io_concurrency` and `maintenance_io_concurrency`. Setting these values for a particular tablespace will override the planner's usual estimate of the cost of reading pages from tables in that tablespace, and the executor's prefetching behavior, as established by the configuration parameters of the same name (see [???](#guc-seq-page-cost), [???](#guc-random-page-cost), [???](#guc-effective-io-concurrency), [???](#guc-maintenance-io-concurrency)). This may be useful if one tablespace is located on a disk which is faster or slower than the remainder of the I/O subsystem.

## Examples

Rename tablespace `index_space` to `fast_raid`:

    ALTER TABLESPACE index_space RENAME TO fast_raid;

Change the owner of tablespace `index_space`:

    ALTER TABLESPACE index_space OWNER TO mary;

## Compatibility

There is no `ALTER TABLESPACE` statement in the SQL standard.

## See Also
