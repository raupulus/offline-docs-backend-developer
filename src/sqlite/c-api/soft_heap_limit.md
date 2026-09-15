---
title: Deprecated Soft Heap Limit Interface
source_url: https://www.sqlite.org/c3ref/soft_heap_limit.html
source_path: c3ref/soft_heap_limit.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1850
---

> \
> void sqlite3_soft_heap_limit(int N);\

This is a deprecated version of the [sqlite3_soft_heap_limit64()](../c3ref/hard_heap_limit64.md) interface. This routine is provided for historical compatibility only. All new applications should use the [sqlite3_soft_heap_limit64()](../c3ref/hard_heap_limit64.md) interface rather than this one.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
