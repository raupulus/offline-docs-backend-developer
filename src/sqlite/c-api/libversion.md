---
title: Run-Time Library Version Numbers
source_url: https://www.sqlite.org/c3ref/libversion.html
source_path: c3ref/libversion.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1440
---

> \
> SQLITE_EXTERN const char sqlite3_version\[\];\
> const char \*sqlite3_libversion(void);\
> const char \*sqlite3_sourceid(void);\
> int sqlite3_libversion_number(void);\

These interfaces provide the same information as the [SQLITE_VERSION](../c3ref/c_scm_branch.md), [SQLITE_VERSION_NUMBER](../c3ref/c_scm_branch.md), and [SQLITE_SOURCE_ID](../c3ref/c_scm_branch.md) C preprocessor macros but are associated with the library instead of the header file. Cautious programmers might include assert() statements in their application to verify that values returned by these interfaces match the macros in the header, and thus ensure that the application is compiled with matching library and header files.

> \
> assert( sqlite3_libversion_number()==SQLITE_VERSION_NUMBER );\
> assert( strncmp(sqlite3_sourceid(),SQLITE_SOURCE_ID,80)==0 );\
> assert( strcmp(sqlite3_libversion(),SQLITE_VERSION)==0 );\

The sqlite3_version\[\] string constant contains the text of the [SQLITE_VERSION](../c3ref/c_scm_branch.md) macro. The sqlite3_libversion() function returns a pointer to the sqlite3_version\[\] string constant. The sqlite3_libversion() function is provided for use in DLLs since DLL users usually do not have direct access to string constants within the DLL. The sqlite3_libversion_number() function returns an integer equal to [SQLITE_VERSION_NUMBER](../c3ref/c_scm_branch.md). The sqlite3_sourceid() function returns a pointer to a string constant whose value is the same as the [SQLITE_SOURCE_ID](../c3ref/c_scm_branch.md) C preprocessor macro. Except if SQLite is built using an edited copy of [the amalgamation](../amalgamation.md), then the last four characters of the hash might be different from [SQLITE_SOURCE_ID](../c3ref/c_scm_branch.md).

See also: [sqlite_version()](../lang_corefunc.md#sqlite_version) and [sqlite_source_id()](../lang_corefunc.md#sqlite_source_id).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
