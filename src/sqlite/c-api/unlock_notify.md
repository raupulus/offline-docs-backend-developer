---
title: Unlock Notification
source_url: https://www.sqlite.org/c3ref/unlock_notify.html
source_path: c3ref/unlock_notify.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2130
---

> \
> int sqlite3_unlock_notify(\
>   sqlite3 \*pBlocked,                          /\* Waiting connection \*/\
>   void (\*xNotify)(void \*\*apArg, int nArg),    /\* Callback function to invoke \*/\
>   void \*pNotifyArg                            /\* Argument to pass to xNotify \*/\
> );\

When running in shared-cache mode, a database operation may fail with an [SQLITE_LOCKED](../rescode.md#locked) error if the required locks on the shared-cache or individual tables within the shared-cache cannot be obtained. See [SQLite Shared-Cache Mode](../sharedcache.md) for a description of shared-cache locking. This API may be used to register a callback that SQLite will invoke when the connection currently holding the required lock relinquishes it. This API is only available if the library was compiled with the [SQLITE_ENABLE_UNLOCK_NOTIFY](../compile.md#enable_unlock_notify) C-preprocessor symbol defined.

See Also: [Using the SQLite Unlock Notification Feature](../unlock_notify.md).

Shared-cache locks are released when a database connection concludes its current transaction, either by committing it or rolling it back.

When a connection (known as the blocked connection) fails to obtain a shared-cache lock and SQLITE_LOCKED is returned to the caller, the identity of the database connection (the blocking connection) that has locked the required resource is stored internally. After an application receives an SQLITE_LOCKED error, it may call the sqlite3_unlock_notify() method with the blocked connection handle as the first argument to register for a callback that will be invoked when the blocking connection's current transaction is concluded. The callback is invoked from within the [sqlite3_step](../c3ref/step.md) or [sqlite3_close](../c3ref/close.md) call that concludes the blocking connection's transaction.

If sqlite3_unlock_notify() is called in a multi-threaded application, there is a chance that the blocking connection will have already concluded its transaction by the time sqlite3_unlock_notify() is invoked. If this happens, then the specified callback is invoked immediately, from within the call to sqlite3_unlock_notify().

If the blocked connection is attempting to obtain a write-lock on a shared-cache table, and more than one other connection currently holds a read-lock on the same table, then SQLite arbitrarily selects one of the other connections to use as the blocking connection.

There may be at most one unlock-notify callback registered by a blocked connection. If sqlite3_unlock_notify() is called when the blocked connection already has a registered unlock-notify callback, then the new callback replaces the old. If sqlite3_unlock_notify() is called with a NULL pointer as its second argument, then any existing unlock-notify callback is canceled. The blocked connection's unlock-notify callback may also be canceled by closing the blocked connection using [sqlite3_close()](../c3ref/close.md).

The unlock-notify callback is not reentrant. If an application invokes any sqlite3_xxx API functions from within an unlock-notify callback, a crash or deadlock may be the result.

Unless deadlock is detected (see below), sqlite3_unlock_notify() always returns SQLITE_OK.

**Callback Invocation Details**

When an unlock-notify callback is registered, the application provides a single void\* pointer that is passed to the callback when it is invoked. However, the signature of the callback function allows SQLite to pass it an array of void\* context pointers. The first argument passed to an unlock-notify callback is a pointer to an array of void\* pointers, and the second is the number of entries in the array.

When a blocking connection's transaction is concluded, there may be more than one blocked connection that has registered for an unlock-notify callback. If two or more such blocked connections have specified the same callback function, then instead of invoking the callback function multiple times, it is invoked once with the set of void\* context pointers specified by the blocked connections bundled together into an array. This gives the application an opportunity to prioritize any actions related to the set of unblocked database connections.

**Deadlock Detection**

Assuming that after registering for an unlock-notify callback a database waits for the callback to be issued before taking any further action (a reasonable assumption), then using this API may cause the application to deadlock. For example, if connection X is waiting for connection Y's transaction to be concluded, and similarly connection Y is waiting on connection X's transaction, then neither connection will proceed and the system may remain deadlocked indefinitely.

To avoid this scenario, the sqlite3_unlock_notify() performs deadlock detection. If a given call to sqlite3_unlock_notify() would put the system in a deadlocked state, then SQLITE_LOCKED is returned and no unlock-notify callback is registered. The system is said to be in a deadlocked state if connection A has registered for an unlock-notify callback on the conclusion of connection B's transaction, and connection B has itself registered for an unlock-notify callback when connection A's transaction is concluded. Indirect deadlock is also detected, so the system is also considered to be deadlocked if connection B has registered for an unlock-notify callback on the conclusion of connection C's transaction, where connection C is waiting on connection A. Any number of levels of indirection are allowed.

**The "DROP TABLE" Exception**

When a call to [sqlite3_step()](../c3ref/step.md) returns SQLITE_LOCKED, it is almost always appropriate to call sqlite3_unlock_notify(). There is however, one exception. When executing a "DROP TABLE" or "DROP INDEX" statement, SQLite checks if there are any currently executing SELECT statements that belong to the same connection. If there are, SQLITE_LOCKED is returned. In this case there is no "blocking connection", so invoking sqlite3_unlock_notify() results in the unlock-notify callback being invoked immediately. If the application then re-attempts the "DROP TABLE" or "DROP INDEX" query, an infinite loop might be the result.

One way around this problem is to check the extended error code returned by an sqlite3_step() call. If there is a blocking connection, then the extended error code is set to SQLITE_LOCKED_SHAREDCACHE. Otherwise, in the special "DROP TABLE/INDEX" case, the extended error code is just SQLITE_LOCKED.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
