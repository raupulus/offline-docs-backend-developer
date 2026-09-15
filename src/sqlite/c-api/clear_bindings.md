---
title: Reset All Bindings On A Prepared Statement
source_url: https://www.sqlite.org/c3ref/clear_bindings.html
source_path: c3ref/clear_bindings.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 830
---

> \
> int sqlite3_clear_bindings(sqlite3_stmt\*);\

Contrary to the intuition of many, [sqlite3_reset()](../c3ref/reset.md) does not reset the [bindings](../c3ref/bind_blob.md) on a [prepared statement](../c3ref/stmt.md). Use this routine to reset all host parameters to NULL.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
