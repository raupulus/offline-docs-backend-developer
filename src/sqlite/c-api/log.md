---
title: Error Logging Interface
source_url: https://www.sqlite.org/c3ref/log.html
source_path: c3ref/log.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1470
---

> \
> void sqlite3_log(int iErrCode, const char \*zFormat, ...);\

The [sqlite3_log()](../c3ref/log.md) interface writes a message into the [error log](../errlog.md) established by the [SQLITE_CONFIG_LOG](../c3ref/c_config_covering_index_scan.md#sqliteconfiglog) option to [sqlite3_config()](../c3ref/config.md). If logging is enabled, the zFormat string and subsequent arguments are used with [sqlite3_snprintf()](../c3ref/mprintf.md) to generate the final output string.

The sqlite3_log() interface is intended for use by extensions such as virtual tables, collating functions, and SQL functions. While there is nothing to prevent an application from calling sqlite3_log(), doing so is considered bad form.

The zFormat string must not be NULL.

To avoid deadlocks and other threading problems, the sqlite3_log() routine will not use dynamically allocated memory. The log message is stored in a fixed-length buffer on the stack. If the log message is longer than a few hundred characters, it will be truncated to the length of the buffer.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
