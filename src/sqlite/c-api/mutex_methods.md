---
title: Mutex Methods Object
source_url: https://www.sqlite.org/c3ref/mutex_methods.html
source_path: c3ref/mutex_methods.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1550
---

> \
> typedef struct sqlite3_mutex_methods sqlite3_mutex_methods;\
> struct sqlite3_mutex_methods {\
>   int (\*xMutexInit)(void);\
>   int (\*xMutexEnd)(void);\
>   sqlite3_mutex \*(\*xMutexAlloc)(int);\
>   void (\*xMutexFree)(sqlite3_mutex \*);\
>   void (\*xMutexEnter)(sqlite3_mutex \*);\
>   int (\*xMutexTry)(sqlite3_mutex \*);\
>   void (\*xMutexLeave)(sqlite3_mutex \*);\
>   int (\*xMutexHeld)(sqlite3_mutex \*);\
>   int (\*xMutexNotheld)(sqlite3_mutex \*);\
> };\

An instance of this structure defines the low-level routines used to allocate and use mutexes.

Usually, the default mutex implementations provided by SQLite are sufficient, however the application has the option of substituting a custom implementation for specialized deployments or systems for which SQLite does not provide a suitable implementation. In this case, the application creates and populates an instance of this structure to pass to sqlite3_config() along with the [SQLITE_CONFIG_MUTEX](../c3ref/c_config_covering_index_scan.md#sqliteconfigmutex) option. Additionally, an instance of this structure can be used as an output variable when querying the system for the current mutex implementation, using the [SQLITE_CONFIG_GETMUTEX](../c3ref/c_config_covering_index_scan.md#sqliteconfiggetmutex) option.

The xMutexInit method defined by this structure is invoked as part of system initialization by the sqlite3_initialize() function. The xMutexInit routine is called by SQLite exactly once for each effective call to [sqlite3_initialize()](../c3ref/initialize.md).

The xMutexEnd method defined by this structure is invoked as part of system shutdown by the sqlite3_shutdown() function. The implementation of this method is expected to release all outstanding resources obtained by the mutex methods implementation, especially those obtained by the xMutexInit method. The xMutexEnd() interface is invoked exactly once for each call to [sqlite3_shutdown()](../c3ref/initialize.md).

The remaining seven methods defined by this structure (xMutexAlloc, xMutexFree, xMutexEnter, xMutexTry, xMutexLeave, xMutexHeld and xMutexNotheld) implement the following interfaces (respectively):

- [sqlite3_mutex_alloc()](../c3ref/mutex_alloc.md)
- [sqlite3_mutex_free()](../c3ref/mutex_alloc.md)
- [sqlite3_mutex_enter()](../c3ref/mutex_alloc.md)
- [sqlite3_mutex_try()](../c3ref/mutex_alloc.md)
- [sqlite3_mutex_leave()](../c3ref/mutex_alloc.md)
- [sqlite3_mutex_held()](../c3ref/mutex_held.md)
- [sqlite3_mutex_notheld()](../c3ref/mutex_held.md)

The only difference is that the public sqlite3_XXX functions enumerated above silently ignore any invocations that pass a NULL pointer instead of a valid mutex handle. The implementations of the methods defined by this structure are not required to handle this case. The results of passing a NULL pointer instead of a valid mutex handle are undefined (i.e. it is acceptable to provide an implementation that segfaults if it is passed a NULL pointer).

The xMutexInit() method must be threadsafe. It must be harmless to invoke xMutexInit() multiple times within the same process and without intervening calls to xMutexEnd(). Second and subsequent calls to xMutexInit() must be no-ops.

xMutexInit() must not use SQLite memory allocation ([sqlite3_malloc()](../c3ref/free.md) and its associates). Similarly, xMutexAlloc() must not use SQLite memory allocation for a static mutex. However xMutexAlloc() may use SQLite memory allocation for a fast or recursive mutex.

SQLite will invoke the xMutexEnd() method when [sqlite3_shutdown()](../c3ref/initialize.md) is called, but only if the prior call to xMutexInit returned SQLITE_OK. If xMutexInit fails in any way, it is expected to clean up after itself prior to returning.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
