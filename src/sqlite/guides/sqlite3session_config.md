---
title: Configure global parameters
source_url: https://www.sqlite.org/session/sqlite3session_config.html
source_path: session/sqlite3session_config.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7090
---

[](../session/intro.md)

## Session Module C Interface

## Configure global parameters

> int sqlite3session_config(int op, void \*pArg);\

The sqlite3session_config() interface is used to make global configuration changes to the sessions module in order to tune it to the specific needs of the application.

The sqlite3session_config() interface is not threadsafe. If it is invoked while any other thread is inside any other sessions method then the results are undefined. Furthermore, if it is invoked after any sessions related objects have been created, the results are also undefined.

The first argument to the sqlite3session_config() function must be one of the SQLITE_SESSION_CONFIG_XXX constants defined below. The interpretation of the (void\*) value passed as the second parameter and the effect of calling this function depends on the value of the first parameter.

SQLITE_SESSION_CONFIG_STRMSIZE  
By default, the sessions module streaming interfaces attempt to input and output data in approximately 1 KiB chunks. This operand may be used to set and query the value of this configuration setting. The pointer passed as the second argument must point to a value of type (int). If this value is greater than 0, it is used as the new streaming data chunk size for both input and output. Before returning, the (int) value pointed to by pArg is set to the final value of the streaming interface chunk size.

This function returns SQLITE_OK if successful, or an SQLite error code otherwise.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
