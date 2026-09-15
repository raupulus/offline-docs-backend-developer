---
title: RESET
description: restore the value of a run-time parameter to the default value
source_url: https://www.postgresql.org/docs/17/sql-reset.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/reset.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 3200
---

RESET

RESET

7

SQL - Language Statements

RESET

restore the value of a run-time parameter to the default value

RESET

configuration_parameter

RESET ALL

## Description

`RESET` restores run-time parameters to their default values. `RESET` is an alternative spelling for SET \<configuration_parameter\> TO DEFAULT Refer to [???](#sql-set) for details.

The default value is defined as the value that the parameter would have had, if no `SET` had ever been issued for it in the current session. The actual source of this value might be a compiled-in default, the configuration file, command-line options, or per-database or per-user default settings. This is subtly different from defining it as “the value that the parameter had at session start”, because if the value came from the configuration file, it will be reset to whatever is specified by the configuration file now. See [???](#runtime-config) for details.

The transactional behavior of `RESET` is the same as `SET`: its effects will be undone by transaction rollback.

## Parameters

\<configuration_parameter\>  
Name of a settable run-time parameter. Available parameters are documented in [???](#runtime-config) and on the [???](#sql-set) reference page.

`ALL`  
Resets all settable run-time parameters to default values.

## Examples

Set the `timezone` configuration variable to its default value:

    RESET timezone;

## Compatibility

`RESET` is a PostgreSQL extension.

## See Also
