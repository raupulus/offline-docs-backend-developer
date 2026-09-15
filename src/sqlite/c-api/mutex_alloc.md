---
title: Mutexes
source_url: https://www.sqlite.org/c3ref/mutex_alloc.html
source_path: c3ref/mutex_alloc.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1530
---

> \
> sqlite3_mutex \*sqlite3_mutex_alloc(int);\
> void sqlite3_mutex_free(sqlite3_mutex\*);\
> void sqlite3_mutex_enter(sqlite3_mutex\*);\
> int sqlite3_mutex_try(sqlite3_mutex\*);\
> void sqlite3_mutex_leave(sqlite3_mutex\*);\

The SQLite core uses these routines for thread synchronization. Though they are intended for internal use by SQLite, code that links against SQLite is permitted to use any of these routines.

The SQLite source code contains multiple implementations of these mutex routines. An appropriate implementation is selected automatically at compile-time. The following implementations are available in the SQLite core:

- SQLITE_MUTEX_PTHREADS
- SQLITE_MUTEX_W32
- SQLITE_MUTEX_NOOP

The SQLITE_MUTEX_NOOP implementation is a set of routines that does no real locking and is appropriate for use in a single-threaded application. The SQLITE_MUTEX_PTHREADS and SQLITE_MUTEX_W32 implementations are appropriate for use on Unix and Windows.

The sqlite3_mutex_alloc() routine allocates a new mutex and returns a pointer to it. The sqlite3_mutex_alloc() routine returns NULL if it is unable to allocate the requested mutex. The argument to sqlite3_mutex_alloc() must be one of these integer constants:

- SQLITE_MUTEX_FAST
- SQLITE_MUTEX_RECURSIVE
- SQLITE_MUTEX_STATIC_MAIN
- SQLITE_MUTEX_STATIC_MEM
- SQLITE_MUTEX_STATIC_OPEN
- SQLITE_MUTEX_STATIC_PRNG
- SQLITE_MUTEX_STATIC_LRU
- SQLITE_MUTEX_STATIC_PMEM
- SQLITE_MUTEX_STATIC_APP1
- SQLITE_MUTEX_STATIC_APP2
- SQLITE_MUTEX_STATIC_APP3
- SQLITE_MUTEX_STATIC_VFS1
- SQLITE_MUTEX_STATIC_VFS2
- SQLITE_MUTEX_STATIC_VFS3

The first two constants (SQLITE_MUTEX_FAST and SQLITE_MUTEX_RECURSIVE) cause sqlite3_mutex_alloc() to create a new mutex. The new mutex is recursive when SQLITE_MUTEX_RECURSIVE is used but not necessarily so when SQLITE_MUTEX_FAST is used. The mutex implementation does not need to make a distinction between SQLITE_MUTEX_RECURSIVE and SQLITE_MUTEX_FAST if it does not want to. SQLite will only request a recursive mutex in cases where it really needs one. If a faster non-recursive mutex implementation is available on the host platform, the mutex subsystem might return such a mutex in response to SQLITE_MUTEX_FAST.

The other allowed parameters to sqlite3_mutex_alloc() (anything other than SQLITE_MUTEX_FAST and SQLITE_MUTEX_RECURSIVE) each return a pointer to a static preexisting mutex. Nine static mutexes are used by the current version of SQLite. Future versions of SQLite may add additional static mutexes. Static mutexes are for internal use by SQLite only. Applications that use SQLite mutexes should use only the dynamic mutexes returned by SQLITE_MUTEX_FAST or SQLITE_MUTEX_RECURSIVE.

Note that if one of the dynamic mutex parameters (SQLITE_MUTEX_FAST or SQLITE_MUTEX_RECURSIVE) is used then sqlite3_mutex_alloc() returns a different mutex on every call. For the static mutex types, the same mutex is returned on every call that has the same type number.

The sqlite3_mutex_free() routine deallocates a previously allocated dynamic mutex. Attempting to deallocate a static mutex results in undefined behavior.

The sqlite3_mutex_enter() and sqlite3_mutex_try() routines attempt to enter a mutex. If another thread is already within the mutex, sqlite3_mutex_enter() will block and sqlite3_mutex_try() will return SQLITE_BUSY. The sqlite3_mutex_try() interface returns [SQLITE_OK](../rescode.md#ok) upon successful entry. Mutexes created using SQLITE_MUTEX_RECURSIVE can be entered multiple times by the same thread. In such cases, the mutex must be exited an equal number of times before another thread can enter. If the same thread tries to enter any mutex other than an SQLITE_MUTEX_RECURSIVE more than once, the behavior is undefined.

Some systems (for example, Windows 95) do not support the operation implemented by sqlite3_mutex_try(). On those systems, sqlite3_mutex_try() will always return SQLITE_BUSY. In most cases the SQLite core only uses sqlite3_mutex_try() as an optimization, so this is acceptable behavior. The exceptions are unix builds that set the SQLITE_ENABLE_SETLK_TIMEOUT build option. In that case a working sqlite3_mutex_try() is required.

The sqlite3_mutex_leave() routine exits a mutex that was previously entered by the same thread. The behavior is undefined if the mutex is not currently entered by the calling thread or is not currently allocated.

If the argument to sqlite3_mutex_enter(), sqlite3_mutex_try(), sqlite3_mutex_leave(), or sqlite3_mutex_free() is a NULL pointer, then any of the four routines behaves as a no-op.

See also: [sqlite3_mutex_held()](../c3ref/mutex_held.md) and [sqlite3_mutex_notheld()](../c3ref/mutex_held.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
