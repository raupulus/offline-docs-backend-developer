---
title: Set a table filter on a Session Object.
source_url: https://www.sqlite.org/session/sqlite3session_table_filter.html
source_path: session/sqlite3session_table_filter.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7190
---

[](../session/intro.md)

## Session Module C Interface

## Set a table filter on a Session Object.

> void sqlite3session_table_filter(\
>   sqlite3_session \*pSession,      /\* Session object \*/\
>   int(\*xFilter)(\
>     void \*pCtx,                   /\* Copy of third arg to \_filter_table() \*/\
>     const char \*zTab              /\* Table name \*/\
>   ),\
>   void \*pCtx                      /\* First argument passed to xFilter \*/\
> );\

The second argument (xFilter) is the "filter callback". For changes to rows in tables that are not attached to the Session object, the filter is called to determine whether changes to the table's rows should be tracked or not. If xFilter returns 0, changes are not tracked. Note that once a table is attached, xFilter will not be called again.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
