---
title: SQLite Documentation
source_url: https://www.sqlite.org/docs.html
source_path: docs.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2760
---

### Common Links

- [Features](features.md)
- [When to use SQLite](whentouse.md)
- [Getting Started](quickstart.md)
- Try it live!
- [SQL Syntax](lang.md)
  - [Pragmas](pragma.md#toc)
  - [SQL functions](lang_corefunc.md)
  - [Date & time functions](lang_datefunc.md)
  - [Aggregate functions](lang_aggfunc.md#aggfunclist)
  - [Window functions](windowfunctions.md#biwinfunc)
  - [Math functions](lang_mathfunc.md)
  - [JSON functions](json1.md)
- [C/C++ Interface Spec](c3ref/intro.md)
  - [Introduction](cintro.md)
  - [List of C-language APIs](c3ref/funclist.md)
- [The TCL Interface Spec](tclsqlite.md)
- [Quirks and Gotchas](quirks.md)
- [Frequently Asked Questions](faq.md)
- [Commit History](https://www.sqlite.org/src/timeline)
- [Prior Releases](chronology.md)
- [Bugs](https://www.sqlite.org/src/wiki?name=Bug+Reports)
- [News](news.md)

Documentation

Search Documentation Search Changelog

- <span onclick="showhide(1)"><span id="sh_mark_1" class="sh_mark">▼</span> Document Lists And Indexes</span>
  - <a href="doclist.html" class="sh_link">Alphabetical Listing Of All Documents</a>
  - <a href="keyword_index.html" class="sh_link">Website Keyword Index</a>
  - <a href="sitemap.html" class="sh_link">Permuted Title Index</a>
- <span onclick="showhide(2)"><span id="sh_mark_2" class="sh_mark">►</span> Overview Documents</span>
  - <a href="about.html" class="sh_link">About SQLite</a> <span class="desktoponly">→ A high-level overview of what SQLite is and why you might be interested in using it. </span>
  - <a href="whentouse.html" class="sh_link">Appropriate Uses For SQLite</a> <span class="desktoponly">→ This document describes situations where SQLite is an appropriate database engine to use versus situations where a client/server database engine might be a better choice. </span>
  - <a href="different.html" class="sh_link">Distinctive Features</a> <span class="desktoponly">→ This document enumerates and describes some of the features of SQLite that make it different from other SQL database engines. </span>
  - <a href="quirks.html" class="sh_link">Quirks of SQLite</a> <span class="desktoponly">→ This document is a short list of some unusual features of SQLite that tend to cause misunderstandings and confusion. The list includes both deliberate innovations and "misfeatures" that are retained only for backwards compatibility. </span>
  - <a href="testing.html" class="sh_link">How SQLite Is Tested</a> <span class="desktoponly">→ The reliability and robustness of SQLite is achieved in large part by thorough and careful testing. This document identifies the many tests that occur before every release of SQLite. </span>
  - <a href="copyright.html" class="sh_link">Copyright</a> <span class="desktoponly">→ SQLite is in the public domain. This document describes what that means and the implications for contributors. </span>
  - <a href="faq.html" class="sh_link">Frequently Asked Questions</a> <span class="desktoponly">→ The title of the document says all... </span>
  - <a href="books.html" class="sh_link">Books About SQLite</a> <span class="desktoponly">→ A list of independently written books about SQLite. </span>
- <span onclick="showhide(3)"><span id="sh_mark_3" class="sh_mark">►</span> Programming Interfaces</span>
  - <a href="quickstart.html" class="sh_link">SQLite In 5 Minutes Or Less</a> <span class="desktoponly">→ A very quick introduction to programming with SQLite. </span>
  - <a href="cintro.html" class="sh_link">Introduction to the C/C++ API</a> <span class="desktoponly">→ This document introduces the C/C++ API. Users should read this document before the C/C++ API Reference Guide linked below. </span>
  - <a href="howtocompile.html" class="sh_link">How To Compile SQLite</a> <span class="desktoponly">→ Instructions and hints for compiling SQLite C code and integrating that code with your own application. </span>
  - <a href="c3ref/intro.html" class="sh_link">C/C++ API Reference</a> <span class="desktoponly">→ This document describes each API function separately. </span>
  - <a href="rescode.html" class="sh_link">Result and Error Codes</a> <span class="desktoponly">→ A description of the meanings of the numeric result codes returned by various C/C++ interfaces. </span>
  - <a href="appfunc.html" class="sh_link">Application-Defined SQL Function</a> <span class="desktoponly">→ An overview of the C-language interfaces used to create new application-defined SQL functions in SQLite. </span>
  - <a href="tclsqlite.html" class="sh_link">Tcl API</a> <span class="desktoponly">→ A description of the TCL interface bindings for SQLite. </span>
  - <a href="http://sqlite.org/android/" class="sh_link">SQLite Android Bindings</a> <span class="desktoponly">→ Information on how to deploy your own private copy of SQLite on Android, bypassing the built-in SQLite, but using the same Java interface. </span>
  - <a href="http://system.data.sqlite.org/" class="sh_link">System.Data.SQLite</a> <span class="desktoponly">→ C#/.NET bindings for SQLite </span>
- <span onclick="showhide(4)"><span id="sh_mark_4" class="sh_mark">►</span> SQL Language Documentation</span>
  - <a href="lang.html" class="sh_link">SQL Syntax</a> <span class="desktoponly">→ This document describes the SQL language that is understood by SQLite. </span>
  - <a href="pragma.html" class="sh_link">Pragma commands</a> <span class="desktoponly">→ This document describes SQLite performance tuning options and other special purpose database commands. </span>
  - <a href="lang_corefunc.html" class="sh_link">Core SQL Functions</a> <span class="desktoponly">→ General-purpose built-in scalar SQL functions. </span>
  - <a href="lang_aggfunc.html" class="sh_link">Aggregate SQL Functions</a> <span class="desktoponly">→ General-purpose built-in aggregate SQL functions. </span>
  - <a href="lang_datefunc.html" class="sh_link">Date and Time SQL Functions</a> <span class="desktoponly">→ SQL functions for manipulating dates and times. </span>
  - <a href="windowfunctions.html" class="sh_link">Window Functions</a> <span class="desktoponly">→ SQL Window functions. </span>
  - <a href="gencol.html" class="sh_link">Generated Columns</a> <span class="desktoponly">→ Stored and virtual columns in table definitions. </span>
  - <a href="datatype3.html" class="sh_link">DataTypes</a> <span class="desktoponly">→ SQLite version 3 introduces the concept of manifest typing, where the type of a value is associated with the value itself, not the column that it is stored in. This page describes data typing for SQLite version 3 in further detail. </span>
  - <a href="expridx.html" class="sh_link">Indexes On Expressions</a> <span class="desktoponly">→ Indexes in SQLite do not have to be over just plain table columns. Expressions can also be indexed. </span>
  - <a href="rowvalue.html" class="sh_link">Row Values</a> <span class="desktoponly">→ SQLite supports comparisons, including inequality comparisons, between tuples of values, call "row values". This document explains. </span>
  - <a href="stricttables.html" class="sh_link">STRICT Tables</a> <span class="desktoponly">→ A STRICT table in SQLite does rigid type enforcement, in order to more closely mimic the behavior of other SQL database engines. </span>
- <span onclick="showhide(5)"><span id="sh_mark_5" class="sh_mark">►</span> Extensions</span>
  - <a href="json1.html" class="sh_link">JSON Functions</a> <span class="desktoponly">→ SQL functions for creating, parsing, and querying JSON content. </span>
  - <a href="fts5.html" class="sh_link">FTS5 - Full Text Search</a> <span class="desktoponly">→ A description of the SQLite Full Text Search (FTS5) extension. </span>
  - <a href="fts3.html" class="sh_link">FTS3 - Full Text Search</a> <span class="desktoponly">→ A description of the SQLite Full Text Search (FTS3) extension. </span>
  - <a href="rtree.html" class="sh_link">R-Tree Module</a> <span class="desktoponly">→ A description of the SQLite R-Tree extension. An R-Tree is a specialized data structure that supports fast multi-dimensional range queries often used in geospatial systems. </span>
  - <a href="sessionintro.html" class="sh_link">Sessions</a> <span class="desktoponly">→ The Sessions extension allows change to an SQLite database to be captured in a compact file which can be reverted on the original database (to implement "undo") or transferred and applied to another similar database. </span>
  - <a href="loadext.html" class="sh_link">Run-Time Loadable Extensions</a> <span class="desktoponly">→ A general overview on how run-time loadable extensions work, how they are compiled, and how developers can create their own run-time loadable extensions for SQLite. </span>
  - <a href="dbstat.html" class="sh_link">Dbstat Virtual Table</a> <span class="desktoponly">→ The DBSTAT virtual table reports on the sizes and geometries of tables storing content in an SQLite database, and is the basis for the [sqlite3_analyzer](sqlanalyze.md) utility program. </span>
  - <a href="csv.html" class="sh_link">Csv Virtual Table</a> <span class="desktoponly">→ The CSV virtual table allows SQLite to directly read and query [RFC 4180](https://www.ietf.org/rfc/rfc4180.txt) formatted files. </span>
  - <a href="carray.html" class="sh_link">Carray</a> <span class="desktoponly">→ CARRAY is a [table-valued function](vtab.md#tabfunc2) that allows C-language arrays to be used in SQL queries. </span>
  - <a href="series.html" class="sh_link">generate_series</a> <span class="desktoponly">→ A description of the generate_series() [table-valued function](vtab.md#tabfunc2). </span>
  - <a href="spellfix1.html" class="sh_link">Spellfix1</a> <span class="desktoponly">→ The spellfix1 extension is an experiment in doing spelling correction for [full-text search](fts3.md). </span>
  - <a href="zipfile.html" class="sh_link">Zipfile</a> <span class="desktoponly">→ A \[virtual table\] with accompanying support functions that can read and write a ZIP archive as if it were a database. </span>
  - <a href="floatingpoint.html#the_ieee754_c_extension" class="sh_link">The IEEE754 Extension</a> <span class="desktoponly">→ A set of SQL functions for encoding and decoding IEEE-754 floating point numbers. </span>
  - <a href="floatingpoint.html#the_decimal_c_extension" class="sh_link">The Decimal Extension</a> <span class="desktoponly">→ A set of functions for doing arbitrary-precision decimal arithmetic, including expanding IEEE-754 floating point values to their exact decimal representation. </span>
  - <a href="uintcseq.html" class="sh_link">The UINT Collating Sequence</a> <span class="desktoponly">→ A collating sequence that sorts text with embedded numbers in numeric order. </span>
  - <a href="percentile.html" class="sh_link">The Percentile Extension</a> <span class="desktoponly">→ An implementation of aggregate functions: [median()](percentile.md#*medianfunc), [percentile()](percentile.md#*percentilefunc), [percentile_cont()](percentile.md#*percentilecontfunc), and [percentile_disc()](percentile.md#*percentilediscfunc). </span>
- <span onclick="showhide(6)"><span id="sh_mark_6" class="sh_mark">►</span> Features</span>
  - <a href="shortnames.html" class="sh_link">8+3 Filenames</a> <span class="desktoponly">→ How to make SQLite work on filesystems that only support 8+3 filenames. </span>
  - <a href="autoinc.html" class="sh_link">Autoincrement</a> <span class="desktoponly">→ A description of the AUTOINCREMENT keyword in SQLite, what it does, why it is sometimes useful, and why it should be avoided if not strictly necessary. </span>
  - <a href="backup.html" class="sh_link">Backup API</a> <span class="desktoponly">→ The [online-backup interface](c3ref/backup_finish.md) can be used to copy content from a disk file into an in-memory database or vice versa and it can make a hot backup of a live database. This application note gives examples of how. </span>
  - <a href="errlog.html" class="sh_link">Error and Warning Log</a> <span class="desktoponly">→ SQLite supports an "error and warning log" design to capture information about suspicious and/or error events during operation. Embedded applications are encouraged to enable the error and warning log to help with debugging application problems that arise in the field. This document explains how to do that. </span>
  - <a href="foreignkeys.html" class="sh_link">Foreign Key Support</a> <span class="desktoponly">→ This document describes the support for foreign key constraints introduced in version 3.6.19. </span>
  - <a href="expridx.html" class="sh_link">Indexes On Expressions</a> <span class="desktoponly">→ Notes on how to create indexes on expressions instead of just individual columns. </span>
  - <a href="intern-v-extern-blob.html" class="sh_link">Internal versus External Blob Storage</a> <span class="desktoponly">→ Should you store large BLOBs directly in the database, or store them in files and just record the filename in the database? This document seeks to shed light on that question. </span>
  - <a href="limits.html" class="sh_link">Limits In SQLite</a> <span class="desktoponly">→ This document describes limitations of SQLite (the maximum length of a string or blob, the maximum size of a database, the maximum number of tables in a database, etc.) and how these limits can be altered at compile-time and run-time. </span>
  - <a href="mmap.html" class="sh_link">Memory-Mapped I/O</a> <span class="desktoponly">→ SQLite supports memory-mapped I/O. Learn how to enable memory-mapped I/O and about the various advantages and disadvantages to using memory-mapped I/O in this document. </span>
  - <a href="threadsafe.html" class="sh_link">Multi-threaded Programs and SQLite</a> <span class="desktoponly">→ SQLite is safe to use in multi-threaded programs. This document provides the details and hints on how to maximize performance. </span>
  - <a href="nulls.html" class="sh_link">Null Handling</a> <span class="desktoponly">→ Different SQL database engines handle NULLs in different ways. The SQL standards are ambiguous. This (circa 2003) document describes how SQLite handles NULLs in comparison with other SQL database engines. </span>
  - <a href="partialindex.html" class="sh_link">Partial Indexes</a> <span class="desktoponly">→ A partial index is an index that only covers a subset of the rows in a table. Learn how to use partial indexes in SQLite from this document. </span>
  - <a href="sharedcache.html" class="sh_link">Shared Cache Mode</a> <span class="desktoponly">→ Version 3.3.0 and later supports the ability for two or more database connections to share the same page and schema cache. This feature is useful for certain specialized applications. </span>
  - <a href="unlock_notify.html" class="sh_link">Unlock Notify</a> <span class="desktoponly">→ The "unlock notify" feature can be used in conjunction with [shared cache mode](sharedcache.md) to more efficiently manage resource conflict (database table locks). </span>
  - <a href="uri.html" class="sh_link">URI Filenames</a> <span class="desktoponly">→ The names of database files can be specified using either an ordinary filename or a URI. Using URI filenames provides additional capabilities, as this document describes. </span>
  - <a href="withoutrowid.html" class="sh_link">WITHOUT ROWID Tables</a> <span class="desktoponly">→ The WITHOUT ROWID optimization is a option that can sometimes result in smaller and faster databases. </span>
  - <a href="wal.html" class="sh_link">Write-Ahead Log (WAL) Mode</a> <span class="desktoponly">→ Transaction control using a write-ahead log offers more concurrency and is often faster than the default rollback transactions. This document explains how to use WAL mode for improved performance. </span>
- <span onclick="showhide(7)"><span id="sh_mark_7" class="sh_mark">►</span> Tools</span>
  - <a href="cli.html" class="sh_link">Command-Line Shell (sqlite3.exe)</a> <span class="desktoponly">→ Notes on using the "sqlite3.exe" command-line interface that can be used to create, modify, and query arbitrary SQLite database files. </span>
  - <a href="rsync.html" class="sh_link">Remote Copy Of A Live Database</a> <span class="desktoponly">→ The `sqlite3_rsync` program makes a consistent copy of a live database to or from a remote system. </span>
  - <a href="dbhash.html" class="sh_link">Database Hash (dbhash.exe)</a> <span class="desktoponly">→ This program demonstrates how to compute a hash over the content of an SQLite database. </span>
  - <a href="http://www.fossil-scm.org/" class="sh_link">Fossil</a> <span class="desktoponly">→ The Fossil Version Control System is a distributed VCS designed specifically to support SQLite development. Fossil uses SQLite as for storage. </span>
  - <a href="rbu.html" class="sh_link">RBU</a> <span class="desktoponly">→ The "Resumable Bulk Update" utility program allows a batch of changes to be applied to a remote database running on embedded hardware in a way that is resumeable and does not interrupt ongoing operation. </span>
  - <a href="sqlanalyze.html" class="sh_link">SQLite Database Analyzer (sqlite3_analyzer.exe)</a> <span class="desktoponly">→ This stand-alone program reads an SQLite database and outputs a file showing the space used by each table and index and other statistics. Built using the [dbstat virtual table](dbstat.md). </span>
  - <a href="sqldiff.html" class="sh_link">SQLite Database Diff (sqldiff.exe)</a> <span class="desktoponly">→ This stand-alone program compares two SQLite database files and outputs the SQL needed to convert one into the other. </span>
  - <a href="https://sqlite.org/sqlar/" class="sh_link">SQLite Archiver (sqlar.exe)</a> <span class="desktoponly">→ A ZIP-like archive program that uses SQLite for storage. </span>
- <span onclick="showhide(8)"><span id="sh_mark_8" class="sh_mark">►</span> Advocacy</span>
  - <a href="fasterthanfs.html" class="sh_link">35% Faster Than The Filesystem</a> <span class="desktoponly">→ This article points out that reading blobs out of an SQLite database is often faster than reading the same blobs from individual files in the filesystem. </span>
  - <a href="flextypegood.html" class="sh_link">Flexible Typing Is A Feature</a> <span class="desktoponly">→ SQLite provides developers with the freedom to store content in any desired format, regardless of the declared datatype of the column. This article explains why that is a feature, not a bug. </span>
  - <a href="appfileformat.html" class="sh_link">SQLite As An Application File Format</a> <span class="desktoponly">→ This article advocates using SQLite as an application file format in place of XML or JSON or a "pile-of-file". </span>
  - <a href="famous.html" class="sh_link">Well Known Users</a> <span class="desktoponly">→ This page lists a small subset of the many thousands of devices and application programs that make use of SQLite. </span>
  - <a href="whyc.html" class="sh_link">Why SQLite Is Coded In C</a> <span class="desktoponly">→ Why is SQLite not coded in some other trendy language like C++ or Rust? Isn't C obsolete? </span>
  - <a href="whynotgit.html" class="sh_link">Why SQLite Does Not Use Git</a> <span class="desktoponly">→ Why SQLite does not use Git for version control, like most everybody else? </span>
- <span onclick="showhide(9)"><span id="sh_mark_9" class="sh_mark">►</span> Technical and Design Documentation</span>
  - <a href="howtocorrupt.html" class="sh_link">How Database Corruption Can Occur</a> <span class="desktoponly">→ SQLite is highly resistant to database corruption. But application, OS, and hardware bugs can still result in corrupt database files. This article describes many of the ways that SQLite database files can go corrupt. </span>
  - <a href="security.html" class="sh_link">Defense Against Dark Arts</a> <span class="desktoponly">→ Hints for avoiding application vulnerabilities when using SQLite. </span>
  - <a href="tempfiles.html" class="sh_link">Temporary Files Used By SQLite</a> <span class="desktoponly">→ SQLite can potentially use many different temporary files when processing certain SQL statements. This document describes the many kinds of temporary files that SQLite uses and offers suggestions for avoiding them on systems where creating a temporary file is an expensive operation. </span>
  - <a href="inmemorydb.html" class="sh_link">In-Memory Databases</a> <span class="desktoponly">→ SQLite normally stores content in a disk file. However, it can also be used as an in-memory database engine. This document explains how. </span>
  - <a href="atomiccommit.html" class="sh_link">How SQLite Implements Atomic Commit</a> <span class="desktoponly">→ A description of the logic within SQLite that implements transactions with atomic commit, even in the face of power failures. </span>
  - <a href="malloc.html" class="sh_link">Dynamic Memory Allocation in SQLite</a> <span class="desktoponly">→ SQLite has a sophisticated memory allocation subsystem that can be configured and customized to meet memory usage requirements of the application and that is robust against out-of-memory conditions and leak-free. This document provides the details. </span>
  - <a href="custombuild.html" class="sh_link">Customizing And Porting SQLite</a> <span class="desktoponly">→ This document explains how to customize the build of SQLite and how to port SQLite to new platforms. </span>
  - <a href="lockingv3.html" class="sh_link">Locking And Concurrency In SQLite Version 3</a> <span class="desktoponly">→ A description of how the new locking code in version 3 increases concurrency and decreases the problem of writer starvation. </span>
  - <a href="isolation.html" class="sh_link">Isolation In SQLite</a> <span class="desktoponly">→ When we say that SQLite transactions are "serializable" what exactly does that mean? How and when are changes made visible within the same database connection and to other database connections? </span>
  - <a href="optoverview.html" class="sh_link">Overview Of The Optimizer</a> <span class="desktoponly">→ A quick overview of the various query optimizations that are attempted by the SQLite code generator. </span>
  - <a href="queryplanner-ng.html" class="sh_link">The Next-Generation Query Planner</a> <span class="desktoponly">→ Additional information about the SQLite query planner, and in particular the redesign of the query planner that occurred for version 3.8.0. </span>
  - <a href="arch.html" class="sh_link">Architecture</a> <span class="desktoponly">→ An architectural overview of the SQLite library, useful for those who want to hack the code. </span>
  - <a href="opcode.html" class="sh_link">VDBE Opcodes</a> <span class="desktoponly">→ This document is an automatically generated description of the various opcodes that the VDBE understands. Programmers can use this document as a reference to better understand the output of EXPLAIN listings from SQLite. </span>
  - <a href="vfs.html" class="sh_link">Virtual Filesystem</a> <span class="desktoponly">→ The "VFS" object is the interface between the SQLite core and the underlying operating system. Learn more about how the VFS object works and how to create new VFS objects from this article. </span>
  - <a href="vtab.html" class="sh_link">Virtual Tables</a> <span class="desktoponly">→ This article describes the virtual table mechanism and API in SQLite and how it can be used to add new capabilities to the core SQLite library. </span>
  - <a href="fileformat2.html" class="sh_link">The SQLite File Format</a> <span class="desktoponly">→ A description of the format used for SQLite database and journal files, and other details required to create software to read and write SQLite databases without using SQLite. </span>
  - <a href="compile.html" class="sh_link">Compilation Options</a> <span class="desktoponly">→ This document describes the compile time options that may be set to modify the default behavior of the library or omit optional features in order to reduce binary size. </span>
  - <a href="https://sqlite.org/android/" class="sh_link">Android Bindings for SQLite</a> <span class="desktoponly">→ A description of how to compile your own SQLite for Android (bypassing the SQLite that is built into Android) together with code and makefiles. </span>
  - <a href="debugging.html" class="sh_link">Debugging Hints</a> <span class="desktoponly">→ A list of tricks and techniques used to trace, examine, and understand the operation of the core SQLite library. </span>
- <span onclick="showhide(10)"><span id="sh_mark_10" class="sh_mark">►</span> Upgrading SQLite, Backwards Compatibility</span>
  - <a href="35to36.html" class="sh_link">Moving From SQLite 3.5 to 3.6</a> <span class="desktoponly">→ A document describing the differences between SQLite version 3.5.9 and 3.6.0. </span>
  - <a href="34to35.html" class="sh_link">Moving From SQLite 3.4 to 3.5</a> <span class="desktoponly">→ A document describing the differences between SQLite version 3.4.2 and 3.5.0. </span>
  - <a href="changes.html" class="sh_link">Release History</a> <span class="desktoponly">→ A chronology of SQLite releases going back to version 1.0.0 </span>
  - <a href="formatchng.html" class="sh_link">Backwards Compatibility</a> <span class="desktoponly">→ This document details all of the incompatible changes to the SQLite file format that have occurred since version 1.0.0. </span>
  - <a href="privatebranch.html" class="sh_link">Private Branches</a> <span class="desktoponly">→ This document suggests procedures for maintaining a private branch or fork of SQLite and keeping that branch or fork in sync with the public SQLite source tree. </span>
- <span onclick="showhide(11)"><span id="sh_mark_11" class="sh_mark">►</span> Obsolete Documents</span>
  - <a href="asyncvfs.html" class="sh_link">Asynchronous IO Mode</a> <span class="desktoponly">→ This page describes the asynchronous IO extension developed alongside SQLite. Using asynchronous IO can cause SQLite to appear more responsive by delegating database writes to a background thread. *NB: This extension is deprecated. [WAL mode](wal.md) is recommended as a replacement.* </span>
  - <a href="c_interface.html" class="sh_link">Version 2 C/C++ API</a> <span class="desktoponly">→ A description of the C/C++ interface bindings for SQLite through version 2.8 </span>
  - <a href="datatypes.html" class="sh_link">Version 2 DataTypes</a> <span class="desktoponly">→ A description of how SQLite version 2 handles SQL datatypes. Short summary: Everything is a string. </span>
  - <a href="vdbe.html" class="sh_link">VDBE Tutorial</a> <span class="desktoponly">→ The VDBE is the subsystem within SQLite that does the actual work of executing SQL statements. This page describes the principles of operation for the VDBE in SQLite version 2.7. This is essential reading for anyone who want to modify the SQLite sources. </span>
  - <a href="version3.html" class="sh_link">SQLite Version 3</a> <span class="desktoponly">→ A summary of the changes between SQLite version 2.8 and SQLite version 3.0. </span>
  - <a href="capi3.html" class="sh_link">Version 3 C/C++ API</a> <span class="desktoponly">→ A summary of the API related changes between SQLite version 2.8 and SQLite version 3.0. </span>
  - <a href="speed.html" class="sh_link">Speed Comparison</a> <span class="desktoponly">→ The speed of version 2.7.6 of SQLite is compared against PostgreSQL and MySQL. </span>

\
