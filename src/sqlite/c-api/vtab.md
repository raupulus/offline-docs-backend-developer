---
title: Virtual Table Instance Object
source_url: https://www.sqlite.org/c3ref/vtab.html
source_path: c3ref/vtab.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2240
---

> \
> struct sqlite3_vtab {\
>   const sqlite3_module \*pModule;  /\* The module for this virtual table \*/\
>   int nRef;                       /\* Number of open cursors \*/\
>   char \*zErrMsg;                  /\* Error message from sqlite3_mprintf() \*/\
>   /\* Virtual table implementations will typically add additional fields \*/\
> };\

Every [virtual table module](../c3ref/module.md) implementation uses a subclass of this object to describe a particular instance of the [virtual table](../vtab.md). Each subclass will be tailored to the specific needs of the module implementation. The purpose of this superclass is to define certain fields that are common to all module implementations.

Virtual tables methods can set an error message by assigning a string obtained from [sqlite3_mprintf()](../c3ref/mprintf.md) to zErrMsg. The method should take care that any prior string is freed by a call to [sqlite3_free()](../c3ref/free.md) prior to assigning a new string to zErrMsg. After the error message is delivered up to the client application, the string will be automatically freed by sqlite3_free() and the zErrMsg field will be zeroed.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
