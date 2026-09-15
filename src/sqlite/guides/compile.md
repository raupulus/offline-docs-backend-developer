---
title: Compile-time Options
source_url: https://www.sqlite.org/compile.html
source_path: compile.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2510
---

# 1. Overview

For most purposes, SQLite can be built just fine using the default compilation options. However, if required, the compile-time options documented below can be used to [omit SQLite features](#omitfeatures) (resulting in a [smaller compiled library size](footprint.md)) or to change the [default values](#defaults) of some parameters.

Every effort has been made to ensure that the various combinations of compilation options work harmoniously and produce a working library. Nevertheless, it is strongly recommended that the SQLite test-suite be executed to check for errors before using an SQLite library built with non-standard compilation options.

The [compile_options pragma](pragma.md#pragma_compile_options) can be used to determine which of the options listed below were used in building a given copy of SQLite.

<span id="rcmd"></span>

# 2. Recommended Compile-time Options

The following compile-time options are recommended for applications that are able to use them, in order to minimized the number of CPU cycles and the bytes of memory used by SQLite. Not all of these compile-time options are usable by every application. For example, the SQLITE_THREADSAFE=0 option is only usable by applications that never access SQLite from more than one thread at a time. And the SQLITE_OMIT_PROGRESS_CALLBACK option is only usable by applications that do not use the [sqlite3_progress_handler()](c3ref/progress_handler.md) interface. And so forth.

It is impossible to test every possible combination of compile-time options for SQLite. But the following set of compile-time options is one configuration that is always fully tested.

1.  **[SQLITE_DQS=0](compile.md#dqs)**. This setting disables the [double-quoted string literal](quirks.md#dblquote) misfeature.

2.  **[SQLITE_THREADSAFE=0](compile.md#threadsafe)**. Setting -DSQLITE_THREADSAFE=0 causes all of the mutex and thread-safety logic in SQLite to be omitted. This is the single compile-time option causes SQLite to run about 2% faster and also reduces the size of the library by about 2%. But the downside is that using the compile-time option means that SQLite can never be used by more than a single thread at a time, even if each thread has its own database connection.

3.  **[SQLITE_DEFAULT_MEMSTATUS=0](compile.md#default_memstatus)**. This setting causes the [sqlite3_status()](c3ref/status.md) interfaces that track memory usage to be disabled. This helps the [sqlite3_malloc()](c3ref/free.md) routines run much faster, and since SQLite uses [sqlite3_malloc()](c3ref/free.md) internally, this helps to make the entire library faster.

4.  **[SQLITE_DEFAULT_WAL_SYNCHRONOUS=1](compile.md#default_wal_synchronous)**. For maximum database safety following a power loss, the setting of [PRAGMA synchronous=FULL](pragma.md#pragma_synchronous) is recommended. However, in [WAL mode](wal.md), complete database integrity is guaranteed with [PRAGMA synchronous=NORMAL](pragma.md#pragma_synchronous). With [PRAGMA synchronous=NORMAL](pragma.md#pragma_synchronous) in [WAL mode](wal.md), recent changes to the database might be rolled back by a power loss, but the database will not be corrupted. Furthermore, transaction commit is much faster in WAL mode using synchronous=NORMAL than with the default synchronous=FULL. For these reasons, it is recommended that the synchronous setting be changed from FULL to NORMAL when switching to WAL mode. This compile-time option will accomplish that.

5.  **[SQLITE_LIKE_DOESNT_MATCH_BLOBS](compile.md#like_doesnt_match_blobs)**. Historically, SQLite has allowed BLOB operands to the [LIKE](lang_expr.md#like) and [GLOB](lang_expr.md#glob) operators. But having a BLOB as an operand of [LIKE](lang_expr.md#like) or [GLOB](lang_expr.md#glob) complicates and slows the [LIKE optimization](optoverview.md#like_opt). When this option is set, it means that the LIKE and GLOB operators always return FALSE if either operand is a BLOB. That simplifies the implementation of the [LIKE optimization](optoverview.md#like_opt) and allows queries that use the [LIKE optimization](optoverview.md#like_opt) to run faster.

6.  **[SQLITE_MAX_EXPR_DEPTH=0](limits.md#max_expr_depth)**. Setting the maximum expression parse-tree depth to zero disables all checking of the expression parse-tree depth, which simplifies the code resulting in faster execution, and helps the parse tree to use less memory.

7.  **[SQLITE_OMIT_DECLTYPE](compile.md#omit_decltype)**. By omitting the (seldom-needed) ability to return the declared type of columns from the result set of query, [prepared statements](c3ref/stmt.md) can be made to consume less memory.

8.  **[SQLITE_OMIT_DEPRECATED](compile.md#omit_deprecated)**. Omitting deprecated interfaces and features will not help SQLite to run any faster. It will reduce the library footprint, however. And it is the right thing to do.

9.  **[SQLITE_OMIT_PROGRESS_CALLBACK](compile.md#omit_progress_callback)**. The progress handler callback counter must be checked in the inner loop of the [bytecode engine](opcode.md). By omitting this interface, a single conditional is removed from the inner loop of the [bytecode engine](opcode.md), helping SQL statements to run slightly faster.

10. **[SQLITE_OMIT_SHARED_CACHE](compile.md#omit_shared_cache)**. Omitting the possibility of using [shared cache](sharedcache.md) allows many conditionals in performance-critical sections of the code to be eliminated. This can give a noticeable improvement in performance.

11. **[SQLITE_OMIT_AUTOINIT](compile.md#omit_autoinit)**. The SQLite library needs to be initialized using a call to [sqlite3_initialize()](c3ref/initialize.md) before certain interfaces are used. This initialization normally happens automatically the first time it is needed. However, with the SQLITE_OMIT_AUTOINIT option, the automatic initialization is omitted. This helps many API calls to run a little faster (since they do not have to check to see if initialization has already occurred and then run initialization if it has not previously been invoked) but it also means that the application must call [sqlite3_initialize()](c3ref/initialize.md) manually. If SQLite is compiled with -DSQLITE_OMIT_AUTOINIT and a routine like [sqlite3_malloc()](c3ref/free.md) or [sqlite3_vfs_find()](c3ref/vfs_find.md) or [sqlite3_open()](c3ref/open.md) is invoked without first calling [sqlite3_initialize()](c3ref/initialize.md), the likely result will be a segfault.

12. **[SQLITE_STRICT_SUBTYPE=1](compile.md#strict_subtype)**. This option causes an error to be raised if an application defined function that does not have the [SQLITE_RESULT_SUBTYPE](c3ref/c_deterministic.md#sqliteresultsubtype) property invokes the [sqlite3_result_subtype()](c3ref/result_subtype.md) interface. The sqlite3_result_subtype() interface does not work reliably unless the function is registered with the SQLITE_RESULT_SUBTYPE property. This compile-time option is designed to bring this problem to the attention of developers early.

When all of the recommended compile-time options above are used, the SQLite library will be approximately 3% smaller and use about 5% fewer CPU cycles. So these options do not make a huge difference. But in some design situations, every little bit helps.

Library-level configuration options, such as those listed above, may optionally be defined in a client-side header file. Defining SQLITE_CUSTOM_INCLUDE=myconfig.h (with no quotes) will cause sqlite3.c to include myconfig.h early on in the compilation process, enabling the client to customize the flags without having to explicitly pass all of them to the compiler. <span id="osconfig"></span>

# 3.  Platform Configuration

<span id="sqlite_config_h"></span>

**\_HAVE_SQLITE_CONFIG_H**

> If the \_HAVE_SQLITE_CONFIG_H macro is defined then the SQLite source code will attempt to \#include a file named "sqlite_cfg.h". The "sqlite_cfg.h" file usually contains other configuration options, especially "HAVE\_*INTERFACE*" type options generated by the configure process. Note that this header is intended only for use for platform-level configuration, not library-level configuration. To set SQLite-level configuration flags in a custom header, define SQLITE_CUSTOM_INCLUDE=myconfig.h, as described in the previous section.

<span id="fdatasync"></span>

**HAVE_FDATASYNC**

> If the HAVE_FDATASYNC compile-time option is true, then the default [VFS](vfs.md) for unix systems will attempt to use fdatasync() instead of fsync() where appropriate. If this flag is missing or false, then fsync() is always used.

<span id="gmtime_r"></span>

**HAVE_GMTIME_R**

> If the HAVE_GMTIME_R option is true and if [SQLITE_OMIT_DATETIME_FUNCS](compile.md#omit_datetime_funcs) is true, then the CURRENT_TIME, CURRENT_DATE, and CURRENT_TIMESTAMP keywords will use the threadsafe "gmtime_r()" interface rather than "gmtime()". In the usual case where [SQLITE_OMIT_DATETIME_FUNCS](compile.md#omit_datetime_funcs) is not defined or is false, then the built-in [date and time functions](lang_datefunc.md) are used to implement the CURRENT_TIME, CURRENT_DATE, and CURRENT_TIMESTAMP keywords and neither gmtime_r() nor gmtime() is ever called.

<span id="isnan"></span>

**HAVE_ISNAN**

> If the HAVE_ISNAN option is true, then SQLite invokes the system library isnan() function to determine if a double-precision floating point value is a NaN. If HAVE_ISNAN is undefined or false, then SQLite substitutes its own home-grown implementation of isnan().

<span id="localtime_r"></span>

**HAVE_LOCALTIME_R**

> If the HAVE_LOCALTIME_R option is true, then SQLite uses the threadsafe localtime_r() library routine instead of localtime() to help implement the [localtime modifier](lang_datefunc.md#localtime) to the built-in [date and time functions](lang_datefunc.md).

<span id="localtime_s"></span>

**HAVE_LOCALTIME_S**

> If the HAVE_LOCALTIME_S option is true, then SQLite uses the threadsafe localtime_s() library routine instead of localtime() to help implement the [localtime modifier](lang_datefunc.md#localtime) to the built-in [date and time functions](lang_datefunc.md).

<span id="malloc_usable_size"></span>

**HAVE_MALLOC_USABLE_SIZE**

> If the HAVE_MALLOC_USABLE_SIZE option is true, then SQLite uses the malloc_usable_size() interface to find the size of a memory allocation obtained from the standard-library malloc() or realloc() routines. This option is only applicable if the standard-library malloc() is used. On Apple systems, "zone malloc" is used instead, and so this option is not applicable. And, of course, if the application supplies its own malloc implementation using [SQLITE_CONFIG_MALLOC](c3ref/c_config_covering_index_scan.md#sqliteconfigmalloc) then this option has no effect.
>
> If the HAVE_MALLOC_USABLE_SIZE option is omitted or is false, then SQLite uses a wrapper around system malloc() and realloc() that enlarges each allocation by 8 bytes and writes the size of the allocation in the initial 8 bytes, and then SQLite also implements its own home-grown version of malloc_usable_size() that consults that 8-byte prefix to find the allocation size. This approach works but it is suboptimal. Applications are encouraged to use HAVE_MALLOC_USABLE_SIZE whenever possible.

<span id="strchrnul"></span>

**HAVE_STRCHRNUL**

> If the HAVE_STRCHRNUL option is true, then SQLite uses the strchrnul() library function. If this option is missing or false, then SQLite substitutes its own home-grown implementation of strchrnul().

<span id="utime"></span>

**HAVE_UTIME**

> If the HAVE_UTIME option is true, then the built-in but non-standard "unix-dotfile" VFS will use the utime() system call, instead of utimes(), to set the last access time on the lock file.

<span id="byteorder"></span>

**SQLITE_BYTEORDER=*(0\|1234\|4321)***

> SQLite needs to know if the native byte order of the target CPU is big-endian or little-endian. The SQLITE_BYTEORDER preprocessor is set to 4321 for big-endian machines and 1234 for little-endian machines, or it can be 0 to mean that the byte order must be determined at run-time. There are \#ifdefs in the code that set SQLITE_BYTEORDER automatically for all common platforms and compilers. However, it may be advantageous to set SQLITE_BYTEORDER appropriately when compiling SQLite for obscure targets. If the target byte order cannot be determined at compile-time, then SQLite falls back to doing run-time checks, which always work, though with a small performance penalty.

<span id="defaults"></span>

# 4.  Options To Set Default Parameter Values

<span id="default_automatic_index"></span>

**SQLITE_DEFAULT_AUTOMATIC_INDEX=*\<0 or 1\>***

> This macro determines the initial setting for [PRAGMA automatic_index](pragma.md#pragma_automatic_index) for newly opened [database connections](c3ref/sqlite3.md). For all versions of SQLite through 3.7.17, automatic indices are normally enabled for new database connections if this compile-time option is omitted. However, that might change in future releases of SQLite.
>
> See also: [SQLITE_OMIT_AUTOMATIC_INDEX](compile.md#omit_automatic_index)

<span id="default_autovacuum"></span>

**SQLITE_DEFAULT_AUTOVACUUM=*\<0 or 1 or 2\>***

> This macro determines if SQLite creates databases with the [auto_vacuum](pragma.md#pragma_auto_vacuum) flag set by default to OFF (0), FULL (1), or INCREMENTAL (2). The default value is 0 meaning that databases are created with auto-vacuum turned off. In any case the compile-time default may be overridden by the [PRAGMA auto_vacuum](pragma.md#pragma_auto_vacuum) command.

<span id="default_cache_size"></span>

**SQLITE_DEFAULT_CACHE_SIZE=*\<N\>***

> This macro sets the default maximum size of the page-cache for each attached database. A positive value means that the limit is N page. If N is negative that means to limit the cache size to -N\*1024 bytes. The suggested maximum cache size can be overridden by the [PRAGMA cache_size](pragma.md#pragma_cache_size) command. The default value is -2000, which translates into a maximum of 2048000 bytes per cache.

<span id="default_file_format"></span>

**SQLITE_DEFAULT_FILE_FORMAT=*\<1 or 4\>***

> The default [schema format number](fileformat2.md#schemaformat) used by SQLite when creating new database files is set by this macro. The schema formats are all very similar. The difference between formats 1 and 4 is that format 4 understands [descending indices](lang_createindex.md#descidx) and has a tighter encoding for boolean values.
>
> All versions of SQLite since 3.3.0 (2006-01-10) can read and write any schema format between 1 and 4. But older versions of SQLite might not be able to read formats greater than 1. So that older versions of SQLite will be able to read and write database files created by newer versions of SQLite, the default schema format was set to 1 for SQLite versions through 3.7.9 (2011-11-01). Beginning with [version 3.7.10](releaselog/3_7_10.md) (2012-01-16), the default schema format is 4.
>
> The schema format number for a new database can be set at runtime using the [PRAGMA legacy_file_format](pragma.md#pragma_legacy_file_format) command.

<span id="default_file_permissions"></span>

**SQLITE_DEFAULT_FILE_PERMISSIONS=*N***

> The default numeric file permissions for newly created database files under unix. If not specified, the default is 0644 which means that the files is globally readable but only writable by the creator.

<span id="default_foreign_keys"></span>

**SQLITE_DEFAULT_FOREIGN_KEYS=*\<0 or 1\>***

> This macro determines whether enforcement of [foreign key constraints](foreignkeys.md) is enabled or disabled by default for new database connections. Each database connection can always turn enforcement of foreign key constraints on and off at run-time using the [foreign_keys pragma](pragma.md#pragma_foreign_keys). Enforcement of foreign key constraints is normally off by default, but if this compile-time parameter is set to 1, enforcement of foreign key constraints will be on by default.

<span id="default_mmap_size"></span>

**SQLITE_DEFAULT_MMAP_SIZE=*N***

> This macro sets the default limit on the amount of memory that will be used for memory-mapped I/O for each open database file. If *N* is zero, then memory mapped I/O is disabled by default. This compile-time limit and the [SQLITE_MAX_MMAP_SIZE](compile.md#max_mmap_size) can be modified at start-time using the [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_MMAP_SIZE](c3ref/c_config_covering_index_scan.md#sqliteconfigmmapsize)) call, or at run-time using the [mmap_size pragma](pragma.md#pragma_mmap_size).

<span id="default_journal_size_limit"></span>

**SQLITE_DEFAULT_JOURNAL_SIZE_LIMIT=*\<bytes\>***

> This option sets the size limit on [rollback journal](lockingv3.md#rollback) files in [persistent journal mode](pragma.md#pragma_journal_mode) and [exclusive locking mode](pragma.md#pragma_locking_mode) or sets the size of the write-ahead log file in [WAL mode](wal.md). When this compile-time option is omitted there is no upper bound on the size of the rollback journals or write-ahead logs. The journal file size limit can be changed at run-time using the [journal_size_limit pragma](pragma.md#pragma_journal_size_limit).

<span id="default_locking_mode"></span>

**SQLITE_DEFAULT_LOCKING_MODE=*\<1 or 0\>***

> If set to 1, then the default [locking_mode](pragma.md#pragma_locking_mode) is set to EXCLUSIVE. If omitted or set to 0 then the default [locking_mode](pragma.md#pragma_locking_mode) is NORMAL.

<span id="default_lookaside"></span>

**SQLITE_DEFAULT_LOOKASIDE=*SZ,N***

> Sets the default size of the [lookaside memory allocator](malloc.md#lookaside) memory pool to N entries of SZ bytes each. This setting can be modified at start-time using [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_LOOKASIDE](c3ref/c_config_covering_index_scan.md#sqliteconfiglookaside)) and/or as each [database connection](c3ref/sqlite3.md) is opened using [sqlite3_db_config](c3ref/db_config.md)(db, [SQLITE_DBCONFIG_LOOKASIDE](c3ref/c_dbconfig_defensive.md#sqlitedbconfiglookaside)).

<span id="default_memstatus"></span>

**SQLITE_DEFAULT_MEMSTATUS=*\<1 or 0\>***

> This macro is used to determine whether or not the features enabled and disabled using the SQLITE_CONFIG_MEMSTATUS argument to [sqlite3_config()](c3ref/config.md) are available by default. The default value is 1 ([SQLITE_CONFIG_MEMSTATUS](c3ref/c_config_covering_index_scan.md#sqliteconfigmemstatus) related features enabled).
>
> The [sqlite3_memory_used()](c3ref/memory_highwater.md) and [sqlite3_memory_highwater()](c3ref/memory_highwater.md) interfaces, the [sqlite3_status64](c3ref/status.md)([SQLITE_STATUS_MEMORY_USED](c3ref/c_status_malloc_count.md#sqlitestatusmemoryused)) interface, and the [SQLITE_MAX_MEMORY](compile.md#max_memory) compile-time option are all non-functional when memory usage tracking is disabled.

<span id="default_pcache_initsz"></span>

**SQLITE_DEFAULT_PCACHE_INITSZ=*N***

> This macro determines the number of pages initially allocated by the page cache module when [SQLITE_CONFIG_PAGECACHE](c3ref/c_config_covering_index_scan.md#sqliteconfigpagecache) configuration option is not used and memory for the page cache is obtained from [sqlite3_malloc()](c3ref/free.md) instead. The number of pages set by this macro are allocated in a single allocation, which reduces the load on the memory allocator.

<span id="default_page_size"></span>

**SQLITE_DEFAULT_PAGE_SIZE=*\<bytes\>***

> This macro is used to set the default page-size used when a database is created. The value assigned must be a power of 2. The default value is 4096. The compile-time default may be overridden at runtime by the [PRAGMA page_size](pragma.md#pragma_page_size) command.

<span id="default_synchronous"></span>

**SQLITE_DEFAULT_SYNCHRONOUS=*\<0-3\>***

> This macro determines the default value of the [PRAGMA synchronous](pragma.md#pragma_synchronous) setting. If not overridden at compile-time, the default setting is 2 (FULL).

<span id="default_wal_synchronous"></span>

**SQLITE_DEFAULT_WAL_SYNCHRONOUS=*\<0-3\>***

> This macro determines the default value of the [PRAGMA synchronous](pragma.md#pragma_synchronous) setting for database files that open in [WAL mode](wal.md). If not overridden at compile-time, this value is the same as [SQLITE_DEFAULT_SYNCHRONOUS](compile.md#default_synchronous).
>
> If SQLITE_DEFAULT_WAL_SYNCHRONOUS differs from SQLITE_DEFAULT_SYNCHRONOUS, and if the application has not modified the synchronous setting for the database file using the [PRAGMA synchronous](pragma.md#pragma_synchronous) statement, then the synchronous setting is changed to the value defined by SQLITE_DEFAULT_WAL_SYNCHRONOUS when the database connection switches into WAL mode for the first time. If the SQLITE_DEFAULT_WAL_SYNCHRONOUS value is not overridden at compile-time, then it will always be the same as [SQLITE_DEFAULT_SYNCHRONOUS](compile.md#default_synchronous) and so no automatic synchronous setting changes will ever occur.

<span id="default_wal_autocheckpoint"></span>

**SQLITE_DEFAULT_WAL_AUTOCHECKPOINT=*\<pages\>***

> This macro sets the default page count for the [WAL](wal.md) [automatic checkpointing](wal.md#ckpt) feature. If unspecified, the default page count is 1000.

<span id="default_worker_threads"></span>

**SQLITE_DEFAULT_WORKER_THREADS=*N***

> This macro sets the default value for the maximum number of auxiliary threads that a single [prepared statement](c3ref/stmt.md) will launch to assist it with a query. If not specified, the default maximum is 0. The value set here cannot be more than [SQLITE_MAX_WORKER_THREADS](compile.md#max_worker_threads).

<span id="dqs"></span>

**SQLITE_DQS=*N***

> This macro determines the default values for [SQLITE_DBCONFIG_DQS_DDL](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdqsddl) and [SQLITE_DBCONFIG_DQS_DML](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdqsdml), which in turn determine how SQLite handles each [double-quoted string literal](quirks.md#dblquote). The "DQS" name stands for "<u>D</u>ouble-<u>Q</u>uoted <u>S</u>tring". The *N* argument should be an integer 0, 1, 2, or 3.
>
> > SQLITE_DQS
> >
> > Double-Quoted Strings Allowed
> >
> > Remarks
> >
> > In DDL
> >
> > In DML
> >
> > 3
> >
> > yes
> >
> > yes
> >
> > default
> >
> > 2
> >
> > yes
> >
> > no
> >
> >  
> >
> > 1
> >
> > no
> >
> > yes
> >
> >  
> >
> > 0
> >
> > no
> >
> > no
> >
> > recommended
>
> The recommended setting is 0, meaning that double-quoted strings are disallowed in all contexts. However, the default setting is 3 for maximum compatibility with legacy applications.

<span id="extra_durable"></span>

**SQLITE_EXTRA_DURABLE**

> The SQLITE_EXTRA_DURABLE compile-time option that used to cause the default [PRAGMA synchronous](pragma.md#pragma_synchronous) setting to be EXTRA, rather than FULL. This option is no longer supported. Use [SQLITE_DEFAULT_SYNCHRONOUS=3](compile.md#default_synchronous) instead.

<span id="fts3_max_expr_depth"></span>

**SQLITE_FTS3_MAX_EXPR_DEPTH=*N***

> This macro sets the maximum depth of the search tree that corresponds to the right-hand side of the MATCH operator in an [FTS3](fts3.md) or [FTS4](fts3.md#fts4) full-text index. The full-text search uses a recursive algorithm, so the depth of the tree is limited to prevent using too much stack space. The default limit is 12. This limit is sufficient for up to 4095 search terms on the right-hand side of the MATCH operator and it holds stack space usage to less than 2000 bytes.
>
> For ordinary FTS3/FTS4 queries, the search tree depth is approximately the base-2 logarithm of the number of terms in the right-hand side of the MATCH operator. However, for [phrase queries](fts3.md#phrase) and [NEAR queries](fts3.md#near) the search tree depth is linear in the number of right-hand side terms. So the default depth limit of 12 is sufficient for up to 4095 ordinary terms on a MATCH, it is only sufficient for 11 or 12 phrase or NEAR terms. Even so, the default is more than enough for most application.

<span id="json_max_depth"></span>

**SQLITE_JSON_MAX_DEPTH=*N***

> This macro sets the maximum nesting depth for JSON objects and arrays. The default value is 1000.
>
> The [JSON SQL functions](json1.md) use a [recursive descent parser](https://en.wikipedia.org/wiki/Recursive_descent_parser). This means that deeply nested JSON might require a lot of stack space to parse. On systems with limited stack space, SQLite can be compiled with a greatly reduced maximum JSON nesting depth to avoid the possibility of a stack overflow, even from hostile inputs. A value of 10 or 20 is normally sufficient even for the most complex real-world JSON.

<span id="like_doesnt_match_blobs"></span>

**SQLITE_LIKE_DOESNT_MATCH_BLOBS**

> This compile-time option causes the [LIKE](lang_expr.md#like) operator to always return False if either operand is a BLOB. The default behavior of [LIKE](lang_expr.md#like) is that BLOB operands are cast to TEXT before the comparison is done.
>
> This compile-time option makes SQLite run more efficiently when processing queries that use the [LIKE](lang_expr.md#like) operator, at the expense of breaking backwards compatibility. However, the backwards compatibility break may be only a technicality. There was a long-standing bug in the [LIKE](lang_expr.md#like) processing logic (see <https://sqlite.org/src/info/05f43be8fdda9f>) that caused it to misbehave for BLOB operands and nobody observed that bug in nearly 10 years of active use. So for more users, it is probably safe to enable this compile-time option and thereby save a little CPU time on LIKE queries.
>
> This compile-time option affects the SQL [LIKE](lang_expr.md#like) operator only and has no impact on the [sqlite3_strlike()](c3ref/strlike.md) C-language interface.

<span id="max_memory"></span>

**SQLITE_MAX_MEMORY=*N***

> This option limits the total amount of memory that SQLite will request from malloc() to *N* bytes. Any attempt by SQLite to allocate new memory that would cause the sum of all allocations held by SQLite to exceed *N* bytes will result in an out-of-memory error. This is a hard upper limit. See also the [sqlite3_soft_heap_limit()](c3ref/soft_heap_limit.md) interface.
>
> This option is a limit on the *total* amount of memory allocated. See the [SQLITE_MAX_ALLOCATION_SIZE](compile.md#max_allocation_size) option for a limitation on the amount of memory allowed in any single memory allocation.
>
> This limit is only functional if memory usage statistics are available via the [sqlite3_memory_used()](c3ref/memory_highwater.md) and [sqlite3_status64](c3ref/status.md)([SQLITE_STATUS_MEMORY_USED](c3ref/c_status_malloc_count.md#sqlitestatusmemoryused)) interfaces. Without that memory usage information, SQLite has no way of knowing when it is about to go over the limit, and thus is unable to prevent the excess memory allocation. Memory usage tracking is turned on by default, but can be disabled at compile-time using the [SQLITE_DEFAULT_MEMSTATUS](compile.md#default_memstatus) option, or at start-time using [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_MEMSTATUS](c3ref/c_config_covering_index_scan.md#sqliteconfigmemstatus)).

<span id="max_mmap_size"></span>

**SQLITE_MAX_MMAP_SIZE=*N***

> This macro sets a hard upper bound on the amount of address space that can be used by any single database for memory-mapped I/O. Setting this value to 0 completely disables memory-mapped I/O and causes logic associated with memory-mapped I/O to be omitted from the build. This option does change the default memory-mapped I/O address space size (set by [SQLITE_DEFAULT_MMAP_SIZE](compile.md#default_mmap_size) or sqlite3_config([SQLITE_CONFIG_MMAP_SIZE](c3ref/c_config_covering_index_scan.md#sqliteconfigmmapsize))) or the run-time memory-mapped I/O address space size (set by sqlite3_file_control([SQLITE_FCNTL_MMAP_SIZE](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlmmapsize)) or [PRAGMA mmap_size](pragma.md#pragma_mmap_size)) as long as those other settings are less than the maximum value defined here.

<span id="max_schema_retry"></span>

**SQLITE_MAX_SCHEMA_RETRY=*N***

> Whenever the database schema changes, prepared statements are automatically reprepared to accommodate the new schema. There is a race condition here in that if one thread is constantly changing the schema, another thread might spin on reparses and repreparations of a prepared statement and never get any real work done. This parameter prevents an infinite loop by forcing the spinning thread to give up after a fixed number of attempts at recompiling the prepared statement. The default setting is 50 which is more than adequate for most applications.

<span id="max_worker_threads"></span>

**SQLITE_MAX_WORKER_THREADS=*N***

> Set an upper bound on the [sqlite3_limit](c3ref/limit.md)(db,[SQLITE_LIMIT_WORKER_THREADS](c3ref/c_limit_attached.md#sqlitelimitworkerthreads),N) setting that determines the maximum number of auxiliary threads that a single [prepared statement](c3ref/stmt.md) will use to aid with CPU-intensive computations (mostly sorting). See also the [SQLITE_DEFAULT_WORKER_THREADS](compile.md#default_worker_threads) options.

<span id="memdb_default_maxsize"></span>

**SQLITE_MEMDB_DEFAULT_MAXSIZE=*N***

> Set the default size limit (in bytes) for in-memory databases created using [sqlite3_deserialize()](c3ref/deserialize.md). This is just the default. The limit can be changed at start-time using [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_MEMDB_MAXSIZE](c3ref/c_config_covering_index_scan.md#sqliteconfigmemdbmaxsize),N) or at run-time for individual databases using the [SQLITE_FCNTL_SIZE_LIMIT](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlsizelimit) [file-control](c3ref/file_control.md). If no default is specified, 1073741824 is used.

<span id="minimum_file_descriptor"></span>

**SQLITE_MINIMUM_FILE_DESCRIPTOR=*N***

> The unix [VFS](vfs.md) will never use a file descriptor less than *N*. The default value of *N* is 3.
>
> Avoiding the use of low-numbered file descriptors is a defense against accidental database corruption. If a database file was opened using file descriptor 2, for example, and then an assert() failed and invoked write(2,...), that would likely cause database corruption by overwriting part of the database file with the assertion error message. Using only higher-valued file descriptors avoids this potential problem. The protection against using low-numbered file descriptors can be disabled by setting this compile-time option to 0.

<span id="powersafe_overwrite"></span>

**SQLITE_POWERSAFE_OVERWRITE=*\<0 or 1\>***

> This option changes the default assumption about [powersafe overwrite](psow.md) for the underlying filesystems for the unix and windows [VFSes](vfs.md). Setting SQLITE_POWERSAFE_OVERWRITE to 1 causes SQLite to assume that application-level writes cannot changes bytes outside the range of bytes written even if the write occurs just before a power loss. With SQLITE_POWERSAFE_OVERWRITE set to 0, SQLite assumes that other bytes in the same sector with a written byte might be changed or damaged by a power loss.

<span id="printf_precision_limit"></span>

**SQLITE_PRINTF_PRECISION_LIMIT=*N***

> This option limits the maximum width and precision of substitutions for the [printf() SQL function](lang_corefunc.md#printf) and the other C-language string formatting functions such as [sqlite3_mprintf()](c3ref/mprintf.md) and [sqlite3_str_appendf()](c3ref/str_append.md). This is turn can prevent a hostile or malfunctioning script from using excessive memory by invoking a format such as: "`printf('%*s',2147483647,'hi')`". A value for *N* of around 100000 is normally sufficient.
>
> The [printf() SQL function](lang_corefunc.md#printf) is subject to the [SQLITE_LIMIT_LENGTH](c3ref/c_limit_attached.md#sqlitelimitlength) limit of [sqlite3_limit()](c3ref/limit.md). Hence any printf() result with a width or precision more than the SQLITE_LIMIT_LENGTH will cause an [SQLITE_TOOBIG](rescode.md#toobig) error. However, the low-level formatting for the printf() function is done by a subroutine that does not have access to SQLITE_LIMIT_LENGTH. So the low-level formatting is done into a memory allocation that might be considerably larger than SQLITE_LIMIT_LENGTH and the SQLITE_LIMIT_LENGTH check is only performed after all formatting is complete. Thus there might be a transient buffer that exceeds SQLITE_LIMIT_LENGTH. The SQLITE_PRINTF_PRECISION_LIMIT option is an additional check that prevents excess sizes for the transient buffer used inside the low-level formatting subroutine, prior to the SQLITE_LIMIT_LENGTH check.
>
> Be careful not to set SQLITE_PRINTF_PRECISION_LIMIT too low. SQLite uses its [built-in printf()](printf.md) functionality to format the text of CREATE statements stored in the [sqlite_schema table](schematab.md). So SQLITE_PRINTF_PRECISION_LIMIT should be at least as big as the largest table, index, view, or trigger definition that you are likely to encounter.
>
> No error is raised if a width or precision exceeds SQLITE_PRINTF_PRECISION_LIMIT. Instead, the large width or precision is silently truncated.
>
> The default value for SQLITE_PRINTF_PRECISION_LIMIT is 2147483647 (0x7fffffff).

<span id="query_planner_limit"></span>

**SQLITE_QUERY_PLANNER_LIMIT=*N***

> As part of the query planning process, SQLite enumerates all usable combinations of indexes and WHERE-clause constraints. For certain pathological queries, the number of these index-and-constraint combinations can be very large, resulting in slow performance by the query planner. The SQLITE_QUERY_PLANNER_LIMIT value (in conjunction with the related [SQLITE_QUERY_PLANNER_LIMIT_INCR](compile.md#query_planner_limit_incr) setting) limits the number of index-and-constraint combinations that the query planner will consider, in order to prevent the query planner from using excess CPU time. The default value for SQLITE_QUERY_PLANNER_LIMIT is set high enough so that is never reached for real-world queries. The query planner search limit only applies to queries that are deliberately crafted to use excess planning time.

<span id="query_planner_limit_incr"></span>

**SQLITE_QUERY_PLANNER_LIMIT_INCR=*N***

> The [SQLITE_QUERY_PLANNER_LIMIT](compile.md#query_planner_limit) option sets an initial baseline value for the maximum number of index-and-constraint combinations that the query planner will consider. The baseline query planner limit is increased by SQLITE_QUERY_PLANNER_LIMIT_INCR prior to processing each table of a join so that each table is guaranteed to be able to propose at least some index-and-constraint combinations to the optimizer even if prior tables of the join have exhausted the baseline limit. The default value for both this compile-time option and the [SQLITE_QUERY_PLANNER_LIMIT](compile.md#query_planner_limit) option are set high enough so that they should never be reached for real-world queries.

<span id="reverse_unordered_selects"></span>

**SQLITE_REVERSE_UNORDERED_SELECTS**

> This option causes the [PRAGMA reverse_unordered_selects](pragma.md#pragma_reverse_unordered_selects) setting to be enabled by default. When enabled, [SELECT](lang_select.md) statements that lack an ORDER BY clause will run in reverse order.
>
> This option is useful for detecting when applications (incorrectly) assume that the order of rows in a SELECT without an ORDER BY clause will always be the same.

<span id="sorter_pmasz"></span>

**SQLITE_SORTER_PMASZ=*N***

> If multi-threaded processing is enabled via the [PRAGMA threads](pragma.md#pragma_threads) setting, then sort operations will attempt to start helper threads when the amount of content to be sorted exceeds the minimum of the [cache_size](pragma.md#pragma_cache_size) and PMA Size determined by the [SQLITE_CONFIG_PMASZ](c3ref/c_config_covering_index_scan.md#sqliteconfigpmasz) start-time option. This compile-time option sets the default value for the [SQLITE_CONFIG_PMASZ](c3ref/c_config_covering_index_scan.md#sqliteconfigpmasz) start-time option. The default value is 250.

<span id="stmtjrnl_spill"></span>

**SQLITE_STMTJRNL_SPILL=*N***

> The SQLITE_STMTJRNL_SPILL compile-time option determines the default setting of the [SQLITE_CONFIG_STMTJRNL_SPILL](c3ref/c_config_covering_index_scan.md#sqliteconfigstmtjrnlspill) start-time setting. That setting determines the size threshold above which [statement journals](tempfiles.md#stmtjrnl) are moved from memory to disk.

<span id="win32_malloc"></span>

**SQLITE_WIN32_MALLOC**

> This option enables the use of the Windows Heap API functions for memory allocation instead of the standard library malloc() and free() routines.

<span id="yystackdepth"></span>

**YYSTACKDEPTH=*\<max_depth\>***

> This macro sets the maximum depth of the LALR(1) stack used by the SQL parser within SQLite. The default value is 100. A typical application will use less than about 20 levels of the stack. Developers whose applications contain SQL statements that need more than 100 LALR(1) stack entries should seriously consider refactoring their SQL as it is likely to be well beyond the ability of any human to comprehend.

# 5.  Options To Set Size Limits

There are compile-time options that will set upper bounds on the sizes of various structures in SQLite. The compile-time options normally set a hard upper bound that can be changed at run-time on individual [database connections](c3ref/sqlite3.md) using the [sqlite3_limit()](c3ref/limit.md) interface.

The compile-time options for setting upper bounds are [documented separately](limits.md). The following is a list of the available settings:

- [SQLITE_MAX_ATTACHED](limits.md#max_attached)
- [SQLITE_MAX_COLUMN](limits.md#max_column)
- [SQLITE_MAX_COMPOUND_SELECT](limits.md#max_compound_select)
- [SQLITE_MAX_EXPR_DEPTH](limits.md#max_expr_depth)
- [SQLITE_MAX_FUNCTION_ARG](limits.md#max_function_arg)
- [SQLITE_MAX_LENGTH](limits.md#max_length)
- [SQLITE_MAX_LIKE_PATTERN_LENGTH](limits.md#max_like_pattern_length)
- [SQLITE_MAX_PAGE_COUNT](limits.md#max_page_count)
- [SQLITE_MAX_SQL_LENGTH](limits.md#max_sql_length)
- [SQLITE_MAX_VARIABLE_NUMBER](limits.md#max_variable_number)

There are also some size limits that cannot be modified using [sqlite3_limit()](c3ref/limit.md). See, for example:

- [SQLITE_FTS3_MAX_EXPR_DEPTH](compile.md#fts3_max_expr_depth)
- [SQLITE_JSON_MAX_DEPTH](compile.md#json_max_depth)
- [SQLITE_MAX_ALLOCATION_SIZE](compile.md#max_allocation_size)
- [SQLITE_MAX_MEMORY](compile.md#max_memory)
- [SQLITE_MAX_MMAP_SIZE](compile.md#max_mmap_size)
- [SQLITE_PRINTF_PRECISION_LIMIT](compile.md#printf_precision_limit)
- [SQLITE_TRACE_SIZE_LIMIT](compile.md#trace_size_limit)
- [YYSTACKDEPTH](compile.md#yystackdepth)

<span id="controlfeatures"></span>

# 6.  Options To Control Operating Characteristics

<span id="4_byte_aligned_malloc"></span>

**SQLITE_4_BYTE_ALIGNED_MALLOC**

> On most systems, the malloc() system call returns a buffer that is aligned to an 8-byte boundary. But on some systems (ex: windows) malloc() returns 4-byte aligned pointer. This compile-time option must be used on systems that return 4-byte aligned pointers from malloc().

<span id="case_sensitive_like"></span>

**SQLITE_CASE_SENSITIVE_LIKE**

> If this option is present, then the built-in [LIKE](lang_expr.md#like) operator will be case sensitive. This same effect can be achieved at run-time using the [case_sensitive_like pragma](pragma.md#pragma_case_sensitive_like).

<span id="direct_overflow_read"></span>

**SQLITE_DIRECT_OVERFLOW_READ**

> When this option is present, content contained in [overflow pages](fileformat2.md#ovflpgs) of the database file is read directly from disk, bypassing the [page cache](c3ref/pcache_methods2.md), during read transactions. In applications that do a lot of reads of large BLOBs or strings, this option improves read performance.
>
> As of version 3.45.0 (2024-01-15), this option is enabled by default. To disable it, using -DSQLITE_DIRECT_OVERFLOW_READ=0.

<span id="have_isnan"></span>

**SQLITE_HAVE_ISNAN**

> If this option is present, then SQLite will use the isnan() function from the system math library. This is an alias for the [HAVE_ISNAN](compile.md#isnan) configuration option.

<span id="max_allocation_size"></span>

**SQLITE_MAX_ALLOCATION_SIZE=*N***

> This compile-time option sets an upper bound on the size of memory allocations that can be requested using [sqlite3_malloc64()](c3ref/free.md), [sqlite3_realloc64()](c3ref/free.md), and similar. The default value is 2,147,483,391 (0x7ffffeff) and this should be considered an upper bound. Most applications can get by with a maximum allocation size of a few million bytes.
>
> This is a limit on the maximum size of any single memory allocation. It is *not* a limit on the total amount of memory allocated. See [SQLITE_MAX_MEMORY](compile.md#max_memory) for a limitation on the total amount of memory allocated.
>
> Reducing the maximum size of individual memory allocations provides extra defense against denial-of-service attacks that attempt to exhaust system memory by doing many large allocations. It is also an extra layer of defense against application bugs where the size of a memory allocation is computed using a signed 32-bit integer that could overflow → with a small maximum allocation size, such buggy memory allocation size computations are likely to be spotted sooner due to out-of-memory errors and before the integer actually overflows.

<span id="os_other"></span>

**SQLITE_OS_OTHER=*\<0 or 1\>***

> The option causes SQLite to omit its built-in operating system interfaces for Unix, Windows, and OS/2. The resulting library will have no default [operating system interface](c3ref/vfs.md). Applications must use [sqlite3_vfs_register()](c3ref/vfs_find.md) to register an appropriate interface before using SQLite. Applications must also supply implementations for the [sqlite3_os_init()](c3ref/initialize.md) and [sqlite3_os_end()](c3ref/initialize.md) interfaces. The usual practice is for the supplied [sqlite3_os_init()](c3ref/initialize.md) to invoke [sqlite3_vfs_register()](c3ref/vfs_find.md). SQLite will automatically invoke [sqlite3_os_init()](c3ref/initialize.md) when it initializes.
>
> This option is typically used when building SQLite for an embedded platform with a custom operating system.

<span id="secure_delete"></span>

**SQLITE_SECURE_DELETE**

> This compile-time option changes the default setting of the [secure_delete pragma](pragma.md#pragma_secure_delete). When this option is not used, secure_delete defaults to off. When this option is present, secure_delete defaults to on.
>
> The secure_delete setting causes deleted content to be overwritten with zeros. There is a small performance penalty since additional I/O must occur. On the other hand, secure_delete can prevent fragments of sensitive information from lingering in unused parts of the database file after it has been deleted. See the documentation on the [secure_delete pragma](pragma.md#pragma_secure_delete) for additional information.

<span id="threadsafe"></span>

**SQLITE_THREADSAFE=*\<0 or 1 or 2\>***

> This option controls whether or not code is included in SQLite to enable it to operate safely in a multithreaded environment. The default is SQLITE_THREADSAFE=1 which is safe for use in a multithreaded environment. When compiled with SQLITE_THREADSAFE=0 all mutexing code is omitted and it is unsafe to use SQLite in a multithreaded program. When compiled with SQLITE_THREADSAFE=2, SQLite can be used in a multithreaded program so long as no two threads attempt to use the same [database connection](c3ref/sqlite3.md) (or any [prepared statements](c3ref/stmt.md) derived from that database connection) at the same time.
>
> To put it another way, SQLITE_THREADSAFE=1 sets the default [threading mode](threadsafe.md) to Serialized. SQLITE_THREADSAFE=2 sets the default [threading mode](threadsafe.md) to Multi-threaded. And SQLITE_THREADSAFE=0 sets the [threading mode](threadsafe.md) to Single-threaded.
>
> The value of SQLITE_THREADSAFE can be determined at run-time using the [sqlite3_threadsafe()](c3ref/threadsafe.md) interface.
>
> When SQLite has been compiled with SQLITE_THREADSAFE=1 or SQLITE_THREADSAFE=2 then the [threading mode](threadsafe.md) can be altered at run-time using the [sqlite3_config()](c3ref/config.md) interface together with one of these verbs:
>
> - [SQLITE_CONFIG_SINGLETHREAD](c3ref/c_config_covering_index_scan.md#sqliteconfigsinglethread)
> - [SQLITE_CONFIG_MULTITHREAD](c3ref/c_config_covering_index_scan.md#sqliteconfigmultithread)
> - [SQLITE_CONFIG_SERIALIZED](c3ref/c_config_covering_index_scan.md#sqliteconfigserialized)
>
> The [SQLITE_OPEN_NOMUTEX](c3ref/c_open_autoproxy.md) and [SQLITE_OPEN_FULLMUTEX](c3ref/c_open_autoproxy.md) flags to [sqlite3_open_v2()](c3ref/open.md) can also be used to adjust the [threading mode](threadsafe.md) of individual [database connections](c3ref/sqlite3.md) at run-time.
>
> Note that when SQLite is compiled with SQLITE_THREADSAFE=0, the code to make SQLite threadsafe is omitted from the build. When this occurs, it is impossible to change the [threading mode](threadsafe.md) at start-time or run-time.
>
> See the [threading mode](threadsafe.md) documentation for additional information on aspects of using SQLite in a multithreaded environment.

<span id="temp_store"></span>

**SQLITE_TEMP_STORE=*\<0 through 3\>***

> This option controls whether temporary files are stored on disk or in memory. The meanings for various settings of this compile-time option are as follows:
>
> | SQLITE_TEMP_STORE | Meaning |
> |:--:|----|
> | 0 | Always use temporary files |
> | 1 | Use files by default but allow the [PRAGMA temp_store](pragma.md#pragma_temp_store) command to override |
> | 2 | Use memory by default but allow the [PRAGMA temp_store](pragma.md#pragma_temp_store) command to override |
> | 3 | Always use memory |
>
> The default setting is 1. Additional information can be found in [tempfiles.html](tempfiles.md#tempstore).

<span id="trace_size_limit"></span>

**SQLITE_TRACE_SIZE_LIMIT=*N***

> If this macro is defined to a positive integer *N*, then the length of strings and BLOBs that are expanded into parameters in the output of [sqlite3_trace()](c3ref/profile.md) is limited to *N* bytes.

<span id="trusted_schema"></span>

**SQLITE_TRUSTED_SCHEMA=*\<0 or 1\>***

> This macro determines the default value for the [SQLITE_DBCONFIG_TRUSTED_SCHEMA](c3ref/c_dbconfig_defensive.md#sqlitedbconfigtrustedschema) and [PRAGMA trusted_schema](pragma.md#pragma_trusted_schema) setting. If no alternative is specified, the trusted-schema setting defaults to ON (a value of 1) for legacy compatibility. However, for best security, systems that implement [application-defined SQL functions](appfunc.md) and/or [virtual tables](vtab.md) should consider changing the default to OFF.

<span id="use_uri"></span>

**SQLITE_USE_URI**

> This option causes the [URI filename](uri.md) process logic to be enabled by default.

<span id="enablefeatures"></span>

# 7.  Options To Enable Features Normally Turned Off

<span id="allow_uri_authority"></span>

**SQLITE_ALLOW_URI_AUTHORITY**

> [URI filenames](uri.md) normally throws an error if the authority section is not either empty or "localhost". However, if SQLite is compiled with the SQLITE_ALLOW_URI_AUTHORITY compile-time option, then the URI is converted into a Uniform Naming Convention (UNC) filename and passed down to the underlying operating system that way.
>
> Some future versions of SQLite may change to enable this feature by default.

<span id="allow_covering_index_scan"></span>

**SQLITE_ALLOW_COVERING_INDEX_SCAN=*\<0 or 1\>***

> This C-preprocess macro determines the default setting of the [SQLITE_CONFIG_COVERING_INDEX_SCAN](c3ref/c_config_covering_index_scan.md#sqliteconfigcoveringindexscan) configuration setting. It defaults to 1 (on) which means that covering indices are used for full table scans where possible, in order to reduce I/O and improve performance. However, the use of a covering index for a full scan will cause results to appear in a different order from legacy, which could cause some (incorrectly-coded) legacy applications to break. Hence, the covering index scan option can be disabled at compile-time on systems that want to minimize their risk of exposing errors in legacy applications.

<span id="enable_8_3_names"></span>

**SQLITE_ENABLE_8_3_NAMES=*\<1 or 2\>***

> If this C-preprocessor macro is defined, then extra code is included that allows SQLite to function on a filesystem that only supports 8+3 filenames. If the value of this macro is 1, then the default behavior is to continue to use long filenames and to only use 8+3 filenames if the database connection is opened using [URI filenames](uri.md) with the "`8_3_names=1`" query parameter. If the value of this macro is 2, then the use of 8+3 filenames becomes the default but may be disabled on using the `8_3_names=0` query parameter.

<span id="enable_api_armor"></span>

**SQLITE_ENABLE_API_ARMOR**

> When defined, this C-preprocessor macro activates extra code that attempts to detect misuse of the SQLite API, such as passing in NULL pointers to required parameters or using objects after they have been destroyed. When this option is enabled and an illegal API usage is detected, the interface will typically return SQLITE_MISUSE.
>
> The SQLITE_ENABLE_API_ARMOR option does not guarantee that all illegal API usages will be detected. Even when SQLITE_ENABLE_API_ARMOR is enabled, passing incorrect values into the C-language APIs can cause a process crash due to segmentation fault or null-pointer deference or other reasons. The SQLITE_ENABLE_API_ARMOR compile-time option is intended as an aid for application testing and debugging option. Applications should not depend on SQLITE_ENABLE_API_ARMOR for safety. SQLITE_ENABLE_API_ARMOR is appropriate as a second line of defense against application bugs, but it should not be the only defense. If any SQLite interface returns SQLITE_MISUSE, that indicates that the application is using SQLite contrary to the spec and that the application contains a bug. The SQLITE_MISUSE return provides the application with the opportunity to respond gracefully to that bug, rather than simply crashing the process or invoking undefined behavior, but nothing more. Applications should neither make use of nor depend upon SQLITE_MISUSE for routine processing.

<span id="enable_atomic_write"></span>

**SQLITE_ENABLE_ATOMIC_WRITE**

> If this C-preprocessor macro is defined and if the xDeviceCharacteristics method of [sqlite3_io_methods](c3ref/io_methods.md) object for a database file reports (via one of the [SQLITE_IOCAP_ATOMIC](c3ref/c_iocap_atomic.md) bits) that the filesystem supports atomic writes and if a transaction involves a change to only a single page of the database file, then the transaction commits with just a single write request of a single page of the database and no rollback journal is created or written. On filesystems that support atomic writes, this optimization can result in significant speed improvements for small updates. However, few filesystems support this capability and the code paths that check for this capability slow down write performance on systems that lack atomic write capability, so this feature is disabled by default.

<span id="enable_batch_atomic_write"></span>

**SQLITE_ENABLE_BATCH_ATOMIC_WRITE**

> This compile-time option enables SQLite to take advantage of batch atomic write capabilities in the underlying filesystem. As of SQLite version 3.21.0 (2017-10-24) this is only supported on [F2FS](https://en.wikipedia.org/wiki/F2FS). However, the interface is implemented generically, using [sqlite3_file_control()](c3ref/file_control.md) with [SQLITE_FCNTL_BEGIN_ATOMIC_WRITE](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlbeginatomicwrite) and [SQLITE_FCNTL_COMMIT_ATOMIC_WRITE](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlcommitatomicwrite) so the capability can be added to other filesystems in the future. When this option is enabled, SQLite automatically detects that the underlying filesystem supports batch atomic writes, and when it does so it avoids writing the [rollback journal](lockingv3.md#rollback) for transaction control. This can make transactions over twice as fast, while simultaneously reducing wear on SSD storage devices.
>
> Future versions of SQLite might enable the batch-atomic-write capability by default, at which point this compile-time option will become superfluous.

<span id="enable_bytecode_vtab"></span>

**SQLITE_ENABLE_BYTECODE_VTAB**

> This option enables the [bytecode and tables_used virtual tables](bytecodevtab.md).

<span id="enable_carray"></span>

**SQLITE_ENABLE_CARRAY**

> This option enables the [carray() extension](carray.md), which has been available in [the amalgamation](amalgamation.md) since SQLite version 3.51.0 (2025-11-04). Prior to version 3.51.0, the carray() extension was in a separate source code file that needed to be compiled independently and linked as a [loadable extension](loadext.md).

<span id="enable_column_metadata"></span>

**SQLITE_ENABLE_COLUMN_METADATA**

> When this C-preprocessor macro is defined, SQLite includes some additional APIs that provide convenient access to meta-data about tables and queries. The APIs that are enabled by this option are:
>
> - [sqlite3_column_database_name()](c3ref/column_database_name.md)
> - [sqlite3_column_database_name16()](c3ref/column_database_name.md)
> - [sqlite3_column_table_name()](c3ref/column_database_name.md)
> - [sqlite3_column_table_name16()](c3ref/column_database_name.md)
> - [sqlite3_column_origin_name()](c3ref/column_database_name.md)
> - [sqlite3_column_origin_name16()](c3ref/column_database_name.md)

<span id="enable_dbpage_vtab"></span>

**SQLITE_ENABLE_DBPAGE_VTAB**

> This option enables the [SQLITE_DBPAGE virtual table](dbpage.md).

<span id="enable_dbstat_vtab"></span>

**SQLITE_ENABLE_DBSTAT_VTAB**

> This option enables the [dbstat virtual table](dbstat.md).

<span id="enable_deserialize"></span>

**SQLITE_ENABLE_DESERIALIZE**

> This option was formerly used to enable the [sqlite3_serialize()](c3ref/serialize.md) and [sqlite3_deserialize()](c3ref/deserialize.md) interfaces. However, as of SQLite 3.36.0 (2021-06-18) those interfaces are enabled by default and a new compile-time option [SQLITE_OMIT_DESERIALIZE](compile.md#omit_deserialize) is added to omit them.

<span id="enable_explain_comments"></span>

**SQLITE_ENABLE_EXPLAIN_COMMENTS**

> This option adds extra logic to SQLite that inserts comment text into the output of [EXPLAIN](lang_explain.md). These extra comments use extra memory, thus making [prepared statements](c3ref/stmt.md) larger and very slightly slower, and so they are turned off by default and in most applications. But some applications, such as the [command-line shell](cli.md) for SQLite, value clarity of EXPLAIN output over raw performance and so this compile-time option is available to them. The SQLITE_ENABLE_EXPLAIN_COMMENTS compile-time option is also enabled automatically if [SQLITE_DEBUG](compile.md#debug) is enabled.

<span id="enable_fts3"></span>

**SQLITE_ENABLE_FTS3**

> When this option is defined in the [amalgamation](amalgamation.md), versions 3 and 4 of the full-text search engine are added to the build automatically.

<span id="enable_fts3_parenthesis"></span>

**SQLITE_ENABLE_FTS3_PARENTHESIS**

> This option modifies the query pattern parser in FTS3 such that it supports operators AND and NOT (in addition to the usual OR and NEAR) and also allows query expressions to contain nested parentheses.

<span id="enable_fts3_tokenizer"></span>

**SQLITE_ENABLE_FTS3_TOKENIZER**

> This option enables the two-argument version of the [fts3_tokenizer()](fts3.md#f3tknzr) interface. The second argument to fts3_tokenizer() should be a pointer to a function (encoded as a BLOB) that implements an application defined tokenizer. If hostile actors are able to run the two-argument version of fts3_tokenizer() with an arbitrary second argument, they could crash or take control of the process.
>
> Because of security concerns, the two-argument fts3_tokenizer() feature was disabled beginning with [Version 3.11.0](releaselog/3_11_0.md) (2016-02-15) unless this compile-time option is used. [Version 3.12.0](releaselog/3_12_0.md) (2016-03-29) added the [sqlite3_db_config](c3ref/db_config.md)(db,[SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenablefts3tokenizer),1,0) interface that activates the two-argument version of [fts3_tokenizer()](fts3.md#f3tknzr) for a specific [database connection](c3ref/sqlite3.md) at run-time.

<span id="enable_fts4"></span>

**SQLITE_ENABLE_FTS4**

> When this option is defined in the [amalgamation](amalgamation.md), versions 3 and 4 of the full-text search engine are added to the build automatically.

<span id="enable_fts5"></span>

**SQLITE_ENABLE_FTS5**

> When this option is defined in the [amalgamation](amalgamation.md), version 5 of the full-text search engine ([fts5](fts5.md)) is added to the build automatically.

<span id="enable_geopoly"></span>

**SQLITE_ENABLE_GEOPOLY**

> When this option is defined in the [amalgamation](amalgamation.md), the [Geopoly extension](geopoly.md) is included in the build.

<span id="enable_hidden_columns"></span>

**SQLITE_ENABLE_HIDDEN_COLUMNS**

> When this option is defined in the [amalgamation](amalgamation.md), The [hidden columns](vtab.md#hiddencol) feature is enabled for virtual tables.

<span id="enable_icu"></span>

**SQLITE_ENABLE_ICU**

> This option causes the [International Components for Unicode](https://icu.unicode.org) or "ICU" extension to SQLite to be added to the build.

<span id="enable_iotrace"></span>

**SQLITE_ENABLE_IOTRACE**

> When both the SQLite core and the [Command Line Interface](cli.md) (CLI) are both compiled with this option, then the CLI provides an extra command named ".iotrace" that provides a low-level log of I/O activity. This option is experimental and may be discontinued in a future release.

<span id="enable_json1"></span>

**SQLITE_ENABLE_JSON1**

> This compile-time option is a no-op. Prior to SQLite version 3.38.0 (2022-02-22), it was necessary to compile with this option in order to include the [JSON SQL functions](json1.md) in the build. However, beginning with SQLite version 3.38.0, those functions are included by default. Use the [-DSQLITE_OMIT_JSON](compile.md#omit_json) option to omit them.

<span id="enable_locking_style"></span>

**SQLITE_ENABLE_LOCKING_STYLE**

> This option enables additional logic in the OS interface layer for Mac OS X. The additional logic attempts to determine the type of the underlying filesystem and choose an alternative locking strategy that works correctly for that filesystem type. Five locking strategies are available:
>
> - POSIX locking style. This is the default locking style and the style used by other (non Mac OS X) Unixes. Locks are obtained and released using the fcntl() system call.
> - AFP locking style. This locking style is used for network file systems that use the AFP (Apple Filing Protocol) protocol. Locks are obtained by calling the library function \_AFPFSSetLock().
> - Flock locking style. This is used for file-systems that do not support POSIX locking style. Locks are obtained and released using the flock() system call.
> - Dot-file locking style. This locking style is used when neither flock nor POSIX locking styles are supported by the file system. Database locks are obtained by creating an entry in the file-system at a well-known location relative to the database file (a "dot-file") and relinquished by deleting the same file.
> - No locking style. If none of the above can be supported, this locking style is used. No database locking mechanism is used. When this system is used it is not safe for a single database to be accessed by multiple clients.
>
> Additionally, five extra [VFS](vfs.md) implementations are provided as well as the default. By specifying one of the extra VFS implementations when calling [sqlite3_open_v2()](c3ref/open.md), an application may bypass the file-system detection logic and explicitly select one of the above locking styles. The five extra [VFS](vfs.md) implementations are called "unix-posix", "unix-afp", "unix-flock", "unix-dotfile" and "unix-none".

<span id="enable_math_functions"></span>

**SQLITE_ENABLE_MATH_FUNCTIONS**

> This macro enables the [built-in SQL math functions](lang_mathfunc.md). This option is automatically added to the Makefile by the configure script on unix platforms, unless the --disable-math option is used. This option is also included on Windows builds using the "Makefile.msc" makefile for nmake.

<span id="enable_memory_management"></span>

**SQLITE_ENABLE_MEMORY_MANAGEMENT**

> This option adds extra logic to SQLite that allows it to release unused memory upon request. This option must be enabled in order for the [sqlite3_release_memory()](c3ref/release_memory.md) interface to work. If this compile-time option is not used, the [sqlite3_release_memory()](c3ref/release_memory.md) interface is a no-op.

<span id="enable_memsys3"></span>

**SQLITE_ENABLE_MEMSYS3**

> This option includes code in SQLite that implements an alternative memory allocator. This alternative memory allocator is only engaged when the [SQLITE_CONFIG_HEAP](c3ref/c_config_covering_index_scan.md#sqliteconfigheap) option to [sqlite3_config()](c3ref/config.md) is used to supply a large chunk of memory from which all memory allocations are taken. The MEMSYS3 memory allocator uses a hybrid allocation algorithm patterned after dlmalloc(). Only one of SQLITE_ENABLE_MEMSYS3 and SQLITE_ENABLE_MEMSYS5 may be enabled at once.

<span id="enable_memsys5"></span>

**SQLITE_ENABLE_MEMSYS5**

> This option includes code in SQLite that implements an alternative memory allocator. This alternative memory allocator is only engaged when the [SQLITE_CONFIG_HEAP](c3ref/c_config_covering_index_scan.md#sqliteconfigheap) option to [sqlite3_config()](c3ref/config.md) is used to supply a large chunk of memory from which all memory allocations are taken. The MEMSYS5 module rounds all allocations up to the next power of two and uses a first-fit, buddy-allocator algorithm that provides strong guarantees against fragmentation and breakdown subject to certain operating constraints.

<span id="enable_normalize"></span>

**SQLITE_ENABLE_NORMALIZE**

> This option includes the [sqlite3_normalized_sql()](c3ref/expanded_sql.md) API.

<span id="enable_null_trim"></span>

**SQLITE_ENABLE_NULL_TRIM**

> This option enables an optimization that omits NULL columns at the ends of rows, for a space savings on disk.
>
> Databases generated with this option enabled are not readable by SQLite version 3.1.6 (2005-03-17) and earlier. Also, databases generated with this option enabled are prone to triggering the [e6e962d6b0f06f46](https://sqlite.org/src/info/e6e962d6b0f06f46e) bug in the [sqlite3_blob_reopen()](c3ref/blob_reopen.md) interface. For those reasons, this optimization is disabled by default. However, this optimization may be enabled by default in a future release of SQLite.

<span id="enable_offset_sql_func"></span>

**SQLITE_ENABLE_OFFSET_SQL_FUNC**

> This option enables support for the [sqlite_offset(X)](lang_corefunc.md#sqlite_offset) SQL function.
>
> The [sqlite_offset(X)](lang_corefunc.md#sqlite_offset) SQL function requires a new interface on the B-tree storage engine, a new opcode in the [virtual machine](opcode.md) that runs SQL statements, and a new conditional in a critical path of the code generator. To avoid that overhead in applications that do not need the utility of sqlite_offset(X), the function is disabled by default.

<span id="enable_ordered_set_aggregates"></span>

**SQLITE_ENABLE_ORDERED_SET_AGGREGATES**

> This option enables support for the "WITHIN GROUP ORDER BY" ordered-set aggregate syntax. For example:
>
> \
>           SELECT percentile_cont(0.75) WITHIN GROUP (ORDER BY x) FROM tab;
>
> The above is the SQL-standard way to compute the 75th-percentile value of a distribution. The usual way to do this in SQLite is as follows:
>
> \
>           SELECT percentile_cont(x,0.75) FROM tab;
>
> Though simpler, easier to read, and easier to type, this syntax is *not* compliant with standard SQL. The simpler, non-standard syntax is always available in SQLite. But the SQL-standard compliant syntax is only available if compiled using -DSQLITE_ENABLE_ORDERED_SET_AGGREGATES. The SQL-standard compliant syntax is disabled by default because (A) it requires about 1,200 bytes of extra code in the compiled SQLite binary and (B) because it makes your SQL code more difficult to read, write, and understand without adding any value. Use this option only if you need to write cross-platform SQL that uses ordered-set aggregate functions such as [percentile_cont()](lang_aggfunc.md#percentile_cont).
>
> Using this compile-time option adds WITHIN as a keyword.
>
> The ordered-set aggregate syntax can only be used by aggregate functions that have the [SQLITE_SELFORDER1](c3ref/c_deterministic.md#sqliteselforder1) property. If the SQLITE_ENABLE_ORDERED_SET_AGGREGATES compile-time option is not specified, then the [SQLITE_SELFORDER1](c3ref/c_deterministic.md#sqliteselforder1) property is essentially a no-op.
>
> This compile-time option only works when building from canonical source code, since it changes the LALR(1) parser tables. This compile-time option cannot be used to change the behavior of an [amalgamation](amalgamation.md).

<span id="enable_percentile"></span>

**SQLITE_ENABLE_PERCENTILE**

> This option enables the [percentile extension](percentile.md), which has been available in [the amalgamation](amalgamation.md) since SQLite version 3.51.0 (2025-11-04). Prior to version 3.51.0, the percentile extension was in a separate source code file that needed to be compiled independently and linked as a [loadable extension](loadext.md).

<span id="enable_preupdate_hook"></span>

**SQLITE_ENABLE_PREUPDATE_HOOK**

> This option enables [several new APIs](c3ref/preupdate_blobwrite.md) that provide callbacks prior to any change to a [rowid table](rowidtable.md). The callbacks can be used to record the state of the row before the change occurs.
>
> The action of the preupdate hook is similar to the [update hook](c3ref/update_hook.md) except that the callback is invoked before the change, not afterwards, and the preupdate hook interfaces are omitted unless this compile-time option is used.
>
> The preupdate hook interfaces were originally added to support the [session](sessionintro.md) extension.

<span id="enable_qpsg"></span>

**SQLITE_ENABLE_QPSG**

> This option causes the [query planner stability guarantee](queryplanner-ng.md#qpstab) (QPSG) to be on by default. Normally the QPSG is off and must be activated at run-time using the [SQLITE_DBCONFIG_ENABLE_QPSG](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableqpsg) option to the [sqlite3_db_config()](c3ref/db_config.md) interface.

<span id="enable_rbu"></span>

**SQLITE_ENABLE_RBU**

> Enable the code that implements the [RBU extension](rbu.md).

<span id="enable_rtree"></span>

**SQLITE_ENABLE_RTREE**

> This option causes SQLite to include support for the [R\*Tree index extension](rtree.md).

<span id="enable_session"></span>

**SQLITE_ENABLE_SESSION**

> This option enables the [session extension](sessionintro.md).

<span id="enable_snapshot"></span>

**SQLITE_ENABLE_SNAPSHOT**

> This option enables the code to support the [sqlite3_snapshot](c3ref/snapshot.md) object and its related interfaces:
>
> - [sqlite3_snapshot_get()](c3ref/snapshot_get.md) (constructor)
> - [sqlite3_snapshot_free()](c3ref/snapshot_free.md) (destructor)
> - [sqlite3_snapshot_open()](c3ref/snapshot_open.md)
> - [sqlite3_snapshot_cmp()](c3ref/snapshot_cmp.md)
> - [sqlite3_snapshot_recover()](c3ref/snapshot_recover.md)

<span id="enable_sorter_references"></span>

**SQLITE_ENABLE_SORTER_REFERENCES**

> This option activates an optimization that reduces the memory required by the sorter at the cost of doing additional B-tree lookups after the sort has occurred.
>
> The default sorting procedure is to gather all information that will ultimately be output into a "record" and pass that complete record to the sorter. But in some cases, for example if some of the output columns consists of large BLOB values, the size of the each record can be large, which means that the sorter has to either use more memory, and/or write more content to temporary storage.
>
> When SQLITE_ENABLE_SORTER_REFERENCES is enabled, the records passed to the sorter often contain only a [ROWID](lang_createtable.md#rowid) value. Such records are much smaller. This means the sorter has much less "payload" to deal with and can run faster. After sorting has occurred, the ROWID is used to look up the output column values in the original table. That requires another search into the table, and could potentially result in a slowdown. Or, it might be a performance win, depending on how large the values are.
>
> Even when the SQLITE_ENABLE_SORTER_REFERENCES compile-time option is on, sorter references are still disabled by default. To use sorter references, the application must set a sorter reference size threshold using the [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_SORTERREF_SIZE](c3ref/c_config_covering_index_scan.md#sqliteconfigsorterrefsize)) interface at start-time.
>
> Because the SQLite developers do not know whether the SQLITE_ENABLE_SORTER_REFERENCES option will help or hurt performance, it is disabled by default at this time (2018-05-04). It might be enabled by default in some future release, depending on what is learned about its impact on performance.

<span id="enable_stmt_scanstatus"></span>

**SQLITE_ENABLE_STMT_SCANSTATUS**

> This option enables the [sqlite3_stmt_scanstatus()](c3ref/stmt_scanstatus.md) and [sqlite3_stmt_scanstatus_v2()](c3ref/stmt_scanstatus.md) interfaces and activates the [nexec and ncycle](bytecodevtab.md#nexec) columns of the [bytecode virtual table](bytecodevtab.md). These features are normally omitted or deactivated because they impose a run-time performance cost even if unused.
>
> The SQLITE_ENABLE_STMT_SCANSTATUS option is not recommended for production builds because of the added run-time cost even when the performance statistics are not used. But SQLITE_ENABLE_STMT_SCANSTATUS is useful for diagnostic and debugging builds.

<span id="enable_stmtvtab"></span>

**SQLITE_ENABLE_STMTVTAB**

> This compile-time option enables the [SQLITE_STMT virtual table](stmt.md) logic.

<span id="rtree_int_only"></span>

**SQLITE_RTREE_INT_ONLY**

> This compile-time option is deprecated and untested.

<span id="enable_sqllog"></span>

**SQLITE_ENABLE_SQLLOG**

> This option enables extra code (especially the [SQLITE_CONFIG_SQLLOG](c3ref/c_config_covering_index_scan.md#sqliteconfigsqllog) option to [sqlite3_config()](c3ref/config.md)) that can be used to create logs of all SQLite processing performed by an application. These logs can be useful in doing off-line analysis of the behavior of an application, and especially for performance analysis. In order for the SQLITE_ENABLE_SQLLOG option to be useful, some extra code is required. The ["test_sqllog.c"](https://sqlite.org/src/doc/trunk/src/test_sqllog.c) source code file in the SQLite source tree is a working example of the required extra code. On unix and windows systems, a developer can append the text of the "test_sqllog.c" source code file to the end of an "sqlite3.c" amalgamation, recompile the application using the -DSQLITE_ENABLE_SQLLOG option, then control logging using environment variables. See the header comment on the "test_sqllog.c" source file for additional detail.

<span id="enable_stat2"></span>

**SQLITE_ENABLE_STAT2**

> This option used to cause the [ANALYZE](lang_analyze.md) command to collect index histogram data in the **sqlite_stat2** table. But that functionality was superseded by [SQLITE_ENABLE_STAT3](compile.md#enable_stat3) as of SQLite [version 3.7.9](releaselog/3_7_9.md) (2011-11-01). The SQLITE_ENABLE_STAT2 compile-time option is now a no-op.

<span id="enable_stat3"></span>

**SQLITE_ENABLE_STAT3**

> This option used to cause the [ANALYZE](lang_analyze.md) command to collect index histogram data in the **sqlite_stat3** table. But that functionality was superseded by [SQLITE_ENABLE_STAT4](compile.md#enable_stat4) as of SQLite [version 3.8.1](releaselog/3_8_1.md) (2013-10-17). The SQLITE_ENABLE_STAT3 compile-time option continued to be supported through [version 3.29.0](releaselog/3_29_0.md) (2019-07-10) but has now become a no-op.

<span id="enable_stat4"></span>

**SQLITE_ENABLE_STAT4**

> This option adds additional logic to the [ANALYZE](lang_analyze.md) command and to the [query planner](optoverview.md) that can help SQLite to choose a better query plan under certain situations. The [ANALYZE](lang_analyze.md) command is enhanced to collect histogram data from all columns of every index and store that data in the [sqlite_stat4](fileformat2.md#stat4tab) table. The query planner will then use the histogram data to help it make better index choices. The downside of this compile-time option is that it violates the [query planner stability guarantee](queryplanner-ng.md#qpstab) making it more difficult to ensure consistent performance in mass-produced applications.
>
> SQLITE_ENABLE_STAT4 is an enhancement of [SQLITE_ENABLE_STAT3](compile.md#enable_stat3). STAT3 only recorded histogram data for the left-most column of each index whereas the STAT4 enhancement records histogram data from all columns of each index. The [SQLITE_ENABLE_STAT3](compile.md#enable_stat3) compile-time option has become a no-op.

<span id="enable_tree_explain"></span>

**SQLITE_ENABLE_TREE_EXPLAIN**

> This compile-time option is no longer used.

<span id="enable_update_delete_limit"></span>

**SQLITE_ENABLE_UPDATE_DELETE_LIMIT**

> This option enables an optional ORDER BY and LIMIT clause on [UPDATE](lang_update.md) and [DELETE](lang_delete.md) statements.
>
> If this option is defined, then it must also be defined when using the [Lemon parser generator](lemon.md) tool to generate a parse.c file. Because of this, this option may only be used when the library is built from source, not from the [amalgamation](amalgamation.md) or from the collection of pre-packaged C files provided for non-Unix like platforms on the website.

<span id="enable_unknown_sql_function"></span>

**SQLITE_ENABLE_UNKNOWN_SQL_FUNCTION**

> When the SQLITE_ENABLE_UNKNOWN_SQL_FUNCTION compile-time option is activated, SQLite will suppress "unknown function" errors when running an [EXPLAIN](lang_explain.md) or [EXPLAIN QUERY PLAN](eqp.md). Instead of throwing an error, SQLite will insert a substitute no-op function named "unknown()". The substitution of "unknown()" in place of unrecognized functions only occurs on [EXPLAIN](lang_explain.md) and [EXPLAIN QUERY PLAN](eqp.md), not on ordinary statements.
>
> When used in the [command-line shell](cli.md), the SQLITE_ENABLE_UNKNOWN_SQL_FUNCTION feature allows SQL text that contains application-defined functions to be pasted into the shell for analysis and debugging without having to create and load an extension that implements the application-defined functions.

<span id="enable_unlock_notify"></span>

**SQLITE_ENABLE_UNLOCK_NOTIFY**

> This option enables the [sqlite3_unlock_notify()](c3ref/unlock_notify.md) interface and its associated functionality. See the documentation titled [Using the SQLite Unlock Notification Feature](unlock_notify.md) for additional information.

<span id="introspection_pragmas"></span>

**SQLITE_INTROSPECTION_PRAGMAS**

> This option is obsolete. It used to enable some extra PRAGMA statements such as [PRAGMA function_list](pragma.md#pragma_function_list), [PRAGMA module_list](pragma.md#pragma_module_list), and [PRAGMA pragma_list](pragma.md#pragma_pragma_list), but those pragmas are now all enabled by default. See [SQLITE_OMIT_INTROSPECTION_PRAGMAS](compile.md#omit_introspection_pragmas).

<span id="soundex"></span>

**SQLITE_SOUNDEX**

> This option enables the [soundex() SQL function](lang_corefunc.md#soundex).

<span id="strict_subtype"></span>

**SQLITE_STRICT_SUBTYPE=1**

> This option causes [application-defined SQL functions](appfunc.md) to raise an SQL error if they invoke the [sqlite3_result_subtype()](c3ref/result_subtype.md) interface but were not registered with the [SQLITE_RESULT_SUBTYPE](c3ref/c_deterministic.md#sqliteresultsubtype) property. This recommended option helps to identify problems in the implementation of application-defined SQL functions early in the development cycle.

<span id="use_alloca"></span>

**SQLITE_USE_ALLOCA**

> If this option is enabled, then the alloca() memory allocator will be used in a few situations where it is appropriate. This results in a slightly smaller and faster binary. The SQLITE_USE_ALLOCA compile-time only works, of course, on systems that support alloca().

<span id="use_fcntl_trace"></span>

**SQLITE_USE_FCNTL_TRACE**

> This option causes SQLite to issue extra [SQLITE_FCNTL_TRACE](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntltrace) file controls to provide supplementary information to the VFS. The "vfslog.c" extension makes use of this to provide enhanced logs of VFS activity.

<span id="use_seh"></span>

**SQLITE_USE_SEH**

> This option used to be a toggle to enable what is now controlled by [SQLITE_OMIT_SEH](compile.md#omit_seh). Client code should not use this define, as it is used internally by the library.

<span id="have_zlib"></span>

**SQLITE_HAVE_ZLIB**

> This option causes some extensions to link against the [zlib compression library](https://zlib.net).
>
> This option has no effect on the SQLite core. It is only used by extensions. This option is necessary for the compression and decompression functions that are part of [SQL Archive](sqlar.md) support in the [command-line shell](cli.md).
>
> When compiling with this option, it will normally be necessary to add a linker option to include the zlib library in the build. Normally this option is "-lz" but might be different on different systems.
>
> When building with MSVC on Windows systems, one can put the zlib source code in the compat/zlib subdirectory of the source tree and then add the USE_ZLIB=1 option to the nmake command to cause the Makefile.msc to automatically build and use an appropriate zlib library implementation.

<span id="yytrackmaxstackdepth"></span>

**YYTRACKMAXSTACKDEPTH**

> This option causes the LALR(1) parser stack depth to be tracked and reported using the [sqlite3_status](c3ref/status.md)([SQLITE_STATUS_PARSER_STACK](c3ref/c_status_malloc_count.md#sqlitestatusparserstack),...) interface. SQLite's LALR(1) parser has a fixed stack depth (determined at compile-time using the [YYSTACKDEPTH](compile.md#yystackdepth) options). This option can be used to help determine if an application is getting close to exceeding the maximum LALR(1) stack depth.

<span id="disablefeatures"></span>

# 8.  Options To Disable Features Normally Turned On

<span id="disable_lfs"></span>

**SQLITE_DISABLE_LFS**

> If this C-preprocessor macro is defined, large file support is disabled.

<span id="disable_dirsync"></span>

**SQLITE_DISABLE_DIRSYNC**

> If this C-preprocessor macro is defined, directory syncs are disabled. SQLite typically attempts to sync the parent directory when a file is deleted to ensure the directory entries are updated immediately on disk.

<span id="disable_fts3_unicode"></span>

**SQLITE_DISABLE_FTS3_UNICODE**

> If this C-preprocessor macro is defined, the [unicode61](fts3.md#unicode61) tokenizer in [FTS3](fts3.md) is omitted from the build and is unavailable to applications.

<span id="disable_fts4_deferred"></span>

**SQLITE_DISABLE_FTS4_DEFERRED**

> If defined, this C-preprocessor macro disables the "deferred token" optimization in [FTS4](fts3.md#fts4). The "deferred token" optimization avoids loading massive posting lists for terms that are in most documents of the collection and instead simply scans for those tokens in the document source. [FTS4](fts3.md#fts4) should get exactly the same answer both with and without this optimization.

<span id="disable_intrinsic"></span>

**SQLITE_DISABLE_INTRINSIC**

> This option disables the use of compiler-specific built-in functions such as \_\_builtin_bswap32() and \_\_builtin_add_overflow() in GCC and Clang, or \_byteswap_ulong() and \_ReadWriteBarrier() with MSVC.

<span id="disable_pagecache_overflow_stats"></span>

**SQLITE_DISABLE_PAGECACHE_OVERFLOW_STATS**

> This option disables the collection of the [sqlite3_status()](c3ref/status.md), [SQLITE_STATUS_PAGECACHE_OVERFLOW](c3ref/c_status_malloc_count.md#sqlitestatuspagecacheoverflow) and [SQLITE_STATUS_PAGECACHE_SIZE](c3ref/c_status_malloc_count.md#sqlitestatuspagecachesize) statistics. Setting this option has been shown to increase performance in high concurrency multi-threaded applications.

<span id="omitfeatures"></span>

# 9.  Options To Omit Features

The following options can be used to [reduce the size of the compiled library](footprint.md) by omitting unused features. This is probably only useful in embedded systems where space is especially tight, as even with all features included the SQLite library is relatively small. Don't forget to tell your compiler to optimize for binary size! (the -Os option if using GCC). Telling your compiler to optimize for size usually has a much larger impact on library footprint than employing any of these compile-time options. You should also verify that [debugging options](#debugoptions) are disabled.

The macros in this section do not require values. The following compilation switches all have the same effect:\
-DSQLITE_OMIT_ALTERTABLE\
-DSQLITE_OMIT_ALTERTABLE=1\
-DSQLITE_OMIT_ALTERTABLE=0

If any of these options are defined, then the same set of SQLITE_OMIT\_\* options must also be defined when using the [Lemon parser generator](lemon.md) tool to generate the parse.c file and when compiling the 'mkkeywordhash' tool which generates the keywordhash.h file. Because of this, these options may only be used when the library is built from canonical source, not from the [amalgamation](amalgamation.md). Some SQLITE_OMIT\_\* options might work, or appear to work, when used with the [amalgamation](amalgamation.md). But this is not guaranteed. In general, always compile from canonical sources in order to take advantage of SQLITE_OMIT\_\* options.

> ***Important Note:** The SQLITE_OMIT\_\* options may not work with the [amalgamation](amalgamation.md). SQLITE_OMIT\_\* compile-time options usually work correctly only when SQLite is built from canonical source files.*

Special versions of the SQLite amalgamation that do work with a predetermined set of SQLITE_OMIT\_\* options can be generated. To do so, make a copy of the Makefile.linux-gcc makefile template in the canonical source code distribution. Change the name of your copy to simply "Makefile". Then edit "Makefile" to set up appropriate compile-time options. Then type:

make clean; make sqlite3.c\

The resulting "sqlite3.c" amalgamation code file (and its associated header file "sqlite3.h") can then be moved to a non-unix platform for final compilation using a native compiler.

The SQLITE_OMIT\_\* options are unsupported. By this we mean that an SQLITE_OMIT\_\* option that omits code from the build in the current release might become a no-op in the next release. Or the other way around: an SQLITE_OMIT\_\* that is a no-op in the current release might cause code to be excluded in the next release. Also, not all SQLITE_OMIT\_\* options are tested. Some SQLITE_OMIT\_\* options might cause SQLite to malfunction and/or provide incorrect answers.

> ***Important Note:** The SQLITE_OMIT\_\* compile-time options are mostly unsupported.*

The following are the available OMIT options: <span id="omit_altertable"></span>

**SQLITE_OMIT_ALTERTABLE**

> When this option is defined, the [ALTER TABLE](lang_altertable.md) command is not included in the library. Executing an [ALTER TABLE](lang_altertable.md) statement causes a parse error.

<span id="omit_analyze"></span>

**SQLITE_OMIT_ANALYZE**

> When this option is defined, the [ANALYZE](lang_analyze.md) command is omitted from the build.

<span id="omit_attach"></span>

**SQLITE_OMIT_ATTACH**

> When this option is defined, the [ATTACH](lang_attach.md) and [DETACH](lang_detach.md) commands are omitted from the build.

<span id="omit_authorization"></span>

**SQLITE_OMIT_AUTHORIZATION**

> Defining this option causes the [sqlite3_set_authorizer()](c3ref/set_authorizer.md) API function and related logic to be omitted.

<span id="omit_autoincrement"></span>

**SQLITE_OMIT_AUTOINCREMENT**

> This option is omits the [AUTOINCREMENT](autoinc.md) feature. When this is macro is defined, columns declared as "[INTEGER PRIMARY KEY](lang_createtable.md#rowid) AUTOINCREMENT" behave in the same way as columns declared as "[INTEGER PRIMARY KEY](lang_createtable.md#rowid)" when a NULL is inserted. The sqlite_sequence system table is neither created, nor respected if it already exists.

<span id="omit_autoinit"></span>

**SQLITE_OMIT_AUTOINIT**

> For backwards compatibility with older versions of SQLite that lack the [sqlite3_initialize()](c3ref/initialize.md) interface, the [sqlite3_initialize()](c3ref/initialize.md) interface is called automatically upon entry to certain key interfaces such as [sqlite3_open()](c3ref/open.md), [sqlite3_vfs_register()](c3ref/vfs_find.md), and [sqlite3_mprintf()](c3ref/mprintf.md). The overhead of invoking [sqlite3_initialize()](c3ref/initialize.md) automatically in this way may be omitted by building SQLite with the SQLITE_OMIT_AUTOINIT C-preprocessor macro. When built using SQLITE_OMIT_AUTOINIT, SQLite will not automatically initialize itself and the application is required to invoke [sqlite3_initialize()](c3ref/initialize.md) directly prior to beginning use of the SQLite library.

<span id="omit_automatic_index"></span>

**SQLITE_OMIT_AUTOMATIC_INDEX**

> This option is used to omit the [automatic indexing](optoverview.md#autoindex) functionality. See also: [SQLITE_DEFAULT_AUTOMATIC_INDEX](compile.md#default_automatic_index).

<span id="omit_autoreset"></span>

**SQLITE_OMIT_AUTORESET**

> By default, the [sqlite3_step()](c3ref/step.md) interface will automatically invoke [sqlite3_reset()](c3ref/reset.md) to reset the [prepared statement](c3ref/stmt.md) if necessary. This compile-time option changes that behavior so that [sqlite3_step()](c3ref/step.md) will return [SQLITE_MISUSE](rescode.md#misuse) if it is called again after returning anything other than [SQLITE_ROW](rescode.md#row), [SQLITE_BUSY](rescode.md#busy), or [SQLITE_LOCKED](rescode.md#locked) unless there was an intervening call to [sqlite3_reset()](c3ref/reset.md).
>
> In SQLite [version 3.6.23.1](releaselog/3_6_23_1.md) (2010-03-26) and earlier, [sqlite3_step()](c3ref/step.md) used to always return [SQLITE_MISUSE](rescode.md#misuse) if it was invoked again after returning anything other than [SQLITE_ROW](rescode.md#row) without an intervening call to [sqlite3_reset()](c3ref/reset.md). This caused problems on some poorly written smartphone applications which did not correctly handle the [SQLITE_LOCKED](rescode.md#locked) and [SQLITE_BUSY](rescode.md#busy) error returns. Rather than fix the many defective smartphone applications, the behavior of SQLite was changed in 3.6.23.2 to automatically reset the prepared statement. But that change caused issues in other improperly implemented applications that were actually looking for an [SQLITE_MISUSE](rescode.md#misuse) return to terminate their query loops. (When an application gets an SQLITE_MISUSE error code from SQLite, that means the application is misusing the SQLite interface and is thus incorrectly implemented.) The SQLITE_OMIT_AUTORESET interface was added to SQLite [version 3.7.5](releaselog/3_7_5.md) (2011-02-01) in an effort to get all of the (broken) applications to work again without having to actually fix the applications.

<span id="omit_autovacuum"></span>

**SQLITE_OMIT_AUTOVACUUM**

> If this option is defined, the library cannot create or write to databases that support [auto_vacuum](pragma.md#pragma_auto_vacuum). Executing a [PRAGMA auto_vacuum](pragma.md#pragma_auto_vacuum) statement is not an error (since unknown PRAGMAs are silently ignored), but does not return a value or modify the auto-vacuum flag in the database file. If a database that supports auto-vacuum is opened by a library compiled with this option, it is automatically opened in read-only mode.

<span id="omit_between_optimization"></span>

**SQLITE_OMIT_BETWEEN_OPTIMIZATION**

> This option disables the use of indices with WHERE clause terms that employ the BETWEEN operator.

<span id="omit_blob_literal"></span>

**SQLITE_OMIT_BLOB_LITERAL**

> When this option is defined, it is not possible to specify a blob in an SQL statement using the X'ABCD' syntax.

<span id="omit_btreecount"></span>

**SQLITE_OMIT_BTREECOUNT**

> This option is no longer used for anything. It is a no-op.

<span id="omit_builtin_test"></span>

**SQLITE_OMIT_BUILTIN_TEST**

> This compile-time option has been renamed to [SQLITE_UNTESTABLE](compile.md#untestable).

<span id="omit_case_sensitive_like_pragma"></span>

**SQLITE_OMIT_CASE_SENSITIVE_LIKE_PRAGMA**

> This compile-time option disables the [PRAGMA case_sensitive_like](pragma.md#pragma_case_sensitive_like) command.

<span id="omit_cast"></span>

**SQLITE_OMIT_CAST**

> This option causes SQLite to omit support for the CAST operator.

<span id="omit_check"></span>

**SQLITE_OMIT_CHECK**

> This option causes SQLite to omit support for CHECK constraints. The parser will still accept CHECK constraints in SQL statements, they will just not be enforced.

<span id="omit_compileoption_diags"></span>

**SQLITE_OMIT_COMPILEOPTION_DIAGS**

> This option is used to omit the compile-time option diagnostics available in SQLite, including the [sqlite3_compileoption_used()](c3ref/compileoption_get.md) and [sqlite3_compileoption_get()](c3ref/compileoption_get.md) C/C++ functions, the [sqlite_compileoption_used()](lang_corefunc.md#sqlite_compileoption_used) and [sqlite_compileoption_get()](lang_corefunc.md#sqlite_compileoption_get) SQL functions, and the [compile_options pragma](pragma.md#pragma_compile_options).

<span id="omit_complete"></span>

**SQLITE_OMIT_COMPLETE**

> This option causes the [sqlite3_complete()](c3ref/complete.md) and [sqlite3_complete16()](c3ref/complete.md) interfaces to be omitted.

<span id="omit_compound_select"></span>

**SQLITE_OMIT_COMPOUND_SELECT**

> This option is used to omit the compound [SELECT](lang_select.md) functionality. [SELECT](lang_select.md) statements that use the UNION, UNION ALL, INTERSECT or EXCEPT compound SELECT operators will cause a parse error.
>
> An [INSERT](lang_insert.md) statement with multiple values in the VALUES clause is implemented internally as a compound SELECT. Hence, this option also disables the ability to insert more than a single row using an INSERT INTO ... VALUES ... statement.

<span id="omit_cte"></span>

**SQLITE_OMIT_CTE**

> This option causes support for [common table expressions](lang_with.md) to be omitted.

<span id="omit_datetime_funcs"></span>

**SQLITE_OMIT_DATETIME_FUNCS**

> If this option is defined, SQLite's built-in date and time manipulation functions are omitted. Specifically, the SQL functions julianday(), date(), time(), datetime() and strftime() are not available. The default column values CURRENT_TIME, CURRENT_DATE and CURRENT_TIMESTAMP are still available.

<span id="omit_decltype"></span>

**SQLITE_OMIT_DECLTYPE**

> This option causes SQLite to omit support for the [sqlite3_column_decltype()](c3ref/column_decltype.md) and [sqlite3_column_decltype16()](c3ref/column_decltype.md) interfaces.

<span id="omit_deprecated"></span>

**SQLITE_OMIT_DEPRECATED**

> This option causes SQLite to omit support for interfaces marked as deprecated. This includes [sqlite3_aggregate_count()](c3ref/aggregate_count.md), [sqlite3_expired()](c3ref/aggregate_count.md), [sqlite3_transfer_bindings()](c3ref/aggregate_count.md), [sqlite3_global_recover()](c3ref/aggregate_count.md), [sqlite3_thread_cleanup()](c3ref/aggregate_count.md) and [sqlite3_memory_alarm()](c3ref/aggregate_count.md) interfaces and [PRAGMA](pragma.md#syntax) statements [PRAGMA count_changes](pragma.md#pragma_count_changes), [PRAGMA data_store_directory](pragma.md#pragma_data_store_directory), [PRAGMA default_cache_size](pragma.md#pragma_default_cache_size), [PRAGMA empty_result_callbacks](pragma.md#pragma_empty_result_callbacks), [PRAGMA full_column_names](pragma.md#pragma_full_column_names), [PRAGMA short_column_names](pragma.md#pragma_short_column_names), and [PRAGMA temp_store_directory](pragma.md#pragma_temp_store_directory).

<span id="omit_deserialize"></span>

**SQLITE_OMIT_DESERIALIZE**

> This option causes the [sqlite3_serialize()](c3ref/serialize.md) and [sqlite3_deserialize()](c3ref/deserialize.md) interfaces to be omitted from the build.

<span id="omit_diskio"></span>

**SQLITE_OMIT_DISKIO**

> This option omits all support for writing to the disk and forces databases to exist in memory only. This option has not been maintained and probably does not work with newer versions of SQLite.

<span id="omit_explain"></span>

**SQLITE_OMIT_EXPLAIN**

> Defining this option causes the [EXPLAIN](lang_explain.md) command to be omitted from the library. Attempting to execute an [EXPLAIN](lang_explain.md) statement will cause a parse error.

<span id="omit_flag_pragmas"></span>

**SQLITE_OMIT_FLAG_PRAGMAS**

> This option omits support for a subset of [PRAGMA](pragma.md#syntax) commands that query and set boolean properties.

<span id="omit_floating_point"></span>

**SQLITE_OMIT_FLOATING_POINT**

> This option is used to omit floating-point number support from the SQLite library. When specified, specifying a floating point number as a literal (i.e. "1.01") results in a parse error.
>
> In the future, this option may also disable other floating point functionality, for example the [sqlite3_result_double()](c3ref/result_blob.md), [sqlite3_bind_double()](c3ref/bind_blob.md), [sqlite3_value_double()](c3ref/value_blob.md) and [sqlite3_column_double()](c3ref/column_blob.md) API functions.

<span id="omit_foreign_key"></span>

**SQLITE_OMIT_FOREIGN_KEY**

> If this option is defined, then [foreign key constraint](foreignkeys.md) syntax is not recognized.

<span id="omit_generated_columns"></span>

**SQLITE_OMIT_GENERATED_COLUMNS**

> If this option is defined, then [generated column](gencol.md) syntax is not recognized.

<span id="omit_get_table"></span>

**SQLITE_OMIT_GET_TABLE**

> This option causes support for [sqlite3_get_table()](c3ref/free_table.md) and [sqlite3_free_table()](c3ref/free_table.md) to be omitted.

<span id="omit_hex_integer"></span>

**SQLITE_OMIT_HEX_INTEGER**

> This option omits support for [hexadecimal integer literals](lang_expr.md#hexint).

<span id="omit_incrblob"></span>

**SQLITE_OMIT_INCRBLOB**

> This option causes support for [incremental BLOB I/O](c3ref/blob.md) to be omitted.

<span id="omit_integrity_check"></span>

**SQLITE_OMIT_INTEGRITY_CHECK**

> This option omits support for the [integrity_check pragma](pragma.md#pragma_integrity_check).

<span id="omit_introspection_pragmas"></span>

**SQLITE_OMIT_INTROSPECTION_PRAGMAS**

> This option omits support for [PRAGMA function_list](pragma.md#pragma_function_list), [PRAGMA module_list](pragma.md#pragma_module_list), and [PRAGMA pragma_list](pragma.md#pragma_pragma_list).

<span id="omit_json"></span>

**SQLITE_OMIT_JSON**

> This option omits the [JSON SQL functions](json1.md) from the build.

<span id="omit_like_optimization"></span>

**SQLITE_OMIT_LIKE_OPTIMIZATION**

> This option disables the ability of SQLite to use indices to help resolve [LIKE](lang_expr.md#like) and [GLOB](lang_expr.md#glob) operators in a WHERE clause.

<span id="omit_load_extension"></span>

**SQLITE_OMIT_LOAD_EXTENSION**

> This option omits the entire extension loading mechanism from SQLite, including [sqlite3_enable_load_extension()](c3ref/enable_load_extension.md) and [sqlite3_load_extension()](c3ref/load_extension.md) interfaces.

<span id="omit_localtime"></span>

**SQLITE_OMIT_LOCALTIME**

> This option omits the "localtime" modifier from the date and time functions. This option is sometimes useful when trying to compile the date and time functions on a platform that does not support the concept of local time.

<span id="omit_lookaside"></span>

**SQLITE_OMIT_LOOKASIDE**

> This option omits the [lookaside memory allocator](malloc.md#lookaside).

<span id="omit_memorydb"></span>

**SQLITE_OMIT_MEMORYDB**

> When this is defined, the library does not respect the special database name ":memory:" (normally used to create an [in-memory database](inmemorydb.md)). If ":memory:" is passed to [sqlite3_open()](c3ref/open.md), [sqlite3_open16()](c3ref/open.md), or [sqlite3_open_v2()](c3ref/open.md), a file with this name will be opened or created.

<span id="omit_or_optimization"></span>

**SQLITE_OMIT_OR_OPTIMIZATION**

> This option disables the ability of SQLite to use an index together with terms of a WHERE clause connected by the OR operator.

<span id="omit_pager_pragmas"></span>

**SQLITE_OMIT_PAGER_PRAGMAS**

> Defining this option omits pragmas related to the pager subsystem from the build.

<span id="omit_pragma"></span>

**SQLITE_OMIT_PRAGMA**

> This option is used to omit the [PRAGMA](pragma.md#syntax) command from the library. Note that it is useful to define the macros that omit specific pragmas in addition to this, as they may also remove supporting code in other sub-systems. This macro removes the [PRAGMA](pragma.md#syntax) command only.

<span id="omit_progress_callback"></span>

**SQLITE_OMIT_PROGRESS_CALLBACK**

> When defined, this option omits the \[sqlite3_progress_handler() API and related logic.

<span id="omit_quickbalance"></span>

**SQLITE_OMIT_QUICKBALANCE**

> This option omits an alternative, faster B-Tree balancing routine. Using this option makes SQLite slightly smaller at the expense of making it run slightly slower.

<span id="omit_reindex"></span>

**SQLITE_OMIT_REINDEX**

> When this option is defined, the [REINDEX](lang_reindex.md) command is not included in the library. Executing a [REINDEX](lang_reindex.md) statement causes a parse error.

<span id="omit_schema_pragmas"></span>

**SQLITE_OMIT_SCHEMA_PRAGMAS**

> Defining this option omits pragmas for querying the database schema from the build.

<span id="omit_schema_version_pragmas"></span>

**SQLITE_OMIT_SCHEMA_VERSION_PRAGMAS**

> Defining this option omits pragmas for querying and modifying the database schema version and user version from the build. Specifically, the [schema_version](pragma.md#pragma_schema_version) and [user_version](pragma.md#pragma_user_version) PRAGMAs are omitted.

<span id="omit_shared_cache"></span>

**SQLITE_OMIT_SHARED_CACHE**

> This option builds SQLite without support for [shared cache mode](sharedcache.md). The [sqlite3_enable_shared_cache()](c3ref/enable_shared_cache.md) is omitted along with a fair amount of logic within the B-Tree subsystem associated with shared cache management.
>
> This compile-time option is recommended for most applications as it results in improved performance and reduced library footprint.

<span id="omit_seh"></span>

**SQLITE_OMIT_SEH**

> If defined, Structured Exception Handling (SEH) is disabled on Windows builds. SEH is a Windows-specific technique for catching exceptions raised while accessing a memory-mapped file. SEH is used to intercept errors that might occur while accessing the memory-mapped [shm file](walformat.md#shm) that are part of [WAL mode](wal.md) processing. If the operating system raised errors while SQLite is trying to access the shm file, this option causes those errors to be caught and dealt with by SQLite, rather than aborting the whole process.
>
> This has no effect except when compiling on Windows using MSVC.

<span id="omit_subquery"></span>

**SQLITE_OMIT_SUBQUERY**

> If defined, support for sub-selects and the IN() operator are omitted.

<span id="omit_tcl_variable"></span>

**SQLITE_OMIT_TCL_VARIABLE**

> If this macro is defined, then the special "\$" syntax used to automatically bind SQL variables to TCL variables is omitted.

<span id="omit_tempdb"></span>

**SQLITE_OMIT_TEMPDB**

> This option omits support for TEMP or TEMPORARY tables.

<span id="omit_trace"></span>

**SQLITE_OMIT_TRACE**

> This option omits support for the [sqlite3_profile()](c3ref/profile.md) and [sqlite3_trace()](c3ref/profile.md) interfaces and their associated logic.

<span id="omit_trigger"></span>

**SQLITE_OMIT_TRIGGER**

> Defining this option omits support for TRIGGER objects. Neither the [CREATE TRIGGER](lang_createtrigger.md) or [DROP TRIGGER](lang_droptrigger.md) commands are available in this case, and attempting to execute either will result in a parse error. This option also disables enforcement of [foreign key constraints](foreignkeys.md), since the code that implements triggers and which is omitted by this option is also used to implement [foreign key actions](foreignkeys.md#fk_actions).

<span id="omit_truncate_optimization"></span>

**SQLITE_OMIT_TRUNCATE_OPTIMIZATION**

> This option omits the [truncate optimization](lang_delete.md#truncateopt).

<span id="omit_utf16"></span>

**SQLITE_OMIT_UTF16**

> This macro is used to omit support for UTF16 text encoding. When this is defined all API functions that return or accept UTF16 encoded text are unavailable. These functions can be identified by the fact that they end with '16', for example [sqlite3_prepare16()](c3ref/prepare.md), [sqlite3_column_text16()](c3ref/column_blob.md) and [sqlite3_bind_text16()](c3ref/bind_blob.md).

<span id="omit_vacuum"></span>

**SQLITE_OMIT_VACUUM**

> When this option is defined, the [VACUUM](lang_vacuum.md) command is not included in the library. Executing a [VACUUM](lang_vacuum.md) statement causes a parse error.

<span id="omit_view"></span>

**SQLITE_OMIT_VIEW**

> Defining this option omits support for VIEW objects. Neither the [CREATE VIEW](lang_createview.md) nor the [DROP VIEW](lang_dropview.md) commands are available in this case, and attempting to execute either will result in a parse error.
>
> WARNING: If this macro is defined, it will not be possible to open a database for which the schema contains VIEW objects.

<span id="omit_virtualtable"></span>

**SQLITE_OMIT_VIRTUALTABLE**

> This option omits support for the [Virtual Table](c3ref/vtab.md) mechanism in SQLite.

<span id="omit_wal"></span>

**SQLITE_OMIT_WAL**

> This option omits the "[write-ahead log](wal.md)" (a.k.a. "[WAL](wal.md)") capability.

<span id="omit_windowfunc"></span>

**SQLITE_OMIT_WINDOWFUNC**

> This option omits [window functions](windowfunctions.md) from the build.

<span id="omit_wsd"></span>

**SQLITE_OMIT_WSD**

> This option builds a version of the SQLite library that contains no Writable Static Data (WSD). WSD is global variables and/or static variables. Some platforms do not support WSD, and this option is necessary in order for SQLite to work those platforms.
>
> Unlike other OMIT options which make the SQLite library smaller, this option actually increases the size of SQLite and makes it run a little slower. Only use this option if SQLite is being built for an embedded target that does not support WSD.

<span id="omit_xfer_opt"></span>

**SQLITE_OMIT_XFER_OPT**

> This option omits support for optimizations that help statements of the form "INSERT INTO ... SELECT ..." run faster.

<span id="untestable"></span>

**SQLITE_UNTESTABLE**

> A standard SQLite build includes a small amount of logic associated with [sqlite3_test_control()](c3ref/test_control.md) to exercise parts of the SQLite core that are otherwise difficult to validate. This compile-time option omits that extra testing logic. This compile-time option was called "SQLITE_OMIT_BUILTIN_TEST" prior to SQLite version 3.16.0 (2017-01-02). The name was changed to better describe the implications of using it.
>
> Setting this compile-time option prevents SQLite from being fully testable. Branch test coverage drops from 100% down to about 95%.
>
> SQLite developers follow the NASA principle of "fly what you test and test what you fly". This principle is violated if this option is enabled for delivery but disabled for testing. But if this option is enabled during testing, not all branches are reachable. Therefore, the use of this compile-time option is discouraged.

<span id="zero_malloc"></span>

**SQLITE_ZERO_MALLOC**

> This option omits both the [default memory allocator](malloc.md#defaultalloc) and the [debugging memory allocator](malloc.md#memdebug) from the build and substitutes a stub memory allocator that always fails. SQLite will not run with this stub memory allocator since it will be unable to allocate memory. But this stub can be replaced at start-time using [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_MALLOC](c3ref/c_config_covering_index_scan.md#sqliteconfigmalloc),...) or [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_HEAP](c3ref/c_config_covering_index_scan.md#sqliteconfigheap),...). So the net effect of this compile-time option is that it allows SQLite to be compiled and linked against a system library that does not support malloc(), free(), and/or realloc().

<span id="debugoptions"></span>

# 10.  Analysis and Debugging Options

<span id="debug"></span>

**SQLITE_DEBUG**

> The SQLite source code contains literally thousands of assert() statements used to verify internal assumptions and subroutine preconditions and postconditions. These assert() statements are normally turned off (they generate no code) since turning them on makes SQLite run approximately three times slower. But for testing and analysis, it is useful to turn the assert() statements on. The SQLITE_DEBUG compile-time option does this.
>
> SQLITE_DEBUG also enables some other debugging features, such as special [PRAGMA](pragma.md#syntax) statements that turn on tracing and listing features used for troubleshooting and analysis of the [VDBE](opcode.md) and code generator.

<span id="memdebug"></span>

**SQLITE_MEMDEBUG**

> The SQLITE_MEMDEBUG option causes an instrumented [debugging memory allocator](malloc.md#memdebug) to be used as the default memory allocator within SQLite. The instrumented memory allocator checks for misuse of dynamically allocated memory. Examples of misuse include using memory after it is freed, writing off the ends of a memory allocation, freeing memory not previously obtained from the memory allocator, or failing to initialize newly allocated memory.

<span id="win32options"></span>

# 11.  Windows-Specific Options

<span id="win32_heap_create"></span>

**SQLITE_WIN32_HEAP_CREATE**

> This option forces the Win32 native memory allocator, when enabled, to create a private heap to hold all memory allocations.

<span id="win32_malloc_validate"></span>

**SQLITE_WIN32_MALLOC_VALIDATE**

> This option forces the Win32 native memory allocator, when enabled, to make strategic calls into the HeapValidate() function if assert() is also enabled.

<span id="linkage"></span>

# 12. Compiler Linkage and Calling Convention Control

The following macros specify interface details for certain kinds of SQLite builds. The Makefiles will normally handle setting these macros automatically. Application developers should not need to worry with these macros. The following documentation about these macros is included for completeness.

<span id="api"></span>

**SQLITE_API**

> This macro identifies an externally visible interface for SQLite. This macro is sometimes set to "extern". But the definition is compiler-specific.

<span id="apicall"></span>

**SQLITE_APICALL**

> This macro identifies the calling convention used by public interface routines in SQLite which accept a fixed number of arguments. This macro is normally defined to be nothing, though on Windows builds it can sometimes be set to "\_\_cdecl" or "\_\_stdcall". The "\_\_cdecl" setting is the default, but "\_\_stdcall" is used when SQLite is intended to be compiled as a Windows system library.
>
> A single function declaration should contain no more than one of the following: [SQLITE_APICALL](compile.md#apicall), [SQLITE_CDECL](compile.md#cdecl), or [SQLITE_SYSAPI](compile.md#sysapi).

<span id="callback"></span>

**SQLITE_CALLBACK**

> This macro specifies the calling convention used with callback pointers in SQLite. This macro is normally defined to be nothing, though on Windows builds it can sometimes be set to "\_\_cdecl" or "\_\_stdcall". The "\_\_cdecl" setting is the default, but "\_\_stdcall" is used when SQLite is intended to be compiled as a Windows system library.

<span id="cdecl"></span>

**SQLITE_CDECL**

> This macro specifies the calling convention used by varargs interface routines in SQLite. This macro is normally defined to be nothing, though on Windows builds it can sometimes be set to "\_\_cdecl". This macro is used on varargs routines and so cannot be set to "\_\_stdcall" since the \_\_stdcall calling convention does not support varargs functions.
>
> A single function declaration should contain no more than one of the following: [SQLITE_APICALL](compile.md#apicall), [SQLITE_CDECL](compile.md#cdecl), or [SQLITE_SYSAPI](compile.md#sysapi).

<span id="extern"></span>

**SQLITE_EXTERN**

> This macro specifies linkage for public interface variables in SQLite. It should normally be allowed to default to "extern".

<span id="stdcall"></span>

**SQLITE_STDCALL**

> This macro is no longer used and is now deprecated.

<span id="sysapi"></span>

**SQLITE_SYSAPI**

> This macro identifies the calling convention used by operating system interfaces for the target platform for an SQLite build. This macro is normally defined to be nothing, though on Windows builds it can sometimes be set to "\_\_stdcall".
>
> A single function declaration should contain no more than one of the following: [SQLITE_APICALL](compile.md#apicall), [SQLITE_CDECL](compile.md#cdecl), or [SQLITE_SYSAPI](compile.md#sysapi).

<span id="tclapi"></span>

**SQLITE_TCLAPI**

> This macro specifies the calling convention used by the [TCL](http://www.tcl.tk) library interface routines. This macro is not used by the SQLite core, but only by the [TCL Interface](tclsqlite.md) and [TCL test suite](testing.md#tcl). This macro is normally defined to be nothing, though on Windows builds it can sometimes be set to "\_\_cdecl". This macro is used on TCL library interface routines which are always compiled as \_\_cdecl, even on platforms that prefer to use \_\_stdcall, so this macro should not be set to \_\_stdcall unless the platform has a custom TCL library build that supports \_\_stdcall.
>
> This macro may not be used in combination with any of [SQLITE_APICALL](compile.md#apicall), [SQLITE_CALLBACK](compile.md#callback), [SQLITE_CDECL](compile.md#cdecl) or [SQLITE_SYSAPI](compile.md#sysapi).
