---
title: SQLite Release 3.53.4 On 2026-07-24
source_url: https://www.sqlite.org/releaselog/current.html
source_path: releaselog/current.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6480
---

## SQLite Release 3.53.4 On 2026-07-24

**Prior changes from version 3.53.0 (2026-04-09):**

1.  Fix the [WAL-reset database corruption bug](../wal.md#walresetbug).
2.  Add the [Query Result Formatter (QRF)](https://sqlite.org/src/file/ext/qrf) library for formatting the results of SQL queries for human readability on a fixed-pitch font screen.
    1.  Add the [format method](../tclsqlite.md#format) to the [TCL Interface](../tclsqlite.md) so that QRF is accessible from TCL.
    2.  QRF is used for result formatting in the [CLI](../cli.md), resulting in improved display capabilities.
3.  New SQL language features:
    1.  Enhance [ALTER TABLE](../lang_altertable.md) to permit adding and removing NOT NULL and CHECK constraints.
    2.  The [REINDEX EXPRESSIONS](../lang_reindex.md) statement rebuilds expression indexes. (Useful to repair [stale expression indexes](../staleexpridx.md).)
    3.  The body of [TEMP triggers](../lang_createtrigger.md#temptrig) may now modify and/or query tables in the main schema.
    4.  Enhance [VACUUM INTO](../lang_vacuum.md#vacuuminto) so that if a [URI filename](../uri.md) is used as the target and that filename has a reserve=N query parameter with N between 0 and 255, then the [reserve amount](../fileformat2.md#resbyte) for the generated database copy is set to N.
4.  New SQL functions:
    1.  [json_array_insert()](../json1.md#jarrayins)
    2.  [jsonb_array_insert()](../json1.md#jarrayins)
5.  Renovations to the [CLI](../cli.md):
    1.  Major enhancements to the [.mode command](../climode.md).
    2.  Improved result formatting, due to the addition of the [QRF extension](https://sqlite.org/src/file/ext/qrf). For example, numeric values are now right-justified by default in [tabular output modes](../climode.md#clmnr).
    3.  The default output mode for interactive CLI sessions now uses QRF to display query results in boxes formed using Unicode box-drawing characters, for improved legibility. Batch CLI sessions use the legacy output format for compatibility.
    4.  Bare (unquoted) semicolons at the end of [dot-commands](../cli.md#dotcmd) are silently ignored.  ← Potential incompatibility!
    5.  Fix the .testcase and .check commands so that they actually work, and use those commands in scripts that are part of the standard SQLite test suite included with the source tree.
    6.  Command-line arguments that match \*.sql or \*.txt and are the names of non-empty files are read and interpreted as scripts of SQL statements and/or [dot-commands](../cli.md#dotcmd).
    7.  The argument to the ".timer" command can now be "once", to run the timer on only the next SQL statement.
    8.  The new "--timeout S" option to the ".progress" dot-command causes SQL statements to interrupt after S seconds.
    9.  The ".indexes" command was changed so that the PATTERN argument matches the name of the index, not the name of the table being indexed (thus making the PATTERN argument actually useful). And, several new options were added to ".indexes".
6.  New C-language interfaces:
    1.  [sqlite3_str_truncate()](../c3ref/str_append.md)
    2.  [sqlite3_str_free()](../c3ref/str_finish.md)
    3.  [sqlite3_carray_bind_v2()](../c3ref/carray_bind.md)
    4.  Add the [SQLITE_PREPARE_FROM_DDL](../c3ref/c_prepare_dont_log.md#sqlitepreparefromddl) option to [sqlite3_prepare_v3()](../c3ref/prepare.md) which permits [virtual table](../vtab.md) implementations to safely prepare SQL statements that are derived from the database schema.
    5.  Added the [SQLITE_UTF8_ZT](../c3ref/c_any.md#sqliteutf8zt) constant which can be used as the encoding parameter to [sqlite3_result_text64()](../c3ref/result_blob.md) or [sqlite3_bind_text64()](../c3ref/bind_blob.md) to indicate that the value is UTF-8 encoded and zero terminated.
    6.  The [SQLITE_LIMIT_PARSER_DEPTH](../c3ref/c_limit_attached.md#sqlitelimitparserdepth) option is added to [sqlite3_limit()](../c3ref/limit.md).
    7.  The [SQLITE_DBCONFIG_FP_DIGITS](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigfpdigits) option is added to [sqlite3_db_config()](../c3ref/db_config.md). See also item 9b below.
7.  Query planner improvements:
    1.  Always use a sort-and-merge algorithm for EXCEPT, INTERSECT, and UNION, since this is almost always faster than using a hash table.
    2.  Improvements to join order selection in large multi-way joins on a star schema.
    3.  Enhance the EXISTS-to-JOIN optimization so that the inserted JOIN terms are not required to be on the inner-most loops, as long as all dependencies for the EXISTS-to-JOIN loops are in outer loops.
    4.  Enhance the omit-noop-join optimization so that it is able to omit a chain of joins that do not affect the output.
    5.  Allow queries that use "GROUP BY e1 ORDER BY e2" where e1 and e2 are identical apart from ASC/DESC sort-orders to be optimized using a single index.
    6.  Allow virtual tables to optimize DISTINCT in cases where the result-set of a query does not exactly match the ORDER BY clause.
8.  Add new interfaces to the [session extension](../sessionintro.md) that enable an application to add changes one at a time to the sqlite3_changegroup object:
    1.  [sqlite3changegroup_change_begin()](../session/sqlite3changegroup_change_begin.md)
    2.  [sqlite3changegroup_change_blob()](../session/sqlite3changegroup_change_blob.md)
    3.  [sqlite3changegroup_change_double()](../session/sqlite3changegroup_change_double.md)
    4.  [sqlite3changegroup_change_int64()](../session/sqlite3changegroup_change_int64.md)
    5.  [sqlite3changegroup_change_null()](../session/sqlite3changegroup_change_null.md)
    6.  [sqlite3changegroup_change_text()](../session/sqlite3changegroup_change_text.md)
    7.  [sqlite3changegroup_change_finish()](../session/sqlite3changegroup_change_finish.md)
    8.  [sqlite3changegroup_config()](../session/sqlite3changegroup_config.md)
9.  Improvements to floating-point ↔ text conversions.
    1.  Reimplemented to improve performance.
    2.  Rounding is now done by [default to 17 significant digits](../floatingpoint.md#*fpdigits), instead of 15, as was the case for all prior versions. The [sqlite3_db_config](../c3ref/db_config.md)([SQLITE_DBCONFIG_FP_DIGITS](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigfpdigits)) API (item 6g above) can change this, if desired.
10. Added the [self-healing index](../staleexpridx.md#selfheal) feature to deal with the [stale expression index](../staleexpridx.md) problem.
11. Add the "-p\|--port" option to [sqlite3_rsync](../rsync.md).
12. Discontinue support for [Windows RT](https://en.wikipedia.org/wiki/Windows_RT).
13. JavaScript/WASM
    1.  Add the "opfs-wl" VFS, functionally identical to the "opfs" VFS but using Web Locks for locking, which can promise fairer lock sharing than the "opfs" bespoke protocol can. "opfs-wl" requires `Atomics.waitAsync()`, so requires newer browsers than "opfs" does.

**Changes in this specific patch release, version 3.53.4 (2026-07-24):**

1.  Fixes for problems in 3.53.0 (and 3.53.1, 3.53.2, and 3.53.3) mostly coming from AIs. See the [check-in timeline](https://sqlite.org/src/timeline?from=version-3.53.0&to=version-3.53.4&to2=branch-3.53&y=ci) for details.
    **Hashes:**
2.  SQLITE_SOURCE_ID: 2026-07-24 19:02:57 bf7c7f30031888f4e796e429ab3978879485813aaca6f641c7b33e4e09459bcc
3.  SHA3-256 for sqlite3.c: 67f423e9ebbbdc473cbc4772c872ee6b89f31fde4ed0279a5c25d5f65c043a16

A [complete list of SQLite releases](../changes.md) in a single page and a [chronology](../chronology.md) are both also available. A detailed history of every check-in is available at [SQLite version control site](https://sqlite.org/src/timeline).
