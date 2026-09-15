---
title: Load An Extension
source_url: https://www.sqlite.org/c3ref/load_extension.html
source_path: c3ref/load_extension.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1460
---

> \
> int sqlite3_load_extension(\
>   sqlite3 \*db,          /\* Load the extension into this database connection \*/\
>   const char \*zFile,    /\* Name of the shared library containing extension \*/\
>   const char \*zProc,    /\* Entry point.  Derived from zFile if 0 \*/\
>   char \*\*pzErrMsg       /\* Put error message here if not 0 \*/\
> );\

This interface loads an SQLite extension library from the named file.

The sqlite3_load_extension() interface attempts to load an [SQLite extension](../loadext.md) library contained in the file zFile. If the file cannot be loaded directly, attempts are made to load with various operating-system specific filename extensions added. So for example, if "samplelib" cannot be loaded, then names like "samplelib.so" or "samplelib.dylib" or "samplelib.dll" might be tried also.

The entry point is zProc. zProc may be 0, in which case SQLite will try to come up with an entry point name on its own. It first tries "sqlite3_extension_init". If that does not work, it tries names of the form "sqlite3_X_init" where X consists of the lower-case equivalent of all ASCII alphabetic characters or all ASCII alphanumeric characters in the filename from the last "/" to the first following "." and omitting any initial "lib". The sqlite3_load_extension() interface returns [SQLITE_OK](../rescode.md#ok) on success and [SQLITE_ERROR](../rescode.md#error) if something goes wrong. If an error occurs and pzErrMsg is not 0, then the [sqlite3_load_extension()](../c3ref/load_extension.md) interface shall attempt to fill \*pzErrMsg with error message text stored in memory obtained from [sqlite3_malloc()](../c3ref/free.md). The calling function should free this memory by calling [sqlite3_free()](../c3ref/free.md).

Extension loading must be enabled using [sqlite3_enable_load_extension()](../c3ref/enable_load_extension.md) or [sqlite3_db_config](../c3ref/db_config.md)(db,[SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableloadextension),1,NULL) prior to calling this API, otherwise an error will be returned.

**Security warning:** It is recommended that the [SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION](../c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableloadextension) method be used to enable only this interface. The use of the [sqlite3_enable_load_extension()](../c3ref/enable_load_extension.md) interface should be avoided. This will keep the SQL function [load_extension()](../lang_corefunc.md#load_extension) disabled and prevent SQL injections from giving attackers access to extension loading capabilities.

See also the [load_extension() SQL function](../lang_corefunc.md#load_extension).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
