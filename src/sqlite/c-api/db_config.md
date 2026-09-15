---
title: Configure database connections
source_url: https://www.sqlite.org/c3ref/db_config.html
source_path: c3ref/db_config.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1060
---

> \
> int sqlite3_db_config(sqlite3\*, int op, ...);\

The sqlite3_db_config() interface is used to make configuration changes to a [database connection](../c3ref/sqlite3.md). The interface is similar to [sqlite3_config()](../c3ref/config.md) except that the changes apply to a single [database connection](../c3ref/sqlite3.md) (specified in the first argument).

The second argument to sqlite3_db_config(D,V,...) is the [configuration verb](../c3ref/c_dbconfig_defensive.md#sqlitedbconfiglookaside) - an integer code that indicates what aspect of the [database connection](../c3ref/sqlite3.md) is being configured. Subsequent arguments vary depending on the configuration verb.

Calls to sqlite3_db_config() return SQLITE_OK if and only if the call is considered successful.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
