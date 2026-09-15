---
title: Custom Page Cache Object
source_url: https://www.sqlite.org/c3ref/pcache.html
source_path: c3ref/pcache.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1600
---

> \
> typedef struct sqlite3_pcache sqlite3_pcache;\

The sqlite3_pcache type is opaque. It is implemented by the pluggable module. The SQLite core has no knowledge of its size or internal structure and never deals with the sqlite3_pcache object except by holding and passing pointers to the object.

See [sqlite3_pcache_methods2](../c3ref/pcache_methods2.md) for additional information.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
