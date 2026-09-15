---
title: Status Parameters for prepared statements
source_url: https://www.sqlite.org/c3ref/c_stmtstatus_counter.html
source_path: c3ref/c_stmtstatus_counter.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 730
---

> \
> \#define SQLITE_STMTSTATUS_FULLSCAN_STEP     1\
> \#define SQLITE_STMTSTATUS_SORT              2\
> \#define SQLITE_STMTSTATUS_AUTOINDEX         3\
> \#define SQLITE_STMTSTATUS_VM_STEP           4\
> \#define SQLITE_STMTSTATUS_REPREPARE         5\
> \#define SQLITE_STMTSTATUS_RUN               6\
> \#define SQLITE_STMTSTATUS_FILTER_MISS       7\
> \#define SQLITE_STMTSTATUS_FILTER_HIT        8\
> \#define SQLITE_STMTSTATUS_MEMUSED           99\

These preprocessor macros define integer codes that name counter values associated with the [sqlite3_stmt_status()](../c3ref/stmt_status.md) interface. The meanings of the various counters are as follows:

SQLITE_STMTSTATUS_FULLSCAN_STEP  
This is the number of times that SQLite has stepped forward in a table as part of a full table scan. Large numbers for this counter may indicate opportunities for performance improvement through careful use of indices.

SQLITE_STMTSTATUS_SORT  
This is the number of sort operations that have occurred. A non-zero value in this counter may indicate an opportunity to improve performance through careful use of indices.

SQLITE_STMTSTATUS_AUTOINDEX  
This is the number of rows inserted into transient indices that were created automatically in order to help joins run faster. A non-zero value in this counter may indicate an opportunity to improve performance by adding permanent indices that do not need to be reinitialized each time the statement is run.

SQLITE_STMTSTATUS_VM_STEP  
This is the number of virtual machine operations executed by the prepared statement if that number is less than or equal to 2147483647. The number of virtual machine operations can be used as a proxy for the total work done by the prepared statement. If the number of virtual machine operations exceeds 2147483647 then the value returned by this statement status code is undefined.

SQLITE_STMTSTATUS_REPREPARE  
This is the number of times that the prepare statement has been automatically regenerated due to schema changes or changes to [bound parameters](../lang_expr.md#varparam) that might affect the query plan.

SQLITE_STMTSTATUS_RUN  
This is the number of times that the prepared statement has been run. A single "run" for the purposes of this counter is one or more calls to [sqlite3_step()](../c3ref/step.md) followed by a call to [sqlite3_reset()](../c3ref/reset.md). The counter is incremented on the first [sqlite3_step()](../c3ref/step.md) call of each cycle.

SQLITE_STMTSTATUS_FILTER_HIT\
SQLITE_STMTSTATUS_FILTER_MISS  
SQLITE_STMTSTATUS_FILTER_HIT is the number of times that a join step was bypassed because a Bloom filter returned not-found. The corresponding SQLITE_STMTSTATUS_FILTER_MISS value is the number of times that the Bloom filter returned a find, and thus the join step had to be processed as normal.

SQLITE_STMTSTATUS_MEMUSED  
This is the approximate number of bytes of heap memory used to store the prepared statement. This value is not actually a counter, and so the resetFlg parameter to sqlite3_stmt_status() is ignored when the opcode is SQLITE_STMTSTATUS_MEMUSED.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
