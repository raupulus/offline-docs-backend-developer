---
title: Determine The Collation For a Virtual Table Constraint
source_url: https://www.sqlite.org/c3ref/vtab_collation.html
source_path: c3ref/vtab_collation.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2250
---

> \
> const char \*sqlite3_vtab_collation(sqlite3_index_info\*,int);\

This function may only be called from within a call to the [xBestIndex](../vtab.md#xbestindex) method of a [virtual table](../vtab.md). This function returns a pointer to a string that is the name of the appropriate collation sequence to use for text comparisons on the constraint identified by its arguments.

The first argument must be the pointer to the [sqlite3_index_info](../c3ref/index_info.md) object that is the first parameter to the xBestIndex() method. The second argument must be an index into the aConstraint\[\] array belonging to the sqlite3_index_info structure passed to xBestIndex.

Important: The first parameter must be the same pointer that is passed into the xBestMethod() method. The first parameter may not be a pointer to a different [sqlite3_index_info](../c3ref/index_info.md) object, even an exact copy.

The return value is computed as follows:

1.  If the constraint comes from a WHERE clause expression that contains a [COLLATE operator](../lang_expr.md#collateop), then the name of the collation specified by that COLLATE operator is returned.

2.  If there is no COLLATE operator, but the column that is the subject of the constraint specifies an alternative collating sequence via a [COLLATE clause](../lang_createtable.md#collateclause) on the column definition within the CREATE TABLE statement that was passed into [sqlite3_declare_vtab()](../c3ref/declare_vtab.md), then the name of that alternative collating sequence is returned.

3.  Otherwise, "BINARY" is returned.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
