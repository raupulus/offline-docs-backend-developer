---
title: Full-Featured SQL
source_url: https://www.sqlite.org/fullsql.html
source_path: fullsql.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2940
---

Do not be misled by the "Lite" in the name. SQLite has a full-featured SQL implementation, including:

- [Tables](lang_createtable.md), [indexes](lang_createindex.md), [triggers](lang_createtrigger.md), and [views](lang_createview.md) in unlimited quantity
- Up to 32K columns in a table and unlimited rows
- Multi-column indexes
- Indexes can use [DESC](lang_createindex.md#descidx) and [COLLATE](lang_createindex.md#collidx)
- [Partial indexes](partialindex.md)
- [Indexes On Expressions](expridx.md)
- [Clustered indexes](withoutrowid.md)
- [Covering indexes](queryplanner.md#covidx)
- [CHECK](lang_createtable.md#ckconst), [UNIQUE](lang_createtable.md#uniqueconst), [NOT NULL](lang_createtable.md#notnullconst), and [FOREIGN KEY constraints](foreignkeys.md).
- ACID transactions using [BEGIN](lang_transaction.md), [COMMIT](lang_transaction.md), and [ROLLBACK](lang_transaction.md)
- Nested transactions using [SAVEPOINT](lang_savepoint.md), [RELEASE](lang_savepoint.md), and [ROLLBACK TO](lang_transaction.md)
- [Subqueries](lang_expr.md#subq), including [correlated subqueries](lang_expr.md#cosub)
- Up to 64-way joins
- LEFT, RIGHT, and FULL OUTER JOINs
- DISTINCT, ORDER BY, GROUP BY, HAVING, LIMIT, and OFFSET
- UNION, UNION ALL, INTERSECT, and EXCEPT
- A rich library of [standard SQL functions](lang_corefunc.md)
- [Aggregate functions](lang_aggfunc.md) including DISTINCT aggregates
- [Window functions](windowfunctions.md)
- [UPDATE](lang_update.md), [DELETE](lang_delete.md), and [INSERT](lang_insert.md) (of course)
- [Common table expressions](lang_with.md) including [recursive common table expressions](lang_with.md#recursivecte)
- [Row values](rowvalue.md)
- [UPSERT](lang_upsert.md)
- An advanced [query planner](optoverview.md)
- [Full-text search](fts5.md)
- [R-tree indexes](rtree.md)
- [JSON support](json1.md)
- The [IS operator](lang_expr.md#isisnot)
- [Table-valued functions](vtab.md#tabfunc2)
- [REPLACE INTO](lang_replace.md)
- [VACUUM](lang_vacuum.md)
- [REINDEX](lang_reindex.md)
- The [GLOB](lang_expr.md#glob) operator
- [Hexadecimal integer literals](lang_expr.md#hexint)
- The [ON CONFLICT](lang_conflict.md) clause
- The [INDEXED BY](lang_indexedby.md) clause
- [Virtual tables](vtab.md)
- Multiple databases on the same [database connection](c3ref/sqlite3.md) using [ATTACH DATABASE](lang_attach.md)
- The ability to add [application-defined SQL functions](appfunc.md), including aggregate and table-valued functions.
- [Application-defined collating functions](c3ref/create_collation.md)

There are many more features not listed above. SQLite may be small in size and have "Lite" in its name, but it is not lacking in capability.
