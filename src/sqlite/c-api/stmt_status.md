---
title: Prepared Statement Status
source_url: https://www.sqlite.org/c3ref/stmt_status.html
source_path: c3ref/stmt_status.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1960
---

> \
> int sqlite3_stmt_status(sqlite3_stmt\*, int op,int resetFlg);\

Each prepared statement maintains various [SQLITE_STMTSTATUS counters](../c3ref/c_stmtstatus_counter.md) that measure the number of times it has performed specific operations. These counters can be used to monitor the performance characteristics of the prepared statements. For example, if the number of table steps greatly exceeds the number of table searches or result rows, that would tend to indicate that the prepared statement is using a full table scan rather than an index.

This interface is used to retrieve and reset counter values from a [prepared statement](../c3ref/stmt.md). The first argument is the prepared statement object to be interrogated. The second argument is an integer code for a specific [SQLITE_STMTSTATUS counter](../c3ref/c_stmtstatus_counter.md) to be interrogated. The current value of the requested counter is returned. If the resetFlg is true, then the counter is reset to zero after this interface call returns.

See also: [sqlite3_status()](../c3ref/status.md) and [sqlite3_db_status()](../c3ref/db_status.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
