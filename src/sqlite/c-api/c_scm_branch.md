---
title: Compile-Time Library Version Numbers
source_url: https://www.sqlite.org/c3ref/c_scm_branch.html
source_path: c3ref/c_scm_branch.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 660
---

> \
> \#define SQLITE_VERSION        "3.53.4"\
> \#define SQLITE_VERSION_NUMBER 3053004\
> \#define SQLITE_SOURCE_ID      "2026-07-24 19:02:57 bf7c7f30031888f4e796e429ab3978879485813aaca6f641c7b33e4e09459bcc"\
> \#define SQLITE_SCM_BRANCH     "branch-3.53"\
> \#define SQLITE_SCM_TAGS       "release version-3.53.4"\
> \#define SQLITE_SCM_DATETIME   "2026-07-24T19:02:57.525Z"\

The [SQLITE_VERSION](../c3ref/c_scm_branch.md) C preprocessor macro in the sqlite3.h header evaluates to a string literal that is the SQLite version in the format "X.Y.Z" where X is the major version number (always 3 for SQLite3) and Y is the minor version number and Z is the release number. The [SQLITE_VERSION_NUMBER](../c3ref/c_scm_branch.md) C preprocessor macro resolves to an integer with the value (X\*1000000 + Y\*1000 + Z) where X, Y, and Z are the same numbers used in [SQLITE_VERSION](../c3ref/c_scm_branch.md). The SQLITE_VERSION_NUMBER for any given release of SQLite will also be larger than the release from which it is derived. Either Y will be held constant and Z will be incremented or else Y will be incremented and Z will be reset to zero.

Since [version 3.6.18](../releaselog/3_6_18.md) (2009-09-11), SQLite source code has been stored in the [Fossil configuration management system](http://fossil-scm.org/). The SQLITE_SOURCE_ID macro evaluates to a string which identifies a particular check-in of SQLite within its configuration management system. The SQLITE_SOURCE_ID string contains the date and time of the check-in (UTC) and a SHA1 or SHA3-256 hash of the entire source tree. If the source code has been edited in any way since it was last checked in, then the last four hexadecimal digits of the hash may be modified.

See also: [sqlite3_libversion()](../c3ref/libversion.md), [sqlite3_libversion_number()](../c3ref/libversion.md), [sqlite3_sourceid()](../c3ref/libversion.md), [sqlite_version()](../lang_corefunc.md#sqlite_version) and [sqlite_source_id()](../lang_corefunc.md#sqlite_source_id).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
