---
title: Find all elements on the right-hand side of an IN constraint.
source_url: https://www.sqlite.org/c3ref/vtab_in_first.html
source_path: c3ref/vtab_in_first.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2300
---

> \
> int sqlite3_vtab_in_first(sqlite3_value \*pVal, sqlite3_value \*\*ppOut);\
> int sqlite3_vtab_in_next(sqlite3_value \*pVal, sqlite3_value \*\*ppOut);\

These interfaces are only useful from within the [xFilter() method](../vtab.md#xfilter) of a [virtual table](../vtab.md) implementation. The result of invoking these interfaces from any other context is undefined and probably harmful.

The X parameter in a call to sqlite3_vtab_in_first(X,P) or sqlite3_vtab_in_next(X,P) should be one of the parameters to the xFilter method which invokes these routines, and specifically a parameter that was previously selected for all-at-once IN constraint processing using the [sqlite3_vtab_in()](../c3ref/vtab_in.md) interface in the [xBestIndex method](../vtab.md#xbestindex). If the X parameter is not an xFilter argument that was selected for all-at-once IN constraint processing, then these routines return [SQLITE_ERROR](../rescode.md#error).

Use these routines to access all values on the right-hand side of the IN constraint using code like the following:

> \
>    for(rc=sqlite3_vtab_in_first(pList, &pVal);\
>        rc==SQLITE_OK && pVal;\
>        rc=sqlite3_vtab_in_next(pList, &pVal)\
>    ){\
>      // do something with pVal\
>    }\
>    if( rc!=SQLITE_DONE ){\
>      // an error has occurred\
>    }\

On success, the sqlite3_vtab_in_first(X,P) and sqlite3_vtab_in_next(X,P) routines return SQLITE_OK and set \*P to point to the first or next value on the RHS of the IN constraint. If there are no more values on the right hand side of the IN constraint, then \*P is set to NULL and these routines return [SQLITE_DONE](../rescode.md#done). The return value might be some other value, such as SQLITE_NOMEM, in the event of a malfunction.

The \*ppOut values returned by these routines are only valid until the next call to either of these routines or until the end of the xFilter method from which these routines were called. If the virtual table implementation needs to retain the \*ppOut values for longer, it must make copies. The \*ppOut values are [protected](../c3ref/value.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
