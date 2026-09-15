---
title: Prepare Flags
source_url: https://www.sqlite.org/c3ref/c_prepare_dont_log.html
source_path: c3ref/c_prepare_dont_log.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 630
---

> \
> \#define SQLITE_PREPARE_PERSISTENT              0x01\
> \#define SQLITE_PREPARE_NORMALIZE               0x02\
> \#define SQLITE_PREPARE_NO_VTAB                 0x04\
> \#define SQLITE_PREPARE_DONT_LOG                0x10\
> \#define SQLITE_PREPARE_FROM_DDL                0x20\

These constants define various flags that can be passed into the "prepFlags" parameter of the [sqlite3_prepare_v3()](../c3ref/prepare.md) and [sqlite3_prepare16_v3()](../c3ref/prepare.md) interfaces.

New flags may be added in future releases of SQLite.

SQLITE_PREPARE_PERSISTENT  
The SQLITE_PREPARE_PERSISTENT flag is a hint to the query planner that the prepared statement will be retained for a long time and probably reused many times. Without this flag, [sqlite3_prepare_v3()](../c3ref/prepare.md) and [sqlite3_prepare16_v3()](../c3ref/prepare.md) assume that the prepared statement will be used just once or at most a few times and then destroyed using [sqlite3_finalize()](../c3ref/finalize.md) relatively soon. The current implementation acts on this hint by avoiding the use of [lookaside memory](../malloc.md#lookaside) so as not to deplete the limited store of lookaside memory. Future versions of SQLite may act on this hint differently.

<span id="sqlitepreparenormalize"></span>

SQLITE_PREPARE_NORMALIZE  
The SQLITE_PREPARE_NORMALIZE flag is a no-op. This flag used to be required for any prepared statement that wanted to use the [sqlite3_normalized_sql()](../c3ref/expanded_sql.md) interface. However, the [sqlite3_normalized_sql()](../c3ref/expanded_sql.md) interface is now available to all prepared statements, regardless of whether or not they use this flag.

<span id="sqlitepreparenovtab"></span>

SQLITE_PREPARE_NO_VTAB  
The SQLITE_PREPARE_NO_VTAB flag causes the SQL compiler to return an error (error code SQLITE_ERROR) if the statement uses any virtual tables.

<span id="sqlitepreparedontlog"></span>

SQLITE_PREPARE_DONT_LOG  
The SQLITE_PREPARE_DONT_LOG flag prevents SQL compiler errors from being sent to the error log defined by [SQLITE_CONFIG_LOG](../c3ref/c_config_covering_index_scan.md#sqliteconfiglog). This can be used, for example, to do test compiles to see if some SQL syntax is well-formed, without generating messages on the global error log when it is not. If the test compile fails, the sqlite3_prepare_v3() call returns the same error indications with or without this flag; it just omits the call to [sqlite3_log()](../c3ref/log.md) that logs the error.

<span id="sqlitepreparefromddl"></span>

SQLITE_PREPARE_FROM_DDL  
The SQLITE_PREPARE_FROM_DDL flag causes the SQL compiler to enforce security constraints that would otherwise only be enforced when parsing the database schema. In other words, the SQLITE_PREPARE_FROM_DDL flag causes the SQL compiler to treat the SQL statement being prepared as if it had come from an attacker. When SQLITE_PREPARE_FROM_DDL is used and [SQLITE_DBCONFIG_TRUSTED_SCHEMA](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigtrustedschema) is off, SQL functions may only be called if they are tagged with [SQLITE_INNOCUOUS](../c3ref/c_deterministic.md#sqliteinnocuous) and virtual tables may only be used if they are tagged with [SQLITE_VTAB_INNOCUOUS](../c3ref/c_vtab_constraint_support.md#sqlitevtabinnocuous). Best practice is to use the SQLITE_PREPARE_FROM_DDL option when preparing any SQL that is derived from parts of the database schema. In particular, virtual table implementations that run SQL statements that are derived from arguments to their CREATE VIRTUAL TABLE statement should always use [sqlite3_prepare_v3()](../c3ref/prepare.md) and set the SQLITE_PREPARE_FROM_DDL flag to prevent bypass of the [SQLITE_DBCONFIG_TRUSTED_SCHEMA](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigtrustedschema) security checks.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
