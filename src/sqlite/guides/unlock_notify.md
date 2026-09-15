---
title: SQLite Unlock-Notify API
source_url: https://www.sqlite.org/unlock_notify.html
source_path: unlock_notify.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 8190
---

# Using the sqlite3_unlock_notify() API

\
<span style="color:blue;font-style:italic">/\* This example uses the pthreads API \*/</span>\
\#include \<pthread.h\>\
\
<span style="color:blue;font-style:italic">/\*</span>\
<span style="color:blue;font-style:italic">\*\* A pointer to an instance of this structure is passed as the user-context</span>\
<span style="color:blue;font-style:italic">\*\* pointer when registering for an unlock-notify callback.</span>\
<span style="color:blue;font-style:italic">\*/</span>\
typedef struct UnlockNotification UnlockNotification;\
struct UnlockNotification {\
  int fired;                         <span style="color:blue;font-style:italic">/\* True after unlock event has occurred \*/</span>\
  pthread_cond_t cond;               <span style="color:blue;font-style:italic">/\* Condition variable to wait on \*/</span>\
  pthread_mutex_t mutex;             <span style="color:blue;font-style:italic">/\* Mutex to protect structure \*/</span>\
};\
\
<span style="color:blue;font-style:italic">/\*</span>\
<span style="color:blue;font-style:italic">\*\* This function is an unlock-notify callback registered with SQLite.</span>\
<span style="color:blue;font-style:italic">\*/</span>\
static void unlock_notify_cb(void \*\*apArg, int nArg){\
  int i;\
  for(i=0; i\<nArg; i++){\
    UnlockNotification \*p = (UnlockNotification \*)apArg\[i\];\
    pthread_mutex_lock(&p-\>mutex);\
    p-\>fired = 1;\
    pthread_cond_signal(&p-\>cond);\
    pthread_mutex_unlock(&p-\>mutex);\
  }\
}\
\
<span style="color:blue;font-style:italic">/\*</span>\
<span style="color:blue;font-style:italic">\*\* This function assumes that an SQLite API call (either [sqlite3_prepare_v2](c3ref/prepare.md)() </span>\
<span style="color:blue;font-style:italic">\*\* or [sqlite3_step](c3ref/step.md)()) has just returned SQLITE_LOCKED. The argument is the</span>\
<span style="color:blue;font-style:italic">\*\* associated database connection.</span>\
<span style="color:blue;font-style:italic">\*\*</span>\
<span style="color:blue;font-style:italic">\*\* This function calls [sqlite3_unlock_notify](c3ref/unlock_notify.md)() to register for an </span>\
<span style="color:blue;font-style:italic">\*\* unlock-notify callback, then blocks until that callback is delivered </span>\
<span style="color:blue;font-style:italic">\*\* and returns SQLITE_OK. The caller should then retry the failed operation.</span>\
<span style="color:blue;font-style:italic">\*\*</span>\
<span style="color:blue;font-style:italic">\*\* Or, if [sqlite3_unlock_notify](c3ref/unlock_notify.md)() indicates that to block would deadlock </span>\
<span style="color:blue;font-style:italic">\*\* the system, then this function returns SQLITE_LOCKED immediately. In </span>\
<span style="color:blue;font-style:italic">\*\* this case the caller should not retry the operation and should roll </span>\
<span style="color:blue;font-style:italic">\*\* back the current transaction (if any).</span>\
<span style="color:blue;font-style:italic">\*/</span>\
static int wait_for_unlock_notify([sqlite3](c3ref/sqlite3.md) \*db){\
  int rc;\
  UnlockNotification un;\
\
  <span style="color:blue;font-style:italic">/\* Initialize the UnlockNotification structure. \*/</span>\
  un.fired = 0;\
  pthread_mutex_init(&un.mutex, 0);\
  pthread_cond_init(&un.cond, 0);\
\
  <span style="color:blue;font-style:italic">/\* Register for an unlock-notify callback. \*/</span>\
  rc = [sqlite3_unlock_notify](c3ref/unlock_notify.md)(db, unlock_notify_cb, (void \*)&un);\
  assert( rc==SQLITE_LOCKED \|\| rc==SQLITE_OK );\
\
  <span style="color:blue;font-style:italic">/\* The call to [sqlite3_unlock_notify](c3ref/unlock_notify.md)() always returns either SQLITE_LOCKED </span>\
<span style="color:blue;font-style:italic">  \*\* or SQLITE_OK. </span>\
<span style="color:blue;font-style:italic">  \*\*</span>\
<span style="color:blue;font-style:italic">  \*\* If SQLITE_LOCKED was returned, then the system is deadlocked. In this</span>\
<span style="color:blue;font-style:italic">  \*\* case this function needs to return SQLITE_LOCKED to the caller so </span>\
<span style="color:blue;font-style:italic">  \*\* that the current transaction can be rolled back. Otherwise, block</span>\
<span style="color:blue;font-style:italic">  \*\* until the unlock-notify callback is invoked, then return SQLITE_OK.</span>\
  <span style="color:blue;font-style:italic">\*/</span>\
  if( rc==SQLITE_OK ){\
    pthread_mutex_lock(&un.mutex);\
    if( !un.fired ){\
      pthread_cond_wait(&un.cond, &un.mutex);\
    }\
    pthread_mutex_unlock(&un.mutex);\
  }\
\
  <span style="color:blue;font-style:italic">/\* Destroy the mutex and condition variables. \*/</span>\
  pthread_cond_destroy(&un.cond);\
  pthread_mutex_destroy(&un.mutex);\
\
  return rc;\
}\
\
<span style="color:blue;font-style:italic">/\*</span>\
<span style="color:blue;font-style:italic">\*\* This function is a wrapper around the SQLite function [sqlite3_step](c3ref/step.md)().</span>\
<span style="color:blue;font-style:italic">\*\* It functions in the same way as step(), except that if a required</span>\
<span style="color:blue;font-style:italic">\*\* shared-cache lock cannot be obtained, this function may block waiting for</span>\
<span style="color:blue;font-style:italic">\*\* the lock to become available. In this scenario the normal API step()</span>\
<span style="color:blue;font-style:italic">\*\* function always returns SQLITE_LOCKED.</span>\
<span style="color:blue;font-style:italic">\*\*</span>\
<span style="color:blue;font-style:italic">\*\* If this function returns SQLITE_LOCKED, the caller should rollback</span>\
<span style="color:blue;font-style:italic">\*\* the current transaction (if any) and try again later. Otherwise, the</span>\
<span style="color:blue;font-style:italic">\*\* system may become deadlocked.</span>\
<span style="color:blue;font-style:italic">\*/</span>\
int sqlite3_blocking_step([sqlite3_stmt](c3ref/stmt.md) \*pStmt){\
  int rc;\
  while( SQLITE_LOCKED==(rc = [sqlite3_step](c3ref/step.md)(pStmt)) ){\
    rc = wait_for_unlock_notify([sqlite3_db_handle](c3ref/db_handle.md)(pStmt));\
    if( rc!=SQLITE_OK ) break;\
    [sqlite3_reset](c3ref/reset.md)(pStmt);\
  }\
  return rc;\
}\
\
<span style="color:blue;font-style:italic">/\*</span>\
<span style="color:blue;font-style:italic">\*\* This function is a wrapper around the SQLite function [sqlite3_prepare_v2](c3ref/prepare.md)().</span>\
<span style="color:blue;font-style:italic">\*\* It functions in the same way as prepare_v2(), except that if a required</span>\
<span style="color:blue;font-style:italic">\*\* shared-cache lock cannot be obtained, this function may block waiting for</span>\
<span style="color:blue;font-style:italic">\*\* the lock to become available. In this scenario the normal API prepare_v2()</span>\
<span style="color:blue;font-style:italic">\*\* function always returns SQLITE_LOCKED.</span>\
<span style="color:blue;font-style:italic">\*\*</span>\
<span style="color:blue;font-style:italic">\*\* If this function returns SQLITE_LOCKED, the caller should rollback</span>\
<span style="color:blue;font-style:italic">\*\* the current transaction (if any) and try again later. Otherwise, the</span>\
<span style="color:blue;font-style:italic">\*\* system may become deadlocked.</span>\
<span style="color:blue;font-style:italic">\*/</span>\
int sqlite3_blocking_prepare_v2(\
  [sqlite3](c3ref/sqlite3.md) \*db,              <span style="color:blue;font-style:italic">/\* Database handle. \*/</span>\
  const char \*zSql,         <span style="color:blue;font-style:italic">/\* UTF-8 encoded SQL statement. \*/</span>\
  int nSql,                 <span style="color:blue;font-style:italic">/\* Length of zSql in bytes. \*/</span>\
  [sqlite3_stmt](c3ref/stmt.md) \*\*ppStmt,    <span style="color:blue;font-style:italic">/\* OUT: A pointer to the prepared statement \*/</span>\
  const char \*\*pz           <span style="color:blue;font-style:italic">/\* OUT: End of parsed string \*/</span>\
){\
  int rc;\
  while( SQLITE_LOCKED==(rc = [sqlite3_prepare_v2](c3ref/prepare.md)(db, zSql, nSql, ppStmt, pz)) ){\
    rc = wait_for_unlock_notify(db);\
    if( rc!=SQLITE_OK ) break;\
  }\
  return rc;\
}\

When two or more connections access the same database in shared-cache mode, read and write (shared and exclusive) locks on individual tables are used to ensure that concurrently executing transactions are kept isolated. Before writing to a table, a write (exclusive) lock must be obtained on that table. Before reading, a read (shared) lock must be obtained. A connection releases all held table locks when it concludes its transaction. If a connection cannot obtain a required lock, then the call to [sqlite3_step()](c3ref/step.md) returns SQLITE_LOCKED.

Although it is less common, a call to [sqlite3_prepare()](c3ref/prepare.md) or [sqlite3_prepare_v2()](c3ref/prepare.md) may also return SQLITE_LOCKED if it cannot obtain a read-lock on the [sqlite_schema table](schematab.md) of each attached database. These APIs need to read the schema data contained in the sqlite_schema table in order to compile SQL statements to [sqlite3_stmt\*](c3ref/stmt.md) objects.

This article presents a technique using the SQLite [sqlite3_unlock_notify()](c3ref/unlock_notify.md) interface such that calls to [sqlite3_step()](c3ref/step.md) and [sqlite3_prepare_v2()](c3ref/prepare.md) block until the required locks are available instead of returning SQLITE_LOCKED immediately. If the sqlite3_blocking_step() or sqlite3_blocking_prepare_v2() functions presented to the right return SQLITE_LOCKED, this indicates that to block would deadlock the system.

The [sqlite3_unlock_notify()](c3ref/unlock_notify.md) API, which is only available if the library is compiled with the pre-processor symbol [SQLITE_ENABLE_UNLOCK_NOTIFY](compile.md#enable_unlock_notify) defined, is [documented here](c3ref/unlock_notify.md). This article is not a substitute for reading the full API documentation!

The [sqlite3_unlock_notify()](c3ref/unlock_notify.md) interface is designed for use in systems that have a separate thread assigned to each [database connection](c3ref/sqlite3.md). There is nothing in the implementation that prevents a single thread from running multiple database connections. However, the [sqlite3_unlock_notify()](c3ref/unlock_notify.md) interface only works on a single connection at a time, so the lock resolution logic presented here will only work for a single database connection per thread.

**The sqlite3_unlock_notify() API**

After a call to [sqlite3_step()](c3ref/step.md) or [sqlite3_prepare_v2()](c3ref/prepare.md) returns SQLITE_LOCKED, the [sqlite3_unlock_notify()](c3ref/unlock_notify.md) API may be invoked to register for an unlock-notify callback. The unlock-notify callback is invoked by SQLite after the database connection holding the table-lock that prevented the call to [sqlite3_step()](c3ref/step.md) or [sqlite3_prepare_v2()](c3ref/prepare.md) from succeeding has finished its transaction and released all locks. For example, if a call to sqlite3_step() is an attempt to read from table X, and some other connection Y is holding a write-lock on table X, then sqlite3_step() will return SQLITE_LOCKED. If [sqlite3_unlock_notify()](c3ref/unlock_notify.md) is then called, the unlock-notify callback will be invoked after connection Y's transaction is concluded. The connection that the unlock-notify callback is waiting on, in this case connection Y, is known as the "blocking connection".

If a call to sqlite3_step() that attempts to write to a database table returns SQLITE_LOCKED, then more than one other connection may be holding a read-lock on the database table in question. In this case SQLite simply selects one of those other connections arbitrarily and issues the unlock-notify callback when that connection's transaction is finished. Whether the call to sqlite3_step() was blocked by one or many connections, when the corresponding unlock-notify callback is issued it is not guaranteed that the required lock is available, only that it may be.

When the unlock-notify callback is issued, it is issued from within a call to sqlite3_step() (or sqlite3_close()) associated with the blocking connection. It is illegal to invoke any sqlite3_XXX() API functions from within an unlock-notify callback. The expected use is that the unlock-notify callback will signal some other waiting thread or schedule some action to take place later.

The algorithm used by the sqlite3_blocking_step() function is as follows:

1.  Call sqlite3_step() on the supplied statement handle. If the call returns anything other than SQLITE_LOCKED, then return this value to the caller. Otherwise, continue.

2.  Invoke [sqlite3_unlock_notify()](c3ref/unlock_notify.md) on the database connection handle associated with the supplied statement handle to register for an unlock-notify callback. If the call to unlock_notify() returns SQLITE_LOCKED, then return this value to the caller.

3.  Block until the unlock-notify callback is invoked by another thread.

4.  Call sqlite3_reset() on the statement handle. Since an SQLITE_LOCKED error may only occur on the first call to sqlite3_step() (it is not possible for one call to sqlite3_step() to return SQLITE_ROW and then the next SQLITE_LOCKED), the statement handle may be reset at this point without affecting the results of the query from the point of view of the caller. If sqlite3_reset() were not called at this point, the next call to sqlite3_step() would return SQLITE_MISUSE.

5.  Return to step 1.

The algorithm used by the sqlite3_blocking_prepare_v2() function is similar, except that step 4 (resetting the statement handle) is omitted.

**Writer Starvation**

Multiple connections may hold a read-lock simultaneously. If many threads are acquiring overlapping read-locks, it might be the case that at least one thread is always holding a read lock. Then a table waiting for a write-lock will wait forever. This scenario is called "writer starvation."

SQLite helps applications avoid writer starvation. After any attempt to obtain a write-lock on a table fails (because one or more other connections are holding read-locks), all attempts to open new transactions on the shared-cache fail until one of the following is true:

- The current writer concludes its transaction, OR
- The number of open read-transactions on the shared-cache drops to zero.

Failed attempts to open new read-transactions return SQLITE_LOCKED to the caller. If the caller then calls [sqlite3_unlock_notify()](c3ref/unlock_notify.md) to register for an unlock-notify callback, the blocking connection is the connection that currently has an open write-transaction on the shared-cache. This prevents writer-starvation since if no new read-transactions may be opened and assuming all existing read-transactions are eventually concluded, the writer will eventually have an opportunity to obtain the required write-lock.

**The pthreads API**

By the time [sqlite3_unlock_notify()](c3ref/unlock_notify.md) is invoked by wait_for_unlock_notify(), it is possible that the blocking connection that prevented the sqlite3_step() or sqlite3_prepare_v2() call from succeeding has already finished its transaction. In this case, the unlock-notify callback is invoked immediately, before [sqlite3_unlock_notify()](c3ref/unlock_notify.md) returns. Or, it is possible that the unlock-notify callback is invoked by a second thread after [sqlite3_unlock_notify()](c3ref/unlock_notify.md) is called but before the thread starts waiting to be asynchronously signaled.

Exactly how such a potential race-condition is handled depends on the threads and synchronization primitives interface used by the application. This example uses pthreads, the interface provided by modern UNIX-like systems, including Linux.

The pthreads interface provides the pthread_cond_wait() function. This function allows the caller to simultaneously release a mutex and start waiting for an asynchronous signal. Using this function, a "fired" flag and a mutex, the race-condition described above may be eliminated as follows:

When the unlock-notify callback is invoked, which may be before the thread that called [sqlite3_unlock_notify()](c3ref/unlock_notify.md) begins waiting for the asynchronous signal, it does the following:

1.  Obtains the mutex.
2.  Sets the "fired" flag to true.
3.  Attempts to signal a waiting thread.
4.  Releases the mutex.

When the wait_for_unlock_notify() thread is ready to begin waiting for the unlock-notify callback to arrive, it:

1.  Obtains the mutex.
2.  Checks if the "fired" flag has been set. If so, the unlock-notify callback has already been invoked. Release the mutex and continue.
3.  Atomically releases the mutex and begins waiting for the asynchronous signal. When the signal arrives, continue.

This way, it doesn't matter if the unlock-notify callback has already been invoked, or is being invoked, when the wait_for_unlock_notify() thread begins blocking.

**Possible Enhancements**

The code in this article could be improved in at least two ways:

- It could manage thread priorities.
- It could handle a special case of SQLITE_LOCKED that can occur when dropping a table or index.

Even though the [sqlite3_unlock_notify()](c3ref/unlock_notify.md) function only allows the caller to specify a single user-context pointer, an unlock-notify callback is passed an array of such context pointers. This is because if when a blocking connection concludes its transaction, if there is more than one unlock-notify registered to call the same C function, the context-pointers are marshaled into an array and a single callback issued. If each thread were assigned a priority, then instead of just signaling the threads in arbitrary order as this implementation does, higher priority threads could be signaled before lower priority threads.

If a "DROP TABLE" or "DROP INDEX" SQL command is executed, and the same database connection currently has one or more actively executing SELECT statements, then SQLITE_LOCKED is returned. If [sqlite3_unlock_notify()](c3ref/unlock_notify.md) is called in this case, then the specified callback will be invoked immediately. Re-attempting the "DROP TABLE" or "DROP INDEX" statement will return another SQLITE_LOCKED error. In the implementation of sqlite3_blocking_step() shown to the right, this could cause an infinite loop.

The caller could distinguish between this special "DROP TABLE\|INDEX" case and other cases by using [extended error codes](rescode.md#extrc). When it is appropriate to call [sqlite3_unlock_notify()](c3ref/unlock_notify.md), the extended error code is SQLITE_LOCKED_SHAREDCACHE. Otherwise, in the "DROP TABLE\|INDEX" case, it is just plain SQLITE_LOCKED. Another solution might be to limit the number of times that any single query could be reattempted (to say 100). Although this might be less efficient than one might wish, the situation in question is not likely to occur often.
