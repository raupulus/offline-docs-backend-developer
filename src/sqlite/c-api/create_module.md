---
title: Register A Virtual Table Implementation
source_url: https://www.sqlite.org/c3ref/create_module.html
source_path: c3ref/create_module.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1010
---

> \
> int sqlite3_create_module(\
>   sqlite3 \*db,               /\* SQLite connection to register module with \*/\
>   const char \*zName,         /\* Name of the module \*/\
>   const sqlite3_module \*p,   /\* Methods for the module \*/\
>   void \*pClientData          /\* Client data for xCreate/xConnect \*/\
> );\
> int sqlite3_create_module_v2(\
>   sqlite3 \*db,               /\* SQLite connection to register module with \*/\
>   const char \*zName,         /\* Name of the module \*/\
>   const sqlite3_module \*p,   /\* Methods for the module \*/\
>   void \*pClientData,         /\* Client data for xCreate/xConnect \*/\
>   void(\*xDestroy)(void\*)     /\* Module destructor function \*/\
> );\

These routines are used to register a new [virtual table module](../c3ref/module.md) name. Module names must be registered before creating a new [virtual table](../vtab.md) using the module and before using a preexisting [virtual table](../vtab.md) for the module.

The module name is registered on the [database connection](../c3ref/sqlite3.md) specified by the first parameter. The name of the module is given by the second parameter. The third parameter is a pointer to the implementation of the [virtual table module](../c3ref/module.md). The fourth parameter is an arbitrary client data pointer that is passed through into the [xCreate](../vtab.md#xcreate) and [xConnect](../vtab.md#xconnect) methods of the virtual table module when a new virtual table is being created or reinitialized.

The sqlite3_create_module_v2() interface has a fifth parameter which is a pointer to a destructor for the pClientData. SQLite will invoke the destructor function (if it is not NULL) when SQLite no longer needs the pClientData pointer. The destructor will also be invoked if the call to sqlite3_create_module_v2() fails. The sqlite3_create_module() interface is equivalent to sqlite3_create_module_v2() with a NULL destructor.

If the third parameter (the pointer to the sqlite3_module object) is NULL then no new module is created and any existing modules with the same name are dropped.

See also: [sqlite3_drop_modules()](../c3ref/drop_modules.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
