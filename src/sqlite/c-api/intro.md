---
title: Introduction
source_url: https://www.sqlite.org/c3ref/intro.html
source_path: c3ref/intro.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1400
---

# C-language Interface Specification for SQLite

These pages are intended to be a precise and detailed specification. For a tutorial introduction, see instead:

- [SQLite In 5 Minutes Or Less](../quickstart.md) and/or
- the [Introduction To The SQLite C/C++ Interface](../cintro.md).

This same content is also available as a [single large HTML file](../capi3ref.md).

The SQLite interface elements can be grouped into three categories:

1.  [**List Of Objects.**](../c3ref/objlist.md) This is a list of all abstract objects and datatypes used by the SQLite library. There are a couple of dozen objects in total, but the two most important objects are: A database connection object [sqlite3](../c3ref/sqlite3.md), and the prepared statement object [sqlite3_stmt](../c3ref/stmt.md).

2.  [**List Of Constants.**](../c3ref/constlist.md) This is a list of numeric constants used by SQLite and represented by \#defines in the sqlite3.h header file. These constants are things such as numeric [result codes](../rescode.md) from various interfaces (ex: [SQLITE_OK](../rescode.md#ok)) or flags passed into functions to control behavior (ex: [SQLITE_OPEN_READONLY](../c3ref/c_open_autoproxy.md)).

3.  [**List Of Functions.**](../c3ref/funclist.md) This is a list of all functions and methods operating on the [objects](../c3ref/objlist.md) and using and/or returning [constants](../c3ref/constlist.md). There are many functions, but most applications only use a handful.
