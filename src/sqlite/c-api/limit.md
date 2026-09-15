---
title: Run-time Limits
source_url: https://www.sqlite.org/c3ref/limit.html
source_path: c3ref/limit.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1450
---

> \
> int sqlite3_limit(sqlite3\*, int id, int newVal);\

This interface allows the size of various constructs to be limited on a connection by connection basis. The first parameter is the [database connection](../c3ref/sqlite3.md) whose limit is to be set or queried. The second parameter is one of the [limit categories](../c3ref/c_limit_attached.md) that define a class of constructs to be size limited. The third parameter is the new limit for that construct.

If the new limit is a negative number, the limit is unchanged. For each limit category SQLITE_LIMIT\_*NAME* there is a [hard upper bound](../limits.md) set at compile-time by a C preprocessor macro called [SQLITE_MAX\_*NAME*](../limits.md). (The "\_LIMIT\_" in the name is changed to "\_MAX\_".) Attempts to increase a limit above its hard upper bound are silently truncated to the hard upper bound.

Regardless of whether or not the limit was changed, the [sqlite3_limit()](../c3ref/limit.md) interface returns the prior value of the limit. Hence, to find the current value of a limit without changing it, simply invoke this interface with the third parameter set to -1.

Run-time limits are intended for use in applications that manage both their own internal database and also databases that are controlled by untrusted external sources. An example application might be a web browser that has its own databases for storing history and separate databases controlled by JavaScript applications downloaded off the Internet. The internal databases can be given the large, default limits. Databases managed by external sources can be given much smaller limits designed to prevent a denial of service attack. Developers might also want to use the [sqlite3_set_authorizer()](../c3ref/set_authorizer.md) interface to further control untrusted SQL. The size of the database created by an untrusted script can be contained using the [max_page_count](../pragma.md#pragma_max_page_count) [PRAGMA](../pragma.md#syntax).

New run-time limit categories may be added in future releases.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
