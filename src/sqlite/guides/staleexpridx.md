---
title: Stale Expression Indexes
source_url: https://www.sqlite.org/staleexpridx.html
source_path: staleexpridx.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 7310
---

# 1. Overview

An [expression index](expridx.md) is an [index](lang_createindex.md) on either a [VIRTUAL generated column](gencol.md#vgc*) or on an expression of table columns. Expression indexes are different in that one or more of their key values is the result of computing an expression rather than just making a copy of a column from the table being indexed.

In order for the index to work correctly, the value of the expression must not change as long as the corresponding table row is unchanged. Hence, indexed expressions must use [deterministic functions](deterministic.md) - functions that always return the same output given the same inputs. Deterministic functions are things like "abs(X)" and "concat(X,Y)". Non-deterministic functions are things like "datetime('now')" and "random()".

Sometimes functions that are identified as "deterministic" are not completely deterministic across different CPU architectures, operating systems, and/or SQLite versions. When that happens, an expression index created on one CPU/OS/SQLite-version might be incorrect on a different CPU/OS/SQLite-version. We call this a "**stale expression index**".

Stale expression indexes rarely occur. All known occurrences involve indexes on floating-point values plus one of the following circumstances:

- The SQLite database is moved from one CPU architecture to another (example: x86_64 to ARM),
- The SQLite database is moved from one operating system to another (example: Windows to Mac)
- There is a version change in the SQLite library and/or an external library that SQLite uses to implement SQL functions.

# 2. Deterministic Functions That Are Not Always 100% Deterministic

A deterministic function is supposed to give the same result always, even when run on different platforms and in different versions of SQLite. But sometimes, rarely, moving from one operating system to another, or when changing from one version of SQLite to another, the output from a supposedly deterministic function can change slightly. Some examples of when this might happen:

1.  The transcendental SQL math functions work by calling the corresponding system C-library functions. So for example, the "sin(X)" SQL function just invokes the sin() function in the standard C math library. The various C math libraries in use today are remarkably consistent. Nevertheless there is nothing in the C-language standards that requires sin(X) to return exactly the same value from one system to another. The sin(X) only needs to return a number that is "close" (within one or two [ULPs](https://en.wikipedia.org/wiki/Unit_in_the_last_place) of the correct value) in order to be considered "correct".

2.  Suppose you are using the [ICU](https://github.com/unicode-org/icu) extension function "lower()" and linking against your systems libicu.so. Then an upgrade happens that converts your system libicu.so to a newer version, possibly on a different version of Unicode. The outputs from the lower() function might change, slightly, in extreme corner cases.

3.  Sometimes built-in functions in SQLite get bug fixes or upgrades that can change their behavior ever so slightly in extreme corner cases - sometimes without the developers even being aware of the change.

4.  If the database is using an [application-defined SQL function](appfunc.md) (ADF), and there is a bug fix or enhancement to that ADF, the values returned might be different.

A notable instance of case 3 is when the internal text→float conversion routines in SQLite get upgraded for improved accuracy and/or performance, such as happened when moving from version 3.42 to 3.43 and again going from 3.51 to 3.52. There need not be an explicit "`CAST(... AS REAL)`" to force a text→float conversion. The conversion might happen due to automatic type coercion. Another common "hidden" text→float conversion happens when using [the -\>\> operator](json1.md#jptr) to extract a floating-point value out of a JSON document. Suppose you want the ability to search a large corpus of JSON documents according to a range of the "mtime" values, which is a floating point number of seconds since the Unix epoch. You might write:

CREATE INDEX doc_mtime ON docstore(doc-\>\>'mtime');\

Then if you switch from one version of SQLite to another that implements text→float conversion differently, you might sometimes get a value from the "`doc->>'mtime'`" expression that is one ULP different from the value stored in the index.

When the value computed for the expression of an expression index differs from the value actually stored in the index and used as an index key, we call that a "**stale expression index**".

# 3. Are Stale Expression Indexes Really A Problem?

Stale expression indexes rarely occur. You are unlikely to ever encounter one in practice.

Back in 2023, almost three years before the SQLite developers realized that stale expression indexes might exist and might cause concerns, there was an update to text→float conversion logic inside of SQLite that caused some floating-point value computations to shift by one ULP. This change will cause stale expression indexes. (We know, because we have gone back and tried it.) And yet, even though that change went into billions and billions of phones and personal computers, the SQLite developers never received a single report of index corruption because of it.

Stale expression indexes usually do not cause problems for the application even when they do occur. If the stale value is a floating-point number that is off by one ULP (the only case ever actually observed in the wild), then the error does not normally cause problems for search. You can get differing results when the anomolous entry is right at the boundary of the search range, but [floating point values are approximations](floatingpoint.md#fpapprox) - close approximations to be sure, but approximations all the same - so missing an entry that occurs right at the boundary of a search is usually not considered a problem.

Trying to DELETE or UPDATE a row that has a stale expression index entry will cause an error in older versions of SQLite (but not with SQLite 3.53.0 (2026-04-09) or later - see below) and errors will appear when running [PRAGMA integrity_check](pragma.md#pragma_integrity_check). But such problems can be easily cleared by running [REINDEX](lang_reindex.md). If users in the field ever encountered such problems, they never told the SQLite developers about them.

In summary then, stale expression indexes rarely occur, and when they do occur, they are not fatal to the application. Those who aspire to be SQLite experts should be aware of stale expression indexes, but for the average developer, stale expression indexes should never be an issue. <span id="selfheal"></span>

# 4. Self-Healing Expression Indexes

Beginning with SQLite version 3.53.0 (2026-04-09), SQLite attempts to fix stale expression indexes automatically in some circumstances. When attempting to DELETE or UPDATE a table row that is associated with a stale expression index entry, instead of raising an error, SQLite now fixes the index. No errors are raised. The application never knows that something was ever amiss.

The [PRAGMA integrity_check](pragma.md#pragma_integrity_check) command still reports stale index entries in its output. But in the common case that the stale entry is a floating-point number that is only off by one or two ULPs, then instead of saying that the index is corrupt, the message emitted by PRAGMA integrity_check says something like:

> \
> index NAME stores an imprecise floating-point value for row N\

# 5. How To Avoid And/Or Fix Stale Expression Indexes

If you never want there to be any possibility of encountering a stale expression index, then don't use expression indexes. A good alternative is to create [STORED generated columns](gencol.md#vgc*) for expressions that you want to compute automatically, and then create indexes on those STORED generated columns.

The doc_mtime index example shown above would change to be something like the following:

CREATE TABLE doc(\
  doc JSON,\
  mtime AS (doc-\>\>'mtime') STORED\
);\
CREATE INDEX doc_mtime ON doc(mtime);\

If you have a database that you did not design and just want to know which indexes are expression indexes, you can bring the database up in the [CLI](cli.md) (version 3.53.0 or later) and type the command:

.indexes --expr\

If you think you have stale expression indexes (maybe you know that you changed an [ADF](appfunc.md) that is used in an index expression) then you can refresh all your indexes by running the [REINDEX](lang_reindex.md) command. Since SQLite version 3.53.0 (2026-04-09) you can save time and I/O by running:

REINDEX EXPRESSIONS;\

The REINDEX EXPRESSIONS command rebuilds only expression indexes and leaves other indexes unchanged. If the database has no expression indexes (the usual case), then REINDEX EXPRESSIONS is a no-op.
