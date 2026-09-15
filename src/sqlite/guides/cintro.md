---
title: An Introduction To The SQLite C/C++ Interface
source_url: https://www.sqlite.org/cintro.html
source_path: cintro.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2450
---

# 1. Summary

The following two objects and eight methods comprise the essential elements of the SQLite interface:

- **[sqlite3](c3ref/sqlite3.md)** → The database connection object. Created by [sqlite3_open()](c3ref/open.md) and destroyed by [sqlite3_close()](c3ref/close.md).

- **[sqlite3_stmt](c3ref/stmt.md)** → The prepared statement object. Created by [sqlite3_prepare()](c3ref/prepare.md) and destroyed by [sqlite3_finalize()](c3ref/finalize.md).

- **[sqlite3_open()](c3ref/open.md)** → Open a connection to a new or existing SQLite database. The constructor for [sqlite3](c3ref/sqlite3.md).

- **[sqlite3_prepare()](c3ref/prepare.md)** → Compile SQL text into byte-code that will do the work of querying or updating the database. The constructor for [sqlite3_stmt](c3ref/stmt.md).

- **[sqlite3_bind()](c3ref/bind_blob.md)** → Store application data into [parameters](lang_expr.md#varparam) of the original SQL.

- **[sqlite3_step()](c3ref/step.md)** → Advance an [sqlite3_stmt](c3ref/stmt.md) to the next result row or to completion.

- **[sqlite3_column()](c3ref/column_blob.md)** → Column values in the current result row for an [sqlite3_stmt](c3ref/stmt.md).

- **[sqlite3_finalize()](c3ref/finalize.md)** → Destructor for [sqlite3_stmt](c3ref/stmt.md).

- **[sqlite3_close()](c3ref/close.md)** → Destructor for [sqlite3](c3ref/sqlite3.md).

- **[sqlite3_exec()](c3ref/exec.md)** → A wrapper function that does [sqlite3_prepare()](c3ref/prepare.md), [sqlite3_step()](c3ref/step.md), [sqlite3_column()](c3ref/column_blob.md), and [sqlite3_finalize()](c3ref/finalize.md) for a string of one or more SQL statements.

# 2. Introduction

SQLite has more than 225 APIs. However, most of the APIs are optional and very specialized and can be ignored by beginners. The core API is small, simple, and easy to learn. This article summarizes the core API.

A separate document, [The SQLite C/C++ Interface](c3ref/intro.md), provides detailed specifications for all C/C++ APIs for SQLite. Once the reader understands the basic principles of operation for SQLite, [that document](c3ref/intro.md) should be used as a reference guide. This article is intended as introduction only and is neither a complete nor authoritative reference for the SQLite API.

# 3. Core Objects And Interfaces

The principal task of an SQL database engine is to evaluate SQL statements of SQL. To accomplish this, the developer needs two objects:

- The [database connection](c3ref/sqlite3.md) object: sqlite3
- The [prepared statement](c3ref/stmt.md) object: sqlite3_stmt

Strictly speaking, the [prepared statement](c3ref/stmt.md) object is not required since the convenience wrapper interfaces, [sqlite3_exec](c3ref/exec.md) or [sqlite3_get_table](c3ref/free_table.md), can be used and these convenience wrappers encapsulate and hide the [prepared statement](c3ref/stmt.md) object. Nevertheless, an understanding of [prepared statements](c3ref/stmt.md) is needed to make full use of SQLite.

The [database connection](c3ref/sqlite3.md) and [prepared statement](c3ref/stmt.md) objects are controlled by a small set of C/C++ interface routines listed below.

- [sqlite3_open()](c3ref/open.md)
- [sqlite3_prepare()](c3ref/prepare.md)
- [sqlite3_step()](c3ref/step.md)
- [sqlite3_column()](c3ref/column_blob.md)
- [sqlite3_finalize()](c3ref/finalize.md)
- [sqlite3_close()](c3ref/close.md)

Note that the list of routines above is conceptual rather than actual. Many of these routines come in multiple versions. For example, the list above shows a single routine named [sqlite3_open()](c3ref/open.md) when in fact there are three separate routines that accomplish the same thing in slightly different ways: [sqlite3_open()](c3ref/open.md), [sqlite3_open16()](c3ref/open.md) and [sqlite3_open_v2()](c3ref/open.md). The list mentions [sqlite3_column()](c3ref/column_blob.md) when in fact no such routine exists. The "sqlite3_column()" shown in the list is a placeholder for an entire family of routines that extract column data in various datatypes.

Here is a summary of what the core interfaces do:

- **[sqlite3_open()](c3ref/open.md)**

  This routine opens a connection to an SQLite database file and returns a [database connection](c3ref/sqlite3.md) object. This is often the first SQLite API call that an application makes and is a prerequisite for most other SQLite APIs. Many SQLite interfaces require a pointer to the [database connection](c3ref/sqlite3.md) object as their first parameter and can be thought of as methods on the [database connection](c3ref/sqlite3.md) object. This routine is the constructor for the [database connection](c3ref/sqlite3.md) object.

- **[sqlite3_prepare()](c3ref/prepare.md)**

  This routine converts SQL text into a [prepared statement](c3ref/stmt.md) object and returns a pointer to that object. This interface requires a [database connection](c3ref/sqlite3.md) pointer created by a prior call to [sqlite3_open()](c3ref/open.md) and a text string containing the SQL statement to be prepared. This API does not actually evaluate the SQL statement. It merely prepares the SQL statement for evaluation.

  Think of each SQL statement as a small computer program. The purpose of [sqlite3_prepare()](c3ref/prepare.md) is to compile that program into object code. The [prepared statement](c3ref/stmt.md) is the object code. The [sqlite3_step()](c3ref/step.md) interface then runs the object code to get a result.

  New applications should always invoke [sqlite3_prepare_v2()](c3ref/prepare.md) instead of [sqlite3_prepare()](c3ref/prepare.md). The older [sqlite3_prepare()](c3ref/prepare.md) is retained for backwards compatibility. But [sqlite3_prepare_v2()](c3ref/prepare.md) provides a much better interface.

- **[sqlite3_step()](c3ref/step.md)**

  This routine is used to evaluate a [prepared statement](c3ref/stmt.md) that has been previously created by the [sqlite3_prepare()](c3ref/prepare.md) interface. The statement is evaluated up to the point where the first row of results are available. To advance to the second row of results, invoke [sqlite3_step()](c3ref/step.md) again. Continue invoking [sqlite3_step()](c3ref/step.md) until the statement is complete. Statements that do not return results (ex: INSERT, UPDATE, or DELETE statements) run to completion on a single call to [sqlite3_step()](c3ref/step.md).

- **[sqlite3_column()](c3ref/column_blob.md)**

  This routine returns a single column from the current row of a result set for a [prepared statement](c3ref/stmt.md) that is being evaluated by [sqlite3_step()](c3ref/step.md). Each time [sqlite3_step()](c3ref/step.md) stops with a new result set row, this routine can be called multiple times to find the values of all columns in that row.

  As noted above, there really is no such thing as a "sqlite3_column()" function in the SQLite API. Instead, what we here call "sqlite3_column()" is a place-holder for an entire family of functions that return a value from the result set in various data types. There are also routines in this family that return the size of the result (if it is a string or BLOB) and the number of columns in the result set.

  - [sqlite3_column_blob()](c3ref/column_blob.md)
  - [sqlite3_column_bytes()](c3ref/column_blob.md)
  - [sqlite3_column_bytes16()](c3ref/column_blob.md)
  - [sqlite3_column_count()](c3ref/column_count.md)
  - [sqlite3_column_double()](c3ref/column_blob.md)
  - [sqlite3_column_int()](c3ref/column_blob.md)
  - [sqlite3_column_int64()](c3ref/column_blob.md)
  - [sqlite3_column_text()](c3ref/column_blob.md)
  - [sqlite3_column_text16()](c3ref/column_blob.md)
  - [sqlite3_column_type()](c3ref/column_blob.md)
  - [sqlite3_column_value()](c3ref/column_blob.md)

- **[sqlite3_finalize()](c3ref/finalize.md)**

  This routine destroys a [prepared statement](c3ref/stmt.md) created by a prior call to [sqlite3_prepare()](c3ref/prepare.md). Every prepared statement must be destroyed using a call to this routine in order to avoid memory leaks.

- **[sqlite3_close()](c3ref/close.md)**

  This routine closes a [database connection](c3ref/sqlite3.md) previously opened by a call to [sqlite3_open()](c3ref/open.md). All [prepared statements](c3ref/stmt.md) associated with the connection should be [finalized](c3ref/finalize.md) prior to closing the connection.

# 4. Typical Usage Of Core Routines And Objects

An application will typically use [sqlite3_open()](c3ref/open.md) to create a single [database connection](c3ref/sqlite3.md) during initialization. Note that [sqlite3_open()](c3ref/open.md) can be used to either open existing database files or to create and open new database files. While many applications use only a single [database connection](c3ref/sqlite3.md), there is no reason why an application cannot call [sqlite3_open()](c3ref/open.md) multiple times in order to open multiple [database connections](c3ref/sqlite3.md) - either to the same database or to different databases. Sometimes a multi-threaded application will create separate [database connections](c3ref/sqlite3.md) for each thread. Note that a single [database connection](c3ref/sqlite3.md) can access two or more databases using the [ATTACH](lang_attach.md) SQL command, so it is not necessary to have a separate database connection for each database file.

Many applications destroy their [database connections](c3ref/sqlite3.md) using calls to [sqlite3_close()](c3ref/close.md) at shutdown. Or, for example, an application that uses SQLite as its [application file format](appfileformat.md) might open [database connections](c3ref/sqlite3.md) in response to a File/Open menu action and then destroy the corresponding [database connection](c3ref/sqlite3.md) in response to the File/Close menu.

To run an SQL statement, the application follows these steps:

1.  Create a [prepared statement](c3ref/stmt.md) using [sqlite3_prepare()](c3ref/prepare.md).
2.  Evaluate the [prepared statement](c3ref/stmt.md) by calling [sqlite3_step()](c3ref/step.md) one or more times.
3.  For queries, extract results by calling [sqlite3_column()](c3ref/column_blob.md) in between two calls to [sqlite3_step()](c3ref/step.md).
4.  Destroy the [prepared statement](c3ref/stmt.md) using [sqlite3_finalize()](c3ref/finalize.md).

The foregoing is all one really needs to know in order to use SQLite effectively. All the rest is optimization and detail.

# 5. Convenience Wrappers Around Core Routines

The [sqlite3_exec()](c3ref/exec.md) interface is a convenience wrapper that carries out all four of the above steps with a single function call. A callback function passed into [sqlite3_exec()](c3ref/exec.md) is used to process each row of the result set. The [sqlite3_get_table()](c3ref/free_table.md) is another convenience wrapper that does all four of the above steps. The [sqlite3_get_table()](c3ref/free_table.md) interface differs from [sqlite3_exec()](c3ref/exec.md) in that it stores the results of queries in heap memory rather than invoking a callback.

It is important to realize that neither [sqlite3_exec()](c3ref/exec.md) nor [sqlite3_get_table()](c3ref/free_table.md) do anything that cannot be accomplished using the core routines. In fact, these wrappers are implemented purely in terms of the core routines.

# 6. Binding Parameters and Reusing Prepared Statements

In prior discussion, it was assumed that each SQL statement is prepared once, evaluated, then destroyed. However, SQLite allows the same [prepared statement](c3ref/stmt.md) to be evaluated multiple times. This is accomplished using the following routines:

- [sqlite3_reset()](c3ref/reset.md)
- [sqlite3_bind()](c3ref/bind_blob.md)

After a [prepared statement](c3ref/stmt.md) has been evaluated by one or more calls to [sqlite3_step()](c3ref/step.md), it can be reset in order to be evaluated again by a call to [sqlite3_reset()](c3ref/reset.md). Think of [sqlite3_reset()](c3ref/reset.md) as rewinding the [prepared statement](c3ref/stmt.md) program back to the beginning. Using [sqlite3_reset()](c3ref/reset.md) on an existing [prepared statement](c3ref/stmt.md) rather than creating a new [prepared statement](c3ref/stmt.md) avoids unnecessary calls to [sqlite3_prepare()](c3ref/prepare.md). For many SQL statements, the time needed to run [sqlite3_prepare()](c3ref/prepare.md) equals or exceeds the time needed by [sqlite3_step()](c3ref/step.md). So avoiding calls to [sqlite3_prepare()](c3ref/prepare.md) can give a significant performance improvement.

It is not commonly useful to evaluate the *exact* same SQL statement more than once. More often, one wants to evaluate similar statements. For example, you might want to evaluate an INSERT statement multiple times with different values. Or you might want to evaluate the same query multiple times using a different key in the WHERE clause. To accommodate this, SQLite allows SQL statements to contain [parameters](lang_expr.md#varparam) which are "bound" to values prior to being evaluated. These values can later be changed and the same [prepared statement](c3ref/stmt.md) can be evaluated a second time using the new values.

SQLite allows a [parameter](lang_expr.md#varparam) wherever a string literal, blob literal, numeric constant, or NULL is allowed in queries or data modification statements. (DQL or DML) (Parameters may not be used for column or table names, or as values for constraints or default values. (DDL)) A [parameter](lang_expr.md#varparam) takes one of the following forms:

- **?**
- **?***NNN*
- **:***AAA*
- **\$***AAA*
- **@***AAA*

In the examples above, *NNN* is an integer value and *AAA* is an identifier. A parameter initially has a value of NULL. Prior to calling [sqlite3_step()](c3ref/step.md) for the first time or immediately after [sqlite3_reset()](c3ref/reset.md), the application can invoke the [sqlite3_bind()](c3ref/bind_blob.md) interfaces to attach values to the parameters. Each call to [sqlite3_bind()](c3ref/bind_blob.md) overrides prior bindings on the same parameter.

An application is allowed to prepare multiple SQL statements in advance and evaluate them as needed. There is no arbitrary limit to the number of outstanding [prepared statements](c3ref/stmt.md). Some applications call [sqlite3_prepare()](c3ref/prepare.md) multiple times at start-up to create all of the [prepared statements](c3ref/stmt.md) they will ever need. Other applications keep a cache of the most recently used [prepared statements](c3ref/stmt.md) and then reuse [prepared statements](c3ref/stmt.md) out of the cache when available. Another approach is to only reuse [prepared statements](c3ref/stmt.md) when they are inside of a loop.

# 7. Configuring SQLite

The default configuration for SQLite works great for most applications. But sometimes developers want to tweak the setup to try to squeeze out a little more performance, or take advantage of some obscure feature.

The [sqlite3_config()](c3ref/config.md) interface is used to make global, process-wide configuration changes for SQLite. The [sqlite3_config()](c3ref/config.md) interface must be called before any [database connections](c3ref/sqlite3.md) are created. The [sqlite3_config()](c3ref/config.md) interface allows the programmer to do things like:

- Adjust how SQLite does [memory allocation](malloc.md), including setting up alternative memory allocators appropriate for safety-critical real-time embedded systems and application-defined memory allocators.
- Set up a process-wide [error log](errlog.md).
- Specify an application-defined page cache.
- Adjust the use of mutexes so that they are appropriate for various [threading models](threadsafe.md), or substitute an application-defined mutex system.

After process-wide configuration is complete and [database connections](c3ref/sqlite3.md) have been created, individual database connections can be configured using calls to [sqlite3_limit()](c3ref/limit.md) and [sqlite3_db_config()](c3ref/db_config.md).

# 8. Extending SQLite

SQLite includes interfaces that can be used to extend its functionality. Such routines include:

- [sqlite3_create_collation()](c3ref/create_collation.md)
- [sqlite3_create_function()](c3ref/create_function.md)
- [sqlite3_create_module()](c3ref/create_module.md)
- [sqlite3_vfs_register()](c3ref/vfs_find.md)

The [sqlite3_create_collation()](c3ref/create_collation.md) interface is used to create new [collating sequences](datatype3.md#collation) for sorting text. The [sqlite3_create_module()](c3ref/create_module.md) interface is used to register new [virtual table](vtab.md) implementations. The [sqlite3_vfs_register()](c3ref/vfs_find.md) interface creates new [VFSes](vfs.md).

The [sqlite3_create_function()](c3ref/create_function.md) interface creates new SQL functions - either scalar or aggregate. The new function implementation typically makes use of the following additional interfaces:

- [sqlite3_aggregate_context()](c3ref/aggregate_context.md)
- [sqlite3_result()](c3ref/result_blob.md)
- [sqlite3_user_data()](c3ref/user_data.md)
- [sqlite3_value()](c3ref/value_blob.md)

All of the built-in SQL functions of SQLite are created using exactly these same interfaces. Refer to the SQLite source code, and in particular the [date.c](https://sqlite.org/src/doc/trunk/src/date.c) and [func.c](https://sqlite.org/src/doc/trunk/src/func.c) source files for examples.

Shared libraries or DLLs can be used as [loadable extensions](loadext.md) to SQLite.

# 9. Other Interfaces

This article only mentions the most important and most commonly used SQLite interfaces. The SQLite library includes many other APIs implementing useful features that are not described here. A [complete list of functions](c3ref/funclist.md) that form the SQLite application programming interface is found at the [C/C++ Interface Specification](c3ref/intro.md). Refer to that document for complete and authoritative information about all SQLite interfaces.
