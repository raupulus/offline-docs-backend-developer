---
title: Run-Time Loadable Extensions
source_url: https://www.sqlite.org/loadext.html
source_path: loadext.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 3510
---

# 1. Overview

SQLite has the ability to load extensions (including new [application-defined SQL functions](appfunc.md), [collating sequences](datatype3.md#collation), [virtual tables](vtab.md), and [VFSes](vfs.md)) at run-time. This feature allows the code for extensions to be developed and tested separately from the application and then loaded on an as-needed basis.

Extensions can also be statically linked with the application. The code template shown below will work just as well as a statically linked extension as it does as a run-time loadable extension except that you should give the entry point function ("sqlite3_extension_init") a different name to avoid name collisions if your application contains two or more extensions.

# 2. Loading An Extension

An SQLite extension is a shared library or DLL. To load it, you need to supply SQLite with the name of the file containing the shared library or DLL and an entry point to initialize the extension. In C code, this information is supplied using the [sqlite3_load_extension()](c3ref/load_extension.md) API. See the documentation on that routine for additional information.

Note that different operating systems use different filename suffixes for their shared libraries. Windows uses ".dll", Mac uses ".dylib", and most unixes other than mac use ".so". If you want to make your code portable, you can omit the suffix from the shared library filename and the appropriate suffix will be added automatically by the [sqlite3_load_extension()](c3ref/load_extension.md) interface.

There is also an SQL function that can be used to load extensions: [load_extension(X,Y)](lang_corefunc.md#load_extension). It works just like the [sqlite3_load_extension()](c3ref/load_extension.md) C interface.

Both methods for loading an extension allow you to specify the name of an entry point for the extension. You can leave this argument blank - passing in a NULL pointer for the [sqlite3_load_extension()](c3ref/load_extension.md) C-language interface or omitting the second argument for the [load_extension()](lang_corefunc.md#load_extension) SQL interface - and the extension loader logic will attempt to figure out the entry point on its own. It will first try the generic extension name "sqlite3_extension_init". If that does not work, it constructs an entry point using the template "sqlite3_X_init" where the X is replaced by the lowercase equivalent of every ASCII character in the filename after the last "/" and before the first following "." omitting the first three characters if they happen to be "lib". So, for example, if the filename is "/usr/lib/libmathfunc-4.8.so" the entry point name would be "sqlite3_mathfunc_init". Or if the filename is "./SpellFixExt.dll" then the entry point would be called "sqlite3_spellfixext_init".

For security reasons, extension loading is turned off by default. In order to use either the C-language or SQL extension loading functions, one must first enable extension loading using the [sqlite3_db_config](c3ref/db_config.md)(db,[SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION](c3ref/c_dbconfig_defensive.md#sqlitedbconfigenableloadextension),1,NULL) C-language API in your application.

From the [command-line shell](cli.md), extensions can be loaded using the ".load" dot-command. For example:

> \
> .load ./YourCode\

Note that the command-line shell program has already enabled extension loading for you (by calling the [sqlite3_enable_load_extension()](c3ref/enable_load_extension.md) interface as part of its setup) so the command above works without any special switches, setup, or other complications.

The ".load" command with one argument invokes sqlite3_load_extension() with the zProc parameter set to NULL, causing SQLite to first look for an entry point named "sqlite3_extension_init" and then "sqlite3_X_init" where "X" is derived from the filename. If your extension has an entry point with a different name, simply supply that name as the second argument. For example:

> \
> .load ./YourCode nonstandard_entry_point\

<span id="build"></span>

# 3. Compiling A Loadable Extension

Loadable extensions are C-code. To compile them on most unix-like operating systems, the usual command is something like this:

> \
> gcc -g -fPIC -shared YourCode.c -o YourCode.so\

Macs are unix-like, but they do not follow the usual shared library conventions. To compile a shared library on a Mac, use a command like this:

> \
> gcc -g -fPIC -dynamiclib YourCode.c -o YourCode.dylib\

If when you try to load your library you get back an error message that says "mach-o, but wrong architecture" then you might need to add command-line options "-arch i386" or "arch x86_64" to gcc, depending on how your application is built.

To compile on Windows using MSVC, a command similar to the following will usually work:

> \
> cl YourCode.c -link -dll -out:YourCode.dll\

To compile for Windows using MinGW, the command line is just like it is for unix except that the output file suffix is changed to ".dll" and the -fPIC argument is omitted:

> \
> gcc -g -shared YourCode.c -o YourCode.dll\

<span id="write"></span>

# 4. Programming Loadable Extensions

A template loadable extension contains the following three elements:

1.  Use "`#include <sqlite3ext.h>`" at the top of your source code files instead of "`#include <sqlite3.h>`".

2.  Put the macro "`SQLITE_EXTENSION_INIT1`" on a line by itself right after the "`#include <sqlite3ext.h>`" line.

3.  Add an extension loading entry point routine that looks something like the following:

    \#ifdef \_WIN32\
    \_\_declspec(dllexport)\
    \#endif\
    int sqlite3_extension_init( /\* \<== Change this name, maybe \*/\
      sqlite3 \*db, \
      char \*\*pzErrMsg, \
      const sqlite3_api_routines \*pApi\
    ){\
      int rc = SQLITE_OK;\
      SQLITE_EXTENSION_INIT2(pApi);\
      /\* insert code to initialize your extension here \*/\
      return rc;\
    }\

    You will do well to customize the name of your entry point to correspond to the name of the shared library you will be generating, rather than using the generic "sqlite3_extension_init" name. Giving your extension a custom entry point name will enable you to statically link two or more extensions into the same program without a linker conflict, if you later decide to use static linking rather than run-time linking. If your shared library ends up being named "YourCode.so" or "YourCode.dll" or "YourCode.dylib" as shown in the compiler examples above, then the correct entry point name would be "sqlite3_yourcode_init".

Here is a complete template extension that you can copy/paste to get started:

/\* Add your header comment here \*/\
\#include \<sqlite3ext.h\> /\* Do not use \<sqlite3.h\>! \*/\
SQLITE_EXTENSION_INIT1\
\
/\* Insert your extension code here \*/\
\
\#ifdef \_WIN32\
\_\_declspec(dllexport)\
\#endif\
/\* TODO: Change the entry point name so that "extension" is replaced by\
\*\* text derived from the shared library filename as follows:  Copy every\
\*\* ASCII alphabetic character from the filename after the last "/" through\
\*\* the next following ".", converting each character to lowercase, and\
\*\* discarding the first three characters if they are "lib".\
\*/\
int sqlite3_extension_init(\
  sqlite3 \*db,\
  char \*\*pzErrMsg,\
  const sqlite3_api_routines \*pApi\
){\
  int rc = SQLITE_OK;\
  SQLITE_EXTENSION_INIT2(pApi);\
  /\* Insert here calls to\
  \*\*     sqlite3_create_function_v2(),\
  \*\*     sqlite3_create_collation_v2(),\
  \*\*     sqlite3_create_module_v2(), and/or\
  \*\*     sqlite3_vfs_register()\
  \*\* to register the new features that your extension adds.\
  \*/\
  return rc;\
}\

## 4.1. Example Extensions

Many examples of complete and working loadable extensions can be seen in the SQLite source tree in the [ext/misc](https://sqlite.org/src/file/ext/misc) subdirectory. Each file in that directory is a separate extension. Documentation is provided by a header comment on the file. Here are brief notes on a few of the extensions in the [ext/misc](https://sqlite.org/src/file/ext/misc) subdirectory:

- [carray.c](https://sqlite.org/src/file/ext/misc/carray.c) — Implementation of the [carray table-valued function](carray.md).

- [compress.c](https://sqlite.org/src/file/ext/misc/compress.c) — Implementation of [application-defined SQL functions](appfunc.md) compress() and uncompress() that do zLib compression of text or blob content.

- [rot13.c](https://sqlite.org/src/file/ext/misc/rot13.c) — Implementation of a [rot13()](https://en.wikipedia.org/wiki/ROT13) SQL function. This is a very simple example of an extension function and is useful as a template for creating new extensions.

- [series.c](https://sqlite.org/src/file/ext/misc/series.c) — Implementation of the generate_series [virtual table](vtab.md) and [table-valued function](vtab.md#tabfunc2). This is a relatively simple example of a virtual table implementation which can serve as a template for writing new virtual tables.

Other and more complex extensions can be found in subfolders under [ext/](https://sqlite.org/src/file/ext) other than ext/misc/. <span id="persist"></span>

# 5. Persistent Loadable Extensions

The default behavior for a loadable extension is that it is unloaded from process memory when the database connection that originally invoked [sqlite3_load_extension()](c3ref/load_extension.md) closes. (In other words, the xDlClose method of the [sqlite3_vfs](c3ref/vfs.md) object is called for all extensions when a database connection closes.) However, if the initialization procedure returns [SQLITE_OK_LOAD_PERMANENTLY](rescode.md#ok_load_permanently) instead of SQLITE_OK, then the extension will not be unloaded (xDlClose will not be invoked) and the extension will remain in process memory indefinitely. The SQLITE_OK_LOAD_PERMANENTLY return value is useful for extensions that want to register new [VFSes](vfs.md).

To clarify: an extension for which the initialization function returns SQLITE_OK_LOAD_PERMANENTLY continues to exist in memory after the database connection closes. However, the extension is *not* automatically registered with subsequent database connections. This makes it possible to load extensions that implement new [VFSes](vfs.md). To persistently load and register an extension that implements new SQL functions, collating sequences, and/or virtual tables, such that those added capabilities are available to all subsequent database connections, then the initialization routine should also invoke [sqlite3_auto_extension()](c3ref/auto_extension.md) on a subfunction that will register those services.

The [vfsstat.c](https://sqlite.org/src/file/ext/misc/vfsstat.c) extension show an example of a loadable extension that persistently registers both a new VFS and a new virtual table. The [sqlite3_vfsstat_init()](https://sqlite.org/src/info/77b5b4235c9f7f11?ln=801-819) initialization routine in that extension is called only once, when the extension is first loaded. It registers the new "vfslog" VFS just that one time, and it returns SQLITE_OK_LOAD_PERMANENTLY so that the code used to implement the "vfslog" VFS will remain in memory. The initialization routine also invokes [sqlite3_auto_extension()](c3ref/auto_extension.md) on a pointer to the "vstatRegister()" function so that all subsequent database connections will invoke the "vstatRegister()" function as they start up, and hence register the "vfsstat" virtual table. <span id="statext"></span>

# 6. Statically Linking A Run-Time Loadable Extension

The exact same source code can be used for both a run-time loadable shared library or DLL and as a module that is statically linked with your application. This provides flexibility and allows you to reuse the same code in different ways.

To statically link your extension, simply add the -DSQLITE_CORE compile-time option. The SQLITE_CORE macro causes the SQLITE_EXTENSION_INIT1 and SQLITE_EXTENSION_INIT2 macros to become no-ops. Then modify your application to invoke the entry point directly, passing in a NULL pointer as the third "pApi" parameter.

It is particularly important to use an entry point name that is based on the extension filename, rather than the generic "sqlite3_extension_init" entry point name, if you will be statically linking two or more extensions. If you use the generic name, there will be multiple definitions of the same symbol and the link will fail.

If you will be opening multiple database connections in your application, rather than invoking the extension entry points for each database connection separately, you might want to consider using the [sqlite3_auto_extension()](c3ref/auto_extension.md) interface to register your extensions and to cause them to be automatically started as each database connection is opened. You only have to register each extension once, and you can do so near the beginning of your main() routine. Using the [sqlite3_auto_extension()](c3ref/auto_extension.md) interface to register your extensions makes your extensions work as if they were built into the core SQLite - they automatically exist whenever you open a new database connection without needing to be initialized. Just be sure to complete any configuration you need to accomplish using [sqlite3_config()](c3ref/config.md) before registering your extensions, since the [sqlite3_auto_extension()](c3ref/auto_extension.md) interface implicitly calls [sqlite3_initialize()](c3ref/initialize.md).

# 7. Implementation Details

SQLite implements run-time extension loading using the xDlOpen(), xDlError(), xDlSym(), and xDlClose() methods of the [sqlite3_vfs](c3ref/vfs.md) object. These methods are implemented using the dlopen() library on unix (which explains why SQLite commonly needs to be linked against the "-ldl" library on unix systems) and using LoadLibrary() API on Windows. In a custom [VFS](vfs.md) for unusual systems, these methods can all be omitted, in which case the run-time extension loading mechanism will not work (though you will still be able to statically link the extension code, assuming the entry pointers are uniquely named). SQLite can be compiled with [SQLITE_OMIT_LOAD_EXTENSION](compile.md#omit_load_extension) to omit the extension loading code from the build.
