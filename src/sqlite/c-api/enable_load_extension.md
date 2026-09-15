---
title: Enable Or Disable Extension Loading
source_url: https://www.sqlite.org/c3ref/enable_load_extension.html
source_path: c3ref/enable_load_extension.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1170
---

> \
> int sqlite3_enable_load_extension(sqlite3 \*db, int onoff);\

So as not to open security holes in older applications that are unprepared to deal with [extension loading](../loadext.md), and as a means of disabling [extension loading](../loadext.md) while evaluating user-entered SQL, the following API is provided to turn the [sqlite3_load_extension()](../c3ref/load_extension.md) mechanism on and off.

Extension loading is off by default. Call the sqlite3_enable_load_extension() routine with onoff==1 to turn extension loading on and call it with onoff==0 to turn it back off again.

This interface enables or disables both the C-API [sqlite3_load_extension()](../c3ref/load_extension.md) and the SQL function [load_extension()](../lang_corefunc.md#load_extension). Use [sqlite3_db_config](../c3ref/db_config.md)(db,[SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableloadextension),..) to enable or disable only the C-API.

**Security warning:** It is recommended that extension loading be enabled using the [SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableloadextension) method rather than this interface, so the [load_extension()](../lang_corefunc.md#load_extension) SQL function remains disabled. This will prevent SQL injections from giving attackers access to extension loading capabilities.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
