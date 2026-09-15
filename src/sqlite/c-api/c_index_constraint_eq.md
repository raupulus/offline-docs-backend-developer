---
title: Virtual Table Constraint Operator Codes
source_url: https://www.sqlite.org/c3ref/c_index_constraint_eq.html
source_path: c3ref/c_index_constraint_eq.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 560
---

> \
> \#define SQLITE_INDEX_CONSTRAINT_EQ          2\
> \#define SQLITE_INDEX_CONSTRAINT_GT          4\
> \#define SQLITE_INDEX_CONSTRAINT_LE          8\
> \#define SQLITE_INDEX_CONSTRAINT_LT         16\
> \#define SQLITE_INDEX_CONSTRAINT_GE         32\
> \#define SQLITE_INDEX_CONSTRAINT_MATCH      64\
> \#define SQLITE_INDEX_CONSTRAINT_LIKE       65\
> \#define SQLITE_INDEX_CONSTRAINT_GLOB       66\
> \#define SQLITE_INDEX_CONSTRAINT_REGEXP     67\
> \#define SQLITE_INDEX_CONSTRAINT_NE         68\
> \#define SQLITE_INDEX_CONSTRAINT_ISNOT      69\
> \#define SQLITE_INDEX_CONSTRAINT_ISNOTNULL  70\
> \#define SQLITE_INDEX_CONSTRAINT_ISNULL     71\
> \#define SQLITE_INDEX_CONSTRAINT_IS         72\
> \#define SQLITE_INDEX_CONSTRAINT_LIMIT      73\
> \#define SQLITE_INDEX_CONSTRAINT_OFFSET     74\
> \#define SQLITE_INDEX_CONSTRAINT_FUNCTION  150\

These macros define the allowed values for the [sqlite3_index_info](../c3ref/index_info.md).aConstraint\[\].op field. Each value represents an operator that is part of a constraint term in the WHERE clause of a query that uses a [virtual table](../vtab.md).

The left-hand operand of the operator is given by the corresponding aConstraint\[\].iColumn field. An iColumn of -1 indicates the left-hand operand is the rowid. The SQLITE_INDEX_CONSTRAINT_LIMIT and SQLITE_INDEX_CONSTRAINT_OFFSET operators have no left-hand operand, and so for those operators the corresponding aConstraint\[\].iColumn is meaningless and should not be used.

All operator values from SQLITE_INDEX_CONSTRAINT_FUNCTION through value 255 are reserved to represent functions that are overloaded by the [xFindFunction method](../vtab.md#xfindfunction) of the virtual table implementation.

The right-hand operands for each constraint might be accessible using the [sqlite3_vtab_rhs_value()](../c3ref/vtab_rhs_value.md) interface. Usually the right-hand operand is only available if it appears as a single constant literal in the input SQL. If the right-hand operand is another column or an expression (even a constant expression) or a parameter, then the sqlite3_vtab_rhs_value() probably will not be able to extract it. The SQLITE_INDEX_CONSTRAINT_ISNULL and SQLITE_INDEX_CONSTRAINT_ISNOTNULL operators have no right-hand operand and hence calls to sqlite3_vtab_rhs_value() for those operators will always return SQLITE_NOTFOUND.

The collating sequence to be used for comparison can be found using the [sqlite3_vtab_collation()](../c3ref/vtab_collation.md) interface. For most real-world virtual tables, the collating sequence of constraints does not matter (for example because the constraints are numeric) and so the sqlite3_vtab_collation() interface is not commonly needed.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
