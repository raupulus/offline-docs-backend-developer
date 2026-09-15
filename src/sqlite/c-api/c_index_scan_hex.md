---
title: Virtual Table Scan Flags
source_url: https://www.sqlite.org/c3ref/c_index_scan_hex.html
source_path: c3ref/c_index_scan_hex.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 570
---

> \
> \#define SQLITE_INDEX_SCAN_UNIQUE 0x00000001 /\* Scan visits at most 1 row \*/\
> \#define SQLITE_INDEX_SCAN_HEX    0x00000002 /\* Display idxNum as hex \*/\
>                                             /\* in EXPLAIN QUERY PLAN \*/\

Virtual table implementations are allowed to set the [sqlite3_index_info](../c3ref/index_info.md).idxFlags field to some combination of these bits.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
