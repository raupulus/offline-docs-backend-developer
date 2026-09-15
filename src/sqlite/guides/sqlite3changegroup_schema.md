---
title: Add a Schema to a Changegroup
source_url: https://www.sqlite.org/session/sqlite3changegroup_schema.html
source_path: session/sqlite3changegroup_schema.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6890
---

[](../session/intro.md)

## Session Module C Interface

## Add a Schema to a Changegroup

> int sqlite3changegroup_schema(sqlite3_changegroup\*, sqlite3\*, const char \*zDb);\

This method may be used to optionally enforce the rule that the changesets added to the changegroup handle must match the schema of database zDb ("main", "temp", or the name of an attached database). If sqlite3changegroup_add() is called to add a changeset that is not compatible with the configured schema, SQLITE_SCHEMA is returned and the changegroup object is left in an undefined state.

A changeset schema is considered compatible with the database schema in the same way as for sqlite3changeset_apply(). Specifically, for each table in the changeset, there exists a database table with:

- The name identified by the changeset, and
- at least as many columns as recorded in the changeset, and
- the primary key columns in the same position as recorded in the changeset.

The output of the changegroup object always has the same schema as the database nominated using this function. In cases where changesets passed to sqlite3changegroup_add() have fewer columns than the corresponding table in the database schema, these are filled in using the default column values from the database schema. This makes it possible to combined changesets that have different numbers of columns for a single table within a changegroup, provided that they are otherwise compatible.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
