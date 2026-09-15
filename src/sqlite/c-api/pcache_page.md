---
title: Custom Page Cache Object
source_url: https://www.sqlite.org/c3ref/pcache_page.html
source_path: c3ref/pcache_page.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1620
---

> \
> typedef struct sqlite3_pcache_page sqlite3_pcache_page;\
> struct sqlite3_pcache_page {\
>   void \*pBuf;        /\* The content of the page \*/\
>   void \*pExtra;      /\* Extra information associated with the page \*/\
> };\

The sqlite3_pcache_page object represents a single page in the page cache. The page cache will allocate instances of this object. Various methods of the page cache use pointers to instances of this object as parameters or as their return value.

See [sqlite3_pcache_methods2](../c3ref/pcache_methods2.md) for additional information.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
