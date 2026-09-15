---
title: Constraint values in xBestIndex()
source_url: https://www.sqlite.org/c3ref/vtab_rhs_value.html
source_path: c3ref/vtab_rhs_value.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2330
---

> \
> int sqlite3_vtab_rhs_value(sqlite3_index_info\*, int, sqlite3_value \*\*ppVal);\

This API may only be used from within the [xBestIndex method](../vtab.md#xbestindex) of a [virtual table](../vtab.md) implementation. The result of calling this interface from outside of an xBestIndex method are undefined and probably harmful.

When the sqlite3_vtab_rhs_value(P,J,V) interface is invoked from within the [xBestIndex](../vtab.md#xbestindex) method of a [virtual table](../vtab.md) implementation, with P being a copy of the [sqlite3_index_info](../c3ref/index_info.md) object pointer passed into xBestIndex and J being a 0-based index into P-\>aConstraint\[\], then this routine attempts to set \*V to the value of the right-hand operand of that constraint if the right-hand operand is known. If the right-hand operand is not known, then \*V is set to a NULL pointer. The sqlite3_vtab_rhs_value(P,J,V) interface returns SQLITE_OK if and only if \*V is set to a value. The sqlite3_vtab_rhs_value(P,J,V) inteface returns SQLITE_NOTFOUND if the right-hand side of the J-th constraint is not available. The sqlite3_vtab_rhs_value() interface can return a result code other than SQLITE_OK or SQLITE_NOTFOUND if something goes wrong.

The sqlite3_vtab_rhs_value() interface is usually only successful if the right-hand operand of a constraint is a literal value in the original SQL statement. If the right-hand operand is an expression or a reference to some other column or a [host parameter](../c3ref/bind_blob.md), then sqlite3_vtab_rhs_value() will probably return [SQLITE_NOTFOUND](../rescode.md#notfound).

Some constraints, such as [SQLITE_INDEX_CONSTRAINT_ISNULL](../c3ref/c_index_constraint_eq.md) and [SQLITE_INDEX_CONSTRAINT_ISNOTNULL](../c3ref/c_index_constraint_eq.md), have no right-hand operand. For such constraints, sqlite3_vtab_rhs_value() always returns SQLITE_NOTFOUND.

The [sqlite3_value](../c3ref/value.md) object returned in \*V is a protected sqlite3_value and remains valid for the duration of the xBestIndex method call. When xBestIndex returns, the sqlite3_value object returned by sqlite3_vtab_rhs_value() is automatically deallocated.

The "\_rhs\_" in the name of this routine is an abbreviation for "Right-Hand Side".

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
