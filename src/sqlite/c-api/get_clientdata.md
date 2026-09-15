---
title: Database Connection Client Data
source_url: https://www.sqlite.org/c3ref/get_clientdata.html
source_path: c3ref/get_clientdata.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1340
---

> \
> void \*sqlite3_get_clientdata(sqlite3\*,const char\*);\
> int sqlite3_set_clientdata(sqlite3\*, const char\*, void\*, void(\*)(void\*));\

These functions are used to associate one or more named pointers with a [database connection](../c3ref/sqlite3.md). A call to sqlite3_set_clientdata(D,N,P,X) causes the pointer P to be attached to [database connection](../c3ref/sqlite3.md) D using name N. Subsequent calls to sqlite3_get_clientdata(D,N) will return a copy of pointer P or a NULL pointer if there were no prior calls to sqlite3_set_clientdata() with the same values of D and N. Names are compared using strcmp() and are thus case sensitive. It returns 0 on success and SQLITE_NOMEM on allocation failure.

If P and X are both non-NULL, then the destructor X is invoked with argument P on the first of the following occurrences:

- An out-of-memory error occurs during the call to sqlite3_set_clientdata() which attempts to register pointer P.
- A subsequent call to sqlite3_set_clientdata(D,N,P,X) is made with the same D and N parameters.
- The database connection closes. SQLite does not make any guarantees about the order in which destructors are called, only that all destructors will be called exactly once at some point during the database connection closing process.

SQLite does not do anything with client data other than invoke destructors on the client data at the appropriate time. The intended use for client data is to provide a mechanism for wrapper libraries to store additional information about an SQLite database connection.

There is no limit (other than available memory) on the number of different client data pointers (with different names) that can be attached to a single database connection. However, the current implementation stores the content on a linked list. Insert and retrieval performance will be proportional to the number of entries. The design use case, and the use case for which the implementation is optimized, is that an application will store only small number of client data names, typically just one or two. This interface is not intended to be a generalized key/value store for thousands or millions of keys. It will work for that, but performance might be disappointing.

There is no way to enumerate the client data pointers associated with a database connection. The N parameter can be thought of as a secret key such that only code that knows the secret key is able to access the associated data.

Security Warning: These interfaces should not be exposed in scripting languages or in other circumstances where it might be possible for an attacker to invoke them. Any agent that can invoke these interfaces can probably also take control of the process.

Database connection client data is only available for SQLite version 3.44.0 (2023-11-01) and later.

See also: [sqlite3_set_auxdata()](../c3ref/get_auxdata.md) and [sqlite3_get_auxdata()](../c3ref/get_auxdata.md).

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
