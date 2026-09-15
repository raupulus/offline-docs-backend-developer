---
title: Add a 64-bit integer to a changegroup
source_url: https://www.sqlite.org/session/sqlite3changegroup_change_int64.html
source_path: session/sqlite3changegroup_change_int64.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6820
---

[](../session/intro.md)

## Session Module C Interface

## Add a 64-bit integer to a changegroup

> int sqlite3changegroup_change_int64(\
>   sqlite3_changegroup\*, \
>   int bNew,\
>   int iCol,\
>   sqlite3_int64 iVal\
> );\

This function may only be called between a successful call to sqlite3changegroup_change_begin() and its matching sqlite3changegroup_change_finish() call. If it is called at any other time, it is an SQLITE_MISUSE error. Calling this function specifies a 64-bit integer value to be used in the change currently being added to the changegroup object passed as the first argument.

The second parameter, bNew, specifies whether the value is to be part of the new.\* (if bNew is non-zero) or old.\* (if bNew is zero) record of the change under construction. If this does not match the type of change specified by the preceding call to sqlite3changegroup_change_begin() (i.e. an old.\* value for an SQLITE_INSERT change, or a new.\* value for an SQLITE_DELETE), then SQLITE_ERROR is returned.

The third parameter specifies the column of the old.\* or new.\* record that the value will be a part of. If the specified table has an explicit primary key, then this is the index of the table column, numbered from 0 in the order specified within the CREATE TABLE statement. Or, if the table uses an implicit rowid key, then the column 0 is the rowid and the explicit columns are numbered starting from 1. If the iCol parameter is less than 0 or greater than the index of the last column in the table, SQLITE_RANGE is returned.

The fourth parameter is the integer value to use as part of the old.\* or new.\* record.

If this call is successful, SQLITE_OK is returned. Otherwise, if an error occurs, an SQLite error code is returned.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
