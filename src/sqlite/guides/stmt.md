---
title: The SQLITE_STMT Virtual Table
source_url: https://www.sqlite.org/stmt.html
source_path: stmt.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7320
---

# 1. Overview

The SQLITE_STMT extension implements an [eponymous-only virtual table](vtab.md#epoonlyvtab) that provides information about all [prepared statements](c3ref/stmt.md) associated with the [database connection](c3ref/sqlite3.md).

The SQLITE_STMT extension is included in the [amalgamation](amalgamation.md) though it is disabled by default. Use the [SQLITE_ENABLE_STMTVTAB](compile.md#enable_stmtvtab) compile-time option to enable the SQLITE_STMT extension. The SQLITE_STMT extension can also be loaded at run-time by compiling the extension into a shared library or DLL using the source code at <https://sqlite.org/src/file/ext/misc/stmt.c> and following the instructions for how to [compile loadable extensions](loadext.md#build).

The SQLITE_STMT extension is enabled in default builds of the [command-line shell](cli.md).

# 2. Usage

The SQLITE_STMT virtual table is a read-only table that can be directly queried to access information about all prepared statements on the current database connection. For example:

SELECT \* FROM sqlite_stmt;\

A statement such as the above can be run immediately prior to invoking [sqlite3_close()](c3ref/close.md) to confirm that all prepared statements have been [finalized](c3ref/finalize.md) and to help identify and track down prepared statements that have "leaked" and missed finalization.

The SQLITE_STMT virtual table can also be used to access performance information about prepared statements, to aid in optimizing an application. For example, to find out how much memory is being used by [prepared statements](c3ref/stmt.md) that have never been used, one could run:

SELECT sum(mem) FROM sqlite_stmt WHERE run=0;\

## 2.1. Columns

The columns provided by the SQLITE_STMT virtual table are summarized by the hypothetical CREATE TABLE statement show here:

CREATE TABLE sqlite_stmt(\
  sql    TEXT,    -- Original SQL text\
  ncol   INT,     -- Number of output columns\
  ro     BOOLEAN, -- True for "read only" statements\
  busy   BOOLEAN, -- True if the statement is current running\
  nscan  INT,     -- Number of full-scan steps\
  nsort  INT,     -- Number of sort operations\
  naidx  INT,     -- Number of automatic index inserts\
  nstep  INT,     -- Number of byte-code engine steps\
  reprep INT,     -- Number of reprepare operations\
  run    INT,     -- Number of times this statement has been run\
  mem    INT      -- Heap memory used by this statement\
);\

Future releases may add new output columns and may change the order of legacy columns. Further detail about the meaning of each column in the SQLITE_STMT virtual table is provided below:

- **sql**: The original SQL text of the prepared statement. If the prepared statement is compiled using the [sqlite3_prepare()](c3ref/prepare.md) interface, then the SQL text might not have been saved, in which case this column will be NULL.

- **ncol**: The number of columns in the result set of a query. For DML statements, this column has a value of 0.

- **ro**: The "read only" column. This column is true (non-zero) if the SQL statement is a query and false (zero) if it is a DML statement.

- **busy**: This field is true if the prepared statement is currently running. In other words, this field is true if [sqlite3_step()](c3ref/step.md) has been called on the [prepared statement](c3ref/stmt.md) at least once but [sqlite3_reset()](c3ref/reset.md) has not yet been called to reset it.

- **nscan**: This field is the number of times that the [bytecode engine](opcode.md) has stepped through a table as part of a full-table scan. A large number if this field may indicate an opportunity to improve performance by adding an index. This field is equivalent to the [SQLITE_STMTSTATUS_FULLSCAN_STEP](c3ref/c_stmtstatus_counter.md#sqlitestmtstatusfullscanstep) value.

- **nsort**: This field is the number of times that the [bytecode engine](opcode.md) had to sort. A positive value in this field may indicate an opportunity to improve performance by adding an index that will cause the query results to appear naturally in the desired order. This field is equivalent to the [SQLITE_STMTSTATUS_SORT](c3ref/c_stmtstatus_counter.md#sqlitestmtstatussort) value.

- **naidx**: This field is the number of rows that have been inserted into [automatic indexes](optoverview.md#autoindex). A positive value in this field may indicate an opportunity to improve performance by adding a named index that takes the place of the automatic index. This field is equivalent to the [SQLITE_STMTSTATUS_AUTOINDEX](c3ref/c_stmtstatus_counter.md#sqlitestmtstatusautoindex) value.

- **nstep**: This field is the number of [bytecode engine](opcode.md) operations that have been performed for the prepared statement. This field can be used as a proxy for how much CPU time a statement has used. This field is equivalent to the [SQLITE_STMTSTATUS_VM_STEP](c3ref/c_stmtstatus_counter.md#sqlitestmtstatusvmstep) value.

- **reprep**: This field is the number of times that the statement has had to be reprepared due to schema changes or changes to parameter bindings. This field is equivalent to the [SQLITE_STMTSTATUS_REPREPARE](c3ref/c_stmtstatus_counter.md#sqlitestmtstatusreprepare) value.

- **run**: This field is the number of times that the statement has been run. This field is equivalent to the [SQLITE_STMTSTATUS_RUN](c3ref/c_stmtstatus_counter.md#sqlitestmtstatusrun) value.

- **mem**: This field is the number of bytes of heap storage used by the prepared statement. This field is equivalent to the [SQLITE_STMTSTATUS_MEMUSED](c3ref/c_stmtstatus_counter.md#sqlitestmtstatusmemused) value.
