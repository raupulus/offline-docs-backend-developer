---
title: SQLite Frequently Asked Questions
source_url: https://www.sqlite.org/faq.html
source_path: faq.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2820
---

## Frequently Asked Questions

1.  [How do I create an AUTOINCREMENT field?](#q1)
2.  [What datatypes does SQLite support?](#q2)
3.  [SQLite lets me insert a string into a database column of type integer!](#q3)
4.  [Why doesn't SQLite allow me to use '0' and '0.0' as the primary key on two different rows of the same table?](#q4)
5.  [Can multiple applications or multiple instances of the same application access a single database file at the same time?](#q5)
6.  [Is SQLite threadsafe?](#q6)
7.  [How do I list all tables/indices contained in an SQLite database](#q7)
8.  [Are there any known size limits to SQLite databases?](#q8)
9.  [What is the maximum size of a VARCHAR in SQLite?](#q9)
10. [Does SQLite support a BLOB type?](#q10)
11. [How do I add, delete or rename columns from an existing table in SQLite?](#q11)
12. [I deleted a lot of data but the database file did not get any smaller. Is this a bug?](#q12)
13. [Can I use SQLite in my commercial product without paying royalties?](#q13)
14. [How do I use a string literal that contains an embedded single-quote (') character?](#q14)
15. [What is an SQLITE_SCHEMA error, and why am I getting one?](#q15)
16. [I get some compiler warnings when I compile SQLite. Isn't this a problem? Doesn't it indicate poor code quality?](#q17)
17. [Case-insensitive matching of Unicode characters does not work.](#q18)
18. [INSERT is really slow - I can only do few dozen INSERTs per second](#q19)
19. [I accidentally deleted some important information from my SQLite database. How can I recover it?](#q20)
20. [What is an SQLITE_CORRUPT error? What does it mean for the database to be "malformed"? Why am I getting this error?](#q21)
21. [Does SQLite support foreign keys?](#q22)
22. [I get a compiler error if I use the SQLITE_OMIT\_... compile-time options when building SQLite.](#q23)
23. [My WHERE clause expression `column1="column1"` does not work. It causes every row of the table to be returned, not just the rows where column1 has the value "column1".](#q24)
24. [How are the syntax diagrams (a.k.a. "railroad" diagrams) for SQLite generated?](#q25)
25. [The SQL standard requires that a UNIQUE constraint be enforced even if one or more of the columns in the constraint are NULL, but SQLite does not do this. Isn't that a bug?](#q26)
26. [What is the Export Control Classification Number (ECCN) for SQLite?](#q27)
27. [My query does not return the column name that I expect. Is this a bug?](#q28)
28. [Where did my database go? (Or: How did my database become empty?)](#q29)

<span id="q1"></span>

**(1) How do I create an AUTOINCREMENT field?**

> Short answer: A column declared [INTEGER PRIMARY KEY](lang_createtable.md#rowid) will autoincrement.
>
> Longer answer: If you declare a column of a table to be [INTEGER PRIMARY KEY](lang_createtable.md#rowid), then whenever you insert a NULL into that column of the table, the NULL is automatically converted into an integer which is one greater than the largest value of that column over all other rows in the table, or 1 if the table is empty. Or, if the largest existing integer key 9223372036854775807 is in use then an unused key value is chosen at random. For example, suppose you have a table like this:
>
> > \
> > CREATE TABLE t1(\
> >   a INTEGER PRIMARY KEY,\
> >   b INTEGER\
> > );\
>
> With this table, the statement
>
> > \
> > INSERT INTO t1 VALUES(NULL,123);\
>
> is logically equivalent to saying:
>
> > \
> > INSERT INTO t1 VALUES((SELECT max(a) FROM t1)+1,123);\
>
> There is a function named [sqlite3_last_insert_rowid()](c3ref/last_insert_rowid.md) which will return the integer key for the most recent insert operation.
>
> Note that the integer key is one greater than the largest key that was in the table just prior to the insert. The new key will be unique over all keys currently in the table, but it might overlap with keys that have been previously deleted from the table. To create keys that are unique over the lifetime of the table, add the [AUTOINCREMENT](autoinc.md) keyword to the [INTEGER PRIMARY KEY](lang_createtable.md#rowid) declaration. Then the key chosen will be one more than the largest key that has ever existed in that table. If the largest possible key has previously existed in that table, then the [INSERT](lang_insert.md) will fail with an [SQLITE_FULL](rescode.md#full) error code.

<span id="q2"></span>

**(2) What datatypes does SQLite support?**

> SQLite uses [dynamic typing](datatype3.md). Content can be stored as INTEGER, REAL, TEXT, BLOB, or as NULL.

<span id="q3"></span>

**(3) SQLite lets me insert a string into a database column of type integer!**

> This is a feature, not a bug. SQLite uses [dynamic typing](datatype3.md). It does not enforce data type constraints. Data of any type can (usually) be inserted into any column. You can put arbitrary length strings into integer columns, floating point numbers in boolean columns, or dates in character columns. The [datatype](datatype3.md) you assign to a column in the CREATE TABLE command does not restrict what data can be put into that column. Every column is able to hold an arbitrary length string. (There is one exception: Columns of type [INTEGER PRIMARY KEY](lang_createtable.md#rowid) may only hold a 64-bit signed integer. An error will result if you try to put anything other than an integer into an [INTEGER PRIMARY KEY](lang_createtable.md#rowid) column.)
>
> But SQLite does use the declared type of a column as a hint that you prefer values in that format. So, for example, if a column is of type INTEGER and you try to insert a string into that column, SQLite will attempt to convert the string into an integer. If it can, it inserts the integer instead. If not, it inserts the string. This feature is called [type affinity](datatype3.md#affinity).

<span id="q4"></span>

**(4) Why doesn't SQLite allow me to use '0' and '0.0' as the primary key on two different rows of the same table?**

> This problem occurs when your primary key is a numeric type. Change the [datatype](datatype3.md) of your primary key to TEXT and it should work.
>
> Every row must have a unique primary key. For a column with a numeric type, SQLite thinks that **'0'** and **'0.0'** are the same value because they compare equal to one another numerically. (See the previous question.) Hence the values are not unique.

<span id="q5"></span>

**(5) Can multiple applications or multiple instances of the same application access a single database file at the same time?**

> Multiple processes can have the same database open at the same time. Multiple processes can be doing a SELECT at the same time. But only one process can be making changes to the database at any moment in time, however.
>
> SQLite uses reader/writer locks to control access to the database. (Under Win95/98/ME which lacks support for reader/writer locks, a probabilistic simulation is used instead.) But use caution: this locking mechanism might not work correctly if the database file is kept on an NFS filesystem. This is because fcntl() file locking is broken on many NFS implementations. You should avoid putting SQLite database files on NFS if multiple processes might try to access the file at the same time. On Windows, Microsoft's documentation says that locking may not work under FAT filesystems if you are not running the Share.exe daemon. People who have a lot of experience with Windows tell me that file locking of network files is very buggy and is not dependable. If what they say is true, sharing an SQLite database between two or more Windows machines might cause unexpected problems.
>
> We are aware of no other *embedded* SQL database engine that supports as much concurrency as SQLite. SQLite allows multiple processes to have the database file open at once, and for multiple processes to read the database at once. When any process wants to write, it must lock the entire database file for the duration of its update. But that normally only takes a few milliseconds. Other processes just wait on the writer to finish then continue about their business. Other embedded SQL database engines typically only allow a single process to connect to the database at once.
>
> However, client/server database engines (such as PostgreSQL, MySQL, or Oracle) usually support a higher level of concurrency and allow multiple processes to be writing to the same database at the same time. This is possible in a client/server database because there is always a single well-controlled server process available to coordinate access. If your application has a need for a lot of concurrency, then you should consider using a client/server database. But experience suggests that most applications need much less concurrency than their designers imagine.
>
> When SQLite tries to access a file that is locked by another process, the default behavior is to return SQLITE_BUSY. You can adjust this behavior from C code using the [sqlite3_busy_handler()](c3ref/busy_handler.md) or [sqlite3_busy_timeout()](c3ref/busy_timeout.md) API functions.

<span id="q6"></span>

**(6) Is SQLite threadsafe?**

> [Threads are evil](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-1.html). Avoid them.
>
> SQLite is threadsafe. We make this concession since many users choose to ignore the advice given in the previous paragraph. But in order to be thread-safe, SQLite must be compiled with the SQLITE_THREADSAFE preprocessor macro set to 1. Both the Windows and Linux precompiled binaries in the distribution are compiled this way. If you are unsure if the SQLite library you are linking against is compiled to be threadsafe you can call the [sqlite3_threadsafe()](c3ref/threadsafe.md) interface to find out.
>
> SQLite is threadsafe because it uses mutexes to serialize access to common data structures. However, the work of acquiring and releasing these mutexes will slow SQLite down slightly. Hence, if you do not need SQLite to be threadsafe, you should disable the mutexes for maximum performance. See the [threading mode](threadsafe.md) documentation for additional information.
>
> Under Unix, you should not carry an open SQLite database across a fork() system call into the child process.

<span id="q7"></span>

**(7) How do I list all tables/indices contained in an SQLite database**

> If you are running the **sqlite3** command-line access program you can type "**.tables**" to get a list of all tables. Or you can type "**.schema**" to see the complete database schema including all tables and indices. Either of these commands can be followed by a LIKE pattern that will restrict the tables that are displayed.
>
> From within a C/C++ program (or a script using Tcl/Ruby/Perl/Python bindings) you can get access to table and index names by doing a SELECT on a special table named "**SQLITE_SCHEMA**". Every SQLite database has an SQLITE_SCHEMA table that defines the schema for the database. The SQLITE_SCHEMA table looks like this:
>
> > \
> > CREATE TABLE sqlite_schema (\
> >   type TEXT,\
> >   name TEXT,\
> >   tbl_name TEXT,\
> >   rootpage INTEGER,\
> >   sql TEXT\
> > );\
>
> For tables, the **type** field will always be **'table'** and the **name** field will be the name of the table. So to get a list of all tables in the database, use the following SELECT command:
>
> > \
> > SELECT name FROM sqlite_schema\
> > WHERE type='table'\
> > ORDER BY name;\
>
> For indices, **type** is equal to **'index'**, **name** is the name of the index and **tbl_name** is the name of the table to which the index belongs. For both tables and indices, the **sql** field is the text of the original CREATE TABLE or CREATE INDEX statement that created the table or index. For automatically created indices (used to implement the PRIMARY KEY or UNIQUE constraints) the **sql** field is NULL.
>
> The SQLITE_SCHEMA table cannot be modified using UPDATE, INSERT, or DELETE (except under [extraordinary conditions](pragma.md#pragma_writable_schema)). The SQLITE_SCHEMA table is automatically updated by commands like CREATE TABLE, CREATE INDEX, DROP TABLE, and DROP INDEX.
>
> Temporary tables do not appear in the SQLITE_SCHEMA table. Temporary tables and their indices and triggers occur in another special table named SQLITE_TEMP_SCHEMA. SQLITE_TEMP_SCHEMA works just like SQLITE_SCHEMA except that it is only visible to the application that created the temporary tables. To get a list of all tables, both permanent and temporary, one can use a command similar to the following:
>
> > \
> > SELECT name FROM \
> >    (SELECT \* FROM sqlite_schema UNION ALL\
> >     SELECT \* FROM sqlite_temp_schema)\
> > WHERE type='table'\
> > ORDER BY name\

<span id="q8"></span>

**(8) Are there any known size limits to SQLite databases?**

> See [limits.html](limits.md) for a full discussion of the limits of SQLite.

<span id="q9"></span>

**(9) What is the maximum size of a VARCHAR in SQLite?**

> SQLite does not enforce the length of a VARCHAR. You can declare a VARCHAR(10) and SQLite will be happy to store a 500-million character string there. And it will keep all 500-million characters intact. Your content is never truncated. SQLite understands the column type of "VARCHAR(*N*)" to be the same as "TEXT", regardless of the value of *N*.

<span id="q10"></span>

**(10) Does SQLite support a BLOB type?**

> SQLite allows you to store BLOB data in any column, even columns that are declared to hold some other type. BLOBs can even be used as PRIMARY KEYs.

<span id="q11"></span>

**(11) How do I add, delete or rename columns from an existing table in SQLite?**

> SQLite has limited ALTER TABLE support that you can use to add, rename or drop columns or to change the name of a table as detailed at [ALTER TABLE](lang_altertable.md).
>
> If you want to make more complex changes in the structure or constraints of a table or its columns, you will have to recreate it. You can save existing data to a temporary table, drop the old table, create the new table, then copy the data back in from the temporary table. See [Making Other Kinds Of Table Schema Changes](lang_altertable.md#otheralter) for procedure.

<span id="q12"></span>

**(12) I deleted a lot of data but the database file did not get any smaller. Is this a bug?**

> No. When you delete information from an SQLite database, the unused disk space is added to an internal "free-list" and is reused the next time you insert data. The disk space is not lost. But neither is it returned to the operating system.
>
> If you delete a lot of data and want to shrink the database file, run the [VACUUM](lang_vacuum.md) command. VACUUM will reconstruct the database from scratch. This will leave the database with an empty free-list and a file that is minimal in size. Note, however, that the VACUUM can take some time to run and it can use up to twice as much temporary disk space as the original file while it is running.
>
> An alternative to using the VACUUM command is auto-vacuum mode, enabled using the [auto_vacuum pragma](pragma.md#pragma_auto_vacuum).

<span id="q13"></span>

**(13) Can I use SQLite in my commercial product without paying royalties?**

> Yes. SQLite is in the [public domain](copyright.md). No claim of ownership is made to any part of the code. You can do anything you want with it.

<span id="q14"></span>

**(14) How do I use a string literal that contains an embedded single-quote (') character?**

> The SQL standard specifies that single-quotes in strings are escaped by putting two single quotes in a row. SQL works like the Pascal programming language in this regard. Example:
>
> > \
> >     INSERT INTO xyz VALUES('5 O''clock');\
> >   

<span id="q15"></span>

**(15) What is an SQLITE_SCHEMA error, and why am I getting one?**

> An [SQLITE_SCHEMA](rescode.md#schema) error is returned when a prepared SQL statement is no longer valid and cannot be executed. When this occurs, the statement must be recompiled from SQL using the [sqlite3_prepare()](c3ref/prepare.md) API. An SQLITE_SCHEMA error can only occur when using the [sqlite3_prepare()](c3ref/prepare.md), and [sqlite3_step()](c3ref/step.md) interfaces to run SQL. You will never receive an [SQLITE_SCHEMA](rescode.md#schema) error from [sqlite3_exec()](c3ref/exec.md). Nor will you receive an error if you prepare statements using [sqlite3_prepare_v2()](c3ref/prepare.md) instead of [sqlite3_prepare()](c3ref/prepare.md).
>
> The [sqlite3_prepare_v2()](c3ref/prepare.md) interface creates a [prepared statement](c3ref/stmt.md) that will automatically recompile itself if the schema changes. The easiest way to deal with [SQLITE_SCHEMA](rescode.md#schema) errors is to always use [sqlite3_prepare_v2()](c3ref/prepare.md) instead of [sqlite3_prepare()](c3ref/prepare.md).

<span id="q17"></span>

**(17) I get some compiler warnings when I compile SQLite. Isn't this a problem? Doesn't it indicate poor code quality?**

> Quality assurance in SQLite is done using [full-coverage testing](testing.md#coverage), not by compiler warnings or other static code analysis tools. In other words, we verify that SQLite actually gets the correct answer, not that it merely satisfies stylistic constraints. Most of the SQLite code base is devoted purely to testing. The SQLite test suite runs tens of thousands of separate test cases and many of those test cases are parameterized so that hundreds of millions of tests involving billions of SQL statements are run and evaluated for correctness prior to every release. The developers use code coverage tools to verify that all paths through the code are tested. Whenever a bug is found in SQLite, new test cases are written to exhibit the bug so that the bug cannot recur undetected in the future.
>
> During testing, the SQLite library is compiled with special instrumentation that allows the test scripts to simulate a wide variety of failures in order to verify that SQLite recovers correctly. Memory allocation is carefully tracked and no memory leaks occur, even following memory allocation failures. A custom VFS layer is used to simulate operating system crashes and power failures in order to ensure that transactions are atomic across these events. A mechanism for deliberately injecting I/O errors shows that SQLite is resilient to such malfunctions. (As an experiment, try inducing these kinds of errors on other SQL database engines and see what happens!)
>
> We also run SQLite using [Valgrind](http://valgrind.org) on Linux and verify that it detects no problems.
>
> Some people say that we should eliminate all warnings because benign warnings mask real warnings that might arise in future changes. This is true enough. But in reply, the developers observe that all warnings have already been fixed in the builds used for SQLite development (various versions of GCC, MSVC, and clang). Compiler warnings usually only arise from compilers or compile-time options that the SQLite developers do not use themselves.

<span id="q18"></span>

**(18) Case-insensitive matching of Unicode characters does not work.**

> The default configuration of SQLite only supports case-insensitive comparisons of ASCII characters. The reason for this is that doing full Unicode case-insensitive comparisons and case conversions requires tables and logic that would nearly double the size of the SQLite library. The SQLite developers reason that any application that needs full Unicode case support probably already has the necessary tables and functions and so SQLite should not take up space to duplicate this ability.
>
> Instead of providing full Unicode case support by default, SQLite provides the ability to link against external Unicode comparison and conversion routines. The application can overload the built-in [NOCASE](datatype3.md#collation) collating sequence (using [sqlite3_create_collation()](c3ref/create_collation.md)) and the built-in [like()](lang_corefunc.md#like), [upper()](lang_corefunc.md#upper), and [lower()](lang_corefunc.md#lower) functions (using [sqlite3_create_function()](c3ref/create_function.md)). The SQLite source code includes an "ICU" extension that does these overloads. Or, developers can write their own overloads based on their own Unicode-aware comparison routines already contained within their project.

<span id="q19"></span>

**(19) INSERT is really slow - I can only do few dozen INSERTs per second**

> Actually, SQLite will easily do 50,000 or more [INSERT](lang_insert.md) statements per second on an average desktop computer. But it will only do a few dozen transactions per second. Transaction speed is limited by the rotational speed of your disk drive. A transaction normally requires two complete rotations of the disk platter, which on a 7200RPM disk drive limits you to about 60 transactions per second.
>
> Transaction speed is limited by disk drive speed because (by default) SQLite actually waits until the data really is safely stored on the disk surface before the transaction is complete. That way, if you suddenly lose power or if your OS crashes, your data is still safe. For details, read about [atomic commit in SQLite.](atomiccommit.md).
>
> By default, each INSERT statement is its own transaction. But if you surround multiple INSERT statements with [BEGIN](lang_transaction.md)...[COMMIT](lang_transaction.md) then all the inserts are grouped into a single transaction. The time needed to commit the transaction is amortized over all the enclosed insert statements and so the time per insert statement is greatly reduced.
>
> Another option is to run [PRAGMA synchronous=OFF](pragma.md#pragma_synchronous). This command will cause SQLite to not wait on data to reach the disk surface, which will make write operations appear to be much faster. But if you lose power in the middle of a transaction, your database file might go corrupt.
>
> ***Update 2024-11-19:** The text above is a really old answer. SQLite will do far more than 50K inserts/second now, and everybody uses SSD nowadays, making the performance faster still. But the gist of the answer above remains correct: Putting multiple operations inside a single transaction can improve performance dramatically by avoiding the overhead of transaction control after each individual operation.*

<span id="q20"></span>

**(20) I accidentally deleted some important information from my SQLite database. How can I recover it?**

> If you have a backup copy of your database file, recover the information from your backup.
>
> If you do not have a backup, recovery is very difficult. You might be able to find partial string data in a binary dump of the raw database file. Recovering numeric data might also be possible given special tools, though to our knowledge no such tools exist. SQLite is sometimes compiled with the [SQLITE_SECURE_DELETE](compile.md#secure_delete) option which overwrites all deleted content with zeros. If that is the case then recovery is clearly impossible. Recovery is also impossible if you have run [VACUUM](lang_vacuum.md) since the data was deleted. If SQLITE_SECURE_DELETE is not used and VACUUM has not been run, then some of the deleted content might still be in the database file, in areas marked for reuse. But, again, there exist no procedures or tools that we know of to help you recover that data.

<span id="q21"></span>

**(21) What is an SQLITE_CORRUPT error? What does it mean for the database to be "malformed"? Why am I getting this error?**

> An [SQLITE_CORRUPT](rescode.md#corrupt) error is returned when SQLite detects an error in the structure, format, or other control elements of the database file.
>
> SQLite does not corrupt database files without external help. If your application crashes in the middle of an update, your data is safe. The database is safe even if your OS crashes or takes a power loss. The crash-resistance of SQLite has been extensively studied and tested and is attested by years of real-world experience by billions of users.
>
> That said, there are a number of things that external programs or bugs in your hardware or OS can do to corrupt a database file. See [How To Corrupt An SQLite Database File](howtocorrupt.md) for further information.
>
> You can use [PRAGMA integrity_check](pragma.md#pragma_integrity_check) to do a thorough but time intensive test of the database integrity.
>
> You can use [PRAGMA quick_check](pragma.md#pragma_quick_check) to do a faster but less thorough test of the database integrity.
>
> Depending how badly your database is corrupted, you may be able to recover some of the data by using the CLI to dump the schema and contents to a file and then recreate. Unfortunately, once humpty-dumpty falls off the wall, it is generally not possible to put him back together again.

<span id="q22"></span>

**(22) Does SQLite support foreign keys?**

> As of [version 3.6.19](releaselog/3_6_19.md) (2009-10-14), SQLite supports [foreign key constraints](foreignkeys.md). But enforcement of foreign key constraints is turned off by default (for backwards compatibility). To enable foreign key constraint enforcement, run [PRAGMA foreign_keys=ON](pragma.md#pragma_foreign_keys) or compile with [-DSQLITE_DEFAULT_FOREIGN_KEYS=1](compile.md#default_foreign_keys).

<span id="q23"></span>

**(23) I get a compiler error if I use the SQLITE_OMIT\_... compile-time options when building SQLite.**

> The [SQLITE_OMIT\_...](compile.md#omitfeatures) compile-time options only work when building from canonical source files. They do <u>not</u> work when you build from the SQLite [amalgamation](amalgamation.md) or from the pre-processed source files.
>
> It is possible to build a special [amalgamation](amalgamation.md) that will work with a predetermined set of SQLITE_OMIT\_... options. Instructions for doing so can be found with the [SQLITE_OMIT\_... documentation](compile.md#omitfeatures).

<span id="q24"></span>

**(24) My WHERE clause expression `column1="column1"` does not work. It causes every row of the table to be returned, not just the rows where column1 has the value "column1".**

> Use single-quotes, not double-quotes, around string literals in SQL. This is what the SQL standard requires. Your WHERE clause expression should read: `column1='column1'`
>
> SQL uses double-quotes around identifiers (column or table names) that contains special characters or which are keywords. So double-quotes are a way of escaping identifier names. Hence, when you say `column1="column1"` that is equivalent to `column1=column1` which is obviously always true.

<span id="q25"></span>

**(25) How are the syntax diagrams (a.k.a. "railroad" diagrams) for SQLite generated?**

> Each diagram is hand-written using the [Pikchr](https://pikchr.org/) diagramming language. These hand-written specifications are converted into SVG and inserted inline in the HTML files as part of the documentation build process.
>
> Many historical versions of the SQLite documentation used a different process for generating the syntax diagrams. The historical process was based on Tcl/Tk and is described at <http://wiki.tcl-lang.org/21708>. The newer Pikchr-based syntax diagrams first landed on trunk on 2020-09-26.

<span id="q26"></span>

**(26) The SQL standard requires that a UNIQUE constraint be enforced even if one or more of the columns in the constraint are NULL, but SQLite does not do this. Isn't that a bug?**

> Perhaps you are referring to the following statement from SQL92:
>
> > A unique constraint is satisfied if and only if no two rows in a table have the same non-null values in the unique columns.
>
> That statement is ambiguous, having at least two possible interpretations:
>
> 1.  A unique constraint is satisfied if and only if no two rows in a table have the same values and have non-null values in the unique columns.
> 2.  A unique constraint is satisfied if and only if no two rows in a table have the same values in the subset of unique columns that are not null.
>
> SQLite follows interpretation (1), as does PostgreSQL, MySQL, Oracle, and Firebird. It is true that Informix and Microsoft SQL Server use interpretation (2), however we the SQLite developers hold that interpretation (1) is the most natural reading of the requirement and we also want to maximize compatibility with other SQL database engines, and most other database engines also go with (1), so that is what SQLite does.

<span id="q27"></span>

**(27) What is the Export Control Classification Number (ECCN) for SQLite?**

> After careful review of the Commerce Control List (CCL), we are convinced that the core public-domain SQLite source code is not described by any ECCN, hence the ECCN should be reported as **EAR99**.
>
> The above is true for the core public-domain SQLite. If you extend SQLite by adding new code, or if you statically link SQLite with your application, that might change the ECCN in your particular case.

<span id="q28"></span>

**(28) My query does not return the column name that I expect. Is this a bug?**

> If the columns of your result set are named by AS clauses, then SQLite is guaranteed to use the identifier to the right of the AS keyword as the column name. If the result set does not use an AS clause, then SQLite is free to name the column anything it wants. See the [sqlite3_column_name()](c3ref/column_name.md) documentation for further information.

<span id="q29"></span>

**(29) Where did my database go? (Or: How did my database become empty?)**

> Unless opened with flags to prevent it, a SQLite database is created if it does not already exist. Newly created databases are initially empty. This can confuse people who inadvertantly open different database files in different contexts, due to either a typo in the filename or use of a relative pathname that is used with differing current directories for the opening processes.
