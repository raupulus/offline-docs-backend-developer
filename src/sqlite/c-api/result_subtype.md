---
title: Setting The Subtype Of An SQL Function
source_url: https://www.sqlite.org/c3ref/result_subtype.html
source_path: c3ref/result_subtype.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1720
---

> \
> void sqlite3_result_subtype(sqlite3_context\*,unsigned int);\

The sqlite3_result_subtype(C,T) function causes the subtype of the result from the [application-defined SQL function](../appfunc.md) with [sqlite3_context](../c3ref/context.md) C to be the value T. Only the lower 8 bits of the subtype T are preserved in current versions of SQLite; higher order bits are discarded. The number of subtype bytes preserved by SQLite might increase in future releases of SQLite.

Every [application-defined SQL function](../appfunc.md) that invokes this interface should include the [SQLITE_RESULT_SUBTYPE](../c3ref/c_deterministic.md#sqliteresultsubtype) property in its text encoding argument when the SQL function is [registered](../c3ref/create_function.md). If the [SQLITE_RESULT_SUBTYPE](../c3ref/c_deterministic.md#sqliteresultsubtype) property is omitted from the function that invokes sqlite3_result_subtype(), then in some cases the sqlite3_result_subtype() might fail to set the result subtype.

If SQLite is compiled with -DSQLITE_STRICT_SUBTYPE=1, then any SQL function that invokes the sqlite3_result_subtype() interface and that does not have the SQLITE_RESULT_SUBTYPE property will raise an error. Future versions of SQLite might enable -DSQLITE_STRICT_SUBTYPE=1 by default.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
