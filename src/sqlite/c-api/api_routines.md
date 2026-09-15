---
title: Loadable Extension Thunk
source_url: https://www.sqlite.org/c3ref/api_routines.html
source_path: c3ref/api_routines.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 220
---

> \
> typedef struct sqlite3_api_routines sqlite3_api_routines;\

A pointer to the opaque sqlite3_api_routines structure is passed as the third parameter to entry points of [loadable extensions](../loadext.md). This structure must be typedefed in order to work around compiler warnings on some platforms.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
