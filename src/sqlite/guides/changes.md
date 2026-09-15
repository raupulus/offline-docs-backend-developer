---
title: Release History Of SQLite
source_url: https://www.sqlite.org/changes.html
source_path: changes.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2430
---

# Release History

This page provides a high-level summary of changes to SQLite. For more detail, see the Fossil checkin logs at <https://sqlite.org/src/timeline> and <https://sqlite.org/src/timeline?t=release>. See the [chronology](chronology.md) a succinct listing of releases.

<span id="version_3_53_4"></span>

### 2026-07-24 (3.53.4)

1.  Fixes for problems in 3.53.0 (and 3.53.1, 3.53.2, and 3.53.3) mostly coming from AIs. See the [check-in timeline](https://sqlite.org/src/timeline?from=version-3.53.0&to=version-3.53.4&to2=branch-3.53&y=ci) for details.
    **Hashes:**
2.  SQLITE_SOURCE_ID: 2026-07-24 19:02:57 bf7c7f30031888f4e796e429ab3978879485813aaca6f641c7b33e4e09459bcc
3.  SHA3-256 for sqlite3.c: 67f423e9ebbbdc473cbc4772c872ee6b89f31fde4ed0279a5c25d5f65c043a16

<span id="version_3_53_3"></span>

### 2026-06-26 (3.53.3)

1.  Fixes for problems in 3.53.0 (and 3.53.1 and 3.53.2) mostly coming from AIs. See the [check-in timeline](https://sqlite.org/src/timeline?from=version-3.53.0&to=version-3.53.3&to2=branch-3.53&y=ci) for details.
    **Hashes:**
2.  SQLITE_SOURCE_ID: 2026-06-26 20:14:12 d4c0e51e4aeb96955b99185ab9cde75c339e2c29c3f3f12428d364a10d782c62
3.  SHA3-256 for sqlite3.c: 28e484abdaa43630e34040ef6ed92be973a1ad54107803d8af5145b889c23ed7

<span id="version_3_53_2"></span>

### 2026-06-03 (3.53.2)

1.  Fixes for problems in 3.53.0 reported by users. See the [check-in timeline](https://sqlite.org/src/timeline?from=version-3.53.0&to=version-3.53.2&to2=branch-3.53&y=ci) for details.
    **Hashes:**
2.  SQLITE_SOURCE_ID: 2026-06-03 19:12:13 d6e03d8c777cfa2d35e3b60d8ec3e0187f3e9f99d8e2ee9cac695fd6fcdf1a24
3.  SHA3-256 for sqlite3.c: 44fd61b9f93b4155105cb2d80c957ae6c64a8b5bd6ed51a4992f0dbd438e4e11

<span id="version_3_53_1"></span>

### 2026-05-05 (3.53.1)

1.  Fixes for problems in 3.53.1 reported by users. See the [check-in timeline](https://sqlite.org/src/timeline?from=version-3.53.0&to=version-3.53.1&y=ci) for details.
    **Hashes:**
2.  SQLITE_SOURCE_ID: 2026-05-05 10:34:17 c88b22011a54b4f6fbd149e9f8e4de77658ce58143a1af0e3785e4e6475127e9
3.  SHA3-256 for sqlite3.c: 414432ae5719f6cdc485f3927e12c7ad107e2b8c6b434e5df2eadb5312bfabb5

<span id="version_3_53_0"></span>

### 2026-04-09 (3.53.0)

1.  Fix the [WAL-reset database corruption bug](wal.md#walresetbug).
2.  Add the [Query Result Formatter (QRF)](https://sqlite.org/src/file/ext/qrf) library for formatting the results of SQL queries for human readability on a fixed-pitch font screen.
    1.  Add the [format method](tclsqlite.md#format) to the [TCL Interface](tclsqlite.md) so that QRF is accessible from TCL.
    2.  QRF is used for result formatting in the [CLI](cli.md), resulting in improved display capabilities.
3.  New SQL language features:
    1.  Enhance [ALTER TABLE](lang_altertable.md) to permit adding and removing NOT NULL and CHECK constraints.
    2.  The [REINDEX EXPRESSIONS](lang_reindex.md) statement rebuilds expression indexes. (Useful to repair [stale expression indexes](staleexpridx.md).)
    3.  The body of [TEMP triggers](lang_createtrigger.md#temptrig) may now modify and/or query tables in the main schema.
    4.  Enhance [VACUUM INTO](lang_vacuum.md#vacuuminto) so that if a [URI filename](uri.md) is used as the target and that filename has a reserve=N query parameter with N between 0 and 255, then the [reserve amount](fileformat2.md#resbyte) for the generated database copy is set to N.
4.  New SQL functions:
    1.  [json_array_insert()](json1.md#jarrayins)
    2.  [jsonb_array_insert()](json1.md#jarrayins)
5.  Renovations to the [CLI](cli.md):
    1.  Major enhancements to the [.mode command](climode.md).
    2.  Improved result formatting, due to the addition of the [QRF extension](https://sqlite.org/src/file/ext/qrf). For example, numeric values are now right-justified by default in [tabular output modes](climode.md#clmnr).
    3.  The default output mode for interactive CLI sessions now uses QRF to display query results in boxes formed using Unicode box-drawing characters, for improved legibility. Batch CLI sessions use the legacy output format for compatibility.
    4.  Bare (unquoted) semicolons at the end of [dot-commands](cli.md#dotcmd) are silently ignored.  ← Potential incompatibility!
    5.  Fix the .testcase and .check commands so that they actually work, and use those commands in scripts that are part of the standard SQLite test suite included with the source tree.
    6.  Command-line arguments that match \*.sql or \*.txt and are the names of non-empty files are read and interpreted as scripts of SQL statements and/or [dot-commands](cli.md#dotcmd).
    7.  The argument to the ".timer" command can now be "once", to run the timer on only the next SQL statement.
    8.  The new "--timeout S" option to the ".progress" dot-command causes SQL statements to interrupt after S seconds.
    9.  The ".indexes" command was changed so that the PATTERN argument matches the name of the index, not the name of the table being indexed (thus making the PATTERN argument actually useful). And, several new options were added to ".indexes".
6.  New C-language interfaces:
    1.  [sqlite3_str_truncate()](c3ref/str_append.md)
    2.  [sqlite3_str_free()](c3ref/str_finish.md)
    3.  [sqlite3_carray_bind_v2()](c3ref/carray_bind.md)
    4.  Add the [SQLITE_PREPARE_FROM_DDL](c3ref/c_prepare_dont_log.md#sqlitepreparefromddl) option to [sqlite3_prepare_v3()](c3ref/prepare.md) which permits [virtual table](vtab.md) implementations to safely prepare SQL statements that are derived from the database schema.
    5.  Added the [SQLITE_UTF8_ZT](c3ref/c_any.md#sqliteutf8zt) constant which can be used as the encoding parameter to [sqlite3_result_text64()](c3ref/result_blob.md) or [sqlite3_bind_text64()](c3ref/bind_blob.md) to indicate that the value is UTF-8 encoded and zero terminated.
    6.  The [SQLITE_LIMIT_PARSER_DEPTH](c3ref/c_limit_attached.md#sqlitelimitparserdepth) option is added to [sqlite3_limit()](c3ref/limit.md).
    7.  The [SQLITE_DBCONFIG_FP_DIGITS](c3ref/c_dbconfig_defensive.md#sqlitedbconfigfpdigits) option is added to [sqlite3_db_config()](c3ref/db_config.md). See also item 9b below.
7.  Query planner improvements:
    1.  Always use a sort-and-merge algorithm for EXCEPT, INTERSECT, and UNION, since this is almost always faster than using a hash table.
    2.  Improvements to join order selection in large multi-way joins on a star schema.
    3.  Enhance the EXISTS-to-JOIN optimization so that the inserted JOIN terms are not required to be on the inner-most loops, as long as all dependencies for the EXISTS-to-JOIN loops are in outer loops.
    4.  Enhance the omit-noop-join optimization so that it is able to omit a chain of joins that do not affect the output.
    5.  Allow queries that use "GROUP BY e1 ORDER BY e2" where e1 and e2 are identical apart from ASC/DESC sort-orders to be optimized using a single index.
    6.  Allow virtual tables to optimize DISTINCT in cases where the result-set of a query does not exactly match the ORDER BY clause.
8.  Add new interfaces to the [session extension](sessionintro.md) that enable an application to add changes one at a time to the sqlite3_changegroup object:
    1.  [sqlite3changegroup_change_begin()](session/sqlite3changegroup_change_begin.md)
    2.  [sqlite3changegroup_change_blob()](session/sqlite3changegroup_change_blob.md)
    3.  [sqlite3changegroup_change_double()](session/sqlite3changegroup_change_double.md)
    4.  [sqlite3changegroup_change_int64()](session/sqlite3changegroup_change_int64.md)
    5.  [sqlite3changegroup_change_null()](session/sqlite3changegroup_change_null.md)
    6.  [sqlite3changegroup_change_text()](session/sqlite3changegroup_change_text.md)
    7.  [sqlite3changegroup_change_finish()](session/sqlite3changegroup_change_finish.md)
    8.  [sqlite3changegroup_config()](session/sqlite3changegroup_config.md)
9.  Improvements to floating-point ↔ text conversions.
    1.  Reimplemented to improve performance.
    2.  Rounding is now done by [default to 17 significant digits](floatingpoint.md#*fpdigits), instead of 15, as was the case for all prior versions. The [sqlite3_db_config](c3ref/db_config.md)([SQLITE_DBCONFIG_FP_DIGITS](c3ref/c_dbconfig_defensive.md#sqlitedbconfigfpdigits)) API (item 6g above) can change this, if desired.
10. Added the [self-healing index](staleexpridx.md#selfheal) feature to deal with the [stale expression index](staleexpridx.md) problem.
11. Add the "-p\|--port" option to [sqlite3_rsync](rsync.md).
12. Discontinue support for [Windows RT](https://en.wikipedia.org/wiki/Windows_RT).
13. JavaScript/WASM
    1.  Add the "opfs-wl" VFS, functionally identical to the "opfs" VFS but using Web Locks for locking, which can promise fairer lock sharing than the "opfs" bespoke protocol can. "opfs-wl" requires `Atomics.waitAsync()`, so requires newer browsers than "opfs" does.

    **Hashes:**
14. SQLITE_SOURCE_ID: 2026-04-09 11:41:38 4525003a53a7fc63ca75c59b22c79608659ca12f0131f52c18637f829977f20b
15. SHA3-256 for sqlite3.c: bb317fbbd2b3bc53233ddd5894bf4d2dc6f533445f350d4235dbcc86f65af4ec

<span id="version_3_51_3"></span>

### 2026-03-13 (3.51.3)

1.  Fix the [WAL-reset database corruption bug](wal.md#walresetbug).
2.  Other minor bug fixes.
3.  SQLITE_SOURCE_ID: 2026-03-13 10:38:09 737ae4a34738ffa0c3ff7f9bb18df914dd1cad163f28fd6b6e114a344fe6d618
4.  SHA3-256 for sqlite3.c: 32d5424f97e0a7fc5ed2f6335afbb58be4e0298bd7117a34e39d345ff13d859e

<span id="version_3_52_0"></span>

### 2026-03-06 (3.52.0)

1.  *Withdrawn*

    *All of the features that were originally scheduled for the 3.52.0 release have been moved forward into [version 3.53.0](#version_3_53_0).*

<span id="version_3_51_2"></span>

### 2026-01-09 (3.51.2)

1.  Fix an obscure deadlock in the new broken-posix-lock detection logic in item 17 above.
2.  Fix multiple problems in the EXISTS-to-JOIN optimization that was added as part of optimization item 6b above.
3.  Other minor bug fixes.
4.  SQLITE_SOURCE_ID: 2026-01-09 17:27:48 b270f8339eb13b504d0b2ba154ebca966b7dde08e40c3ed7d559749818cb2075
5.  SHA3-256 for sqlite3.c: 733b3fcc6cccb1e334424b9b91a9d68b618385b76ebfcbb106690bd3a9e61367

<span id="version_3_51_1"></span>

### 2025-11-28 (3.51.1)

1.  Fix incorrect results from nested EXISTS queries caused by the optimization in item 6b in the 3.51.0 release.
2.  Fix a latent bug in [fts5vocab](fts5.md#the_fts5vocab_virtual_table_module) virtual table, exposed by new optimizations in the 3.51.0 release
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2025-11-28 17:28:25 281fc0e9afc38674b9b0991943b9e9d1e64c6cbdb133d35f6f5c87ff6af38a88
4.  SHA3-256 for sqlite3.c: 7cec3a104797bea93970408168197af37f178ab608ea55efd48d28daa87a8ce3

<span id="version_3_51_0"></span>

### 2025-11-04 (3.51.0)

1.  New macros in `sqlite3.h`:
    1.  `SQLITE_SCM_BRANCH` → the name of the branch from which the source code is taken.
    2.  `SQLITE_SCM_TAGS` → space-separated list of tags on the source code check-in.
    3.  `SQLITE_SCM_DATETIME` → ISO-8601 date and time of the source code check-in.
2.  Two new JSON functions, [jsonb_each()](json1.md#jbeach) and [jsonb_tree()](json1.md#jbtree) work the same as the existing json_each() and json_tree() functions except that they return [JSONB](json1.md#jsonbx) for the "value" column when the "type" is 'array' or 'object'.
3.  The [carray](carray.md) and [percentile](percentile.md) extensions are now built into [the amalgamation](amalgamation.md), though they are disabled by default and must be activated at compile-time using the [-DSQLITE_ENABLE_CARRAY](compile.md#enable_carray) and/or [-DSQLITE_ENABLE_PERCENTILE](compile.md#enable_percentile) options, respectively.
4.  Enhancements to [TCL Interface](tclsqlite.md):
    1.  Add the `-asdict` flag to the `eval` command to have it set the row data as a dict instead of an array.
    2.  User-defined functions may now `break` to return an SQL NULL.
5.  [CLI](cli.md) enhancements:
    1.  Increase the precision of ".timer" to microseconds.
    2.  Enhance the "box" and "column" formatting modes to deal with double-wide characters.
    3.  The ".imposter" command provides read-only [imposter tables](imposter.md) that work with [VACUUM](lang_vacuum.md) and do not require the --unsafe-testing option.
    4.  Add the --ifexists option to the CLI command-line option and to the [.open command](cli.md#dotopen).
    5.  Limit columns widths set by the ".width" command to 30,000 or less, as there is not good reason to have wider columns, but supporting wider columns provides opportunity to malefactors.
6.  Performance enhancements:
    1.  Use fewer CPU cycles to commit a read transaction.
    2.  Early detection of joins that return no rows due to one or more of the tables containing no rows.
    3.  Avoid evaluation of scalar subqueries if the result of the subquery does not change the result of the overall expression.
    4.  Faster window function queries when using "`BETWEEN :x FOLLOWING AND :y FOLLOWING`" with a large :y.
7.  Add the [PRAGMA wal_checkpoint=NOOP;](pragma.md#pragma_wal_checkpoint) command and the [SQLITE_CHECKPOINT_NOOP](c3ref/c_checkpoint_full.md) argument for [sqlite3_wal_checkpoint_v2()](c3ref/wal_checkpoint_v2.md).
8.  Add the [sqlite3_set_errmsg()](c3ref/set_errmsg.md) API for use by extensions.
9.  Add the [sqlite3_db_status64()](c3ref/db_status.md) API, which works just like the existing [sqlite3_db_status()](c3ref/db_status.md) API except that it returns 64-bit results.
10. Add the [SQLITE_DBSTATUS_TEMPBUF_SPILL](c3ref/c_dbstatus_options.md) option to the [sqlite3_db_status()](c3ref/db_status.md) and [sqlite3_db_status64()](c3ref/db_status.md) interfaces.
11. In the [session extension](sessionintro.md) add the [sqlite3changeset_apply_v3()](session/sqlite3changeset_apply.md) interface.
12. For the [built-in printf()](printf.md) and the [format() SQL function](lang_corefunc.md#format), omit the leading '-' from negative floating point numbers if the '+' flag is omitted and the "#" flag is present and all displayed digits are '0'. Use '%#f' or similar to avoid outputs like '-0.00' and instead show just '0.00'.
13. Improved error messages generated by [FTS5](fts5.md).
14. Enforce STRICT typing on computed columns.
15. Improved support for VxWorks
16. JavaScript/WASM now supports 64-bit WASM. The canonical builds continue to be 32-bit but creating one's own 64-bit build is now as simple as running "make".
17. Improved resistance to database corruption caused by an application [breaking Posix advisory locks using close()](howtocorrupt.md#posix_close_bug).
    **Hashes:**
18. SQLITE_SOURCE_ID: 2025-11-04 19:38:17 fb2c931ae597f8d00a37574ff67aeed3eced4e5547f9120744ae4bfa8e74527b
19. SHA3-256 for sqlite3.c: e2add951748f73587cadd1b2684defb4f39fa58dca14b16162d4237e50af9afa

<span id="version_3_50_4"></span>

### 2025-07-30 (3.50.4)

1.  Fix two long-standings cases of the use of uninitialized variables in obscure circumstances.
    **Hashes:**
2.  SQLITE_SOURCE_ID: 2025-07-30 19:33:53 4d8adfb30e03f9cf27f800a2c1ba3c48fb4ca1b08b0f5ed59a4d5ecbf45e20a3
3.  SHA3-256 for sqlite3.c: 9145255e83da6529e70121ee4d7a4c88fe83ca4511da0c9ed13d10842df36782

<span id="version_3_50_3"></span>

### 2025-07-17 (3.50.3)

1.  Fix a possible memory error that can occur if a query is made against against FTS5 index that has been deliberately corrupted in a very specific way.
2.  Fix the parser so that it ignored SQL comments in all places of a CREATE TRIGGER statement. This resolves a problem that was introduced by the introduction of the SQLITE_DBCONFIG_ENABLE_COMMENTS feature in version 3.49.0.
3.  Fix an incorrect answer due to over-optimization of an AND operator. [Forum post f4878de3e](https://sqlite.org/forum/forumpost/f4878de3e7dd4764).
4.  Fix minor makefile issues and documentation typos.
    **Hashes:**
5.  SQLITE_SOURCE_ID: 2025-07-17 13:25:10 3ce993b8657d6d9deda380a93cdd6404a8c8ba1b185b2bc423703e41ae5f2543
6.  SHA3-256 for sqlite3.c: 934fafe96caa7f4c16e82e0c2b674441a715c038acc9780bf15e09411daba70c

<span id="version_3_50_2"></span>

### 2025-06-28 (3.50.2)

1.  Fix the [concat_ws()](lang_corefunc.md#concat_ws) SQL function so that it includes empty strings in the concatenation. [Forum post 52503ac21d](https://sqlite.org/forum/forumpost/52503ac21d).
2.  Fix the file-io extension (used by the CLI) so that it can be built using the MinGW compiler chain.
3.  Avoid writing frames with no checksums into the wal file if a savepoint is rolled back after dirty pages have already been spilled into the wal file. [Forum post b490f726db](https://sqlite.org/forum/forumpost/b490f726db).
4.  Fix the Bitvec object to avoid stack overflow when the database is within 60 pages of its maximum size.
5.  Fix a problem with UPDATEs on fts5 tables that contain BLOB values.
6.  Fix an issue with transitive IS constraints on a RIGHT JOIN.
7.  Raise an error early if the number of aggregate terms in a query exceeds the maximum number of columns, to avoid downstream assertion faults.
8.  Ensure that sqlite3_setlk_timeout() holds the database mutex.
9.  Fix typos in API documentation.
    **Hashes:**
10. SQLITE_SOURCE_ID: 2025-06-28 14:00:48 2af157d77fb1304a74176eaee7fbc7c7e932d946bf25325e9c26c91db19e3079
11. SHA3-256 for sqlite3.c: 889bf23942c52f38a6f182e71d3f0a03db490fd731f02147b1142c11153f3b3a

<span id="version_3_50_1"></span>

### 2025-06-06 (3.50.1)

1.  Fix a long-standing bug in [jsonb_set()](json1.md#jsetb) and similar that was exposed by new optimizations added in version 3.50.0.
2.  Fix an apparently harmless ASAN warning that can occur on builds that use [-DSQLITE_DEFAULT_MEMSTATUS=0](compile.md#default_memstatus).
3.  Fix an off-by-one bug in [sqlite3_rsync](rsync.md) that can result in the last page not being transferred for the replicate database.
4.  Query planner optimization: Allow the right-hand side of a LEFT JOIN to be [flattened](optoverview.md#flattening) even if it is a virtual table.
5.  Fix [sqlite3_setlk_timeout()](c3ref/setlk_timeout.md) to use a blocking lock when opening a snapshot transaction and when blocked by another process running recovery.
6.  Other minor fixes that were reported after the 3.50.0 release.
    **Hashes:**
7.  SQLITE_SOURCE_ID: 2025-06-06 14:52:32 b77dc5e0f596d2140d9ac682b2893ff65d3a4140aa86067a3efebe29dc914c95
8.  SHA3-256 for sqlite3.c: c3bdffa01dab94be370bdcaeb819cda4a6e0c61f0c6e19a6f94ccba76fc9eeca

<span id="version_3_50_0"></span>

### 2025-05-29 (3.50.0)

1.  Add the [sqlite3_setlk_timeout()](c3ref/setlk_timeout.md) interface which sets a separate timeout, distinct from the [sqlite3_busy_timeout()](c3ref/busy_timeout.md), for blocking locks on builds that support blocking locks.
2.  The [SQLITE_DBCONFIG_ENABLE_COMMENTS](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenablecomments) constraint (added in the [previous release](#version_3_49_0)) is relaxed slightly so that comments are always allowed when reading the schema out of a pre-existing [sqlite_schema](schematab.md) table. Comments are only blocked in new SQL.
3.  New SQL functions:
    1.  [unistr()](lang_corefunc.md#unistr)
    2.  [unistr_quote()](lang_corefunc.md#unistr_quote)
4.  For the [%Q and %q conversions](printf.md#percentq) in the [built-in printf()](printf.md) (which covers the [sqlite3_mprintf()](c3ref/mprintf.md) API and the [format() SQL function](lang_corefunc.md#format) and similar) the [alternate-form-1 flag](printf.md#alt1) ("#") causes [control characters](climode.md#ctrlchr) to be converted into backslash-escapes suitable for [unistr()](lang_corefunc.md#unistr).
5.  CLI enhancements:
    1.  Avoids direct output of most [control characters](climode.md#ctrlchr).
    2.  The output of the [.dump command](cli.md#dump) makes use of the new [unistr()](lang_corefunc.md#unistr) SQL function to encode special characters, unless the --escape mode is set to off.
    3.  Better formatting of complex partial indexes in the output from the [".schema --indent" command](cli.md#dschema).
6.  Enhancements to [sqlite3_rsync](rsync.md):
    1.  The requirement that the database be in WAL mode has been removed.
    2.  The sync protocol is enhanced to use less network bandwidth when both sides start out being very similar to one another.
    3.  The sqlite3_rsync program now works on Macs without having to specify the full pathname of the sqlite3_rsync executable on the remote side as long as you install the sqlite3_rsync executable in one of these directories: \$HOME/bin:/usr/local/bin:/opt/homebrew/bin
7.  Changes to JSON functions:
    1.  Bug fix: Enforce the JSON5 restriction that the "\0" escape must not be followed by a digit.
    2.  Bug fix: When the LABEL argument to [json_group_object(LABEL,VALUE)](json1.md#jgroupobject) is NULL, that element of the resulting object is omitted.
    3.  Optimization: If the [jsonb_set()](json1.md#jsetb) or [jsonb_replace()](json1.md#jreplb) functions make a change in the interior of a large [JSONB](json1.md#jsonbx) object, they strive to keep the size of the JSONB object unchanged and to modify as few bytes as possible on the interior of the object. This helps reduce I/O as it allows SQLite to write only the page that contains the changed bytes and not all the surrounding pages.
8.  Improved support for building on Cygwin and MinGW and similar, as well as Termux.
9.  Typo fixes in the documentation and in the source code comments.
10. Miscellaneous performance improvements.
11. JavaScript/WASM:
    1.  Fix a long-standing filename digest calculation bug in the OPFS SAHPool VFS. Databases created in that VFS by 3.50.0+ cannot be read by older versions of the VFS, but 3.50.0 can backwards-compatibly work with existing databases created by older versions.

    **Hashes:**
12. SQLITE_SOURCE_ID: 2025-05-29 14:26:00 dfc790f998f450d9c35e3ba1c8c89c17466cb559f87b0239e4aab9d34e28f742
13. SHA3-256 for sqlite3.c: b8a2bcdd2ec60f87c3bbe7a2c25eb65e476e40fe80cd066ab8aa98e5d516c1e4

<span id="version_3_49_2"></span>

### 2025-05-07 (3.49.2)

1.  Fix a bug in the NOT NULL optimization of version 3.40.0 (item 3c in the [version 3.40.0 change log](#version_3_40_0)) that can lead to a memory error if abused.
2.  Fix the count-of-view optimization so that it does not give an incorrect answer for a DISTINCT query.
3.  Fix a possible incorrect answer that can result if a UNIQUE constraint of a table contains the PRIMARY KEY column and that UNIQUE constraint is used by an IN operator.
4.  Fix obscure problems with the generate_series() extension function.
5.  Incremental improvements to the configure/make.
    **Hashes:**
6.  SQLITE_SOURCE_ID: 2025-05-07 10:39:52 17144570b0d96ae63cd6f3edca39e27ebd74925252bbaf6723bcb2f6b4861fb1
7.  SHA3-256 for sqlite3.c: 17f4857fc6a0def2749d248d5365c59282c044270533c6c2b21287295f01eb23

<span id="version_3_49_1"></span>

### 2025-02-18 (3.49.1)

1.  Improve portability of makefiles and configure scripts.
2.  Fix a bug in the [concat_ws()](lang_corefunc.md#concat_ws) function, introduced in [version 3.44.0](#version_3_44_0), that could lead to a memory error, specifically a write past the end of allocated space, if the separator string is larger than two megabytes.
3.  Enhanced the [SQLITE_DBCONFIG_LOOKASIDE](c3ref/c_dbconfig_defensive.md#sqlitedbconfiglookaside) interface to make it more robust against misuse.
    **Hashes:**
4.  SQLITE_SOURCE_ID: 2025-02-18 13:38:58 873d4e274b4988d260ba8354a9718324a1c26187a4ab4c1cc0227c03d0f10e70
5.  SHA3-256 for sqlite3.c: 22eab05c842463a3705c63922f12f68531200185ced510ed6aed2065ca44e816

<span id="version_3_49_0"></span>

### 2025-02-06 (3.49.0)

1.  Enhancements to the [query planner](optoverview.md):
    1.  Improve the [query-time index](optoverview.md#autoindex) optimization so that it works on [WITHOUT ROWID](withoutrowid.md) tables.
    2.  Better query plans for large [star-query](queryplanner-ng.md#starq) joins. This fixes three different performance regressions that were reported on the SQLite Forum.
    3.  When two or more queries have the same estimated cost, use the one with the fewer bytes per row.
2.  Enhance the [iif() SQL function](lang_corefunc.md#iif) so that it can accept any number of arguments greater than or equal to two.
3.  Enhance the [session extension](sessionintro.md) so that it works on databases that make use of [generated columns](gencol.md).
4.  Omit the SQLITE_USE_STDIO_FOR_CONSOLE compile-time option which was not implemented correctly and never worked right. In its place add the SQLITE_USE_W32_FOR_CONSOLE_IO compile-time option. This option applies to command-line tools like the [CLI](cli.md) only, not to the SQLite core. It causes Win32 APIs to be used for console I/O instead of stdio. This option affects Windows builds only.
5.  Three new options to [sqlite3_db_config()](c3ref/db_config.md). All default to "on".
    1.  [SQLITE_DBCONFIG_ENABLE_ATTACH_CREATE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableattachcreate)
    2.  [SQLITE_DBCONFIG_ENABLE_ATTACH_WRITE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableattachwrite)
    3.  [SQLITE_DBCONFIG_ENABLE_COMMENTS](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenablecomments)
6.  Replace [Autotools](https://en.wikipedia.org/wiki/GNU_Autotools) with [Autosetup](https://msteveb.github.io/autosetup/) for the configure script used in the [precompiled amalgamation tarball](amalgamation.md#amalgtarball). The configure script for the [canonical source code](amalg-v-canon.md#canon) was changed to Autosetup in the previous (3.48.0) release. Only the main SQLite configure script in the amalgamation tarball is changed. The (deprecated) configuration script use by [TEA](https://www.tcl-lang.org/doc/tea/TEAOverview.html) subdirectory of the amalgamation tarball still relies on Autotools.
7.  Various minor patches and fixes for problems seen in the 3.48.0 release.
    **Hashes:**
8.  SQLITE_SOURCE_ID: 2025-02-06 11:55:18 4a7dd425dc2a0e5082a9049c9b4a9d4f199a71583d014c24b4cfe276c5a77cde
9.  SHA3-256 for sqlite3.c: 030c764eba64a3fa3bbf87447abd175bfef94851f970d62126a92877b30b611e

<span id="version_3_48_0"></span>

### 2025-01-14 (3.48.0)

1.  Refactor the "configure" script used to help build SQLite from [canonical sources](amalg-v-canon.md#canon), to fix bugs, improve performance, and make the code more maintainable.
    - This does not affect the "configure" script in the sqlite3-autoconf-NNNNNNN.tar.gz "amalgamation tarball", only the [canonical sources](amalg-v-canon.md#canon). The build system for the amalgamation tarball is unchanged. If you are using the amalgamation tarball, nothing about this change log entry applies to you.
    - The key innovation here is that [Autosetup](https://msteveb.github.io/autosetup/) is now used instead of [GNU Autoconf](https://www.gnu.org/software/autoconf/). That seems like a big change, but it is really just an implementation detail. The ./configure script is coded very differently, but should work the same as before.
    - One advantage of the new configure is that you no longer need to install [TCL](https://en.wikipedia.org/wiki/Tcl) in order to build most SQLite targets. TCL is still required to run tests or to build accessory programs (like [sqlite3_analyzer](sqlanalyze.md)) that use TCL, but it is not required for most common targets. Hence, as of this release, the only build dependencies are a C compiler and "make" or "nmake".
2.  Improved [EXPLAIN QUERY PLAN](eqp.md) output for [covering indexes](queryplanner.md#covidx).
3.  Allow a two-argument version of the [iif() SQL function](lang_corefunc.md#iif). Also allow [if()](lang_corefunc.md#iif) as an alternative spelling for [iif()](lang_corefunc.md#iif).
4.  Add the ".dbtotxt" command to the [CLI](cli.md).
5.  Add the [SQLITE_IOCAP_SUBPAGE_READ](c3ref/c_iocap_atomic.md) property to the xDeviceCharacteristics method of the [sqlite3_io_methods](c3ref/io_methods.md) object.
6.  Add the [SQLITE_PREPARE_DONT_LOG](c3ref/c_prepare_dont_log.md#sqlitepreparedontlog) option to [sqlite3_prepare_v3()](c3ref/prepare.md) that prevents warning messages being sent to the [error log](errlog.md) if the SQL is ill-formed. This allows sqlite3_prepare_v3() to be used to do test compiles of SQL to check for validity without polluting the error log with false messages.
7.  Increase the minimum allowed value of [SQLITE_LIMIT_LENGTH](c3ref/c_limit_attached.md#sqlitelimitlength) from 1 to 30.
8.  Added the [SQLITE_FCNTL_NULL_IO](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlnullio) file control.
9.  Extend the FTS5 auxiliary API xInstToken() to work with prefix queries via the [insttoken](fts5.md#the_insttoken_configuration_option) configuration option and the [fts5_insttoken()](fts5.md#the_fts5_insttoken_function) SQL function.
10. Increase the [maximum number of arguments to an SQL function](limits.md#max_function_arg) from 127 to 1000.
11. Remove vestigial traces of SQLITE_USER_AUTHENTICATION.
12. Various obscure bug fixes.
    **Hashes:**
13. SQLITE_SOURCE_ID: 2025-01-14 11:05:00 d2fe6b05f38d9d7cd78c5d252e99ac59f1aea071d669830c1ffe4e8966e84010
14. SHA3-256 for sqlite3.c: 522bd9492526147d12fc8521028eb960557353d8f08c2035f15ac737d4b91e21

<span id="version_3_47_2"></span>

### 2024-12-07 (3.47.2)

1.  Fix a problem in text-to-floating-point conversion for SQLite that can cause values between '1.8446744073709550592eNNN' and '1.8446744073709551609eNNN' for any exponent NNN to be rendered incorrectly. In other words, some numeric text values where the first 16 significant digits are '1844674407370955' might be converted into the wrong floating-point value. See [forum thread 569a7209179a7f5e](https://sqlite.org/forum/forumpost/569a7209179a7f5e). This problem only arises on x64 and i386 hardware. The problem was introduced in 3.47.0.
2.  Other minor bug fixes.
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2024-12-07 20:39:59 2aabe05e2e8cae4847a802ee2daddc1d7413d8fc560254d93ee3e72c14685b6c
4.  SHA3-256 for sqlite3.c: 586b5789453ee5c51e8d858cd836f20ce60df882323f2070547cbaf23a5898af

<span id="version_3_47_1"></span>

### 2024-11-25 (3.47.1)

1.  Fix the makefiles so that they once again honored DESTDIR for the "install" target.
2.  Add the [SQLITE_IOCAP_SUBPAGE_READ](c3ref/c_iocap_atomic.md) capability to the VFS, to work around issues on some non-standard VFSes caused by making SQLITE_DIRECT_OVERFLOW_READ the default in version 3.45.0.
3.  Fix problems with line endings in the new sqlite3_rsync.exe utility on Windows.
4.  Fix incorrect answers to certain obscure IN queries caused by new query optimizations added in the 3.47.0 release.
5.  Other minor bug fixes.
    **Hashes:**
6.  SQLITE_SOURCE_ID: 2024-11-25 12:07:48 b95d11e958643b969c47a8e5857f3793b9e69700b8f1469371386369a26e577e
7.  SHA3-256 for sqlite3.c: d91b8b5671a127bd41057bc758d6d59fb7aceda67934a1c0166ab2e133f2f902

<span id="version_3_47_0"></span>

### 2024-10-21 (3.47.0)

1.  Allow arbitrary expressions in the second argument to the [RAISE function](lang_createtrigger.md#raise).
2.  If the RHS of [the -\>\> operator](json1.md#jptr) is negative, then access array elements counting from the right.
3.  Fix a problem with rolling back hot journal files in the seldom-used [unix-dotfile VFS](../vfs.md#standard_unix_vfses).
4.  FTS5 tables can now be dropped even if they use a non-standard tokenizer that has not been registered.
5.  Fix the [group_concat() aggregate function](lang_aggfunc.md#group_concat) so that it returns an empty string, not a NULL, if it receives a single input value which is an empty string.
6.  Enhance the [generate_series()](series.md) table-valued function so that it is able to recognize and use constraints on its output value.
7.  Preupdate hooks now recognize when a column added by ALTER TABLE ADD COLUMN has a non-null default value.
8.  Performance optimizations:
    1.  Improved reuse of subqueries associated with the [IN operator](lang_expr.md#in_op), especially when the IN operator has been duplicated due to [predicate push-down](optoverview.md#pushdown).
    2.  Use a Bloom filter on subqueries on the right-hand side of the [IN operator](lang_expr.md#in_op), in cases where that seems likely to improve performance.
    3.  Ensure that queries like "`SELECT func(a) FROM tab GROUP BY 1`" only invoke the func() function once per row.
    4.  No attempt is made to create [automatic indexes](optoverview.md#autoindex) on a column that is known to be non-selective because of its use in other indexes that have been analyzed.
    5.  Adjustments to the query planner so that it produces better plans for star queries with a large number of dimension tables.
    6.  Add the "order-by-subquery" optimization, that seeks to disable sort operations in outer queries if the desired order is obtained naturally due to ORDER BY clauses in subqueries.
    7.  The "indexed-subtype-expr" optimization strives to use expressions that are part of an index rather than recomputing the expression based on table values, as long as the query planner can prove that the [subtype](c3ref/value_subtype.md) of the expression will never be used.
    8.  Miscellaneous coding tweaks for faster runtimes.
9.  Enhancements to SQLite-related command-line programs:
    1.  Add the experimental [sqlite3_rsync](rsync.md) program.
    2.  Add extension functions [median()](lang_aggfunc.md#median), [percentile()](lang_aggfunc.md#percentile), [percentile_cont()](lang_aggfunc.md#percentile_cont), and [percentile_disc()](lang_aggfunc.md#percentile_disc) to the [CLI](cli.md).
    3.  Add the [.www dot-command](cli.md#dotwww) to the [CLI](cli.md).
    4.  The [sqlite3_analyzer](sqlanalyze.md) utility now provides a break-out of statistics for WITHOUT ROWID tables.
    5.  The [sqldiff](sqldiff.md) utility avoids creating an empty database if its second argument does not exist.
10. Enhance the [sqlite_dbpage](dbpage.md) table-valued function such that [INSERT](lang_insert.md) can be used to increase or decrease the size of the database file.
11. SQLite no longer makes any use of the "long double" data type, as hardware support for long double is becoming less common and long double creates challenges for some compiler tool chains. Instead, SQLite uses [Dekker's algorithm](https://csclub.uwaterloo.ca/~pbarfuss/dekker1971.pdf) when extended precision is needed.
12. The [TCL Interface](tclsqlite.md) for SQLite supports TCL9. Everything probably still works for TCL 8.5 and later, though this is not guaranteed. Users are encouraged to upgrade to TCL9.
13. JavaScript/WASM:
    1.  Fix a corruption-causing bug in the JavaScript "opfs" VFS.
    2.  Correct "mode=ro" handling for the "opfs" VFS.
    3.  Work around a couple of browser-specific OPFS quirks.
14. FTS5 Changes:
    1.  Add the fts5_tokenizer_v2 API and the locale=1 option, for creating custom locale-aware tokenizers and fts5 tables that may take advantage of them.
    2.  Add the contentless_unindexed=1 option, for creating contentless fts5 tables that store the values of any UNINDEXED columns persistently in the database.
    3.  Allow an FTS5 table to be dropped even if it uses a custom tokenizer whose implementation is not available.

    **Hashes:**
15. SQLITE_SOURCE_ID: 2024-10-21 16:30:22 03a9703e27c44437c39363d0baf82db4ebc94538a0f28411c85dda156f82636e
16. SHA3-256 for sqlite3.c: bcec3a4fbc97e973547924677332996ef64e06a6d10d22e2c2344f447536cc29

<span id="version_3_46_1"></span>

### 2024-08-13 (3.46.1)

1.  Improved robustness while parsing the [tokenize= arguments](fts5.md#tokenizers) in [FTS5](fts5.md). [Forum post 171bcc2bcd](https://sqlite.org/forum/forumpost/171bcc2bcd).
2.  Enhancements to [covering index](queryplanner.md#covidx) prediction in the query planner. Add early detection of over-prediction of covering indexes so that [sqlite3_prepare()](c3ref/prepare.md) will return an error rather than just generate bad bytecode. [Forum post e60e4c295d22f8ce](https://sqlite.org/forum/forumpost/e60e4c295d22f8ce).
3.  Do not let the number of terms on a [VALUES clause](lang_select.md#values) be limited by [SQLITE_LIMIT_COMPOUND_SELECT](c3ref/c_limit_attached.md#sqlitelimitcompoundselect), even if the VALUES clause contains elements that appear to be variables due to [double-quoted string literals](quirks.md#dblquote).
4.  Fix the [window function](windowfunctions.md) version of [group_concat()](lang_aggfunc.md#group_concat) so that it returns an empty string if it has one or more empty string inputs.
5.  In [FTS5 secure-delete mode](fts5.md#the_secure_delete_configuration_option), fix false-positive integrity-check reports about corrupt indexes.
6.  Syntax errors in [ALTER TABLE](lang_altertable.md) should always return [SQLITE_ERROR](rescode.md#error). In some cases, they were formerly returning [SQLITE_INTERNAL](rescode.md#internal).
7.  JavaScript/WASM:
    1.  Fix a corruption-causing bug in the JavaScript "opfs" VFS.
    2.  Work around a couple of browser-specific OPFS quirks.
8.  Other minor fixes.
    **Hashes:**
9.  SQLITE_SOURCE_ID: 2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69a1e33
10. SHA3-256 for sqlite3.c: 186a1baa476b6d546de155160ca6d30ff7b7e6ee375f0bb6445e1a3d180a7dad

<span id="version_3_46_0"></span>

### 2024-05-23 (3.46.0)

1.  Enhance [PRAGMA optimize](pragma.md#pragma_optimize) in multiple ways, to make it [simpler to use](lang_analyze.md#pragopt):
    1.  PRAGMA optimize automatically implements a temporary [analysis limit](pragma.md#pragma_analysis_limit) to prevent excess runtime on large databases.
    2.  Added the new 0x10000 bitmask option to check for updates on all tables.
    3.  Automatically re-analyze tables that do not have sqlite_stat1 entries.
2.  Enhancements to the [date and time functions](lang_datefunc.md):
    1.  The [strftime() SQL function](lang_datefunc.md#strftm) now supports %G, %g, %U, and %V.
    2.  New modifiers 'ceiling' and 'floor' control the algorithm used to resolve [ambiguous dates](lang_datefunc.md#dtambg) when shifting a date by an integer number of months and/or years.
    3.  The ['utc' and 'localtime' modifiers](lang_datefunc.md#localtime) are now no-ops if SQLite knows that the time is already in UTC or in the localtime, respectively.
3.  Add support for underscore ("\_") characters between digits in [numeric literals](lang_expr.md#litvalue).
4.  Add the [json_pretty()](json1.md#jpretty) SQL function.
5.  Query planner improvements:
    1.  The "VALUES-as-coroutine" optimization enables INSERT statements with thousands of rows in the VALUES clause to parse and run in about half the time and using about half as much memory.
    2.  Allow the use of an index for queries like "SELECT count(DISTINCT col) FROM ...", even if the index records are not smaller than the table records.
    3.  Improved recognition of cases where the value of an SQL function is constant because all its arguments are constant.
    4.  Enhance the [WHERE-clause push-down optimization](optoverview.md#pushdown) so that it is able to push down WHERE clause terms containing uncorrelated subqueries.
6.  Allocate additional memory from the heap for the SQL parser stack if that stack overflows, rather than reporting a "parser stack overflow" error.
7.  JSON changes:
    1.  Allow ASCII control characters within JSON5 string literals.
    2.  Fix [the -\> and -\>\> operators](json1.md#jptr) so that when the right-hand side operand is a string that looks like an integer it is still treated as a string, because that is what PostgreSQL does.
8.  Allow large hexadecimal literals to be used as the DEFAULT value to a table column.
    **Hashes:**
9.  SQLITE_SOURCE_ID: 2024-05-23 13:25:27 96c92aba00c8375bc32fafcdf12429c58bd8aabfcadab6683e35bbb9cdebf19e
10. SHA3-256 for sqlite3.c: 094429ea827fcd32275e767134bc6c7b9ea394a2c5a9e653dd0a0690b2c11358

<span id="version_3_45_3"></span>

### 2024-04-15 (3.45.3)

1.  Fix a long-standing bug (going back to [version 3.24.0](#version_3_24_0)) that might (rarely) cause the "old.\*" values of an [UPDATE trigger](lang_createtrigger.md) to be incorrect if that trigger fires in response to an [UPSERT](lang_upsert.md). [Forum post 284955a3cd454a15](https://sqlite.org/forum/forumpost/284955a3cd454a15).
2.  Fix a bug in [sum()](lang_aggfunc.md#sumunc) that could cause it to return NULL when it should return Infinity. [Forum post 23b8688ef4](https://sqlite.org/forum/forumpost/23b8688ef4).
3.  Other trifling corrections and compiler warning fixes that have come up since the previous patch release. See the [timeline](https://sqlite.org/src/timeline?from=version-3.45.2&to=version-3.45.3&to2=branch-3.45) for details.
    **Hashes:**
4.  SQLITE_SOURCE_ID: 2024-04-15 13:34:05 8653b758870e6ef0c98d46b3ace27849054af85da891eb121e9aaa537f1e8355
5.  SHA3-256 for sqlite3.c: 21dbe688a71b449d28e2a8ec6a43e7520e54df456e02b6d4f6a1d1c7a998c826

<span id="version_3_45_2"></span>

### 2024-03-12 (3.45.2)

1.  Fix an error in [UPSERT](lang_upsert.md), introduced by enhancement 3a in [version 3.35.0](#version_3_35_0) (2021-03-12), that could cause an index to get out-of-sync with its table. [Forum thread 919c6579c8](https://sqlite.org/forum/forumpost/919c6579c8).
2.  Reduce the scope of the NOT NULL strength reduction optimization that was added as item 8e in [version 3.35.0](#version_3_35_0) (2021-03-12). The optimization was being attempted in some contexts where it did not work, resulting in incorrect query results. [Forum thread 440f2a2f17](https://sqlite.org/forum/forumpost/440f2a2f17).
3.  Other trifling corrections and compiler warning fixes that have come up since the previous patch release. See the [timeline](https://sqlite.org/src/timeline?from=version-3.45.1&to=version-3.45.2&to2=branch-3.45) for details.
    **Hashes:**
4.  SQLITE_SOURCE_ID: "2024-03-12 11:06:23 d8cd6d49b46a395b13955387d05e9e1a2a47e54fb99f3c9b59835bbefad6af77"
5.  SHA3-256 for sqlite3.c: bd76ad2dc9cde151e469e86627a7e8753aa8ef1a6f657c5a80ba48324b53226b

<span id="version_3_45_1"></span>

### 2024-01-30 (3.45.1)

1.  Restore the [JSON BLOB input bug](json1.md#jblobbug), and promise to support the anomaly in subsequent releases, for backward compatibility.
2.  Fix the [PRAGMA integrity_check](pragma.md#pragma_integrity_check) command so that it works on read-only databases that contain FTS3 and FTS5 tables. This resolves an issue introduced in [version 3.44.0](#version_3_44_0) but was undiscovered until after the 3.45.0 release.
3.  Fix issues associated with processing corrupt [JSONB](json1.md#jsonbx) inputs:
    1.  Prevent exponential runtime when converting a corrupt JSONB into text.
    2.  Fix a possible read of one byte past the end of the JSONB blob when converting a corrupt JSONB into text.
    3.  Enhanced testing using [jfuzz](testing.md#dbsqlfuzz) to prevent any future JSONB problems such as the above.
4.  Fix a long-standing bug in which a read of a few bytes past the end of a memory-mapped segment might occur when accessing a craftily corrupted database using [memory-mapped database](pragma.md#pragma_mmap_size).
5.  Fix a long-standing bug in which a NULL pointer dereference might occur in the [bytecode engine](opcode.md) due to incorrect bytecode being generated for a class of SQL statements that are deliberately designed to stress the query planner but which are otherwise pointless.
    **Hashes:**
6.  SQLITE_SOURCE_ID: 2024-01-30 16:01:20 e876e51a0ed5c5b3126f52e532044363a014bc594cfefa87ffb5b82257cc467a
7.  SHA3-256 for sqlite3.c: 0474604df9e1b69a5544295dd046aad954749279780d557da80f44b958100295

<span id="version_3_45_0"></span>

### 2024-01-15 (3.45.0)

1.  Added the [SQLITE_RESULT_SUBTYPE](c3ref/c_deterministic.md#sqliteresultsubtype) property for [application-defined SQL functions](appfunc.md). All application defined SQL functions that invokes [sqlite3_result_subtype()](c3ref/result_subtype.md) must be registered with this new property. Failure to do so might cause the call to sqlite3_result_subtype() to behave as a no-op. Compile with [-DSQLITE_STRICT_SUBTYPE=1](compile.md#strict_subtype) to cause an SQL error to be raised if a function that is not [SQLITE_RESULT_SUBTYPE](c3ref/c_deterministic.md#sqliteresultsubtype) tries invokes [sqlite3_result_subtype()](c3ref/result_subtype.md). The use of [-DSQLITE_STRICT_SUBTYPE=1](compile.md#strict_subtype) is a recommended compile-time option for every application that makes use of subtypes.
2.  Enhancements to the [JSON SQL functions](json1.md):
    1.  All JSON functions are rewritten to use a new internal parse tree format called [JSONB](json1.md#jsonbx). The new parse-tree format is serializable and hence can be stored in the database to avoid unnecessary re-parsing whenever the JSON value is used.
    2.  New versions of JSON-generating functions generate binary JSONB instead of JSON text.
    3.  The [json_valid()](json1.md#jvalid) function adds an optional second argument that specifies what it means for the first argument to be "well-formed".
3.  Add the [FTS5 tokendata option](fts5.md#the_tokendata_option) to the [FTS5](fts5.md) virtual table.
4.  The [SQLITE_DIRECT_OVERFLOW_READ](compile.md#direct_overflow_read) optimization is now enabled by default. Disable it at compile-time using -DSQLITE_DIRECT_OVERFLOW_READ=0.
5.  Query planner improvements:
    1.  Do not allow the transitive constraint optimization to trick the query planner into using a range constraint when a better equality constraint is available. ([Forum post 2568d1f6e6](https://sqlite.org/forum/forumpost/2568d1f6e6).)
    2.  The query planner now does a better job of disregarding indexes that [ANALYZE](lang_analyze.md) identifies as low-quality. ([Forum post 6f0958b03b](https://sqlite.org/forum/forumpost/6f0958b03b).)
6.  Increase the default value for [SQLITE_MAX_PAGE_COUNT](limits.md#max_page_count) from 1073741824 to 4294967294.
7.  Enhancements to the [CLI](cli.md):
    1.  Improvements to the display of UTF-8 content on Windows
    2.  Automatically detect playback of ".dump" scripts and make appropriate changes to settings such as ".dbconfig defensive off" and ".dbconfig dqs_dll on".

    **Hashes:**
8.  SQLITE_SOURCE_ID: 2024-01-15 17:01:13 1066602b2b1976fe58b5150777cced894af17c803e068f5918390d6915b46e1d
9.  SHA3-256 for sqlite3.c: f56d8e5e8c61d87b957f1cc60b3042c134d7bc0ca3aba002e6999e8f0af310a3

<span id="version_3_44_2"></span>

### 2023-11-24 (3.44.2)

1.  Fix a mistake in the [CLI](cli.md) that was introduced by the fix (item 15 above) in 3.44.1.
2.  Fix a problem in FTS5 that was discovered during internal fuzz testing only minutes after the 3.44.1 release was tagged.
3.  Fix incomplete assert() statements that the fuzzer discovered the day after the previous release.
4.  Fix a couple of harmless compiler warnings that appeared in debug builds with GCC 16.
    **Hashes:**
5.  SQLITE_SOURCE_ID: 2023-11-24 11:41:44 ebead0e7230cd33bcec9f95d2183069565b9e709bf745c9b5db65cc0cbf92c0f
6.  SHA3-256 for sqlite3.c: bd70b012e2d1b3efa132d905224cd0ab476a69b892f8c6b21135756ec7ffbb13

<span id="version_3_44_1"></span>

### 2023-11-22 (3.44.1)

1.  Change the [CLI](cli.md) so that it uses UTF-16 for console I/O on Windows. This enables proper display of unicode text on old Windows7 machines.
2.  Other obscure bug fixes.
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2023-11-22 14:18:12 d295f48e8f367b066b881780c98bdf980a1d550397d5ba0b0e49842c95b3e8b4
4.  SHA3-256 for sqlite3.c: e359dc502a73f3a8ad8e976a51231134d25cb93ad557a724dd92fe0c5897113a

<span id="version_3_44_0"></span>

### 2023-11-01 (3.44.0)

1.  [Aggregate functions](lang_aggfunc.md) can now include an ORDER BY clause after their last parameter. The arguments to the function are processed in the order specified. This can be important for functions like [string_agg()](lang_aggfunc.md#group_concat) and [json_group_array()](json1.md#jgrouparray).
2.  Add support for the [concat()](lang_corefunc.md#concat) and [concat_ws()](lang_corefunc.md#concat_ws) scalar SQL functions, compatible with PostgreSQL, SQLServer, and MySQL.
3.  Add support for the [string_agg()](lang_aggfunc.md#group_concat) aggregate SQL function, compatible with PostgreSQL and SQLServer.
4.  New conversion letters on the [strftime() SQL function](lang_datefunc.md#strftm): %e %F %I %k %l %p %P %R %T %u
5.  Add new C-language APIs: [sqlite3_get_clientdata()](c3ref/get_clientdata.md) and [sqlite3_set_clientdata()](c3ref/get_clientdata.md).
6.  Many errors associated with CREATE TABLE are now raised when the CREATE TABLE statement itself is run, rather than being deferred until the first time the table is actually used.
7.  The [PRAGMA integrity_check](pragma.md#pragma_integrity_check) command now verifies the consistency of the content in various built-in [virtual tables](vtab.md) using the new [xIntegrity method](vtab.md#xintegrity). This works for the [FTS3](fts3.md), [FTS4](fts3.md#fts4), [FTS5](fts5.md), [RTREE](rtree.md), and [GEOPOLY](geopoly.md) extensions.
8.  The [SQLITE_DBCONFIG_DEFENSIVE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdefensive) setting now prevents [PRAGMA writable_schema](pragma.md#pragma_writable_schema) from being turned on. Previously writable_schema could be turned on, but would not actually allow the schema to be writable. Now it simply cannot be turned on.
9.  Tag the built-in [FTS3](fts3.md), [FTS4](fts3.md#fts4), [FTS5](fts5.md), [RTREE](rtree.md), and [GEOPOLY](geopoly.md) virtual tables as [SQLITE_VTAB_INNOCUOUS](c3ref/c_vtab_constraint_support.md#sqlitevtabinnocuous) so that they can be used inside of triggers in high-security deployments.
10. The [PRAGMA case_sensitive_like](pragma.md#pragma_case_sensitive_like) statement is deprecated, as its use when the schema contains LIKE operators can lead to reports of database corruption by [PRAGMA integrity_check](pragma.md#pragma_integrity_check).
11. [SQLITE_USE_SEH](compile.md#use_seh) (Structured Exception Handling) is now enabled by default whenever SQLite is built using the Microsoft C compiler. It can be disabled using -D[SQLITE_OMIT_SEH](compile.md#omit_seh).
12. Query planner optimizations:
    1.  In partial index scans, if the WHERE clause implies a constant value for a table column, replace occurrences of that table column with the constant. This increases the likelihood of the partial index being a covering index.
    2.  Disable the view-scan optimization (added in [version 3.40.0](#version_3_40_0) - item 3d) as it was causing multiple performance regressions. In its place, reduce the estimated row count for DISTINCT subqueries by a factor of 8.
13. SQLite now performs run-time detection of whether or not the underlying hardware supports "long double" with precision greater than "double" and uses appropriate floating-point routines depending on what it discovered.
14. The [CLI](cli.md) for Windows now defaults to using UTF-8 for both input and output on platforms that support it. The --no-utf8 option is available to disable UTF8 support.
    **Hashes:**
15. SQLITE_SOURCE_ID: 2023-11-01 11:23:50 17129ba1ff7f0daf37100ee82d507aef7827cf38de1866e2633096ae6ad8130
16. SHA3-256 for sqlite3.c: d9e6530096136067644b1cb2057b3b0fa51070df99ec61971f73c9ba6aa9a36e

<span id="version_3_43_2"></span>

### 2023-10-10 (3.43.2)

1.  Fix a couple of obscure UAF errors and an obscure memory leak.
2.  Omit the use of the sprintf() function from the standard library in the [CLI](cli.md), as this now generates warnings on some platforms.
3.  Avoid conversion of a double into unsigned long long integer, as some platforms do not do such conversions correctly.
    **Hashes:**
4.  SQLITE_SOURCE_ID: 2023-10-10 12:14:04 4310099cce5a487035fa535dd3002c59ac7f1d1bec68d7cf317fd3e769484790
5.  SHA3-256 for sqlite3.c: e17a3dc69330bd109256fb5a6e2b3ce8fbec48892a800389eb7c0f8856703161

<span id="version_3_43_1"></span>

### 2023-09-11 (3.43.1)

1.  Fix a regression in the way that the [sum()](lang_aggfunc.md#sumunc), [avg()](lang_aggfunc.md#avg), and [total()](lang_aggfunc.md#sumunc) aggregate functions handle infinities.
2.  Fix a bug in the [json_array_length()](json1.md#jarraylen) function that occurs when the argument comes directly from [json_remove()](json1.md#jrm).
3.  Fix the omit-unused-subquery-columns optimization (introduced in in version 3.42.0) so that it works correctly if the subquery is a compound where one arm is DISTINCT and the other is not.
4.  Other minor fixes.
    **Hashes:**
5.  SQLITE_SOURCE_ID: 2023-09-11 12:01:27 2d3a40c05c49e1a49264912b1a05bc2143ac0e7c3df588276ce80a4cbc9bd1b0
6.  SHA3-256 for sqlite3.c: 391af0a4755e31ae8b29776a4a060b678823ffe4c4db558567567c688a578589

<span id="version_3_43_0"></span>

### 2023-08-24 (3.43.0)

1.  Add support for [Contentless-Delete FTS5 Indexes](fts5.md#clssdeltab). This is a variety of [FTS5](fts5.md) full-text search index that omits storing the content that is being indexed while also allowing records to be deleted.
2.  Enhancements to the [date and time functions](lang_datefunc.md):
    1.  Added new [time shift modifiers](lang_datefunc.md#tmshf) of the form `±YYYY-MM-DD HH:MM:SS.SSS`.
    2.  Added the [timediff() SQL function](lang_datefunc.md#tmdif).
3.  Added the [octet_length(X)](lang_corefunc.md#octet_length) SQL function.
4.  Added the [sqlite3_stmt_explain()](c3ref/stmt_explain.md) API.
5.  Query planner enhancements:
    1.  Generalize the LEFT JOIN strength reduction optimization so that it works for RIGHT and FULL JOINs as well. Rename it to [OUTER JOIN strength reduction](optoverview.md#leftjoinreduction).
    2.  Enhance the theorem prover in the [OUTER JOIN strength reduction](optoverview.md#leftjoinreduction) optimization so that it returns fewer false-negatives.
6.  Enhancements to the [decimal extension](floatingpoint.md#decext):
    1.  New function decimal_pow2(N) returns the N-th power of 2 for integer N between -20000 and +20000.
    2.  New function decimal_exp(X) works like decimal(X) except that it returns the result in exponential notation - with a "e+NN" at the end.
    3.  If X is a floating-point value, then the decimal(X) function now does a full expansion of that value into its exact decimal equivalent.
7.  Performance enhancements to [JSON processing](json1.md) results in a 2x performance improvement for some kinds of processing on large JSON strings.
8.  New makefile target "verify-source" checks to ensure that there are no unintentional changes in the source tree. (Works for [canonical source code](amalg-v-canon.md#canon) only - not for [precompiled amalgamation tarballs](amalgamation.md#amalgtarball).)
9.  Added the [SQLITE_USE_SEH](compile.md#use_seh) compile-time option that enables Structured Exception Handling on Windows while working with the memory-mapped [shm file](walformat.md#shm) that is part of [WAL mode](wal.md) processing. This option is enabled by default when building on Windows using Makefile.msc.
10. The [VFS](vfs.md) for unix now assumes that the nanosleep() system call is available unless compiled with -DHAVE_NANOSLEEP=0.
    **Hashes:**
11. SQLITE_SOURCE_ID: 2023-08-24 12:36:59 0f80b798b3f4b81a7bb4233c58294edd0f1156f36b6ecf5ab8e83631d468778c
12. SHA3-256 for sqlite3.c: a6fc5379891d77b69a7d324cd24a437307af66cfdc3fef5dfceec3c82c8d4078

<span id="version_3_42_0"></span>

### 2023-05-16 (3.42.0)

1.  Add the [FTS5 secure-delete command](fts5.md#the_secure_delete_configuration_option). This option causes all forensic traces to be removed from the FTS5 inverted index when content is deleted.
2.  Enhance the [JSON SQL functions](json1.md) to support [JSON5 extensions](json1.md#json5).
3.  The [SQLITE_CONFIG_LOG](c3ref/c_config_covering_index_scan.md#sqliteconfiglog) and [SQLITE_CONFIG_PCACHE_HDRSZ](c3ref/c_config_covering_index_scan.md#sqliteconfigpcachehdrsz) calls to [sqlite3_config()](c3ref/config.md) are now allowed to occur *after* [sqlite3_initialize()](c3ref/initialize.md).
4.  New [sqlite3_db_config()](c3ref/db_config.md) options: [SQLITE_DBCONFIG_STMT_SCANSTATUS](c3ref/c_dbconfig_defensive.md#sqlitedbconfigstmtscanstatus) and [SQLITE_DBCONFIG_REVERSE_SCANORDER](c3ref/c_dbconfig_defensive.md#sqlitedbconfigreversescanorder).
5.  Query planner improvements:
    1.  Enable the "count-of-view" optimization by default.
    2.  Avoid computing unused columns in subqueries.
    3.  Improvements to the [WHERE-clause push-down optimization](optoverview.md#pushdown).
6.  Enhancements to the [CLI](cli.md):
    1.  Add the --unsafe-testing command-line option. Without this option, some dot-commands (ex: ".testctrl") are now disabled because those commands that are intended for testing only and can cause malfunctions if misused.
    2.  Allow commands ".log on" and ".log off", even in --safe mode.
    3.  "--" as a command-line argument means all subsequent arguments that start with "-" are interpreted as normal non-option argument.
    4.  Magic parameters ":inf" and ":nan" bind to floating point literals Infinity and NaN, respectively.
    5.  The --utf8 command-line option omits all translation to or from MBCS on the Windows console for interactive sessions, and sets the console code page for UTF-8 I/O during such sessions. The --utf8 option is a no-op on all other platforms.
7.  Add the ability for [application-defined SQL functions](appfunc.md) to have the same name as join keywords: CROSS, FULL, INNER, LEFT, NATURAL, OUTER, or RIGHT.
8.  Enhancements to [PRAGMA integrity_check](pragma.md#pragma_integrity_check):
    1.  Detect and raise an error when a NaN value is stored in a NOT NULL column.
    2.  Improved error message output identifies the root page of a b-tree when an error is found within a b-tree.
9.  Allow the [session extension](sessionintro.md) to be configured to capture changes from tables that lack an explicit ROWID.
10. Added the [subsecond modifier](lang_datefunc.md#subsec) to the [date and time functions](lang_datefunc.md).
11. Negative values passed into [sqlite3_sleep()](c3ref/sleep.md) are henceforth interpreted as 0.
12. The maximum recursion depth for JSON arrays and objects is lowered from 2000 to 1000.
13. Extended the [built-in printf()](printf.md) function so the [comma option](printf.md#comma) now works with floating-point conversions in addition to integer conversions.
14. Miscellaneous bug fixes and performance optimizations
    **Hashes:**
15. SQLITE_SOURCE_ID: 2023-05-16 12:36:15 831d0fb2836b71c9bc51067c49fee4b8f18047814f2ff22d817d25195cf350b0
16. SHA3-256 for sqlite3.c: 6aa3fadf000000625353bbaa1e83af114c40c240a0aa5a2c1c2aabcfc28d4f92

<span id="version_3_41_2"></span>

### 2023-03-22 (3.41.2)

1.  Multiple fixes for reads past the end of memory buffers (NB: *reads* not *writes*) in the following circumstances:
    1.  When processing a corrupt database file using the non-standard [SQLITE_ENABLE_STAT4](compile.md#enable_stat4) compile-time option.
    2.  In the [CLI](cli.md) when the [sqlite3_error_offset()](c3ref/errcode.md) routine returns an out-of-range value (see also the fix to sqlite3_error_offset() below).
    3.  In the [recovery extension](recovery.md).
    4.  In [FTS3](fts3.md) when processing a corrupt database file.
2.  Fix the [sqlite3_error_offset()](c3ref/errcode.md) so that it does not return out-of-range values when reporting errors associated with [generated columns](gencol.md).
3.  Multiple fixes in the query optimizer for problems that cause incorrect results for bizarre, fuzzer-generated queries.
4.  Increase the size of the reference counter in the page cache object to 64 bits to ensure that the counter never overflows.
5.  Fix a performance regression caused by a bug fix in patch release 3.41.1.
6.  Fix a few incorrect assert() statements.
    **Hashes:**
7.  SQLITE_SOURCE_ID: 2023-03-22 11:56:21 0d1fc92f94cb6b76bffe3ec34d69cffde2924203304e8ffc4155597af0c191da
8.  SHA3-256 for sqlite3.c: c83f68b7aac1e7d3ed0fcdb9857742f024449e1300bfb3375131a6180b36cf7c

<span id="version_3_41_1"></span>

### 2023-03-10 (3.41.1)

1.  Provide compile-time options -DHAVE_LOG2=0 and -DHAVE_LOG10=0 to enable SQLite to be compiled on systems that omit the standard library functions log2() and log10(), repectively.
2.  Ensure that the datatype for column t1.x in "`CREATE TABLE t1 AS SELECT CAST(7 AS INT) AS x;`" continues to be INT and is not NUM, for historical compatibility.
3.  Enhance [PRAGMA integrity_check](pragma.md#pragma_integrity_check) to detect when extra bytes appear at the end of an index record.
4.  Fix various obscure bugs reported by the user community. See the [timeline of changes](https://sqlite.org/src/timeline?from=version-3.41.0&to=version-3.41.1) for details.
    **Hashes:**
5.  SQLITE_SOURCE_ID: 2023-03-10 12:13:52 20399f3eda5ec249d147ba9e48da6e87f969d7966a9a896764ca437ff7e737ff
6.  SHA3-256 for sqlite3.c: d0d9db8425570f4a57def04fb8f4ac84f5c3e4e71d3d4d10472e3639c5fdf09f

<span id="version_3_41_0"></span>

### 2023-02-21 (3.41.0)

1.  Query planner improvements:
    1.  Make use of [indexed expressions](expridx.md) within an aggregate query that includes a GROUP BY clause.
    2.  The query planner has improved awareness of when an index is a [covering index](queryplanner.md#covidx) and adjusts predicted runtimes accordingly.
    3.  The query planner is more aggressive about using [co-routines](optoverview.md#coroutines) rather than materializing subqueries and views.
    4.  Queries against the built-in table-valued functions [json_tree()](json1.md#jtree) and [json_each()](json1.md#jeach) will now usually treat "ORDER BY rowid" as a no-op.
    5.  Enhance the ability of the query planner to use [indexed expressions](expridx.md) even if the expression has been modified by the [constant-propagation optimization](optoverview.md#constprop). (See [forum thread 0a539c7](https://sqlite.org/forum/forumpost/0a539c76db3b9e29).)
2.  Add the built-in [unhex()](lang_corefunc.md#unhex) SQL function.
3.  Add the base64 and base85 application-defined functions as an extension and include that extension in the [CLI](cli.md).
4.  Add the [sqlite3_stmt_scanstatus_v2()](c3ref/stmt_scanstatus.md) interface. (This interface is only available if SQLite is compiled using [SQLITE_ENABLE_STMT_SCANSTATUS](compile.md#enable_stmt_scanstatus).)
5.  In-memory databases created using [sqlite3_deserialize()](c3ref/deserialize.md) now report their filename as an empty string, not as 'x'.
6.  Changes to the [CLI](cli.md):
    1.  Add the new base64() and base85() SQL functions
    2.  Enhanced [EXPLAIN QUERY PLAN](eqp.md) output using the new [sqlite3_stmt_scanstatus_v2()](c3ref/stmt_scanstatus.md) interface when compiled using [SQLITE_ENABLE_STMT_SCANSTATUS](compile.md#enable_stmt_scanstatus).
    3.  The "`.scanstats est`" command provides query planner estimates in profiles.
    4.  The continuation prompt indicates if the input is currently inside of a string literal, identifier literal, comment, trigger definition, etc.
    5.  Enhance the --safe command-line option to disallow dangerous SQL functions.
    6.  The [double-quoted string misfeature](quirks.md#dblquote) is now disabled by default for CLI builds. Legacy use cases can reenable the misfeature at run-time using the "`.dbconfig dqs_dml on`" and "`.dbconfig dqs_ddl on`" commands.
7.  Enhance the [PRAGMA integrity_check](pragma.md#pragma_integrity_check) command so that it detects when text strings in a table are equivalent to but not byte-for-byte identical to the same strings in the index.
8.  Enhance the [carray table-valued function](carray.md) so that it is able to bind an array of BLOB objects.
9.  Added the [sqlite3_is_interrupted()](c3ref/interrupt.md) interface.
10. Long-running calls to [sqlite3_prepare()](c3ref/prepare.md) and similar now invoke the [progress handler callback](c3ref/progress_handler.md) and react to [sqlite3_interrupt()](c3ref/interrupt.md).
11. The [sqlite3_vtab_in_first()](c3ref/vtab_in_first.md) and [sqlite3_vtab_in_next()](c3ref/vtab_in_first.md) functions are enhanced so that they reliably detect if they are invoked on a parameter that was not selected for multi-value IN processing using [sqlite3_vtab_in()](c3ref/vtab_in.md). They return SQLITE_ERROR instead of SQLITE_MISUSE in this case.
12. The parser now ignores excess parentheses around a subquery on the right-hand side of an IN operator, so that SQLite now works the same as PostgreSQL in this regard. Formerly, SQLite treated the subquery as an expression with an implied "LIMIT 1".
13. Added the [SQLITE_FCNTL_RESET_CACHE](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlresetcache) option to the [sqlite3_file_control()](c3ref/file_control.md) API.
14. Makefile improvements:
    1.  The new makefile target "sqlite3r.c" builds an [amalgamation](amalgamation.md) that includes the [recovery extension](recovery.md).
    2.  New makefile targets "devtest" and "releasetest" for running a quick developmental test prior to doing a check-in and for doing a full release test, respectively.
15. Miscellaneous performance enhancements.
    **Hashes:**
16. SQLITE_SOURCE_ID: 2023-02-21 18:09:37 05941c2a04037fc3ed2ffae11f5d2260706f89431f463518740f72ada350866d
17. SHA3-256 for sqlite3.c: 02bd9e678460946810801565667fdb8f0c29c78e51240512d2e5bb3dbdee7464

<span id="version_3_40_1"></span>

### 2022-12-28 (3.40.1)

1.  Fix the [--safe command-line option](cli.md#safemode) to the [CLI](cli.md) such that it correctly disallows the use of SQL functions like writefile() that can cause harmful side-effects.
2.  Fix a potential infinite loop in the [memsys5](malloc.md#memsys5) alternative memory allocator. This bug was introduced by a performance optimization in version 3.39.0.
3.  Various other obscure fixes.
    **Hashes:**
4.  SQLITE_SOURCE_ID: 2022-12-28 14:03:47 df5c253c0b3dd24916e4ec7cf77d3db5294cc9fd45ae7b9c5e82ad8197f38a24
5.  SHA3-256 for sqlite3.c: 4d6800e9032ff349376fe612e422b49ba5eb4e378fac0b3e405235d09dd366ab

<span id="version_3_40_0"></span>

### 2022-11-16 (3.40.0)

1.  Add support for compiling [SQLite to WASM](https://sqlite.org/wasm) and running it in web browsers. NB: The WASM build and its interfaces are considered "beta" and are subject to minor changes if the need arises. We anticipate finalizing the interface for the next release.
2.  Add the [recovery extension](recovery.md) that might be able to recover some content from a corrupt database file.
3.  Query planner enhancements:
    1.  Recognize [covering indexes](queryplanner.md#covidx) on tables with more than 63 columns where columns beyond the 63rd column are used in the query and/or are referenced by the index.
    2.  Extract the values of expressions contained within [expression indexes](expridx.md) where practical, rather than recomputing the expression.
    3.  The NOT NULL and IS NULL operators (and their equivalents) avoid loading the content of large strings and BLOB values from disk.
    4.  Avoid materializing a view on which a full scan is performed exactly once. Use and discard the rows of the view as they are computed.
    5.  Allow flattening of a subquery that is the right-hand operand of a LEFT JOIN in an aggregate query.
4.  A new typedef named [sqlite3_filename](c3ref/filename.md) is added and used to represent the name of a database file. Various interfaces are modified to use the new typedef instead of "char\*". This interface change should be fully backwards compatible, though it might cause (harmless) compiler warnings when rebuilding some legacy applications.
5.  Add the [sqlite3_value_encoding()](c3ref/value_encoding.md) interface.
6.  Security enhancement: [SQLITE_DBCONFIG_DEFENSIVE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdefensive) is augmented to prohibit changing the [schema_version](pragma.md#pragma_schema_version). The schema_version becomes read-only in defensive mode.
7.  Enhancements to the [PRAGMA integrity_check](pragma.md#pragma_integrity_check) statement:
    1.  Columns in non-STRICT tables with TEXT affinity should not contain numeric values.
    2.  Columns in non-STRICT tables with NUMERIC affinity should not contain TEXT values that could be converted into numbers.
    3.  Verify that the rows of a [WITHOUT ROWID](withoutrowid.md) table are in the correct order.
8.  Enhance the [VACUUM INTO](lang_vacuum.md#vacuuminto) statement so that it honors the [PRAGMA synchronous](pragma.md#pragma_synchronous) setting.
9.  Enhance the [sqlite3_strglob()](c3ref/strglob.md) and [sqlite3_strlike()](c3ref/strlike.md) APIs so that they are able to accept NULL pointers for their string parameters and still generate a sensible result.
10. Provide the new [SQLITE_MAX_ALLOCATION_SIZE](compile.md#max_allocation_size) compile-time option for limiting the size of memory allocations.
11. Change the algorithm used by SQLite's built-in pseudo-random number generator (PRNG) from RC4 to Chacha20.
12. Allow two or more indexes to have the same name as long as they are all in separate schemas.
13. Miscellaneous performance optimizations result in about 1% fewer CPU cycles used on typical workloads.
    **Hashes:**
14. SQLITE_SOURCE_ID: 2022-11-16 12:10:08 89c459e766ea7e9165d0beeb124708b955a4950d0f4792f457465d71b158d318
15. SHA3-256 for sqlite3.c: ab8da6bc754642989e67d581f26683dc705b068cea671970f0a7d32cfacbad19

<span id="version_3_39_4"></span>

### 2022-09-29 (3.39.4)

1.  Fix the build on Windows so that it works with -DSQLITE_OMIT_AUTOINIT
2.  Fix a long-standing problem in the btree balancer that might, in rare cases, cause database corruption if the application uses an [application-defined page cache](c3ref/pcache_methods2.md).
3.  Enhance [SQLITE_DBCONFIG_DEFENSIVE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdefensive) so that it disallows [CREATE TRIGGER](lang_createtrigger.md) statements if one or more of the statements in the body of the trigger write into [shadow tables](vtab.md#xshadowname).
4.  Fix a possible integer overflow in the size computation for a memory allocation in FTS3.
5.  Fix a misuse of the [sqlite3_set_auxdata()](c3ref/get_auxdata.md) interface in the [ICU Extension](https://sqlite.org/src/dir/ext/icu).
    **Hashes:**
6.  SQLITE_SOURCE_ID: 2022-09-29 15:55:41 a29f9949895322123f7c38fbe94c649a9d6e6c9cd0c3b41c96d694552f26b309
7.  SHA3-256 for sqlite3.c: f65082298127e2ddae6539beb94f5204b591df64ba2c7da83c7d0faffd6959d8

<span id="version_3_39_3"></span>

### 2022-09-05 (3.39.3)

1.  Use a statement journal on DML statement affecting two or more database rows if the statement makes use of a SQL functions that might abort. See [forum thread 9b9e4716c0d7bbd1](https://sqlite.org/forum/forumpost/9b9e4716c0d7bbd1).
2.  Use a mutex to protect the [PRAGMA temp_store_directory](pragma.md#pragma_temp_store_directory) and [PRAGMA data_store_directory](pragma.md#pragma_data_store_directory) statements, even though they are deprecated and documented as not being threadsafe. See [forum post 719a11e1314d1c70](https://sqlite.org/forum/forumpost/719a11e1314d1c70).
3.  Other bug and warning fixes. See the [timeline](https://sqlite.org/src/timeline?p=version-3.39.3&bt=version-3.39.2) for details.
    **Hashes:**
4.  SQLITE_SOURCE_ID: 2022-09-05 11:02:23 4635f4a69c8c2a8df242b384a992aea71224e39a2ccab42d8c0b0602f1e826e8
5.  SHA3-256 for sqlite3.c: 2fc273cf8032b601c9e06207efa0ae80eb73d5a1d283eb91096c815fa9640257

<span id="version_3_39_2"></span>

### 2022-07-21 (3.39.2)

1.  Fix a performance regression in the query planner associated with rearranging the order of FROM clause terms in the presences of a LEFT JOIN.
2.  Apply fixes for CVE-2022-35737, Chromium bugs 1343348 and 1345947, [forum post 3607259d3c](https://sqlite.org/forum/forumpost/3607259d3c), and other minor problems discovered by internal testing.
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2022-07-21 15:24:47 698edb77537b67c41adc68f9b892db56bcf9a55e00371a61420f3ddd668e6603
4.  SHA3-256 for sqlite3.c: bffbaafa94706f0ed234f183af3eb46e6485e7e2c75983173ded76e0da805f11

<span id="version_3_39_1"></span>

### 2022-07-13 (3.39.1)

1.  Fix an incorrect result from a query that uses a view that contains a compound SELECT in which only one arm contains a RIGHT JOIN and where the view is not the first FROM clause term of the query that contains the view. [forum post 174afeae5734d42d](https://sqlite.org/forum/forumpost/174afeae5734d42d).
2.  Fix some harmless compiler warnings.
3.  Fix a long-standing problem with [ALTER TABLE RENAME](lang_altertable.md#altertabrename) that can only arise if the [sqlite3_limit](c3ref/limit.md)([SQLITE_LIMIT_SQL_LENGTH](c3ref/c_limit_attached.md#sqlitelimitsqllength)) is set to a very small value.
4.  Fix a long-standing problem in [FTS3](fts3.md) that can only arise when compiled with the [SQLITE_ENABLE_FTS3_PARENTHESIS](compile.md#enable_fts3_parenthesis) compile-time option.
5.  Fix the build so that is works when the [SQLITE_DEBUG](compile.md#debug) and [SQLITE_OMIT_WINDOWFUNC](compile.md#omit_windowfunc) compile-time options are both provided at the same time.
6.  Fix the initial-prefix optimization for the [REGEXP](lang_expr.md#regexp) extension so that it works correctly even if the prefix contains characters that require a 3-byte UTF8 encoding.
7.  Enhance the [sqlite_stmt](stmt.md) virtual table so that it buffers all of its output.
    **Hashes:**
8.  SQLITE_SOURCE_ID: 2022-07-13 19:41:41 7c16541a0efb3985578181171c9f2bb3fdc4bad6a2ec85c6e31ab96f3eff201f
9.  SHA3-256 for sqlite3.c: 6d13fcf1c31133da541d1eb8a83552d746f39b81a0657bd4077fed0221749511

<span id="version_3_39_0"></span>

### 2022-06-25 (3.39.0)

1.  Add (long overdue) support for [RIGHT and FULL OUTER JOIN](lang_select.md#rjoin).
2.  Add new binary comparison operators [IS NOT DISTINCT FROM](lang_expr.md#isdf) and [IS DISTINCT FROM](lang_expr.md#isdf) that are equivalent to IS and IS NOT, respective, for compatibility with PostgreSQL and SQL standards.
3.  Add a new return code (value "3") from the [sqlite3_vtab_distinct()](c3ref/vtab_distinct.md) interface that indicates a query that has both DISTINCT and ORDER BY clauses.
4.  Added the [sqlite3_db_name()](c3ref/db_name.md) interface.
5.  The unix os interface resolves all symbolic links in database filenames to create a canonical name for the database before the file is opened. If the [SQLITE_OPEN_NOFOLLOW](c3ref/c_open_autoproxy.md) flag is used with [sqlite3_open_v2()](c3ref/open.md) or similar, the open will fail if any element of the path is a symbolic link.
6.  Defer materializing views until the materialization is actually needed, thus avoiding unnecessary work if the materialization turns out to never be used.
7.  The [HAVING clause](lang_select.md#resultset) of a [SELECT statement](lang_select.md) is now allowed on any aggregate query, even queries that do not have a [GROUP BY clause](lang_select.md#resultset).
8.  Many [microoptimizations](cpu.md#microopt) collectively reduce CPU cycles by about 2.3%.
    **Hashes:**
9.  SQLITE_SOURCE_ID: 2022-06-25 14:57:57 14e166f40dbfa6e055543f8301525f2ca2e96a02a57269818b9e69e162e98918
10. SHA3-256 for sqlite3.c: d9c439cacad5e4992d0d25989cfd27a4c4f59a3183c97873bc03f0ad1aa78b7a

<span id="version_3_38_5"></span>

### 2022-05-06 (3.38.5)

1.  Fix [a blunder](news.md#2022_05_06) in the [CLI](cli.md) of the 3.38.4 release.
    **Hashes:**
2.  SQLITE_SOURCE_ID: 2022-05-06 15:25:27 78d9c993d404cdfaa7fdd2973fa1052e3da9f66215cff9c5540ebe55c407d9fe
3.  SHA3-256 for sqlite3.c: b05ef42ed234009b4b3dfb36c5f5ccf6d728da80f25ee560291269cf6cfe635f

<span id="version_3_38_4"></span>

### 2022-05-04 (3.38.4)

1.  Fix a byte-code problem in the Bloom filter pull-down optimization added by release 3.38.0 in which an error in the byte code causes the byte code engine to enter an infinite loop when the pull-down optimization encounters a NULL key. [Forum thread 2482b32700384a0f](https://sqlite.org/forum/forumpost/2482b32700384a0f).
2.  Other minor patches. See the [timeline](https://sqlite.org/src/timeline?p=branch-3.38&bt=version-3.38.3) for details.
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2022-05-04 15:45:55 d402f49871152670a62f4f28cacb15d814f2c1644e9347ad7d258e562978e45e
4.  SHA3-256 for sqlite3.c: e6a50effb021858c200e885664611ed3c5e949413ff2dca452ac7ee336b9de1d

<span id="version_3_38_3"></span>

### 2022-04-27 (3.38.3)

1.  Fix a case of the query planner be overly aggressive with optimizing automatic-index and Bloom-filter construction, using inappropriate ON clause terms to restrict the size of the automatic-index or Bloom filter, and resulting in missing rows in the output. [Forum thread 0d3200f4f3bcd3a3](https://sqlite.org/forum/forumpost/0d3200f4f3bcd3a3).
2.  Other minor patches. See the [timeline](https://sqlite.org/src/timeline?p=version-3.38.3&bt=version-3.38.2) for details.
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2022-04-27 12:03:15 9547e2c38a1c6f751a77d4d796894dec4dc5d8f5d79b1cd39e1ffc50df7b3be4
4.  SHA3-256 for sqlite3.c: d4d66feffad66ea82073fbb97ae9c84e3615887ebc5168226ccee28d82424517

<span id="version_3_38_2"></span>

### 2022-03-26 (3.38.2)

1.  Fix a user-discovered problem with the new Bloom filter optimization that might cause an incorrect answer when doing a LEFT JOIN with a WHERE clause constraint that says that one of the columns on the right table of the LEFT JOIN is NULL. See [forum thread 031e262a89b6a9d2](https://sqlite.org/forum/forumpost/031e262a89b6a9d2).
2.  Other minor patches. See the [timeline](https://sqlite.org/src/timeline?p=version-3.38.2&bt=version-3.38.1) for details.
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2022-03-26 13:51:10 d33c709cc0af66bc5b6dc6216eba9f1f0b40960b9ae83694c986fbf4c1d6f08f
4.  SHA3-256 for sqlite3.c: 0fbac6b6999f894184899431fb77b9792324c61246b2a010d736694ccaa6d613

<span id="version_3_38_1"></span>

### 2022-03-12 (3.38.1)

1.  Fix problems with the new Bloom filter optimization that might cause some obscure queries to get an incorrect answer.
2.  Fix the [localtime modifier](lang_datefunc.md#localtime) of the [date and time functions](lang_datefunc.md) so that it preserves fractional seconds.
3.  Fix the [sqlite_offset SQL function](lang_corefunc.md#sqlite_offset) so that it works correctly even in corner cases such as when the argument is a virtual column or the column of a view.
4.  Fix [row value IN operator](rowvalue.md#rvinop) constraints on [virtual tables](vtab.md) so that they work correctly even if the virtual table implementation relies on bytecode to filter rows that do not satisfy the constraint.
5.  Other minor fixes to assert() statements, test cases, and documentation. See the [source code timeline](https://sqlite.org/src/timeline?p=version-3.38.1&bt=version-3.38.0) for details.
    **Hashes:**
6.  SQLITE_SOURCE_ID: 2022-03-12 13:37:29 38c210fdd258658321c85ec9c01a072fda3ada94540e3239d29b34dc547a8cbc
7.  SHA3-256 for sqlite3.c: 262ba071e960a8a0a6ce39307ae30244a2b0dc9fe1c4c09d0e1070d4353cd92c

<span id="version_3_38_0"></span>

### 2022-02-22 (3.38.0)

1.  Added [the -\> and -\>\> operators](json1.md#jptr) for easier processing of JSON. The new operators are compatible with MySQL and PostgreSQL.
2.  The JSON functions are now built-ins. It is no longer necessary to use the [-DSQLITE_ENABLE_JSON1](compile.md#enable_json1) compile-time option to enable JSON support. JSON is on by default. Disable the JSON interface using the new [-DSQLITE_OMIT_JSON](compile.md#omit_json) compile-time option.
3.  Enhancements to [date and time functions](lang_datefunc.md):
    1.  Added the [unixepoch() function](lang_datefunc.md#uepch).
    2.  Added the [auto modifier](lang_datefunc.md#automod) and the [julianday modifier](lang_datefunc.md#jdmod).
4.  Rename the [printf() SQL function](lang_corefunc.md#printf) to [format()](lang_corefunc.md#format) for better compatibility. The original printf() name is retained as an alias for backwards compatibility.
5.  Added the [sqlite3_error_offset()](c3ref/errcode.md) interface, which can sometimes help to localize an SQL error to a specific character in the input SQL text, so that applications can provide better error messages.
6.  Enhanced the interface to [virtual tables](vtab.md) as follows:
    1.  Added the [sqlite3_vtab_distinct()](c3ref/vtab_distinct.md) interface.
    2.  Added the [sqlite3_vtab_rhs_value()](c3ref/vtab_rhs_value.md) interface.
    3.  Added new operator types [SQLITE_INDEX_CONSTRAINT_LIMIT](c3ref/c_index_constraint_eq.md) and [SQLITE_INDEX_CONSTRAINT_OFFSET](c3ref/c_index_constraint_eq.md).
    4.  Added the [sqlite3_vtab_in()](c3ref/vtab_in.md) interface (and related) to enable a virtual table to process [IN operator](lang_expr.md#in_op) constraints all at once, rather than processing each value of the right-hand side of the IN operator separately.
7.  [CLI](cli.md) enhancements:
    1.  [Columnar output modes](climode.md#clmnr) are enhanced to correctly handle tabs and newlines embedded in text.
    2.  Added options like "--wrap N", "--wordwrap on", and "--quote" to the [columnar output modes](climode.md#clmnr).
    3.  Added the [.mode qbox](climode.md#qbox) alias.
    4.  The [.import command](cli.md#csv) automatically disambiguates column names.
    5.  Use the new [sqlite3_error_offset()](c3ref/errcode.md) interface to provide better error messages.
8.  Query planner enhancements:
    1.  Use a Bloom filter to speed up large analytic queries.
    2.  Use a balanced merge tree to evaluate UNION or UNION ALL compound SELECT statements that have an ORDER BY clause.
9.  The [ALTER TABLE](lang_altertable.md) statement is changed to silently ignores entries in the [sqlite_schema table](schematab.md) that do not parse when [PRAGMA writable_schema=ON](pragma.md#pragma_writable_schema).
    **Hashes:**
10. SQLITE_SOURCE_ID: 2022-02-22 18:58:40 40fa792d359f84c3b9e9d6623743e1a59826274e221df1bde8f47086968a1bab
11. SHA3-256 for sqlite3.c: a69af0a88d59271a2dd3c846a3e93cbd29e7c499864f6c0462a3b4160bee1762

<span id="version_3_37_2"></span>

### 2022-01-06 (3.37.2)

1.  Fix [a bug](https://sqlite.org/forum/forumpost/b03d86f9516cb3a2) introduced in [version 3.35.0](#version_3_35_0) (2021-03-12) that [can cause database corruption](howtocorrupt.md#svptbug) if a [SAVEPOINT](lang_savepoint.md) is rolled back while in [PRAGMA temp_store=MEMORY](pragma.md#pragma_temp_store) mode, and other changes are made, and then the outer transaction commits. [Check-in 73c2b50211d3ae26](https://sqlite.org/src/info/73c2b50211d3ae26)
2.  Fix a long-standing problem with ON DELETE CASCADE and ON UPDATE CASCADE in which a cache of the [bytecode](opcode.md) used to implement the cascading change was not being reset following a local DDL change. [Check-in 5232c9777fe4fb13](https://sqlite.org/src/info/5232c9777fe4fb13).
3.  Other minor fixes that should not impact production builds.
    **Hashes:**
4.  SQLITE_SOURCE_ID: 2022-01-06 13:25:41 872ba256cbf61d9290b571c0e6d82a20c224ca3ad82971edc46b29818d5d17a0
5.  SHA3-256 for sqlite3.c: 1bb01c382295cba85ec4685cedc52a7477cdae71cc37f1ad0f48719a17af1e1e

<span id="version_3_37_1"></span>

### 2021-12-30 (3.37.1)

1.  Fix a bug introduced by the [UPSERT](lang_upsert.md) enhancements of [version 3.35.0](#version_3_35_0) that can cause incorrect byte-code to be generated for some obscure but valid SQL, possibly resulting in a NULL-pointer dereference.
2.  Fix an OOB read that can occur in [FTS5](fts5.md) when reading corrupt database files.
3.  Improved robustness of the --safe option in the [CLI](cli.md).
4.  Other minor fixes to assert() statements and test cases.
    **Hashes:**
5.  SQLITE_SOURCE_ID: 2021-12-30 15:30:28 378629bf2ea546f73eee84063c5358439a12f7300e433f18c9e1bddd948dea62
6.  SHA3-256 for sqlite3.c: 915afb3f29c2d217ea0c283326a9df7d505e6c73b40236f0b33ded91f812d174

<span id="version_3_37_0"></span>

### 2021-11-27 (3.37.0)

1.  [STRICT tables](stricttables.md) provide a prescriptive style of data type management, for developers who prefer that kind of thing.
2.  When adding columns that contain a [CHECK constraint](lang_createtable.md#ckconst) or a [generated column](gencol.md) containing a [NOT NULL constraint](lang_createtable.md#notnullconst), the [ALTER TABLE ADD COLUMN](lang_altertable.md#altertabaddcol) now checks new constraints against preexisting rows in the database and will only proceed if no constraints are violated.
3.  Added the [PRAGMA table_list](pragma.md#pragma_table_list) statement.
4.  [CLI](cli.md) enhancements:
    1.  Add the [.connection](cli.md#dotconn) command, allowing the CLI to keep multiple database connections open at the same time.
    2.  Add the [--safe command-line option](cli.md#safemode) that disables [dot-commands](cli.md#dotcmd) and SQL statements that might cause side-effects that extend beyond the single database file named on the command-line.
    3.  Performance improvements when reading SQL statements that span many lines.
5.  Added the [sqlite3_autovacuum_pages()](c3ref/autovacuum_pages.md) interface.
6.  The [sqlite3_deserialize()](c3ref/deserialize.md) does not and has never worked for the TEMP database. That limitation is now noted in the documentation.
7.  The query planner now omits ORDER BY clauses on subqueries and views if removing those clauses does not change the semantics of the query.
8.  The [generate_series](series.md) table-valued function extension is modified so that the first parameter ("START") is now required. This is done as a way to demonstrate how to write table-valued functions with required parameters. The legacy behavior is available using the -DZERO_ARGUMENT_GENERATE_SERIES compile-time option.
9.  Added new [sqlite3_changes64()](c3ref/changes.md) and [sqlite3_total_changes64()](c3ref/total_changes.md) interfaces.
10. Added the [SQLITE_OPEN_EXRESCODE](c3ref/c_open_autoproxy.md) flag option to [sqlite3_open_v2()](c3ref/open.md).
11. Use less memory to hold the database schema.
    **Hashes:**
12. SQLITE_SOURCE_ID: 2021-11-27 14:13:22 bd41822c7424d393a30e92ff6cb254d25c26769889c1499a18a0b9339f5d6c8a
13. SHA3-256 for sqlite3.c: a202a950ab401cda052e81259e96d6e64ad91faaaaf5690d769f64c2ab962f27

<span id="version_3_36_0"></span>

### 2021-06-18 (3.36.0)

1.  Improvement to the [EXPLAIN QUERY PLAN](eqp.md) output to make it easier to understand.
2.  Byte-order marks at the start of a token are skipped as if they were whitespace.
3.  An error is raised on any attempt to access the [rowid](lang_createtable.md#rowid) of a VIEW or subquery. Formerly, the rowid of a VIEW would be indeterminate and often would be NULL. The -DSQLITE_ALLOW_ROWID_IN_VIEW compile-time option is available to restore the legacy behavior for applications that need it.
4.  The [sqlite3_deserialize()](c3ref/deserialize.md) and [sqlite3_serialize()](c3ref/serialize.md) interfaces are now enabled by default. The -DSQLITE_ENABLE_DESERIALIZE compile-time option is no longer required. Instead, there is a new [-DSQLITE_OMIT_DESERIALIZE](compile.md#omit_deserialize) compile-time option to omit those interfaces.
5.  The "memdb" VFS now allows the same in-memory database to be shared among multiple database connections in the same process as long as the database name begins with "/".
6.  Back out the EXISTS-to-IN optimization (item 8b in the [SQLite 3.35.0 change log](#version_3_35_0)) as it was found to slow down queries more often than speed them up.
7.  Improve the [constant-propagation optimization](optoverview.md#constprop) so that it works on non-join queries.
8.  The [REGEXP extension](https://sqlite.org/src/file/ext/misc/regexp.c) is now included in [CLI](cli.md) builds.
    **Hashes:**
9.  SQLITE_SOURCE_ID: 2021-06-18 18:36:39 5c9a6c06871cb9fe42814af9c039eb6da5427a6ec28f187af7ebfb62eafa66e5
10. SHA3-256 for sqlite3.c: 2a8e87aaa414ac2d45ace8eb74e710935423607a8de0fafcb36bbde5b952d157

<span id="version_3_35_5"></span>

### 2021-04-19 (3.35.5)

1.  Fix defects in the new ALTER TABLE DROP COLUMN feature that could corrupt the database file.
2.  Fix an obscure query optimizer problem that might cause an incorrect query result.
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2021-04-19 18:32:05 1b256d97b553a9611efca188a3d995a2fff712759044ba480f9a0c9e98fae886
4.  SHA3-256 for sqlite3.c: e42291343e8f03940e57fffcf1631e7921013b94419c2f943e816d3edf4e1bbe

<span id="version_3_35_4"></span>

### 2021-04-02 (3.35.4)

1.  Fix a defect in the query planner optimization identified by item 8b above. Ticket [de7db14784a08053](https://sqlite.org/src/info/de7db14784a08053).
2.  Fix a defect in the new [RETURNING](lang_returning.md) syntax. Ticket [132994c8b1063bfb](https://sqlite.org/src/info/132994c8b1063bfb).
3.  Fix the new [RETURNING](lang_returning.md) feature so that it raises an error if one of the terms in the RETURNING clause references a unknown table, instead of silently ignoring that error.
4.  Fix an assertion associated with aggregate function processing that was incorrectly triggered by the [push-down optimization](optoverview.md#pushdown).
    **Hashes:**
5.  SQLITE_SOURCE_ID: 2021-04-02 15:20:15 5d4c65779dab868b285519b19e4cf9d451d50c6048f06f653aa701ec212df45e
6.  SHA3-256 for sqlite3.c: 528b8a26bf5ffd4c7b4647b5b799f86e8fb1a075f715b87a414e94fba3d09dbe

<span id="version_3_35_3"></span>

### 2021-03-26 (3.35.3)

1.  Enhance the OP_OpenDup opcode of the [bytecode engine](opcode.md) so that it works even if the cursor being duplicated itself came from OP_OpenDup. Fix for [ticket bb8a9fd4a9b7fce5](https://sqlite.org/src/info/bb8a9fd4a9b7fce5). This problem only came to light due to the recent MATERIALIZED hint enhancement.
2.  When materializing correlated [common table expressions](lang_with.md), do so separately for each use case, as that is required for correctness. This fixes a problem that was introduced by the MATERIALIZED hint enhancement.
3.  Fix a problem in the filename normalizer of the unix [VFS](vfs.md).
4.  Fix the ["box" output mode](climode.md) in the [CLI](cli.md) so that it works with statements that returns one or more rows of zero columns (such as [PRAGMA incremental_vacuum](pragma.md#pragma_incremental_vacuum)). [Forum post afbbcb5b72](https://sqlite.org/forum/forumpost/afbbcb5b72).
5.  Improvements to error messages generated by faulty common table expressions. [Forum post aa5a0431c99e](https://sqlite.org/forum/forumpost/aa5a0431c99e631).
6.  Fix some incorrect assert() statements.
7.  Fix to the [SELECT statement syntax diagram](syntax/select-stmt.md) so that the FROM clause syntax is shown correctly. [Forum post 9ed02582fe](https://sqlite.org/forum/forumpost/9ed02582fe).
8.  Fix the EBCDIC character classifier so that it understands newlines as whitespace. [Forum post 58540ce22dcd](https://sqlite.org/forum/forumpost/58540ce22dcd5fdcd).
9.  Improvements the [xBestIndex](vtab.md#xbestindex) method in the implementation of the (unsupported) [wholenumber virtual table](https://sqlite.org/src/file/ext/misc/wholenumber.c) extension so that it does a better job of convincing the query planner to avoid trying to materialize a table with an infinite number of rows. [Forum post b52a020ce4](https://sqlite.org/forum/forumpost/b52a020ce4).
    **Hashes:**
10. SQLITE_SOURCE_ID: 2021-03-26 12:12:52 4c5e6c200adc8afe0814936c67a971efc516d1bd739cb620235592f18f40be2a
11. SHA3-256 for sqlite3.c: 91ca6c0a30ebfdba4420bb35f4fd9149d13e45fc853d86ad7527db363e282683

<span id="version_3_35_2"></span>

### 2021-03-17 (3.35.2)

1.  Fix a problem in the [appendvfs.c](https://sqlite.org/src/file/ext/misc/appendvfs.c) extension that was introduced into version 3.35.0.
2.  Ensure that date/time functions with no arguments (which generate responses that depend on the current time) are treated as [non-deterministic functions](deterministic.md). Ticket [2c6c8689fb5f3d2f](https://sqlite.org/src/info/2c6c8689fb5f3d2f)
3.  Fix a problem in the [sqldiff](sqldiff.md) utility program having to do with unusual whitespace characters in a [virtual table](vtab.md) definition.
4.  Limit the new UNION ALL optimization described by item 8c in the 3.35.0 release so that it does not try to make too many new subqueries. See [forum thread 140a67d3d2](https://sqlite.org/forum/forumpost/140a67d3d2) for details.
    **Hashes:**
5.  SQLITE_SOURCE_ID: 2021-03-17 19:07:21 ea80f3002f4120f5dcee76e8779dfdc88e1e096c5cdd06904c20fd26d50c3827
6.  SHA3-256 for sqlite3.c: e8edc7b1512a2e050d548d0840bec6eef83cc297af1426c34c0ee8720f378a11

<span id="version_3_35_1"></span>

### 2021-03-15 (3.35.1)

1.  Fix [a bug](https://sqlite.org/src/info/1c24a659e6d7f3a1) in the new DROP COLUMN feature when used on columns that are indexed and that are quoted in the index definition.
2.  Improve the built-in documentation for the [.dump](cli.md#dump) command in the [CLI](cli.md).
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2021-03-15 16:53:57 aea12399bf1fdc76af43499d4624c3afa17c3e6c2459b71c195804bb98def66a
4.  SHA3-256 for sqlite3.c: fc79e27fd030226c07691b7d7c23aa81c8d46bc3bef5af39060e1507c82b0523

<span id="version_3_35_0"></span>

### 2021-03-12 (3.35.0)

1.  Added [built-in SQL math functions()](lang_mathfunc.md). (Requires the [-DSQLITE_ENABLE_MATH_FUNCTIONS](compile.md#enable_math_functions) compile-time option.)
2.  Added support for [ALTER TABLE DROP COLUMN](lang_altertable.md#altertabdropcol).
3.  Generalize [UPSERT](lang_upsert.md):
    1.  Allow multiple ON CONFLICT clauses that are evaluated in order,
    2.  The final ON CONFLICT clause may omit the conflict target and yet still use DO UPDATE.
4.  Add support for the [RETURNING](lang_returning.md) clause on [DELETE](lang_delete.md), [INSERT](lang_insert.md), and [UPDATE](lang_update.md) statements.
5.  Use less memory when running [VACUUM](lang_vacuum.md) on databases containing very large TEXT or BLOB values. It is no longer necessary to hold the entire TEXT or BLOB in memory all at once.
6.  Add support for the [MATERIALIZED](lang_with.md#mathint) and [NOT MATERIALIZED](lang_with.md#mathint) hints when specifying [common table expressions](lang_with.md). The default behavior was formerly NOT MATERIALIZED, but is now changed to MATERIALIZED for CTEs that are used more than once.
7.  The [SQLITE_DBCONFIG_ENABLE_TRIGGER](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenabletrigger) and [SQLITE_DBCONFIG_ENABLE_VIEW](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableview) settings are modified so that they only control triggers and views in the main database schema or in attached database schemas and not in the TEMP schema. TEMP triggers and views are always allowed.
8.  Query planner/optimizer improvements:
    1.  Enhancements to the [min/max optimization](optoverview.md#minmax) so that it works better with the IN operator and the OP_SeekScan optimization of the previous release.
    2.  Attempt to process EXISTS operators in the WHERE clause as if they were IN operators, in cases where this is a valid transformation and seems likely to improve performance.
    3.  Allow UNION ALL sub-queries to be [flattened](optoverview.md#flattening) even if the parent query is a join.
    4.  Use an index, if appropriate, on IS NOT NULL expressions in the WHERE clause, even if STAT4 is disabled.
    5.  Expressions of the form "x IS NULL" or "x IS NOT NULL" might be converted to simply FALSE or TRUE, if "x" is a column that has a "NOT NULL" constraint and is not involved in an outer join.
    6.  Avoid checking foreign key constraints on an UPDATE statement if the UPDATE does not modify any columns associated with the foreign key.
    7.  Allow WHERE terms to be [pushed down](optoverview.md#pushdown) into sub-queries that contain window functions, as long as the WHERE term is made up of entirely of constants and copies of expressions found in the PARTITION BY clauses of all window functions in the sub-query.
9.  [CLI](cli.md) enhancements:
    1.  Enhance the ".stats" command to accept new arguments "stmt" and "vmstep", causing prepare statement statistics and only the virtual-machine step count to be shown, respectively.
    2.  Add the ".filectrl data_version" command.
    3.  Enhance the ".once" and ".output" commands so that if the destination argument begins with "\|" (indicating that output is redirected into a pipe) then the argument does not need to be quoted.
10. Bug fixes:
    1.  Fix a potential NULL pointer dereference when processing a syntactically incorrect SELECT statement with a correlated WHERE clause and a "HAVING 0" clause. (Also fixed in the 3.34.1 patch release.)
    2.  Fix a [bug in the IN-operator optimization](https://sqlite.org/src/info/ee51301f316c09e9) of version 3.33.0 that can cause an incorrect answer.
    3.  Fix incorrect answers from the [LIKE operator](lang_expr.md#like) if the pattern ends with "%" and there is an "ESCAPE '\_'" clause.

    **Hashes:**
11. SQLITE_SOURCE_ID: 2021-03-12 15:10:09 acd63062eb06748bfe9e4886639e4f2b54ea6a496a83f10716abbaba4115500b
12. SHA3-256 for sqlite3.c: 73a740d881735bef9de7f7bce8c9e6b9e57fe3e77fa7d76a6e8fc5c262fbaedf

<span id="version_3_34_1"></span>

### 2021-01-20 (3.34.1)

1.  Fix a potential use-after-free bug when processing a a subquery with both a correlated WHERE clause and a "HAVING 0" clause and where the parent query is an aggregate.
2.  Fix documentation typos
3.  Fix minor problems in extensions.
    **Hashes:**
4.  SQLITE_SOURCE_ID: 2021-01-20 14:10:07 10e20c0b43500cfb9bbc0eaa061c57514f715d87238f4d835880cd846b9ebd1f
5.  SHA3-256 for sqlite3.c: 799a7be90651fc7296113b641a70b028c142d767b25af1d0a78f93dcf1a2bf20

<span id="version_3_34_0"></span>

### 2020-12-01 (3.34.0)

1.  Added the [sqlite3_txn_state()](c3ref/txn_state.md) interface for reporting on the current transaction state of the database connection.
2.  Enhance [recursive common table expressions](lang_with.md#recursivecte) to support two or more recursive terms as is done by SQL Server, since this helps make [queries against graphs](lang_with.md#rcex3) easier to write and faster to execute.
3.  Improved error messages on [CHECK constraint](lang_createtable.md#ckconst) failures.
4.  [CLI](cli.md) enhancements:
    1.  The [.read](cli.md#dotread) dot-command now accepts a pipeline in addition to a filename.
    2.  Added options --data-only and --nosys to the [.dump](cli.md#dump) dot-command.
    3.  Added the --nosys option to the [.schema](cli.md#dschema) dot-command.
    4.  Table name quoting works correctly for the [.import](cli.md#csv) dot-command.
    5.  The [generate_series(START,END,STEP)](series.md) table-valued function extension is now built into the CLI.
    6.  The [.databases](cli.md#dotdatabases) dot-command now shows the status of each database file as determined by [sqlite3_db_readonly()](c3ref/db_readonly.md) and [sqlite3_txn_state()](c3ref/txn_state.md).
    7.  Added the --tabs command-line option that sets [.mode tabs](climode.md).
    8.  The --init option reports an error if the file named as its argument cannot be opened. The --init option also now honors the --bail option.
5.  Query planner improvements:
    1.  Improved estimates for the cost of running a DISTINCT operator.
    2.  When doing an UPDATE or DELETE using a multi-column index where only a few of the earlier columns of the index are useful for the index lookup, postpone doing the main table seek until after all WHERE clause constraints have been evaluated, in case those constraints can be covered by unused later terms of the index, thus avoiding unnecessary main table seeks.
    3.  The new OP_SeekScan opcode is used to improve performance of multi-column index look-ups when later columns are constrained by an IN operator.
6.  The [BEGIN IMMEDIATE](lang_transaction.md#immediate) and [BEGIN EXCLUSIVE](lang_transaction.md#immediate) commands now work even if one or more attached database files are read-only.
7.  Enhanced [FTS5](fts5.md) to support [trigram indexes](fts5.md#trigramidx).
8.  Improved performance of [WAL mode](wal.md) locking primitives in cases where there are hundreds of connections all accessing the same database file at once.
9.  Enhanced the [carray() table-valued function](carray.md) to include a single-argument form that is bound using the auxiliary [sqlite3_carray_bind()](c3ref/carray_bind.md) interface.
10. The [substr() SQL function](lang_corefunc.md#substr) can now also be called "substring()" for compatibility with SQL Server.
11. The [syntax diagrams](syntaxdiagrams.md) are now implemented as [Pikchr](https://pikchr.org/) scripts and rendered as SVG for improved legibility and ease of maintenance.
    **Hashes:**
12. SQLITE_SOURCE_ID: 2020-12-01 16:14:00 a26b6597e3ae272231b96f9982c3bcc17ddec2f2b6eb4df06a224b91089fed5b
13. SHA3-256 for sqlite3.c: fbd895b0655a337b2cd657675f314188a4e9fe614444cc63dfeb3f066f674514

<span id="version_3_33_0"></span>

### 2020-08-14 (3.33.0)

1.  Support for [UPDATE FROM](lang_update.md#upfrom) following the PostgreSQL syntax.
2.  Increase the maximum size of database files to 281 TB.
3.  Extended the [PRAGMA integrity_check](pragma.md#pragma_integrity_check) statement so that it can optionally be limited to verifying just a single table and its indexes, rather than the entire database file.
4.  Added the [decimal extension](floatingpoint.md#decext) for doing arbitrary-precision decimal arithmetic.
5.  Enhancements to the [ieee754 extension](floatingpoint.md#ieee754ext) for working with IEEE 754 binary64 numbers.
6.  [CLI](cli.md) enhancements:
    1.  Added four new [output modes](climode.md): "box", "json", "markdown", and "table".
    2.  The "column" output mode automatically expands columns to contain the longest output row and automatically turns ".header" on if it has not been previously set.
    3.  The "quote" output mode honors ".separator"
    4.  The [decimal extension](floatingpoint.md#decext) and the [ieee754 extension](floatingpoint.md#ieee754ext) are built-in to the CLI
7.  Query planner improvements:
    1.  Add the ability to find a full-index-scan query plan for queries using [INDEXED BY](lang_indexedby.md) which previously would fail with "no query solution".
    2.  Do a better job of detecting missing, incomplete, and/or dodgy [sqlite_stat1](fileformat2.md#stat1tab) data and generates good query plans in spite of the misinformation.
    3.  Improved performance of queries like "SELECT min(x) FROM t WHERE y IN (?,?,?)" assuming an index on t(x,y).
8.  In [WAL mode](wal.md), if a writer crashes and leaves the [shm file](walformat.md#shm) in an inconsistent state, subsequent transactions are now able to recover the shm file even if there are active read transactions. Before this enhancement, shm file recovery that scenario would result in an [SQLITE_PROTOCOL](rescode.md#protocol) error.
    **Hashes:**
9.  SQLITE_SOURCE_ID: 2020-08-14 13:23:32 fca8dc8b578f215a969cd899336378966156154710873e68b3d9ac5881b0ff3f
10. SHA3-256 for sqlite3.c: d00b7fffa6d33af2303430eaf394321da2960604d25a4471c7af566344f2abf9

<span id="version_3_32_3"></span>

### 2020-06-18 (3.32.3)

1.  Various minor bug fixes including fixes for tickets [8f157e8010b22af0](https://sqlite.org/src/info/8f157e8010b22af0), [9fb26d37cefaba40](https://sqlite.org/src/info/9fb26d37cefaba40), [e367f31901ea8700](https://sqlite.org/src/info/e367f31901ea8700), [b706351ce2ecf59a](https://sqlite.org/src/info/b706351ce2ecf59a), [7c6d876f84e6e7e2](https://sqlite.org/src/info/7c6d876f84e6e7e2), and [c8d3b9f0a750a529](https://sqlite.org/src/info/c8d3b9f0a750a529).
    **Hashes:**
2.  SQLITE_SOURCE_ID: 2020-06-18 14:00:33 7ebdfa80be8e8e73324b8d66b3460222eb74c7e9dfd655b48d6ca7e1933cc8fd
3.  SHA3-256 for sqlite3.c: b62b77ee1c561a69a71bb557694aaa5141f1714c1ff6cc1ba8aa8733c92d4f52

<span id="version_3_32_2"></span>

### 2020-06-04 (3.32.2)

1.  Fix a long-standing bug in the byte-code engine that can cause a [COMMIT](lang_transaction.md) command report as success when in fact it failed to commit. Ticket [810dc8038872e212](https://sqlite.org/src/info/810dc8038872e212)
    **Hashes:**
2.  SQLITE_SOURCE_ID: 2020-06-04 12:58:43 ec02243ea6ce33b090870ae55ab8aa2534b54d216d45c4aa2fdbb00e86861e8c
3.  SHA3-256 for sqlite3.c: f17a2a57f7eebc72d405f3b640b4a49bcd02364a9c36e04feeb145eccafa3f8d

<span id="version_3_32_1"></span>

### 2020-05-25 (3.32.1)

1.  Fix two long-standing bugs that allow malicious SQL statements to crash the process that is running SQLite. These bugs were announced by a third-party approximately 24 hours after the 3.32.0 release but are not specific to the 3.32.0 release.
2.  Other minor compiler-warning fixes and whatnot.
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2020-05-25 16:19:56 0c1fcf4711a2e66c813aed38cf41cd3e2123ee8eb6db98118086764c4ba83350
4.  SHA3-256 for sqlite3.c: f695ae21abf045e4ee77980a67ab2c6e03275009e593ee860a2eabf840482372

<span id="version_3_32_0"></span>

### 2020-05-22 (3.32.0)

1.  Added support for [approximate ANALYZE](lang_analyze.md#approx) using the [PRAGMA analysis_limit](pragma.md#pragma_analysis_limit) command.
2.  Added the [bytecode virtual table](bytecodevtab.md).
3.  Add the [checksum VFS shim](cksumvfs.md) to the set of run-time loadable extensions included in the source tree.
4.  Added the [iif() SQL function](lang_corefunc.md#iif).
5.  INSERT and UPDATE statements now always apply [column affinity](datatype3.md#affinity) before computing [CHECK constraints](lang_createtable.md#ckconst). This bug fix could, in theory, cause problems for legacy databases with unorthodox CHECK constraints the require the input type for an INSERT is different from the declared column type. See ticket [86ba67afafded936](https://sqlite.org/src/info/86ba67afafded936) for more information.
6.  Added the [sqlite3_create_filename()](c3ref/create_filename.md), [sqlite3_free_filename()](c3ref/create_filename.md), and [sqlite3_database_file_object()](c3ref/database_file_object.md) interfaces to better support of [VFS shim](vfs.md#shim) implementations.
7.  Increase the [default upper bound](limits.md#max_variable_number) on the number of [parameters](lang_expr.md#varparam) from 999 to 32766.
8.  Added code for the [UINT collating sequence](uintcseq.md) as an optional [loadable extension](loadext.md).
9.  Enhancements to the [CLI](cli.md):
    1.  Add options to the [.import](cli.md#csv) command: --csv, --ascii, --skip
    2.  The [.dump](cli.md#dump) command now accepts multiple LIKE-pattern arguments and outputs the union of all matching tables.
    3.  Add the .oom command in debugging builds
    4.  Add the --bom option to the [.excel](cli.md#dotexcel), [.output](cli.md#dotoutput), and [.once](cli.md#dotoutput) commands.
    5.  Enhance the .filectrl command to support the --schema option.
    6.  The [UINT collating sequence](uintcseq.md) extension is automatically loaded
10. The [ESCAPE](lang_expr.md#like) clause of a [LIKE](lang_expr.md#like) operator now overrides wildcard characters, so that the behavior matches what PostgreSQL does.
11. SQLITE_SOURCE_ID: 2020-05-22 17:46:16 5998789c9c744bce92e4cff7636bba800a75574243d6977e1fc8281e360f8d5a
12. SHA3-256 for sqlite3.c: 33ed868b21b62ce1d0352ed88bdbd9880a42f29046497a222df6459fc32a356f

<span id="version_3_31_1"></span>

### 2020-01-27 (3.31.1)

1.  Revert the data layout for an internal-use-only SQLite data structure. Applications that use SQLite should never reference internal SQLite data structures, but some do anyhow, and a change to one such data structure in 3.30.0 broke a popular and widely-deployed application. Reverting that change in SQLite, at least temporarily, gives developers of misbehaving applications time to fix their code.
2.  Fix a typos in the sqlite3ext.h header file that prevented the [sqlite3_stmt_isexplain()](c3ref/stmt_isexplain.md) and [sqlite3_value_frombind()](c3ref/value_blob.md) interfaces from being called from [run-time loadable extensions](loadext.md).
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2020-01-27 19:55:54 3bfa9cc97da10598521b342961df8f5f68c7388fa117345eeb516eaa837bb4d6
4.  SHA3-256 for sqlite3.c: de465c64f09529429a38cbdf637acce4dfda6897f93e3db3594009e0fed56d27

<span id="version_3_31_0"></span>

### 2020-01-22 (3.31.0)

1.  Add support for [generated columns](gencol.md).
2.  Add the [sqlite3_hard_heap_limit64()](c3ref/hard_heap_limit64.md) interface and the corresponding [PRAGMA hard_heap_limit](pragma.md#pragma_hard_heap_limit) command.
3.  Enhance the [function_list pragma](pragma.md#pragma_function_list) to show the number of arguments on each function, the type of function (scalar, aggregate, window), and the function property flags [SQLITE_DETERMINISTIC](c3ref/c_deterministic.md#sqlitedeterministic), [SQLITE_DIRECTONLY](c3ref/c_deterministic.md#sqlitedirectonly), [SQLITE_INNOCUOUS](c3ref/c_deterministic.md#sqliteinnocuous), and/or [SQLITE_SUBTYPE](c3ref/c_deterministic.md#sqlitesubtype).
4.  Add the [aggregated mode](dbstat.md#dbstatagg) feature to the [DBSTAT virtual table](dbstat.md).
5.  Add the [SQLITE_OPEN_NOFOLLOW](c3ref/open.md#opennofollow) option to [sqlite3_open_v2()](c3ref/open.md) that prevents SQLite from opening symbolic links.
6.  Added the "#-N" array notation for [JSON function path arguments](json1.md#jsonpath).
7.  Added the [SQLITE_DBCONFIG_TRUSTED_SCHEMA](c3ref/c_dbconfig_defensive.md#sqlitedbconfigtrustedschema) connection setting which is also controllable via the new [trusted_schema pragma](pragma.md#pragma_trusted_schema) and at compile-time using the [-DSQLITE_TRUSTED_SCHEMA](compile.md#trusted_schema) compile-time option.
8.  Added APIs [sqlite3_filename_database()](c3ref/filename_database.md), [sqlite3_filename_journal()](c3ref/filename_database.md), and [sqlite3_filename_wal()](c3ref/filename_database.md) which are useful for specialized extensions.
9.  Add the [sqlite3_uri_key()](c3ref/uri_boolean.md) interface.
10. Upgraded the [sqlite3_uri_parameter()](c3ref/uri_boolean.md) function so that it works with the rollback journal or WAL filename in addition to the database filename.
11. Provide the ability to tag [application-defined SQL functions](appfunc.md) with new properties [SQLITE_INNOCUOUS](c3ref/c_deterministic.md#sqliteinnocuous) or [SQLITE_DIRECTONLY](c3ref/c_deterministic.md#sqlitedirectonly).
12. Add new verbs to [sqlite3_vtab_config()](c3ref/vtab_config.md) so that the [xConnect](vtab.md#xconnect) method of virtual tables can declare the virtual table as [SQLITE_VTAB_INNOCUOUS](c3ref/c_vtab_constraint_support.md#sqlitevtabinnocuous) or [SQLITE_VTAB_DIRECTONLY](c3ref/c_vtab_constraint_support.md#sqlitevtabdirectonly).
13. Faster response to [sqlite3_interrupt()](c3ref/interrupt.md).
14. Added the [uuid.c](https://sqlite.org/src/file/ext/misc/uuid.c) extension module implementing functions for processing RFC-4122 UUIDs.
15. The [lookaside memory allocator](malloc.md#lookaside) is enhanced to support two separate memory pools with different sized allocations in each pool. This allows more memory allocations to be covered by lookaside while at the same time reducing the heap memory usage to 48KB per connection, down from 120KB.
16. The [legacy_file_format pragma](pragma.md#pragma_legacy_file_format) is deactivated. It is now a no-op. In its place, the [SQLITE_DBCONFIG_LEGACY_FILE_FORMAT](c3ref/c_dbconfig_defensive.md#sqlitedbconfiglegacyfileformat) option to [sqlite3_db_config()](c3ref/db_config.md) is provided. The legacy_file_format pragma is deactivated because (1) it is rarely useful and (2) it is incompatible with [VACUUM](lang_vacuum.md) in schemas that have tables with both generated columns and descending indexes. Ticket [6484e6ce678fffab](https://sqlite.org/src/info/6484e6ce678fffab)
    **Hashes:**
17. SQLITE_SOURCE_ID: 2020-01-22 18:38:59 f6affdd41608946fcfcea914ece149038a8b25a62bbe719ed2561c649b86d824
18. SHA3-256 for sqlite3.c: a5fca0b9f8cbf80ac89b97193378c719d4af4b7d647729d8df9c0c0fca7b1388

<span id="version_3_30_1"></span>

### 2019-10-10 (3.30.1)

1.  Fix a bug in the [query flattener](optoverview.md#flattening) that might cause a segfault for nested queries that use the new [FILTER clause on aggregate functions](lang_aggfunc.md#aggfilter). Ticket [1079ad19993d13fa](https://sqlite.org/src/info/1079ad19993d13fa)
2.  Cherrypick fixes for other obscure problems found since the 3.30.0 release
    **Hashes:**
3.  SQLITE_SOURCE_ID: 2019-10-10 20:19:45 18db032d058f1436ce3dea84081f4ee5a0f2259ad97301d43c426bc7f3df1b0b
4.  SHA3-256 for sqlite3.c: f96fafe4c110ed7d77fc70a7d690e5edd1e64fefb84b3b5969a722d885de1f2d

<span id="version_3_30_0"></span>

### 2019-10-04 (3.30.0)

1.  Add support for the [FILTER clause on aggregate functions](lang_aggfunc.md#aggfilter).
2.  Add support for the [NULLS FIRST](lang_select.md#nullslast) and [NULLS LAST](lang_select.md#nullslast) syntax in [ORDER BY](lang_select.md#orderby) clauses.
3.  The [index_info](pragma.md#pragma_index_info) and [index_xinfo](pragma.md#pragma_index_xinfo) pragmas are enhanced to provide information about the on-disk representation of [WITHOUT ROWID](withoutrowid.md) tables.
4.  Add the [sqlite3_drop_modules()](c3ref/drop_modules.md) interface, allowing applications to disable automatically loaded virtual tables that they do not need.
5.  Improvements to the [.recover dot-command](cli.md#recover) in the [CLI](cli.md) so that it recovers more content from corrupt database files.
6.  Enhance the [RBU](rbu.md) extension to support [indexes on expressions](expridx.md).
7.  Change the schema parser so that it will error out if any of the type, name, and tbl_name columns of the [sqlite_master table](schematab.md) have been corrupted and the database connection is not in [writable_schema](pragma.md#pragma_writable_schema) mode.
8.  The [PRAGMA function_list](pragma.md#pragma_function_list), [PRAGMA module_list](pragma.md#pragma_module_list), and [PRAGMA pragma_list](pragma.md#pragma_pragma_list) commands are now enabled in all builds by default. Disable them using [-DSQLITE_OMIT_INTROSPECTION_PRAGMAS](compile.md#omit_introspection_pragmas).
9.  Add the [SQLITE_DBCONFIG_ENABLE_VIEW](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableview) option for [sqlite3_db_config()](c3ref/db_config.md).
10. Added the [TCL Interface](tclsqlite.md) [config method](tclsqlite.md#config) in order to be able to disable [SQLITE_DBCONFIG_ENABLE_VIEW](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableview) as well as control other [sqlite3_db_config()](c3ref/db_config.md) options from TCL.
11. Added the [SQLITE_DIRECTONLY](c3ref/c_deterministic.md#sqlitedirectonly) flag for [application-defined SQL functions](appfunc.md) to prevent those functions from being used inside triggers and views.
12. The legacy [SQLITE_ENABLE_STAT3](compile.md#enable_stat3) compile-time option is now a no-op.
    **Hashes:**
13. SQLITE_SOURCE_ID: 2019-10-04 15:03:17 c20a35336432025445f9f7e289d0cc3e4003fb17f45a4ce74c6269c407c6e09f
14. SHA3-256 for sqlite3.c: f04393dd47205a4ee2b98ff737dc51a3fdbcc14c055b88d58f5b27d0672158f5

<span id="version_3_29_0"></span>

### 2019-07-10 (3.29.0)

1.  Added the [SQLITE_DBCONFIG_DQS_DML](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdqsdml) and [SQLITE_DBCONFIG_DQS_DDL](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdqsddl) actions to [sqlite3_db_config()](c3ref/db_config.md) for activating and deactivating the [double-quoted string literal](quirks.md#dblquote) misfeature. Both default to "on" for legacy compatibility, but developers are encouraged to turn them "off", perhaps using the [-DSQLITE_DQS=0](compile.md#dqs) compile-time option.
2.  [-DSQLITE_DQS=0](compile.md#dqs) is now a [recommended compile-time option](compile.md#rcmd).
3.  Improvements to the [query planner](optoverview.md):
    1.  Improved optimization of AND and OR operators when one or the other operand is a constant.
    2.  Enhancements to the [LIKE optimization](optoverview.md#like_opt) for cases when the left-hand side column has numeric affinity.
4.  Added the "[sqlite_dbdata](https://sqlite.org/src/file/ext/misc/dbdata.c)" virtual table for extracting raw low-level content from an SQLite database, even a database that is corrupt.
5.  Improvements to rounding behavior, so that the results of rounding binary numbers using the [round()](lang_corefunc.md#round) function are closer to what people who are used to thinking in decimal actually expect.
6.  Enhancements to the [CLI](cli.md):
    1.  Add the ".recover" command which tries to recover as much content as possible from a corrupt database file.
    2.  Add the ".filectrl" command useful for testing.
    3.  Add the long-standing ".testctrl" command to the ".help" menu.
    4.  Added the ".dbconfig" command

    **Hashes:**
7.  SQLITE_SOURCE_ID: 2019-07-10 17:32:03 fc82b73eaac8b36950e527f12c4b5dc1e147e6f4ad2217ae43ad82882a88bfa6
8.  SHA3-256 for sqlite3.c: d9a5daf7697a827f4b2638276ce639fa04e8e8bb5fd3a6b683cfad10f1c81b12

<span id="version_3_28_0"></span>

### 2019-04-16 (3.28.0)

1.  Enhanced [window functions](windowfunctions.md):
    1.  Add support the [EXCLUDE clause](windowfunctions.md#wexcls).
    2.  Add support for [window chaining](windowfunctions.md#wchaining).
    3.  Add support for [GROUPS frames](windowfunctions.md#grouptype).
    4.  Add support for "[\<expr\> PRECEDING](windowfunctions.md#exprrange)" and "[\<expr\> FOLLOWING](windowfunctions.md#exprrange)" boundaries in RANGE [frames](windowfunctions.md#framespec).
2.  Added the new [sqlite3_stmt_isexplain(S)](c3ref/stmt_isexplain.md) interface for determining whether or not a [prepared statement](c3ref/stmt.md) is an [EXPLAIN](lang_explain.md).
3.  Enhanced [VACUUM INTO](lang_vacuum.md#vacuuminto) so that it works for read-only databases.
4.  New query optimizations:
    1.  Enable the [LIKE optimization](optoverview.md#like_opt) for cases when the ESCAPE keyword is present and [PRAGMA case_sensitive_like](pragma.md#pragma_case_sensitive_like) is on.
    2.  In queries that are driven by a [partial index](partialindex.md), avoid unnecessary tests of the constraint named in the WHERE clause of the partial index, since we know that constraint must always be true.
5.  Enhancements to the [TCL Interface](tclsqlite.md):
    1.  Added the -returntype option to the [function method](tclsqlite.md#function).
    2.  Added the new [bind_fallback method](tclsqlite.md#bind_fallback).
6.  Enhancements to the [CLI](cli.md):
    1.  Added support for [bound parameters](lang_expr.md#varparam) and the [.parameter command](cli.md#param).
    2.  Fix the [readfile()](cli.md#fileio) function so that it returns an empty BLOB rather than throwing an out-of-memory error when reading an empty file.
    3.  Fix the [writefile()](cli.md#fileio) function so that when it creates new directories along the path of a new file, it gives them umask permissions rather than the same permissions as the file.
    4.  Change [--update option](cli.md#arinsup) in the [.archive command](cli.md#sqlar) so that it skips files that are already in the archive and are unchanged. Add the new --insert option that works like --update used to work.
7.  Added the [fossildelta.c](https://sqlite.org/src/file/ext/misc/fossildelta.c) extension that can create, apply, and deconstruct the [Fossil DVCS file delta format](https://fossil-scm.org/fossil/doc/trunk/www/delta_format.wiki) that is used by the [RBU extension](rbu.md).
8.  Added the [SQLITE_DBCONFIG_WRITABLE_SCHEMA](c3ref/c_dbconfig_defensive.md#sqlitedbconfigwritableschema) verb for the [sqlite3_db_config()](c3ref/db_config.md) interface, that does the same work as [PRAGMA writable_schema](pragma.md#pragma_writable_schema) without using the SQL parser.
9.  Added the [sqlite3_value_frombind()](c3ref/value_blob.md) API for determining if the argument to an SQL function is from a [bound parameter](lang_expr.md#varparam).
10. Security and compatibilities enhancements to [fts3_tokenizer()](fts3.md#f3tknzr):
    1.  The [fts3_tokenizer()](fts3.md#f3tknzr) function always returns NULL unless either the legacy application-defined FTS3 tokenizers interface are enabled using the [sqlite3_db_config](c3ref/db_config.md)([SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenablefts3tokenizer)) setting, or unless the first argument to fts3_tokenizer() is a [bound parameter](lang_expr.md#varparam).
    2.  The two-argument version of [fts3_tokenizer()](fts3.md#f3tknzr) accepts a pointer to the tokenizer method object even without the [sqlite3_db_config](c3ref/db_config.md)([SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenablefts3tokenizer)) setting if the second argument is a [bound parameter](lang_expr.md#varparam)
11. Improved robustness against corrupt database files.
12. Miscellaneous performance enhancements
13. Established a Git mirror of the offical SQLite source tree. The canonical sources for SQLite are maintained using the [Fossil DVCS](https://fossil-scm.org/) at <https://sqlite.org/src>. The Git mirror can be seen at <https://github.com/sqlite/sqlite>.
    **Hashes:**
14. SQLITE_SOURCE_ID: 2019-04-16 19:49:53 884b4b7e502b4e991677b53971277adfaf0a04a284f8e483e2553d0f83156b50
15. SHA3-256 for sqlite3.c: 411efca996b65448d9798eb203d6ebe9627b7161a646f5d00911e2902a57b2e9

<span id="version_3_27_2"></span>

### 2019-02-25 (3.27.2)

1.  Fix a bug in the IN operator that was introduced by an attempted optimization in version 3.27.0. Ticket [df46dfb631f75694](https://sqlite.org/src/info/df46dfb631f75694)
2.  Fix a bug causing a crash when a [window function](windowfunctions.md) is misused. Ticket [4feb3159c6bc3f7e33959](https://sqlite.org/src/info/4feb3159c6bc3f7e33959).
3.  Fix various documentation typos
    **Hashes:**
4.  SQLITE_SOURCE_ID: bd49a8271d650fa89e446b42e513b595a717b9212c91dd384aab871fc1d0f6d7
5.  SHA3-256 for sqlite3.c: 1dbae33bff261f979d0042338f72c9e734b11a80720fb32498bae9150cc576e7

<span id="version_3_27_1"></span>

### 2019-02-08 (3.27.1)

1.  Fix a bug in the query optimizer: an adverse interaction between the [OR optimization](optoverview.md#or_opt) and the optimization that tries to use values read directly from an [expression index](expridx.md) instead of recomputing the expression. Ticket [4e8e4857d32d401f](https://sqlite.org/src/info/4e8e4857d32d401f)
    **Hashes:**
2.  SQLITE_SOURCE_ID: 2019-02-08 13:17:39 0eca3dd3d38b31c92b49ca2d311128b74584714d9e7de895b1a6286ef959a1dd
3.  SHA3-256 for sqlite3.c: 11c14992660d5ac713ea8bea48dc5e6123f26bc8d3075fe5585d1a217d090233

<span id="version_3_27_0"></span>

### 2019-02-07 (3.27.0)

1.  Added the [VACUUM INTO](lang_vacuum.md#vacuuminto) command
2.  Issue an SQLITE_WARNING message on the [error log](errlog.md) if a [double-quoted string literal](quirks.md#dblquote) is used.
3.  The [sqlite3_normalized_sql()](c3ref/expanded_sql.md) interface works on any prepared statement created using [sqlite3_prepare_v2()](c3ref/prepare.md) or [sqlite3_prepare_v3()](c3ref/prepare.md). It is no longer necessary to use [sqlite3_prepare_v3()](c3ref/prepare.md) with [SQLITE_PREPARE_NORMALIZE](c3ref/c_prepare_dont_log.md#sqlitepreparenormalize) in order to use [sqlite3_normalized_sql()](c3ref/expanded_sql.md).
4.  Added the remove_diacritics=2 option to [FTS3](fts3.md) and [FTS5](fts5.md).
5.  Added the [SQLITE_PREPARE_NO_VTAB](c3ref/c_prepare_dont_log.md#sqlitepreparenovtab) option to [sqlite3_prepare_v3()](c3ref/prepare.md). Use that option to prevent circular references to [shadow tables](vtab.md#xshadowname) from causing resource leaks.
6.  Enhancements to the [sqlite3_deserialize()](c3ref/deserialize.md) interface:
    1.  Add the [SQLITE_FCNTL_SIZE_LIMIT](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlsizelimit) [file-control](c3ref/file_control.md) for setting an upper bound on the size of the in-memory database created by sqlite3_deserialize. The default upper bound is 1GiB, or whatever alternative value is specified by [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_MEMDB_MAXSIZE](c3ref/c_config_covering_index_scan.md#sqliteconfigmemdbmaxsize)) and/or [SQLITE_MEMDB_DEFAULT_MAXSIZE](compile.md#memdb_default_maxsize).
    2.  Honor the [SQLITE_DESERIALIZE_READONLY](c3ref/c_deserialize_freeonclose.md) flag, which was previously described in the documentation, but was previously a no-op.
    3.  Enhance the "deserialize" command of the [TCL Interface](tclsqlite.md) to give it new "--maxsize N" and "--readonly BOOLEAN" options.
7.  Enhancements to the [CLI](cli.md), mostly to support testing and debugging of the SQLite library itself:
    1.  Add support for ".open --hexdb". The "[dbtotxt](https://sqlite.org/src/doc/trunk/tool/dbtotxt.md)" utility program used to generate the text for the "hexdb" is added to the source tree.
    2.  Add support for the "--maxsize N" option on ".open --deserialize".
    3.  Add the "--memtrace" command-line option, to show all memory allocations and deallocations.
    4.  Add the ".eqp trace" option on builds with SQLITE_DEBUG, to enable bytecode program listing with indentation and [PRAGMA vdbe_trace](pragma.md#pragma_vdbe_trace) all in one step.
    5.  Add the ".progress" command for accessing the [sqlite3_progress_handler()](c3ref/progress_handler.md) interface.
    6.  Add the "--async" option to the ".backup" command.
    7.  Add options "--expanded", "--normalized", "--plain", "--profile", "--row", "--stmt", and "--close" to the ".trace" command.
8.  Increased robustness against malicious SQL that is run against a maliciously corrupted database.
    **Bug fixes:**
9.  Do not use a partial index to do a table scan on an IN operator. Ticket [1d958d90596593a774](https://sqlite.org/src/info/1d958d90596593a774).
10. Fix the [query flattener](optoverview.md#flattening) so that it works on queries that contain subqueries that use [window functions](windowfunctions.md). Ticket [709fcd17810f65f717](https://sqlite.org/src/info/f09fcd17810f65f717)
11. Ensure that ALTER TABLE modifies table and column names embedded in WITH clauses that are part of views and triggers.
12. Fix a parser bug that prevented the use of parentheses around table-valued functions.
13. Fix a problem with the [OR optimization](optoverview.md#or_opt) on [indexes on expressions](expridx.md). Ticket [d96eba87698a428c1d](https://sqlite.org/src/info/d96eba87698a428c1d).
14. Fix a problem with the [LEFT JOIN strength reduction optimization](optoverview.md#leftjoinreduction) in which the optimization was being applied inappropriately due to an IS NOT NULL operator. Ticket [5948e09b8c415bc45d](https://sqlite.org/src/info/5948e09b8c415bc45d).
15. Fix the [REPLACE](lang_replace.md) command so that it is no longer able to sneak a NULL value into a NOT NULL column even if the NOT NULL column has a default value of NULL. Ticket [e6f1f2e34dceeb1ed6](https://sqlite.org/src/info/e6f1f2e34dceeb1ed6)
16. Fix a problem with the use of [window functions](windowfunctions.md) used within [correlated subqueries](lang_expr.md#cosub). Ticket [d0866b26f83e9c55e3](https://sqlite.org/src/info/d0866b26f83e9c55e3)
17. Fix the [ALTER TABLE RENAME COLUMN](lang_altertable.md#altertabmvcol) command so that it works for tables that have redundant UNIQUE constraints. Ticket [bc8d94f0fbd633fd9a](https://sqlite.org/src/info/bc8d94f0fbd633fd9a)
18. Fix a bug that caused [zeroblob](lang_corefunc.md#zeroblob) values to be truncated when inserted into a table that uses an [expression index](expridx.md). Ticket [bb4bdb9f7f654b0bb9](https://sqlite.org/src/info/bb4bdb9f7f654b0bb9)
    **Hashes:**
19. SQLITE_SOURCE_ID: "2019-02-07 17:02:52 97744701c3bd414e6c9d7182639d8c2ce7cf124c4fce625071ae65658ac61713 "
20. SHA3-256 for sqlite3.c: ca011a10ee8515b33e5643444b98ee3d74dc45d3ac766c3700320def52bc6aba

<span id="version_3_26_0"></span>

### 2018-12-01 (3.26.0)

1.  Optimization: When doing an [UPDATE](lang_update.md) on a table with [indexes on expressions](expridx.md), do not update the expression indexes if they do not refer to any of the columns of the table being updated.
2.  Allow the [xBestIndex()](vtab.md#xbestindex) method of [virtual table](vtab.md) implementations to return [SQLITE_CONSTRAINT](rescode.md#constraint) to indicate that the proposed query plan is unusable and should not be given further consideration.
3.  Added the [SQLITE_DBCONFIG_DEFENSIVE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdefensive) option which disables the ability to create corrupt database files using ordinary SQL.
4.  Added support for read-only [shadow tables](vtab.md#xshadowname) when the [SQLITE_DBCONFIG_DEFENSIVE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdefensive) option is enabled.
5.  Added the [PRAGMA legacy_alter_table](pragma.md#pragma_legacy_alter_table) command, which if enabled causes the [ALTER TABLE](lang_altertable.md) command to behave like older version of SQLite (prior to version 3.25.0) for compatibility.
6.  Added [PRAGMA table_xinfo](pragma.md#pragma_table_xinfo) that works just like [PRAGMA table_info](pragma.md#pragma_table_info) except that it also shows [hidden columns](vtab.md#hiddencol) in virtual tables.
7.  Added the [explain virtual table](https://sqlite.org/src/file/ext/misc/explain.c) as a run-time loadable extension.
8.  Add a limit counter to the query planner to prevent excessive [sqlite3_prepare()](c3ref/prepare.md) times for certain pathological SQL inputs.
9.  Added support for the [sqlite3_normalized_sql()](c3ref/expanded_sql.md) interface, when compiling with SQLITE_ENABLE_NORMALIZE.
10. Enhanced triggers so that they can use [table-valued functions](vtab.md#tabfunc2) that exist in schemas other than the schema where the trigger is defined.
11. Enhancements to the [CLI](cli.md):
    1.  Improvements to the ".help" command.
    2.  The SQLITE_HISTORY environment variable, if it exists, specifies the name of the command-line editing history file
    3.  The --deserialize option associated with opening a new database cause the database file to be read into memory and accessed using the [sqlite3_deserialize()](c3ref/deserialize.md) API. This simplifies running tests on a database without modifying the file on disk.
12. Enhancements to the [geopoly](geopoly.md) extension:
    1.  Always stores polygons using the binary format, which is faster and uses less space.
    2.  Added the [geopoly_regular()](geopoly.md#regpoly) function.
    3.  Added the [geopoly_ccw()](geopoly.md#ccw) function.
13. Enhancements to the [session](sessionintro.md) extension:
    1.  Added the [SQLITE_CHANGESETAPPLY_INVERT](session/c_changesetapply_fknoaction.md) flag
    2.  Added the [sqlite3changeset_start_v2()](session/sqlite3changeset_start.md) interface and the [SQLITE_CHANGESETSTART_INVERT](session/c_changesetstart_invert.md) flag.
    3.  Added the [changesetfuzz.c](https://sqlite.org/src/file/ext/session/changesetfuzz.c) test-case generator utility.

    **Hashes:**
14. SQLITE_SOURCE_ID: "2018-12-01 12:34:55 bf8c1b2b7a5960c282e543b9c293686dccff272512d08865f4600fb58238b4f9"
15. SHA3-256 for sqlite3.c: 72c08830da9b5d1cb397c612c0e870d7f5eb41a323b41aa3d8aa5ae9ccedb2c4

<span id="version_3_25_3"></span>

### 2018-11-05 (3.25.3)

1.  Disallow the use of [window functions](windowfunctions.md) in the recursive part of a CTE. Ticket [e8275b415a2f03bee](https://sqlite.org/src/info/e8275b415a2f03bee)
2.  Fix the behavior of typeof() and length() on virtual tables. Ticket [69d642332d25aa3b7315a6d385](https://sqlite.org/src/info/69d642332d25aa3b7315a6d385)
3.  Strengthen defenses against deliberately corrupted database files.
4.  Fix a problem in the query planner that results when a row-value expression is used with a PRIMARY KEY with redundant columns. Ticket [1a84668dcfdebaf12415d](https://sqlite.org/src/info/1a84668dcfdebaf12415d)
5.  Fix the query planner so that it works correctly for IS NOT NULL operators in the ON clause of a LEFT JOIN with the SQLITE_ENABLE_STAT4 compile-time option. [65eb38f6e46de8c75e188a17ec](https://sqlite.org/src/info/65eb38f6e46de8c75e188a17ec)
    **Hashes:**
6.  SQLITE_SOURCE_ID: "2018-11-05 20:37:38 89e099fbe5e13c33e683bef07361231ca525b88f7907be7092058007b75036f2"
7.  SHA3-256 for sqlite3.c: 45586e4df74de3a43f3a1f8c7a78c3c3f02edce01af7d10cafe68bb94476a5c5

<span id="version_3_25_2"></span>

### 2018-09-25 (3.25.2)

1.  Add the [PRAGMA legacy_alter_table=ON](pragma.md#pragma_legacy_alter_table) command that causes the "ALTER TABLE RENAME" command to behave as it did in SQLite versions 3.24.0 and earlier: references to the renamed table inside the bodies of triggers and views are not updated. This new pragma provides a compatibility work around for older programs that expected the older, wonky behavior of ALTER TABLE RENAME.
2.  Fix a problem with the new [window functions](windowfunctions.md) implementation that caused a malfunction when complicated expressions involving window functions were used inside of a view.
3.  Fixes for various other compiler warnings and minor problems associated with obscure configurations.
    **Hashes:**
4.  SQLITE_SOURCE_ID: "2018-09-25 19:08:10 fb90e7189ae6d62e77ba3a308ca5d683f90bbe633cf681865365b8e92792d1c7"
5.  SHA3-256 for sqlite3.c: 34c23ff91631ae10354f8c9d62fd7d65732b3d7f3acfd0bbae31ff4a62fe28af

<span id="version_3_25_1"></span>

### 2018-09-18 (3.25.1)

1.  Extra sanity checking added to ALTER TABLE in the 3.25.0 release sometimes raises a false-positive when the table being modified has a trigger that updates a virtual table. The false-positive caused the ALTER TABLE to rollback, thus leaving the schema unchanged. Ticket [b41031ea2b537237](https://sqlite.org/src/info/b41031ea2b537237).
2.  The fix in the 3.25.0 release for the endless-loop in the byte-code associated with the ORDER BY LIMIT optimization did not work for some queries involving window functions. An additional correction is required. Ticket [510cde277783b5fb](https://sqlite.org/src/info/510cde277783b5fb)
    **Hashes:**
3.  SQLITE_SOURCE_ID: "2018-09-18 20:20:44 2ac9003de44da7dafa3fbb1915ac5725a9275c86bf2f3b7aa19321bf1460b386"
4.  SHA3-256 for sqlite3.c: 1b2302e7a54cc99c84ff699a299f61f069a28e1ed090b89e4430ca80ae2aab06

<span id="version_3_25_0"></span>

### 2018-09-15 (3.25.0)

1.  Add support for [window functions](windowfunctions.md)
2.  Enhancements the [ALTER TABLE](lang_altertable.md) command:
    1.  Add support for renaming columns within a table using ALTER TABLE *table* RENAME COLUMN *oldname* TO *newname*.
    2.  Fix table rename feature so that it also updates references to the renamed table in [triggers](lang_createtrigger.md) and [views](lang_createview.md).
3.  Query optimizer improvements:
    1.  Avoid unnecessary loads of columns in an aggregate query that are not within an aggregate function and that are not part of the GROUP BY clause.
    2.  The IN-early-out optimization: When doing a look-up on a multi-column index and an IN operator is used on a column other than the left-most column, then if no rows match against the first IN value, check to make sure there exist rows that match the columns to the right before continuing with the next IN value.
    3.  Use the transitive property to try to propagate constant values within the WHERE clause. For example, convert "a=99 AND b=a" into "a=99 AND b=99".
4.  Use a separate mutex on every inode in the unix [VFS](vfs.md), rather than a single mutex shared among them all, for slightly better concurrency in multi-threaded environments.
5.  Enhance the [PRAGMA integrity_check](pragma.md#pragma_integrity_check) command for improved detection of problems on the page freelist.
6.  Output infinity as 1e999 in the ".dump" command of the [command-line shell](cli.md).
7.  Added the [SQLITE_FCNTL_DATA_VERSION](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntldataversion) file-control.
8.  Added the [Geopoly module](geopoly.md)
    **Bug fixes:**
9.  The ORDER BY LIMIT optimization might have caused an infinite loop in the byte code of the prepared statement under very obscure circumstances, due to a confluence of minor defects in the query optimizer. Fix for ticket [9936b2fa443fec03ff25](https://sqlite.org/src/info/9936b2fa443fec03ff25)
10. On an UPSERT when the order of constraint checks is rearranged, ensure that the affinity transformations on the inserted content occur before any of the constraint checks. Fix for ticket [79cad5e4b2e219dd197242e9e](https://sqlite.org/src/info/79cad5e4b2e219dd197242e9e).
11. Avoid using a prepared statement for ".stats on" command of the [CLI](cli.md) after it has been closed by the ".eqp full" logicc. Fix for ticket [7be932dfa60a8a6b3b26bcf76](https://sqlite.org/src/info/7be932dfa60a8a6b3b26bcf76).
12. The LIKE optimization was generating incorrect byte-code and hence getting the wrong answer if the left-hand operand has numeric affinity and the right-hand-side pattern is '/%' or if the pattern begins with the ESCAPE character. Fix for ticket [c94369cae9b561b1f996d0054b](https://sqlite.org/src/info/c94369cae9b561b1f996d0054b)
    **Hashes:**
13. SQLITE_SOURCE_ID: "2018-09-15 04:01:47 b63af6c3bd33152742648d5d2e8dc5d5fcbcdd27df409272b6aea00a6f761760"
14. SHA3-256 for sqlite3.c: 989e3ff37f2b5eea8e42205f808ccf0ba86c6ea6aa928ad2c011f33a108ac45d

<span id="version_3_24_0"></span>

### 2018-06-04 (3.24.0)

1.  Add support for PostgreSQL-style [UPSERT](lang_upsert.md).
2.  Add support for [auxiliary columns in r-tree tables](rtree.md#auxcol).
3.  Add C-language APIs for discovering SQL keywords used by SQLite: [sqlite3_keyword_count()](c3ref/keyword_check.md), [sqlite3_keyword_name()](c3ref/keyword_check.md), and [sqlite3_keyword_check()](c3ref/keyword_check.md).
4.  Add C-language APIs for dynamic strings based on the [sqlite3_str](c3ref/str.md) object.
5.  Enhance [ALTER TABLE](lang_altertable.md) so that it recognizes "true" and "false" as valid arguments to DEFAULT.
6.  Add the sorter-reference optimization as a compile-time option. Only available if compiled with SQLITE_ENABLE_SORTER_REFERENCES.
7.  Improve the format of the [EXPLAIN QUERY PLAN](eqp.md) raw output, so that it gives better information about the query plan and about the relationships between the various components of the plan.
8.  Added the [SQLITE_DBCONFIG_RESET_DATABASE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigresetdatabase) option to the [sqlite3_db_config()](c3ref/db_config.md) API.
    **[CLI](cli.md) Enhancements:**
9.  Automatically intercepts the raw [EXPLAIN QUERY PLAN](eqp.md) output and reformats it into an ASCII-art graph.
10. Lines that begin with "#" and that are not in the middle of an SQL statement are interpreted as comments.
11. Added the --append option to the ".backup" command.
12. Added the ".dbconfig" command.
    **Performance:**
13. [UPDATE](lang_update.md) avoids unnecessary low-level disk writes when the contents of the database file do not actually change. For example, "UPDATE t1 SET x=25 WHERE y=?" generates no extra disk I/O if the value in column x is already 25. Similarly, when doing [UPDATE](lang_update.md) on records that span multiple pages, only the subset of pages that actually change are written to disk. This is a low-level performance optimization only and does not affect the behavior of TRIGGERs or other higher level SQL structures.
14. Queries that use ORDER BY and LIMIT now try to avoid computing rows that cannot possibly come in under the LIMIT. This can greatly improve performance of ORDER BY LIMIT queries, especially when the LIMIT is small relative to the number of unrestricted output rows.
15. The [OR optimization](optoverview.md#or_opt) is allowed to proceed even if the OR expression has also been converted into an IN expression. Uses of the OR optimization are now also [more clearly shown](eqp.md#or-opt) in the [EXPLAIN QUERY PLAN](eqp.md) output.
16. The query planner is more aggressive about using [automatic indexes](optoverview.md#autoindex) for views and subqueries for which it is not possible to create a persistent index.
17. Make use of the one-pass UPDATE and DELETE query plans in the [R-Tree extension](rtree.md) where appropriate.
18. Performance improvements in the LEMON-generated parser.
    **Bug fixes:**
19. For the right-hand table of a LEFT JOIN, compute the values of expressions directly rather than loading precomputed values out of an [expression index](expridx.md) as the expression index might not contain the correct value. Ticket [7fa8049685b50b5aeb0c2](https://sqlite.org/src/info/7fa8049685b50b5aeb0c2)
20. Do not attempt to use terms from the WHERE clause to enable indexed lookup of the right-hand table of a LEFT JOIN. Ticket [4ba5abf65c5b0f9a96a7a](https://sqlite.org/src/info/4ba5abf65c5b0f9a96a7a)
21. Fix a memory leak that can occur following a failure to open error in the [CSV virtual table](csv.md)
22. Fix a long-standing problem wherein a corrupt schema on the [sqlite_sequence](fileformat2.md#seqtab) table used by [AUTOINCREMENT](autoinc.md) can lead to a crash. Ticket [d8dc2b3a58cd5dc2918a1](https://sqlite.org/src/info/d8dc2b3a58cd5dc29)
23. Fix the [json_each()](json1.md#jeach) function so that it returns valid results on its "fullkey" column when the input is a simple value rather than an array or object.
    **Hashes:**
24. SQLITE_SOURCE_ID: "2018-06-04 19:24:41 c7ee0833225bfd8c5ec2f9bf62b97c4e04d03bd9566366d5221ac8fb199a87ca"
25. SHA3-256 for sqlite3.c: 0d384704e1c66026228336d1e91771d295bf688c9c44c7a44f25a4c16c26ab3c

<span id="version_3_23_1"></span>

### 2018-04-10 (3.23.1)

1.  Fix two problems in the new [LEFT JOIN strength reduction optimization](optoverview.md#leftjoinreduction). Tickets [1e39b966ae9ee739](https://sqlite.org/src/info/1e39b966ae9ee739) and [fac496b61722daf2](https://sqlite.org/src/info/fac496b61722daf2).
2.  Fix misbehavior of the FTS5 xBestIndex method. Ticket [2b8aed9f7c9e61e8](https://sqlite.org/src/info/2b8aed9f7c9e61e8).
3.  Fix a harmless reference to an uninitialized virtual machine register. Ticket [093420fc0eb7cba7](https://sqlite.org/src/info/093420fc0eb7cba7).
4.  Fix the [CLI](cli.md) so that it builds with -DSQLITE_UNTESTABLE
5.  Fix the [eval.c](https://sqlite.org/src/file/ext/misc/eval.c) extension so that it works with [PRAGMA empty_result_callbacks=ON](pragma.md#pragma_empty_result_callbacks).
6.  Fix the [generate_series](series.md) virtual table so that it correctly returns no rows if any of its constraints are NULL.
7.  Performance enhancements in the parser.
    **Hashes:**
8.  SQLITE_SOURCE_ID: "2018-04-10 17:39:29 4bb2294022060e61de7da5c227a69ccd846ba330e31626ebcd59a94efd148b3b"
9.  SHA3-256 for sqlite3.c: 65750d1e506f416a0b0b9dd22d171379679c733e3460549754dc68c92705b5dc

<span id="version_3_23_0"></span>

### 2018-04-02 (3.23.0)

1.  Add the [sqlite3_serialize()](c3ref/serialize.md) and [sqlite3_deserialize()](c3ref/deserialize.md) interfaces when the [SQLITE_ENABLE_DESERIALIZE](compile.md#enable_deserialize) compile-time option is used.
2.  Recognize TRUE and FALSE as constants. (For compatibility, if there exist columns named "true" or "false", then the identifiers refer to the columns rather than Boolean constants.)
3.  Support operators IS TRUE, IS FALSE, IS NOT TRUE, and IS NOT FALSE.
4.  Added the [SQLITE_DBSTATUS_CACHE_SPILL](c3ref/c_dbstatus_options.md#sqlitedbstatuscachespill) option to [sqlite3_db_status()](c3ref/db_status.md) for reporting the number of cache spills that have occurred.
5.  The "alternate-form-2" flag ("!") on the [built-in printf](printf.md) implementation now causes string substitutions to measure the width and precision in characters instead of bytes.
6.  If the [xColumn](vtab.md#xcolumn) method in a [virtual table](vtab.md) implementation returns an error message using [sqlite3_result_error()](c3ref/result_blob.md) then give that error message preference over internally-generated messages.
7.  Added the -A command-line option to the [CLI](cli.md) to make it easier to manage [SQLite Archive files](sqlar.md).
8.  Add support for INSERT OR REPLACE, INSERT OR IGNORE, and UPDATE OR REPLACE in the [Zipfile virtual table](zipfile.md).
9.  Enhance the [sqlite3changeset_apply()](session/sqlite3changeset_apply.md) interface so that it is hardened against attacks from deliberately corrupted [changeset](sessionintro.md#changeset) objects.
10. Added the [sqlite3_normalize()](https://sqlite.org/src/file/ext/misc/normalize.c) extension function.
11. Query optimizer enhancements:
    1.  Improve the [omit-left-join optimization](optoverview.md#omitnoopjoin) so that it works in cases where the right-hand table is UNIQUE but not necessarily NOT NULL.
    2.  Improve the [push-down optimization](optoverview.md#pushdown) so that it works for many LEFT JOINs.
    3.  Add the [LEFT JOIN strength reduction optimization](optoverview.md#leftjoinreduction) that converts a LEFT JOIN into an ordinary JOIN if there exist terms in the WHERE clause that would prevent the extra all-NULL row of the LEFT JOIN from appearing in the output set.
    4.  Avoid unnecessary writes to the sqlite_sequence table when an [AUTOINCREMENT](autoinc.md) table is updated with an rowid that is less than the maximum.
12. Bug fixes:
    1.  Fix the parser to accept valid [row value](rowvalue.md) syntax. Ticket [7310e2fb3d046a5](https://sqlite.org/src/info/7310e2fb3d046a5)
    2.  Fix the query planner so that it takes into account dependencies in the arguments to table-valued functions in subexpressions in the WHERE clause. Ticket [80177f0c226ff54](https://sqlite.org/src/info/80177f0c226ff54)
    3.  Fix incorrect result with complex OR-connected WHERE and STAT4. Ticket [ec32177c99ccac2](https://sqlite.org/src/info/ec32177c99ccac2)
    4.  Fix potential corruption in [indexes on expressions](expridx.md) due to automatic datatype conversions. Ticket [343634942dd54ab](https://sqlite.org/src/info/343634942dd54ab)
    5.  Assertion fault in FTS4. Ticket [d6ec09eccf68cfc](https://sqlite.org/src/info/d6ec09eccf68cfc)
    6.  Incorrect result on the less-than operator in [row values](rowvalue.md). Ticket [f484b65f3d62305](https://sqlite.org/src/info/f484b65f3d62305)
    7.  Always interpret non-zero floating-point values as TRUE, even if the integer part is zero. Ticket [36fae083b450e3a](https://sqlite.org/src/info/36fae083b450e3a)
    8.  Fix an issue in the fsdir(PATH) [table-valued function](vtab.md#tabfunc2) to the [fileio.c](https://sqlite.org/src/file/ext/misc/fileio.c) extension, that caused a segfault if the fsdir() table was used as the inner table of a join. Problem reported on the mailing list and fixed by check-in [7ce4e71c1b7251be](https://sqlite.org/src/info/7ce4e71c1b7251be)
    9.  Issue an error rather instead of an assertion-fault or null-pointer dereference when the sqlite_master table is corrupted so that the sqlite_sequence table root page is really a btree-index page. Check-in [525deb7a67fbd647](https://sqlite.org/src/info/525deb7a67fbd647)
    10. Fix the [ANALYZE](lang_analyze.md) command so that it computes statistics on tables whose names begin with "sqlite". Check-in [0249d9aecf69948d](https://sqlite.org/src/info/0249d9aecf69948d)
13. Additional fixes for issues detected by [OSSFuzz](https://github.com/google/oss-fuzz):
    1.  Fix a possible infinite loop on VACUUM for corrupt database files. Check-in [27754b74ddf64](https://sqlite.org/src/info/27754b74ddf64)
    2.  Disallow [parameters](lang_expr.md#varparam) in the [WITH clause](lang_with.md) of triggers and views. Check-in [b918d4b4e546d](https://sqlite.org/src/info/b918d4b4e546d)
    3.  Fix a potential memory leak in [row value](rowvalue.md) processing. Check-in [2df6bbf1b8ca8](https://sqlite.org/src/info/2df6bbf1b8ca8)
    4.  Improve the performance of the [replace() SQL function](lang_corefunc.md#replace) for cases where there are many substitutions on megabyte-sized strings, in an attempt to avoid OSSFuzz timeouts during testing. Check-in [fab2c2b07b5d3](https://sqlite.org/src/info/fab2c2b07b5d3)
    5.  Provide an appropriate error message when the sqlite_master table contains a CREATE TABLE AS statement. Formerly this caused either an assertion fault or null pointer dereference. Problem found by OSSFuzz on the GDAL project. Check-in [d75e67654aa96](https://sqlite.org/src/info/d75e67654aa96)
    6.  Incorrect assert() statement removed. Check-in [823779d31eb09cda](https://sqlite.org/src/info/823779d31eb09cda).
    7.  Fix a problem with using the [LIKE optimization](optoverview.md#like_opt) on an [INTEGER PRIMARY KEY](lang_createtable.md#rowid). Check-in [b850dd159918af56](https://sqlite.org/src/info/b850dd159918af56).

    **Hashes:**
14. SQLITE_SOURCE_ID: "2018-04-02 11:04:16 736b53f57f70b23172c30880186dce7ad9baa3b74e3838cae5847cffb98f5cd2"
15. SHA3-256 for sqlite3.c: 4bed3dc2dc905ff55e2c21fd2725551fc0ca50912a9c96c6af712a4289cb24fa

<span id="version_3_22_0"></span>

### 2018-01-22 (3.22.0)

1.  The output of [sqlite3_trace_v2()](c3ref/trace_v2.md) now shows each individual SQL statement run within a trigger.
2.  Add the ability to read from [WAL mode](wal.md) databases even if the application lacks write permission on the database and its containing directory, as long as the -shm and -wal files exist in that directory.
3.  Added the [rtreecheck()](rtree.md#rtreecheck) scalar SQL function to the [R-Tree extension](rtree.md).
4.  Added the [sqlite3_vtab_nochange()](c3ref/vtab_nochange.md) and [sqlite3_value_nochange()](c3ref/value_blob.md) interfaces to help virtual table implementations optimize UPDATE operations.
5.  Added the [sqlite3_vtab_collation()](c3ref/vtab_collation.md) interface.
6.  Added support for the ["^" initial token syntax](fts5.md#carrotq) in FTS5.
7.  New extensions:
    1.  The [Zipfile virtual table](zipfile.md) can read and write a [ZIP Archive](https://en.wikipedia.org/wiki/Zip_(file_format)).
    2.  Added the fsdir(PATH) [table-valued function](vtab.md#tabfunc2) to the [fileio.c](https://sqlite.org/src/file/ext/misc/fileio.c) extension, for listing the files in a directory.
    3.  The [sqlite_btreeinfo](https://sqlite.org/src/file/ext/misc/btreeinfo.c) eponymous virtual table for introspecting and estimating the sizes of the btrees in a database.
    4.  The [Append VFS](https://sqlite.org/src/file/ext/misc/appendvfs.c) is a [VFS shim](vfs.md#shim) that allows an SQLite database to be appended to some other file. This allows (for example) a database to be appended to an executable that then opens and reads the database.
8.  Query planner enhancements:
    1.  The optimization that uses an index to quickly compute an aggregate min() or max() is extended to work with [indexes on expressions](expridx.md).
    2.  The decision of whether to implement a FROM-clause subquery as a co-routine or using [query flattening](optoverview.md#flattening) now considers whether the result set of the outer query is "complex" (if it contains functions or expression subqueries). A complex result set biases the decision toward the use of co-routines.
    3.  The planner avoids query plans that use indexes with unknown collating functions.
    4.  The planner omits unused LEFT JOINs even if they are not the right-most joins of a query.
9.  Other performance optimizations:
    1.  A smaller and faster implementation of text to floating-point conversion subroutine: sqlite3AtoF().
    2.  The [Lemon parser generator](lemon.md) creates a faster parser.
    3.  Use the strcspn() C-library routine to speed up the LIKE and GLOB operators.
10. Improvements to the [command-line shell](cli.md):
    1.  The ".schema" command shows the structure of virtual tables.
    2.  Added support for reading and writing [SQLite Archive](sqlar.md) files using the [.archive command](cli.md#sqlar).
    3.  Added the experimental [.expert command](cli.md#expert)
    4.  Added the ".eqp trigger" variant of the ".eqp" command
    5.  Enhance the ".lint fkey-indexes" command so that it works with [WITHOUT ROWID](withoutrowid.md) tables.
    6.  If the filename argument to the shell is a ZIP archive rather than an SQLite database, then the shell automatically opens that ZIP archive using the [Zipfile virtual table](zipfile.md).
    7.  Added the [edit() SQL function](cli.md#editfunc).
    8.  Added the [.excel command](cli.md#exexcel*) to simplify exporting database content to a spreadsheet.
    9.  Databases are opened using [Append VFS](https://sqlite.org/src/file/ext/misc/appendvfs.c) when the --append flag is used on the command line or with the .open command.
11. Enhance the [SQLITE_ENABLE_UPDATE_DELETE_LIMIT](compile.md#enable_update_delete_limit) compile-time option so that it works for [WITHOUT ROWID](withoutrowid.md) tables.
12. Provide the [sqlite_offset(X)](lang_corefunc.md#sqlite_offset) SQL function that returns the byte offset into the database file to the beginning of the record holding value X, when compiling with [-DSQLITE_ENABLE_OFFSET_SQL_FUNC](compile.md#enable_offset_sql_func).
13. Bug fixes:
    1.  Infinite loop on an UPDATE that uses an OR operator in the WHERE clause. Problem introduced with 3.17.0 and reported on the mailing list about one year later. Ticket [47b2581aa9bfecec](https://sqlite.org/src/info/47b2581aa9bfecec).
    2.  Incorrect query results when the skip-ahead-distinct optimization is used. Ticket [ef9318757b152e3a](https://sqlite.org/src/info/ef9318757b152e3a).
    3.  Incorrect query results on a join with a ORDER BY DESC. Ticket [123c9ba32130a6c9](https://sqlite.org/src/info/123c9ba32130a6c9).
    4.  Inconsistent result set column names between CREATE TABLE AS and a simple SELECT. Ticket [3b4450072511e621](https://sqlite.org/src/info/3b4450072511e621)
    5.  Assertion fault when doing REPLACE on an index on an expression. Ticket [dc3f932f5a147771](https://sqlite.org/src/info/dc3f932f5a147771)
    6.  Assertion fault when doing an IN operator on a constant index. Ticket [aa98619ad08ddcab](https://sqlite.org/src/info/aa98619ad08ddcab)

    **Hashes:**
14. SQLITE_SOURCE_ID: "2018-01-22 18:45:57 0c55d179733b46d8d0ba4d88e01a25e10677046ee3da1d5b1581e86726f2171d"
15. SHA3-256 for sqlite3.c: 206df47ebc49cd1710ac0dd716ce5de5854826536993f4feab7a49d136b85069

<span id="version_3_21_0"></span>

### 2017-10-24 (3.21.0)

1.  Take advantage of the atomic-write capabilities in the [F2FS filesystem](https://en.wikipedia.org/wiki/F2FS) when available, for greatly reduced transaction overhead. This currently requires the [SQLITE_ENABLE_BATCH_ATOMIC_WRITE](compile.md#enable_batch_atomic_write) compile-time option.
2.  Allow [ATTACH](lang_attach.md) and [DETACH](lang_detach.md) commands to work inside of a transaction.
3.  Allow [WITHOUT ROWID virtual tables](vtab.md#worid) to be writable if the PRIMARY KEY contains exactly one column.
4.  The "fsync()" that occurs after the header is written in a WAL reset now uses the sync settings for checkpoints. This means it will use a "fullfsync" on macs if [PRAGMA checkpoint_fullfsync](pragma.md#pragma_checkpoint_fullfsync) set on.
5.  The [sqlite3_sourceid()](c3ref/libversion.md) function tries to detect if the source code has been modified from what is checked into version control and if there are modifications, the last four characters of the version hash are shown as "alt1" or "alt2". The objective is to detect accidental and/or careless edits. A forger can subvert this feature.
6.  Improved de-quoting of column names for [CREATE TABLE AS](lang_createtable.md#createtabas) statements with an aggregate query on the right-hand side.
7.  Fewer "stat()" system calls issued by the unix VFS.
8.  Enhanced the [LIKE optimization](optoverview.md#like_opt) so that it works with an [ESCAPE](lang_expr.md#like) clause.
9.  Enhanced [PRAGMA integrity_check](pragma.md#pragma_integrity_check) and [PRAGMA quick_check](pragma.md#pragma_quick_check) to detect obscure row corruption that they were formerly missing. Also update both pragmas so that they return error text rather than SQLITE_CORRUPT when encountering corruption in [records](fileformat2.md#record_format).
10. The query planner now prefers to implement FROM-clause subqueries using [co-routines](optoverview.md#coroutines) rather using the [query flattener](optoverview.md#flattening) optimization. Support for the use of co-routines for subqueries may no longer be disabled.
11. Pass information about !=, IS, IS NOT, NOT NULL, and IS NULL constraints into the [xBestIndex](vtab.md#xbestindex) method of virtual tables.
12. Enhanced the [CSV virtual table](csv.md) so that it accepts the last row of input if the final new-line character is missing.
13. Remove the rarely-used "scratch" memory allocator. Replace it with the [SQLITE_CONFIG_SMALL_MALLOC](c3ref/c_config_covering_index_scan.md#sqliteconfigsmallmalloc) configuration setting that gives SQLite a hint that large memory allocations should be avoided when possible.
14. Added the [swarm virtual table](https://sqlite.org/src/file/ext/misc/unionvtab.c) to the existing union virtual table extension.
15. Added the [sqlite_dbpage virtual table](https://sqlite.org/src/file/src/dbpage.c) for providing direct access to pages of the database file. The source code is built into the [amalgamation](amalgamation.md) and is activated using the [-DSQLITE_ENABLE_DBPAGE_VTAB](compile.md#enable_dbpage_vtab) compile-time option.
16. Add a new type of fts5vocab virtual table - "instance" - that provides direct access to an FTS5 full-text index at the lowest possible level.
17. Remove a call to rand_s() in the Windows VFS since it was causing problems in Firefox on some older laptops.
18. The [src/shell.c](https://sqlite.org/src/finfo?name=src/shell.c) source code to the [command-line shell](cli.md) is no longer under version control. That file is now generated as part of the build process.
19. Miscellaneous [microoptimizations](cpu.md#microopt) reduce CPU usage by about 2.1%.
20. Bug fixes:
    1.  Fix a faulty assert() statement discovered by OSSFuzz. Ticket [cb91bf4290c211d](https://sqlite.org/src/info/cb91bf4290c211d)
    2.  Fix an obscure memory leak in [sqlite3_result_pointer()](c3ref/result_blob.md). Ticket [7486aa54b968e9b](https://sqlite.org/src/info/7486aa54b968e9b)
    3.  Avoid a possible use-after-free error by deferring schema resets until after the query planner has finished running. Ticket [be436a7f4587ce5](https://sqlite.org/src/info/be436a7f4587ce5)
    4.  Only use indexes-on-expressions to optimize ORDER BY or GROUP BY if the COLLATE is correct. Ticket [e20dd54ab0e4383](https://sqlite.org/src/info/e20dd54ab0e4383)
    5.  Fix an assertion fault that was coming up when the expression in an index-on-expressions is really a constant. Ticket [aa98619ad08ddca](https://sqlite.org/src/info/aa98619ad08ddca)
    6.  Fix an assertion fault that could occur following [PRAGMA reverse_unordered_selects](pragma.md#pragma_reverse_unordered_selects). Ticket [cb91bf4290c211d](https://sqlite.org/src/info/cb91bf4290c211d)
    7.  Fix a segfault that can occur for queries that use table-valued functions in an IN or EXISTS subquery. Ticket [b899b6042f97f5](https://sqlite.org/src/info/b899b6042f97f5)
    8.  Fix a potential integer overflow problem when compiling a particular horrendous common table expression. This was another problem discovered by OSSFuzz. Check-in [6ee8cb6ae5](https://sqlite.org/src/info/6ee8cb6ae5).
    9.  Fix a potential out-of-bound read when querying a corrupt database file, a problem detected by Natalie Silvanovich of Google Project Zero. Check-in [04925dee41a21f](https://sqlite.org/src/info/04925dee41a21f).

    **Hashes:**
21. SQLITE_SOURCE_ID: "2017-10-24 18:55:49 1a584e499906b5c87ec7d43d4abce641fdf017c42125b083109bc77c4de48827"
22. SHA3-256 for sqlite3.c: 84c181c0283d0320f488357fc8aab51898370c157601459ebee49d779036fe03

<span id="version_3_20_1"></span>

### 2017-08-24 (3.20.1)

1.  Fix a potential memory leak in the new [sqlite3_result_pointer()](c3ref/result_blob.md) interface. Ticket [7486aa54b968e9b5](https://sqlite.org/src/info/7486aa54b968e9b5).
    **Hashes:**
2.  SQLITE_SOURCE_ID: "2017-08-24 16:21:36 8d3a7ea6c5690d6b7c3767558f4f01b511c55463e3f9e64506801fe9b74dce34"
3.  SHA3-256 for sqlite3.c: 93b1a6d69b48dc39697d1d3a1e4c30b55da0bdd2cad0c054462f91081832954a

<span id="version_3_20_0"></span>

### 2017-08-01 (3.20.0)

1.  Update the text of error messages returned by [sqlite3_errmsg()](c3ref/errcode.md) for some error codes.
2.  Add new [pointer passing interfaces](bindptr.md).
3.  Backwards-incompatible changes to some extensions in order to take advantage of the improved security offered by the new [pointer passing interfaces](bindptr.md):
    1.  [Extending FTS5](fts5.md#extending_fts5) → requires [sqlite3_bind_pointer()](c3ref/bind_blob.md) to find the fts5_api pointer.
    2.  [carray(PTR,N)](carray.md) → requires [sqlite3_bind_pointer()](c3ref/bind_blob.md) to set the PTR parameter.
    3.  [remember(V,PTR)](https://sqlite.org/src/file/ext/misc/remember.c) → requires [sqlite3_bind_pointer()](c3ref/bind_blob.md) to set the PTR parameter.
4.  Added the [SQLITE_STMT virtual table](stmt.md) extension.
5.  Added the [COMPLETION extension](completion.md) - designed to suggest tab-completions for interactive user interfaces. This is a work in progress. Expect further enhancements in future releases.
6.  Added the [UNION virtual table](unionvtab.md) extension.
7.  The built-in [date and time functions](lang_datefunc.md) have been enhanced so that they can be used in [CHECK constraints](lang_createtable.md#ckconst), in [indexes on expressions](expridx.md), and in the WHERE clauses of [partial indexes](partialindex.md), provided that they do not use the 'now', 'localtime', or 'utc' keywords. [More information](deterministic.md#dtexception).
8.  Added the [sqlite3_prepare_v3()](c3ref/prepare.md) and [sqlite3_prepare16_v3()](c3ref/prepare.md) interfaces with the extra "prepFlags" parameters.
9.  Provide the [SQLITE_PREPARE_PERSISTENT](c3ref/c_prepare_dont_log.md#sqlitepreparepersistent) flag for [sqlite3_prepare_v3()](c3ref/prepare.md) and use it to limit [lookaside memory](malloc.md#lookaside) misuse by [FTS3](fts3.md), [FTS5](fts5.md), and the [R-Tree extension](rtree.md).
10. Added the [PRAGMA secure_delete=FAST](pragma.md#pragma_secure_delete) command. When secure_delete is set to FAST, old content is overwritten with zeros as long as that does not increase the amount of I/O. Deleted content might still persist on the [free-page list](fileformat2.md#freelist) but will be purged from all b-tree pages.
11. Enhancements to the [command-line shell](cli.md):
    1.  Add support for tab-completion using the [COMPLETION extension](completion.md), for both readline and linenoise.
    2.  Add the ".cd" command.
    3.  Enhance the "[.schema](cli.md#dschema)" command to show the schema of all attached databases.
    4.  Enhance "[.tables](cli.md#dtables)" so that it shows the schema names for all attached if the name is anything other than "main".
    5.  The "[.import](cli.md#csv)" command ignores an initial UTF-8 BOM.
    6.  Added the "--newlines" option to the "[.dump](cli.md#dump)" command to cause U+000a and U+000d characters to be output literally rather than escaped using the [replace()](lang_corefunc.md#replace) function.
12. Query planner enhancements:
    1.  When generating individual loops for each ORed term of an OR scan, move any constant WHERE expressions outside of the loop, as is done for top-level loops.
    2.  The query planner examines the values of bound parameters to help determine if a partial index is usable.
    3.  When deciding between two plans with the same estimated cost, bias the selection toward the one that does not use the sorter.
    4.  Evaluate WHERE clause constraints involving correlated subqueries last, in the hope that they never have be evaluated at all.
    5.  Do not use the [flattening optimization](optoverview.md#flattening) for a sub-query on the RHS of a LEFT JOIN if that subquery reads data from a [virtual table](vtab.md) as doing so prevents the query planner from creating [automatic indexes](optoverview.md#autoindex) on the results of the sub-query, which can slow down the query.
13. Add [SQLITE_STMTSTATUS_REPREPARE](c3ref/c_stmtstatus_counter.md#sqlitestmtstatusreprepare), [SQLITE_STMTSTATUS_RUN](c3ref/c_stmtstatus_counter.md#sqlitestmtstatusrun), and [SQLITE_STMTSTATUS_MEMUSED](c3ref/c_stmtstatus_counter.md#sqlitestmtstatusmemused) options for the [sqlite3_stmt_status()](c3ref/stmt_status.md) interface.
14. Provide [PRAGMA functions](pragma.md#pragfunc) for [PRAGMA integrity_check](pragma.md#pragma_integrity_check), [PRAGMA quick_check](pragma.md#pragma_quick_check), and [PRAGMA foreign_key_check](pragma.md#pragma_foreign_key_check).
15. Add the -withoutnulls option to the [TCL interface eval method](tclsqlite.md#eval).
16. Enhance the [sqlite3_analyzer.exe](sqlanalyze.md) utility program so that it shows the number of bytes of metadata on btree pages.
17. The [SQLITE_DBCONFIG_ENABLE_QPSG](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableqpsg) run-time option and the [SQLITE_ENABLE_QPSG](compile.md#enable_qpsg) compile-time option enable the [query planner stability guarantee](queryplanner-ng.md#qpstab). See also ticket [892fc34f173e99d8](https://sqlite.org/src/info/892fc34f173e99d8)
18. Miscellaneous optimizations result in a 2% reduction in [CPU cycles used](cpu.md).
    **Bug Fixes:**
19. Fix the behavior of [sqlite3_column_name()](c3ref/column_name.md) for queries that use the [flattening optimization](optoverview.md#flattening) so that the result is consistent with other queries that do not use that optimization, and with PostgreSQL, MySQL, and SQLServer. Ticket [de3403bf5ae](https://sqlite.org/src/info/de3403bf5ae).
20. Fix the query planner so that it knows not to use [automatic indexes](optoverview.md#autoindex) on the right table of LEFT JOIN if the WHERE clause uses the [IS operator](lang_expr.md#isisnot). Fix for [ce68383bf6aba](https://sqlite.org/src/info/ce68383bf6aba).
21. Ensure that the query planner knows that any column of a [flattened](optoverview.md#flattening) LEFT JOIN can be NULL even if that column is labeled with "NOT NULL". Fix for ticket [892fc34f173e99d8](https://sqlite.org/src/info/892fc34f173e99d8).
22. Fix rare false-positives in [PRAGMA integrity_check](pragma.md#pragma_integrity_check) when run on a database connection with [attached databases](lang_attach.md). Ticket [a4e06e75a9ab61a12](https://sqlite.org/src/info/a4e06e75a9ab61a12)
23. Fix a bug (discovered by OSSFuzz) that causes an assertion fault if certain dodgy CREATE TABLE declarations are used. Ticket [bc115541132dad136](https://sqlite.org/src/info/bc115541132dad136)
    **Hashes:**
24. SQLITE_SOURCE_ID: "2017-08-01 13:24:15 9501e22dfeebdcefa783575e47c60b514d7c2e0cad73b2a496c0bc4b680900a8"
25. SHA3-256 for sqlite3.c: 79b7f3b977360456350219cba0ba0e5eb55910565eab68ea83edda2f968ebe95

<span id="version_3_18_2"></span>

### 2017-06-17 (3.18.2)

1.  Fix a bug that might cause duplicate output rows when an IN operator is used in the WHERE clause. Ticket [61fe9745](https://sqlite.org/src/info/61fe9745).
    **Hashes:**
2.  SQLITE_SOURCE_ID: "2017-06-17 09:59:36 036ebf729e4b21035d7f4f8e35a6f705e6bf99887889e2dc14ebf2242e7930dd"
3.  SHA3-256 for sqlite3.c: b0bd014f2776b9f9508a3fc6432f70e2436bf54475369f88f0aeef75b0eec93e

<span id="version_3_18_1"></span>

### 2017-06-16 (3.18.1)

1.  Fix a bug associated with [auto_vacuum](pragma.md#pragma_auto_vacuum) that can lead to database corruption. The bug was introduced in [version 3.16.0](#version_3_16_0) (2017-01-02). Ticket [fda22108](https://sqlite.org/src/info/fda22108).
    **Hashes:**
2.  SQLITE_SOURCE_ID: "2017-06-16 13:41:15 77bb46233db03a3338bacf7e56f439be3dfd1926ea0c44d252eeafa7a7b31c06"
3.  SHA3-256 for sqlite3.c: 334eaf776db9d09a4e69d6012c266bc837107edc2c981739ef82081cb11c5723

<span id="version_3_19_3"></span>

### 2017-06-08 (3.19.3)

1.  Fix a bug associated with [auto_vacuum](pragma.md#pragma_auto_vacuum) that can lead to database corruption. The bug was introduced in [version 3.16.0](#version_3_16_0) (2017-01-02). Ticket [fda22108](https://sqlite.org/src/info/fda22108).
    **Hashes:**
2.  SQLITE_SOURCE_ID: "2017-06-08 14:26:16 0ee482a1e0eae22e08edc8978c9733a96603d4509645f348ebf55b579e89636b"
3.  SHA3-256 for sqlite3.c: 368f1d31272b1739f804bcfa5485e5de62678015c4adbe575003ded85c164bb8

<span id="version_3_19_2"></span>

### 2017-05-25 (3.19.2)

1.  Fix more bugs in the LEFT JOIN [flattening optimization](optoverview.md#flattening). Ticket [7fde638e94287d2c](https://sqlite.org/src/info/7fde638e94287d2c).
    **Hashes:**
2.  SQLITE_SOURCE_ID: "2017-05-25 16:50:27 edb4e819b0c058c7d74d27ebd14cc5ceb2bad6a6144a486a970182b7afe3f8b9"
3.  SHA3-256 for sqlite3.c: 1be0c457869c1f7eba58c3b5097b9ec307a15be338308bee8e5be8570bcf5d1e

<span id="version_3_19_1"></span>

### 2017-05-24 (3.19.1)

1.  Fix a bug in the LEFT JOIN [flattening optimization](optoverview.md#flattening). Ticket [cad1ab4cb7b0fc](https://sqlite.org/src/info/cad1ab4cb7b0fc).
2.  Remove a surplus semicolon that was causing problems for older versions of MSVC.
    **Hashes:**
3.  SQLITE_SOURCE_ID: "2017-05-24 13:08:33 f6d7b988f40217821a382bc298180e9e6794f3ed79a83c6ef5cae048989b3f86"
4.  SHA3-256 for sqlite3.c: 996b2aff37b6e0c6663d0312cd921bbdf6826c989cbbb07dadde5e9672889bca

<span id="version_3_19_0"></span>

### 2017-05-22 (3.19.0)

1.  The [SQLITE_READ](c3ref/c_alter_table.md) [authorizer callback](c3ref/set_authorizer.md) is invoked once with a column name that is an empty string for every table referenced in a query from which no columns are extracted.
2.  When using an index on an expression, try to use expression values already available in the index, rather than loading the original columns and recomputing the expression.
3.  Enhance the [flattening optimization](optoverview.md#flattening) so that it is able to flatten views on the right-hand side of a LEFT JOIN.
4.  Use [replace()](lang_corefunc.md#replace) instead of [char()](lang_corefunc.md#char) for escaping newline and carriage-return characters embedded in strings in the .dump output from the [command-line shell](cli.md).
5.  Avoid unnecessary foreign key processing in UPDATE statements that do not touch the columns that are constrained by the foreign keys.
6.  On a DISTINCT query that uses an index, try to skip ahead to the next distinct entry using the index rather than stepping through rows, when an appropriate index is available.
7.  Avoid unnecessary invalidation of [sqlite3_blob](c3ref/blob.md) handles when making changes to unrelated tables.
8.  Transfer any terms of the HAVING clause that use only columns mentioned in the GROUP BY clause over to the WHERE clause for faster processing.
9.  Reuse the same materialization of a VIEW if that VIEW appears more than once in the same query.
10. Enhance [PRAGMA integrity_check](pragma.md#pragma_integrity_check) so that it identifies tables that have two or more rows with the same [rowid](lang_createtable.md#rowid).
11. Enhance the [FTS5](fts5.md) query syntax so that [column filters](fts5.md#fts5_column_filters) may be applied to arbitrary expressions.
12. Enhance the [json_extract()](json1.md#jex) function to cache and reuse parses of JSON input text.
13. Added the [anycollseq.c](https://sqlite.org/src/file/ext/misc/anycollseq.c) [loadable extension](loadext.md) that allows a generic SQLite database connection to read a schema that contains unknown and/or application-specific [collating sequences](datatype3.md#collation).
    **Bug Fixes:**
14. Fix a problem in [REPLACE](lang_replace.md) that can result in a corrupt database containing two or more rows with the same [rowid](lang_createtable.md#rowid). Fix for ticket [f68dc596c4e6018d](https://sqlite.org/src/info/f68dc596c4e6018d).
15. Fix a problem in [PRAGMA integrity_check](pragma.md#pragma_integrity_check) that was causing a subsequent [VACUUM](lang_vacuum.md) to behave suboptimally.
16. Fix the [PRAGMA foreign_key_check](pragma.md#pragma_foreign_key_check) command so that it works correctly with foreign keys on [WITHOUT ROWID](withoutrowid.md) tables.
17. Fix a bug in the b-tree logic that can result in incorrect duplicate answers for IN operator queries. Ticket [61fe9745](https://sqlite.org/src/info/61fe9745)
18. Disallow leading zeros in numeric constants in JSON. Fix for ticket [b93be8729a895a528e2](https://sqlite.org/src/info/b93be8729a895a528e2).
19. Disallow control characters inside of strings in JSON. Fix for ticket [6c9b5514077fed34551](https://sqlite.org/src/info/6c9b5514077fed34551).
20. Limit the depth of recursion for JSON objects and arrays in order to avoid excess stack usage in the recursive descent parser. Fix for ticket [981329adeef51011052](https://sqlite.org/src/info/981329adeef51011052).
    **Hashes:**
21. SQLITE_SOURCE_ID: "2017-05-22 13:58:13 28a94eb282822cad1d1420f2dad6bf65e4b8b9062eda4a0b9ee8270b2c608e40"
22. SHA3-256 for sqlite3.c: c30326aa1a9cc342061b755725eac9270109acf878bc59200dd4b1cea6bc2908

<span id="version_3_18_0"></span>

### 2017-03-30 (3.18.0)

1.  Added the [PRAGMA optimize](pragma.md#pragma_optimize) command
2.  The SQLite version identifier returned by the [sqlite_source_id()](lang_corefunc.md#sqlite_source_id) SQL function and the [sqlite3_sourceid()](c3ref/libversion.md) C API and found in the [SQLITE_SOURCE_ID](c3ref/c_scm_branch.md) macro is now a 64-digit SHA3-256 hash instead of a 40-digit SHA1 hash.
3.  Added the [json_patch()](json1.md#jpatch) SQL function to the [JSON1 extension](json1.md).
4.  Enhance the [LIKE optimization](optoverview.md#like_opt) so that it works for arbitrary expressions on the left-hand side as long as the LIKE pattern on the right-hand side does not begin with a digit or minus sign.
5.  Added the [sqlite3_set_last_insert_rowid()](c3ref/set_last_insert_rowid.md) interface and use the new interface in the [FTS3](fts3.md), [FTS4](fts3.md#fts4), and [FTS5](fts5.md) extensions to ensure that the [sqlite3_last_insert_rowid()](c3ref/last_insert_rowid.md) interface always returns reasonable values.
6.  Enhance [PRAGMA integrity_check](pragma.md#pragma_integrity_check) and [PRAGMA quick_check](pragma.md#pragma_quick_check) so that they verify [CHECK constraints](lang_createtable.md#ckconst).
7.  Enhance the query plans for joins to detect empty tables early and halt without doing unnecessary work.
8.  Enhance the [sqlite3_mprintf()](c3ref/mprintf.md) family of interfaces and the [printf SQL function](lang_corefunc.md#printf) to put comma separators at the thousands marks for integers, if the "," format modifier is used in between the "%" and the "d" (example: "%,d").
9.  Added the -D[SQLITE_MAX_MEMORY](compile.md#max_memory)=*N* compile-time option.
10. Added the [.sha3sum dot-command](cli.md#sha3sum) and the [.selftest dot-command](cli.md#selftest) to the [command-line shell](cli.md)
11. Begin enforcing [SQLITE_LIMIT_VDBE_OP](c3ref/c_limit_attached.md#sqlitelimitvdbeop). This can be used, for example, to prevent excessively large prepared statements in systems that accept SQL queries from untrusted users.
12. Various performance improvements.
    **Bug Fixes:**
13. Ensure that indexed expressions with collating sequences are handled correctly. Fix for ticket [eb703ba7b50c1a5](https://sqlite.org/src/info/eb703ba7b50c1a5).
14. Fix a bug in the 'start of ...' modifiers for the [date and time functions](lang_datefunc.md). Ticket [6097cb92745327a1](https://sqlite.org/src/info/6097cb92745327a1)
15. Fix a potential segfault in complex recursive triggers, resulting from a bug in the OP_Once opcode introduced as part of a performance optimization in version 3.15.0. Ticket [06796225f59c057c](https://sqlite.org/src/info/06796225f59c057c)
16. In the [RBU extension](rbu.md), add extra sync operations to avoid the possibility of corruption following a power failure.
17. The [sqlite3_trace_v2()](c3ref/trace_v2.md) output for nested SQL statements should always begin with a "--" comment marker.
    **Hashes:**
18. SQLITE_SOURCE_ID: "2017-03-28 18:48:43 424a0d380332858ee55bdebc4af3789f74e70a2b3ba1cf29d84b9b4bcf3e2e37"
19. SHA3-256 for sqlite3.c: cbf322df1f76be57fb3be84f3da1fc71d1d3dfdb7e7c2757fb0ff630b3bc2e5d

<span id="version_3_17_0"></span>

### 2017-02-13 (3.17.0)

1.  Approximately 25% better performance from the [R-Tree extension](rtree.md).
    1.  Uses compiler built-ins (ex: \_\_builtin_bswap32() or \_byteswap_ulong()) for byteswapping when available.
    2.  Uses the [sqlite3_blob](c3ref/blob.md) key/value access object instead of SQL for pulling content out of R-Tree nodes
    3.  Other miscellaneous enhancements such as loop unrolling.
2.  Add the [SQLITE_DEFAULT_LOOKASIDE](compile.md#default_lookaside) compile-time option.
3.  Increase the default [lookaside](malloc.md#lookaside) size from 512,125 to 1200,100 as this provides better performance while only adding 56KB of extra memory per connection. Memory-sensitive applications can restore the old default at compile-time, start-time, or run-time.
4.  Use compiler built-ins \_\_builtin_sub_overflow(), \_\_builtin_add_overflow(), and \_\_builtin_mul_overflow() when available. (All compiler built-ins can be omitted with the [SQLITE_DISABLE_INTRINSIC](compile.md#disable_intrinsic) compile-time option.)
5.  Added the [SQLITE_ENABLE_NULL_TRIM](compile.md#enable_null_trim) compile-time option, which can result in significantly smaller database files for some applications, at the risk of being incompatible with older versions of SQLite.
6.  Change [SQLITE_DEFAULT_PCACHE_INITSZ](compile.md#default_pcache_initsz) from 100 to 20, for improved performance.
7.  Added the SQLITE_UINT64_TYPE compile-time option as an analog to SQLITE_INT64_TYPE.
8.  Perform some [UPDATE](lang_update.md) operations in a single pass instead of in two passes.
9.  Enhance the [session extension](sessionintro.md) to support [WITHOUT ROWID](withoutrowid.md) tables.
10. Fixed performance problems and potential stack overflows when creating [views](lang_createview.md) from multi-row VALUES clauses with hundreds of thousands of rows.
11. Added the [sha1.c](https://sqlite.org/src/file/ext/misc/sha1.c) extension.
12. In the [command-line shell](cli.md), enhance the ".mode" command so that it restores the default column and row separators for modes "line", "list", "column", and "tcl".
13. Enhance the [SQLITE_DIRECT_OVERFLOW_READ](compile.md#direct_overflow_read) option so that it works in [WAL mode](wal.md) as long as the pages being read are not in the WAL file.
14. Enhance the [Lemon parser generator](lemon.md) so that it can store the parser object as a stack variable rather than allocating space from the heap and make use of that enhancement in the [amalgamation](amalgamation.md).
15. Other performance improvements. Uses about [6.5% fewer CPU cycles](cpu.md).
    **Bug Fixes:**
16. Throw an error if the ON clause of a LEFT JOIN references tables to the right of the ON clause. This is the same behavior as PostgreSQL. Formerly, SQLite silently converted the LEFT JOIN into an INNER JOIN. Fix for ticket [25e335f802dd](https://sqlite.org/src/info/25e335f802dd).
17. Use the correct affinity for columns of automatic indexes. Ticket [7ffd1ca1d2ad4ec](https://sqlite.org/src/info/7ffd1ca1d2ad4ec).
18. Ensure that the [sqlite3_blob_reopen()](c3ref/blob_reopen.md) interface can correctly handle short rows. Fix for ticket [e6e962d6b0f06f46e](https://sqlite.org/src/info/e6e962d6b0f06f46e).
    **Hashes:**
19. SQLITE_SOURCE_ID: "2017-02-13 16:02:40 ada05cfa86ad7f5645450ac7a2a21c9aa6e57d2c"
20. SHA1 for sqlite3.c: cc7d708bb073c44102a59ed63ce6142da1f174d1

<span id="version_3_16_2"></span>

### 2017-01-06 (3.16.2)

1.  Fix the [REPLACE](lang_replace.md) statement for [WITHOUT ROWID](withoutrowid.md) tables that lack secondary indexes so that it works correctly with triggers and foreign keys. This was a new bug caused by performance optimizations added in version 3.16.0. Ticket [30027b613b4](https://sqlite.org/src/info/30027b613b4)
2.  Fix the [sqlite3_value_text()](c3ref/value_blob.md) interface so that it correctly translates content generated by [zeroblob()](lang_corefunc.md#zeroblob) into a string of all 0x00 characters. This is a long-standing issue discovered after the 3.16.1 release by [OSS-Fuzz](https://github.com/google/oss-fuzz)
3.  Fix the bytecode generator to deal with a subquery in the FROM clause that is itself a UNION ALL where one side of the UNION ALL is a view that contains an ORDER BY. This is a long-standing issue that was discovered after the release of 3.16.1. See ticket [190c2507](https://sqlite.org/src/info/190c2507).
4.  Adjust the [sqlite3_column_count()](c3ref/column_count.md) API so it more often returns the same values for [PRAGMA](pragma.md#syntax) statements as it did in prior releases, to minimize disruption to applications that might be using that interface in unexpected ways.
    **Hashes:**
5.  SQLITE_SOURCE_ID: "2017-01-06 16:32:41 a65a62893ca8319e89e48b8a38cf8a59c69a8209"
6.  SHA1 for sqlite3.c: 2bebdc3f24911c0d12b6d6c0123c3f84d6946b08

<span id="version_3_16_1"></span>

### 2017-01-03 (3.16.1)

1.  Fix a bug concerning the use of [row values](rowvalue.md) within [triggers](lang_createtrigger.md) (see ticket [8c9458e7](https://sqlite.org/src/info/8c9458e7)) that was in version 3.15.0 but was not reported until moments after the 3.16.0 release was published.
    **Hashes:**
2.  SQLITE_SOURCE_ID: "2017-01-03 18:27:03 979f04392853b8053817a3eea2fc679947b437fd"
3.  SHA1 for sqlite3.c: 354f6223490b30fd5320b4066b1535e4ce33988d

<span id="version_3_16_0"></span>

### 2017-01-02 (3.16.0)

1.  Uses 9% fewer CPU cycles. (See the [CPU performance measurement](cpu.md) report for details on how this performance increase was computed.)
2.  Added experimental support for [PRAGMA functions](pragma.md#pragfunc).
3.  Added the [SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE](c3ref/c_dbconfig_defensive.md#sqlitedbconfignockptonclose) option to [sqlite3_db_config()](c3ref/db_config.md).
4.  Enhance the [date and time functions](lang_datefunc.md) so that the 'unixepoch' modifier works for the full span of supported dates.
5.  Changed the default configuration of the [lookaside memory allocator](malloc.md#lookaside) from 500 slots of 128 bytes each into 125 slots of 512 bytes each.
6.  Enhanced "WHERE x NOT NULL" [partial indexes](partialindex.md) so that they are usable if the "x" column appears in a LIKE or GLOB operator.
7.  Enhanced [sqlite3_interrupt()](c3ref/interrupt.md) so that it interrupts [checkpoint](wal.md#ckpt) operations that are in process.
8.  Enhanced the [LIKE](lang_expr.md#like) and [GLOB](lang_expr.md#glob) matching algorithm to be faster for cases when the pattern contains multiple wildcards.
9.  Added the [SQLITE_FCNTL_WIN32_GET_HANDLE](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlwin32gethandle) file control opcode.
10. Added ".mode quote" to the [command-line shell](cli.md).
11. Added ".lint fkey-indexes" to the [command-line shell](cli.md).
12. Added the [.imposter dot-command](imposter.md#dotimposter) to the [command-line shell](cli.md).
13. Added the [remember(V,PTR)](https://sqlite.org/src/file/ext/misc/remember.c) SQL function as a [loadable extension](loadext.md).
14. Rename the [SQLITE_OMIT_BUILTIN_TEST](compile.md#omit_builtin_test) compile-time option to [SQLITE_UNTESTABLE](compile.md#untestable) to better reflect the implications of using it.
    **Bug Fixes:**
15. Fix a long-standing bug in the query planner that caused incorrect results on a LEFT JOIN where the left-hand table is a subquery and the join constraint is a bare column name coming from the left-hand subquery. Ticket [2df0107b](https://sqlite.org/src/info/2df0107b).
16. Correctly handle the integer literal -0x8000000000000000 in the query planner.
    **Hashes:**
17. SQLITE_SOURCE_ID: "2017-01-02 11:57:58 04ac0b75b1716541b2b97704f4809cb7ef19cccf"
18. SHA1 for sqlite3.c: e2920fb885569d14197c9b7958e6f1db573ee669

<span id="version_3_15_2"></span>

### 2016-11-28 (3.15.2)

1.  Multiple bug fixes to the [row value](rowvalue.md) logic that was introduced in version 3.15.0.
2.  Fix a NULL pointer dereference in ATTACH/DETACH following a maliciously constructed syntax error. Ticket [2f1b168ab4d4844](https://sqlite.org/src/info/2f1b168ab4d4844).
3.  Fix a crash that can occur following an out-of-memory condition in the built-in [instr()](lang_corefunc.md#instr) function.
4.  In the [JSON extension](json1.md), fix the JSON validator so that it correctly rejects invalid backslash escapes within strings.
    **Hashes:**
5.  SQLITE_SOURCE_ID: "2016-11-28 19:13:37 bbd85d235f7037c6a033a9690534391ffeacecc8"
6.  SHA1 for sqlite3.c: 06d77b42a3e70609f8d4bbb97caf53652f1082cb

<span id="version_3_15_1"></span>

### 2016-11-04 (3.15.1)

1.  Added [SQLITE_FCNTL_WIN32_GET_HANDLE](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlwin32gethandle) file control opcode.
2.  Fix the [VACUUM](lang_vacuum.md) command so that it spills excess content to disk rather than holding everything in memory, and possible causing an out-of-memory error for larger database files. This fixes an issue introduced by version 3.15.0.
3.  Fix a case (present since 3.8.0 - 2013-08-26) where OR-connected terms in the ON clause of a LEFT JOIN might cause incorrect results. Ticket [34a579141b2c5ac](https://sqlite.org/src/info/34a579141b2c5ac).
4.  Fix a case where the use of [row values](rowvalue.md) in the ON clause of a LEFT JOIN might cause incorrect results. Ticket [fef4bb4bd9185ec8f](https://sqlite.org/src/info/fef4bb4bd9185ec8f).
    **Hashes:**
5.  SQLITE_SOURCE_ID: "2016-11-04 12:08:49 1136863c76576110e710dd5d69ab6bf347c65e36"
6.  SHA1 for sqlite3.c: e7c26a7be3e431dd06898f8d262c4ef240c07366

<span id="version_3_15_0"></span>

### 2016-10-14 (3.15.0)

1.  Added support for [row values](rowvalue.md).
2.  Allow [deterministic SQL functions](deterministic.md) in the WHERE clause of a [partial index](partialindex.md).
3.  Added the "[modeof=*filename*](uri.md#urimodeof)" URI parameter on the unix VFS
4.  Added support for [SQLITE_DBCONFIG_MAINDBNAME](c3ref/c_dbconfig_defensive.md#sqlitedbconfigmaindbname).
5.  Added the ability to [VACUUM](lang_vacuum.md) an [ATTACH-ed](lang_attach.md) database.
6.  Enhancements to the [command-line shell](cli.md):
    1.  Add the ".testcase" and ".check" [dot-commands](cli.md#dotcmd).
    2.  Added the --new option to the ".open" dot-command, causing any prior content in the database to be purged prior to opening.
7.  Enhance the [fts5vocab](fts5.md#the_fts5vocab_virtual_table_module) virtual table to handle "ORDER BY term" efficiently.
8.  Miscellaneous micro-optimizations reduce CPU usage by more than 7% on common workloads. Most optimization in this release has been on the front-end ([sqlite3_prepare_v2()](c3ref/prepare.md)).
    **Bug Fixes:**
9.  The multiply operator now correctly detects 64-bit integer overflow and promotes to floating point in all corner-cases. Fix for ticket [1ec41379c9c1e400](https://sqlite.org/src/info/1ec41379c9c1e400).
10. Correct handling of columns with redundant unique indexes when those columns are used on the LHS of an [IN operator](lang_expr.md#in_op). Fix for ticket [0eab1ac759](https://sqlite.org/src/info/0eab1ac759).
11. Skip NULL entries on range queries in [indexes on expressions](expridx.md). Fix for ticket [4baa46491212947](https://sqlite.org/src/tktview/4baa46491212947).
12. Ensure that the [AUTOINCREMENT](autoinc.md) counters in the sqlite_sequence table are initialized doing "Xfer Optimization" on "INSERT ... SELECT" statements. Fix for ticket [7b3328086a5c116c](https://sqlite.org/src/info/7b3328086a5c116c).
13. Make sure the ORDER BY LIMIT optimization (from check-in [559733b09e](https://sqlite.org/src/info/559733b09e9630fa)) works with IN operators on INTEGER PRIMARY KEYs. Fix for ticket [96c1454c](https://sqlite.org/src/info/96c1454cbfd9509)
    **Hashes:**
14. SQLITE_SOURCE_ID: "2016-10-14 10:20:30 707875582fcba352b4906a595ad89198d84711d8"
15. SHA1 for sqlite3.c: fba106f8f6493c66eeed08a2dfff0907de54ae76

<span id="version_3_14_2"></span>

### 2016-09-12 (3.14.2)

1.  Improved support for using the STDCALL calling convention in winsqlite3.dll.
2.  Fix the [sqlite3_trace_v2()](c3ref/trace_v2.md) interface so that it is disabled if either the callback or the mask arguments are zero, in accordance with the documentation.
3.  Fix commenting errors and improve the comments generated on [EXPLAIN](lang_explain.md) listings when the [-DSQLITE_ENABLE_EXPLAIN_COMMENTS](compile.md#enable_explain_comments) compile-time option is used.
4.  Fix the ".read" command in the [command-line shell](cli.md) so that it understands that its input is not interactive.
5.  Correct affinity computations for a SELECT on the RHS of an IN operator. Fix for ticket [199df4168c](https://sqlite.org/src/info/199df4168c).
6.  The ORDER BY LIMIT optimization is not valid unless the inner-most IN operator loop is actually used by the query plan. Fix for ticket [0c4df46116e90f92](https://sqlite.org/src/info/0c4df46116e90f92).
7.  Fix an internal code generator problem that was causing some [DELETE](lang_delete.md) operations to no-op. Ticket [ef360601](https://sqlite.org/src/info/ef360601)
    **Hashes:**
8.  SQLITE_SOURCE_ID: "2016-09-12 18:50:49 29dbef4b8585f753861a36d6dd102ca634197bd6"
9.  SHA1 for sqlite3.c: bcc4a1989db45e7f223191f2d0f66c1c28946383

<span id="version_3_14_1"></span>

### 2016-08-11 (3.14.1)

1.  A performance enhancement to the page-cache "truncate" operation reduces [COMMIT](lang_transaction.md) time by dozens of milliseconds on systems with a large [page cache](pragma.md#pragma_cache_size).
2.  Fix to the --rbu option of [sqldiff](sqldiff.md).
    **Hashes:**
3.  SQLITE_SOURCE_ID: "2016-08-11 18:53:32 a12d8059770df4bca59e321c266410344242bf7b"
4.  SHA1 for sqlite3.c: d545b24892278272ce4e40e0567d69c8babf12ea

<span id="version_3_14"></span>

### 2016-08-08 (3.14)

1.  <div style="width:280px;float:right;padding:10px;margin:0px 10px;">

    <img src="images/sqlitepie.jpg" width="280" height="250" />\
    Celebrating the SQLite "π release" with a home-baked pie.

2.  Added support for [WITHOUT ROWID virtual tables](vtab.md#worid).

3.  Improved the query planner so that the [OR optimization](optoverview.md#or_opt) can be used on [virtual tables](vtab.md) even if one or more of the disjuncts use the [LIKE](lang_expr.md#like), [GLOB](lang_expr.md#glob), [REGEXP](lang_expr.md#regexp), [MATCH](lang_expr.md#match) operators.

4.  Added the [CSV virtual table](csv.md) for reading [RFC 4180](https://www.ietf.org/rfc/rfc4180.txt) formatted comma-separated value files.

5.  Added the [carray() table-valued function](carray.md) extension.

6.  Enabled [persistent loadable extensions](loadext.md#persist) using the new [SQLITE_OK_LOAD_PERMANENTLY](rescode.md#ok_load_permanently) return code from the extension entry point.

7.  Added the [SQLITE_DBSTATUS_CACHE_USED_SHARED](c3ref/c_dbstatus_options.md#sqlitedbstatuscacheusedshared) option to [sqlite3_db_status()](c3ref/db_status.md).

8.  Add the [vfsstat.c](https://sqlite.org/src/artifact?ci=trunk&filename=ext/misc/vfsstat.c) loadable extension - a VFS shim that measures I/O together with an [eponymous virtual table](vtab.md#epovtab) that provides access to the measurements.

9.  Improved algorithm for running queries with both an ORDER BY and a LIMIT where only the inner-most loop naturally generates rows in the correct order.

10. Enhancements to [Lemon parser generator](lemon.md), so that it generates a faster parser.

11. The [PRAGMA compile_options](pragma.md#pragma_compile_options) command now attempts to show the version number of the compiler that generated the library.

12. Enhance [PRAGMA table_info](pragma.md#pragma_table_info) so that it provides information about [eponymous virtual tables](vtab.md#epovtab).

13. Added the "win32-none" VFS, analogous to the "unix-none" VFS, that works like the default "win32" VFS except that it ignores all file locks.

14. The query planner uses a full scan of a [partial index](partialindex.md) instead of a full scan of the main table, in cases where that makes sense.

15. Allow [table-valued functions](vtab.md#tabfunc2) to appear on the right-hand side of an [IN operator](lang_expr.md#in_op).

16. Created the [dbhash.exe](dbhash.md) command-line utility.

17. Added two new C-language interfaces: [sqlite3_expanded_sql()](c3ref/expanded_sql.md) and [sqlite3_trace_v2()](c3ref/trace_v2.md). These new interfaces subsume the functions of [sqlite3_trace()](c3ref/profile.md) and [sqlite3_profile()](c3ref/profile.md) which are now deprecated.

18. Added the [json_quote()](json1.md#jquote) SQL function to [the json1 extension](json1.md).

19. Disable the [authorizer callback](c3ref/set_authorizer.md) while reparsing the schema.

20. Added the [SQLITE_ENABLE_UNKNOWN_SQL_FUNCTION](compile.md#enable_unknown_sql_function) compile-time option and turned that option on by default when building the [command-line shell](cli.md).
    **Bug Fixes:**

21. Fix the [ALTER TABLE](lang_altertable.md) command so that it does not corrupt [descending indexes](lang_createindex.md#descidx) when adding a column to a [legacy file format](pragma.md#pragma_legacy_file_format) database. Ticket [f68bf68513a1c15f](https://sqlite.org/src/info/f68bf68513a1c15f)

22. Fix a NULL-pointer dereference/crash that could occurs when a transitive WHERE clause references a non-existent collating sequence. Ticket [e8d439c77685eca6](https://sqlite.org/src/info/e8d439c77685eca6).

23. Improved the cost estimation for an index scan which includes a WHERE clause that can be partially or fully evaluated using columns in the index and without having to do a table lookup. This fixes a performance regression that occurred for some obscure queries following the ORDER BY LIMIT optimization introduced in [version 3.12.0](#version_3_12_0).
    **Hashes:**

24. SQLITE_SOURCE_ID: "2016-08-08 13:40:27 d5e98057028abcf7217d0d2b2e29bbbcdf09d6de"

25. SHA1 for sqlite3.c: 234a3275d03a287434ace3ccdf1afb208e6b0e92

<span id="version_3_13_0"></span>

### 2016-05-18 (3.13.0)

1.  Postpone I/O associated with TEMP files for as long as possible, with the hope that the I/O can ultimately be avoided completely.

2.  Merged the [session](sessionintro.md) extension into trunk.

3.  Added the ".auth ON\|OFF" command to the [command-line shell](cli.md).

4.  Added the "--indent" option to the ".schema" and ".fullschema" commands of the [command-line shell](cli.md), to turn on pretty-printing.

5.  Added the ".eqp full" option to the [command-line shell](cli.md), that does both [EXPLAIN](lang_explain.md) and [EXPLAIN QUERY PLAN](eqp.md) on each statement that is evaluated.

6.  Improved unicode filename handling in the [command-line shell](cli.md) on Windows.

7.  Improved resistance against goofy query planner decisions caused by incomplete or incorrect modifications to the [sqlite_stat1](fileformat2.md#stat1tab) table by the application.

8.  Added the [sqlite3_db_config](c3ref/db_config.md)(db,[SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableloadextension)) interface which allows the [sqlite3_load_extension()](c3ref/load_extension.md) C-API to be enabled while keeping the [load_extension()](lang_corefunc.md#load_extension) SQL function disabled for security.

9.  Change the [temporary directory search algorithm](tempfiles.md#tempdir) on Unix to allow directories with write and execute permission, but without read permission, to serve as temporary directories. Apply this same standard to the "." fallback directory.
    **Bug Fixes:**

10. Fix a problem with the multi-row one-pass DELETE optimization that was causing it to compute incorrect answers with a self-referential subquery in the WHERE clause. Fix for ticket [dc6ebeda9396087](https://sqlite.org/src/info/dc6ebeda9396087)

11. Fix a possible segfault with DELETE when table is a [rowid table](rowidtable.md) with an [INTEGER PRIMARY KEY](lang_createtable.md#rowid) and the WHERE clause contains a OR and the table has one or more indexes that are able to trigger the OR optimization, but none of the indexes reference any table columns other than the INTEGER PRIMARY KEY. Ticket [16c9801ceba49](https://sqlite.org/src/info/16c9801ceba49).

12. When checking for the [WHERE-clause push-down optimization](optoverview.md#pushdown), verify that all terms of the compound inner SELECT are non-aggregate, not just the last term. Fix for ticket [f7f8c97e97597](https://sqlite.org/src/info/f7f8c97e97597).

13. Fix a locking race condition in Windows that can occur when two or more processes attempt to recover the same [hot journal](fileformat2.md#hotjrnl) at the same time.
    **Hashes:**

14. SQLITE_SOURCE_ID: "2016-05-18 10:57:30 fc49f556e48970561d7ab6a2f24fdd7d9eb81ff2"

15. SHA1 for sqlite3.c: 9b9171b1e6ce7a980e6b714e9c0d9112657ad552

    **Bug fixes backported into patch release 3.12.2 (2016-04-18):**

16. Fix a backwards compatibility problem in version 3.12.0 and 3.12.1: Columns declared as `"INTEGER" PRIMARY KEY` (with quotes around the datatype keyword) were not being recognized as an [INTEGER PRIMARY KEY](lang_createtable.md#rowid), which resulted in an incompatible database file. Ticket [7d7525cb01b68](https://sqlite.org/src/info/7d7525cb01b68)

17. Fix a bug (present since [version 3.9.0](#version_3_9_0)) that can cause the [DELETE](lang_delete.md) operation to miss rows if [PRAGMA reverse_unordered_selects](pragma.md#pragma_reverse_unordered_selects) is turned on. Ticket [a306e56ff68b8fa5](https://sqlite.org/src/info/a306e56ff68b8fa5)

18. Fix a bug in the code generator that can cause incorrect results if two or more [virtual tables](vtab.md) are joined and the virtual table used in outer loop of the join has an [IN operator](lang_expr.md#in_op) constraint.

19. Correctly interpret negative "PRAGMA cache_size" values when determining the cache size used for sorting large amounts of data.

    **Bug fixes backported into patch release 3.12.1 (2016-04-08):**

20. Fix a boundary condition error introduced by version 3.12.0 that can result in a crash during heavy [SAVEPOINT](lang_savepoint.md) usage. Ticket [7f7f8026eda38](https://sqlite.org/src/info/7f7f8026eda38).

21. Fix [views](lang_createview.md) so that they inherit column datatypes from the table that they are defined against, when possible.

22. Fix the query planner so that IS and IS NULL operators are able to drive an index on a LEFT OUTER JOIN.

<span id="version_3_12_2"></span>

### 2016-04-18 (3.12.2)

1.  Fix a backwards compatibility problem in version 3.12.0 and 3.12.1: Columns declared as `"INTEGER" PRIMARY KEY` (with quotes around the datatype keyword) were not being recognized as an [INTEGER PRIMARY KEY](lang_createtable.md#rowid), which resulted in an incompatible database file. Ticket [7d7525cb01b68](https://sqlite.org/src/info/7d7525cb01b68)
2.  Fix a bug (present since [version 3.9.0](#version_3_9_0)) that can cause the [DELETE](lang_delete.md) operation to miss rows if [PRAGMA reverse_unordered_selects](pragma.md#pragma_reverse_unordered_selects) is turned on. Ticket [a306e56ff68b8fa5](https://sqlite.org/src/info/a306e56ff68b8fa5)
3.  Fix a bug in the code generator that can cause incorrect results if two or more [virtual tables](vtab.md) are joined and the virtual table used in outer loop of the join has an [IN operator](lang_expr.md#in_op) constraint.
4.  Correctly interpret negative "PRAGMA cache_size" values when determining the cache size used for sorting large amounts of data.
    **Hashes:**
5.  SQLITE_SOURCE_ID: "2016-04-18 17:30:31 92dc59fd5ad66f646666042eb04195e3a61a9e8e"
6.  SHA1 for sqlite3.c: de5a5898ebd3a3477d4652db143746d008b24c83

<span id="version_3_12_1"></span>

### 2016-04-08 (3.12.1)

1.  Fix a boundary condition error introduced by version 3.12.0 that can result in a crash during heavy [SAVEPOINT](lang_savepoint.md) usage. Ticket [7f7f8026eda38](https://sqlite.org/src/info/7f7f8026eda38).
2.  Fix [views](lang_createview.md) so that they inherit column datatypes from the table that they are defined against, when possible.
3.  Fix the query planner so that IS and IS NULL operators are able to drive an index on a LEFT OUTER JOIN.
    **Hashes:**
4.  SQLITE_SOURCE_ID: "2016-04-08 15:09:49 fe7d3b75fe1bde41511b323925af8ae1b910bc4d"
5.  SHA1 for sqlite3.c: ebb18593350779850e3e1a930eb84a70fca8c1d1

<span id="version_3_9_3"></span>

### 2016-04-01 (3.9.3)

1.  Backport a [simple query planner optimization](https://sqlite.org/src/info/c648539b52ca28c0) that allows the IS operator to drive an index on a LEFT OUTER JOIN. No other changes from the [version 3.9.2](#version_3_9_2) baseline.

<span id="version_3_12_0"></span>

### 2016-03-29 (3.12.0)

1.  **Potentially Disruptive Change:**
2.  The [SQLITE_DEFAULT_PAGE_SIZE](compile.md#default_page_size) is increased from 1024 to 4096. The [SQLITE_DEFAULT_CACHE_SIZE](compile.md#default_cache_size) is changed from 2000 to -2000 so the same amount of cache memory is used by default. See the application note on the [version 3.12.0 page size change](pgszchng2016.md) for further information.
    **Performance enhancements:**
3.  Enhancements to the [Lemon parser generator](lemon.md) so that it creates a smaller and faster SQL parser.
4.  Only create [master journal](tempfiles.md#superjrnl) files if two or more attached databases are all modified, do not have [PRAGMA synchronous](pragma.md#pragma_synchronous) set to OFF, and do not have the [journal_mode](pragma.md#pragma_journal_mode) set to OFF, MEMORY, or WAL.
5.  Only create [statement journal](tempfiles.md#stmtjrnl) files when their size exceeds a threshold. Otherwise the journal is held in memory and no I/O occurs. The threshold can be configured at compile-time using [SQLITE_STMTJRNL_SPILL](compile.md#stmtjrnl_spill) or at start-time using [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_STMTJRNL_SPILL](c3ref/c_config_covering_index_scan.md#sqliteconfigstmtjrnlspill)).
6.  The query planner is able to optimize IN operators on [virtual tables](vtab.md) even if the [xBestIndex](vtab.md#xbestindex) method does not set the sqlite3_index_constraint_usage.omit flag of the virtual table column to the left of the IN operator.
7.  The query planner now does a better job of optimizing [virtual table](vtab.md) accesses in a 3-way or higher join where constraints on the virtual table are split across two or more other tables of the join.
8.  More efficient handling of [application-defined SQL functions](appfunc.md), especially in cases where the application defines hundreds or thousands of custom functions.
9.  The query planner considers the LIMIT clause when estimating the cost of ORDER BY.
10. The configure script (on unix) automatically detects pread() and pwrite() and sets compile-time options to use those OS interfaces if they are available.
11. Reduce the amount of memory needed to hold the schema.
12. Other miscellaneous micro-optimizations for improved performance and reduced memory usage.
    **New Features:**
13. Added the [SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenablefts3tokenizer) option to [sqlite3_db_config()](c3ref/db_config.md) which allows the two-argument version of the [fts3_tokenizer()](fts3.md#f3tknzr) SQL function to be enabled or disabled at run-time.
14. Added the [sqlite3rbu_bp_progress()](https://sqlite.org/src/artifact/d7cc99350?ln=403-443) interface to the [RBU](rbu.md) extension.
15. The [PRAGMA defer_foreign_keys=ON](pragma.md#pragma_defer_foreign_keys) statement now also disables [RESTRICT actions](foreignkeys.md#fk_actions) on foreign key.
16. Added the [sqlite3_system_errno()](c3ref/system_errno.md) interface.
17. Added the [SQLITE_DEFAULT_SYNCHRONOUS](compile.md#default_synchronous) and [SQLITE_DEFAULT_WAL_SYNCHRONOUS](compile.md#default_wal_synchronous) compile-time options. The [SQLITE_DEFAULT_SYNCHRONOUS](compile.md#default_synchronous) compile-time option replaces the [SQLITE_EXTRA_DURABLE](compile.md#extra_durable) option, which is no longer supported.
18. Enhanced the ".stats" command in the [command-line shell](cli.md) to show more information about I/O performance obtained from /proc, when available.
    **Bug fixes:**
19. Make sure the [sqlite3_set_auxdata()](c3ref/get_auxdata.md) values from multiple triggers within a single statement do not interfere with one another. Ticket [dc9b1c91](https://sqlite.org/src/info/dc9b1c91).
20. Fix the code generator for expressions of the form "x IN (SELECT...)" where the SELECT statement on the RHS is a correlated subquery. Ticket [5e3c886796e5512e](https://sqlite.org/src/info/5e3c886796e5512e).
21. Fix a harmless TSAN warning associated with the [sqlite3_db_readonly()](c3ref/db_readonly.md) interface.
    **Hashes:**
22. SQLITE_SOURCE_ID: "2016-03-29 10:14:15 e9bb4cf40f4971974a74468ef922bdee481c988b"
23. SHA1 for sqlite3.c: cba2be96d27cb51978cd4a200397a4ad178986eb

<span id="version_3_11_1"></span>

### 2016-03-03 (3.11.1)

1.  Improvements to the Makefiles and build scripts used by VisualStudio.
2.  Fix an [FTS5](fts5.md) issue in which the 'optimize' command could cause index corruption.
3.  Fix a buffer overread that might occur if [FTS5](fts5.md) is used to query a corrupt database file.
4.  Increase the maximum "scope" value for the [spellfix1](spellfix1.md) extension from 6 to 30.
5.  SQLITE_SOURCE_ID: "2016-03-03 16:17:53 f047920ce16971e573bc6ec9a48b118c9de2b3a7"
6.  SHA1 for sqlite3.c: 3da832fd2af36eaedb05d61a8f4c2bb9f3d54265

<span id="version_3_11_0"></span>

### 2016-02-15 (3.11.0)

1.  **General improvements:**
2.  Enhanced [WAL mode](wal.md) so that it works efficiently with transactions that are larger than the [cache_size](pragma.md#pragma_cache_size).
3.  Added the [FTS5 detail option](fts5.md#the_detail_option).
4.  Added the "EXTRA" option to [PRAGMA synchronous](pragma.md#pragma_synchronous) that does a sync of the containing directory when a rollback journal is unlinked in DELETE mode, for better durability. The [SQLITE_EXTRA_DURABLE](compile.md#extra_durable) compile-time option enables [PRAGMA synchronous=EXTRA](pragma.md#pragma_synchronous) by default.
5.  Enhanced the [query planner](optoverview.md) so that it is able to use a [covering index](queryplanner.md#covidx) as part of the [OR optimization](optoverview.md#or_opt).
6.  Avoid recomputing [NOT NULL](lang_createtable.md#notnullconst) and [CHECK constraints](lang_createtable.md#ckconst) on unchanged columns in [UPDATE](lang_update.md) statement.
7.  Many micro-optimizations, resulting in a library that is faster than the previous release.
    **Enhancements to the [command-line shell](cli.md):**
8.  By default, the shell is now in "auto-explain" mode. The output of [EXPLAIN](lang_explain.md) commands is automatically formatted.
9.  Added the ".vfslist" [dot-command](cli.md#dotcmd).
10. The [SQLITE_ENABLE_EXPLAIN_COMMENTS](compile.md#enable_explain_comments) compile-time option is now turned on by default in the standard builds.
    **Enhancements to the [TCL Interface](tclsqlite.md):**
11. If a database connection is opened with the "-uri 1" option, then [URI filenames](uri.md) are honored by the "backup" and "restore" commands.
12. Added the "-sourceid" option to the "sqlite3" command.
    **Makefile improvements:**
13. Improved pthreads detection in configure scripts.
14. Add the ability to do MSVC Windows builds from the [amalgamation tarball](download.md).
    **Bug fixes**
15. Fix an issue with incorrect sharing of VDBE temporary registers between co-routines that could cause incorrect query results in obscure cases. Ticket [d06a25c84454a](https://sqlite.org/src/info/d06a25c84454a).
16. Fix a problem in the [sqlite3_result_subtype()](c3ref/result_subtype.md) interface that could cause problems for the [json1](json1.md) extension under obscure circumstances. Fix for ticket [f45ac567eaa9f9](https://sqlite.org/src/info/f45ac567eaa9f9).
17. Escape control characters in JSON strings. Fix for ticket [ad2559db380abf8](https://sqlite.org/src/info/ad2559db380abf8).
18. Reenable the xCurrentTime and xGetLastError methods in the built-in unix [VFSes](vfs.md) as long as [SQLITE_OMIT_DEPRECATED](compile.md#omit_deprecated) is not defined.
    **Backwards Compatibility:**
19. Because of continuing security concerns, the two-argument version of the seldom-used and little-known [fts3_tokenizer()](fts3.md#f3tknzr) function is disabled unless SQLite is compiled with the [SQLITE_ENABLE_FTS3_TOKENIZER](compile.md#enable_fts3_tokenizer).
    **Hashes:**
20. SQLITE_SOURCE_ID: "2016-02-15 17:29:24 3d862f207e3adc00f78066799ac5a8c282430a5f"
21. SHA1 for sqlite3.c: df01436c5fcfe72d1a95bc172158219796e1a90b

<span id="version_3_10_2"></span>

### 2016-01-20 (3.10.2)

1.  **Critical bug fix:**
2.  Version 3.10.0 introduced a case-folding bug in the [LIKE](lang_expr.md#like) operator which is fixed by this patch release. Ticket [80369eddd5c94](https://sqlite.org/src/info/80369eddd5c94).
    **Other miscellaneous bug fixes:**
3.  Fix a use-after-free that can occur when SQLite is compiled with -DSQLITE_HAS_CODEC.
4.  Fix the build so that it works with -DSQLITE_OMIT_WAL.
5.  Fix the configure script for the amalgamation so that the --readline option works again on Raspberry PIs.
    **Hashes:**
6.  SQLITE_SOURCE_ID: "2016-01-20 15:27:19 17efb4209f97fb4971656086b138599a91a75ff9"
7.  SHA1 for sqlite3.c: f7088b19d97cd7a1c805ee95c696abd54f01de4f

<span id="version_3_10_1"></span>

### 2016-01-14 (3.10.1)

1.  **New feature:**
2.  Add the [SQLITE_FCNTL_JOURNAL_POINTER](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntljournalpointer) file control.
    **Bug fix:**
3.  Fix a 16-month-old bug in the query planner that could generate incorrect results when a scalar subquery attempts to use the [block sorting](queryplanner.md#partialsort) optimization. Ticket [cb3aa0641d9a4](https://sqlite.org/src/info/cb3aa0641d9a4).
    **Hashes:**
4.  SQLITE_SOURCE_ID: "2016-01-13 21:41:56 254419c36766225ca542ae873ed38255e3fb8588"
5.  SHA1 for sqlite3.c: 1398ba8e4043550a533cdd0834bfdad1c9eab0f4

<span id="version_3_10_0"></span>

### 2016-01-06 (3.10.0)

1.  **General improvements:**
2.  Added support for [LIKE](lang_expr.md#like), [GLOB](lang_expr.md#glob), and [REGEXP](lang_expr.md#regexp) operators on [virtual tables](vtab.md).
3.  Added the [colUsed field](vtab.md#colUsed) to [sqlite3_index_info](c3ref/index_info.md) for use by the [sqlite3_module.xBestIndex](vtab.md#xbestindex) method.
4.  Enhance the [PRAGMA cache_spill](pragma.md#pragma_cache_spill) statement to accept a 32-bit integer parameter which is the threshold below which cache spilling is prohibited.
5.  On unix, if a symlink to a database file is opened, then the corresponding journal files are based on the actual filename, not the symlink name.
6.  Added the "--transaction" option to [sqldiff](sqldiff.md).
7.  Added the [sqlite3_db_cacheflush()](c3ref/db_cacheflush.md) interface.
8.  Added the [sqlite3_strlike()](c3ref/strlike.md) interface.
9.  When using [memory-mapped I/O](mmap.md) map the database file read-only so that stray pointers and/or array overruns in the application cannot accidentally modify the database file.
10. Added the *experimental* [sqlite3_snapshot_get()](c3ref/snapshot_get.md), [sqlite3_snapshot_open()](c3ref/snapshot_open.md), and [sqlite3_snapshot_free()](c3ref/snapshot_free.md) interfaces. These are subject to change or removal in a subsequent release.
11. Enhance the ['utc' modifier](lang_datefunc.md#localtime) in the [date and time functions](lang_datefunc.md) so that it is a no-op if the date/time is known to already be in UTC. (This is not a compatibility break since the behavior has long been documented as "undefined" in that case.)
12. Added the [json_group_array()](json1.md#jgrouparray) and [json_group_object()](json1.md#jgroupobject) SQL functions in the [json](json1.md#jmini) extension.
13. Added the [SQLITE_LIKE_DOESNT_MATCH_BLOBS](compile.md#like_doesnt_match_blobs) compile-time option.
14. Many small performance optimizations.
    **Portability enhancements:**
15. Work around a sign-extension bug in the optimizer of the HP C compiler on HP/UX. [(details)](https://sqlite.org/src/fdiff?sbs=1&v1=869c95b0fc73026d&v2=232c242a0ccb3d67)
    **Enhancements to the [command-line shell](cli.md):**
16. Added the ".changes ON\|OFF" and ".vfsinfo" [dot-commands](cli.md#dotcmd).
17. Translate between MBCS and UTF8 when running in [cmd.exe](https://en.wikipedia.org/wiki/Cmd.exe) on Windows.
    **Enhancements to makefiles:**
18. Added the --enable-editline and --enable-static-shell options to the various autoconf-generated configure scripts.
19. Omit all use of "awk" in the makefiles, to make building easier for MSVC users.
    **Important fixes:**
20. Fix inconsistent integer to floating-point comparison operations that could result in a corrupt index if the index is created on a table column that contains both large integers and floating point values of similar magnitude. Ticket [38a97a87a6](https://sqlite.org/src/tktview?name=38a97a87a6).
21. Fix an infinite-loop in the query planner that could occur on malformed [common table expressions](lang_with.md).
22. Various bug fixes in the [sqldiff](sqldiff.md) tool.
    **Hashes:**
23. SQLITE_SOURCE_ID: "2016-01-06 11:01:07 fd0a50f0797d154fefff724624f00548b5320566"
24. SHA1 for sqlite3.c: b92ca988ebb6df02ac0c8f866dbf3256740408ac

<span id="version_3_9_2"></span>

### 2015-11-02 (3.9.2)

1.  Fix the schema parser so that it interprets certain (obscure and ill-formed) CREATE TABLE statements the same as legacy. Fix for ticket [ac661962a2aeab3c331](https://sqlite.org/src/info/ac661962a2aeab3c331)
2.  Fix a query planner problem that could result in an incorrect answer due to the use of [automatic indexing](optoverview.md#autoindex) in subqueries in the FROM clause of a correlated scalar subqueries. Fix for ticket [8a2adec1](https://sqlite.org/src/info/8a2adec1).
3.  SQLITE_SOURCE_ID: "2015-11-02 18:31:45 bda77dda9697c463c3d0704014d51627fceee328"
4.  SHA1 for sqlite3.c: 1c4013876f50bbaa3e6f0f98e0147c76287684c1

<span id="version_3_9_1"></span>

### 2015-10-16 (3.9.1)

1.  Fix [the json1 extension](json1.md) so that it does <u>not</u> recognize ASCII form-feed as a whitespace character, in order to comply with RFC-7159. Fix for ticket [57eec374ae1d0a1d](https://sqlite.org/src/info/57eec374ae1d0a1d)
2.  Add a few \#ifdef and build script changes to address compilation issues that appeared after the 3.9.0 release.
3.  SQLITE_SOURCE_ID: ""2015-10-16 17:31:12 767c1727fec4ce11b83f25b3f1bfcfe68a2c8b02"
4.  SHA1 for sqlite3.c: 5e6d1873a32d82c2cf8581f143649940cac8ae49

<span id="version_3_9_0"></span>

### 2015-10-14 (3.9.0)

1.  **Policy Changes:**
2.  The [version numbering conventions](versionnumbers.md) for SQLite are revised to use the emerging standard of [semantic versioning](http://semver.org/).
    **New Features And Enhancements:**
3.  Added [the json1 extension](json1.md) module in the source tree, and in the [amalgamation](amalgamation.md). Enable support using the [SQLITE_ENABLE_JSON1](compile.md#enable_json1) compile-time option.
4.  Added [Full Text Search version 5 (FTS5)](fts5.md) to the [amalgamation](amalgamation.md), enabled using [SQLITE_ENABLE_FTS5](compile.md#enable_fts5). FTS5 will be considered "experimental" (subject to incompatible changes) for at least one more release cycle.
5.  The [CREATE VIEW](lang_createview.md) statement now accepts an optional list of column names following the view name.
6.  Added support for [indexes on expressions](expridx.md).
7.  Added support for [table-valued functions](vtab.md#tabfunc2) in the FROM clause of a [SELECT](lang_select.md) statement.
8.  Added support for [eponymous virtual tables](vtab.md#epovtab).
9.  A [VIEW](lang_createview.md) may now reference undefined tables and functions when initially created. Missing tables and functions are reported when the VIEW is used in a query.
10. Added the [sqlite3_value_subtype()](c3ref/value_subtype.md) and [sqlite3_result_subtype()](c3ref/result_subtype.md) interfaced (used by [the json1 extension](json1.md)).
11. The query planner is now able to use [partial indexes](partialindex.md) that contain AND-connected terms in the WHERE clause.
12. The sqlite3_analyzer.exe utility is updated to report the depth of each btree and to show the average fanout for indexes and WITHOUT ROWID tables.
13. Enhanced the [dbstat virtual table](dbstat.md) so that it can be used as a [table-valued function](vtab.md#tabfunc2) where the argument is the schema to be analyzed.
    **Other changes:**
14. The [sqlite3_memory_alarm()](c3ref/aggregate_count.md) interface, which has been deprecated and undocumented for 8 years, is changed into a no-op.
    **Important fixes:**
15. Fixed a critical bug in the [SQLite Encryption Extension](https://sqlite.org/see/doc/trunk/www/readme.wiki) that could cause the database to become unreadable and unrecoverable if a [VACUUM](lang_vacuum.md) command changed the size of the encryption nonce.
16. Added a memory barrier in the implementation of [sqlite3_initialize()](c3ref/initialize.md) to help ensure that it is thread-safe.
17. Fix the [OR optimization](optoverview.md#or_opt) so that it always ignores subplans that do not use an index.
18. Do not apply the [WHERE-clause push-down optimization](optoverview.md#pushdown) on terms that originate in the ON or USING clause of a LEFT JOIN. Fix for ticket [c2a19d81652f40568c](https://sqlite.org/src/info/c2a19d81652f40568c).
19. SQLITE_SOURCE_ID: "2015-10-14 12:29:53 a721fc0d89495518fe5612e2e3bbc60befd2e90d"
20. SHA1 for sqlite3.c: c03e47e152ddb9c342b84ffb39448bf4a2bd4288

<span id="version_3_8_11_1"></span>

### 2015-07-29 (3.8.11.1)

1.  Restore an undocumented side-effect of [PRAGMA cache_size](pragma.md#pragma_cache_size): force the database schema to be parsed if the database has not been previously accessed.
2.  Fix a long-standing problem in [sqlite3_changes()](c3ref/changes.md) for [WITHOUT ROWID](withoutrowid.md) tables that was reported a few hours after the 3.8.11 release.
3.  SQLITE_SOURCE_ID: "2015-07-29 20:00:57 cf538e2783e468bbc25e7cb2a9ee64d3e0e80b2f"
4.  SHA1 for sqlite3.c: 3be71d99121fe5b17f057011025bcf84e7cc6c84

<span id="version_3_8_11"></span>

### 2015-07-27 (3.8.11)

1.  Added the experimental [RBU](rbu.md) extension. Note that this extension is experimental and subject to change in incompatible ways.
2.  Added the experimental [FTS5](fts5.md) extension. Note that this extension is experimental and subject to change in incompatible ways.
3.  Added the [sqlite3_value_dup()](c3ref/value_dup.md) and [sqlite3_value_free()](c3ref/value_dup.md) interfaces.
4.  Enhance the [spellfix1](spellfix1.md) extension to support [ON CONFLICT](lang_conflict.md) clauses.
5.  The [IS operator](lang_expr.md#isisnot) is now able to drive indexes.
6.  Enhance the query planner to permit [automatic indexing](optoverview.md#autoindex) on FROM-clause subqueries that are implemented by co-routine.
7.  Disallow the use of "rowid" in [common table expressions](lang_with.md).
8.  Added the [PRAGMA cell_size_check](pragma.md#pragma_cell_size_check) command for better and earlier detection of database file corruption.
9.  Added the [matchinfo 'b' flag](fts3.md#matchinfo-b) to the [matchinfo()](fts3.md#matchinfo) function in [FTS3](fts3.md).
10. Improved fuzz-testing of database files, with fixes for problems found.
11. Add the fuzzcheck test program and automatically run this program using both SQL and database test cases on "make test".
12. Added the [SQLITE_MUTEX_STATIC_VFS1](c3ref/c_mutex_fast.md) static mutex and use it in the Windows [VFS](vfs.md).
13. The [sqlite3_profile()](c3ref/profile.md) callback is invoked (by [sqlite3_reset()](c3ref/reset.md) or [sqlite3_finalize()](c3ref/finalize.md)) for statements that did not run to completion.
14. Enhance the page cache so that it can preallocate a block of memory to use for the initial set page cache lines. Set the default preallocation to 100 pages. Yields about a 5% performance increase on common workloads.
15. Miscellaneous micro-optimizations result in 22.3% more work for the same number of CPU cycles relative to the previous release. SQLite now runs twice as fast as [version 3.8.0](#version_3_8_0) and three times as fast as [version 3.3.9](#version_3_3_9). (Measured using [cachegrind](http://valgrind.org/docs/manual/cg-manual.html) on the [speedtest1.c](https://sqlite.org/src/artifact/83f6b3318f7ee) workload on Ubuntu 14.04 x64 with gcc 4.8.2 and -Os. Your performance may vary.)
16. Added the [sqlite3_result_zeroblob64()](c3ref/result_blob.md) and [sqlite3_bind_zeroblob64()](c3ref/bind_blob.md) interfaces.
    **Important bug fixes:**
17. Fix [CREATE TABLE AS](lang_createtable.md#createtabas) so that columns of type TEXT never end up holding an INT value. Ticket [f2ad7de056ab1dc9200](https://sqlite.org/src/info/f2ad7de056ab1dc9200)
18. Fix [CREATE TABLE AS](lang_createtable.md#createtabas) so that it does not leave NULL entries in the [sqlite_master table](schematab.md) if the SELECT statement on the right-hand side aborts with an error. Ticket [873cae2b6e25b](https://sqlite.org/src/info/873cae2b6e25b)
19. Fix the [skip-scan optimization](optoverview.md#skipscan) so that it works correctly when the [OR optimization](optoverview.md#or_opt) is used on [WITHOUT ROWID](withoutrowid.md) tables. Ticket [8fd39115d8f46](https://sqlite.org/src/info/8fd39115d8f46)
20. Fix the [sqlite3_memory_used()](c3ref/memory_highwater.md) and [sqlite3_memory_highwater()](c3ref/memory_highwater.md) interfaces so that they actually do provide a 64-bit answer.
    **Hashes:**
21. SQLITE_SOURCE_ID: "2015-07-27 13:49:41 b8e92227a469de677a66da62e4361f099c0b79d0"
22. SHA1 for sqlite3.c: 719f6891abcd9c459b5460b191d731cd12a3643e

<span id="version_3_8_10_2"></span>

### 2015-05-20 (3.8.10.2)

1.  Fix an index corruption issue introduced by [version 3.8.7](#version_3_8_7). An index with a TEXT key can be corrupted by an [INSERT](lang_insert.md) into the corresponding table if the table has two nested triggers that convert the key value to INTEGER and back to TEXT again. Ticket [34cd55d68e0](https://sqlite.org/src/info/34cd55d68e0e6e7c9a0711aab81a2ee3c354b4c0)
2.  SQLITE_SOURCE_ID: "2015-05-20 18:17:19 2ef4f3a5b1d1d0c4338f8243d40a2452cc1f7fe4"
3.  SHA1 for sqlite3.c: 638abb77965332c956dbbd2c8e4248e84da4eb63

<span id="version_3_8_10_1"></span>

### 2015-05-09 (3.8.10.1)

1.  Make [sqlite3_compileoption_used()](c3ref/compileoption_get.md) responsive to the [SQLITE_ENABLE_DBSTAT_VTAB](compile.md#enable_dbstat_vtab) compile-time option.
2.  Fix a harmless warning in the [command-line shell](cli.md) on some versions of MSVC.
3.  Fix minor issues with the [dbstat virtual table](dbstat.md).
4.  SQLITE_SOURCE_ID: "2015-05-09 12:14:55 05b4b1f2a937c06c90db70c09890038f6c98ec40"
5.  SHA1 for sqlite3.c: 85e4e1c08c7df28ef61bb9759a0d466e0eefbaa2

<span id="version_3_8_10"></span>

### 2015-05-07 (3.8.10)

1.  Added the [sqldiff.exe](sqldiff.md) utility program for computing the differences between two SQLite database files.
2.  Added the [matchinfo y flag](fts3.md#matchinfo-y) to the [matchinfo()](fts3.md#matchinfo) function of [FTS3](fts3.md).
3.  Performance improvements for [ORDER BY](lang_select.md#orderby), [VACUUM](lang_vacuum.md), [CREATE INDEX](lang_createindex.md), [PRAGMA integrity_check](pragma.md#pragma_integrity_check), and [PRAGMA quick_check](pragma.md#pragma_quick_check).
4.  Fix many obscure problems discovered while [SQL fuzzing](testing.md#fuzztesting).
5.  Identify all methods for important objects in the interface documentation. ([example](c3ref/context.md))
6.  Made the [American Fuzzy Lop fuzzer](testing.md#aflfuzz) a standard part of SQLite's [testing strategy](testing.md).
7.  Add the ".binary" and ".limits" commands to the [command-line shell](cli.md).
8.  Make the [dbstat virtual table](dbstat.md) part of standard builds when compiled with the [SQLITE_ENABLE_DBSTAT_VTAB](compile.md#enable_dbstat_vtab) option.
9.  SQLITE_SOURCE_ID: "2015-05-07 11:53:08 cf975957b9ae671f34bb65f049acf351e650d437"
10. SHA1 for sqlite3.c: 0b34f0de356a3f21b9dfc761f3b7821b6353c570

<span id="version_3_8_9"></span>

### 2015-04-08 (3.8.9)

1.  Add VxWorks-7 as an officially supported and tested platform.
2.  Added the [sqlite3_status64()](c3ref/status.md) interface.
3.  Fix memory size tracking so that it works even if SQLite uses more than 2GiB of memory.
4.  Added the [PRAGMA index_xinfo](pragma.md#pragma_index_xinfo) command.
5.  Fix a potential 32-bit integer overflow problem in the [sqlite3_blob_read()](c3ref/blob_read.md) and [sqlite3_blob_write()](c3ref/blob_write.md) interfaces.
6.  Ensure that prepared statements automatically reset on extended error codes of SQLITE_BUSY and SQLITE_LOCKED even when compiled using [SQLITE_OMIT_AUTORESET](compile.md#omit_autoreset).
7.  Correct miscounts in the sqlite3_analyzer.exe utility related to WITHOUT ROWID tables.
8.  Added the ".dbinfo" command to the [command-line shell](cli.md).
9.  Improve the performance of fts3/4 queries that use the OR operator and at least one auxiliary fts function.
10. Fix a bug in the fts3 snippet() function causing it to omit leading separator characters from snippets that begin with the first token in a column.
11. SQLITE_SOURCE_ID: "2015-04-08 12:16:33 8a8ffc862e96f57aa698f93de10dee28e69f6e09"
12. SHA1 for sqlite3.c: 49f1c3ae347e1327b5aaa6c7f76126bdf09c6f42

<span id="version_3_8_8_3"></span>

### 2015-02-25 (3.8.8.3)

1.  Fix a bug (ticket [2326c258d02ead33](https://sqlite.org/src/info/2326c258d02ead33)) that can lead to incorrect results if the qualifying constraint of a [partial index](partialindex.md) appears in the ON clause of a LEFT JOIN.
2.  Added the ability to link against the "[linenoise](https://github.com/antirez/linenoise)" command-line editing library in unix builds of the [command-line shell](cli.md).
3.  SQLITE_SOURCE_ID: "2015-02-25 13:29:11 9d6c1880fb75660bbabd693175579529785f8a6b"
4.  SHA1 for sqlite3.c: 74ee38c8c6fd175ec85a47276dfcefe8a262827a

<span id="version_3_8_8_2"></span>

### 2015-01-30 (3.8.8.2)

1.  Enhance [sqlite3_wal_checkpoint_v2(TRUNCATE)](c3ref/wal_checkpoint_v2.md) interface so that it truncates the WAL file even if there is no checkpoint work to be done.
2.  SQLITE_SOURCE_ID: "2015-01-30 14:30:45 7757fc721220e136620a89c9d28247f28bbbc098"
3.  SHA1 for sqlite3.c: 85ce79948116aa9a087ec345c9d2ce2c1d3cd8af

<span id="version_3_8_8_1"></span>

### 2015-01-20 (3.8.8.1)

1.  Fix a bug in the sorting logic, present since version 3.8.4, that can cause output to appear in the wrong order on queries that contains an ORDER BY clause, a LIMIT clause, and that have approximately 60 or more columns in the result set. Ticket [f97c4637102a3ae72b79](https://sqlite.org/src/tktview?name=f97c4637102a3ae72b79).
2.  SQLITE_SOURCE_ID: "2015-01-20 16:51:25 f73337e3e289915a76ca96e7a05a1a8d4e890d55"
3.  SHA1 for sqlite3.c: 33987fb50dcc09f1429a653d6b47672f5a96f19e

<span id="version_3_8_8"></span>

### 2015-01-16 (3.8.8)

1.  **New Features:**
2.  Added the [PRAGMA data_version](pragma.md#pragma_data_version) command that can be used to determine if a database file has been modified by another process.
3.  Added the [SQLITE_CHECKPOINT_TRUNCATE](c3ref/c_checkpoint_full.md) option to the [sqlite3_wal_checkpoint_v2()](c3ref/wal_checkpoint_v2.md) interface, with corresponding enhancements to [PRAGMA wal_checkpoint](pragma.md#pragma_wal_checkpoint).
4.  Added the [sqlite3_stmt_scanstatus()](c3ref/stmt_scanstatus.md) interface, available only when compiled with [SQLITE_ENABLE_STMT_SCANSTATUS](compile.md#enable_stmt_scanstatus).
5.  The [sqlite3_table_column_metadata()](c3ref/table_column_metadata.md) is enhanced to work correctly on [WITHOUT ROWID](withoutrowid.md) tables and to check for the existence of a a table if the column name parameter is NULL. The interface is now also included in the build by default, without requiring the [SQLITE_ENABLE_COLUMN_METADATA](compile.md#enable_column_metadata) compile-time option.
6.  Added the [SQLITE_ENABLE_API_ARMOR](compile.md#enable_api_armor) compile-time option.
7.  Added the [SQLITE_REVERSE_UNORDERED_SELECTS](compile.md#reverse_unordered_selects) compile-time option.
8.  Added the [SQLITE_SORTER_PMASZ](compile.md#sorter_pmasz) compile-time option and [SQLITE_CONFIG_PMASZ](c3ref/c_config_covering_index_scan.md#sqliteconfigpmasz) start-time option.
9.  Added the [SQLITE_CONFIG_PCACHE_HDRSZ](c3ref/c_config_covering_index_scan.md#sqliteconfigpcachehdrsz) option to [sqlite3_config()](c3ref/config.md) which makes it easier for applications to determine the appropriate amount of memory for use with [SQLITE_CONFIG_PAGECACHE](c3ref/c_config_covering_index_scan.md#sqliteconfigpagecache).
10. The number of rows in a [VALUES clause](lang_select.md#values) is no longer limited by [SQLITE_LIMIT_COMPOUND_SELECT](c3ref/c_limit_attached.md#sqlitelimitcompoundselect).
11. Added the [eval.c](https://sqlite.org/src/artifact/f971962e92ebb8b0) [loadable extension](loadext.md) that implements an eval() SQL function that will recursively evaluate SQL.
    **Performance Enhancements:**
12. Reduce the number of memcpy() operations involved in balancing a b-tree, for 3.2% overall performance boost.
13. Improvements to cost estimates for the [skip-scan optimization](optoverview.md#skipscan).
14. The [automatic indexing](optoverview.md#autoindex) optimization is now capable of generating a [partial index](partialindex.md) if that is appropriate.
    **Bug fixes:**
15. Ensure durability following a power loss with "PRAGMA journal_mode=TRUNCATE" by calling fsync() right after truncating the journal file.
16. The query planner now recognizes that any column in the right-hand table of a LEFT JOIN can be NULL, even if that column has a NOT NULL constraint. Avoid trying to optimize out NULL tests in those cases. Fix for ticket [6f2222d550f5b0ee7ed](https://sqlite.org/src/info/6f2222d550f5b0ee7ed).
17. Make sure ORDER BY puts rows in ascending order even if the DISTINCT operator is implemented using a descending index. Fix for ticket [c5ea805691bfc4204b1cb9e](https://sqlite.org/src/info/c5ea805691bfc4204b1cb9e).
18. Fix data races that might occur under stress when running with many threads in [shared cache mode](sharedcache.md) where some of the threads are opening and closing connections.
19. Fix obscure crash bugs found by [american fuzzy lop](http://lcamtuf.coredump.cx/afl/). Ticket [a59ae93ee990a55](https://sqlite.org/src/info/a59ae93ee990a55).
20. Work around a GCC optimizer bug (for gcc 4.2.1 on MacOS 10.7) that caused the [R-Tree extension](rtree.md) to compute incorrect results when compiled with -O3.
    **Other changes:**
21. Disable the use of the strchrnul() C-library routine unless it is specifically enabled using the -DHAVE_STRCHRNULL compile-time option.
22. Improvements to the effectiveness and accuracy of the [likelihood()](lang_corefunc.md#likelihood), [likely()](lang_corefunc.md#likely), and [unlikely()](lang_corefunc.md#unlikely) SQL hint functions.
23. SQLITE_SOURCE_ID: "2015-01-16 12:08:06 7d68a42face3ab14ed88407d4331872f5b243fdf"
24. SHA1 for sqlite3.c: 91aea4cc722371d58aae3d22e94d2a4165276905

<span id="version_3_8_7_4"></span>

### 2014-12-09 (3.8.7.4)

1.  Bug fix: Add in a mutex that was omitted from the previous release.
2.  SQLITE_SOURCE_ID: "2014-12-09 01:34:36 f66f7a17b78ba617acde90fc810107f34f1a1f2e"
3.  SHA1 for sqlite3.c: 0a56693a3c24aa3217098afab1b6fecccdedfd23

<span id="version_3_8_7_3"></span>

### 2014-12-05 (3.8.7.3)

1.  Bug fix: Ensure the cached KeyInfo objects (an internal abstraction not visible to the application) do not go stale when operating in [shared cache mode](sharedcache.md) and frequently closing and reopening some database connections while leaving other database connections on the same shared cache open continuously. Ticket [e4a18565a36884b00edf](https://sqlite.org/src/info/e4a18565a36884b00edf).
2.  Bug fix: Recognize that any column in the right-hand table of a LEFT JOIN can be NULL even if the column has a NOT NULL constraint. Do not apply optimizations that assume the column is never NULL. Ticket [6f2222d550f5b0ee7ed](https://sqlite.org/src/info/6f2222d550f5b0ee7ed).
3.  SQLITE_SOURCE_ID: "2014-12-05 22:29:24 647e77e853e81a5effeb4c33477910400a67ba86"
4.  SHA1 for sqlite3.c: 3ad2f5ba3a4a3e3e51a1dac9fda9224b359f0261

<span id="version_3_8_7_2"></span>

### 2014-11-18 (3.8.7.2)

1.  Enhance the [ROLLBACK](lang_transaction.md) command so that pending queries are allowed to continue as long as the schema is unchanged. Formerly, a ROLLBACK would cause all pending queries to fail with an [SQLITE_ABORT](rescode.md#abort) or [SQLITE_ABORT_ROLLBACK](rescode.md#abort_rollback) error. That error is still returned if the ROLLBACK modifies the schema.
2.  Bug fix: Make sure that NULL results from OP_Column are fully and completely NULL and do not have the MEM_Ephem bit set. Ticket [094d39a4c95ee4](https://sqlite.org/src/info/094d39a4c95ee4).
3.  Bug fix: The %c format in sqlite3_mprintf() is able to handle precisions greater than 70.
4.  Bug fix: Do not automatically remove the DISTINCT keyword from a SELECT that forms the right-hand side of an IN operator since it is necessary if the SELECT also contains a LIMIT. Ticket [db87229497](https://sqlite.org/src/info/db87229497).
5.  SQLITE_SOURCE_ID: "2014-11-18 20:57:56 2ab564bf9655b7c7b97ab85cafc8a48329b27f93"
6.  SHA1 for sqlite3.c: b2a68d5783f48dba6a8cb50d8bf69b238c5ec53a

<span id="version_3_8_7_1"></span>

### 2014-10-29 (3.8.7.1)

1.  In [PRAGMA journal_mode=TRUNCATE](pragma.md#pragma_journal_mode) mode, call fsync() immediately after truncating the journal file to ensure that the transaction is durable across a power loss.
2.  Fix an assertion fault that can occur when updating the NULL value of a field at the end of a table that was added using [ALTER TABLE ADD COLUMN](lang_altertable.md).
3.  Do not attempt to use the strchrnul() function from the standard C library unless the HAVE_STRCHRNULL compile-time option is set.
4.  Fix a couple of problems associated with running an UPDATE or DELETE on a [VIEW](lang_createview.md) with a [rowid](lang_createtable.md#rowid) in the WHERE clause.
5.  SQLITE_SOURCE_ID: "2014-10-29 13:59:56 3b7b72c4685aa5cf5e675c2c47ebec10d9704221"
6.  SHA1 for sqlite3.c: 2d25bd1a73dc40f538f3a81c28e6efa5999bdf0c

<span id="version_3_8_7"></span>

### 2014-10-17 (3.8.7)

1.  **Performance Enhancements:**
2.  Many micro-optimizations result in 20.3% more work for the same number of CPU cycles relative to the previous release. The cumulative performance increase since [version 3.8.0](#version_3_8_0) is 61%. (Measured using [cachegrind](http://valgrind.org/docs/manual/cg-manual.html) on the [speedtest1.c](https://sqlite.org/src/artifact/83f6b3318f7ee) workload on Ubuntu 13.10 x64 with gcc 4.8.1 and -Os. Your performance may vary.)
3.  The sorter can use auxiliary helper threads to increase real-time response. This feature is off by default and may be enabled using the [PRAGMA threads](pragma.md#pragma_threads) command or the [SQLITE_DEFAULT_WORKER_THREADS](compile.md#default_worker_threads) compile-time option.
4.  Enhance the [skip-scan](optoverview.md#skipscan) optimization so that it is able to skip index terms that occur in the middle of the index, not just as the left-hand side of the index.
5.  Improved optimization of [CAST](lang_expr.md#castexpr) operators.
6.  Various improvements in how the query planner uses [sqlite_stat4](fileformat2.md#stat4tab) information to estimate plan costs.
    **New Features:**
7.  Added new interfaces with 64-bit length parameters: [sqlite3_malloc64()](c3ref/free.md), [sqlite3_realloc64()](c3ref/free.md), [sqlite3_bind_blob64()](c3ref/bind_blob.md), [sqlite3_result_blob64()](c3ref/result_blob.md), [sqlite3_bind_text64()](c3ref/bind_blob.md), and [sqlite3_result_text64()](c3ref/result_blob.md).
8.  Added the new interface [sqlite3_msize()](c3ref/free.md) that returns the size of a memory allocation obtained from [sqlite3_malloc64()](c3ref/free.md) and its variants.
9.  Added the [SQLITE_LIMIT_WORKER_THREADS](c3ref/c_limit_attached.md#sqlitelimitworkerthreads) option to [sqlite3_limit()](c3ref/limit.md) and [PRAGMA threads](pragma.md#pragma_threads) command for configuring the number of available worker threads.
10. The [spellfix1](spellfix1.md) extension allows the application to optionally specify the rowid for each INSERT.
11. Added the [User Authentication](https://sqlite.org/src/doc/trunk/ext/userauth/user-auth.txt) extension.
    **Bug Fixes:**
12. Fix a bug in the [partial index](partialindex.md) implementation that might result in an incorrect answer if a partial index is used in a subquery or in a [view](lang_createview.md). Ticket [98d973b8f5](https://sqlite.org/src/info/98d973b8f5).
13. Fix a query planner bug that might cause a table to be scanned in the wrong direction (thus reversing the order of output) when a DESC index is used to implement the ORDER BY clause on a query that has an identical GROUP BY clause. Ticket [ba7cbfaedc7e6](https://sqlite.org/src/info/ba7cbfaedc7e6).
14. Fix a bug in [sqlite3_trace()](c3ref/profile.md) that was causing it to sometimes fail to print an SQL statement if that statement needed to be re-prepared. Ticket [11d5aa455e0d98f3c1e6a08](https://sqlite.org/src/info/11d5aa455e0d98f3c1e6a08)
15. Fix a faulty assert() statement. Ticket [369d57fb8e5ccdff06f1](https://sqlite.org/src/info/369d57fb8e5ccdff06f1)
    **Test, Debug, and Analysis Changes:**
16. Show ASCII-art abstract syntax tree diagrams using the ".selecttrace" and ".wheretrace" commands in the [command-line shell](cli.md) when compiled with [SQLITE_DEBUG](compile.md#debug), SQLITE_ENABLE_SELECTTRACE, and SQLITE_ENABLE_WHERETRACE. Also provide the sqlite3TreeViewExpr() and sqlite3TreeViewSelect() entry points that can be invoked from with the debugger to show the parse tree when stopped at a breakpoint.
17. Drop support for SQLITE_ENABLE_TREE_EXPLAIN. The SELECTTRACE mechanism provides more useful diagnostics information.
18. New options to the [command-line shell](cli.md) for configuring auxiliary memory usage: --pagecache, --lookaside, and --scratch.
19. SQLITE_SOURCE_ID: "2014-10-17 11:24:17 e4ab094f8afce0817f4074e823fabe59fc29ebb4"
20. SHA1 for sqlite3.c: 56dcf5e931a9e1fa12fc2d600cd91d3bf9b639cd

<span id="version_3_8_6"></span>

### 2014-08-15 (3.8.6)

1.  Added support for [hexadecimal integer literals](lang_expr.md#hexint) in the SQL parser. (Ex: 0x123abc)
2.  Enhanced the [PRAGMA integrity_check](pragma.md#pragma_integrity_check) command to detect [UNIQUE](lang_createtable.md#uniqueconst) and [NOT NULL](lang_createtable.md#notnullconst) constraint violations.
3.  Increase the maximum value of [SQLITE_MAX_ATTACHED](limits.md#max_attached) from 62 to 125.
4.  Increase the timeout in [WAL mode](wal.md) before issuing an [SQLITE_PROTOCOL](rescode.md#protocol) error from 1 second to 10 seconds.
5.  Added the [likely(X)](lang_corefunc.md#likely) SQL function.
6.  The [unicode61](fts3.md#unicode61) tokenizer is now included in [FTS4](fts3.md#fts4) by default.
7.  Trigger automatic reprepares on all prepared statements when [ANALYZE](lang_analyze.md) is run.
8.  Added a new [loadable extension](loadext.md) source code file to the source tree: [fileio.c](https://sqlite.org/src/finfo?name=ext/misc/fileio.c)
9.  Add extension functions [readfile(X) and writefile(X,Y)](cli.md#fileio) (using code copy/pasted from fileio.c in the previous bullet) to the [command-line shell](cli.md).
10. Added the [.fullschema](cli.md#fullschema) dot-command to the [command-line shell](cli.md).
    **Performance Enhancements:**
11. Deactivate the [DISTINCT](lang_select.md#distinct) keyword on subqueries on the right-hand side of the [IN operator](lang_expr.md#in_op).
12. Add the capability of evaluating an [IN operator](lang_expr.md#in_op) as a sequence of comparisons as an alternative to using a table lookup. Use the sequence of comparisons implementation in circumstances where it is likely to be faster, such as when the right-hand side of the IN operator is small and/or changes frequently.
13. The query planner now uses [sqlite_stat4](fileformat2.md#stat4tab) information (created by [ANALYZE](lang_analyze.md)) to help determine if the [skip-scan optimization](optoverview.md#skipscan) is appropriate.
14. Ensure that the query planner never tries to use a self-made transient index in place of a schema-defined index.
15. Other minor tweaks to improve the quality of [VDBE](opcode.md) code.
    **Bug Fixes:**
16. Fix a bug in [CREATE UNIQUE INDEX](lang_createindex.md), introduced when [WITHOUT ROWID](withoutrowid.md) support added in version 3.8.2, that allows a non-unique NOT NULL column to be given a UNIQUE index. Ticket [9a6daf340df99ba93c](https://sqlite.org/src/info/9a6daf340df99ba93c)
17. Fix a bug in [R-Tree extension](rtree.md), introduced in the previous release, that can cause an incorrect results for queries that use the rowid of the R-Tree on the left-hand side of an [IN operator](lang_expr.md#in_op). Ticket [d2889096e7bdeac6](https://sqlite.org/src/info/d2889096e7bdeac6).
18. Fix the [sqlite3_stmt_busy()](c3ref/stmt_busy.md) interface so that it gives the correct answer for [ROLLBACK](lang_transaction.md) statements that have been stepped but never reset.
19. Fix a bug in that would cause a null pointer to be dereferenced if a column with a DEFAULT that is an aggregate function tried to usee its DEFAULT. Ticket [3a88d85f36704eebe1](https://sqlite.org/src/info/3a88d85f36704eebe1)
20. CSV output from the [command-line shell](cli.md) now always uses CRLF for the row separator and avoids inserting CR in front of NLs contained in data.
21. Fix a [column affinity](datatype3.md#affinity) problem with the [IN operator](lang_expr.md#in_op). Ticket [9a8b09f8e6](https://sqlite.org/src/info/9a8b09f8e6).
22. Fix the [ANALYZE](lang_analyze.md) command so that it adds correct samples for [WITHOUT ROWID](withoutrowid.md) tables in the [sqlite_stat4](fileformat2.md#stat4tab) table. Ticket [b2fa5424e6fcb15](https://sqlite.org/src/info/b2fa5424e6fcb15).
23. SQLITE_SOURCE_ID: "2014-08-15 11:46:33 9491ba7d738528f168657adb43a198238abde19e"
24. SHA1 for sqlite3.c: 72c64f05cd9babb9c0f9b3c82536d83be7804b1c

<span id="version_3_8_5"></span>

### 2014-06-04 (3.8.5)

1.  Added support for [partial sorting by index](queryplanner.md#partialsort).
2.  Enhance the query planner so that it always prefers an index that uses a superset of WHERE clause terms relative to some other index.
3.  Improvements to the [automerge command](fts3.md#*fts4automergecmd) of [FTS4](fts3.md#fts4) to better control the index size for a full-text index that is subject to a large number of updates.
4.  Added the [sqlite3_rtree_query_callback()](rtree.md#xquery) interface to [R-Tree extension](rtree.md)
5.  Added new [URI query parameters](uri.md#coreqp) "nolock" and "immutable".
6.  Use less memory by not remembering CHECK constraints on read-only database connections.
7.  Enable the [OR optimization](queryplanner.md#or_in_where) for [WITHOUT ROWID](withoutrowid.md) tables.
8.  Render expressions of the form "x IN (?)" (with a single value in the list on the right-hand side of the IN operator) as if they where "x==?", Similarly optimize "x NOT IN (?)"
9.  Add the ".system" and ".once" commands to the [command-line shell](cli.md).
10. Added the [SQLITE_IOCAP_IMMUTABLE](c3ref/c_iocap_atomic.md) bit to the set of bits that can be returned by the xDeviceCharacteristics method of a [VFS](vfs.md).
11. Added the [SQLITE_TESTCTRL_BYTEORDER](c3ref/c_testctrl_always.md) test control.
    **Bug Fixes:**
12. OFFSET clause ignored on queries without a FROM clause. Ticket [07d6a0453d](https://sqlite.org/src/info/07d6a0453d)
13. Assertion fault on queries involving expressions of the form "x IN (?)". Ticket [e39d032577](https://sqlite.org/src/info/e39d032577).
14. Incorrect column datatype reported. Ticket [a8a0d2996a](https://sqlite.org/src/info/a8a0d2996a)
15. Duplicate row returned on a query against a table with more than 16 indices, each on a separate column, and all used via OR-connected constraints. Ticket [10fb063b11](https://sqlite.org/src/info/10fb063b11)
16. Partial index causes assertion fault on UPDATE OR REPLACE. Ticket [2ea3e9fe63](https://sqlite.org/src/info/2ea3e9fe63)
17. Crash when calling undocumented SQL function sqlite_rename_parent() with NULL parameters. Ticket [264b970c43](https://sqlite.org/src/info/264b970c4379fd)
18. ORDER BY ignored if the query has an identical GROUP BY. Ticket [b75a9ca6b0](https://sqlite.org/src/info/b75a9ca6b0499)
19. The group_concat(x,'') SQL function returns NULL instead of an empty string when all inputs are empty strings. Ticket [55746f9e65](https://sqlite.org/src/info/55746f9e65f85)
20. Fix a bug in the VDBE code generator that caused crashes when doing an INSERT INTO ... SELECT statement where the number of columns being inserted is larger than the number of columns in the destination table. Ticket [e9654505cfd](https://sqlite.org/src/info/e9654505cfda9)
21. Fix a problem in CSV import in the [command-line shell](cli.md) where if the leftmost field of the first row in the CSV file was both zero bytes in size and unquoted no data would be imported.
22. Fix a problem in FTS4 where the left-most column that contained the [notindexed column](fts3.md#fts4notindexed) name as a prefix was not indexed rather than the column whose name matched exactly.
23. Fix the [sqlite3_db_readonly()](c3ref/db_readonly.md) interface so that it returns true if the database is read-only due to the file format write version number being too large.
24. SQLITE_SOURCE_ID: "2014-06-04 14:06:34 b1ed4f2a34ba66c29b130f8d13e9092758019212"
25. SHA1 for sqlite3.c: 7bc194957238c61b1a47f301270286be5bc5208c

<span id="version_3_8_4_3"></span>

### 2014-04-03 (3.8.4.3)

1.  Add a [one-character fix](https://sqlite.org/src/fdiff?sbs=1&v1=7d539cedb1c&v2=ebad891b7494d&smhdr) for a problem that might cause incorrect query results on a query that mixes DISTINCT, GROUP BY in a subquery, and ORDER BY. [Ticket 98825a79ce14](https://sqlite.org/src/info/98825a79ce1456863).
2.  SQLITE_SOURCE_ID: "2014-04-03 16:53:12 a611fa96c4a848614efe899130359c9f6fb889c3"
3.  SHA1 for sqlite3.c: 310a1faeb9332a3cd8d1f53b4a2e055abf537bdc

<span id="version_3_8_4_2"></span>

### 2014-03-26 (3.8.4.2)

1.  Fix a potential buffer overread that could result when trying to search a corrupt database file.
2.  SQLITE_SOURCE_ID: "2014-03-26 18:51:19 02ea166372bdb2ef9d8dfbb05e78a97609673a8e"
3.  SHA1 for sqlite3.c: 4685ca86c2ea0649ed9f59a500013e90b3fe6d03

<span id="version_3_8_4_1"></span>

### 2014-03-11 (3.8.4.1)

1.  Work around a C-preprocessor macro conflict that breaks the build for some configurations with Microsoft Visual Studio.
2.  When computing the cost of the [skip-scan optimization](optoverview.md#skipscan), take into account the fact that multiple seeks are required.
3.  SQLITE_SOURCE_ID: "2014-03-11 15:27:36 018d317b1257ce68a92908b05c9c7cf1494050d0"
4.  SHA1 for sqlite3.c: d5cd1535053a50aa8633725e3595740b33709ac5

<span id="version_3_8_4"></span>

### 2014-03-10 (3.8.4)

1.  Code optimization and refactoring for improved performance.
2.  Add the ".clone" and ".save" commands to the command-line shell.
3.  Update the banner on the command-line shell to alert novice users when they are using an ephemeral in-memory database.
4.  Fix editline support in the command-line shell.
5.  Add support for coverage testing of VDBE programs using the [SQLITE_TESTCTRL_VDBE_COVERAGE](c3ref/c_testctrl_always.md) verb of [sqlite3_test_control()](c3ref/test_control.md).
6.  Update the \_FILE_OFFSET_BITS macro so that builds work again on QNX.
7.  Change the datatype of SrcList.nSrc from type u8 to type int to work around an issue in the C compiler on AIX.
8.  Get extension loading working on Cygwin.
9.  Bug fix: Fix the [char()](lang_corefunc.md#char) SQL function so that it returns an empty string rather than an "out of memory" error when called with zero arguments.
10. Bug fix: DISTINCT now recognizes that a [zeroblob](lang_corefunc.md#zeroblob) and a blob of all 0x00 bytes are the same thing. [Ticket \[fccbde530a\]](https://sqlite.org/src/info/fccbde530a)
11. Bug fix: Compute the correct answer for queries that contain an IS NOT NULL term in the WHERE clause and also contain an OR term in the WHERE clause and are compiled with [SQLITE_ENABLE_STAT4](compile.md#enable_stat4). [Ticket \[4c86b126f2\]](https://sqlite.org/src/info/4c86b126f2)
12. Bug fix: Make sure "rowid" columns are correctly resolved in joins between normal tables and WITHOUT ROWID tables. [Ticket \[c34d0557f7\]](https://sqlite.org/src/info/c34d0557f7)
13. Bug fix: Make sure the same temporary registers are not used in concurrent co-routines used to implement compound SELECT statements containing ORDER BY clauses, as such use can lead to incorrect answers. [Ticket \[8c63ff0eca\]](https://sqlite.org/src/info/8c63ff0eca)
14. Bug fix: Ensure that "ORDER BY random()" clauses do not get optimized out. [Ticket \[65bdeb9739\]](https://sqlite.org/src/info/65bdeb9739)
15. Bug fix: Repair a name-resolution error that can occur in sub-select statements contained within a TRIGGER. [Ticket \[4ef7e3cfca\]](https://sqlite.org/src/info/4ef7e3cfca)
16. Bug fix: Fix column default values expressions of the form "DEFAULT(-(-9223372036854775808))" so that they work correctly, initializing the column to a floating point value approximately equal to +9223372036854775808.0.
17. SQLITE_SOURCE_ID: "2014-03-10 12:20:37 530a1ee7dc2435f80960ce4710a3c2d2bfaaccc5"
18. SHA1 for sqlite3.c: b0c22e5f15f5ba2afd017ecd990ea507918afe1c

<span id="version_3_8_3_1"></span>

### 2014-02-11 (3.8.3.1)

1.  Fix a bug (ticket [4c86b126f2](https://sqlite.org/src/info/4c86b126f2)) that causes rows to go missing on some queries with OR clauses and IS NOT NULL operators in the WHERE clause, when the [SQLITE_ENABLE_STAT3](compile.md#enable_stat3) or [SQLITE_ENABLE_STAT4](compile.md#enable_stat4) compile-time options are used.
2.  Fix a harmless compiler warning that was causing problems for VS2013.
3.  SQLITE_SOURCE_ID: "2014-02-11 14:52:19 ea3317a4803d71d88183b29f1d3086f46d68a00e"
4.  SHA1 for sqlite3.c: 990004ef2d0eec6a339e4caa562423897fe02bf0

<span id="version_3_8_3"></span>

### 2014-02-03 (3.8.3)

1.  Added support for [common table expressions](lang_with.md) and the [WITH clause](lang_with.md).
2.  Added the [printf()](lang_corefunc.md#printf) SQL function.
3.  Added [SQLITE_DETERMINISTIC](c3ref/c_deterministic.md#sqlitedeterministic) as an optional bit in the 4th argument to the [sqlite3_create_function()](c3ref/create_function.md) and related interfaces, providing applications with the ability to create new functions that can be factored out of inner loops when they have constant arguments.
4.  Add [SQLITE_READONLY_DBMOVED](rescode.md#readonly_dbmoved) error code, returned at the beginning of a transaction, to indicate that the underlying database file has been renamed or moved out from under SQLite.
5.  Allow arbitrary expressions, including function calls and subqueries, in the filename argument to [ATTACH](lang_attach.md).
6.  Allow a [VALUES clause](lang_select.md#values) to be used anywhere a [SELECT](lang_select.md) statement is valid.
7.  Reseed the PRNG used by [sqlite3_randomness(N,P)](c3ref/randomness.md) when invoked with N==0. Automatically reseed after a fork() on unix.
8.  Enhance the [spellfix1](spellfix1.md) virtual table so that it can search efficiently by rowid.
9.  Performance enhancements.
10. Improvements to the comments in the VDBE byte-code display when running [EXPLAIN](lang_explain.md).
11. Add the "%token_class" directive to [Lemon parser generator](lemon.md) and use it to simplify the grammar.
12. Change the [Lemon](lemon.md) source code to avoid calling C-library functions that OpenBSD considers dangerous. (Ex: sprintf).
13. Bug fix: In the [command-line shell](cli.md) CSV import feature, do not end a field when an escaped double-quote occurs at the end of a CRLN line.
14. SQLITE_SOURCE_ID: "2014-02-03 13:52:03 e816dd924619db5f766de6df74ea2194f3e3b538"
15. SHA1 for sqlite3.c: 98a07da78f71b0275e8d9c510486877adc31dbee

<span id="version_3_8_2"></span>

### 2013-12-06 (3.8.2)

1.  Changed the defined behavior for the [CAST expression](lang_expr.md#castexpr) when floating point values greater than +9223372036854775807 are cast into integers so that the result is the largest possible integer, +9223372036854775807, instead of the smallest possible integer, -9223372036854775808. After this change, CAST(9223372036854775809.0 as INT) yields +9223372036854775807 instead of -9223372036854775808. **← Potentially Incompatible Change!**
2.  Added support for [WITHOUT ROWID](withoutrowid.md) tables.
3.  Added the [skip-scan optimization](optoverview.md#skipscan) to the query planner.
4.  Extended the [virtual table](vtab.md) interface, and in particular the [sqlite3_index_info](c3ref/index_info.md) object to allow a virtual table to report its estimate on the number of rows that will be returned by a query.
5.  Update the [R-Tree extension](rtree.md) to make use of the enhanced virtual table interface.
6.  Add the [SQLITE_ENABLE_EXPLAIN_COMMENTS](compile.md#enable_explain_comments) compile-time option.
7.  Enhanced the comments that are inserted into [EXPLAIN](lang_explain.md) output when the [SQLITE_ENABLE_EXPLAIN_COMMENTS](compile.md#enable_explain_comments) compile-time option is enabled.
8.  Performance enhancements in the VDBE, especially to the OP_Column opcode.
9.  Factor constant subexpressions in inner loops out to the initialization code in prepared statements.
10. Enhanced the ".explain" output formatting of the [command-line shell](cli.md) so that loops are indented to better show the structure of the program.
11. Enhanced the ".timer" feature of the [command-line shell](cli.md) so that it shows wall-clock time in addition to system and user times.
12. SQLITE_SOURCE_ID: "2013-12-06 14:53:30 27392118af4c38c5203a04b8013e1afdb1cebd0d"
13. SHA1 for sqlite3.c: 6422c7d69866f5ea3db0968f67ee596e7114544e

<span id="version_3_8_1"></span>

### 2013-10-17 (3.8.1)

1.  Added the [unlikely()](lang_corefunc.md#unlikely) and [likelihood()](lang_corefunc.md#likelihood) SQL functions to be used as hints to the query planner.
2.  Enhancements to the query planner:
    1.  Take into account the fact WHERE clause terms that cannot be used with indices still probably reduce the number of output rows.
    2.  Estimate the sizes of table and index rows and use the smallest applicable B-Tree for full scans and "count(\*)" operations.
3.  Added the [soft_heap_limit pragma](pragma.md#pragma_soft_heap_limit).
4.  Added support for [SQLITE_ENABLE_STAT4](compile.md#enable_stat4)
5.  Added support for "sz=NNN" parameters at the end of [sqlite_stat1.stat](fileformat2.md#stat1tab) fields used to specify the average length in bytes for table and index rows.
6.  Avoid running foreign-key constraint checks on an UPDATE if none of the modified columns are associated with foreign keys.
7.  Added the [SQLITE_MINIMUM_FILE_DESCRIPTOR](compile.md#minimum_file_descriptor) compile-time option
8.  Added the win32-longpath VFS on windows, permitting filenames up to 32K characters in length.
9.  The [Date And Time Functions](lang_datefunc.md) are enhanced so that the current time (ex: julianday('now')) is always the same for multiple function invocations within the same [sqlite3_step()](c3ref/step.md) call.
10. Add the "totype.c" extension, implementing the tointeger() and toreal() SQL functions.
11. [FTS4](fts3.md#fts4) queries are better able to make use of docid\<\$limit constraints to limit the amount of I/O required.
12. Added the hidden [fts4aux languageid column](fts3.md#f4alid) to the [fts4aux](fts3.md#fts4aux) virtual table.
13. The [VACUUM](lang_vacuum.md) command packs the database about 1% tighter.
14. The sqlite3_analyzer utility program is updated to provide better descriptions and to compute a more accurate estimate for "Non-sequential pages"
15. Refactor the implementation of PRAGMA statements to improve parsing performance.
16. The directory used to hold temporary files on unix can now be set using the SQLITE_TMPDIR environment variable, which takes precedence over the TMPDIR environment variable. The [sqlite3_temp_directory](c3ref/temp_directory.md) global variable still has higher precedence than both environment variables, however.
17. Added the [PRAGMA stats](pragma.md#pragma_stats) statement.
18. **Bug fix:** Return the correct answer for "SELECT count(\*) FROM table" even if there is a [partial index](partialindex.md) on the table. Ticket [a5c8ed66ca](https://sqlite.org/src/info/a5c8ed66ca).
19. SQLITE_SOURCE_ID: "2013-10-17 12:57:35 c78be6d786c19073b3a6730dfe3fb1be54f5657a"
20. SHA1 for sqlite3.c: 0a54d76566728c2ba96292a49b138e4f69a7c391

<span id="version_3_8_0_2"></span>

### 2013-09-03 (3.8.0.2)

1.  Fix a bug in the optimization that attempts to omit unused LEFT JOINs
2.  SQLITE_SOURCE_ID: "2013-09-03 17:11:13 7dd4968f235d6e1ca9547cda9cf3bd570e1609ef"
3.  SHA1 for sqlite3.c: 6cf0c7b46975a87a0dc3fba69c229a7de61b0c21

<span id="version_3_8_0_1"></span>

### 2013-08-29 (3.8.0.1)

1.  Fix an off-by-one error that caused quoted empty string at the end of a CRLF-terminated line of CSV input to be misread by the command-line shell.
2.  Fix a query planner bug involving a LEFT JOIN with a BETWEEN or LIKE/GLOB constraint and then another INNER JOIN to the right that involves an OR constraint.
3.  Fix a query planner bug that could result in a segfault when querying tables with a UNIQUE or PRIMARY KEY constraint with more than four columns.
4.  SQLITE_SOURCE_ID: "2013-08-29 17:35:01 352362bc01660edfbda08179d60f09e2038a2f49"
5.  SHA1 for sqlite3.c: 99906bf63e6cef63d6f3d7f8526ac4a70e76559e

<span id="version_3_8_0"></span>

### 2013-08-26 (3.8.0)

1.  Add support for [partial indexes](partialindex.md)
2.  Cut-over to the [next generation query planner](queryplanner-ng.md) for faster and better query plans.
3.  The [EXPLAIN QUERY PLAN](eqp.md) output no longer shows an estimate of the number of rows generated by each loop in a join.
4.  Added the [FTS4 notindexed option](fts3.md#fts4notindexed), allowing non-indexed columns in an FTS4 table.
5.  Added the [SQLITE_STMTSTATUS_VM_STEP](c3ref/c_stmtstatus_counter.md#sqlitestmtstatusvmstep) option to [sqlite3_stmt_status()](c3ref/stmt_status.md).
6.  Added the [cache_spill pragma](pragma.md#pragma_cache_spill).
7.  Added the [query_only pragma](pragma.md#pragma_query_only).
8.  Added the [defer_foreign_keys pragma](pragma.md#pragma_defer_foreign_keys) and the [sqlite3_db_status](c3ref/db_status.md)(db, [SQLITE_DBSTATUS_DEFERRED_FKS](c3ref/c_dbstatus_options.md#sqlitedbstatusdeferredfks),...) C-language interface.
9.  Added the "percentile()" function as a [loadable extension](loadext.md) in the ext/misc subdirectory of the source tree.
10. Added the [SQLITE_ALLOW_URI_AUTHORITY](compile.md#allow_uri_authority) compile-time option.
11. Add the [sqlite3_cancel_auto_extension(X)](c3ref/cancel_auto_extension.md) interface.
12. A running SELECT statement that lacks a FROM clause (or any other statement that never reads or writes from any database file) will not prevent a read transaction from closing.
13. Add the [SQLITE_DEFAULT_AUTOMATIC_INDEX](compile.md#default_automatic_index) compile-time option. Setting this option to 0 disables automatic indices by default.
14. Issue an [SQLITE_WARNING_AUTOINDEX](rescode.md#warning_autoindex) warning on the [SQLITE_CONFIG_LOG](c3ref/c_config_covering_index_scan.md#sqliteconfiglog) whenever the query planner uses an automatic index.
15. Added the [SQLITE_FTS3_MAX_EXPR_DEPTH](compile.md#fts3_max_expr_depth) compile-time option.
16. Added an optional 5th parameter defining the collating sequence to the next_char() extension SQL function.
17. The [SQLITE_BUSY_SNAPSHOT](rescode.md#busy_snapshot) extended error code is returned in WAL mode when a read transaction cannot be upgraded to a write transaction because the read is on an older snapshot.
18. Enhancements to the sqlite3_analyzer utility program to provide size information separately for each individual index of a table, in addition to the aggregate size.
19. Allow read transactions to be freely opened and closed by SQL statements run from within the implementation of [application-defined SQL functions](appfunc.md) if the function is called by a SELECT statement that does not access any database table.
20. Disable the use of posix_fallocate() on all (unix) systems unless the HAVE_POSIX_FALLOCATE compile-time option is used.
21. Update the ".import" command in the [command-line shell](cli.md) to support multi-line fields and correct RFC-4180 quoting and to issue warning and/or error messages if the input text is not strictly RFC-4180 compliant.
22. Bug fix: In the [unicode61](fts3.md#unicode61) tokenizer of [FTS4](fts3.md#fts4), treat all private code points as identifier symbols.
23. Bug fix: Bare identifiers in ORDER BY clauses bind more tightly to output column names, but identifiers in expressions bind more tightly to input column names. Identifiers in GROUP BY clauses always prefer output column names, however.
24. Bug fixes: Multiple problems in the legacy query optimizer were fixed by the move to [NGQP](queryplanner-ng.md).
25. SQLITE_SOURCE_ID: "2013-08-26 04:50:08 f64cd21e2e23ed7cff48f7dafa5e76adde9321c2"
26. SHA1 for sqlite3.c: b7347f4b4c2a840e6ba12040093d606bd16ea21e

<span id="version_3_7_17"></span>

### 2013-05-20 (3.7.17)

1.  Add support for [memory-mapped I/O](mmap.md).
2.  Add the [sqlite3_strglob()](c3ref/strglob.md) convenience interface.
3.  Assigned the integer at offset 68 in the [database header](fileformat2.md#database_header) as the [Application ID](fileformat2.md#appid) for when SQLite is used as an [application file-format](appfileformat.md). Added the [PRAGMA application_id](pragma.md#pragma_application_id) command to query and set the Application ID.
4.  Report rollback recovery in the [error log](errlog.md) as SQLITE_NOTICE_RECOVER_ROLLBACK. Change the error log code for WAL recover from SQLITE_OK to SQLITE_NOTICE_RECOVER_WAL.
5.  Report the risky uses of [unlinked database files](howtocorrupt.md#unlink) and [database filename aliasing](howtocorrupt.md#alias) as SQLITE_WARNING messages in the [error log](errlog.md).
6.  Added the [SQLITE_TRACE_SIZE_LIMIT](compile.md#trace_size_limit) compile-time option.
7.  Increase the default value of [SQLITE_MAX_SCHEMA_RETRY](compile.md#max_schema_retry) to 50 and make sure that it is honored in every place that a schema change might force a statement retry.
8.  Add a new test harness called "mptester" used to verify correct operation when multiple processes are using the same database file at the same time.
9.  Enhance the [extension loading](loadext.md) mechanism to be more flexible (while still maintaining backwards compatibility) in two ways:
    1.  If the default entry point "sqlite3_extension_init" is not present in the loadable extension, also try an entry point "sqlite3_X_init" where "X" is based on the shared library filename. This allows every extension to have a different entry point, which allows them to be statically linked with no code changes.
    2.  The shared library filename passed to [sqlite3_load_extension()](c3ref/load_extension.md) may omit the filename suffix, and an appropriate architecture-dependent suffix (".so", ".dylib", or ".dll") will be added automatically.
10. Added many new loadable extensions to the source tree, including amatch, closure, fuzzer, ieee754, nextchar, regexp, spellfix, and wholenumber. See header comments on each extension source file for further information about what that extension does.
11. Enhance [FTS3](fts3.md) to avoid using excess stack space when there are a huge number of terms on the right-hand side of the MATCH operator. A side-effect of this change is that the MATCH operator can only accommodate 12 NEAR operators at a time.
12. Enhance the [fts4aux](fts3.md#fts4aux) virtual table so that it can be a TEMP table.
13. Added the [fts3tokenize virtual table](fts3.md#fts3tok) to the [full-text search](fts3.md) logic.
14. Query planner enhancement: Use the transitive property of constraints to move constraints into the outer loops of a join whenever possible, thereby reducing the amount of work that needs to occur in inner loops.
15. Discontinue the use of posix_fallocate() on unix, as it does not work on all filesystems.
16. Improved tracing and debugging facilities in the Windows [VFS](vfs.md).
17. Bug fix: Fix a potential **database corruption bug** in [shared cache mode](sharedcache.md) when one [database connection](c3ref/sqlite3.md) is closed while another is in the middle of a write transaction. Ticket [e636a050b7](https://sqlite.org/src/info/e636a050b7)
18. Bug fix: Only consider AS names from the result set as candidates for resolving identifiers in the WHERE clause if there are no other matches. In the ORDER BY clause, AS names take priority over any column names. Ticket [2500cdb9be05](https://sqlite.org/src/info/2500cdb9be05)
19. Bug fix: Do not allow a virtual table to cancel the ORDER BY clause unless all outer loops are guaranteed to return no more than one row result. Ticket [ba82a4a41eac1](https://sqlite.org/src/info/ba82a4a41eac1).
20. Bug fix: Do not suppress the ORDER BY clause on a virtual table query if an IN constraint is used. Ticket [f69b96e3076e](https://sqlite.org/src/info/f69b96e3076e).
21. Bug fix: The [command-line shell](cli.md) gives an exit code of 0 when terminated using the ".quit" command.
22. Bug fix: Make sure [PRAGMA](pragma.md#syntax) statements appear in [sqlite3_trace()](c3ref/profile.md) output.
23. Bug fix: When a [compound query](lang_select.md#compound) that uses an ORDER BY clause with a [COLLATE operator](lang_expr.md#collateop), make sure that the sorting occurs according to the specified collation and that the comparisons associate with the compound query use the native collation. Ticket [6709574d2a8d8](https://sqlite.org/src/info/6709574d2a8d8).
24. Bug fix: Makes sure the [authorizer](c3ref/set_authorizer.md) callback gets a valid pointer to the string "ROWID" for the column-name parameter when doing an [UPDATE](lang_update.md) that changes the rowid. Ticket [0eb70d77cb05bb2272](https://sqlite.org/src/info/0eb70d77cb05bb2272)
25. Bug fix: Do not move WHERE clause terms inside OR expressions that are contained within an ON clause of a LEFT JOIN. Ticket [f2369304e4](https://sqlite.org/src/info/f2369304e4)
26. Bug fix: Make sure an error is always reported when attempting to preform an operation that requires a [collating sequence](datatype3.md#collation) that is missing. Ticket [0fc59f908b](https://sqlite.org/src/info/0fc59f908b)
27. SQLITE_SOURCE_ID: "2013-05-20 00:56:22 118a3b35693b134d56ebd780123b7fd6f1497668"
28. SHA1 for sqlite3.c: 246987605d0503c700a08b9ee99a6b5d67454aab

<span id="version_3_7_16_2"></span>

### 2013-04-12 (3.7.16.2)

1.  Fix a bug (present since version 3.7.13) that could result in database corruption on windows if two or more processes try to access the same database file at the same time and immediately after third process crashed in the middle of committing to that same file. See ticket [7ff3120e4f](https://sqlite.org/src/info/7ff3120e4f) for further information.
2.  SQLITE_SOURCE_ID: "2013-04-12 11:52:43 cbea02d93865ce0e06789db95fd9168ebac970c7"
3.  SHA1 for sqlite3.c: d466b54789dff4fb0238b9232e74896deaefab94

<span id="version_3_7_16_1"></span>

### 2013-03-29 (3.7.16.1)

1.  Fix for a bug in the ORDER BY optimizer that was introduced in [version 3.7.15](#version_3_7_15) which would sometimes optimize out the sorting step when in fact the sort was required. Ticket [a179fe7465](https://sqlite.org/src/info/a179fe7465)
2.  Fix a long-standing bug in the [CAST expression](lang_expr.md#castexpr) that would recognize UTF16 characters as digits even if their most-significant-byte was not zero. Ticket [689137afb6da41](https://sqlite.org/src/info/689137afb6da41).
3.  Fix a bug in the NEAR operator of [FTS3](fts3.md) when applied to subfields. Ticket [38b1ae018f](https://sqlite.org/src/info/38b1ae018f).
4.  Fix a long-standing bug in the storage engine that would (very rarely) cause a spurious report of an SQLITE_CORRUPT error but which was otherwise harmless. Ticket [6bfb98dfc0c](https://sqlite.org/src/info/6bfb98dfc0c).
5.  The SQLITE_OMIT_MERGE_SORT option has been removed. The merge sorter is now a required component of SQLite.
6.  Fixed lots of spelling errors in the source-code comments
7.  SQLITE_SOURCE_ID: "2013-03-29 13:44:34 527231bc67285f01fb18d4451b28f61da3c4e39d"
8.  SHA1 for sqlite3.c: 7a91ceceac9bcf47ceb8219126276e5518f7ff5a

<span id="version_3_7_16"></span>

### 2013-03-18 (3.7.16)

1.  Added the [PRAGMA foreign_key_check](pragma.md#pragma_foreign_key_check) command.
2.  Added new extended error codes for all SQLITE_CONSTRAINT errors
3.  Added the SQLITE_READONLY_ROLLBACK extended error code for when a database cannot be opened because it needs rollback recovery but is read-only.
4.  Added SQL functions [unicode(A)](lang_corefunc.md#unicode) and [char(X1,...,XN)](lang_corefunc.md#char).
5.  Performance improvements for [PRAGMA incremental_vacuum](pragma.md#pragma_incremental_vacuum), especially in cases where the number of free pages is greater than what will fit on a single trunk page of the freelist.
6.  Improved optimization of queries containing aggregate min() or max().
7.  Enhance virtual tables so that they can potentially use an index when the WHERE clause contains the IN operator.
8.  Allow indices to be used for sorting even if prior terms of the index are constrained by IN operators in the WHERE clause.
9.  Enhance the [PRAGMA table_info](pragma.md#pragma_table_info) command so that the "pk" column is an increasing integer to show the order of columns in the primary key.
10. Enhance the query optimizer to exploit transitive join constraints.
11. Performance improvements in the query optimizer.
12. Allow the error message from [PRAGMA integrity_check](pragma.md#pragma_integrity_check) to be longer than 20000 bytes.
13. Improved name resolution for deeply nested queries.
14. Added the test_regexp.c module as a demonstration of how to implement the REGEXP operator.
15. Improved error messages in the [RTREE](rtree.md) extension.
16. Enhance the [command-line shell](cli.md) so that a non-zero argument to the ".exit" command causes the shell to exit immediately without cleanly shutting down the database connection.
17. Improved error messages for invalid boolean arguments to dot-commands in the [command-line shell](cli.md).
18. Improved error messages for "foreign key mismatch" showing the names of the two tables involved.
19. Remove all uses of umask() in the unix VFS.
20. Added the [PRAGMA vdbe_addoptrace](pragma.md#pragma_vdbe_addoptrace) and [PRAGMA vdbe_debug](pragma.md#pragma_vdbe_debug) commands.
21. Change to use strncmp() or the equivalent instead of memcmp() when comparing non-zero-terminated strings.
22. Update cygwin interfaces to omit deprecated API calls.
23. Enhance the [spellfix1](spellfix1.md) extension so that the edit distance cost table can be changed at runtime by inserting a string like 'edit_cost_table=TABLE' into the "command" field.
24. Bug fix: repair a long-standing problem that could cause incorrect query results in a 3-way or larger join that compared INTEGER fields against TEXT fields in two or more places. Ticket [fc7bd6358f](https://sqlite.org/src/info/fc7bd6358f)
25. Bug fix: Issue an error message if the 16-bit reference counter on a view overflows due to an overly complex query.
26. Bug fix: Avoid leaking memory on LIMIT and OFFSET clauses in deeply nested UNION ALL queries.
27. Bug fix: Make sure the schema is up-to-date prior to running pragmas table_info, index_list, index_info, and foreign_key_list.
28. SQLITE_SOURCE_ID: "2013-03-18 11:39:23 66d5f2b76750f3520eb7a495f6247206758f5b90"
29. SHA1 for sqlite3.c: 7308ab891ca1b2ebc596025cfe4dc36f1ee89cf6

<span id="version_3_7_15_2"></span>

### 2013-01-09 (3.7.15.2)

1.  Fix a bug, introduced in [version 3.7.15](#version_3_7_15), that causes an ORDER BY clause to be optimized out of a three-way join when the ORDER BY is actually required. Ticket [598f5f7596b055](https://sqlite.org/src/info/598f5f7596b055)
2.  SQLITE_SOURCE_ID: "2013-01-09 11:53:05 c0e09560d26f0a6456be9dd3447f5311eb4f238f"
3.  SHA1 for sqlite3.c: 5741f47d1bc38aa0a8c38f09e60a5fe0031f272d

<span id="version_3_7_15_1"></span>

### 2012-12-19 (3.7.15.1)

1.  Fix a bug, introduced in [version 3.7.15](#version_3_7_15), that causes a segfault if the AS name of a result column of a SELECT statement is used as a logical term in the WHERE clause. Ticket [a7b7803e8d1e869](https://sqlite.org/src/info/a7b7803e8d1e869).
2.  SQLITE_SOURCE_ID: "2012-12-19 20:39:10 6b85b767d0ff7975146156a99ad673f2c1a23318"
3.  SHA1 for sqlite3.c: bbbaa68061e925bd4d7d18d7e1270935c5f7e39a

<span id="version_3_7_15"></span>

### 2012-12-12 (3.7.15)

1.  Added the [sqlite3_errstr()](c3ref/errcode.md) interface.
2.  Avoid invoking the [sqlite3_trace()](c3ref/profile.md) callback multiple times when a statement is automatically reprepared due to [SQLITE_SCHEMA](rescode.md#schema) errors.
3.  Added support for Windows Phone 8 platforms
4.  Enhance IN operator processing to make use of indices with numeric affinities.
5.  Do full-table scans using covering indices when possible, under the theory that an index will be smaller and hence can be scanned with less I/O.
6.  Enhance the query optimizer so that ORDER BY clauses are more aggressively optimized, especially in joins where various terms of the ORDER BY clause come from separate tables of the join.
7.  Add the ability to implement FROM clause subqueries as coroutines rather that manifesting the subquery into a temporary table.
8.  Enhancements the command-line shell:
    1.  Added the ".print" command
    2.  Negative numbers in the ".width" command cause right-alignment
    3.  Add the ".wheretrace" command when compiled with SQLITE_DEBUG
9.  Added the [busy_timeout pragma](pragma.md#pragma_busy_timeout).
10. Added the [instr()](lang_corefunc.md#instr) SQL function.
11. Added the [SQLITE_FCNTL_BUSYHANDLER](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlbusyhandler) file control, used to allow VFS implementations to get access to the busy handler callback.
12. The xDelete method in the built-in [VFSes](vfs.md) now return SQLITE_IOERR_DELETE_NOENT if the file to be deleted does not exist.
13. Enhanced support for QNX.
14. Work around an optimizer bug in the MSVC compiler when targeting ARM.
15. Bug fix: Avoid various concurrency problems in [shared cache mode](sharedcache.md).
16. Bug fix: Avoid a deadlock or crash if the [backup API](backup.md), [shared cache](sharedcache.md), and the SQLite Encryption Extension are all used at once.
17. Bug fix: SQL functions created using the TCL interface honor the "nullvalue" setting.
18. Bug fix: Fix a 32-bit overflow problem on CREATE INDEX for databases larger than 16GB.
19. Bug fix: Avoid segfault when using the [COLLATE operator](lang_expr.md#collateop) inside of a [CHECK constraint](lang_createtable.md#ckconst) or [view](lang_createview.md) in [shared cache mode](sharedcache.md).
20. SQLITE_SOURCE_ID: "2012-12-12 13:36:53 cd0b37c52658bfdf992b1e3dc467bae1835a94ae"
21. SHA1 for sqlite3.c: 2b413611f5e3e3b6ef5f618f2a9209cdf25cbcff"

<span id="version_3_7_14_1"></span>

### 2012-10-04 (3.7.14.1)

1.  Fix a bug (ticket [\[d02e1406a58ea02d\]\]](https://sqlite.org/src/tktview/d02e1406a58ea02d)) that causes a segfault on a LEFT JOIN that includes an OR in the ON clause.
2.  Work around a bug in the optimizer in the VisualStudio-2012 compiler that causes invalid code to be generated when compiling SQLite on ARM.
3.  Fix the TCL interface so that the "nullvalue" setting is honored for TCL implementations of SQL functions.
4.  SQLITE_SOURCE_ID: "2012-10-04 19:37:12 091570e46d04e84b67228e0bdbcd6e1fb60c6bdb"
5.  SHA1 for sqlite3.c: 62aaecaacab3a4bf4a8fe4aec1cfdc1571fe9a44

<span id="version_3_7_14"></span>

### 2012-09-03 (3.7.14)

1.  Drop built-in support for OS/2. If you need to upgrade an OS/2 application to use this or a later version of SQLite, then add an application-defined [VFS](vfs.md) using the [sqlite3_vfs_register()](c3ref/vfs_find.md) interface. The code removed in this release can serve as a baseline for the application-defined VFS.
2.  Ensure that floating point values are preserved exactly when reconstructing a database from the output of the ".dump" command of the [command-line shell](cli.md).
3.  Added the [sqlite3_close_v2()](c3ref/close.md) interface.
4.  Updated the [command-line shell](cli.md) so that it can be built using [SQLITE_OMIT_FLOATING_POINT](compile.md#omit_floating_point) and [SQLITE_OMIT_AUTOINIT](compile.md#omit_autoinit).
5.  Improvements to the windows makefiles and build processes.
6.  Enhancements to [PRAGMA integrity_check](pragma.md#pragma_integrity_check) and [PRAGMA quick_check](pragma.md#pragma_quick_check) so that they can optionally check just a single attached database instead of all attached databases.
7.  Enhancements to [WAL mode](wal.md) processing that ensure that at least one valid read-mark is available at all times, so that read-only processes can always read the database.
8.  Performance enhancements in the sorter used by ORDER BY and CREATE INDEX.
9.  Added the [SQLITE_DISABLE_FTS4_DEFERRED](compile.md#disable_fts4_deferred) compile-time option.
10. Better handling of aggregate queries where the aggregate functions are contained within subqueries.
11. Enhance the query planner so that it will try to use a [covering index](queryplanner.md#covidx) on queries that make use of [or optimization](optoverview.md#or_opt).
12. SQLITE_SOURCE_ID: "2012-09-03 15:42:36 c0d89d4a9752922f9e367362366efde4f1b06f2a"
13. SHA1 for sqlite3.c: 5fdf596b29bb426001f28b488ff356ae14d5a5a6

<span id="version_3_7_13"></span>

### 2012-06-11 (3.7.13)

1.  [In-memory databases](inmemorydb.md) that are specified using [URI filenames](uri.md) are allowed to use [shared cache](sharedcache.md#inmemsharedcache), so that the same in-memory database can be accessed from multiple database connections.
2.  Recognize and use the [mode=memory](uri.md#coreqp) query parameter in [URI filenames](uri.md).
3.  Avoid resetting the schema of [shared cache](sharedcache.md) connections when any one connection closes. Instead, wait for the last connection to close before resetting the schema.
4.  In the [RTREE](rtree.md) extension, when rounding 64-bit floating point numbers to 32-bit for storage, always round in a direction that causes the bounding box to get larger.
5.  Adjust the unix driver to avoid unnecessary calls to fchown().
6.  Add interfaces sqlite3_quota_ferror() and sqlite3_quota_file_available() to the test_quota.c module.
7.  The [sqlite3_create_module()](c3ref/create_module.md) and [sqlite3_create_module_v2()](c3ref/create_module.md) interfaces return SQLITE_MISUSE on any attempt to overload or replace a [virtual table](vtab.md) module. The destructor is always called in this case, in accordance with historical and current documentation.
8.  SQLITE_SOURCE_ID: "2012-06-11 02:05:22 f5b5a13f7394dc143aa136f1d4faba6839eaa6dc"
9.  SHA1 for sqlite3.c: ff0a771d6252545740ba9685e312b0e3bb6a641b

<span id="version_3_7_12_1"></span>

### 2012-05-22 (3.7.12.1)

1.  Fix a bug [(ticket c2ad16f997)](https://sqlite.org/src/info/c2ad16f997ee9c) in the 3.7.12 release that can cause a segfault for certain obscure nested aggregate queries.
2.  Fix various other minor test script problems.
3.  SQLITE_SOURCE_ID: "2012-05-22 02:45:53 6d326d44fd1d626aae0e8456e5fa2049f1ce0789"
4.  SHA1 for sqlite3.c: d494e8d81607f0515d4f386156fb0fd86d5ba7df

<span id="version_3_7_12"></span>

### 2012-05-14 (3.7.12)

1.  Add the [SQLITE_DBSTATUS_CACHE_WRITE](c3ref/c_dbstatus_options.md#sqlitedbstatuscachewrite) option for [sqlite3_db_status()](c3ref/db_status.md).
2.  Optimize the [typeof()](lang_corefunc.md#typeof) and [length()](lang_corefunc.md#length) SQL functions so that they avoid unnecessary reading of database content from disk.
3.  Add the [FTS4 "merge" command](fts3.md#*fts4mergecmd), the [FTS4 "automerge" command](fts3.md#*fts4automergecmd), and the [FTS4 "integrity-check" command](fts3.md#*fts4ickcmd).
4.  Report the name of specific [CHECK](lang_createtable.md#ckconst) constraints that fail.
5.  In the command-line shell, use popen() instead of fopen() if the first character of the argument to the ".output" command is "\|".
6.  Make use of OVERLAPPED in the windows [VFS](vfs.md) to avoid some system calls and thereby obtain a performance improvement.
7.  More aggressive optimization of the AND operator when one side or the other is always false.
8.  Improved performance of queries with many OR-connected terms in the WHERE clause that can all be indexed.
9.  Add the [SQLITE_RTREE_INT_ONLY](compile.md#rtree_int_only) compile-time option to force the [R\*Tree Extension Module](rtree.md) to use integer instead of floating point values for both storage and computation.
10. Enhance the [PRAGMA integrity_check](pragma.md#pragma_integrity_check) command to use much less memory when processing multi-gigabyte databases.
11. New interfaces added to the test_quota.c add-on module.
12. Added the ".trace" dot-command to the command-line shell.
13. Allow virtual table constructors to be invoked recursively.
14. Improved optimization of ORDER BY clauses on compound queries.
15. Improved optimization of aggregate subqueries contained within an aggregate query.
16. Bug fix: Fix the [RELEASE](lang_savepoint.md) command so that it does not cancel pending queries. This repairs a problem introduced in 3.7.11.
17. Bug fix: Do not discard the DISTINCT as superfluous unless a subset of the result set is subject to a UNIQUE constraint *and* it none of the columns in that subset can be NULL. Ticket [385a5b56b9](https://sqlite.org/src/info/385a5b56b9).
18. Bug fix: Do not optimize away an ORDER BY clause that has the same terms as a UNIQUE index unless those terms are also NOT NULL. Ticket [2a5629202f](https://sqlite.org/src/info/2a5629202f).
19. SQLITE_SOURCE_ID: "2012-05-14 01:41:23 8654aa9540fe9fd210899d83d17f3f407096c004"
20. SHA1 for sqlite3.c: 57e2104a0f7b3f528e7f6b7a8e553e2357ccd2e1

<span id="version_3_7_11"></span>

### 2012-03-20 (3.7.11)

1.  Enhance the [INSERT](lang_insert.md) syntax to allow multiple rows to be inserted via the VALUES clause.
2.  Enhance the [CREATE VIRTUAL TABLE](lang_createvtab.md) command to support the IF NOT EXISTS clause.
3.  Added the [sqlite3_stricmp()](c3ref/stricmp.md) interface as a counterpart to [sqlite3_strnicmp()](c3ref/stricmp.md).
4.  Added the [sqlite3_db_readonly()](c3ref/db_readonly.md) interface.
5.  Added the [SQLITE_FCNTL_PRAGMA](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlpragma) file control, giving [VFS](vfs.md) implementations the ability to add new [PRAGMA](pragma.md#syntax) statements or to override built-in PRAGMAs.
6.  Queries of the form: "SELECT max(x), y FROM table" returns the value of y on the same row that contains the maximum x value.
7.  Added support for the [FTS4 languageid option](fts3.md#*fts4languageid).
8.  Documented support for the [FTS4 content option](fts3.md#*fts4content). This feature has actually been in the code since [version 3.7.9](#version_3_7_9) but is only now considered to be officially supported.
9.  Pending statements no longer block [ROLLBACK](lang_transaction.md). Instead, the pending statement will return SQLITE_ABORT upon next access after the ROLLBACK.
10. Improvements to the handling of CSV inputs in the [command-line shell](cli.md)
11. Fix a [bug](https://sqlite.org/src/info/b7c8682cc1) introduced in [version 3.7.10](#version_3_7_10) that might cause a LEFT JOIN to be incorrectly converted into an INNER JOIN if the WHERE clause indexable terms connected by OR.
12. SQLITE_SOURCE_ID: "2012-03-20 11:35:50 00bb9c9ce4f465e6ac321ced2a9d0062dc364669"
13. SHA1 for sqlite3.c: d460d7eda3a9dccd291aed2a9fda868b9b120a10

<span id="version_3_7_10"></span>

### 2012-01-16 (3.7.10)

1.  The default [schema format number](fileformat2.md#schemaformat) is changed from 1 to 4. This means that, unless the [PRAGMA legacy_file_format=ON](pragma.md#pragma_legacy_file_format) statement is run, newly created database files will be unreadable by version of SQLite prior to 3.3.0 (2006-01-10). It also means that the [descending indices](lang_createindex.md#descidx) are enabled by default.
2.  The sqlite3_pcache_methods structure and the [SQLITE_CONFIG_PCACHE](c3ref/c_config_covering_index_scan.md#sqliteconfigpcache) and [SQLITE_CONFIG_GETPCACHE](c3ref/c_config_covering_index_scan.md#sqliteconfiggetpcache) configuration parameters are deprecated. They are replaced by a new [sqlite3_pcache_methods2](c3ref/pcache_methods2.md) structure and [SQLITE_CONFIG_PCACHE2](c3ref/c_config_covering_index_scan.md#sqliteconfigpcache2) and [SQLITE_CONFIG_GETPCACHE2](c3ref/c_config_covering_index_scan.md#sqliteconfiggetpcache2) configuration parameters.
3.  Added the [powersafe overwrite](psow.md) property to the VFS interface. Provide the [SQLITE_IOCAP_POWERSAFE_OVERWRITE](c3ref/c_iocap_atomic.md) I/O capability, the [SQLITE_POWERSAFE_OVERWRITE](compile.md#powersafe_overwrite) compile-time option, and the "psow=BOOLEAN" query parameter for [URI filenames](uri.md).
4.  Added the [sqlite3_db_release_memory()](c3ref/db_release_memory.md) interface and the [shrink_memory pragma](pragma.md#pragma_shrink_memory).
5.  Added the [sqlite3_db_filename()](c3ref/db_filename.md) interface.
6.  Added the [sqlite3_stmt_busy()](c3ref/stmt_busy.md) interface.
7.  Added the [sqlite3_uri_boolean()](c3ref/uri_boolean.md) and [sqlite3_uri_int64()](c3ref/uri_boolean.md) interfaces.
8.  If the argument to [PRAGMA cache_size](pragma.md#pragma_cache_size) is negative N, that means to use approximately -1024\*N bytes of memory for the page cache regardless of the page size.
9.  Enhanced the default memory allocator to make use of \_msize() on windows, malloc_size() on Mac, and malloc_usable_size() on Linux.
10. Enhanced the query planner to support index queries with range constraints on the rowid.
11. Enhanced the query planner flattening logic to allow UNION ALL compounds to be promoted upwards to replace a simple wrapper SELECT even if the compounds are joins.
12. Enhanced the query planner so that the xfer optimization can be used with INTEGER PRIMARY KEY ON CONFLICT as long as the destination table is initially empty.
13. Enhanced the windows [VFS](vfs.md) so that all system calls can be overridden using the xSetSystemCall interface.
14. Updated the "unix-dotfile" [VFS](vfs.md) to use locking directories with mkdir() and rmdir() instead of locking files with open() and unlink().
15. Enhancements to the test_quota.c extension to support stdio-like interfaces with quotas.
16. Change the unix [VFS](vfs.md) to be tolerant of read() system calls that return less then the full number of requested bytes.
17. Change both unix and windows [VFSes](vfs.md) to report a sector size of 4096 instead of the old default of 512.
18. In the [TCL Interface](tclsqlite.md), add the -uri option to the "sqlite3" TCL command used for creating new database connection objects.
19. Added the [SQLITE_TESTCTRL_EXPLAIN_STMT](c3ref/c_testctrl_always.md) test-control option with the [SQLITE_ENABLE_TREE_EXPLAIN](compile.md#enable_tree_explain) compile-time option to enable the [command-line shell](cli.md) to display ASCII-art parse trees of SQL statements that it processes, for debugging and analysis.
20. **Bug fix:** Add an additional xSync when restarting a WAL in order to prevent an exceedingly unlikely but theoretically possible database corruption following power-loss. Ticket [ff5be73dee](https://sqlite.org/src/info/ff5be73dee).
21. **Bug fix:** Change the VDBE so that all registers are initialized to Invalid instead of NULL. Ticket [7bbfb7d442](https://sqlite.org/src/info/7bbfb7d442)
22. **Bug fix:** Fix problems that can result from 32-bit integer overflow. Ticket [ac00f496b7e2](https://sqlite.org/src/info/ac0ff496b7e2)
23. SQLITE_SOURCE_ID: "2012-01-16 13:28:40 ebd01a8deffb5024a5d7494eef800d2366d97204"
24. SHA1 for sqlite3.c: 6497cbbaad47220bd41e2e4216c54706e7ae95d4

<span id="version_3_7_9"></span>

### 2011-11-01 (3.7.9)

1.  If a search token (on the right-hand side of the MATCH operator) in [FTS4](fts3.md#fts4) begins with "^" then that token must be the first in its field of the document. **\*\* Potentially Incompatible Change \*\***
2.  Added options [SQLITE_DBSTATUS_CACHE_HIT](c3ref/c_dbstatus_options.md#sqlitedbstatuscachehit) and [SQLITE_DBSTATUS_CACHE_MISS](c3ref/c_dbstatus_options.md#sqlitedbstatuscachemiss) to the [sqlite3_db_status()](c3ref/db_status.md) interface.
3.  Removed support for [SQLITE_ENABLE_STAT2](compile.md#enable_stat2), replacing it with the much more capable [SQLITE_ENABLE_STAT3](compile.md#enable_stat3) option.
4.  Enhancements to the sqlite3_analyzer utility program, including the --pageinfo and --stats options and support for multiplexed databases.
5.  Enhance the [sqlite3_data_count()](c3ref/data_count.md) interface so that it can be used to determine if SQLITE_DONE has been seen on the prepared statement.
6.  Added the [SQLITE_FCNTL_OVERWRITE](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntloverwrite) file-control by which the SQLite core indicates to the VFS that the current transaction will overwrite the entire database file.
7.  Increase the default [lookaside memory allocator](malloc.md#lookaside) allocation size from 100 to 128 bytes.
8.  Enhanced the query planner so that it can factor terms in and out of OR expressions in the WHERE clause in an effort to find better indices.
9.  Added the [SQLITE_DIRECT_OVERFLOW_READ](compile.md#direct_overflow_read) compile-time option, causing [overflow pages](fileformat2.md#ovflpgs) to be read directly from the database file, bypassing the [page cache](c3ref/pcache_methods2.md).
10. Remove limits on the magnitude of precision and width value in the format specifiers of the [sqlite3_mprintf()](c3ref/mprintf.md) family of string rendering routines.
11. Fix a bug that prevent [ALTER TABLE ... RENAME](lang_altertable.md) from working on some virtual tables in a database with a UTF16 encoding.
12. Fix a bug in ASCII-to-float conversion that causes slow performance and incorrect results when converting numbers with ridiculously large exponents.
13. Fix a bug that causes incorrect results in aggregate queries that use multiple aggregate functions whose arguments contain complicated expressions that differ only in the case of string literals contained within those expressions.
14. Fix a bug that prevented the [page_count](pragma.md#pragma_page_count) and [quick_check](pragma.md#pragma_quick_check) pragmas from working correctly if their names were capitalized.
15. Fix a bug that caused [VACUUM](lang_vacuum.md) to fail if the [count_changes pragma](pragma.md#pragma_count_changes) was engaged.
16. Fix a bug in [virtual table](vtab.md) implementation that causes a crash if an [FTS4](fts3.md#fts4) table is [dropped](lang_droptable.md) inside a transaction and a [SAVEPOINT](lang_savepoint.md) occurs afterwards.
17. SQLITE_SOURCE_ID: "2011-11-01 00:52:41 c7c6050ef060877ebe77b41d959e9df13f8c9b5e"
18. SHA1 for sqlite3.c: becd16877f4f9b281b91c97e106089497d71bb47

<span id="version_3_7_8"></span>

### 2011-09-19 (3.7.8)

1.  Orders of magnitude performance improvement for [CREATE INDEX](lang_createindex.md) on very large tables.
2.  Improved the windows VFS to better defend against interference from anti-virus software.
3.  Improved query plan optimization when the DISTINCT keyword is present.
4.  Allow more system calls to be overridden in the unix VFS - to provide better support for chromium sandboxes.
5.  Increase the default size of a lookahead cache line from 100 to 128 bytes.
6.  Enhancements to the test_quota.c module so that it can track preexisting files.
7.  Bug fix: Virtual tables now handle IS NOT NULL constraints correctly.
8.  Bug fixes: Correctly handle nested correlated subqueries used with indices in a WHERE clause.
9.  SQLITE_SOURCE_ID: "2011-09-19 14:49:19 3e0da808d2f5b4d12046e05980ca04578f581177"
10. SHA1 for sqlite3.c: bfcd74a655636b592c5dba6d0d5729c0f8e3b4de

<span id="version_3_7_7_1"></span>

### 2011-06-28 (3.7.7.1)

1.  Fix [a bug](https://sqlite.org/src/info/25ee812710) causing [PRAGMA case_sensitive_like](pragma.md#pragma_case_sensitive_like) statements compiled using sqlite3_prepare() to fail with an [SQLITE_SCHEMA](rescode.md#schema) error.
2.  SQLITE_SOURCE_ID: "2011-06-28 17:39:05 af0d91adf497f5f36ec3813f04235a6e195a605f"
3.  SHA1 for sqlite3.c: d47594b8a02f6cf58e91fb673e96cb1b397aace0

<span id="version_3_7_7"></span>

### 2011-06-23 (3.7.7)

1.  Add support for [URI filenames](uri.md)
2.  Add the [sqlite3_vtab_config()](c3ref/vtab_config.md) interface in support of [ON CONFLICT](lang_conflict.md) clauses with [virtual tables](vtab.md).
3.  Add the [xSavepoint](vtab.md#xsavepoint), [xRelease](vtab.md#xsavepoint) and [xRollbackTo](vtab.md#xsavepoint) methods in [virtual tables](vtab.md) in support of [SAVEPOINT](lang_savepoint.md) for virtual tables.
4.  Update the built-in [FTS3/FTS4](fts3.md) and [RTREE](rtree.md) virtual tables to support [ON CONFLICT](lang_conflict.md) clauses and [REPLACE](lang_replace.md).
5.  Avoid unnecessary reparsing of the database schema.
6.  Added support for the [FTS4 prefix option](fts3.md#fts4prefix) and the [FTS4 order option](fts3.md#fts4order).
7.  Allow [WAL-mode](wal.md) databases to be opened read-only as long as there is an existing read/write connection.
8.  Added support for [short filenames](shortnames.md).
9.  SQLITE_SOURCE_ID: "2011-06-23 19:49:22 4374b7e83ea0a3fbc3691f9c0c936272862f32f2"
10. SHA1 for sqlite3.c: 5bbe79e206ae5ffeeca760dbd0d66862228db551

<span id="version_3_7_6_3"></span>

### 2011-05-19 (3.7.6.3)

1.  Fix a problem with [WAL mode](wal.md) which could cause transactions to silently rollback if the [cache_size](pragma.md#pragma_cache_size) is set very small (less than 10) and SQLite comes under memory pressure.

<span id="version_3_7_6_2"></span>

### 2011-04-17 (3.7.6.2)

1.  Fix the function prototype for the open(2) system call to agree with POSIX. Without this fix, pthreads does not work correctly on NetBSD.
2.  SQLITE_SOURCE_ID: "2011-04-17 17:25:17 154ddbc17120be2915eb03edc52af1225eb7cb5e"
3.  SHA1 for sqlite3.c: 806577fd524dd5f3bfd8d4d27392ed2752bc9701

<span id="version_3_7_6_1"></span>

### 2011-04-13 (3.7.6.1)

1.  Fix a bug in 3.7.6 that only appears if the [SQLITE_FCNTL_SIZE_HINT](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlsizehint) file control is used with a build of SQLite that makes use of the HAVE_POSIX_FALLOCATE compile-time option and which has SQLITE_ENABLE_LOCKING_MODE turned off.
2.  SQLITE_SOURCE_ID: "2011-04-13 14:40:25 a35e83eac7b185f4d363d7fa51677f2fdfa27695"
3.  SHA1 for sqlite3.c: b81bfa27d3e09caf3251475863b1ce6dd9f6ab66

<span id="version_3_7_6"></span>

### 2011-04-12 (3.7.6)

1.  Added the [sqlite3_wal_checkpoint_v2()](c3ref/wal_checkpoint_v2.md) interface and enhanced the [wal_checkpoint pragma](pragma.md#pragma_wal_checkpoint) to support blocking checkpoints.
2.  Improvements to the query planner so that it makes better estimates of plan costs and hence does a better job of choosing the right plan, especially when [SQLITE_ENABLE_STAT2](compile.md#enable_stat2) is used.
3.  Fix a bug which prevented deferred foreign key constraints from being enforced when [sqlite3_finalize()](c3ref/finalize.md) was not called by one statement with a failed foreign key constraint prior to another statement with foreign key constraints running.
4.  Integer arithmetic operations that would have resulted in overflow are now performed using floating-point instead.
5.  Increased the version number on the [VFS object](c3ref/vfs.md) to 3 and added new methods xSetSysCall, xGetSysCall, and xNextSysCall used for doing full-coverage testing.
6.  Increase the maximum value of [SQLITE_MAX_ATTACHED](limits.md#max_attached) from 30 to 62 (though the default value remains at 10).
7.  Enhancements to FTS4:
    1.  Added the [fts4aux](fts3.md#fts4aux) table
    2.  Added support for [compressed FTS4 content](fts3.md#*fts4compression)
8.  Enhance the [ANALYZE](lang_analyze.md) command to support the name of an index as its argument, in order to analyze just that one index.
9.  Added the "unix-excl" built-in VFS on unix and unix-like platforms.
10. SQLITE_SOURCE_ID: "2011-04-12 01:58:40 f9d43fa363d54beab6f45db005abac0a7c0c47a7"
11. SHA1 for sqlite3.c: f38df08547efae0ff4343da607b723f588bbd66b

<span id="version_3_7_5"></span>

### 2011-02-01 (3.7.5)

1.  Added the [sqlite3_vsnprintf()](c3ref/mprintf.md) interface.
2.  Added the [SQLITE_DBSTATUS_LOOKASIDE_HIT](c3ref/c_dbstatus_options.md#sqlitedbstatuslookasidehit), [SQLITE_DBSTATUS_LOOKASIDE_MISS_SIZE](c3ref/c_dbstatus_options.md#sqlitedbstatuslookasidemisssize), and [SQLITE_DBSTATUS_LOOKASIDE_MISS_FULL](c3ref/c_dbstatus_options.md#sqlitedbstatuslookasidemissfull) options for the [sqlite3_db_status()](c3ref/db_status.md) interface.
3.  Added the [SQLITE_OMIT_AUTORESET](compile.md#omit_autoreset) compile-time option.
4.  Added the [SQLITE_DEFAULT_FOREIGN_KEYS](compile.md#default_foreign_keys) compile-time option.
5.  Updates to [sqlite3_stmt_readonly()](c3ref/stmt_readonly.md) so that its result is well-defined for all prepared statements and so that it works with [VACUUM](lang_vacuum.md).
6.  Added the "-heap" option to the [command-line shell](cli.md)
7.  Fix [a bug](https://sqlite.org/src/info/5d863f876e) involving frequent changes in and out of WAL mode and VACUUM that could (in theory) cause database corruption.
8.  Enhance the [sqlite3_trace()](c3ref/profile.md) mechanism so that nested SQL statements such as might be generated by virtual tables are shown but are shown in comments and without parameter expansion. This greatly improves tracing output when using the FTS3/4 and/or RTREE virtual tables.
9.  Change the xFileControl() methods on all built-in VFSes to return [SQLITE_NOTFOUND](rescode.md#notfound) instead of [SQLITE_ERROR](rescode.md#error) for an unrecognized operation code.
10. The SQLite core invokes the [SQLITE_FCNTL_SYNC_OMITTED](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlsyncomitted) [file control](c3ref/file_control.md) to the VFS in place of a call to xSync if the database has [PRAGMA synchronous](pragma.md#pragma_synchronous) set to OFF.

<span id="version_3_7_4"></span>

### 2010-12-07 (3.7.4)

1.  Added the [sqlite3_blob_reopen()](c3ref/blob_reopen.md) interface to allow an existing [sqlite3_blob](c3ref/blob.md) object to be rebound to a new row.
2.  Use the new [sqlite3_blob_reopen()](c3ref/blob_reopen.md) interface to improve the performance of FTS.
3.  [VFSes](c3ref/vfs.md) that do not support shared memory are allowed to access [WAL](wal.md) databases if [PRAGMA locking_mode](pragma.md#pragma_locking_mode) is set to EXCLUSIVE.
4.  Enhancements to [EXPLAIN QUERY PLAN](eqp.md).
5.  Added the [sqlite3_stmt_readonly()](c3ref/stmt_readonly.md) interface.
6.  Added [PRAGMA checkpoint_fullfsync](pragma.md#pragma_checkpoint_fullfsync).
7.  Added the [SQLITE_FCNTL_FILE_POINTER](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlfilepointer) option to [sqlite3_file_control()](c3ref/file_control.md).
8.  Added support for [FTS4](fts3.md#fts4) and enhancements to the FTS [matchinfo()](fts3.md#matchinfo) function.
9.  Added the test_superlock.c module which provides example code for obtaining an exclusive lock to a rollback or WAL database.
10. Added the test_multiplex.c module which provides an example VFS that provides multiplexing (sharding) of a DB, splitting it over multiple files of fixed size.
11. A [very obscure bug](https://sqlite.org/src/info/80ba201079) associated with the [or optimization](optoverview.md#or_opt) was fixed.

<span id="version_3_7_3"></span>

### 2010-10-08 (3.7.3)

1.  Added the [sqlite3_create_function_v2()](c3ref/create_function.md) interface that includes a destructor callback.
2.  Added support for [custom r-tree queries](rtree.md#customquery) using application-supplied callback routines to define the boundary of the query region.
3.  The default page cache strives more diligently to avoid using memory beyond what is allocated to it by [SQLITE_CONFIG_PAGECACHE](c3ref/c_config_covering_index_scan.md#sqliteconfigpagecache). Or if using page cache is allocating from the heap, it strives to avoid going over the [sqlite3_soft_heap_limit64()](c3ref/hard_heap_limit64.md), even if [SQLITE_ENABLE_MEMORY_MANAGEMENT](compile.md#enable_memory_management) is not set.
4.  Added the [sqlite3_soft_heap_limit64()](c3ref/hard_heap_limit64.md) interface as a replacement for [sqlite3_soft_heap_limit()](c3ref/soft_heap_limit.md).
5.  The [ANALYZE](lang_analyze.md) command now gathers statistics on tables even if they have no indices.
6.  Tweaks to the query planner to help it do a better job of finding the most efficient query plan for each query.
7.  Enhanced the internal text-to-numeric conversion routines so that they work with UTF8 or UTF16, thereby avoiding some UTF16-to-UTF8 text conversions.
8.  Fix a problem that was causing excess memory usage with large [WAL](wal.md) transactions in win32 systems.
9.  The interface between the VDBE and B-Tree layer is enhanced such that the VDBE provides hints to the B-Tree layer letting the B-Tree layer know when it is safe to use hashing instead of B-Trees for transient tables.
10. Miscellaneous documentation enhancements.

<span id="version_3_7_2"></span>

### 2010-08-24 (3.7.2)

1.  Fix an [old and very obscure bug](https://sqlite.org/src/info/5e10420e8d) that can lead to corruption of the database [free-page list](fileformat2.md#freelist) when [incremental_vacuum](pragma.md#pragma_incremental_vacuum) is used.

<span id="version_3_7_1"></span>

### 2010-08-23 (3.7.1)

1.  Added new commands [SQLITE_DBSTATUS_SCHEMA_USED](c3ref/c_dbstatus_options.md#sqlitedbstatusschemaused) and [SQLITE_DBSTATUS_STMT_USED](c3ref/c_dbstatus_options.md#sqlitedbstatusstmtused) to the [sqlite3_db_status()](c3ref/db_status.md) interface, in order to report out the amount of memory used to hold the schema and prepared statements of a connection.
2.  Increase the maximum size of a database pages from 32KiB to 64KiB.
3.  Use the [LIKE optimization](optoverview.md#like_opt) even if the right-hand side string contains no wildcards.
4.  Added the [SQLITE_FCNTL_CHUNK_SIZE](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlchunksize) verb to the [sqlite3_file_control()](c3ref/file_control.md) interface for both unix and windows, to cause database files to grow in large chunks in order to reduce disk fragmentation.
5.  Fixed a bug in the query planner that caused performance regressions relative to 3.6.23.1 on some complex joins.
6.  Fixed a typo in the OS/2 backend.
7.  Refactored the pager module.
8.  The SQLITE_MAX_PAGE_SIZE compile-time option is now silently ignored. The maximum page size is hard-coded at 65536 bytes.

<span id="version_3_7_0_1"></span>

### 2010-08-04 (3.7.0.1)

1.  Fix a potential database corruption bug that can occur if version 3.7.0 and version 3.6.23.1 alternately write to the same database file. [Ticket \[51ae9cad317a1\]](https://sqlite.org/src/info/51ae9cad317a1)
2.  Fix a performance regression related to the query planner enhancements of version 3.7.0.

<span id="version_3_7_0"></span>

### 2010-07-21 (3.7.0)

1.  Added support for [write-ahead logging](wal.md).
2.  Query planner enhancement - automatic transient indices are created when doing so reduces the estimated query time.
3.  Query planner enhancement - the ORDER BY becomes a no-op if the query also contains a GROUP BY clause that forces the correct output order.
4.  Add the [SQLITE_DBSTATUS_CACHE_USED](c3ref/c_dbstatus_options.md#sqlitedbstatuscacheused) verb for [sqlite3_db_status()](c3ref/db_status.md).
5.  The logical database size is now stored in the database header so that bytes can be appended to the end of the database file without corrupting it and so that SQLite will work correctly on systems that lack support for ftruncate().

<span id="version_3_6_23_1"></span>

### 2010-03-26 (3.6.23.1)

1.  Fix a bug in the offsets() function of [FTS3](fts3.md)
2.  Fix a missing "sync" that when omitted could lead to database corruption if a power failure or OS crash occurred just as a ROLLBACK operation was finishing.

<span id="version_3_6_23"></span>

### 2010-03-09 (3.6.23)

1.  Added the [secure_delete pragma](pragma.md#pragma_secure_delete).
2.  Added the [sqlite3_compileoption_used()](c3ref/compileoption_get.md) and [sqlite3_compileoption_get()](c3ref/compileoption_get.md) interfaces as well as the [compile_options pragma](pragma.md#pragma_compile_options) and the [sqlite_compileoption_used()](lang_corefunc.md#sqlite_compileoption_used) and [sqlite_compileoption_get()](lang_corefunc.md#sqlite_compileoption_get) SQL functions.
3.  Added the [sqlite3_log()](c3ref/log.md) interface together with the [SQLITE_CONFIG_LOG](c3ref/c_config_covering_index_scan.md#sqliteconfiglog) verb to [sqlite3_config()](c3ref/config.md). The ".log" command is added to the [Command Line Interface](cli.md).
4.  Improvements to [FTS3](fts3.md).
5.  Improvements and bug-fixes in support for [SQLITE_OMIT_FLOATING_POINT](compile.md#omit_floating_point).
6.  The [integrity_check pragma](pragma.md#pragma_integrity_check) is enhanced to detect out-of-order rowids.
7.  The ".genfkey" operator has been removed from the [Command Line Interface](cli.md).
8.  Updates to the co-hosted [Lemon LALR(1) parser generator](lemon.md). (These updates did not affect SQLite.)
9.  Various minor bug fixes and performance enhancements.

<span id="version_3_6_22"></span>

### 2010-01-06 (3.6.22)

1.  Fix bugs that can (rarely) lead to incorrect query results when the CAST or OR operators are used in the WHERE clause of a query.
2.  Continuing enhancements and improvements to [FTS3](fts3.md).
3.  Other miscellaneous bug fixes.

<span id="version_3_6_21"></span>

### 2009-12-07 (3.6.21)

1.  The SQL output resulting from [sqlite3_trace()](c3ref/profile.md) is now modified to include the values of [bound parameters](lang_expr.md#varparam).
2.  Performance optimizations targeting a specific use case from a single high-profile user of SQLite. A 12% reduction in the number of CPU operations is achieved (as measured by Valgrind). Actual performance improvements in practice may vary depending on workload. Changes include:
    1.  The [ifnull()](lang_corefunc.md#ifnull) and [coalesce()](lang_corefunc.md#coalesce) SQL functions are now implemented using in-line VDBE code rather than calling external functions, so that unused arguments need never be evaluated.
    2.  The [substr()](lang_corefunc.md#substr) SQL function does not bother to measure the length its entire input string if it is only computing a prefix
    3.  Unnecessary OP_IsNull, OP_Affinity, and OP_MustBeInt VDBE opcodes are suppressed
    4.  Various code refactorizations for performance
3.  The FTS3 extension has undergone a major rework and cleanup. New [FTS3 documentation](fts3.md) is now available.
4.  The [SQLITE_SECURE_DELETE](compile.md#secure_delete) compile-time option fixed to make sure that content is deleted even when the [truncate optimization](lang_delete.md#truncateopt) applies.
5.  Improvements to "dot-command" handling in the [Command Line Interface](cli.md).
6.  Other minor bug fixes and documentation enhancements.

<span id="version_3_6_20"></span>

### 2009-11-04 (3.6.20)

1.  Optimizer enhancement: [prepared statements](c3ref/stmt.md) are automatically re-compiled when a binding on the RHS of a LIKE operator changes or when any range constraint changes under [SQLITE_ENABLE_STAT2](compile.md#enable_stat2).
2.  Various minor bug fixes and documentation enhancements.

<span id="version_3_6_16_1"></span>

### 2009-10-30 (3.6.16.1)

1.  A small patch to version 3.6.16 to fix [the OP_If bug](https://sqlite.org/src/info/6b00e0a34c).

<span id="version_3_6_19"></span>

### 2009-10-14 (3.6.19)

1.  Added support for [foreign key constraints](foreignkeys.md). Foreign key constraints are disabled by default. Use the [foreign_keys pragma](pragma.md#pragma_foreign_keys) to turn them on.
2.  Generalized the IS and IS NOT operators to take arbitrary expressions on their right-hand side.
3.  The [TCL Interface](tclsqlite.md) has been enhanced to use the [Non-Recursive Engine (NRE)](http://www.tcl-lang.org/cgi-bin/tct/tip/322.html) interface to the TCL interpreter when linked against TCL 8.6 or later.
4.  Fix a bug introduced in 3.6.18 that can lead to a segfault when an attempt is made to write on a read-only database.

<span id="version_3_6_18"></span>

### 2009-09-11 (3.6.18)

1.  Versioning of the SQLite source code has transitioned from CVS to [Fossil](http://www.fossil-scm.org/).
2.  Query planner enhancements.
3.  The [SQLITE_ENABLE_STAT2](compile.md#enable_stat2) compile-time option causes the [ANALYZE](lang_analyze.md) command to collect a small histogram of each index, to help SQLite better select among competing range query indices.
4.  Recursive triggers can be enabled using the [PRAGMA recursive_triggers](pragma.md#pragma_recursive_triggers) statement.
5.  Delete triggers fire when rows are removed due to a [REPLACE conflict resolution](lang_conflict.md). This feature is only enabled when recursive triggers are enabled.
6.  Added the [SQLITE_OPEN_SHAREDCACHE](c3ref/c_open_autoproxy.md) and [SQLITE_OPEN_PRIVATECACHE](c3ref/c_open_autoproxy.md) flags for [sqlite3_open_v2()](c3ref/open.md) used to override the global [shared cache mode](sharedcache.md) settings for individual database connections.
7.  Added improved version identification features: C-Preprocessor macro [SQLITE_SOURCE_ID](c3ref/c_scm_branch.md), C/C++ interface [sqlite3_sourceid()](c3ref/libversion.md), and SQL function [sqlite_source_id()](lang_corefunc.md#sqlite_source_id).
8.  Obscure bug fix on triggers ([\[efc02f9779\]](https://sqlite.org/src/info/efc02f9779)).

<span id="version_3_6_17"></span>

### 2009-08-10 (3.6.17)

1.  Expose the [sqlite3_strnicmp()](c3ref/stricmp.md) interface for use by extensions and applications.
2.  Remove the restriction on [virtual tables](vtab.md) and [shared cache mode](sharedcache.md). Virtual tables and shared cache can now be used at the same time.
3.  Many code simplifications and obscure bug fixes in support of providing [100% branch test coverage](testing.md#coverage).

<span id="version_3_6_16"></span>

### 2009-06-27 (3.6.16)

1.  Fix a bug (ticket \#3929) that occasionally causes INSERT or UPDATE operations to fail on an indexed table that has a self-modifying trigger.
2.  Other minor bug fixes and performance optimizations.

<span id="version_3_6_15"></span>

### 2009-06-15 (3.6.15)

1.  Refactor the internal representation of SQL expressions so that they use less memory on embedded platforms.
2.  Reduce the amount of stack space used
3.  Fix an 64-bit alignment bug on HP/UX and Sparc
4.  The [sqlite3_create_function()](c3ref/create_function.md) family of interfaces now return [SQLITE_MISUSE](rescode.md#misuse) instead of [SQLITE_ERROR](rescode.md#error) when passed invalid parameter combinations.
5.  When new tables are created using CREATE TABLE ... AS SELECT ... the datatype of the columns is the simplified SQLite datatype (TEXT, INT, REAL, NUMERIC, or BLOB) instead of a copy of the original datatype from the source table.
6.  Resolve race conditions when checking for a hot rollback journal.
7.  The [sqlite3_shutdown()](c3ref/initialize.md) interface frees all mutexes under windows.
8.  Enhanced robustness against corrupt database files
9.  Continuing improvements to the test suite and fixes to obscure bugs and inconsistencies that the test suite improvements are uncovering.

<span id="version_3_6_14_2"></span>

### 2009-05-25 (3.6.14.2)

1.  Fix a code generator bug introduced in [version 3.6.14](#version_3_6_14). This bug can cause incorrect query results under obscure circumstances. Ticket \#3879.

<span id="version_3_6_14_1"></span>

### 2009-05-19 (3.6.14.1)

1.  Fix a bug in [group_concat()](lang_aggfunc.md#group_concat), ticket \#3841
2.  Fix a performance bug in the pager cache, ticket \#3844
3.  Fix a bug in the [sqlite3_backup](c3ref/backup.md) implementation that can lead to a corrupt backup database. Ticket \#3858.

<span id="version_3_6_14"></span>

### 2009-05-07 (3.6.14)

1.  Added the optional asynchronous VFS module.
2.  Enhanced the query optimizer so that [virtual tables](vtab.md) are able to make use of OR and IN operators in the WHERE clause.
3.  Speed improvements in the btree and pager layers.
4.  Added the [SQLITE_HAVE_ISNAN](compile.md#have_isnan) compile-time option which will cause the isnan() function from the standard math library to be used instead of SQLite's own home-brew NaN checker.
5.  Countless minor bug fixes, documentation improvements, new and improved test cases, and code simplifications and cleanups.

<span id="version_3_6_13"></span>

### 2009-04-13 (3.6.13)

1.  Fix a bug in [version 3.6.12](#version_3_6_12) that causes a segfault when running a count(\*) on the sqlite_master table of an empty database. Ticket \#3774.
2.  Fix a bug in [version 3.6.12](#version_3_6_12) that causes a segfault that when inserting into a table using a DEFAULT value where there is a function as part of the DEFAULT value expression. Ticket \#3791.
3.  Fix data structure alignment issues on Sparc. Ticket \#3777.
4.  Other minor bug fixes.

<span id="version_3_6_12"></span>

### 2009-03-31 (3.6.12)

1.  Fixed a bug that caused database corruption when an [incremental_vacuum](pragma.md#pragma_incremental_vacuum) is rolled back in an in-memory database. Ticket \#3761.
2.  Added the [sqlite3_unlock_notify()](c3ref/unlock_notify.md) interface.
3.  Added the [reverse_unordered_selects pragma](pragma.md#pragma_reverse_unordered_selects).
4.  The default page size on windows is automatically adjusted to match the capabilities of the underlying filesystem.
5.  Add the new ".genfkey" command in the [CLI](cli.md) for generating triggers to implement foreign key constraints.
6.  Performance improvements for "count(\*)" queries.
7.  Reduce the amount of heap memory used, especially by TRIGGERs.
8.  

<span id="version_3_6_11"></span>

### 2009-02-18 (3.6.11)

1.  Added the [hot-backup interface](c3ref/backup_finish.md#sqlite3backupinit).
2.  Added new commands ".backup" and ".restore" to the [CLI](cli.md).
3.  Added new methods [backup](tclsqlite.md#backup) and [restore](tclsqlite.md#restore) to the TCL interface.
4.  Improvements to the [syntax bubble diagrams](syntaxdiagrams.md)
5.  Various minor bug fixes

<span id="version_3_6_10"></span>

### 2009-01-15 (3.6.10)

1.  Fix a cache coherency problem that could lead to database corruption. Ticket \#3584.

<span id="version_3_6_9"></span>

### 2009-01-14 (3.6.9)

1.  Fix two bugs, which when combined might result in incorrect query results. Both bugs were harmless by themselves; only when they team up do they cause problems. Ticket \#3581.

<span id="version_3_6_8"></span>

### 2009-01-12 (3.6.8)

1.  Added support for [nested transactions](lang_savepoint.md)
2.  Enhanced the query optimizer so that it is able to use multiple indices to efficiently process [OR-connected constraints](optoverview.md#or_opt) in a WHERE clause.
3.  Added support for parentheses in FTS3 query patterns using the [SQLITE_ENABLE_FTS3_PARENTHESIS](compile.md#enable_fts3_parenthesis) compile-time option.

<span id="version_3_6_7"></span>

### 2008-12-16 (3.6.7)

1.  Reorganize the Unix interface in os_unix.c
2.  Added support for "Proxy Locking" on Mac OS X.
3.  Changed the prototype of the [sqlite3_auto_extension()](c3ref/auto_extension.md) interface in a way that is backwards compatible but which might cause warnings in new builds of applications that use that interface.
4.  Changed the signature of the xDlSym method of the [sqlite3_vfs](c3ref/vfs.md) object in a way that is backwards compatible but which might cause compiler warnings.
5.  Added superfluous casts and variable initializations in order to suppress nuisance compiler warnings.
6.  Fixes for various minor bugs.

<span id="version_3_6_6_2"></span>

### 2008-11-26 (3.6.6.2)

1.  Fix a bug in the b-tree delete algorithm that seems like it might be able to cause database corruption. The bug was first introduced in [version 3.6.6](#version_3_6_6) by check-in \[5899\] on 2008-11-13.
2.  Fix a memory leak that can occur following a disk I/O error.

<span id="version_3_6_6_1"></span>

### 2008-11-22 (3.6.6.1)

1.  Fix a bug in the page cache that can lead database corruption following a rollback. This bug was first introduced in [version 3.6.4](#version_3_6_4).
2.  Two other very minor bug fixes

<span id="version_3_6_6"></span>

### 2008-11-19 (3.6.6)

1.  Fix a \#define that prevented [memsys5](malloc.md#memsys5) from compiling
2.  Fix a problem in the virtual table commit mechanism that was causing a crash in FTS3. Ticket \#3497.
3.  Add the [application-defined page cache](c3ref/pcache_methods2.md)
4.  Added built-in support for VxWorks

<span id="version_3_6_5"></span>

### 2008-11-12 (3.6.5)

1.  Add the MEMORY option to the [journal_mode pragma](pragma.md#pragma_journal_mode).
2.  Added the [sqlite3_db_mutex()](c3ref/db_mutex.md) interface.
3.  Added the [SQLITE_OMIT_TRUNCATE_OPTIMIZATION](compile.md#omit_truncate_optimization) compile-time option.
4.  Fixed the [truncate optimization](lang_delete.md#truncateopt) so that [sqlite3_changes()](c3ref/changes.md) and [sqlite3_total_changes()](c3ref/total_changes.md) interfaces and the [count_changes pragma](pragma.md#pragma_count_changes) return the correct values.
5.  Added the [sqlite3_extended_errcode()](c3ref/errcode.md) interface.
6.  The [COMMIT](lang_transaction.md) command now succeeds even if there are pending queries. It returns [SQLITE_BUSY](rescode.md#busy) if there are pending incremental BLOB I/O requests.
7.  The error code is changed to [SQLITE_BUSY](rescode.md#busy) (instead of [SQLITE_ERROR](rescode.md#error)) when an attempt is made to [ROLLBACK](lang_transaction.md) while one or more queries are still pending.
8.  Drop all support for the [experimental memory allocators](malloc.md#memsysx) memsys4 and memsys6.
9.  Added the [SQLITE_ZERO_MALLOC](compile.md#zero_malloc) compile-time option.

<span id="version_3_6_4"></span>

### 2008-10-15 (3.6.4)

1.  Add option support for LIMIT and ORDER BY clauses on [DELETE](lang_delete.md) and [UPDATE](lang_update.md) statements. Only works if SQLite is compiled with [SQLITE_ENABLE_UPDATE_DELETE_LIMIT](compile.md#enable_update_delete_limit).
2.  Added the [sqlite3_stmt_status()](c3ref/stmt_status.md) interface for performance monitoring.
3.  Add the [INDEXED BY](lang_indexedby.md) clause.
4.  The LOCKING_STYLE extension is now enabled by default on Mac OS X
5.  Added the TRUNCATE option to [PRAGMA journal_mode](pragma.md#pragma_journal_mode)
6.  Performance enhancements to tree balancing logic in the B-Tree layer.
7.  Added the [source code](https://sqlite.org/src/finfo?name=tool/genfkey.c) and [documentation](https://sqlite.org/src/finfo?name=tool/genfkey.README) for the **genfkey** program for automatically generating triggers to enforce foreign key constraints.
8.  Added the [SQLITE_OMIT_TRUNCATE_OPTIMIZATION](compile.md#omit_truncate_optimization) compile-time option.
9.  The [SQL language documentation](lang.md) is converted to use [syntax diagrams](syntaxdiagrams.md) instead of BNF.
10. Other minor bug fixes

<span id="version_3_6_3"></span>

### 2008-09-22 (3.6.3)

1.  Fix for a bug in the SELECT DISTINCT logic that was introduced by the prior version.
2.  Other minor bug fixes

<span id="version_3_6_2"></span>

### 2008-08-30 (3.6.2)

1.  Split the pager subsystem into separate pager and pcache subsystems.
2.  Factor out identifier resolution procedures into separate files.
3.  Bug fixes

<span id="version_3_6_1"></span>

### 2008-08-06 (3.6.1)

1.  Added the [lookaside memory allocator](malloc.md#lookaside) for a speed improvement in excess of 15% on some workloads. (Your mileage may vary.)
2.  Added the [SQLITE_CONFIG_LOOKASIDE](c3ref/c_config_covering_index_scan.md#sqliteconfiglookaside) verb to [sqlite3_config()](c3ref/config.md) to control the default lookaside configuration.
3.  Added verbs [SQLITE_STATUS_PAGECACHE_SIZE](c3ref/c_status_malloc_count.md#sqlitestatuspagecachesize) and [SQLITE_STATUS_SCRATCH_SIZE](c3ref/c_status_malloc_count.md#sqlitestatusscratchsize) to the [sqlite3_status()](c3ref/status.md) interface.
4.  Modified [SQLITE_CONFIG_PAGECACHE](c3ref/c_config_covering_index_scan.md#sqliteconfigpagecache) and [SQLITE_CONFIG_SCRATCH](c3ref/c_config_covering_index_scan.md#sqliteconfigscratch) to remove the "+4" magic number in the buffer size computation.
5.  Added the [sqlite3_db_config()](c3ref/db_config.md) and [sqlite3_db_status()](c3ref/db_status.md) interfaces for controlling and monitoring the lookaside allocator separately on each [database connection](c3ref/sqlite3.md).
6.  Numerous other performance enhancements
7.  Miscellaneous minor bug fixes

### 2008-07-16 (3.6.0 beta)

1.  Modifications to the [virtual file system](c3ref/vfs.md) interface to support a wider range of embedded systems. See [35to36.html](35to36.md) for additional information. \*\*\* Potentially incompatible change \*\*\*
2.  All C-preprocessor macros used to control compile-time options now begin with the prefix "SQLITE\_". This may require changes to applications that compile SQLite using their own makefiles and with custom compile-time options, hence we mark this as a \*\*\* Potentially incompatible change \*\*\*
3.  The SQLITE_MUTEX_APPDEF compile-time option is no longer supported. Alternative mutex implementations can now be added at run-time using the [sqlite3_config()](c3ref/config.md) interface with the [SQLITE_CONFIG_MUTEX](c3ref/c_config_covering_index_scan.md#sqliteconfigmutex) verb. \*\*\* Potentially incompatible change \*\*\*
4.  The handling of IN and NOT IN operators that contain a NULL on their right-hand side expression is brought into compliance with the SQL standard and with other SQL database engines. This is a bug fix, but as it has the potential to break legacy applications that depend on the older buggy behavior, we mark that as a \*\*\* Potentially incompatible change \*\*\*
5.  The result column names generated for compound subqueries have been simplified to show only the name of the column of the original table and omit the table name. This makes SQLite operate more like other SQL database engines.
6.  Added the [sqlite3_config()](c3ref/config.md) interface for doing run-time configuration of the entire SQLite library.
7.  Added the [sqlite3_status()](c3ref/status.md) interface used for querying run-time status information about the overall SQLite library and its subsystems.
8.  Added the [sqlite3_initialize()](c3ref/initialize.md) and [sqlite3_shutdown()](c3ref/initialize.md) interfaces.
9.  The [SQLITE_OPEN_NOMUTEX](c3ref/c_open_autoproxy.md) option was added to [sqlite3_open_v2()](c3ref/open.md).
10. Added the [PRAGMA page_count](pragma.md#pragma_page_count) command.
11. Added the [sqlite3_next_stmt()](c3ref/next_stmt.md) interface.
12. Added a new [R\*Tree virtual table](rtree.md)

<span id="version_3_5_9"></span>

### 2008-05-14 (3.5.9)

1.  Added *experimental* support for the [journal_mode](pragma.md#pragma_journal_mode) PRAGMA and persistent journal.
2.  [Journal mode PERSIST](pragma.md#pragma_journal_mode) is the default behavior in [exclusive locking mode](pragma.md#pragma_locking_mode).
3.  Fix a performance regression on LEFT JOIN (see ticket \#3015) that was mistakenly introduced in [version 3.5.8](#version_3_5_8).
4.  Performance enhancement: Reengineer the internal routines used to interpret and render variable-length integers.
5.  Fix a buffer-overrun problem in [sqlite3_mprintf()](c3ref/mprintf.md) which occurs when a string without a zero-terminator is passed to "%.\*s".
6.  Always convert IEEE floating point NaN values into NULL during processing. (Ticket \#3060)
7.  Make sure that when a connection blocks on a RESERVED lock that it is able to continue after the lock is released. (Ticket \#3093)
8.  The "configure" scripts should now automatically configure Unix systems for large file support. Improved error messages for when large files are encountered and large file support is disabled.
9.  Avoid cache pages leaks following disk-full or I/O errors
10. And, many more minor bug fixes and performance enhancements....

<span id="version_3_5_8"></span>

### 2008-04-16 (3.5.8)

1.  Expose SQLite's internal pseudo-random number generator (PRNG) via the [sqlite3_randomness()](c3ref/randomness.md) interface
2.  New interface [sqlite3_context_db_handle()](c3ref/context_db_handle.md) that returns the [database connection](c3ref/sqlite3.md) handle that has invoked an application-defined SQL function.
3.  New interface [sqlite3_limit()](c3ref/limit.md) allows size and length limits to be set on a per-connection basis and at run-time.
4.  Improved crash-robustness: write the database page size into the rollback journal header.
5.  Allow the [VACUUM](lang_vacuum.md) command to change the page size of a database file.
6.  The xAccess() method of the VFS is allowed to return -1 to signal a memory allocation error.
7.  Performance improvement: The OP_IdxDelete opcode uses unpacked records, obviating the need for one OP_MakeRecord opcode call for each index record deleted.
8.  Performance improvement: Constant subexpressions are factored out of loops.
9.  Performance improvement: Results of OP_Column are reused rather than issuing multiple OP_Column opcodes.
10. Fix a bug in the RTRIM collating sequence.
11. Fix a bug in the SQLITE_SECURE_DELETE option that was causing Firefox crashes. Make arrangements to always test SQLITE_SECURE_DELETE prior to each release.
12. Other miscellaneous performance enhancements.
13. Other miscellaneous minor bug fixes.

<span id="version_3_5_7"></span>

### 2008-03-17 (3.5.7)

1.  Fix a bug (ticket \#2927) in the register allocation for compound selects - introduced by the new VM code in version 3.5.5.
2.  ALTER TABLE uses double-quotes instead of single-quotes for quoting filenames.
3.  Use the WHERE clause to reduce the size of a materialized VIEW in an UPDATE or DELETE statement. (Optimization)
4.  Do not apply the flattening optimization if the outer query is an aggregate and the inner query contains ORDER BY. (Ticket \#2943)
5.  Additional OS/2 updates
6.  Added an experimental power-of-two, first-fit memory allocator.
7.  Remove all instances of sprintf() from the code
8.  Accept "Z" as the zulu timezone at the end of date strings
9.  Fix a bug in the LIKE optimizer that occurs when the last character before the first wildcard is an upper-case "Z"
10. Added the "bitvec" object for keeping track of which pages have been journalled. Improves speed and reduces memory consumption, especially for large database files.
11. Get the SQLITE_ENABLE_LOCKING_STYLE macro working again on Mac OS X.
12. Store the statement journal in the temporary file directory instead of collocated with the database file.
13. Many improvements and cleanups to the configure script

<span id="version_3_5_6"></span>

### 2008-02-06 (3.5.6)

1.  Fix a bug (ticket \#2913) that prevented virtual tables from working in a LEFT JOIN. The problem was introduced into shortly before the 3.5.5 release.
2.  Bring the OS/2 porting layer up-to-date.
3.  Add the new [sqlite3_result_error_code()](c3ref/result_blob.md) API and use it in the implementation of [ATTACH](lang_attach.md) so that proper error codes are returned when an [ATTACH](lang_attach.md) fails.

<span id="version_3_5_5"></span>

### 2008-01-31 (3.5.5)

1.  Convert the underlying virtual machine to be a register-based machine rather than a stack-based machine. The only user-visible change is in the output of EXPLAIN.
2.  Add the build-in RTRIM collating sequence.

<span id="version_3_5_4"></span>

### 2007-12-14 (3.5.4)

1.  Fix a critical bug in UPDATE or DELETE that occurs when an OR REPLACE clause or a trigger causes rows in the same table to be deleted as side effects. (See ticket \#2832.) The most likely result of this bug is a segmentation fault, though database corruption is a possibility.
2.  Bring the processing of ORDER BY into compliance with the SQL standard for case where a result alias and a table column name are in conflict. Correct behavior is to prefer the result alias. Older versions of SQLite incorrectly picked the table column. (See ticket \#2822.)
3.  The [VACUUM](lang_vacuum.md) command preserves the setting of the [legacy_file_format pragma](pragma.md#pragma_legacy_file_format). (Ticket \#2804.)
4.  Productize and officially support the group_concat() SQL function.
5.  Better optimization of some IN operator expressions.
6.  Add the ability to change the [auto_vacuum](pragma.md#pragma_auto_vacuum) status of a database by setting the auto_vaccum pragma and VACUUMing the database.
7.  Prefix search in FTS3 is much more efficient.
8.  Relax the SQL statement length restriction in the CLI so that the ".dump" output of databases with very large BLOBs and strings can be played back to recreate the database.
9.  Other small bug fixes and optimizations.

<span id="version_3_5_3"></span>

### 2007-11-27 (3.5.3)

1.  Move website and documentation files out of the source tree into a [separate CM system](https://sqlite.org/docsrc/).
2.  Fix a long-standing bug in INSERT INTO ... SELECT ... statements where the SELECT is compound.
3.  Fix a long-standing bug in RAISE(IGNORE) as used in BEFORE triggers.
4.  Fixed the operator precedence for the ~ operator.
5.  On Win32, do not return an error when attempting to delete a file that does not exist.
6.  Allow collating sequence names to be quoted.
7.  Modify the TCL interface to use [sqlite3_prepare_v2()](c3ref/prepare.md).
8.  Fix multiple bugs that can occur following a malloc() failure.
9.  [sqlite3_step()](c3ref/step.md) returns [SQLITE_MISUSE](rescode.md#misuse) instead of crashing when called with a NULL parameter.
10. FTS3 now uses the SQLite memory allocator exclusively. The FTS3 amalgamation can now be appended to the SQLite amalgamation to generate a super-amalgamation containing both.
11. The DISTINCT keyword now will sometimes use an INDEX if an appropriate index is available and the optimizer thinks its use might be advantageous.

<span id="version_3_5_2"></span>

### 2007-11-05 (3.5.2)

1.  Dropped support for the [SQLITE_OMIT_MEMORY_ALLOCATION](compile.md#omitfeatures) compile-time option.
2.  Always open files using FILE_FLAG_RANDOM_ACCESS under Windows.
3.  The 3rd parameter of the built-in SUBSTR() function is now optional.
4.  Bug fix: do not invoke the authorizer when reparsing the schema after a schema change.
5.  Added the experimental malloc-free memory allocator in mem3.c.
6.  Virtual machine stores 64-bit integer and floating point constants in binary instead of text for a performance boost.
7.  Fix a race condition in test_async.c.
8.  Added the ".timer" command to the CLI

<span id="version_3_5_1"></span>

### 2007-10-04 (3.5.1)

1.  ***Nota Bene:** We are not using terms "alpha" or "beta" on this release because the code is stable and because if we use those terms, nobody will upgrade. However, we still reserve the right to make incompatible changes to the new VFS interface in future releases.*
2.  Fix a bug in the handling of [SQLITE_FULL](rescode.md#full) errors that could lead to database corruption. Ticket \#2686.
3.  The test_async.c drive now does full file locking and works correctly when used simultaneously by multiple processes on the same database.
4.  The CLI ignores whitespace (including comments) at the end of lines
5.  Make sure the query optimizer checks dependencies on all terms of a compound SELECT statement. Ticket \#2640.
6.  Add demonstration code showing how to build a VFS for a raw mass storage without a filesystem.
7.  Added an output buffer size parameter to the xGetTempname() method of the VFS layer.
8.  Sticky [SQLITE_FULL](rescode.md#full) or [SQLITE_IOERR](rescode.md#ioerr) errors in the pager are reset when a new transaction is started.

<span id="version_3_5_0"></span>

### 2007-09-04 (3.5.0) alpha

1.  Redesign the OS interface layer. See [34to35.html](34to35.md) for details. \*\*\* Potentially incompatible change \*\*\*
2.  The [sqlite3_release_memory()](c3ref/release_memory.md), [sqlite3_soft_heap_limit()](c3ref/soft_heap_limit.md), and [sqlite3_enable_shared_cache()](c3ref/enable_shared_cache.md) interfaces now work cross all threads in the process, not just the single thread in which they are invoked. \*\*\* Potentially incompatible change \*\*\*
3.  Added the [sqlite3_open_v2()](c3ref/open.md) interface.
4.  Reimplemented the memory allocation subsystem and made it replaceable at compile-time.
5.  Created a new mutex subsystem and made it replicable at compile-time.
6.  The same database connection may now be used simultaneously by separate threads.

<span id="version_3_4_2"></span>

### 2007-08-13 (3.4.2)

1.  Fix a database corruption bug that might occur if a ROLLBACK command is executed in [auto-vacuum mode](pragma.md#pragma_auto_vacuum) and a very small [sqlite3_soft_heap_limit](c3ref/soft_heap_limit.md) is set. Ticket \#2565.
2.  Add the ability to run a full regression test with a small [sqlite3_soft_heap_limit](c3ref/soft_heap_limit.md).
3.  Fix other minor problems with using small soft heap limits.
4.  Work-around for [GCC bug 32575](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=32575).
5.  Improved error detection of misused aggregate functions.
6.  Improvements to the amalgamation generator script so that all symbols are prefixed with either SQLITE_PRIVATE or SQLITE_API.

<span id="version_3_4_1"></span>

### 2007-07-20 (3.4.1)

1.  Fix a bug in [VACUUM](lang_vacuum.md) that can lead to database corruptio if two processes are connected to the database at the same time and one VACUUMs then the other then modifies the database.
2.  The expression "+column" is now considered the same as "column" when computing the collating sequence to use on the expression.
3.  In the [TCL language interface](tclsqlite.md), "@variable" instead of "\$variable" always binds as a blob.
4.  Added [PRAGMA freelist_count](pragma.md#pragma_freelist_count) for determining the current size of the freelist.
5.  The [PRAGMA auto_vacuum=incremental](pragma.md#pragma_auto_vacuum) setting is now persistent.
6.  Add FD_CLOEXEC to all open files under Unix.
7.  Fix a bug in the [min()/max() optimization](optoverview.md#minmax) when applied to descending indices.
8.  Make sure the TCL language interface works correctly with 64-bit integers on 64-bit machines.
9.  Allow the value -9223372036854775808 as an integer literal in SQL statements.
10. Add the capability of "hidden" columns in virtual tables.
11. Use the macro SQLITE_PRIVATE (defaulting to "static") on all internal functions in the amalgamation.
12. Add pluggable tokenizers and [ICU](https://icu.unicode.org) tokenization support to FTS2
13. Other minor bug fixes and documentation enhancements

<span id="version_3_4_0"></span>

### 2007-06-18 (3.4.0)

1.  Fix a bug that can lead to database corruption if an [SQLITE_BUSY](rescode.md#busy) error occurs in the middle of an explicit transaction and that transaction is later committed. Ticket \#2409.
2.  Fix a bug that can lead to database corruption if autovacuum mode is on and a malloc() failure follows a CREATE TABLE or CREATE INDEX statement which itself follows a cache overflow inside a transaction. See ticket \#2418.
3.  Added explicit [upper bounds](limits.md) on the sizes and quantities of things SQLite can process. This change might cause compatibility problems for applications that use SQLite in the extreme, which is why the current release is 3.4.0 instead of 3.3.18.
4.  Added support for [Incremental BLOB I/O](c3ref/blob_open.md).
5.  Added the [sqlite3_bind_zeroblob()](c3ref/bind_blob.md) API and the [zeroblob()](lang_corefunc.md#zeroblob) SQL function.
6.  Added support for [Incremental Vacuum](pragma.md#pragma_incremental_vacuum).
7.  Added the SQLITE_MIXED_ENDIAN_64BIT_FLOAT compile-time option to support ARM7 processors with goofy endianness.
8.  Removed all instances of sprintf() and strcpy() from the core library.
9.  Added support for [International Components for Unicode (ICU)](https://icu.unicode.org) to the full-text search extensions.
10. In the Windows OS driver, reacquire a SHARED lock if an attempt to acquire an EXCLUSIVE lock fails. Ticket \#2354
11. Fix the REPLACE() function so that it returns NULL if the second argument is an empty string. Ticket \#2324.
12. Document the hazards of type conversions in [sqlite3_column_blob()](c3ref/column_blob.md) and related APIs. Fix unnecessary type conversions. Ticket \#2321.
13. Internationalization of the TRIM() function. Ticket \#2323
14. Use memmove() instead of memcpy() when moving between memory regions that might overlap. Ticket \#2334
15. Fix an optimizer bug involving subqueries in a compound SELECT that has both an ORDER BY and a LIMIT clause. Ticket \#2339.
16. Make sure the [sqlite3_snprintf()](c3ref/mprintf.md) interface does not zero-terminate the buffer if the buffer size is less than 1. Ticket \#2341
17. Fix the built-in printf logic so that it prints "NaN" not "Inf" for floating-point NaNs. Ticket \#2345
18. When converting BLOB to TEXT, use the text encoding of the main database. Ticket \#2349
19. Keep the full precision of integers (if possible) when casting to NUMERIC. Ticket \#2364
20. Fix a bug in the handling of UTF16 codepoint 0xE000
21. Consider explicit collate clauses when matching WHERE constraints to indices in the query optimizer. Ticket \#2391
22. Fix the query optimizer to correctly handle constant expressions in the ON clause of a LEFT JOIN. Ticket \#2403
23. Fix the query optimizer to handle rowid comparisons to NULL correctly. Ticket \#2404
24. Fix many potential segfaults that could be caused by malicious SQL statements.

<span id="version_3_3_17"></span>

### 2007-04-25 (3.3.17)

1.  When the "write_version" value of the database header is larger than what the library understands, make the database read-only instead of unreadable.
2.  Other minor bug fixes

<span id="version_3_3_16"></span>

### 2007-04-18 (3.3.16)

1.  Fix a bug that caused VACUUM to fail if NULLs appeared in a UNIQUE column.
2.  Reinstate performance improvements that were added in [Version 3.3.14](#version_3_3_14) but regressed in [Version 3.3.15](#version_3_3_15).
3.  Fix problems with the handling of ORDER BY expressions on compound SELECT statements in subqueries.
4.  Fix a potential segfault when destroying locks on WinCE in a multi-threaded environment.
5.  Documentation updates.

<span id="version_3_3_15"></span>

### 2007-04-09 (3.3.15)

1.  Fix a bug introduced in 3.3.14 that caused a rollback of CREATE TEMP TABLE to leave the database connection wedged.
2.  Fix a bug that caused an extra NULL row to be returned when a descending query was interrupted by a change to the database.
3.  The FOR EACH STATEMENT clause on a trigger now causes a syntax error. It used to be silently ignored.
4.  Fix an obscure and relatively harmless problem that might have caused a resource leak following an I/O error.
5.  Many improvements to the test suite. Test coverage now exceeded 98%

<span id="version_3_3_14"></span>

### 2007-04-02 (3.3.14)

1.  Fix a bug (ticket \#2273) that could cause a segfault when the IN operator is used one term of a two-column index and the right-hand side of the IN operator contains a NULL.
2.  Added a new OS interface method for determining the sector size of underlying media: sqlite3OsSectorSize().
3.  A new algorithm for statements of the form INSERT INTO *table1* SELECT \* FROM *table2* is faster and reduces fragmentation. VACUUM uses statements of this form and thus runs faster and defragments better.
4.  Performance enhancements through reductions in disk I/O:
    1.  Do not read the last page of an overflow chain when deleting the row - just add that page to the freelist.
    2.  Do not store pages being deleted in the rollback journal.
    3.  Do not read in the (meaningless) content of pages extracted from the freelist.
    4.  Do not flush the page cache (and thus avoiding a cache refill) unless another process changes the underlying database file.
    5.  Truncate rather than delete the rollback journal when committing a transaction in exclusive access mode, or when committing the TEMP database.
5.  Added support for exclusive access mode using ["PRAGMA locking_mode=EXCLUSIVE"](pragma.md#pragma_locking_mode)
6.  Use heap space instead of stack space for large buffers in the pager - useful on embedded platforms with stack-space limitations.
7.  Add a makefile target "sqlite3.c" that builds an amalgamation containing the core SQLite library C code in a single file.
8.  Get the library working correctly when compiled with GCC option "-fstrict-aliasing".
9.  Removed the vestigal SQLITE_PROTOCOL error.
10. Improvements to test coverage, other minor bugs fixed, memory leaks plugged, code refactored and/or recommended in places for easier reading.

<span id="version_3_3_13"></span>

### 2007-02-13 (3.3.13)

1.  Add a "fragmentation" measurement in the output of sqlite3_analyzer.
2.  Add the COLLATE operator used to explicitly set the collating sequence used by an expression. This feature is considered experimental pending additional testing.
3.  Allow up to 64 tables in a join - the old limit was 32.
4.  Added two new experimental functions: [randomblob()](lang_corefunc.md#randomblob) and [hex()](lang_corefunc.md#hex). Their intended use is to facilitate generating [UUIDs](http://en.wikipedia.org/wiki/UUID).
5.  Fix a problem where [PRAGMA count_changes](pragma.md#pragma_count_changes) was causing incorrect results for updates on tables with triggers
6.  Fix a bug in the ORDER BY clause optimizer for joins where the left-most table in the join is constrained by a UNIQUE index.
7.  Fixed a bug in the "copy" method of the TCL interface.
8.  Bug fixes in fts1 and fts2 modules.

<span id="version_3_3_12"></span>

### 2007-01-27 (3.3.12)

1.  Fix another bug in the IS NULL optimization that was added in version 3.3.9.
2.  Fix an assertion fault that occurred on deeply nested views.
3.  Limit the amount of output that [PRAGMA integrity_check](pragma.md#pragma_integrity_check) generates.
4.  Minor syntactic changes to support a wider variety of compilers.

<span id="version_3_3_11"></span>

### 2007-01-22 (3.3.11)

1.  Fix another bug in the implementation of the new [sqlite3_prepare_v2()](c3ref/prepare.md) API. We'll get it right eventually...
2.  Fix a bug in the IS NULL optimization that was added in version 3.3.9 - the bug was causing incorrect results on certain LEFT JOINs that included in the WHERE clause an IS NULL constraint for the right table of the LEFT JOIN.
3.  Make AreFileApisANSI() a no-op macro in WinCE since WinCE does not support this function.

<span id="version_3_3_10"></span>

### 2007-01-09 (3.3.10)

1.  Fix bugs in the implementation of the new [sqlite3_prepare_v2()](c3ref/prepare.md) API that can lead to segfaults.
2.  Fix 1-second round-off errors in the strftime() function
3.  Enhance the Windows OS layer to provide detailed error codes
4.  Work around a win2k problem so that SQLite can use single-character database file names
5.  The [user_version](pragma.md#pragma_user_version) and [schema_version](pragma.md#pragma_schema_version) pragmas correctly set their column names in the result set
6.  Documentation updates

<span id="version_3_3_9"></span>

### 2007-01-04 (3.3.9)

1.  Fix bugs in pager.c that could lead to database corruption if two processes both try to recover a hot journal at the same instant
2.  Added the [sqlite3_prepare_v2()](c3ref/prepare.md) API.
3.  Fixed the ".dump" command in the command-line shell to show indices, triggers and views again.
4.  Change the table_info pragma so that it returns NULL for the default value if there is no default value
5.  Support for non-ASCII characters in win95 filenames
6.  Query optimizer enhancements:
    1.  Optimizer does a better job of using indices to satisfy ORDER BY clauses that sort on the integer primary key
    2.  Use an index to satisfy an IS NULL operator in the WHERE clause
    3.  Fix a bug that was causing the optimizer to miss an OR optimization opportunity
    4.  The optimizer has more freedom to reorder tables in the FROM clause even in there are LEFT joins.
7.  Extension loading supported added to WinCE
8.  Allow constraint names on the DEFAULT clause in a table definition
9.  Added the ".bail" command to the command-line shell
10. Make CSV (comma separate value) output from the command-line shell more closely aligned to accepted practice
11. Experimental FTS2 module added
12. Use sqlite3_mprintf() instead of strdup() to avoid libc dependencies
13. VACUUM uses a temporary file in the official TEMP folder, not in the same directory as the original database
14. The prefix on temporary filenames on Windows is changed from "sqlite" to "etilqs".

<span id="version_3_3_8"></span>

### 2006-10-09 (3.3.8)

1.  Support for full text search using the FTS1 module (beta)
2.  Added Mac OS X locking patches (beta - disabled by default)
3.  Introduce extended error codes and add error codes for various kinds of I/O errors.
4.  Added support for IF EXISTS on CREATE/DROP TRIGGER/VIEW
5.  Fix the regression test suite so that it works with Tcl8.5
6.  Enhance sqlite3_set_authorizer() to provide notification of calls to SQL functions.
7.  Added experimental API: sqlite3_auto_extension()
8.  Various minor bug fixes

<span id="version_3_3_7"></span>

### 2006-08-12 (3.3.7)

1.  Added support for virtual tables (beta)
2.  Added support for dynamically loaded extensions (beta)
3.  The [sqlite3_interrupt()](c3ref/interrupt.md) routine can be called for a different thread
4.  Added the [MATCH](lang_expr.md#match) operator.
5.  The default file format is now 1.

<span id="version_3_3_6"></span>

### 2006-06-06 (3.3.6)

1.  Plays better with virus scanners on Windows
2.  Faster :memory: databases
3.  Fix an obscure segfault in UTF-8 to UTF-16 conversions
4.  Added driver for OS/2
5.  Correct column meta-information returned for aggregate queries
6.  Enhanced output from EXPLAIN QUERY PLAN
7.  LIMIT 0 now works on subqueries
8.  Bug fixes and performance enhancements in the query optimizer
9.  Correctly handle NULL filenames in ATTACH and DETACH
10. Improved syntax error messages in the parser
11. Fix type coercion rules for the IN operator

<span id="version_3_3_5"></span>

### 2006-04-05 (3.3.5)

1.  CHECK constraints use conflict resolution algorithms correctly.
2.  The SUM() function throws an error on integer overflow.
3.  Choose the column names in a compound query from the left-most SELECT instead of the right-most.
4.  The sqlite3_create_collation() function honors the SQLITE_UTF16_ALIGNED flag.
5.  SQLITE_SECURE_DELETE compile-time option causes deletes to overwrite old data with zeros.
6.  Detect integer overflow in abs().
7.  The random() function provides 64 bits of randomness instead of only 32 bits.
8.  Parser detects and reports automaton stack overflow.
9.  Change the round() function to return REAL instead of TEXT.
10. Allow WHERE clause terms on the left table of a LEFT OUTER JOIN to contain aggregate subqueries.
11. Skip over leading spaces in text to numeric conversions.
12. Various minor bug and documentation typo fixes and performance enhancements.

<span id="version_3_3_4"></span>

### 2006-02-11 (3.3.4)

1.  Fix a blunder in the Unix mutex implementation that can lead to deadlock on multithreaded systems.
2.  Fix an alignment problem on 64-bit machines
3.  Added the fullfsync pragma.
4.  Fix an optimizer bug that could have caused some unusual LEFT OUTER JOINs to give incorrect results.
5.  The SUM function detects integer overflow and converts to accumulating an approximate result using floating point numbers
6.  Host parameter names can begin with '@' for compatibility with SQL Server.
7.  Other miscellaneous bug fixes

<span id="version_3_3_3"></span>

### 2006-01-31 (3.3.3)

1.  Removed support for an ON CONFLICT clause on CREATE INDEX - it never worked correctly so this should not present any backward compatibility problems.
2.  Authorizer callback now notified of ALTER TABLE ADD COLUMN commands
3.  After any changes to the TEMP database schema, all prepared statements are invalidated and must be recreated using a new call to sqlite3_prepare()
4.  Other minor bug fixes in preparation for the first stable release of version 3.3

### 2006-01-24 (3.3.2 beta)

1.  Bug fixes and speed improvements. Improved test coverage.
2.  Changes to the OS-layer interface: mutexes must now be recursive.
3.  Discontinue the use of thread-specific data for out-of-memory exception handling

### 2006-01-16 (3.3.1 alpha)

1.  Countless bug fixes
2.  Speed improvements
3.  Database connections can now be used by multiple threads, not just the thread in which they were created.

### 2006-01-11 (3.3.0 alpha)

1.  CHECK constraints
2.  IF EXISTS and IF NOT EXISTS clauses on CREATE/DROP TABLE/INDEX.
3.  DESC indices
4.  More efficient encoding of boolean values resulting in smaller database files
5.  More aggressive [SQLITE_OMIT_FLOATING_POINT](compile.md#omit_floating_point)
6.  Separate INTEGER and REAL affinity
7.  Added a virtual function layer for the OS interface
8.  "exists" method added to the TCL interface
9.  Improved response to out-of-memory errors
10. Database cache can be optionally shared between connections in the same thread
11. Optional READ UNCOMMITTED isolation (instead of the default isolation level of SERIALIZABLE) and table level locking when database connections share a common cache.

<span id="version_3_2_8"></span>

### 2005-12-19 (3.2.8)

1.  Fix an obscure bug that can cause database corruption under the following unusual circumstances: A large INSERT or UPDATE statement which is part of an even larger transaction fails due to a uniqueness constraint but the containing transaction commits.

<span id="version_2_8_17"></span>

### 2005-12-19 (2.8.17)

1.  Fix an obscure bug that can cause database corruption under the following unusual circumstances: A large INSERT or UPDATE statement which is part of an even larger transaction fails due to a uniqueness contraint but the containing transaction commits.

<span id="version_3_2_7"></span>

### 2005-09-24 (3.2.7)

1.  GROUP BY now considers NULLs to be equal again, as it should
2.  Now compiles on Solaris and OpenBSD and other Unix variants that lack the fdatasync() function
3.  Now compiles on MSVC++6 again
4.  Fix uninitialized variables causing malfunctions for various obscure queries
5.  Correctly compute a LEFT OUTER JOINs that is constrained on the left table only

<span id="version_3_2_6"></span>

### 2005-09-17 (3.2.6)

1.  Fix a bug that can cause database corruption if a VACUUM (or autovacuum) fails and is rolled back on a database that is larger than 1GiB
2.  LIKE optimization now works for columns with COLLATE NOCASE
3.  ORDER BY and GROUP BY now use bounded memory
4.  Added support for COUNT(DISTINCT expr)
5.  Change the way SUM() handles NULL values in order to comply with the SQL standard
6.  Use fdatasync() instead of fsync() where possible in order to speed up commits slightly
7.  Use of the CROSS keyword in a join turns off the table reordering optimization
8.  Added the experimental and undocumented EXPLAIN QUERY PLAN capability
9.  Use the unicode API in Windows

<span id="version_3_2_5"></span>

### 2005-08-27 (3.2.5)

1.  Fix a bug effecting DELETE and UPDATE statements that changed more than 40960 rows.
2.  Change the makefile so that it no longer requires GNUmake extensions
3.  Fix the --enable-threadsafe option on the configure script
4.  Fix a code generator bug that occurs when the left-hand side of an IN operator is constant and the right-hand side is a SELECT statement
5.  The PRAGMA synchronous=off statement now disables syncing of the master journal file in addition to the normal rollback journals

<span id="version_3_2_4"></span>

### 2005-08-24 (3.2.4)

1.  Fix a bug introduced in the previous release that can cause a segfault while generating code for complex WHERE clauses.
2.  Allow floating point literals to begin or end with a decimal point.

<span id="version_3_2_3"></span>

### 2005-08-21 (3.2.3)

1.  Added support for the CAST operator
2.  Tcl interface allows BLOB values to be transferred to user-defined functions
3.  Added the "transaction" method to the Tcl interface
4.  Allow the DEFAULT value of a column to call functions that have constant operands
5.  Added the ANALYZE command for gathering statistics on indices and using those statistics when picking an index in the optimizer
6.  Remove the limit (formerly 100) on the number of terms in the WHERE clause
7.  The right-hand side of the IN operator can now be a list of expressions instead of just a list of constants
8.  Rework the optimizer so that it is able to make better use of indices
9.  The order of tables in a join is adjusted automatically to make better use of indices
10. The IN operator is now a candidate for optimization even if the left-hand side is not the left-most term of the index. Multiple IN operators can be used with the same index.
11. WHERE clause expressions using BETWEEN and OR are now candidates for optimization
12. Added the "case_sensitive_like" pragma and the SQLITE_CASE_SENSITIVE_LIKE compile-time option to set its default value to "on".
13. Use indices to help with GLOB expressions and LIKE expressions too when the case_sensitive_like pragma is enabled
14. Added support for grave-accent quoting for compatibility with MySQL
15. Improved test coverage
16. Dozens of minor bug fixes

<span id="version_3_2_2"></span>

### 2005-06-12 (3.2.2)

1.  Added the sqlite3_db_handle() API
2.  Added the sqlite3_get_autocommit() API
3.  Added a REGEXP operator to the parser. There is no function to back up this operator in the standard build but users can add their own using sqlite3_create_function()
4.  Speed improvements and library footprint reductions.
5.  Fix byte alignment problems on 64-bit architectures.
6.  Many, many minor bug fixes and documentation updates.

<span id="version_3_2_1"></span>

### 2005-03-29 (3.2.1)

1.  Fix a memory allocation error in the new ADD COLUMN comment.
2.  Documentation updates

<span id="version_3_2_0"></span>

### 2005-03-21 (3.2.0)

1.  Added support for ALTER TABLE ADD COLUMN.
2.  Added support for the "T" separator in ISO-8601 date/time strings.
3.  Improved support for Cygwin.
4.  Numerous bug fixes and documentation updates.

<span id="version_3_1_6"></span>

### 2005-03-17 (3.1.6)

1.  Fix a bug that could cause database corruption when inserting record into tables with around 125 columns.
2.  sqlite3_step() is now much more likely to invoke the busy handler and less likely to return SQLITE_BUSY.
3.  Fix memory leaks that used to occur after a malloc() failure.

<span id="version_3_1_5"></span>

### 2005-03-11 (3.1.5)

1.  The ioctl on Mac OS X to control syncing to disk is F_FULLFSYNC, not F_FULLSYNC. The previous release had it wrong.

<span id="version_3_1_4"></span>

### 2005-03-11 (3.1.4)

1.  Fix a bug in autovacuum that could cause database corruption if a CREATE UNIQUE INDEX fails because of a constraint violation. This problem only occurs if the new autovacuum feature introduced in version 3.1 is turned on.
2.  The F_FULLSYNC ioctl (currently only supported on Mac OS X) is disabled if the synchronous pragma is set to something other than "full".
3.  Add additional forward compatibility to the future version 3.2 database file format.
4.  Fix a bug in WHERE clauses of the form (rowid\<'2')
5.  New [SQLITE_OMIT\_...](compile.md#omitfeatures) compile-time options added
6.  Updates to the man page
7.  Remove the use of strcasecmp() from the shell
8.  Windows DLL exports symbols Tclsqlite_Init and Sqlite_Init

<span id="version_3_1_3"></span>

### 2005-02-19 (3.1.3)

1.  Fix a problem with VACUUM on databases from which tables containing AUTOINCREMENT have been dropped.
2.  Add forward compatibility to the future version 3.2 database file format.
3.  Documentation updates

<span id="version_3_1_2"></span>

### 2005-02-15 (3.1.2)

1.  Fix a bug that can lead to database corruption if there are two open connections to the same database and one connection does a VACUUM and the second makes some change to the database.
2.  Allow "?" parameters in the LIMIT clause.
3.  Fix VACUUM so that it works with AUTOINCREMENT.
4.  Fix a race condition in AUTOVACUUM that can lead to corrupt databases
5.  Add a numeric version number to the sqlite3.h include file.
6.  Other minor bug fixes and performance enhancements.

<span id="version_2_8_16"></span>

### 2005-02-15 (2.8.16)

1.  Fix a bug that can lead to database corruption if there are two open connections to the same database and one connection does a VACUUM and the second makes some change to the database.
2.  Correctly handle quoted names in CREATE INDEX statements.
3.  Fix a naming conflict between sqlite.h and sqlite3.h.
4.  Avoid excess heap usage when copying expressions.
5.  Other minor bug fixes.

### 2005-02-01 (3.1.1 BETA)

1.  Automatic caching of prepared statements in the TCL interface
2.  ATTACH and DETACH as well as some other operations cause existing prepared statements to expire.
3.  Numerous minor bug fixes

### 2005-01-21 (3.1.0 ALPHA)

1.  Autovacuum support added
2.  CURRENT_TIME, CURRENT_DATE, and CURRENT_TIMESTAMP added
3.  Support for the EXISTS clause added.
4.  Support for correlated subqueries added.
5.  Added the ESCAPE clause on the LIKE operator.
6.  Support for ALTER TABLE ... RENAME TABLE ... added
7.  AUTOINCREMENT keyword supported on INTEGER PRIMARY KEY
8.  Many SQLITE_OMIT\_ macros inserts to omit features at compile-time and reduce the library footprint.
9.  The REINDEX command was added.
10. The engine no longer consults the main table if it can get all the information it needs from an index.
11. Many nuisance bugs fixed.

<span id="version_3_0_8"></span>

### 2004-10-12 (3.0.8)

1.  Add support for DEFERRED, IMMEDIATE, and EXCLUSIVE transactions.
2.  Allow new user-defined functions to be created when there are already one or more precompiled SQL statements.
3.  
4.  Fix portability problems for MinGW/MSYS.
5.  Fix a byte alignment problem on 64-bit Sparc machines.
6.  Fix the ".import" command of the shell so that it ignores \r characters at the end of lines.
7.  The "csv" mode option in the shell puts strings inside double-quotes.
8.  Fix typos in documentation.
9.  Convert array constants in the code to have type "const".
10. Numerous code optimizations, specially optimizations designed to make the code footprint smaller.

<span id="version_3_0_7"></span>

### 2004-09-18 (3.0.7)

1.  The BTree module allocates large buffers using malloc() instead of off of the stack, in order to play better on machines with limited stack space.
2.  Fixed naming conflicts so that versions 2.8 and 3.0 can be linked and used together in the same ANSI-C source file.
3.  New interface: sqlite3_bind_parameter_index()
4.  Add support for wildcard parameters of the form: "?nnn"
5.  Fix problems found on 64-bit systems.
6.  Removed encode.c file (containing unused routines) from the version 3.0 source tree.
7.  The sqlite3_trace() callbacks occur before each statement is executed, not when the statement is compiled.
8.  Makefile updates and miscellaneous bug fixes.

### 2004-09-02 (3.0.6 beta)

1.  Better detection and handling of corrupt database files.
2.  The sqlite3_step() interface returns SQLITE_BUSY if it is unable to commit a change because of a lock
3.  Combine the implementations of LIKE and GLOB into a single pattern-matching subroutine.
4.  Miscellaneous code size optimizations and bug fixes

### 2004-08-29 (3.0.5 beta)

1.  Support for ":AAA" style bind parameter names.
2.  Added the new sqlite3_bind_parameter_name() interface.
3.  Support for TCL variable names embedded in SQL statements in the TCL bindings.
4.  The TCL bindings transfer data without necessarily doing a conversion to a string.
5.  The database for TEMP tables is not created until it is needed.
6.  Add the ability to specify an alternative temporary file directory using the "sqlite_temp_directory" global variable.
7.  A compile-time option (SQLITE_BUSY_RESERVED_LOCK) causes the busy handler to be called when there is contention for a RESERVED lock.
8.  Various bug fixes and optimizations

### 2004-08-09 (3.0.4 beta)

1.  CREATE TABLE and DROP TABLE now work correctly as prepared statements.
2.  Fix a bug in VACUUM and UNIQUE indices.
3.  Add the ".import" command to the command-line shell.
4.  Fix a bug that could cause index corruption when an attempt to delete rows of a table is blocked by a pending query.
5.  Library size optimizations.
6.  Other minor bug fixes.

<span id="version_2_8_15"></span>

### 2004-07-22 (2.8.15)

1.  This is a maintenance release only. Various minor bugs have been fixed and some portability enhancements are added.

### 2004-07-22 (3.0.3 beta)

1.  The second beta release for SQLite 3.0.
2.  Add support for "PRAGMA page_size" to adjust the page size of the database.
3.  Various bug fixes and documentation updates.

### 2004-06-30 (3.0.2 beta)

1.  The first beta release for SQLite 3.0.

### 2004-06-22 (3.0.1 alpha)

1.  **\*\*\* Alpha Release - Research And Testing Use Only \*\*\***
2.  Lots of bug fixes.

### 2004-06-18 (3.0.0 alpha)

1.  **\*\*\* Alpha Release - Research And Testing Use Only \*\*\***
2.  Support for internationalization including UTF-8, UTF-16, and user defined collating sequences.
3.  New file format that is 25% to 35% smaller for typical use.
4.  Improved concurrency.
5.  Atomic commits for ATTACHed databases.
6.  Remove cruft from the APIs.
7.  BLOB support.
8.  64-bit rowids.
9.  [More information](version3.md).

<span id="version_2_8_14"></span>

### 2004-06-09 (2.8.14)

1.  Fix the min() and max() optimizer so that it works when the FROM clause consists of a subquery.
2.  Ignore extra whitespace at the end of "." commands in the shell.
3.  Bundle sqlite_encode_binary() and sqlite_decode_binary() with the library.
4.  The TEMP_STORE and DEFAULT_TEMP_STORE pragmas now work.
5.  Code changes to compile cleanly using OpenWatcom.
6.  Fix VDBE stack overflow problems with INSTEAD OF triggers and NULLs in IN operators.
7.  Add the global variable sqlite_temp_directory which if set defines the directory in which temporary files are stored.
8.  sqlite_interrupt() plays well with VACUUM.
9.  Other minor bug fixes.

<span id="version_2_8_13"></span>

### 2004-03-08 (2.8.13)

1.  Refactor parts of the code in order to make the code footprint smaller. The code is now also a little bit faster.
2.  sqlite_exec() is now implemented as a wrapper around sqlite_compile() and sqlite_step().
3.  The built-in min() and max() functions now honor the difference between NUMERIC and TEXT datatypes. Formerly, min() and max() always assumed their arguments were of type NUMERIC.
4.  New HH:MM:SS modifier to the built-in date/time functions.
5.  Experimental sqlite_last_statement_changes() API added. Fixed the last_insert_rowid() function so that it works correctly with triggers.
6.  Add functions prototypes for the database encryption API.
7.  Fix several nuisance bugs.

<span id="version_2_8_12"></span>

### 2004-02-08 (2.8.12)

1.  Fix a bug that will might corrupt the rollback journal if a power failure or external program halt occurs in the middle of a COMMIT. The corrupt journal can lead to database corruption when it is rolled back.
2.  Reduce the size and increase the speed of various modules, especially the virtual machine.
3.  Allow "\<expr\> IN \<table\>" as a shorthand for "\<expr\> IN (SELECT \* FROM \<table\>".
4.  Optimizations to the sqlite_mprintf() routine.
5.  Make sure the MIN() and MAX() optimizations work within subqueries.

<span id="version_2_8_11"></span>

### 2004-01-14 (2.8.11)

1.  Fix a bug in how the IN operator handles NULLs in subqueries. The bug was introduced by the previous release.

<span id="version_2_8_10"></span>

### 2004-01-14 (2.8.10)

1.  Fix a potential database corruption problem on Unix caused by the fact that all POSIX advisory locks are cleared whenever you close() a file. The work around it to embargo all close() calls while locks are outstanding.
2.  Performance enhancements on some corner cases of COUNT(\*).
3.  Make sure the in-memory backend response sanely if malloc() fails.
4.  Allow sqlite_exec() to be called from within user-defined SQL functions.
5.  Improved accuracy of floating-point conversions using "long double".
6.  Bug fixes in the experimental date/time functions.

<span id="version_2_8_9"></span>

### 2004-01-06 (2.8.9)

1.  Fix a 32-bit integer overflow problem that could result in corrupt indices in a database if large negative numbers (less than -2147483648) were inserted into an indexed numeric column.
2.  Fix a locking problem on multi-threaded Linux implementations.
3.  Always use "." instead of "," as the decimal point even if the locale requests ",".
4.  Added UTC to localtime conversions to the experimental date/time functions.
5.  Bug fixes to date/time functions.

<span id="version_2_8_8"></span>

### 2003-12-18 (2.8.8)

1.  Fix a critical bug introduced into 2.8.0 which could cause database corruption.
2.  Fix a problem with 3-way joins that do not use indices
3.  The VACUUM command now works with the non-callback API
4.  Improvements to the "PRAGMA integrity_check" command

<span id="version_2_8_7"></span>

### 2003-12-04 (2.8.7)

1.  Added experimental sqlite_bind() and sqlite_reset() APIs.
2.  If the name of the database is an empty string, open a new database in a temporary file that is automatically deleted when the database is closed.
3.  Performance enhancements in the [Lemon](lemon.md)-generated parser
4.  Experimental date/time functions revised.
5.  Disallow temporary indices on permanent tables.
6.  Documentation updates and typo fixes
7.  Added experimental sqlite_progress_handler() callback API
8.  Removed support for the Oracle8 outer join syntax.
9.  Allow GLOB and LIKE operators to work as functions.
10. Other minor documentation and makefile changes and bug fixes.

<span id="version_2_8_6"></span>

### 2003-08-22 (2.8.6)

1.  Moved the CVS repository to www.sqlite.org
2.  Update the NULL-handling documentation.
3.  Experimental date/time functions added.
4.  Bug fix: correctly evaluate a view of a view without segfaulting.
5.  Bug fix: prevent database corruption if you dropped a trigger that had the same name as a table.
6.  Bug fix: allow a VACUUM (without segfaulting) on an empty database after setting the EMPTY_RESULT_CALLBACKS pragma.
7.  Bug fix: if an integer value will not fit in a 32-bit int, store it in a double instead.
8.  Bug fix: Make sure the journal file directory entry is committed to disk before writing the database file.

<span id="version_2_8_5"></span>

### 2003-07-22 (2.8.5)

1.  Make LIMIT work on a compound SELECT statement.
2.  LIMIT 0 now shows no rows. Use LIMIT -1 to see all rows.
3.  Correctly handle comparisons between an INTEGER PRIMARY KEY and a floating point number.
4.  Fix several important bugs in the new ATTACH and DETACH commands.
5.  Updated the [NULL-handling document](nulls.md).
6.  Allow NULL arguments in sqlite_compile() and sqlite_step().
7.  Many minor bug fixes

<span id="version_2_8_4"></span>

### 2003-06-29 (2.8.4)

1.  Enhanced the "PRAGMA integrity_check" command to verify indices.
2.  Added authorization hooks for the new ATTACH and DETACH commands.
3.  Many documentation updates
4.  Many minor bug fixes

<span id="version_2_8_3"></span>

### 2003-06-04 (2.8.3)

1.  Fix a problem that will corrupt the indices on a table if you do an INSERT OR REPLACE or an UPDATE OR REPLACE on a table that contains an INTEGER PRIMARY KEY plus one or more indices.
2.  Fix a bug in Windows locking code so that locks work correctly when simultaneously accessed by Win95 and WinNT systems.
3.  Add the ability for INSERT and UPDATE statements to refer to the "rowid" (or "\_rowid\_" or "oid") columns.
4.  Other important bug fixes

<span id="version_2_8_2"></span>

### 2003-05-17 (2.8.2)

1.  Fix a problem that will corrupt the database file if you drop a table from the main database that has a TEMP index.

<span id="version_2_8_1"></span>

### 2003-05-17 (2.8.1)

1.  Reactivated the VACUUM command that reclaims unused disk space in a database file.
2.  Added the ATTACH and DETACH commands to allow interacting with multiple database files at the same time.
3.  Added support for TEMP triggers and indices.
4.  Added support for in-memory databases.
5.  Removed the experimental sqlite_open_aux_file(). Its function is subsumed in the new ATTACH command.
6.  The precedence order for ON CONFLICT clauses was changed so that ON CONFLICT clauses on BEGIN statements have a higher precedence than ON CONFLICT clauses on constraints.
7.  Many, many bug fixes and compatibility enhancements.

<span id="version_2_8_0"></span>

### 2003-02-16 (2.8.0)

1.  Modified the journal file format to make it more resistant to corruption that can occur after an OS crash or power failure.
2.  Added a new C/C++ API that does not use callback for returning data.

<span id="version_2_7_6"></span>

### 2003-01-25 (2.7.6)

1.  Performance improvements. The library is now much faster.
2.  Added the **sqlite_set_authorizer()** API. Formal documentation has not been written - see the source code comments for instructions on how to use this function.
3.  Fix a bug in the GLOB operator that was preventing it from working with upper-case letters.
4.  Various minor bug fixes.

<span id="version_2_7_5"></span>

### 2002-12-28 (2.7.5)

1.  Fix an uninitialized variable in pager.c which could (with a probability of about 1 in 4 billion) result in a corrupted database.

<span id="version_2_7_4"></span>

### 2002-12-17 (2.7.4)

1.  Database files can now grow to be up to 2^41 bytes. The old limit was 2^31 bytes.
2.  The optimizer will now scan tables in the reverse if doing so will satisfy an ORDER BY ... DESC clause.
3.  The full pathname of the database file is now remembered even if a relative path is passed into sqlite_open(). This allows the library to continue operating correctly after a chdir().
4.  Speed improvements in the VDBE.
5.  Lots of little bug fixes.

<span id="version_2_7_3"></span>

### 2002-10-31 (2.7.3)

1.  Various compiler compatibility fixes.
2.  Fix a bug in the "expr IN ()" operator.
3.  Accept column names in parentheses.
4.  Fix a problem with string memory management in the VDBE
5.  Fix a bug in the "table_info" pragma"
6.  Export the sqlite_function_type() API function in the Windows DLL
7.  Fix locking behavior under Windows
8.  Fix a bug in LEFT OUTER JOIN

<span id="version_2_7_2"></span>

### 2002-09-25 (2.7.2)

1.  Prevent journal file overflows on huge transactions.
2.  Fix a memory leak that occurred when sqlite_open() failed.
3.  Honor the ORDER BY and LIMIT clause of a SELECT even if the result set is used for an INSERT.
4.  Do not put write locks on the file used to hold TEMP tables.
5.  Added documentation on SELECT DISTINCT and on how SQLite handles NULLs.
6.  Fix a problem that was causing poor performance when many thousands of SQL statements were executed by a single sqlite_exec() call.

<span id="version_2_7_1"></span>

### 2002-08-31 (2.7.1)

1.  Fix a bug in the ORDER BY logic that was introduced in version 2.7.0
2.  C-style comments are now accepted by the tokenizer.
3.  INSERT runs a little faster when the source is a SELECT statement.

<span id="version_2_7_0"></span>

### 2002-08-25 (2.7.0)

1.  Make a distinction between numeric and text values when sorting. Text values sort according to memcmp(). Numeric values sort in numeric order.
2.  Allow multiple simultaneous readers under Windows by simulating the reader/writers locks that are missing from Win95/98/ME.
3.  An error is now returned when trying to start a transaction if another transaction is already active.

<span id="version_2_6_3"></span>

### 2002-08-13 (2.6.3)

1.  Add the ability to read both little-endian and big-endian databases. So a database created under SunOS or Mac OS X can be read and written under Linux or Windows and vice versa.
2.  Convert to the new website: https://sqlite.org/
3.  Allow transactions to span Linux Threads
4.  Bug fix in the processing of the ORDER BY clause for GROUP BY queries

<span id="version_2_6_2"></span>

### 2002-07-31 (2.6.2)

1.  Text files read by the COPY command can now have line terminators of LF, CRLF, or CR.
2.  SQLITE_BUSY is handled correctly if encountered during database initialization.
3.  Fix to UPDATE triggers on TEMP tables.
4.  Documentation updates.

<span id="version_2_6_1"></span>

### 2002-07-19 (2.6.1)

1.  Include a static string in the library that responds to the RCS "ident" command and which contains the library version number.
2.  Fix an assertion failure that occurred when deleting all rows of a table with the "count_changes" pragma turned on.
3.  Better error reporting when problems occur during the automatic 2.5.6 to 2.6.0 database format upgrade.

<span id="version_2_6_0"></span>

### 2002-07-18 (2.6.0)

1.  Change the format of indices to correct a design flaw the originated with version 2.1.0. \*\*\* This is an incompatible file format change \*\*\* When version 2.6.0 or later of the library attempts to open a database file created by version 2.5.6 or earlier, it will automatically and irreversibly convert the file format. **Make backup copies of older database files before opening them with version 2.6.0 of the library.**

<span id="version_2_5_6"></span>

### 2002-07-07 (2.5.6)

1.  Fix more problems with rollback. Enhance the test suite to exercise the rollback logic extensively in order to prevent any future problems.

<span id="version_2_5_5"></span>

### 2002-07-06 (2.5.5)

1.  Fix a bug which could cause database corruption during a rollback. This bugs was introduced in version 2.4.0 by the freelist optimization of checkin \[410\].
2.  Fix a bug in aggregate functions for VIEWs.
3.  Other minor changes and enhancements.

<span id="version_2_5_4"></span>

### 2002-07-01 (2.5.4)

1.  Make the "AS" keyword optional again.
2.  The datatype of columns now appear in the 4th argument to the callback.
3.  Added the **sqlite_open_aux_file()** API, though it is still mostly undocumented and untested.
4.  Added additional test cases and fixed a few bugs that those test cases found.

<span id="version_2_5_3"></span>

### 2002-06-25 (2.5.3)

1.  Bug fix: Database corruption can occur due to the optimization that was introduced in version 2.4.0 (check-in \[410\]). The problem should now be fixed. The use of versions 2.4.0 through 2.5.2 is not recommended.

<span id="version_2_5_2"></span>

### 2002-06-25 (2.5.2)

1.  Added the new **SQLITE_TEMP_MASTER** table which records the schema for temporary tables in the same way that **SQLITE_MASTER** does for persistent tables.
2.  Added an optimization to UNION ALL
3.  Fixed a bug in the processing of LEFT OUTER JOIN
4.  The LIMIT clause now works on subselects
5.  ORDER BY works on subselects
6.  There is a new TypeOf() function used to determine if an expression is numeric or text.
7.  Autoincrement now works for INSERT from a SELECT.

<span id="version_2_5_1"></span>

### 2002-06-19 (2.5.1)

1.  The query optimizer now attempts to implement the ORDER BY clause using an index. Sorting is still used if not suitable index is available.

<span id="version_2_5_0"></span>

### 2002-06-17 (2.5.0)

1.  Added support for row triggers.
2.  Added SQL-92 compliant handling of NULLs.
3.  Add support for the full SQL-92 join syntax and LEFT OUTER JOINs.
4.  Double-quoted strings interpreted as column names not text literals.
5.  Parse (but do not implement) foreign keys.
6.  Performance improvements in the parser, pager, and WHERE clause code generator.
7.  Make the LIMIT clause work on subqueries. (ORDER BY still does not work, though.)
8.  Added the "%Q" expansion to sqlite\_\*\_printf().
9.  Bug fixes too numerous to mention (see the change log).

<span id="version_2_4_12"></span>

### 2002-05-10 (2.4.12)

1.  Added logic to detect when the library API routines are called out of sequence.

<span id="version_2_4_11"></span>

### 2002-05-08 (2.4.11)

1.  Bug fix: Column names in the result set were not being generated correctly for some (rather complex) VIEWs. This could cause a segfault under certain circumstances.

<span id="version_2_4_10"></span>

### 2002-05-03 (2.4.10)

1.  Bug fix: Generate correct column headers when a compound SELECT is used as a subquery.
2.  Added the sqlite_encode_binary() and sqlite_decode_binary() functions to the source tree. But they are not yet linked into the library.
3.  Documentation updates.
4.  Export the sqlite_changes() function from Windows DLLs.
5.  Bug fix: Do not attempt the subquery flattening optimization on queries that lack a FROM clause. To do so causes a segfault.

<span id="version_2_4_9"></span>

### 2002-04-22 (2.4.9)

1.  Fix a bug that was causing the precompiled binary of SQLITE.EXE to report "out of memory" under Windows 98.

<span id="version_2_4_8"></span>

### 2002-04-20 (2.4.8)

1.  Make sure VIEWs are created after their corresponding TABLEs in the output of the **.dump** command in the shell.
2.  Speed improvements: Do not do synchronous updates on TEMP tables.
3.  Many improvements and enhancements to the shell.
4.  Make the GLOB and LIKE operators functions that can be overridden by a programmer. This allows, for example, the LIKE operator to be changed to be case sensitive.

<span id="version_2_4_7"></span>

### 2002-04-12 (2.4.7)

1.  Add the ability to put TABLE.\* in the column list of a SELECT statement.
2.  Permit SELECT statements without a FROM clause.
3.  Added the **last_insert_rowid()** SQL function.
4.  Do not count rows where the IGNORE conflict resolution occurs in the row count.
5.  Make sure functions expressions in the VALUES clause of an INSERT are correct.
6.  Added the **sqlite_changes()** API function to return the number of row that changed in the most recent operation.

<span id="version_2_4_6"></span>

### 2002-04-02 (2.4.6)

1.  Bug fix: Correctly handle terms in the WHERE clause of a join that do not contain a comparison operator.

<span id="version_2_4_5"></span>

### 2002-04-02 (2.4.5)

1.  Bug fix: Correctly handle functions that appear in the WHERE clause of a join.
2.  When the PRAGMA vdbe_trace=ON is set, correctly print the P3 operand value when it is a pointer to a structure rather than a pointer to a string.
3.  When inserting an explicit NULL into an INTEGER PRIMARY KEY, convert the NULL value into a unique key automatically.

<span id="version_2_4_4"></span>

### 2002-03-30 (2.4.4)

1.  Allow "VIEW" to be a column name
2.  Added support for CASE expressions (patch from Dan Kennedy)
3.  Added RPMS to the delivery (patches from Doug Henry)
4.  Fix typos in the documentation
5.  Cut over configuration management to a new CVS repository with its own CVSTrac bug tracking system.

<span id="version_2_4_3"></span>

### 2002-03-23 (2.4.3)

1.  Fix a bug in SELECT that occurs when a compound SELECT is used as a subquery in the FROM of a SELECT.
2.  The **sqlite_get_table()** function now returns an error if you give it two or more SELECTs that return different numbers of columns.

<span id="version_2_4_2"></span>

### 2002-03-20 (2.4.2)

1.  Bug fix: Fix an assertion failure that occurred when ROWID was a column in a SELECT statement on a view.
2.  Bug fix: Fix an uninitialized variable in the VDBE that would could an assert failure.
3.  Make the os.h header file more robust in detecting when the compile is for Windows and when it is for Unix.

<span id="version_2_4_1"></span>

### 2002-03-13 (2.4.1)

1.  Using an unnamed subquery in a FROM clause would cause a segfault.
2.  The parser now insists on seeing a semicolon or the end of input before executing a statement. This avoids an accidental disaster if the WHERE keyword is misspelled in an UPDATE or DELETE statement.

<span id="version_2_4_0"></span>

### 2002-03-11 (2.4.0)

1.  Change the name of the sanity_check PRAGMA to **integrity_check** and make it available in all compiles.
2.  SELECT min() or max() of an indexed column with no WHERE or GROUP BY clause is handled as a special case which avoids a complete table scan.
3.  Automatically generated ROWIDs are now sequential.
4.  Do not allow dot-commands of the command-line shell to occur in the middle of a real SQL command.
5.  Modifications to the [Lemon parser generator](lemon.md) so that the parser tables are 4 times smaller.
6.  Added support for user-defined functions implemented in C.
7.  Added support for new functions: **coalesce()**, **lower()**, **upper()**, and **random()**
8.  Added support for VIEWs.
9.  Added the subquery flattening optimizer.
10. Modified the B-Tree and Pager modules so that disk pages that do not contain real data (free pages) are not journaled and are not written from memory back to the disk when they change. This does not impact database integrity, since the pages contain no real data, but it does make large INSERT operations about 2.5 times faster and large DELETEs about 5 times faster.
11. Made the CACHE_SIZE pragma persistent
12. Added the SYNCHRONOUS pragma
13. Fixed a bug that was causing updates to fail inside of transactions when the database contained a temporary table.

<span id="version_2_3_3"></span>

### 2002-02-19 (2.3.3)

1.  Allow identifiers to be quoted in square brackets, for compatibility with MS-Access.
2.  Added support for sub-queries in the FROM clause of a SELECT.
3.  More efficient implementation of sqliteFileExists() under Windows. (by Joel Luscy)
4.  The VALUES clause of an INSERT can now contain expressions, including scalar SELECT clauses.
5.  Added support for CREATE TABLE AS SELECT
6.  Bug fix: Creating and dropping a table all within a single transaction was not working.

<span id="version_2_3_2"></span>

### 2002-02-14 (2.3.2)

1.  Bug fix: There was an incorrect assert() in pager.c. The real code was all correct (as far as is known) so everything should work OK if you compile with -DNDEBUG=1. When asserts are not disabled, there could be a fault.

<span id="version_2_3_1"></span>

### 2002-02-13 (2.3.1)

1.  Bug fix: An assertion was failing if "PRAGMA full_column_names=ON;" was set and you did a query that used a rowid, like this: "SELECT rowid, \* FROM ...".

<span id="version_2_3_0"></span>

### 2002-02-03 (2.3.0)

1.  Fix a serious bug in the INSERT command which was causing data to go into the wrong columns if the data source was a SELECT and the INSERT clauses specified its columns in some order other than the default.
2.  Added the ability to resolve constraint conflicts is ways other than an abort and rollback. See the documentation on the "ON CONFLICT" clause for details.
3.  Temporary files are now automatically deleted by the operating system when closed. There are no more dangling temporary files on a program crash. (If the OS crashes, fsck will delete the file after reboot under Unix. I do not know what happens under Windows.)
4.  NOT NULL constraints are honored.
5.  The COPY command puts NULLs in columns whose data is '\N'.
6.  In the COPY command, backslash can now be used to escape a newline.
7.  Added the SANITY_CHECK pragma.

<span id="version_2_2_5"></span>

### 2002-01-28 (2.2.5)

1.  Important bug fix: the IN operator was not working if either the left-hand or right-hand side was derived from an INTEGER PRIMARY KEY.
2.  Do not escape the backslash '\\ character in the output of the **sqlite** command-line access program.

<span id="version_2_2_4"></span>

### 2002-01-22 (2.2.4)

1.  The label to the right of an AS in the column list of a SELECT can now be used as part of an expression in the WHERE, ORDER BY, GROUP BY, and/or HAVING clauses.
2.  Fix a bug in the **-separator** command-line option to the **sqlite** command.
3.  Fix a problem with the sort order when comparing upper-case strings against characters greater than 'Z' but less than 'a'.
4.  Report an error if an ORDER BY or GROUP BY expression is constant.

<span id="version_2_2_3"></span>

### 2002-01-16 (2.2.3)

1.  Fix warning messages in VC++ 7.0. (Patches from nicolas352001)
2.  Make the library thread-safe. (The code is there and appears to work but has not been stressed.)
3.  Added the new **sqlite_last_insert_rowid()** API function.

<span id="version_2_2_2"></span>

### 2002-01-14 (2.2.2)

1.  Bug fix: An assertion was failing when a temporary table with an index had the same name as a permanent table created by a separate process.
2.  Bug fix: Updates to tables containing an INTEGER PRIMARY KEY and an index could fail.

<span id="version_2_2_1"></span>

### 2002-01-09 (2.2.1)

1.  Bug fix: An attempt to delete a single row of a table with a WHERE clause of "ROWID=x" when no such rowid exists was causing an error.
2.  Bug fix: Passing in a NULL as the 3rd parameter to **sqlite_open()** would sometimes cause a coredump.
3.  Bug fix: DROP TABLE followed by a CREATE TABLE with the same name all within a single transaction was causing a coredump.
4.  Makefile updates from A. Rottmann

<span id="version_2_2_0"></span>

### 2001-12-22 (2.2.0)

1.  Columns of type INTEGER PRIMARY KEY are actually used as the primary key in underlying B-Tree representation of the table.
2.  Several obscure, unrelated bugs were found and fixed while implemented the integer primary key change of the previous bullet.
3.  Added the ability to specify "\*" as part of a larger column list in the result section of a SELECT statement. For example: "**SELECT rowid, \* FROM table1;**".
4.  Updates to comments and documentation.

<span id="version_2_1_7"></span>

### 2001-12-15 (2.1.7)

1.  Fix a bug in **CREATE TEMPORARY TABLE** which was causing the table to be initially allocated in the main database file instead of in the separate temporary file. This bug could cause the library to suffer an assertion failure and it could cause "page leaks" in the main database file.
2.  Fix a bug in the b-tree subsystem that could sometimes cause the first row of a table to be repeated during a database scan.

<span id="version_2_1_6"></span>

### 2001-12-14 (2.1.6)

1.  Fix the locking mechanism yet again to prevent **sqlite_exec()** from returning SQLITE_PROTOCOL unnecessarily. This time the bug was a race condition in the locking code. This change affects both POSIX and Windows users.

<span id="version_2_1_5"></span>

### 2001-12-06 (2.1.5)

1.  Fix for another problem (unrelated to the one fixed in 2.1.4) that sometimes causes **sqlite_exec()** to return SQLITE_PROTOCOL unnecessarily. This time the bug was in the POSIX locking code and should not effect Windows users.

<span id="version_2_1_4"></span>

### 2001-12-05 (2.1.4)

1.  Sometimes **sqlite_exec()** would return SQLITE_PROTOCOL when it should have returned SQLITE_BUSY.
2.  The fix to the previous bug uncovered a deadlock which was also fixed.
3.  Add the ability to put a single .command in the second argument of the sqlite shell
4.  Updates to the FAQ

<span id="version_2_1_3"></span>

### 2001-11-24 (2.1.3)

1.  Fix the behavior of comparison operators (ex: "**\<**", "**==**", etc.) so that they are consistent with the order of entries in an index.
2.  Correct handling of integers in SQL expressions that are larger than what can be represented by the machine integer.

<span id="version_2_1_2"></span>

### 2001-11-23 (2.1.2)

1.  Changes to support 64-bit architectures.
2.  Fix a bug in the locking protocol.
3.  Fix a bug that could (rarely) cause the database to become unreadable after a DROP TABLE due to corruption to the SQLITE_MASTER table.
4.  Change the code so that version 2.1.1 databases that were rendered unreadable by the above bug can be read by this version of the library even though the SQLITE_MASTER table is (slightly) corrupted.

<span id="version_2_1_1"></span>

### 2001-11-13 (2.1.1)

1.  Bug fix: Sometimes arbitrary strings were passed to the callback function when the actual value of a column was NULL.

<span id="version_2_1_0"></span>

### 2001-11-12 (2.1.0)

1.  Change the format of data records so that records up to 16MB in size can be stored.
2.  Change the format of indices to allow for better query optimization.
3.  Implement the "LIMIT ... OFFSET ..." clause on SELECT statements.

<span id="version_2_0_8"></span>

### 2001-11-03 (2.0.8)

1.  Made selected parameters in API functions **const**. This should be fully backwards compatible.
2.  Documentation updates
3.  Simplify the design of the VDBE by restricting the number of sorters and lists to 1. In practice, no more than one sorter and one list was ever used anyhow.

<span id="version_2_0_7"></span>

### 2001-10-22 (2.0.7)

1.  Any UTF-8 character or ISO8859 character can be used as part of an identifier.
2.  Patches from Christian Werner to improve ODBC compatibility and to fix a bug in the round() function.
3.  Plug some memory leaks that use to occur if malloc() failed. We have been and continue to be memory leak free as long as malloc() works.
4.  Changes to some test scripts so that they work on Windows in addition to Unix.

<span id="version_2_0_6"></span>

### 2001-10-19 (2.0.6)

1.  Added the EMPTY_RESULT_CALLBACKS pragma
2.  Support for UTF-8 and ISO8859 characters in column and table names.
3.  Bug fix: Compute correct table names with the FULL_COLUMN_NAMES pragma is turned on.

<span id="version_2_0_5"></span>

### 2001-10-15 (2.0.5)

1.  Added the COUNT_CHANGES pragma.
2.  Changes to the FULL_COLUMN_NAMES pragma to help out the ODBC driver.
3.  Bug fix: "SELECT count(\*)" was returning NULL for empty tables. Now it returns 0.

<span id="version_2_0_4"></span>

### 2001-10-13 (2.0.4)

1.  Bug fix: an obscure and relatively harmless bug was causing one of the tests to fail when gcc optimizations are turned on. This release fixes the problem.

<span id="version_2_0_3"></span>

### 2001-10-13 (2.0.3)

1.  Bug fix: the **sqlite_busy_timeout()** function was delaying 1000 times too long before failing.
2.  Bug fix: an assertion was failing if the disk holding the database file became full or stopped accepting writes for some other reason. New tests were added to detect similar problems in the future.
3.  Added new operators: **&** (bitwise-and) **\|** (bitwise-or), **~** (ones-complement), **\<\<** (shift left), **\>\>** (shift right).
4.  Added new functions: **round()** and **abs()**.

<span id="version_2_0_2"></span>

### 2001-10-09 (2.0.2)

1.  Fix two bugs in the locking protocol. (One was masking the other.)
2.  Removed some unused "#include " that were causing problems for VC++.
3.  Fixed **sqlite.h** so that it is usable from C++
4.  Added the FULL_COLUMN_NAMES pragma. When set to "ON", the names of columns are reported back as TABLE.COLUMN instead of just COLUMN.
5.  Added the TABLE_INFO() and INDEX_INFO() pragmas to help support the ODBC interface.
6.  Added support for TEMPORARY tables and indices.

<span id="version_2_0_1"></span>

### 2001-10-02 (2.0.1)

1.  Remove some C++ style comments from btree.c so that it will compile using compilers other than gcc.
2.  The ".dump" output from the shell does not work if there are embedded newlines anywhere in the data. This is an old bug that was carried forward from version 1.0. To fix it, the ".dump" output no longer uses the COPY command. It instead generates INSERT statements.
3.  Extend the expression syntax to support "expr NOT NULL" (with a space between the "NOT" and the "NULL") in addition to "expr NOTNULL" (with no space).

<span id="version_2_0_0"></span>

### 2001-09-28 (2.0.0)

1.  Automatically build binaries for Linux and Windows and put them on the website.

### 2001-09-28 (2.0-alpha-4)

1.  Incorporate makefile patches form A. Rottmann to use LIBTOOL

### 2001-09-27 (2.0-alpha-3)

1.  SQLite now honors the UNIQUE keyword in CREATE UNIQUE INDEX. Primary keys are required to be unique.
2.  File format changed back to what it was for alpha-1
3.  Fixes to the rollback and locking behavior

### 2001-09-20 (2.0-alpha-2)

1.  Initial release of version 2.0. The idea of renaming the library to "SQLus" was abandoned in favor of keeping the "SQLite" name and bumping the major version number.
2.  The pager and btree subsystems added back. They are now the only available backend.
3.  The Dbbe abstraction and the GDBM and memory drivers were removed.
4.  Copyright on all code was disclaimed. The library is now in the public domain.

<span id="version_1_0_32"></span>

### 2001-07-23 (1.0.32)

1.  Pager and btree subsystems removed. These will be used in a follow-on SQL server library named "SQLus".
2.  Add the ability to use quoted strings as table and column names in expressions.

<span id="version_1_0_31"></span>

### 2001-04-15 (1.0.31)

1.  Pager subsystem added but not yet used.
2.  More robust handling of out-of-memory errors.
3.  New tests added to the test suite.

<span id="version_1_0_30"></span>

### 2001-04-06 (1.0.30)

1.  Remove the **sqlite_encoding** TCL variable that was introduced in the previous version.
2.  Add options **-encoding** and **-tcl-uses-utf** to the **sqlite** TCL command.
3.  Add tests to make sure that tclsqlite was compiled using Tcl header files and libraries that match.

<span id="version_1_0_29"></span>

### 2001-04-05 (1.0.29)

1.  The library now assumes data is stored as UTF-8 if the --enable-utf8 option is given to configure. The default behavior is to assume iso8859-x, as it has always done. This only makes a difference for LIKE and GLOB operators and the LENGTH and SUBSTR functions.
2.  If the library is not configured for UTF-8 and the Tcl library is one of the newer ones that uses UTF-8 internally, then a conversion from UTF-8 to iso8859 and back again is done inside the TCL interface.

<span id="version_1_0_28"></span>

### 2001-04-04 (1.0.28)

1.  Added limited support for transactions. At this point, transactions will do table locking on the GDBM backend. There is no support (yet) for rollback or atomic commit.
2.  Added special column names ROWID, OID, and \_ROWID\_ that refer to the unique random integer key associated with every row of every table.
3.  Additional tests added to the regression suite to cover the new ROWID feature and the TCL interface bugs mentioned below.
4.  Changes to the [Lemon parser generator](lemon.md) to help it work better when compiled using MSVC.
5.  Bug fixes in the TCL interface identified by Oleg Oleinick.

<span id="version_1_0_27"></span>

### 2001-03-20 (1.0.27)

1.  When doing DELETE and UPDATE, the library used to write the record numbers of records to be deleted or updated into a temporary file. This is changed so that the record numbers are held in memory.
2.  The DELETE command without a WHILE clause just removes the database files from the disk, rather than going through and deleting record by record.

<span id="version_1_0_26"></span>

### 2001-03-20 (1.0.26)

1.  A serious bug fixed on Windows. Windows users should upgrade. No impact to Unix.

<span id="version_1_0_25"></span>

### 2001-03-15 (1.0.25)

1.  Modify the test scripts to identify tests that depend on system load and processor speed and to warn the user that a failure of one of those (rare) tests does not necessarily mean the library is malfunctioning. No changes to code.

<span id="version_1_0_24"></span>

### 2001-03-14 (1.0.24)

1.  Fix a bug which was causing the UPDATE command to fail on systems where "malloc(0)" returns NULL. The problem does not appear on Windows, Linux, or HPUX but does cause the library to fail on QNX.

<span id="version_1_0_23"></span>

### 2001-02-20 (1.0.23)

1.  An unrelated (and minor) bug from Mark Muranwski fixed. The algorithm for figuring out where to put temporary files for a "memory:" database was not working quite right.

<span id="version_1_0_22"></span>

### 2001-02-19 (1.0.22)

1.  The previous fix was not quite right. This one seems to work better.

<span id="version_1_0_21"></span>

### 2001-02-19 (1.0.21)

1.  The UPDATE statement was not working when the WHERE clause contained some terms that could be satisfied using indices and other terms that could not. Fixed.

<span id="version_1_0_20"></span>

### 2001-02-11 (1.0.20)

1.  Merge development changes into the main trunk. Future work toward using a BTree file structure will use a separate CVS source tree. This CVS tree will continue to support the GDBM version of SQLite only.

<span id="version_1_0_19"></span>

### 2001-02-06 (1.0.19)

1.  Fix a strange (but valid) C declaration that was causing problems for QNX. No logical changes.

<span id="version_1_0_18"></span>

### 2001-01-04 (1.0.18)

1.  Print the offending SQL statement when an error occurs.
2.  Do not require commas between constraints in CREATE TABLE statements.
3.  Added the "-echo" option to the shell.
4.  Changes to comments.

<span id="version_1_0_17"></span>

### 2000-12-10 (1.0.17)

1.  Rewrote **sqlite_complete()** to make it faster.
2.  Minor tweaks to other code to make it run a little faster.
3.  Added new tests for **sqlite_complete()** and for memory leaks.

<span id="version_1_0_16"></span>

### 2000-11-28 (1.0.16)

1.  Documentation updates. Mostly fixing of typos and spelling errors.

<span id="version_1_0_15"></span>

### 2000-10-23 (1.0.15)

1.  Documentation updates
2.  Some sanity checking code was removed from the inner loop of vdbe.c to help the library to run a little faster. The code is only removed if you compile with -DNDEBUG.

<span id="version_1_0_14"></span>

### 2000-10-19 (1.0.14)

1.  Added a "memory:" backend driver that stores its database in an in-memory hash table.

<span id="version_1_0_13"></span>

### 2000-10-19 (1.0.13)

1.  Break out the GDBM driver into a separate file in anticipation to added new drivers.
2.  Allow the name of a database to be prefixed by the driver type. For now, the only driver type is "gdbm:".

<span id="version_1_0_12"></span>

### 2000-10-17 (1.0.12)

1.  Fixed an off-by-one error that was causing a coredump in the '%q' format directive of the new **sqlite\_...\_printf()** routines.
2.  Added the **sqlite_interrupt()** interface.
3.  In the shell, **sqlite_interrupt()** is invoked when the user presses Control-C
4.  Fixed some instances where **sqlite_exec()** was returning the wrong error code.

<span id="version_1_0_10"></span>

### 2000-10-11 (1.0.10)

1.  Added notes on how to compile for Windows95/98.
2.  Removed a few variables that were not being used. Etc.

<span id="version_1_0_9"></span>

### 2000-10-09 (1.0.9)

1.  Added the **sqlite\_...\_printf()** interface routines.
2.  Modified the **sqlite** shell program to use the new interface routines.
3.  Modified the **sqlite** shell program to print the schema for the built-in SQLITE_MASTER table, if explicitly requested.

<span id="version_1_0_8"></span>

### 2000-09-30 (1.0.8)

1.  Begin writing documentation on the TCL interface.

### 2000-09-29 (Not Released)

1.  Added the **sqlite_get_table()** API
2.  Updated the documentation for due to the above change.
3.  Modified the **sqlite** shell to make use of the new sqlite_get_table() API in order to print a list of tables in multiple columns, similar to the way "ls" prints filenames.
4.  Modified the **sqlite** shell to print a semicolon at the end of each CREATE statement in the output of the ".schema" command.

### 2000-09-21 (Not Released)

1.  Change the tclsqlite "eval" method to return a list of results if no callback script is specified.
2.  Change tclsqlite.c to use the Tcl_Obj interface
3.  Add tclsqlite.c to the libsqlite.a library

<span id="version_1_0_5"></span>

### 2000-09-14 (1.0.5)

1.  Changed the print format for floating point values from "%g" to "%.15g".
2.  Changed the comparison function so that numbers in exponential notation (ex: 1.234e+05) sort in numerical order.

<span id="version_1_0_4"></span>

### 2000-08-28 (1.0.4)

1.  Added functions **length()** and **substr()**.
2.  Fix a bug in the **sqlite** shell program that was causing a coredump when the output mode was "column" and the first row of data contained a NULL.

<span id="version_1_0_3"></span>

### 2000-08-22 (1.0.3)

1.  In the sqlite shell, print the "Database opened READ ONLY" message to stderr instead of stdout.
2.  In the sqlite shell, now print the version number on initial startup.
3.  Add the **sqlite_version\[\]** string constant to the library
4.  Makefile updates
5.  Bug fix: incorrect VDBE code was being generated for the following circumstance: a query on an indexed table containing a WHERE clause with an IN operator that had a subquery on its right-hand side.

<span id="version_1_0_1"></span>

### 2000-08-18 (1.0.1)

1.  Fix a bug in the configure script.
2.  Minor revisions to the website.

<span id="version_1_0"></span>

### 2000-08-17 (1.0)

1.  Change the **sqlite** program so that it can read databases for which it lacks write permission. (It used to refuse all access if it could not write.)

### 2000-08-09

1.  Treat carriage returns as white space.

### 2000-08-08

1.  Added pattern matching to the ".table" command in the "sqlite" command shell.

### 2000-08-04

1.  Documentation updates
2.  Added "busy" and "timeout" methods to the Tcl interface

### 2000-08-03

1.  File format version number was being stored in sqlite_master.tcl multiple times. This was harmless, but unnecessary. It is now fixed.

### 2000-08-02

1.  The file format for indices was changed slightly in order to work around an inefficiency that can sometimes come up with GDBM when there are large indices having many entries with the same key. \*\* Incompatible Change \*\*

### 2000-08-01

1.  The parser's stack was overflowing on a very long UPDATE statement. This is now fixed.

### 2000-07-31

1.  Finish the [VDBE tutorial](vdbe.md).
2.  Added documentation on compiling to WinNT.
3.  Fix a configuration program for WinNT.
4.  Fix a configuration problem for HPUX.

### 2000-07-29

1.  Better labels on column names of the result.

### 2000-07-28

1.  Added the **sqlite_busy_handler()** and **sqlite_busy_timeout()** interface.

### 2000-06-23

1.  Begin writing the [VDBE tutorial](vdbe.md).

### 2000-06-21

1.  Clean up comments and variable names. Changes to documentation. No functional changes to the code.

### 2000-06-19

1.  Column names in UPDATE statements were case sensitive. This mistake has now been fixed.

### 2000-06-18

1.  Added the concatenate string operator (\|\|)

### 2000-06-12

1.  Added the fcnt() function to the SQL interpreter. The fcnt() function returns the number of database "Fetch" operations that have occurred. This function is designed for use in test scripts to verify that queries are efficient and appropriately optimized. Fcnt() has no other useful purpose, as far as I know.
2.  Added a bunch more tests that take advantage of the new fcnt() function. The new tests did not uncover any new problems.

### 2000-06-08

1.  Added lots of new test cases
2.  Fix a few bugs discovered while adding test cases
3.  Begin adding lots of new documentation

### 2000-06-06

1.  Added compound select operators: **UNION**, **UNION ALL**, **INTERSECT**, and **EXCEPT**
2.  Added support for using **(SELECT ...)** within expressions
3.  Added support for **IN** and **BETWEEN** operators
4.  Added support for **GROUP BY** and **HAVING**
5.  NULL values are now reported to the callback as a NULL pointer rather than an empty string.

### 2000-06-03

1.  Added support for default values on columns of a table.
2.  Improved test coverage. Fixed a few obscure bugs found by the improved tests.

### 2000-06-02

1.  All database files to be modified by an UPDATE, INSERT or DELETE are now locked before any changes are made to any files. This makes it safe (I think) to access the same database simultaneously from multiple processes.
2.  The code appears stable so we are now calling it "beta".

### 2000-06-01

1.  Better support for file locking so that two or more processes (or threads) can access the same database simultaneously. More work needed in this area, though.

### 2000-05-31

1.  Added support for aggregate functions (Ex: **COUNT(\*)**, **MIN(...)**) to the SELECT statement.
2.  Added support for **SELECT DISTINCT ...**

### 2000-05-30

1.  Added the **LIKE** operator.
2.  Added a **GLOB** operator: similar to **LIKE** but it uses Unix shell globbing wildcards instead of the '%' and '\_' wildcards of SQL.
3.  Added the **COPY** command patterned after [PostgreSQL](http://www.postgresql.org/) so that SQLite can now read the output of the **pg_dump** database dump utility of PostgreSQL.
4.  Added a **VACUUM** command that calls the **gdbm_reorganize()** function on the underlying database files.
5.  And many, many bug fixes...

### 2000-05-29

1.  Initial Public Release of Alpha code
