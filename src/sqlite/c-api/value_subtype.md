---
title: Finding The Subtype Of SQL Values
source_url: https://www.sqlite.org/c3ref/value_subtype.html
source_path: c3ref/value_subtype.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2210
---

> \
> unsigned int sqlite3_value_subtype(sqlite3_value\*);\

The sqlite3_value_subtype(V) function returns the subtype for an [application-defined SQL function](../appfunc.md) argument V. The subtype information can be used to pass a limited amount of context from one SQL function to another. Use the [sqlite3_result_subtype()](../c3ref/result_subtype.md) routine to set the subtype for the return value of an SQL function.

Every [application-defined SQL function](../appfunc.md) that invokes this interface should include the [SQLITE_SUBTYPE](../c3ref/c_deterministic.md#sqlitesubtype) property in the text encoding argument when the function is [registered](../c3ref/create_function.md). If the [SQLITE_SUBTYPE](../c3ref/c_deterministic.md#sqlitesubtype) property is omitted, then sqlite3_value_subtype() might return zero instead of the upstream subtype in some corner cases.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
