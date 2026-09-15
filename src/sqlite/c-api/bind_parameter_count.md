---
title: Number Of SQL Parameters
source_url: https://www.sqlite.org/c3ref/bind_parameter_count.html
source_path: c3ref/bind_parameter_count.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 280
---

> \
> int sqlite3_bind_parameter_count(sqlite3_stmt\*);\

This routine can be used to find the number of [SQL parameters](../c3ref/bind_blob.md) in a [prepared statement](../c3ref/stmt.md). SQL parameters are tokens of the form "?", "?NNN", ":AAA", "\$AAA", or "@AAA" that serve as placeholders for values that are [bound](../c3ref/bind_blob.md) to the parameters at a later time.

This routine actually returns the index of the largest (rightmost) parameter. For all forms except ?NNN, this will correspond to the number of unique parameters. If parameters of the ?NNN form are used, there may be gaps in the list.

See also: [sqlite3_bind()](../c3ref/bind_blob.md), [sqlite3_bind_parameter_name()](../c3ref/bind_parameter_name.md), and [sqlite3_bind_parameter_index()](../c3ref/bind_parameter_index.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
