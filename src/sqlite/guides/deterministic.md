---
title: Deterministic SQL Functions
source_url: https://www.sqlite.org/deterministic.html
source_path: deterministic.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2690
---

# 1. Overview

SQL functions in SQLite can be either "deterministic" or "non-deterministic".

A deterministic function always gives the same answer when it has the same inputs. Most built-in SQL functions in SQLite are deterministic. For example, the [abs(X)](lang_corefunc.md#abs) function always returns the same answer as long as its input X is the same.

Non-deterministic functions might give different answers on each invocation, even if the arguments are always the same. The following are examples of non-deterministic functions:

- [random()](lang_corefunc.md#random)
- [changes()](lang_corefunc.md#changes)
- [last_insert_rowid()](lang_corefunc.md#last_insert_rowid)
- [sqlite3_version()](c3ref/libversion.md)

The [random()](lang_corefunc.md#random) function is obviously non-deterministic because it gives a different answer every time it is invoked. The answers from [changes()](lang_corefunc.md#changes) and [last_insert_rowid()](lang_corefunc.md#last_insert_rowid) depend on prior SQL statements, and so they are also non-deterministic. The [sqlite3_version()](c3ref/libversion.md) function is mostly constant, but it can change when SQLite is upgraded, and so even though it always returns the same answer for any particular session, because it can change answers across sessions it is still considered non-deterministic.

# 2. Restrictions on the use of non-deterministic functions

There are some contexts in SQLite that do not allow the use of non-deterministic functions:

- In the expression of a [CHECK constraint](lang_createtable.md#ckconst). *← see 2.1 below*
- In the WHERE clause of a [partial index](partialindex.md).
- In an expression used as part of an [expression index](expridx.md).
- In the expression of a [generated column](gencol.md).

In the cases above, the values returned by the function affects the information stored in the database file. The values of functions in CHECK constraints determines which entries are valid for a table, and functions in the WHERE clause of a partial index or in an index on an expression compute values stored in the index b-tree. If any of these functions later returns a different value, then the database might no longer be well-formed. Hence, to avoid database corruption, only deterministic functions can be used in the contexts above.

## 2.1. Historical exception for CHECK constraints

It is stated above that non-deterministic functions are not allowed in CHECK constraints. That really ought to be the case, but due to an historical bug and the desire to maintain backwards compatibility, that restriction is not actually enforced. You can put a non-deterministic function inside of a CHECK constraints and SQLite will not complain. Doing so will not cause a crash or memory error. But apart from not crashing, no guarantees are made about how that CHECK constraint will function. You ought not do this. If you ignore this advice and you get unexpected behavior, that will not be considered a bug (unless it crashes, as crashes are always considered bugs). <span id="dtexception"></span>

# 3. Special-case Processing For Date/Time Functions

The built-in [date and time functions](lang_datefunc.md) of SQLite are a special case. These functions are usually considered deterministic. However, if these functions use the string "now" as the date, or if they use the [localtime modifier](lang_datefunc.md#localtime) or the [utc modifier](lang_datefunc.md#localtime), then they are considered non-deterministic. Because the function inputs are not necessarily known until run-time, the date/time functions will throw an exception if they encounter any of the non-deterministic features in a context where only deterministic functions are allowed.

Prior to SQLite 3.20.0 (2017-08-01) all date/time functions were always considered non-deterministic. The ability for date/time functions to be deterministic sometimes and non-deterministic at other times, depending on their arguments, was added for the 3.20.0 release.

## 3.1. Bug fix in version 3.35.2

When the enhancement was made to SQLite 3.20.0 such that date/time functions would be considered deterministic as they do not depend on the current time, one case was overlooked: Many of the date/time functions can be called with no arguments at all. These no-argument date/time functions behave as if they had a single "`'now'`" argument. Thus "`datetime()`" and "`datetime('now')`" both yield the current date and time. However, only the second form was recognized as non-deterministic. This meant that developers could sneak the non-deterministic "`datetime()`" form into CHECK constraints, index expressions, generated column expressions, and similar places where non-deterministic functions make no sense. This oversight was fixed in version 3.35.2 (2021-03-17). However, there may be legacy databases in circulation that were created by SQLite version 3.20.0 through 3.35.1 that have non-deterministic date/time functions in their schemas.

# 4. Application-defined deterministic functions

By default, [application-defined SQL functions](appfunc.md) are considered to be non-deterministic. However, if the 4th parameter to [sqlite3_create_function_v2()](c3ref/create_function.md) is OR-ed with [SQLITE_DETERMINISTIC](c3ref/c_deterministic.md#sqlitedeterministic), then SQLite will treat that function as if it were deterministic.

Note that if a non-deterministic function is tagged with [SQLITE_DETERMINISTIC](c3ref/c_deterministic.md#sqlitedeterministic) and if that function ends up being used in the WHERE clause of a [partial index](partialindex.md) or in an [expression index](expridx.md), then when the function begins to return different answers, the associated index may become corrupt. If an SQL function is nearly deterministic (which is to say, if it only rarely changes, like [sqlite_version()](lang_corefunc.md#sqlite_version)) and it is used in an index that becomes corrupt, the corruption can be fixed by running [REINDEX](lang_reindex.md).

The interfaces necessary to construct a function that is sometimes deterministic and sometimes non-deterministic depending on their inputs, such as the built-in date/time functions, are not published. Generic [application-defined SQL functions](appfunc.md) must be always deterministic or always non-deterministic.
