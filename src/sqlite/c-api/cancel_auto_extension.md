---
title: Cancel Automatic Extension Loading
source_url: https://www.sqlite.org/c3ref/cancel_auto_extension.html
source_path: c3ref/cancel_auto_extension.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 800
---

> \
> int sqlite3_cancel_auto_extension(void(\*xEntryPoint)(void));\

The [sqlite3_cancel_auto_extension(X)](../c3ref/cancel_auto_extension.md) interface unregisters the initialization routine X that was registered using a prior call to [sqlite3_auto_extension(X)](../c3ref/auto_extension.md). The [sqlite3_cancel_auto_extension(X)](../c3ref/cancel_auto_extension.md) routine returns 1 if initialization routine X was successfully unregistered and it returns 0 if X was not on the list of initialization routines.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
