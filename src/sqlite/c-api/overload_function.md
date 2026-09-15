---
title: Overload A Function For A Virtual Table
source_url: https://www.sqlite.org/c3ref/overload_function.html
source_path: c3ref/overload_function.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1590
---

> \
> int sqlite3_overload_function(sqlite3\*, const char \*zFuncName, int nArg);\

Virtual tables can provide alternative implementations of functions using the [xFindFunction](../vtab.md#xfindfunction) method of the [virtual table module](../c3ref/module.md). But global versions of those functions must exist in order to be overloaded.

This API makes sure a global version of a function with a particular name and number of parameters exists. If no such function exists before this API is called, a new function is created. The implementation of the new function always causes an exception to be thrown. So the new function is not good for anything by itself. Its only purpose is to be a placeholder function that can be overloaded by a [virtual table](../vtab.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
