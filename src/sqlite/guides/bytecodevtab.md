---
title: The Bytecode() And Tables_Used() Table-Valued Functions
source_url: https://www.sqlite.org/bytecodevtab.html
source_path: bytecodevtab.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 190
---

# 1. Overview

Bytecode and tables_used are [virtual tables](vtab.md) built into SQLite that access information about [prepared statements](c3ref/stmt.md). Both bytecode and tables_used operate as [table-valued functions](vtab.md#tabfunc2). They take a single required argument which is either the text of an SQL statement, or a pointer to an existing prepared statement. The bytecode function returns one row of result for each [bytecode](opcode.md) operation in the prepared statement. The tables_used function returns one row for each persistent btree (either a table or an index) accessed by the prepared statement.

# 2. Usage

The bytecode and tables_used tables are only available if SQLite has been compiled with the [-DSQLITE_ENABLE_BYTECODE_VTAB](compile.md#enable_bytecode_vtab) compile-time option. The [CLI](cli.md) has been compiled that way, and so you can use the standard [CLI](cli.md) as a test platform to experiment.

Both virtual tables are read-only [eponymous-only virtual tables](vtab.md#epoonlyvtab). You use them by mentioning them directly in the FROM clause of a SELECT statement. They both require a single argument which is the SQL statement to be analyzed. For example:

SELECT \* FROM bytecode('SELECT \* FROM bytecode(?1)');\

The argument can be either the text of an SQL statement, in which case the bytecode (or tables_used) for that statement is returned, or the argument can be a parameter such as ?1 or \$stmt that is later bound to a [prepared statement](c3ref/stmt.md) object using the [sqlite3_bind_pointer()](c3ref/bind_blob.md) interface. Use a pointer type of "stmt-pointer" for the [sqlite3_bind_pointer()](c3ref/bind_blob.md) interface.

## 2.1. Schema For bytecode

The schema of the bytecode virtual table is:

CREATE TABLE bytecode(\
  addr INT,\
  opcode TEXT,\
  p1 INT,\
  p2 INT,\
  p3 INT,\
  p4 TEXT,\
  p5 INT,\
  comment TEXT,\
  subprog TEXT,\
  nexec INT,\
  ncycle INT,\
  stmt HIDDEN\
);\

The first eight columns are the address, opcode, and operands for a single [bytecode](opcode.md) in the virtual machine that implements the statement. These columns are the same columns output when using EXPLAIN.

The bytecode virtual tables shows all operations in the prepared statement, both the main body of the prepared statement and in subprograms used to implement triggers or foreign key actions. The "subprog" field is NULL for the main body of the prepared statement, or is the trigger name or the string "(FK)" for triggers and foreign key actions, respectively. <span id="nexec"></span>

The "nexec" and "ncycle" columns show the number of times each opcode has been executed, and the total number of CPU cycles used by that opcode, respectively. These fields always have a value of 0 unless SQLite has been compiled with [SQLITE_ENABLE_STMT_SCANSTATUS](compile.md#enable_stmt_scanstatus) compile-time options and scan-status statistics are enabled using the [sqlite3_db_config](c3ref/db_config.md)(db,[SQLITE_DBCONFIG_STMT_SCANSTATUS](c3ref/c_dbconfig_defensive.md#sqlitedbconfigstmtscanstatus),...) interface. The values for nexec and ncycle are cumulative, until reset using [sqlite3_stmt_scanstatus_reset()](c3ref/stmt_scanstatus_reset.md).

The "ncycle" column currently always returns 0 unless SQLite is compiled for X86_64 or AARCH64 processors using GCC, Clang, or MSVC, or compiled for PPC processors using GCC or Clang.

## 2.2. Schema For tables_used

The schema for the tables_used table is:

CREATE TABLE tables_used(\
  type TEXT,\
  schema TEXT,\
  name TEXT,\
  wr INT,\
  subprog TEXT,\
  stmt HIDDEN\
);\

The tables_used table is intended to show which btrees of the database file are read or written by a prepared statement, both by the main statement itself but also by related triggers and foreign key actions. The columns are as follows:

- **type** → Either "table" or "index", depending on what role the btree is serving.

- **schema** → Which database file the btree is located in. This will be "main" for the main database (the usual case), or "temp" for TEMP tables and indexes, or the name assigned to [attached](lang_attach.md) databases by the [ATTACH](lang_attach.md) statement.

- **name** → The name of the table or index

- **wr** → 0 if the object is read, 1 if the object is written

- **subprog** → The sub-program in which the object is accessed. NULL means the main body of the prepared statement. Otherwise this field is the name of a trigger or "(FK)" for a foreign key action.
