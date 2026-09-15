---
title: 64-Bit Integer Types
source_url: https://www.sqlite.org/c3ref/int64.html
source_path: c3ref/int64.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1380
---

> \
> \#ifdef SQLITE_INT64_TYPE\
>   typedef SQLITE_INT64_TYPE sqlite_int64;\
> \# ifdef SQLITE_UINT64_TYPE\
>     typedef SQLITE_UINT64_TYPE sqlite_uint64;\
> \# else\
>     typedef unsigned SQLITE_INT64_TYPE sqlite_uint64;\
> \# endif\
> \#elif defined(\_MSC_VER) \|\| defined(\_\_BORLANDC\_\_)\
>   typedef \_\_int64 sqlite_int64;\
>   typedef unsigned \_\_int64 sqlite_uint64;\
> \#else\
>   typedef long long int sqlite_int64;\
>   typedef unsigned long long int sqlite_uint64;\
> \#endif\
> typedef sqlite_int64 sqlite3_int64;\
> typedef sqlite_uint64 sqlite3_uint64;\

Because there is no cross-platform way to specify 64-bit integer types SQLite includes typedefs for 64-bit signed and unsigned integers.

The sqlite3_int64 and sqlite3_uint64 are the preferred type definitions. The sqlite_int64 and sqlite_uint64 types are supported for backwards compatibility only.

The sqlite3_int64 and sqlite_int64 types can store integer values between -9223372036854775808 and +9223372036854775807 inclusive. The sqlite3_uint64 and sqlite_uint64 types can store integer values between 0 and +18446744073709551615 inclusive.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
