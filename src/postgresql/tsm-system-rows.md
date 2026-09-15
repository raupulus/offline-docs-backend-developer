---
title: tsm_system_rows — the SYSTEM_ROWS sampling method for TABLESAMPLE
source_url: https://www.postgresql.org/docs/17/tsm-system-rows.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: tsm-system-rows.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3680
---

## tsm_system_rows the `SYSTEM_ROWS` sampling method for `TABLESAMPLE`

tsm_system_rows

The `tsm_system_rows` module provides the table sampling method `SYSTEM_ROWS`, which can be used in the `TABLESAMPLE` clause of a [`SELECT`](#sql-select) command.

This table sampling method accepts a single integer argument that is the maximum number of rows to read. The resulting sample will always contain exactly that many rows, unless the table does not contain enough rows, in which case the whole table is selected.

Like the built-in `SYSTEM` sampling method, `SYSTEM_ROWS` performs block-level sampling, so that the sample is not completely random but may be subject to clustering effects, especially if only a small number of rows are requested.

`SYSTEM_ROWS` does not support the `REPEATABLE` clause.

This module is considered “trusted”, that is, it can be installed by non-superusers who have `CREATE` privilege on the current database.

## Examples

Here is an example of selecting a sample of a table with `SYSTEM_ROWS`. First install the extension:

    CREATE EXTENSION tsm_system_rows;

Then you can use it in a `SELECT` command, for instance:

    SELECT * FROM my_table TABLESAMPLE SYSTEM_ROWS(100);

This command will return a sample of 100 rows from the table my_table (unless the table does not have 100 visible rows, in which case all its rows are returned).
