---
title: Virtual Table Cursor Object
source_url: https://www.sqlite.org/c3ref/vtab_cursor.html
source_path: c3ref/vtab_cursor.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2270
---

> \
> struct sqlite3_vtab_cursor {\
>   sqlite3_vtab \*pVtab;      /\* Virtual table of this cursor \*/\
>   /\* Virtual table implementations will typically add additional fields \*/\
> };\

Every [virtual table module](../c3ref/module.md) implementation uses a subclass of the following structure to describe cursors that point into the [virtual table](../vtab.md) and are used to loop through the virtual table. Cursors are created using the [xOpen](../vtab.md#xopen) method of the module and are destroyed by the [xClose](../vtab.md#xclose) method. Cursors are used by the [xFilter](../vtab.md#xfilter), [xNext](../vtab.md#xnext), [xEof](../vtab.md#xeof), [xColumn](../vtab.md#xcolumn), and [xRowid](../vtab.md#xrowid) methods of the module. Each module implementation will define the content of a cursor structure to suit its own needs.

This superclass exists in order to define fields of the cursor that are common to all implementations.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
