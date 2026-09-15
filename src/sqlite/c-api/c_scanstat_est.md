---
title: Prepared Statement Scan Status Opcodes
source_url: https://www.sqlite.org/c3ref/c_scanstat_est.html
source_path: c3ref/c_scanstat_est.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 650
---

> \
> \#define SQLITE_SCANSTAT_NLOOP    0\
> \#define SQLITE_SCANSTAT_NVISIT   1\
> \#define SQLITE_SCANSTAT_EST      2\
> \#define SQLITE_SCANSTAT_NAME     3\
> \#define SQLITE_SCANSTAT_EXPLAIN  4\
> \#define SQLITE_SCANSTAT_SELECTID 5\
> \#define SQLITE_SCANSTAT_PARENTID 6\
> \#define SQLITE_SCANSTAT_NCYCLE   7\

The following constants can be used for the T parameter to the [sqlite3_stmt_scanstatus(S,X,T,V)](../c3ref/stmt_scanstatus.md) interface. Each constant designates a different metric for sqlite3_stmt_scanstatus() to return.

When the value returned to V is a string, space to hold that string is managed by the prepared statement S and will be automatically freed when S is finalized.

Not all values are available for all query elements. When a value is not available, the output variable is set to -1 if the value is numeric, or to NULL if it is a string (SQLITE_SCANSTAT_NAME).

SQLITE_SCANSTAT_NLOOP  
The [sqlite3_int64](../c3ref/int64.md) variable pointed to by the V parameter will be set to the total number of times that the X-th loop has run.

SQLITE_SCANSTAT_NVISIT  
The [sqlite3_int64](../c3ref/int64.md) variable pointed to by the V parameter will be set to the total number of rows examined by all iterations of the X-th loop.

SQLITE_SCANSTAT_EST  
The "double" variable pointed to by the V parameter will be set to the query planner's estimate for the average number of rows output from each iteration of the X-th loop. If the query planner's estimate was accurate, then this value will approximate the quotient NVISIT/NLOOP and the product of this value for all prior loops with the same SELECTID will be the NLOOP value for the current loop.

SQLITE_SCANSTAT_NAME  
The "const char \*" variable pointed to by the V parameter will be set to a zero-terminated UTF-8 string containing the name of the index or table used for the X-th loop.

SQLITE_SCANSTAT_EXPLAIN  
The "const char \*" variable pointed to by the V parameter will be set to a zero-terminated UTF-8 string containing the [EXPLAIN QUERY PLAN](../eqp.md) description for the X-th loop.

SQLITE_SCANSTAT_SELECTID  
The "int" variable pointed to by the V parameter will be set to the id for the X-th query plan element. The id value is unique within the statement. The select-id is the same value as is output in the first column of an [EXPLAIN QUERY PLAN](../eqp.md) query.

SQLITE_SCANSTAT_PARENTID  
The "int" variable pointed to by the V parameter will be set to the id of the parent of the current query element, if applicable, or to zero if the query element has no parent. This is the same value as returned in the second column of an [EXPLAIN QUERY PLAN](../eqp.md) query.

SQLITE_SCANSTAT_NCYCLE  
The sqlite3_int64 output value is set to the number of cycles, according to the processor time-stamp counter, that elapsed while the query element was being processed. This value is not available for all query elements - if it is unavailable the output variable is set to -1.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
