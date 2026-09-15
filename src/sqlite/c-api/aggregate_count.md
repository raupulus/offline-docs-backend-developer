---
title: Deprecated Functions
source_url: https://www.sqlite.org/c3ref/aggregate_count.html
source_path: c3ref/aggregate_count.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 210
---

> \
> \#ifndef SQLITE_OMIT_DEPRECATED\
> int sqlite3_aggregate_count(sqlite3_context\*);\
> int sqlite3_expired(sqlite3_stmt\*);\
> int sqlite3_transfer_bindings(sqlite3_stmt\*, sqlite3_stmt\*);\
> int sqlite3_global_recover(void);\
> void sqlite3_thread_cleanup(void);\
> int sqlite3_memory_alarm(void(\*)(void\*,sqlite3_int64,int),\
>                       void\*,sqlite3_int64);\
> \#endif\

These functions are [deprecated](../c3ref/experimental.md). In order to maintain backwards compatibility with older code, these functions continue to be supported. However, new applications should avoid the use of these functions. To encourage programmers to avoid these functions, we will not explain what they do.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
