---
title: Automatically Load Statically Linked Extensions
source_url: https://www.sqlite.org/c3ref/auto_extension.html
source_path: c3ref/auto_extension.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 230
---

> \
> int sqlite3_auto_extension(void(\*xEntryPoint)(void));\

This interface causes the xEntryPoint() function to be invoked for each new [database connection](../c3ref/sqlite3.md) that is created. The idea here is that xEntryPoint() is the entry point for a statically linked [SQLite extension](../loadext.md) that is to be automatically loaded into all new database connections.

Even though the function prototype shows that xEntryPoint() takes no arguments and returns void, SQLite invokes xEntryPoint() with three arguments and expects an integer result as if the signature of the entry point were as follows:

> \
>    int xEntryPoint(\
>      sqlite3 \*db,\
>      char \*\*pzErrMsg,\
>      const struct sqlite3_api_routines \*pThunk\
>    );\

If the xEntryPoint routine encounters an error, it should make \*pzErrMsg point to an appropriate error message (obtained from [sqlite3_mprintf()](../c3ref/mprintf.md)) and return an appropriate [error code](../rescode.md). SQLite ensures that \*pzErrMsg is NULL before calling the xEntryPoint(). SQLite will invoke [sqlite3_free()](../c3ref/free.md) on \*pzErrMsg after xEntryPoint() returns. If any xEntryPoint() returns an error, the [sqlite3_open()](../c3ref/open.md), [sqlite3_open16()](../c3ref/open.md), or [sqlite3_open_v2()](../c3ref/open.md) call that provoked the xEntryPoint() will fail.

Calling sqlite3_auto_extension(X) with an entry point X that is already on the list of automatic extensions is a harmless no-op. No entry point will be called more than once for each database connection that is opened.

See also: [sqlite3_reset_auto_extension()](../c3ref/reset_auto_extension.md) and [sqlite3_cancel_auto_extension()](../c3ref/cancel_auto_extension.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
