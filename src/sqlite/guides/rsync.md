---
title: Database Remote-Copy Tool For SQLite
source_url: https://www.sqlite.org/rsync.html
source_path: rsync.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6530
---

<span id="intro"></span>

# 1. Overview

The following command causes REPLICA to become a copy of ORIGIN:

\$ sqlite3_rsync ORIGIN REPLICA ?OPTIONS?\

Use the `--help` or `-?` flag to see the complete list of options. Option flags may appear before, after, or between the ORIGIN and REPLICA arguments.

Add the `-v` option to see more output, in a format similar to "rsync".

# 2. Features

1.  One or the other of ORIGIN or REPLICA may be of the form "USER@HOST:PATH". The other is just a simple PATH. This utility causes REPLICA to become a copy of ORIGIN.
    1.  If REPLICA does not already exist, it is created.

    2.  [ssh](https://en.wikipedia.org/wiki/Secure_Shell) is used for communication, so "USER@HOST" may be an SSH alias.

    3.  It is not required that one of ORIGIN or REPLICA be remote. The sqlite3_rsync utility works fine if both ORIGIN and REPLICA are local.

2.  Both databases may be "live" while this utility is running. Other programs can have active connections to the databases on either end while this utility is running. Other programs can write to ORIGIN and can read from REPLICA while this utility runs.

    REPLICA becomes a copy of a snapshot of ORIGIN as it existed when the sqlite3_rsync command started. If other processes change the content of ORIGIN while this command is running, those changes will be applied to ORIGIN, but they are not transferred to REPLICA Thus, REPLICA ends up as a fully-consistent snapshot of ORIGIN at an instant in time.

3.  The synchronization uses a bandwidth-efficient protocol, similar to [rsync](https://rsync.samba.org) (from which its name is derived).

# 3. Limitations

1.  ~~The database files must both be in [WAL](wal.md) mode, and must have the same page-size.~~ ← These limitations were removed in version 3.50.0 (2025-05-29).

2.  While sqlite3_rsync is running, REPLICA is read-only. Queries can be run against REPLICA while this utility is running, just not write transactions.

3.  Only a single database is synchronized for each invocation of this utility. It is not (yet) possible to synchronize many different databases using wildcards, as it is with standard "rsync".

4.  At least one of ORIGIN or REPLICA must be on the local machine. They cannot both be databases on other machines.

5.  On the remote system, this utility must be installed in one of the directories in the default \$PATH for SSH. The `/usr/local/bin` directory is often a good choice. Alternately, the `--exe NAME` flag may be used to specify a remote location for the binary, e.g. `--exe /opt/bin/sqlite3_rsync`.

6.  The replica will be a very close copy of the origin, but not an exact copy. All of the table (and index) content will be byte-for-byte identical in the replica. However, there can be some minor changes in the [database header](fileformat2.md#database_header). In particular, the replica will have the following differences from the origin:

    1.  The [change counter](fileformat2.md#chngctr) in bytes 24 through 27 of the database header might be incremented in the replica.

    2.  The [version-valid-for number](fileformat2.md#validfor) in bytes in 96 through 99 of the database header will be the SQLite version number of the sqlite3_rsync program that made the copy, not the version number of the last writer to the origin database.

7.  On Windows, a single-letter HOST without a USER@ prefix will be interpreted as a Windows drive-letter, not as a hostname.

# 4. How To Install

Install sqlite3_rsync simply by putting the executable somewhere on your \$PATH. If you are synchronizing with a remote system, the sqlite3_rsync executable must be installed on both the local and the remote system. When installing the sqlite3_rsync executable on the remote system, ensure that it is found on the \$PATH used by SSH. Putting the sqlite3_rsync executable in the /usr/local/bin directory is often a good choice.

Unfortunately, on MacOS, the default PATH for ssh is "/usr/bin:/bin:/usr/sbin:/sbin" and MacOS does not allow you to add new programs to any of those directories. As a work-around, sqlite3_rsync will attempt to augment the PATH like this:

> PATH=\$HOME/bin:/usr/local/bin:/opt/homebrew/bin:\$PATH

So if you are trying to sync with a remote Mac, it should suffice to install the sqlite3_rsync binary in any of the three new PATH locations:

- \$HOME/bin
- /usr/local/bin
- /opt/homebrew/bin

If you need to install sqlite3_rsync in some other (non-standard) place on the remote machine, simply use the --exe option on the command line to specify its precise location. For example:

> sqlite3_rsync sample.db mac:sample.db --exe /some/weird/place/sqlite3_rsync

The writer of this document has never had any success in getting SSHD to run on Windows. Perhaps he will figure that out and be able to provide instructions for syncing a database to or from a remote Windows machine in a future release.

## 4.1. Backwards-Compatibility Issues

The sqlite3_rsync program is designed to negotiate the details of the sync algorithm between the origin and the replica at startup, and to use the most advanced algorithm available on both sides. However, due to a bug in this algorithm negotiation logic (a missing fflush() call) it is possible for the application to hang if you try to use sqlite3_rsync with version 3.50.0 or later on the local side of the connection with version 3.49.1 or earlier on the remote side. Your best solution to this is to install the latest version of sqlite3_rsync on both sides. But if that is not possible, you can work around the problem by adding the "--protocol 1" option to the sqlite3_rsync command-line.

# 5. Network Bandwidth

The core idea behind the protocol is that the replica sends cryptographic hashes for pages or groups of pages over to the origin side. The origin sends back page content that differs, or requests finer-grain hashes if a multi-page hash does not match. If the origin and replica start out being vastly different, the total network bandwidth can exceed the size of the entire database, due to the overhead of exchanging hashes, but the excess bandwidth is not great - a few percent at most. On the other hand, if the origin and replica start out being very similar (the usual case) then the total bandwidth is often less than 0.01% of the database size. In tests, a 500MB database will typically synchronize with about 20KB of network traffic.

Prior to version 3.50.0 (2025-05-29), the protocol would only send hashes of individual pages, not groups of pages. The meant that the bandwidth requirements were usually at least about 0.5% of the database size, even if the two sides started out being identical. Version 3.50.0 and later is more bandwidth efficient if there are few differences between the origin and replica. However, both sides of the connection must have sqlite3_rsync version 3.50.0 or later installed or else the protocol falls back to the older and less bandwidth-efficient algorithm.

# 6. Why Can't I Just Use Ordinary `rsync`?

Ordinary rsync does not understand SQLite transactions. Rsync will make a copy of ORIGIN into REPLICA, however the copy might not be consistent. Parts of the copy might be from one transaction, while other parts might be from a different transaction. The database copy might be corrupt.

If no other processes are connected to the database for the entire time that rsync is running, and if the database does not have a [hot journal](fileformat2.md#hotjrnl), then rsync will make a consistent copy of the database. But if you cannot guarantee that both of those conditions are met, then rsync might generate a corrupt copy. The sqlite3_rsync utility, on the other hand, always generates a consistent copy.
