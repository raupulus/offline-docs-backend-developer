---
title: Dynamically Typed Value Object
source_url: https://www.sqlite.org/c3ref/value.html
source_path: c3ref/value.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2170
---

> \
> typedef struct sqlite3_value sqlite3_value;\

SQLite uses the sqlite3_value object to represent all values that can be stored in a database table. SQLite uses dynamic typing for the values it stores. Values stored in sqlite3_value objects can be integers, floating point values, strings, BLOBs, or NULL.

An sqlite3_value object may be either "protected" or "unprotected". Some interfaces require a protected sqlite3_value. Other interfaces will accept either a protected or an unprotected sqlite3_value. Every interface that accepts sqlite3_value arguments specifies whether or not it requires a protected sqlite3_value. The [sqlite3_value_dup()](../c3ref/value_dup.md) interface can be used to construct a new protected sqlite3_value from an unprotected sqlite3_value.

The terms "protected" and "unprotected" refer to whether or not a mutex is held. An internal mutex is held for a protected sqlite3_value object but no mutex is held for an unprotected sqlite3_value object. If SQLite is compiled to be single-threaded (with [SQLITE_THREADSAFE=0](../compile.md#threadsafe) and with [sqlite3_threadsafe()](../c3ref/threadsafe.md) returning 0) or if SQLite is run in one of reduced mutex modes [SQLITE_CONFIG_SINGLETHREAD](../c3ref/c_config_covering_index_scan.md#sqliteconfigsinglethread) or [SQLITE_CONFIG_MULTITHREAD](../c3ref/c_config_covering_index_scan.md#sqliteconfigmultithread) then there is no distinction between protected and unprotected sqlite3_value objects and they can be used interchangeably. However, for maximum code portability it is recommended that applications still make the distinction between protected and unprotected sqlite3_value objects even when not strictly required.

The sqlite3_value objects that are passed as parameters into the implementation of [application-defined SQL functions](../appfunc.md) are protected. The sqlite3_value objects returned by [sqlite3_vtab_rhs_value()](../c3ref/vtab_rhs_value.md) are protected. The sqlite3_value object returned by [sqlite3_column_value()](../c3ref/column_blob.md) is unprotected. Unprotected sqlite3_value objects may only be used as arguments to [sqlite3_result_value()](../c3ref/result_blob.md), [sqlite3_bind_value()](../c3ref/bind_blob.md), and [sqlite3_value_dup()](../c3ref/value_dup.md). The [sqlite3_value_type()](../c3ref/value_blob.md) family of interfaces require protected sqlite3_value objects.

19 Methods using this object:

- [sqlite3_value_blob](../c3ref/value_blob.md)
- [sqlite3_value_bytes](../c3ref/value_blob.md)
- [sqlite3_value_bytes16](../c3ref/value_blob.md)
- [sqlite3_value_double](../c3ref/value_blob.md)
- [sqlite3_value_dup](../c3ref/value_dup.md)
- [sqlite3_value_encoding](../c3ref/value_encoding.md)
- [sqlite3_value_free](../c3ref/value_dup.md)
- [sqlite3_value_frombind](../c3ref/value_blob.md)
- [sqlite3_value_int](../c3ref/value_blob.md)
- [sqlite3_value_int64](../c3ref/value_blob.md)
- [sqlite3_value_nochange](../c3ref/value_blob.md)
- [sqlite3_value_numeric_type](../c3ref/value_blob.md)
- [sqlite3_value_pointer](../c3ref/value_blob.md)
- [sqlite3_value_subtype](../c3ref/value_subtype.md)
- [sqlite3_value_text](../c3ref/value_blob.md)
- [sqlite3_value_text16](../c3ref/value_blob.md)
- [sqlite3_value_text16be](../c3ref/value_blob.md)
- [sqlite3_value_text16le](../c3ref/value_blob.md)
- [sqlite3_value_type](../c3ref/value_blob.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
