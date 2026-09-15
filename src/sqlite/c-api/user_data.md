---
title: User Data For Functions
source_url: https://www.sqlite.org/c3ref/user_data.html
source_path: c3ref/user_data.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2160
---

> \
> void \*sqlite3_user_data(sqlite3_context\*);\

The sqlite3_user_data() interface returns a copy of the pointer that was the pUserData parameter (the 5th parameter) of the [sqlite3_create_function()](../c3ref/create_function.md) and [sqlite3_create_function16()](../c3ref/create_function.md) routines that originally registered the application defined function.

This routine must be called from the same thread in which the application-defined function is running.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
