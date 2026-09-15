---
title: List Of Virtual Tables
source_url: https://www.sqlite.org/vtablist.html
source_path: vtablist.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 8270
---

# 1. Introduction

A [virtual table](vtab.md) is an object that presents an SQL table interface but which is not stored in the database file, at least not directly. The virtual table mechanism is a feature of SQLite that allows SQLite to access and manipulate resources other than bits in the database file using the powerful SQL query language.

The table below lists a few of the virtual table implementations available for SQLite. Developers can deploy these virtual tables in their own applications, or use the implementations shown below as templates for writing their own virtual tables.

The list below is not exhaustive. Other virtual table implementations exist in the SQLite source tree and elsewhere. The list below tries to capture the more interesting virtual table implementations.

# 2. Virtual Tables

| Name | Description |
|----|----|
| **[bytecode](bytecodevtab.md)** | A [table-valued function](vtab.md#tabfunc2) that shows the bytecodes of a prepared statement. |
| **[carray](carray.md)** | A [table-valued function](vtab.md#tabfunc2) that allows a C-language array of integers, doubles, strings, or blobs to be used as a table in a query. |
| **[closure](https://sqlite.org/src/file/ext/misc/closure.c)** | Compute the transitive closure of a set. |
| **[completion](completion.md)** | Suggests completions for partially-entered words during interactive SQL input. Used by the [CLI](cli.md) to help implement tab-completion. |
| **[csv](csv.md)** | A virtual table that represents a comma-separated-value or CSV file ([RFC 4180](https://www.ietf.org/rfc/rfc4180.txt)) as a read-only table so that it can be used as part of a larger query. |
| **[dbstat](dbstat.md)** | Provides information about the purpose and use of each page in a database file. Used in the implementation of the [sqlite3_analyzer](sqlanalyze.md) utility program. |
| **[files_of_checkin](https://fossil-scm.org/fossil/file/src/foci.c)** | Provides information about all files in a single check-in in the [Fossil version control system](https://fossil-scm.org/). This virtual table is not part of the SQLite project but is included because it provides an example of how to use virtual tables and because it is used to help version control the SQLite sources. |
| **[fsdir](https://sqlite.org/src/file/ext/misc/fileio.c)** | A [table-valued function](vtab.md#tabfunc2) returning one row for each file in a selected file hierarchy of the host computer. Used by the [CLI](cli.md) to help implement the [.archive command](cli.md#sqlar). |
| **[FTS3](fts3.md)** | A high-performance full-text search index. |
| **[FTS5](fts5.md)** | A higher-performance full-text search index |
| **[generate_series](series.md)** | A [table-valued function](vtab.md#tabfunc2) returning a sequence of integers, modeled after the table-valued function by the same name in PostgreSQL. |
| **[json_each](json1.md#jeach)** | A [table-valued function](vtab.md#tabfunc2) for decomposing a JSON string. |
| **[json_tree](json1.md#jtree)** | A [table-valued function](vtab.md#tabfunc2) for decomposing a JSON string. |
| **[OsQuery](https://osquery.readthedocs.io/en/stable/)** | Hundreds of virtual tables that publish various aspects of the host computer, such as the process table, user lists, active network connections, and so forth. OsQuery is a separate project, started by Facebook, hosted on [GitHub](https://github.com/facebook/osquery), and intended for security analysis and intrusion detection. OsQuery is not a part of the SQLite project, but is included in this list because it demonstrates how the SQL language and the SQLite virtual table mechanism can be leveraged to provide elegant solutions to important real-world problems. |
| **[pragma](pragma.md#pragfunc)** | Built-in [table-valued functions](vtab.md#tabfunc2) that return the results of [PRAGMA](pragma.md#syntax) statements for use within ordinary SQL queries. |
| **[RTree](rtree.md)** | An implementation of the Guttmann R\*Tree spatial index idea. |
| **[spellfix1](spellfix1.md)** | A virtual table that implements a spelling correction engine. |
| **[sqlite_btreeinfo](https://sqlite.org/src/file/ext/misc/btreeinfo.c)** | This experimental [table-valued function](vtab.md#tabfunc2) provides information about a single [B-tree](fileformat2.md#btree) in a database file, such as the depth, and estimated number of pages and number of entries, and so forth. |
| **[sqlite_dbpage](dbpage.md)** | Key/value store for the raw database file content. The key is the page number and the value is binary page content. |
| **[sqlite_memstat](memstat.md)** | Provides SQL access to the [sqlite3_status64()](c3ref/status.md) and [sqlite3_db_status()](c3ref/db_status.md) interfaces. |
| **[sqlite_stmt](stmt.md)** | A [table-valued function](vtab.md#tabfunc2) containing one row for each [prepared statement](c3ref/stmt.md) associated with an open [database connection](c3ref/sqlite3.md). |
| **[swarmvtab](swarmvtab.md#overview)** | An experimental module providing on-demand read-only access to multiple tables spread across multiple databases, via a single virtual table abstraction. |
| **[tables_used](bytecodevtab.md)** | A [table-valued function](vtab.md#tabfunc2) that shows the tables and indexes that are accessed by a prepared statement. |
| **[tclvar](https://sqlite.org/src/file/src/test_tclvar.c)** | Represents the global variables of a [TCL Interpreter](https://en.wikipedia.org/wiki/Tcl) as an SQL table. Used as part of the SQLite test suite. |
| **[templatevtab](https://sqlite.org/src/file/ext/misc/templatevtab.c)** | A template virtual table implementation useful as a starting point for developers who want to write their own virtual tables |
| **[unionvtab](unionvtab.md)** | An experimental module providing on-demand read-only access to multiple tables spread across multiple databases, via a single virtual table abstraction. |
| **[vfsstat](https://sqlite.org/src/file/ext/misc/vfsstat.c)** | A [table-valued function](vtab.md#tabfunc2) which, in combination with a co-packaged [VFS shim](vfs.md#shim) provides information on the number of system calls performed by SQLite. |
| **[vtablog](https://sqlite.org/src/file/ext/misc/vtablog.c)** | A virtual table that prints diagnostic information on stdout when its key methods are invoked. Intended for interactive analysis and debugging of virtual table interfaces. |
| **[wholenumber](https://sqlite.org/src/file/ext/misc/wholenumber.c)** | A virtual table returns all integers between 1 and 4294967295. |
| **[zipfile](zipfile.md)** | Represent a [ZIP Archive](https://en.wikipedia.org/wiki/Zip_(file_format)) as an SQL table. Works for both reading and writing. Used by the [CLI](cli.md) to implement the ability to read and write ZIP Archives. |
