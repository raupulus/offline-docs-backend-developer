---
title: Database Connection Status
source_url: https://www.sqlite.org/c3ref/db_status.html
source_path: c3ref/db_status.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1130
---

> \
> int sqlite3_db_status(sqlite3\*, int op, int \*pCur, int \*pHiwtr, int resetFlg);\
> int sqlite3_db_status64(sqlite3\*,int,sqlite3_int64\*,sqlite3_int64\*,int);\

This interface is used to retrieve runtime status information about a single [database connection](../c3ref/sqlite3.md). The first argument is the database connection object to be interrogated. The second argument is an integer constant, taken from the set of [SQLITE_DBSTATUS options](../c3ref/c_dbstatus_options.md), that determines the parameter to interrogate. The set of [SQLITE_DBSTATUS options](../c3ref/c_dbstatus_options.md) is likely to grow in future releases of SQLite.

The current value of the requested parameter is written into \*pCur and the highest instantaneous value is written into \*pHiwtr. If the resetFlg is true, then the highest instantaneous value is reset back down to the current value.

The sqlite3_db_status() routine returns SQLITE_OK on success and a non-zero [error code](../rescode.md) on failure.

The sqlite3_db_status64(D,O,C,H,R) routine works exactly the same way as sqlite3_db_status(D,O,C,H,R) routine except that the C and H parameters are pointer to 64-bit integers (type: sqlite3_int64) instead of pointers to 32-bit integers, which allows larger status values to be returned. If a status value exceeds 2,147,483,647 then sqlite3_db_status() will truncate the value whereas sqlite3_db_status64() will return the full value.

See also: [sqlite3_status()](../c3ref/status.md) and [sqlite3_stmt_status()](../c3ref/stmt_status.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
