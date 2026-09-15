---
title: Zero Scan-Status Counters
source_url: https://www.sqlite.org/c3ref/stmt_scanstatus_reset.html
source_path: c3ref/stmt_scanstatus_reset.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1950
---

> \
> void sqlite3_stmt_scanstatus_reset(sqlite3_stmt\*);\

Zero all [sqlite3_stmt_scanstatus()](../c3ref/stmt_scanstatus.md) related event counters.

This API is only available if the library is built with pre-processor symbol [SQLITE_ENABLE_STMT_SCANSTATUS](../compile.md#enable_stmt_scanstatus) defined.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
