---
title: Large Objects
source_url: https://www.postgresql.org/docs/17/largeobjects.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: lobj.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 850
---

## Large Objects

large object

BLOB

large object

PostgreSQL has a large object facility, which provides stream-style access to user data that is stored in a special large-object structure. Streaming access is useful when working with data values that are too large to manipulate conveniently as a whole.

This chapter describes the implementation and the programming and query language interfaces to PostgreSQL large object data. We use the libpq C library for the examples in this chapter, but most programming interfaces native to PostgreSQL support equivalent functionality. Other interfaces might use the large object interface internally to provide generic support for large values. This is not described here.

## Introduction

TOAST

versus large objects

All large objects are stored in a single system table named [pg_largeobject](#catalog-pg-largeobject). Each large object also has an entry in the system table [pg_largeobject_metadata](#catalog-pg-largeobject-metadata). Large objects can be created, modified, and deleted using a read/write API that is similar to standard operations on files.

PostgreSQL also supports a storage system called [“TOAST”](#storage-toast), which automatically stores values larger than a single database page into a secondary storage area per table. This makes the large object facility partially obsolete. One remaining advantage of the large object facility is that it allows values up to 4 TB in size, whereas TOASTed fields can be at most 1 GB. Also, reading and updating portions of a large object can be done efficiently, while most operations on a TOASTed field will read or write the whole value as a unit.

## Implementation Features

The large object implementation breaks large objects up into “chunks” and stores the chunks in rows in the database. A B-tree index guarantees fast searches for the correct chunk number when doing random access reads and writes.

The chunks stored for a large object do not have to be contiguous. For example, if an application opens a new large object, seeks to offset 1000000, and writes a few bytes there, this does not result in allocation of 1000000 bytes worth of storage; only of chunks covering the range of data bytes actually written. A read operation will, however, read out zeroes for any unallocated locations preceding the last existing chunk. This corresponds to the common behavior of “sparsely allocated” files in Unix file systems.

As of PostgreSQL 9.0, large objects have an owner and a set of access permissions, which can be managed using [???](#sql-grant) and [???](#sql-revoke). `SELECT` privileges are required to read a large object, and `UPDATE` privileges are required to write or truncate it. Only the large object's owner (or a database superuser) can delete, comment on, or change the owner of a large object. To adjust this behavior for compatibility with prior releases, see the [???](#guc-lo-compat-privileges) run-time parameter.

## Client Interfaces

This section describes the facilities that PostgreSQL's libpq client interface library provides for accessing large objects. The PostgreSQL large object interface is modeled after the Unix file-system interface, with analogues of `open`, `read`, `write`, `lseek`, etc.

All large object manipulation using these functions *must* take place within an SQL transaction block, since large object file descriptors are only valid for the duration of a transaction. Write operations, including `lo_open` with the `INV_WRITE` mode, are not allowed in a read-only transaction.

If an error occurs while executing any one of these functions, the function will return an otherwise-impossible value, typically 0 or -1. A message describing the error is stored in the connection object and can be retrieved with [???](#libpq-PQerrorMessage).

Client applications that use these functions should include the header file `libpq/libpq-fs.h` and link with the libpq library.

Client applications cannot use these functions while a libpq connection is in pipeline mode.

### Creating a Large Object

<span class="indexterm"></span> The function Oid lo_create(PGconn \*conn, Oid lobjId); creates a new large object. The OID to be assigned can be specified by \<lobjId\>; if so, failure occurs if that OID is already in use for some large object. If \<lobjId\> is `InvalidOid` (zero) then `lo_create` assigns an unused OID. The return value is the OID that was assigned to the new large object, or `InvalidOid` (zero) on failure.

An example:

    inv_oid = lo_create(conn, desired_oid);

<span class="indexterm"></span> The older function Oid lo_creat(PGconn \*conn, int mode); also creates a new large object, always assigning an unused OID. The return value is the OID that was assigned to the new large object, or `InvalidOid` (zero) on failure.

In PostgreSQL releases 8.1 and later, the \<mode\> is ignored, so that `lo_creat` is exactly equivalent to `lo_create` with a zero second argument. However, there is little reason to use `lo_creat` unless you need to work with servers older than 8.1. To work with such an old server, you must use `lo_creat` not `lo_create`, and you must set \<mode\> to one of `INV_READ`, `INV_WRITE`, or `INV_READ` `|` `INV_WRITE`. (These symbolic constants are defined in the header file `libpq/libpq-fs.h`.)

An example:

    inv_oid = lo_creat(conn, INV_READ|INV_WRITE);

### Importing a Large Object

<span class="indexterm"></span> To import an operating system file as a large object, call Oid lo_import(PGconn \*conn, const char \*filename); \<filename\> specifies the operating system name of the file to be imported as a large object. The return value is the OID that was assigned to the new large object, or `InvalidOid` (zero) on failure. Note that the file is read by the client interface library, not by the server; so it must exist in the client file system and be readable by the client application.

<span class="indexterm"></span> The function Oid lo_import_with_oid(PGconn \*conn, const char \*filename, Oid lobjId); also imports a new large object. The OID to be assigned can be specified by \<lobjId\>; if so, failure occurs if that OID is already in use for some large object. If \<lobjId\> is `InvalidOid` (zero) then `lo_import_with_oid` assigns an unused OID (this is the same behavior as `lo_import`). The return value is the OID that was assigned to the new large object, or `InvalidOid` (zero) on failure.

`lo_import_with_oid` is new as of PostgreSQL 8.4 and uses `lo_create` internally which is new in 8.1; if this function is run against 8.0 or before, it will fail and return `InvalidOid`.

### Exporting a Large Object

<span class="indexterm"></span> To export a large object into an operating system file, call int lo_export(PGconn \*conn, Oid lobjId, const char \*filename); The `lobjId` argument specifies the OID of the large object to export and the `filename` argument specifies the operating system name of the file. Note that the file is written by the client interface library, not by the server. Returns 1 on success, -1 on failure.

### Opening an Existing Large Object

<span class="indexterm"></span> To open an existing large object for reading or writing, call int lo_open(PGconn \*conn, Oid lobjId, int mode); The `lobjId` argument specifies the OID of the large object to open. The `mode` bits control whether the object is opened for reading (`INV_READ`), writing (`INV_WRITE`), or both. (These symbolic constants are defined in the header file `libpq/libpq-fs.h`.) `lo_open` returns a (non-negative) large object descriptor for later use in `lo_read`, `lo_write`, `lo_lseek`, `lo_lseek64`, `lo_tell`, `lo_tell64`, `lo_truncate`, `lo_truncate64`, and `lo_close`. The descriptor is only valid for the duration of the current transaction. On failure, -1 is returned.

The server currently does not distinguish between modes `INV_WRITE` and `INV_READ` `|` `INV_WRITE`: you are allowed to read from the descriptor in either case. However there is a significant difference between these modes and `INV_READ` alone: with `INV_READ` you cannot write on the descriptor, and the data read from it will reflect the contents of the large object at the time of the transaction snapshot that was active when `lo_open` was executed, regardless of later writes by this or other transactions. Reading from a descriptor opened with `INV_WRITE` returns data that reflects all writes of other committed transactions as well as writes of the current transaction. This is similar to the behavior of `REPEATABLE READ` versus `READ COMMITTED` transaction modes for ordinary SQL `SELECT` commands.

`lo_open` will fail if `SELECT` privilege is not available for the large object, or if `INV_WRITE` is specified and `UPDATE` privilege is not available. (Prior to PostgreSQL 11, these privilege checks were instead performed at the first actual read or write call using the descriptor.) These privilege checks can be disabled with the [???](#guc-lo-compat-privileges) run-time parameter.

An example:

    inv_fd = lo_open(conn, inv_oid, INV_READ|INV_WRITE);

### Writing Data to a Large Object

<span class="indexterm"></span> The function int lo_write(PGconn \*conn, int fd, const char \*buf, size_t len); writes `len` bytes from `buf` (which must be of size `len`) to large object descriptor `fd`. The `fd` argument must have been returned by a previous `lo_open`. The number of bytes actually written is returned (in the current implementation, this will always equal `len` unless there is an error). In the event of an error, the return value is -1.

Although the `len` parameter is declared as `size_t`, this function will reject length values larger than `INT_MAX`. In practice, it's best to transfer data in chunks of at most a few megabytes anyway.

### Reading Data from a Large Object

<span class="indexterm"></span> The function int lo_read(PGconn \*conn, int fd, char \*buf, size_t len); reads up to `len` bytes from large object descriptor `fd` into `buf` (which must be of size `len`). The `fd` argument must have been returned by a previous `lo_open`. The number of bytes actually read is returned; this will be less than `len` if the end of the large object is reached first. In the event of an error, the return value is -1.

Although the `len` parameter is declared as `size_t`, this function will reject length values larger than `INT_MAX`. In practice, it's best to transfer data in chunks of at most a few megabytes anyway.

### Seeking in a Large Object

<span class="indexterm"></span> To change the current read or write location associated with a large object descriptor, call int lo_lseek(PGconn \*conn, int fd, int offset, int whence); This function moves the current location pointer for the large object descriptor identified by `fd` to the new location specified by `offset`. The valid values for `whence` are `SEEK_SET` (seek from object start), `SEEK_CUR` (seek from current position), and `SEEK_END` (seek from object end). The return value is the new location pointer, or -1 on error.

<span class="indexterm"></span> When dealing with large objects that might exceed 2GB in size, instead use pg_int64 lo_lseek64(PGconn \*conn, int fd, pg_int64 offset, int whence); This function has the same behavior as `lo_lseek`, but it can accept an `offset` larger than 2GB and/or deliver a result larger than 2GB. Note that `lo_lseek` will fail if the new location pointer would be greater than 2GB.

`lo_lseek64` is new as of PostgreSQL 9.3. If this function is run against an older server version, it will fail and return -1.

### Obtaining the Seek Position of a Large Object

<span class="indexterm"></span> To obtain the current read or write location of a large object descriptor, call int lo_tell(PGconn \*conn, int fd); If there is an error, the return value is -1.

<span class="indexterm"></span> When dealing with large objects that might exceed 2GB in size, instead use pg_int64 lo_tell64(PGconn \*conn, int fd); This function has the same behavior as `lo_tell`, but it can deliver a result larger than 2GB. Note that `lo_tell` will fail if the current read/write location is greater than 2GB.

`lo_tell64` is new as of PostgreSQL 9.3. If this function is run against an older server version, it will fail and return -1.

### Truncating a Large Object

<span class="indexterm"></span> To truncate a large object to a given length, call int lo_truncate(PGconn \*conn, int fd, size_t len); This function truncates the large object descriptor `fd` to length `len`. The `fd` argument must have been returned by a previous `lo_open`. If `len` is greater than the large object's current length, the large object is extended to the specified length with null bytes ('\0'). On success, `lo_truncate` returns zero. On error, the return value is -1.

The read/write location associated with the descriptor `fd` is not changed.

Although the `len` parameter is declared as `size_t`, `lo_truncate` will reject length values larger than `INT_MAX`.

<span class="indexterm"></span> When dealing with large objects that might exceed 2GB in size, instead use int lo_truncate64(PGconn \*conn, int fd, pg_int64 len); This function has the same behavior as `lo_truncate`, but it can accept a `len` value exceeding 2GB.

`lo_truncate` is new as of PostgreSQL 8.3; if this function is run against an older server version, it will fail and return -1.

`lo_truncate64` is new as of PostgreSQL 9.3; if this function is run against an older server version, it will fail and return -1.

### Closing a Large Object Descriptor

<span class="indexterm"></span> A large object descriptor can be closed by calling int lo_close(PGconn \*conn, int fd); where `fd` is a large object descriptor returned by `lo_open`. On success, `lo_close` returns zero. On error, the return value is -1.

Any large object descriptors that remain open at the end of a transaction will be closed automatically.

### Removing a Large Object

<span class="indexterm"></span> To remove a large object from the database, call int lo_unlink(PGconn \*conn, Oid lobjId); The `lobjId` argument specifies the OID of the large object to remove. Returns 1 if successful, -1 on failure.

## Server-Side Functions

Server-side functions tailored for manipulating large objects from SQL are listed in [SQL-Oriented Large Object Functions](#lo-funcs-table).

<table id="lo-funcs-table">
<caption>SQL-Oriented Large Object Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lo_from_bytea</code> ( <code>loid</code> <code>oid</code>, <code>data</code> <code>bytea</code> ) oid</p>
<p>Creates a large object and stores <code>data</code> in it. If <code>loid</code> is zero then the system will choose a free OID, otherwise that OID is used (with an error if some large object already has that OID). On success, the large object's OID is returned.</p>
<p><code>lo_from_bytea(0, '\xffffff00')</code> 24528</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lo_put</code> ( <code>loid</code> <code>oid</code>, <code>offset</code> <code>bigint</code>, <code>data</code> <code>bytea</code> ) void</p>
<p>Writes <code>data</code> starting at the given offset within the large object; the large object is enlarged if necessary.</p>
<p><code>lo_put(24528, 1, '\xaa')</code></p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>lo_get</code> ( <code>loid</code> <code>oid</code> [, <code>offset</code> <code>bigint</code>, <code>length</code> <code>integer</code>] ) bytea</p>
<p>Extracts the large object's contents, or a substring thereof.</p>
<p><code>lo_get(24528, 0, 3)</code> \xffaaff</p></td>
</tr>
</tbody>
</table>

There are additional server-side functions corresponding to each of the client-side functions described earlier; indeed, for the most part the client-side functions are simply interfaces to the equivalent server-side functions. The ones just as convenient to call via SQL commands are `lo_creat`<span class="indexterm"></span>, `lo_create`, `lo_unlink`<span class="indexterm"></span>, `lo_import`<span class="indexterm"></span>, and `lo_export`<span class="indexterm"></span>. Here are examples of their use:

    CREATE TABLE image (
        name            text,
        raster          oid
    );

    SELECT lo_creat(-1);       -- returns OID of new, empty large object

    SELECT lo_create(43213);   -- attempts to create large object with OID 43213

    SELECT lo_unlink(173454);  -- deletes large object with OID 173454

    INSERT INTO image (name, raster)
        VALUES ('beautiful image', lo_import('/etc/motd'));

    INSERT INTO image (name, raster)  -- same as above, but specify OID to use
        VALUES ('beautiful image', lo_import('/etc/motd', 68583));

    SELECT lo_export(image.raster, '/tmp/motd') FROM image
        WHERE name = 'beautiful image';

The server-side `lo_import` and `lo_export` functions behave considerably differently from their client-side analogs. These two functions read and write files in the server's file system, using the permissions of the database's owning user. Therefore, by default their use is restricted to superusers. In contrast, the client-side import and export functions read and write files in the client's file system, using the permissions of the client program. The client-side functions do not require any database privileges, except the privilege to read or write the large object in question.

> [!CAUTION]
> It is possible to [???](#sql-grant) use of the server-side `lo_import` and `lo_export` functions to non-superusers, but careful consideration of the security implications is required. A malicious user of such privileges could easily parlay them into becoming superuser (for example by rewriting server configuration files), or could attack the rest of the server's file system without bothering to obtain database superuser privileges as such. *Access to roles having such privilege must therefore be guarded just as carefully as access to superuser roles.* Nonetheless, if use of server-side `lo_import` or `lo_export` is needed for some routine task, it's safer to use a role with such privileges than one with full superuser privileges, as that helps to reduce the risk of damage from accidental errors.

The functionality of `lo_read` and `lo_write` is also available via server-side calls, but the names of the server-side functions differ from the client side interfaces in that they do not contain underscores. You must call these functions as `loread` and `lowrite`.

## Example Program

[example_title](#lo-example) is a sample program which shows how the large object interface in libpq can be used. Parts of the program are commented out but are left in the source for the reader's benefit. This program can also be found in `src/test/examples/testlo.c` in the source distribution.

Large Objects with libpq Example Program

    /*-----------------------------------------------------------------
     *
     * testlo.c
     *    test using large objects with libpq
     *
     * Portions Copyright (c) 1996-2024, PostgreSQL Global Development Group
     * Portions Copyright (c) 1994, Regents of the University of California
     *
     *
     * IDENTIFICATION
     *    src/test/examples/testlo.c
     *
     *-----------------------------------------------------------------
     */
    #include <stdio.h>
    #include <stdlib.h>

    #include <sys/types.h>
    #include <sys/stat.h>
    #include <fcntl.h>
    #include <unistd.h>

    #include "libpq-fe.h"
    #include "libpq/libpq-fs.h"

    #define BUFSIZE         1024

    /*
     * importFile -
     *    import file "in_filename" into database as large object "lobjOid"
     *
     */
    static Oid
    importFile(PGconn *conn, char *filename)
    {
        Oid         lobjId;
        int         lobj_fd;
        char        buf[BUFSIZE];
        int         nbytes,
                    tmp;
        int         fd;

        /*
         * open the file to be read in
         */
        fd = open(filename, O_RDONLY, 0666);
        if (fd < 0)
        {                           /* error */
            fprintf(stderr, "cannot open unix file\"%s\"\n", filename);
        }

        /*
         * create the large object
         */
        lobjId = lo_creat(conn, INV_READ | INV_WRITE);
        if (lobjId == 0)
            fprintf(stderr, "cannot create large object");

        lobj_fd = lo_open(conn, lobjId, INV_WRITE);

        /*
         * read in from the Unix file and write to the inversion file
         */
        while ((nbytes = read(fd, buf, BUFSIZE)) > 0)
        {
            tmp = lo_write(conn, lobj_fd, buf, nbytes);
            if (tmp < nbytes)
                fprintf(stderr, "error while reading \"%s\"", filename);
        }

        close(fd);
        lo_close(conn, lobj_fd);

        return lobjId;
    }

    static void
    pickout(PGconn *conn, Oid lobjId, int start, int len)
    {
        int         lobj_fd;
        char       *buf;
        int         nbytes;
        int         nread;

        lobj_fd = lo_open(conn, lobjId, INV_READ);
        if (lobj_fd < 0)
            fprintf(stderr, "cannot open large object %u", lobjId);

        lo_lseek(conn, lobj_fd, start, SEEK_SET);
        buf = malloc(len + 1);

        nread = 0;
        while (len - nread > 0)
        {
            nbytes = lo_read(conn, lobj_fd, buf, len - nread);
            buf[nbytes] = '\0';
            fprintf(stderr, ">>> %s", buf);
            nread += nbytes;
            if (nbytes <= 0)
                break;              /* no more data? */
        }
        free(buf);
        fprintf(stderr, "\n");
        lo_close(conn, lobj_fd);
    }

    static void
    overwrite(PGconn *conn, Oid lobjId, int start, int len)
    {
        int         lobj_fd;
        char       *buf;
        int         nbytes;
        int         nwritten;
        int         i;

        lobj_fd = lo_open(conn, lobjId, INV_WRITE);
        if (lobj_fd < 0)
            fprintf(stderr, "cannot open large object %u", lobjId);

        lo_lseek(conn, lobj_fd, start, SEEK_SET);
        buf = malloc(len + 1);

        for (i = 0; i < len; i++)
            buf[i] = 'X';
        buf[i] = '\0';

        nwritten = 0;
        while (len - nwritten > 0)
        {
            nbytes = lo_write(conn, lobj_fd, buf + nwritten, len - nwritten);
            nwritten += nbytes;
            if (nbytes <= 0)
            {
                fprintf(stderr, "\nWRITE FAILED!\n");
                break;
            }
        }
        free(buf);
        fprintf(stderr, "\n");
        lo_close(conn, lobj_fd);
    }

    /*
     * exportFile -
     *    export large object "lobjOid" to file "out_filename"
     *
     */
    static void
    exportFile(PGconn *conn, Oid lobjId, char *filename)
    {
        int         lobj_fd;
        char        buf[BUFSIZE];
        int         nbytes,
                    tmp;
        int         fd;

        /*
         * open the large object
         */
        lobj_fd = lo_open(conn, lobjId, INV_READ);
        if (lobj_fd < 0)
            fprintf(stderr, "cannot open large object %u", lobjId);

        /*
         * open the file to be written to
         */
        fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0666);
        if (fd < 0)
        {                           /* error */
            fprintf(stderr, "cannot open unix file\"%s\"",
                    filename);
        }

        /*
         * read in from the inversion file and write to the Unix file
         */
        while ((nbytes = lo_read(conn, lobj_fd, buf, BUFSIZE)) > 0)
        {
            tmp = write(fd, buf, nbytes);
            if (tmp < nbytes)
            {
                fprintf(stderr, "error while writing \"%s\"",
                        filename);
            }
        }

        lo_close(conn, lobj_fd);
        close(fd);
    }

    static void
    exit_nicely(PGconn *conn)
    {
        PQfinish(conn);
        exit(1);
    }

    int
    main(int argc, char **argv)
    {
        char       *in_filename,
                   *out_filename;
        char       *database;
        Oid         lobjOid;
        PGconn     *conn;
        PGresult   *res;

        if (argc != 4)
        {
            fprintf(stderr, "Usage: %s database_name in_filename out_filename\n",
                    argv[0]);
            exit(1);
        }

        database = argv[1];
        in_filename = argv[2];
        out_filename = argv[3];

        /*
         * set up the connection
         */
        conn = PQsetdb(NULL, NULL, NULL, NULL, database);

        /* check to see that the backend connection was successfully made */
        if (PQstatus(conn) != CONNECTION_OK)
        {
            fprintf(stderr, "%s", PQerrorMessage(conn));
            exit_nicely(conn);
        }

        /* Set always-secure search path, so malicious users can't take control. */
        res = PQexec(conn,
                     "SELECT pg_catalog.set_config('search_path', '', false)");
        if (PQresultStatus(res) != PGRES_TUPLES_OK)
        {
            fprintf(stderr, "SET failed: %s", PQerrorMessage(conn));
            PQclear(res);
            exit_nicely(conn);
        }
        PQclear(res);

        res = PQexec(conn, "begin");
        PQclear(res);
        printf("importing file \"%s\" ...\n", in_filename);
    /*  lobjOid = importFile(conn, in_filename); */
        lobjOid = lo_import(conn, in_filename);
        if (lobjOid == 0)
            fprintf(stderr, "%s\n", PQerrorMessage(conn));
        else
        {
            printf("\tas large object %u.\n", lobjOid);

            printf("picking out bytes 1000-2000 of the large object\n");
            pickout(conn, lobjOid, 1000, 1000);

            printf("overwriting bytes 1000-2000 of the large object with X's\n");
            overwrite(conn, lobjOid, 1000, 1000);

            printf("exporting large object to file \"%s\" ...\n", out_filename);
    /*      exportFile(conn, lobjOid, out_filename); */
            if (lo_export(conn, lobjOid, out_filename) < 0)
                fprintf(stderr, "%s\n", PQerrorMessage(conn));
        }

        res = PQexec(conn, "end");
        PQclear(res);
        PQfinish(conn);
        return 0;
    }
