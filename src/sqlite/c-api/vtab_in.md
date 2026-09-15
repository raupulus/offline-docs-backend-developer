---
title: Identify and handle IN constraints in xBestIndex
source_url: https://www.sqlite.org/c3ref/vtab_in.html
source_path: c3ref/vtab_in.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2290
---

> \
> int sqlite3_vtab_in(sqlite3_index_info\*, int iCons, int bHandle);\

This interface may only be used from within an [xBestIndex() method](../vtab.md#xbestindex) of a [virtual table](../vtab.md) implementation. The result of invoking this interface from any other context is undefined and probably harmful.

A constraint on a virtual table of the form "[column IN (...)](../lang_expr.md#in_op)" is communicated to the xBestIndex method as a [SQLITE_INDEX_CONSTRAINT_EQ](../c3ref/c_index_constraint_eq.md) constraint. If xBestIndex wants to use this constraint, it must set the corresponding aConstraintUsage\[\].argvIndex to a positive integer. Then, under the usual mode of handling IN operators, SQLite generates [bytecode](../opcode.md) that invokes the [xFilter() method](../vtab.md#xfilter) once for each value on the right-hand side of the IN operator. Thus the virtual table only sees a single value from the right-hand side of the IN operator at a time.

In some cases, however, it would be advantageous for the virtual table to see all values on the right-hand of the IN operator all at once. The sqlite3_vtab_in() interfaces facilitates this in two ways:

1.  A call to sqlite3_vtab_in(P,N,-1) will return true (non-zero) if and only if the [P-\>aConstraint](../c3ref/index_info.md)\[N\] constraint is an [IN operator](../lang_expr.md#in_op) that can be processed all at once. In other words, sqlite3_vtab_in() with -1 in the third argument is a mechanism by which the virtual table can ask SQLite if all-at-once processing of the IN operator is even possible.

2.  A call to sqlite3_vtab_in(P,N,F) with F==1 or F==0 indicates to SQLite that the virtual table does or does not want to process the IN operator all-at-once, respectively. Thus when the third parameter (F) is non-negative, this interface is the mechanism by which the virtual table tells SQLite how it wants to process the IN operator.

The sqlite3_vtab_in(P,N,F) interface can be invoked multiple times within the same xBestIndex method call. For any given P,N pair, the return value from sqlite3_vtab_in(P,N,F) will always be the same within the same xBestIndex call. If the interface returns true (non-zero), that means that the constraint is an IN operator that can be processed all-at-once. If the constraint is not an IN operator or cannot be processed all-at-once, then the interface returns false.

All-at-once processing of the IN operator is selected if both of the following conditions are met:

1.  The P-\>aConstraintUsage\[N\].argvIndex value is set to a positive integer. This is how the virtual table tells SQLite that it wants to use the N-th constraint.

2.  The last call to sqlite3_vtab_in(P,N,F) for which F was non-negative had F\>=1.

If either or both of the conditions above are false, then SQLite uses the traditional one-at-a-time processing strategy for the IN constraint. If both conditions are true, then the argvIndex-th parameter to the xFilter method will be an [sqlite3_value](../c3ref/value.md) that appears to be NULL, but which can be passed to [sqlite3_vtab_in_first()](../c3ref/vtab_in_first.md) and [sqlite3_vtab_in_next()](../c3ref/vtab_in_first.md) to find all values on the right-hand side of the IN constraint.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
