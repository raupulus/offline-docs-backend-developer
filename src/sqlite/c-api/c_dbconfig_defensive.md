---
title: Database Connection Configuration Options
source_url: https://www.sqlite.org/c3ref/c_dbconfig_defensive.html
source_path: c3ref/c_dbconfig_defensive.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 490
---

> \
> \#define SQLITE_DBCONFIG_MAINDBNAME            1000 /\* const char\* \*/\
> \#define SQLITE_DBCONFIG_LOOKASIDE             1001 /\* void\* int int \*/\
> \#define SQLITE_DBCONFIG_ENABLE_FKEY           1002 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_ENABLE_TRIGGER        1003 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER 1004 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION 1005 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE      1006 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_ENABLE_QPSG           1007 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_TRIGGER_EQP           1008 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_RESET_DATABASE        1009 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_DEFENSIVE             1010 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_WRITABLE_SCHEMA       1011 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_LEGACY_ALTER_TABLE    1012 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_DQS_DML               1013 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_DQS_DDL               1014 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_ENABLE_VIEW           1015 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_LEGACY_FILE_FORMAT    1016 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_TRUSTED_SCHEMA        1017 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_STMT_SCANSTATUS       1018 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_REVERSE_SCANORDER     1019 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_ENABLE_ATTACH_CREATE  1020 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_ENABLE_ATTACH_WRITE   1021 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_ENABLE_COMMENTS       1022 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_FP_DIGITS             1023 /\* int int\* \*/\
> \#define SQLITE_DBCONFIG_MAX                   1023 /\* Largest DBCONFIG \*/\

These constants are the available integer configuration options that can be passed as the second parameter to the [sqlite3_db_config()](../c3ref/db_config.md) interface.

The [sqlite3_db_config()](../c3ref/db_config.md) interface is a var-args function. It takes a variable number of parameters, though always at least two. The number of parameters passed into sqlite3_db_config() depends on which of these constants is given as the second parameter. This documentation page refers to parameters beyond the second as "arguments". Thus, when this page says "the N-th argument" it means "the N-th parameter past the configuration option" or "the (N+2)-th parameter to sqlite3_db_config()".

New configuration options may be added in future releases of SQLite. Existing configuration options might be discontinued. Applications should check the return code from [sqlite3_db_config()](../c3ref/db_config.md) to make sure that the call worked. The [sqlite3_db_config()](../c3ref/db_config.md) interface will return a non-zero [error code](../rescode.md) if a discontinued or unsupported configuration option is invoked.

SQLITE_DBCONFIG_LOOKASIDE  
The SQLITE_DBCONFIG_LOOKASIDE option is used to adjust the configuration of the [lookaside memory allocator](../malloc.md#lookaside) within a database connection. The arguments to the SQLITE_DBCONFIG_LOOKASIDE option are *not* in the [usual format](../c3ref/c_dbconfig_defensive.md#dbconfigarguments). The SQLITE_DBCONFIG_LOOKASIDE option takes three arguments, not two, so that a call to [sqlite3_db_config()](../c3ref/db_config.md) that uses SQLITE_DBCONFIG_LOOKASIDE should have a total of five parameters.

1.  The first argument ("buf") is a pointer to a memory buffer to use for lookaside memory. The first argument may be NULL in which case SQLite will allocate the lookaside buffer itself using [sqlite3_malloc()](../c3ref/free.md).

2.  The second argument ("sz") is the size of each lookaside buffer slot. Lookaside is disabled if "sz" is less than 8. The "sz" argument should be a multiple of 8 less than 65536. If "sz" does not meet this constraint, it is reduced in size until it does.

3.  The third argument ("cnt") is the number of slots. Lookaside is disabled if "cnt"is less than 1. that the product of "sz" and "cnt" does not exceed 2,147,418,112. The "cnt" parameter is usually chosen so that the product of "sz" and "cnt" is less than 1,000,000.

If the "buf" argument is not NULL, then it must point to a memory buffer with a size that is greater than or equal to the product of "sz" and "cnt". The buffer must be aligned to an 8-byte boundary. The lookaside memory configuration for a database connection can only be changed when that connection is not currently using lookaside memory, or in other words when the value returned by [SQLITE_DBSTATUS_LOOKASIDE_USED](../c3ref/c_dbstatus_options.md#sqlitedbstatuslookasideused) is zero. Any attempt to change the lookaside memory configuration when lookaside memory is in use leaves the configuration unchanged and returns [SQLITE_BUSY](../rescode.md#busy). If the "buf" argument is NULL and an attempt to allocate memory based on "sz" and "cnt" fails, then lookaside is silently disabled.

The [SQLITE_CONFIG_LOOKASIDE](../c3ref/c_config_covering_index_scan.md#sqliteconfiglookaside) configuration option can be used to set the default lookaside configuration at initialization. The [-DSQLITE_DEFAULT_LOOKASIDE](../compile.md#default_lookaside) option can be used to set the default lookaside configuration at compile-time. Typical values for lookaside are 1200 for "sz" and 40 to 100 for "cnt".

SQLITE_DBCONFIG_ENABLE_FKEY  
This option is used to enable or disable the enforcement of [foreign key constraints](../foreignkeys.md). This is the same setting that is enabled or disabled by the [PRAGMA foreign_keys](../pragma.md#pragma_foreign_keys) statement. The first argument is an integer which is 0 to disable FK enforcement, positive to enable FK enforcement or negative to leave FK enforcement unchanged. The second parameter is a pointer to an integer into which is written 0 or 1 to indicate whether FK enforcement is off or on following this call. The second parameter may be a NULL pointer, in which case the FK enforcement setting is not reported back.

SQLITE_DBCONFIG_ENABLE_TRIGGER  
This option is used to enable or disable [triggers](../lang_createtrigger.md). There should be two additional arguments. The first argument is an integer which is 0 to disable triggers, positive to enable triggers or negative to leave the setting unchanged. The second parameter is a pointer to an integer into which is written 0 or 1 to indicate whether triggers are disabled or enabled following this call. The second parameter may be a NULL pointer, in which case the trigger setting is not reported back.

Originally this option disabled all triggers. However, since SQLite version 3.35.0, TEMP triggers are still allowed even if this option is off. So, in other words, this option now only disables triggers in the main database schema or in the schemas of [ATTACH](../lang_attach.md)-ed databases.

SQLITE_DBCONFIG_ENABLE_VIEW  
This option is used to enable or disable [views](../lang_createview.md). There must be two additional arguments. The first argument is an integer which is 0 to disable views, positive to enable views or negative to leave the setting unchanged. The second parameter is a pointer to an integer into which is written 0 or 1 to indicate whether views are disabled or enabled following this call. The second parameter may be a NULL pointer, in which case the view setting is not reported back.

Originally this option disabled all views. However, since SQLite version 3.35.0, TEMP views are still allowed even if this option is off. So, in other words, this option now only disables views in the main database schema or in the schemas of ATTACH-ed databases.

SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER  
This option is used to enable or disable using the [fts3_tokenizer()](../fts3.md#f3tknzr) function - part of the [FTS3](../fts3.md) full-text search engine extension - without using bound parameters as the parameters. Doing so is disabled by default. There must be two additional arguments. The first argument is an integer. If it is passed 0, then using fts3_tokenizer() without bound parameters is disabled. If it is passed a positive value, then calling fts3_tokenizer without bound parameters is enabled. If it is passed a negative value, this setting is not modified - this can be used to query for the current setting. The second parameter is a pointer to an integer into which is written 0 or 1 to indicate the current value of this setting (after it is modified, if applicable). The second parameter may be a NULL pointer, in which case the value of the setting is not reported back. Refer to [FTS3](../fts3.md) documentation for further details.

SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION  
This option is used to enable or disable the [sqlite3_load_extension()](../c3ref/load_extension.md) interface independently of the [load_extension()](../lang_corefunc.md#load_extension) SQL function. The [sqlite3_enable_load_extension()](../c3ref/enable_load_extension.md) API enables or disables both the C-API [sqlite3_load_extension()](../c3ref/load_extension.md) and the SQL function [load_extension()](../lang_corefunc.md#load_extension). There must be two additional arguments. When the first argument to this interface is 1, then only the C-API is enabled and the SQL function remains disabled. If the first argument to this interface is 0, then both the C-API and the SQL function are disabled. If the first argument is -1, then no changes are made to the state of either the C-API or the SQL function. The second parameter is a pointer to an integer into which is written 0 or 1 to indicate whether [sqlite3_load_extension()](../c3ref/load_extension.md) interface is disabled or enabled following this call. The second parameter may be a NULL pointer, in which case the new setting is not reported back.

SQLITE_DBCONFIG_MAINDBNAME  
This option is used to change the name of the "main" database schema. This option does not follow the [usual SQLITE_DBCONFIG argument format](../c3ref/c_dbconfig_defensive.md#dbconfigarguments). This option takes exactly one additional argument so that the [sqlite3_db_config()](../c3ref/db_config.md) call has a total of three parameters. The extra argument must be a pointer to a constant UTF8 string which will become the new schema name in place of "main". SQLite does not make a copy of the new main schema name string, so the application must ensure that the argument passed into SQLITE_DBCONFIG MAINDBNAME is unchanged until after the database connection closes.

SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE  
Usually, when a database in [WAL mode](../wal.md) is closed or detached from a database handle, SQLite checks if if there are other connections to the same database, and if there are no other database connection (if the connection being closed is the last open connection to the database), then SQLite performs a [checkpoint](../wal.md#ckpt) before closing the connection and deletes the WAL file. The SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE option can be used to override that behavior. The first argument passed to this operation (the third parameter to [sqlite3_db_config()](../c3ref/db_config.md)) is an integer which is positive to disable checkpoints-on-close, or zero (the default) to enable them, and negative to leave the setting unchanged. The second argument (the fourth parameter) is a pointer to an integer into which is written 0 or 1 to indicate whether checkpoints-on-close have been disabled - 0 if they are not disabled, 1 if they are.

SQLITE_DBCONFIG_ENABLE_QPSG  
The SQLITE_DBCONFIG_ENABLE_QPSG option activates or deactivates the [query planner stability guarantee](../queryplanner-ng.md#qpstab) (QPSG). When the QPSG is active, a single SQL query statement will always use the same algorithm regardless of values of [bound parameters](../lang_expr.md#varparam). The QPSG disables some query optimizations that look at the values of bound parameters, which can make some queries slower. But the QPSG has the advantage of more predictable behavior. With the QPSG active, SQLite will always use the same query plan in the field as was used during testing in the lab. The first argument to this setting is an integer which is 0 to disable the QPSG, positive to enable QPSG, or negative to leave the setting unchanged. The second parameter is a pointer to an integer into which is written 0 or 1 to indicate whether the QPSG is disabled or enabled following this call.

SQLITE_DBCONFIG_TRIGGER_EQP  
By default, the output of EXPLAIN QUERY PLAN commands does not include output for any operations performed by trigger programs. This option is used to set or clear (the default) a flag that governs this behavior. The first parameter passed to this operation is an integer - positive to enable output for trigger programs, or zero to disable it, or negative to leave the setting unchanged. The second parameter is a pointer to an integer into which is written 0 or 1 to indicate whether output-for-triggers has been disabled - 0 if it is not disabled, 1 if it is.

SQLITE_DBCONFIG_RESET_DATABASE  
Set the SQLITE_DBCONFIG_RESET_DATABASE flag and then run [VACUUM](../lang_vacuum.md) in order to reset a database back to an empty database with no schema and no content. The following process works even for a badly corrupted database file:

1.  If the database connection is newly opened, make sure it has read the database schema by preparing then discarding some query against the database, or calling sqlite3_table_column_metadata(), ignoring any errors. This step is only necessary if the application desires to keep the database in WAL mode after the reset if it was in WAL mode before the reset.
2.  sqlite3_db_config(db, SQLITE_DBCONFIG_RESET_DATABASE, 1, 0);
3.  [sqlite3_exec](../c3ref/exec.md)(db, "[VACUUM](../lang_vacuum.md)", 0, 0, 0);
4.  sqlite3_db_config(db, SQLITE_DBCONFIG_RESET_DATABASE, 0, 0);

Because resetting a database is destructive and irreversible, the process requires the use of this obscure API and multiple steps to help ensure that it does not happen by accident. Because this feature must be capable of resetting corrupt databases, and shutting down virtual tables may require access to that corrupt storage, the library must abandon any installed virtual tables without calling their xDestroy() methods.

<span id="sqlitedbconfigdefensive"></span>

SQLITE_DBCONFIG_DEFENSIVE  
The SQLITE_DBCONFIG_DEFENSIVE option activates or deactivates the "defensive" flag for a database connection. When the defensive flag is enabled, language features that allow ordinary SQL to deliberately corrupt the database file are disabled. The disabled features include but are not limited to the following:

- The [PRAGMA writable_schema=ON](../pragma.md#pragma_writable_schema) statement.
- The [PRAGMA journal_mode=OFF](../pragma.md#pragma_journal_mode) statement.
- The [PRAGMA schema_version=N](../pragma.md#pragma_schema_version) statement.
- Writes to the [sqlite_dbpage](../dbpage.md) virtual table.
- Direct writes to [shadow tables](../vtab.md#xshadowname).

SQLITE_DBCONFIG_WRITABLE_SCHEMA  
The SQLITE_DBCONFIG_WRITABLE_SCHEMA option activates or deactivates the "writable_schema" flag. This has the same effect and is logically equivalent to setting [PRAGMA writable_schema=ON](../pragma.md#pragma_writable_schema) or [PRAGMA writable_schema=OFF](../pragma.md#pragma_writable_schema). The first argument to this setting is an integer which is 0 to disable the writable_schema, positive to enable writable_schema, or negative to leave the setting unchanged. The second parameter is a pointer to an integer into which is written 0 or 1 to indicate whether the writable_schema is enabled or disabled following this call.

SQLITE_DBCONFIG_LEGACY_ALTER_TABLE  
The SQLITE_DBCONFIG_LEGACY_ALTER_TABLE option activates or deactivates the legacy behavior of the [ALTER TABLE RENAME](../lang_altertable.md#altertabrename) command such that it behaves as it did prior to [version 3.24.0](../releaselog/3_24_0.md) (2018-06-04). See the "Compatibility Notice" on the [ALTER TABLE RENAME documentation](../lang_altertable.md#altertabrename) for additional information. This feature can also be turned on and off using the [PRAGMA legacy_alter_table](../pragma.md#pragma_legacy_alter_table) statement.

SQLITE_DBCONFIG_DQS_DML  
The SQLITE_DBCONFIG_DQS_DML option activates or deactivates the legacy [double-quoted string literal](../quirks.md#dblquote) misfeature for DML statements only, that is DELETE, INSERT, SELECT, and UPDATE statements. The default value of this setting is determined by the [-DSQLITE_DQS](../compile.md#dqs) compile-time option.

SQLITE_DBCONFIG_DQS_DDL  
The SQLITE_DBCONFIG_DQS option activates or deactivates the legacy [double-quoted string literal](../quirks.md#dblquote) misfeature for DDL statements, such as CREATE TABLE and CREATE INDEX. The default value of this setting is determined by the [-DSQLITE_DQS](../compile.md#dqs) compile-time option.

SQLITE_DBCONFIG_TRUSTED_SCHEMA  
The SQLITE_DBCONFIG_TRUSTED_SCHEMA option tells SQLite to assume that database schemas are untainted by malicious content. When the SQLITE_DBCONFIG_TRUSTED_SCHEMA option is disabled, SQLite takes additional defensive steps to protect the application from harm including:

- Prohibit the use of SQL functions inside triggers, views, CHECK constraints, DEFAULT clauses, expression indexes, partial indexes, or generated columns unless those functions are tagged with [SQLITE_INNOCUOUS](../c3ref/c_deterministic.md#sqliteinnocuous).
- Prohibit the use of virtual tables inside of triggers or views unless those virtual tables are tagged with [SQLITE_VTAB_INNOCUOUS](../c3ref/c_vtab_constraint_support.md#sqlitevtabinnocuous).

This setting defaults to "on" for legacy compatibility, however all applications are advised to turn it off if possible. This setting can also be controlled using the [PRAGMA trusted_schema](../pragma.md#pragma_trusted_schema) statement.

SQLITE_DBCONFIG_LEGACY_FILE_FORMAT  
The SQLITE_DBCONFIG_LEGACY_FILE_FORMAT option activates or deactivates the legacy file format flag. When activated, this flag causes all newly created database files to have a schema format version number (the 4-byte integer found at offset 44 into the database header) of 1. This in turn means that the resulting database file will be readable and writable by any SQLite version back to 3.0.0 (2004-06-18). Without this setting, newly created databases are generally not understandable by SQLite versions prior to 3.3.0 (2006-01-11). As these words are written, there is now scarcely any need to generate database files that are compatible all the way back to version 3.0.0, and so this setting is of little practical use, but is provided so that SQLite can continue to claim the ability to generate new database files that are compatible with version 3.0.0.

Note that when the SQLITE_DBCONFIG_LEGACY_FILE_FORMAT setting is on, the [VACUUM](../lang_vacuum.md) command will fail with an obscure error when attempting to process a table with generated columns and a descending index. This is not considered a bug since SQLite versions 3.3.0 and earlier do not support either generated columns or descending indexes.

SQLITE_DBCONFIG_STMT_SCANSTATUS  
The SQLITE_DBCONFIG_STMT_SCANSTATUS option is only useful in [SQLITE_ENABLE_STMT_SCANSTATUS](../compile.md#enable_stmt_scanstatus) builds. In this case, it sets or clears a flag that enables collection of run-time performance statistics used by [sqlite3_stmt_scanstatus_v2()](../c3ref/stmt_scanstatus.md) and the [nexec and ncycle](../bytecodevtab.md#nexec) columns of the [bytecode virtual table](../bytecodevtab.md). For statistics to be collected, the flag must be set on the database handle both when the SQL statement is [prepared](../c3ref/prepare.md) and when it is [stepped](../c3ref/step.md). The flag is set (collection of statistics is enabled) by default.

This option takes two arguments: an integer and a pointer to an integer. The first argument is 1, 0, or -1 to enable, disable, or leave unchanged the statement scanstatus option. If the second argument is not NULL, then the value of the statement scanstatus setting after processing the first argument is written into the integer that the second argument points to.

SQLITE_DBCONFIG_REVERSE_SCANORDER  
The SQLITE_DBCONFIG_REVERSE_SCANORDER option changes the default order in which tables and indexes are scanned so that the scans start at the end and work toward the beginning rather than starting at the beginning and working toward the end. Setting SQLITE_DBCONFIG_REVERSE_SCANORDER is the same as setting [PRAGMA reverse_unordered_selects](../pragma.md#pragma_reverse_unordered_selects).

This option takes two arguments which are an integer and a pointer to an integer. The first argument is 1, 0, or -1 to enable, disable, or leave unchanged the reverse scan order flag, respectively. If the second argument is not NULL, then 0 or 1 is written into the integer that the second argument points to depending on if the reverse scan order flag is set after processing the first argument.

SQLITE_DBCONFIG_ENABLE_ATTACH_CREATE  
The SQLITE_DBCONFIG_ENABLE_ATTACH_CREATE option enables or disables the ability of the [ATTACH DATABASE](../lang_attach.md) SQL command to create a new database file if the database filed named in the ATTACH command does not already exist. This ability of ATTACH to create a new database is enabled by default. Applications can disable or reenable the ability for ATTACH to create new database files using this DBCONFIG option.

This option takes two arguments which are an integer and a pointer to an integer. The first argument is 1, 0, or -1 to enable, disable, or leave unchanged the attach-create flag, respectively. If the second argument is not NULL, then 0 or 1 is written into the integer that the second argument points to depending on if the attach-create flag is set after processing the first argument.

SQLITE_DBCONFIG_ENABLE_ATTACH_WRITE  
The SQLITE_DBCONFIG_ENABLE_ATTACH_WRITE option enables or disables the ability of the [ATTACH DATABASE](../lang_attach.md) SQL command to open a database for writing. This capability is enabled by default. Applications can disable or reenable this capability using the current DBCONFIG option. If this capability is disabled, the [ATTACH](../lang_attach.md) command will still work, but the database will be opened read-only. If this option is disabled, then the ability to create a new database using [ATTACH](../lang_attach.md) is also disabled, regardless of the value of the [SQLITE_DBCONFIG_ENABLE_ATTACH_CREATE](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableattachcreate) option.

This option takes two arguments which are an integer and a pointer to an integer. The first argument is 1, 0, or -1 to enable, disable, or leave unchanged the ability to ATTACH another database for writing, respectively. If the second argument is not NULL, then 0 or 1 is written into the integer to which the second argument points, depending on whether the ability to ATTACH a read/write database is enabled or disabled after processing the first argument.

SQLITE_DBCONFIG_ENABLE_COMMENTS  
The SQLITE_DBCONFIG_ENABLE_COMMENTS option enables or disables the ability to include comments in SQL text. Comments are enabled by default. An application can disable or reenable comments in SQL text using this DBCONFIG option.

This option takes two arguments which are an integer and a pointer to an integer. The first argument is 1, 0, or -1 to enable, disable, or leave unchanged the ability to use comments in SQL text, respectively. If the second argument is not NULL, then 0 or 1 is written into the integer that the second argument points to depending on if comments are allowed in SQL text after processing the first argument.

SQLITE_DBCONFIG_FP_DIGITS  
The SQLITE_DBCONFIG_FP_DIGITS setting is a small integer that determines the number of significant digits that SQLite will attempt to preserve when converting floating point numbers (IEEE 754 "doubles") into text. The default value 17, as of SQLite version 3.52.0. The value was 15 in all prior versions.

This option takes two arguments which are an integer and a pointer to an integer. The first argument is a small integer, between 3 and 23, or zero. The FP_DIGITS setting is changed to that small integer, or left unaltered if the first argument is zero or out of range. The second argument is a pointer to an integer. If the pointer is not NULL, then the value of the FP_DIGITS setting, after possibly being modified by the first arguments, is written into the integer to which the second argument points.

<span id="dbconfigarguments"></span>

### Arguments To SQLITE_DBCONFIG Options

Most of the SQLITE_DBCONFIG options take two arguments, so that the overall call to [sqlite3_db_config()](../c3ref/db_config.md) has a total of four parameters. The first argument (the third parameter to sqlite3_db_config()) is an integer. The second argument is a pointer to an integer. If the first argument is 1, then the option becomes enabled. If the first integer argument is 0, then the option is disabled. If the first argument is -1, then the option setting is unchanged. The second argument, the pointer to an integer, may be NULL. If the second argument is not NULL, then a value of 0 or 1 is written into the integer to which the second argument points, depending on whether the setting is disabled or enabled after applying any changes specified by the first argument.

While most SQLITE_DBCONFIG options use the argument format described in the previous paragraph, the [SQLITE_DBCONFIG_MAINDBNAME](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigmaindbname), [SQLITE_DBCONFIG_LOOKASIDE](../c3ref/c_dbconfig_defensive.md#sqlitedbconfiglookaside), and [SQLITE_DBCONFIG_FP_DIGITS](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigfpdigits) options are different. See the documentation of those exceptional options for details.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
