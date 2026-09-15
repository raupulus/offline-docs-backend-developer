---
title: Server Setup and Operation
source_url: https://www.postgresql.org/docs/17/runtime.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: runtime.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3490
---

## Server Setup and Operation

This chapter discusses how to set up and run the database server, and its interactions with the operating system.

The directions in this chapter assume that you are working with plain PostgreSQL without any additional infrastructure, for example a copy that you built from source according to the directions in the preceding chapters. If you are working with a pre-packaged or vendor-supplied version of PostgreSQL, it is likely that the packager has made special provisions for installing and starting the database server according to your system's conventions. Consult the package-level documentation for details.

## The PostgreSQL User Account

postgres user

As with any server daemon that is accessible to the outside world, it is advisable to run PostgreSQL under a separate user account. This user account should only own the data that is managed by the server, and should not be shared with other daemons. (For example, using the user `nobody` is a bad idea.) In particular, it is advisable that this user account not own the PostgreSQL executable files, to ensure that a compromised server process could not modify those executables.

Pre-packaged versions of PostgreSQL will typically create a suitable user account automatically during package installation.

To add a Unix user account to your system, look for a command `useradd` or `adduser`. The user name `postgres` is often used, and is assumed throughout this book, but you can use another name if you like.

## Creating a Database Cluster

database cluster

data area

database cluster

Before you can do anything, you must initialize a database storage area on disk. We call this a database cluster. (The SQL standard uses the term catalog cluster.) A database cluster is a collection of databases that is managed by a single instance of a running database server. After initialization, a database cluster will contain a database named `postgres`, which is meant as a default database for use by utilities, users and third party applications. The database server itself does not require the `postgres` database to exist, but many external utility programs assume it exists. There are two more databases created within each cluster during initialization, named `template1` and `template0`. As the names suggest, these will be used as templates for subsequently-created databases; they should not be used for actual work. (See [???](#managing-databases) for information about creating new databases within a cluster.)

In file system terms, a database cluster is a single directory under which all data will be stored. We call this the data directory or data area. It is completely up to you where you choose to store your data. There is no default, although locations such as `/usr/local/pgsql/data` or `/var/lib/pgsql/data` are popular. The data directory must be initialized before being used, using the program [???](#app-initdb)<span class="indexterm"></span> which is installed with PostgreSQL.

If you are using a pre-packaged version of PostgreSQL, it may well have a specific convention for where to place the data directory, and it may also provide a script for creating the data directory. In that case you should use that script in preference to running `initdb` directly. Consult the package-level documentation for details.

To initialize a database cluster manually, run `initdb` and specify the desired file system location of the database cluster with the `-D` option, for example:

    $ initdb -D /usr/local/pgsql/data

Note that you must execute this command while logged into the PostgreSQL user account, which is described in the previous section.

> [!TIP]
> As an alternative to the `-D` option, you can set the environment variable `PGDATA`. <span class="indexterm"></span>

Alternatively, you can run `initdb` via the [???](#app-pg-ctl) program<span class="indexterm"></span> like so:

    $ pg_ctl -D /usr/local/pgsql/data initdb

This may be more intuitive if you are using `pg_ctl` for starting and stopping the server (see [Starting the Database Server](#server-start)), so that `pg_ctl` would be the sole command you use for managing the database server instance.

`initdb` will attempt to create the directory you specify if it does not already exist. Of course, this will fail if `initdb` does not have permissions to write in the parent directory. It's generally recommendable that the PostgreSQL user own not just the data directory but its parent directory as well, so that this should not be a problem. If the desired parent directory doesn't exist either, you will need to create it first, using root privileges if the grandparent directory isn't writable. So the process might look like this:

    root# mkdir /usr/local/pgsql
    root# chown postgres /usr/local/pgsql
    root# su postgres
    postgres$ initdb -D /usr/local/pgsql/data

`initdb` will refuse to run if the data directory exists and already contains files; this is to prevent accidentally overwriting an existing installation.

Because the data directory contains all the data stored in the database, it is essential that it be secured from unauthorized access. `initdb` therefore revokes access permissions from everyone but the PostgreSQL user, and optionally, group. Group access, when enabled, is read-only. This allows an unprivileged user in the same group as the cluster owner to take a backup of the cluster data or perform other operations that only require read access.

Note that enabling or disabling group access on an existing cluster requires the cluster to be shut down and the appropriate mode to be set on all directories and files before restarting PostgreSQL. Otherwise, a mix of modes might exist in the data directory. For clusters that allow access only by the owner, the appropriate modes are `0700` for directories and `0600` for files. For clusters that also allow reads by the group, the appropriate modes are `0750` for directories and `0640` for files.

However, while the directory contents are secure, the default client authentication setup allows any local user to connect to the database and even become the database superuser. If you do not trust other local users, we recommend you use one of `initdb`'s `-W`, `--pwprompt` or `--pwfile` options to assign a password to the database superuser.<span class="indexterm"></span> Also, specify `-A scram-sha-256` so that the default `trust` authentication mode is not used; or modify the generated `pg_hba.conf` file after running `initdb`, but *before* you start the server for the first time. (Other reasonable approaches include using `peer` authentication or file system permissions to restrict connections. See [???](#client-authentication) for more information.)

`initdb` also initializes the default locale<span class="indexterm"></span> for the database cluster. Normally, it will just take the locale settings in the environment and apply them to the initialized database. It is possible to specify a different locale for the database; more information about that can be found in [???](#locale). The default sort order used within the particular database cluster is set by `initdb`, and while you can create new databases using different sort order, the order used in the template databases that initdb creates cannot be changed without dropping and recreating them. There is also a performance impact for using locales other than `C` or `POSIX`. Therefore, it is important to make this choice correctly the first time.

`initdb` also sets the default character set encoding for the database cluster. Normally this should be chosen to match the locale setting. For details see [???](#multibyte).

Non-`C` and non-`POSIX` locales rely on the operating system's collation library for character set ordering. This controls the ordering of keys stored in indexes. For this reason, a cluster cannot switch to an incompatible collation library version, either through snapshot restore, binary streaming replication, a different operating system, or an operating system upgrade.

### Use of Secondary File Systems

file system mount points

Many installations create their database clusters on file systems (volumes) other than the machine's “root” volume. If you choose to do this, it is not advisable to try to use the secondary volume's topmost directory (mount point) as the data directory. Best practice is to create a directory within the mount-point directory that is owned by the PostgreSQL user, and then create the data directory within that. This avoids permissions problems, particularly for operations such as pg_upgrade, and it also ensures clean failures if the secondary volume is taken offline.

### File Systems

Generally, any file system with POSIX semantics can be used for PostgreSQL. Users prefer different file systems for a variety of reasons, including vendor support, performance, and familiarity. Experience suggests that, all other things being equal, one should not expect major performance or behavior changes merely from switching file systems or making minor file system configuration changes.

#### NFS

NFS

It is possible to use an NFS file system for storing the PostgreSQL data directory. PostgreSQL does nothing special for NFS file systems, meaning it assumes NFS behaves exactly like locally-connected drives. PostgreSQL does not use any functionality that is known to have nonstandard behavior on NFS, such as file locking.

The only firm requirement for using NFS with PostgreSQL is that the file system is mounted using the `hard` option. With the `hard` option, processes can “hang” indefinitely if there are network problems, so this configuration will require a careful monitoring setup. The `soft` option will interrupt system calls in case of network problems, but PostgreSQL will not repeat system calls interrupted in this way, so any such interruption will result in an I/O error being reported.

It is not necessary to use the `sync` mount option. The behavior of the `async` option is sufficient, since PostgreSQL issues `fsync` calls at appropriate times to flush the write caches. (This is analogous to how it works on a local file system.) However, it is strongly recommended to use the `sync` export option on the NFS *server* on systems where it exists (mainly Linux). Otherwise, an `fsync` or equivalent on the NFS client is not actually guaranteed to reach permanent storage on the server, which could cause corruption similar to running with the parameter [???](#guc-fsync) off. The defaults of these mount and export options differ between vendors and versions, so it is recommended to check and perhaps specify them explicitly in any case to avoid any ambiguity.

In some cases, an external storage product can be accessed either via NFS or a lower-level protocol such as iSCSI. In the latter case, the storage appears as a block device and any available file system can be created on it. That approach might relieve the DBA from having to deal with some of the idiosyncrasies of NFS, but of course the complexity of managing remote storage then happens at other levels.

## Starting the Database Server

Before anyone can access the database, you must start the database server. The database server program is called `postgres`.<span class="indexterm"></span>

If you are using a pre-packaged version of PostgreSQL, it almost certainly includes provisions for running the server as a background task according to the conventions of your operating system. Using the package's infrastructure to start the server will be much less work than figuring out how to do this yourself. Consult the package-level documentation for details.

The bare-bones way to start the server manually is just to invoke `postgres` directly, specifying the location of the data directory with the `-D` option, for example:

    $ postgres -D /usr/local/pgsql/data

which will leave the server running in the foreground. This must be done while logged into the PostgreSQL user account. Without `-D`, the server will try to use the data directory named by the environment variable `PGDATA`. If that variable is not provided either, it will fail.

Normally it is better to start `postgres` in the background. For this, use the usual Unix shell syntax:

    $ postgres -D /usr/local/pgsql/data >logfile 2>&1 &

It is important to store the server's `stdout` and `stderr` output somewhere, as shown above. It will help for auditing purposes and to diagnose problems. (See [???](#logfile-maintenance) for a more thorough discussion of log file handling.)

The `postgres` program also takes a number of other command-line options. For more information, see the [???](#app-postgres) reference page and [???](#runtime-config) below.

This shell syntax can get tedious quickly. Therefore the wrapper program [???](#app-pg-ctl)<span class="indexterm"></span> is provided to simplify some tasks. For example:

    pg_ctl start -l logfile

will start the server in the background and put the output into the named log file. The `-D` option has the same meaning here as for `postgres`. `pg_ctl` is also capable of stopping the server.

Normally, you will want to start the database server when the computer boots.<span class="indexterm"></span> Autostart scripts are operating-system-specific. There are a few example scripts distributed with PostgreSQL in the `contrib/start-scripts` directory. Installing one will require root privileges.

Different systems have different conventions for starting up daemons at boot time. Many systems have a file `/etc/rc.local` or `/etc/rc.d/rc.local`. Others use `init.d` or `rc.d` directories. Whatever you do, the server must be run by the PostgreSQL user account *and not by root* or any other user. Therefore you probably should form your commands using `su postgres -c '...'`. For example:

    su postgres -c 'pg_ctl start -D /usr/local/pgsql/data -l serverlog'

Here are a few more operating-system-specific suggestions. (In each case be sure to use the proper installation directory and user name where we show generic values.)

- For FreeBSD, look at the file `contrib/start-scripts/freebsd` in the PostgreSQL source distribution. <span class="indexterm"></span>

- On OpenBSD, add the following lines to the file `/etc/rc.local`: <span class="indexterm"></span>

      if [ -x /usr/local/pgsql/bin/pg_ctl -a -x /usr/local/pgsql/bin/postgres ]; then
          su -l postgres -c '/usr/local/pgsql/bin/pg_ctl start -s -l /var/postgresql/log -D /usr/local/pgsql/data'
          echo -n ' postgresql'
      fi

- On Linux systems either add <span class="indexterm"></span>

      /usr/local/pgsql/bin/pg_ctl start -l logfile -D /usr/local/pgsql/data

  to `/etc/rc.d/rc.local` or `/etc/rc.local` or look at the file `contrib/start-scripts/linux` in the PostgreSQL source distribution.

  When using systemd, you can use the following service unit file (e.g., at `/etc/systemd/system/postgresql.service`):<span class="indexterm"></span>

      [Unit]
      Description=PostgreSQL database server
      Documentation=man:postgres(1)
      After=network-online.target
      Wants=network-online.target

      [Service]
      Type=notify
      User=postgres
      ExecStart=/usr/local/pgsql/bin/postgres -D /usr/local/pgsql/data
      ExecReload=/bin/kill -HUP $MAINPID
      KillMode=mixed
      KillSignal=SIGINT
      TimeoutSec=infinity

      [Install]
      WantedBy=multi-user.target

  Using `Type=notify` requires that the server binary was built with `configure --with-systemd`.

  Consider carefully the timeout setting. systemd has a default timeout of 90 seconds as of this writing and will kill a process that does not report readiness within that time. But a PostgreSQL server that might have to perform crash recovery at startup could take much longer to become ready. The suggested value of `infinity` disables the timeout logic.

- On NetBSD, use either the FreeBSD or Linux start scripts, depending on preference. <span class="indexterm"></span>

- On Solaris, create a file called `/etc/init.d/postgresql` that contains the following line: <span class="indexterm"></span>

      su - postgres -c "/usr/local/pgsql/bin/pg_ctl start -l logfile -D /usr/local/pgsql/data"

  Then, create a symbolic link to it in `/etc/rc3.d` as `S99postgresql`.

While the server is running, its PID is stored in the file `postmaster.pid` in the data directory. This is used to prevent multiple server instances from running in the same data directory and can also be used for shutting down the server.

### Server Start-up Failures

There are several common reasons the server might fail to start. Check the server's log file, or start it by hand (without redirecting standard output or standard error) and see what error messages appear. Below we explain some of the most common error messages in more detail.

    LOG:  could not bind IPv4 address "127.0.0.1": Address already in use
    HINT:  Is another postmaster already running on port 5432? If not, wait a few seconds and retry.
    FATAL:  could not create any TCP/IP sockets

This usually means just what it suggests: you tried to start another server on the same port where one is already running. However, if the kernel error message is not `Address already in use` or some variant of that, there might be a different problem. For example, trying to start a server on a reserved port number might draw something like:

    $ postgres -p 666
    LOG:  could not bind IPv4 address "127.0.0.1": Permission denied
    HINT:  Is another postmaster already running on port 666? If not, wait a few seconds and retry.
    FATAL:  could not create any TCP/IP sockets

A message like:

    FATAL:  could not create shared memory segment: Invalid argument
    DETAIL:  Failed system call was shmget(key=5440001, size=4011376640, 03600).

probably means your kernel's limit on the size of shared memory is smaller than the work area PostgreSQL is trying to create (4011376640 bytes in this example). This is only likely to happen if you have set `shared_memory_type` to `sysv`. In that case, you can try starting the server with a smaller-than-normal number of buffers ([???](#guc-shared-buffers)), or reconfigure your kernel to increase the allowed shared memory size. You might also see this message when trying to start multiple servers on the same machine, if their total space requested exceeds the kernel limit.

An error like:

    FATAL:  could not create semaphores: No space left on device
    DETAIL:  Failed system call was semget(5440126, 17, 03600).

does *not* mean you've run out of disk space. It means your kernel's limit on the number of `System V` semaphores is smaller than the number PostgreSQL wants to create. As above, you might be able to work around the problem by starting the server with a reduced number of allowed connections ([???](#guc-max-connections)), but you'll eventually want to increase the kernel limit.

Details about configuring `System V` IPC facilities are given in [Shared Memory and Semaphores](#sysvipc).

### Client Connection Problems

Although the error conditions possible on the client side are quite varied and application-dependent, a few of them might be directly related to how the server was started. Conditions other than those shown below should be documented with the respective client application.

    psql: error: connection to server at "server.joe.com" (123.123.123.123), port 5432 failed: Connection refused
            Is the server running on that host and accepting TCP/IP connections?

This is the generic “I couldn't find a server to talk to” failure. It looks like the above when TCP/IP communication is attempted. A common mistake is to forget to configure the server to allow TCP/IP connections.

Alternatively, you might get this when attempting Unix-domain socket communication to a local server:

    psql: error: connection to server on socket "/tmp/.s.PGSQL.5432" failed: No such file or directory
            Is the server running locally and accepting connections on that socket?

If the server is indeed running, check that the client's idea of the socket path (here `/tmp`) agrees with the server's [???](#guc-unix-socket-directories) setting.

A connection failure message always shows the server address or socket path name, which is useful in verifying that the client is trying to connect to the right place. If there is in fact no server listening there, the kernel error message will typically be either `Connection refused` or `No such file or directory`, as illustrated. (It is important to realize that `Connection refused` in this context does *not* mean that the server got your connection request and rejected it. That case will produce a different message, as shown in [???](#client-authentication-problems).) Other error messages such as `Connection timed out` might indicate more fundamental problems, like lack of network connectivity, or a firewall blocking the connection.

## Managing Kernel Resources

PostgreSQL can sometimes exhaust various operating system resource limits, especially when multiple copies of the server are running on the same system, or in very large installations. This section explains the kernel resources used by PostgreSQL and the steps you can take to resolve problems related to kernel resource consumption.

### Shared Memory and Semaphores

shared memory

semaphores

PostgreSQL requires the operating system to provide inter-process communication (IPC) features, specifically shared memory and semaphores. Unix-derived systems typically provide “`System V`” IPC, “`POSIX`” IPC, or both. `Windows` has its own implementation of these features and is not discussed here.

By default, PostgreSQL allocates a very small amount of System V shared memory, as well as a much larger amount of anonymous `mmap` shared memory. Alternatively, a single large System V shared memory region can be used (see [???](#guc-shared-memory-type)). In addition a significant number of semaphores, which can be either System V or POSIX style, are created at server startup. Currently, POSIX semaphores are used on Linux and FreeBSD systems while other platforms use System V semaphores.

System V IPC features are typically constrained by system-wide allocation limits. When PostgreSQL exceeds one of these limits, the server will refuse to start and should leave an instructive error message describing the problem and what to do about it. (See also [Server Start-up Failures](#server-start-failures).) The relevant kernel parameters are named consistently across different systems; [ Parameters](#sysvipc-parameters) gives an overview. The methods to set them, however, vary. Suggestions for some platforms are given below.

| Name | Description | Values needed to run one PostgreSQL instance |
|----|----|----|
| `SHMMAX` | Maximum size of shared memory segment (bytes) | at least 1kB, but the default is usually much higher |
| `SHMMIN` | Minimum size of shared memory segment (bytes) | 1 |
| `SHMALL` | Total amount of shared memory available (bytes or pages) | same as `SHMMAX` if bytes, or `ceil(SHMMAX/PAGE_SIZE)` if pages, plus room for other applications |
| `SHMSEG` | Maximum number of shared memory segments per process | only 1 segment is needed, but the default is much higher |
| `SHMMNI` | Maximum number of shared memory segments system-wide | like `SHMSEG` plus room for other applications |
| `SEMMNI` | Maximum number of semaphore identifiers (i.e., sets) | at least `ceil((max_connections + autovacuum_max_workers + max_wal_senders + max_worker_processes + 7) / 19)` plus room for other applications |
| `SEMMNS` | Maximum number of semaphores system-wide | `ceil((max_connections + autovacuum_max_workers + max_wal_senders + max_worker_processes + 7) / 19) * 20` plus room for other applications |
| `SEMMSL` | Maximum number of semaphores per set | at least 20 |
| `SEMMAP` | Number of entries in semaphore map | see text |
| `SEMVMX` | Maximum value of semaphore | at least 1000 (The default is often 32767; do not change unless necessary) |

`System V` IPC Parameters {#sysvipc-parameters}

PostgreSQL requires a few bytes of System V shared memory (typically 48 bytes, on 64-bit platforms) for each copy of the server. On most modern operating systems, this amount can easily be allocated. However, if you are running many copies of the server or you explicitly configure the server to use large amounts of System V shared memory (see [???](#guc-shared-memory-type) and [???](#guc-dynamic-shared-memory-type)), it may be necessary to increase `SHMALL`, which is the total amount of System V shared memory system-wide. Note that `SHMALL` is measured in pages rather than bytes on many systems.

Less likely to cause problems is the minimum size for shared memory segments (`SHMMIN`), which should be at most approximately 32 bytes for PostgreSQL (it is usually just 1). The maximum number of segments system-wide (`SHMMNI`) or per-process (`SHMSEG`) are unlikely to cause a problem unless your system has them set to zero.

When using System V semaphores, PostgreSQL uses one semaphore per allowed connection ([???](#guc-max-connections)), allowed autovacuum worker process ([???](#guc-autovacuum-max-workers)), allowed WAL sender process ([???](#guc-max-wal-senders)), and allowed background process ([???](#guc-max-worker-processes)), in sets of 19. Each such set will also contain a 20th semaphore which contains a “magic number”, to detect collision with semaphore sets used by other applications. The maximum number of semaphores in the system is set by `SEMMNS`, which consequently must be at least as high as `max_connections` plus `autovacuum_max_workers` plus `max_wal_senders`, plus `max_worker_processes`, plus one extra for each 19 allowed connections plus workers (see the formula in [ Parameters](#sysvipc-parameters)). The parameter `SEMMNI` determines the limit on the number of semaphore sets that can exist on the system at one time. Hence this parameter must be at least `ceil((max_connections + autovacuum_max_workers + max_wal_senders + max_worker_processes + 7) / 19)`. Lowering the number of allowed connections is a temporary workaround for failures, which are usually confusingly worded “No space left on device”, from the function `semget`.

In some cases it might also be necessary to increase `SEMMAP` to be at least on the order of `SEMMNS`. If the system has this parameter (many do not), it defines the size of the semaphore resource map, in which each contiguous block of available semaphores needs an entry. When a semaphore set is freed it is either added to an existing entry that is adjacent to the freed block or it is registered under a new map entry. If the map is full, the freed semaphores get lost (until reboot). Fragmentation of the semaphore space could over time lead to fewer available semaphores than there should be.

Various other settings related to “semaphore undo”, such as `SEMMNU` and `SEMUME`, do not affect PostgreSQL.

When using POSIX semaphores, the number of semaphores needed is the same as for System V, that is one semaphore per allowed connection ([???](#guc-max-connections)), allowed autovacuum worker process ([???](#guc-autovacuum-max-workers)), allowed WAL sender process ([???](#guc-max-wal-senders)), and allowed background process ([???](#guc-max-worker-processes)). On the platforms where this option is preferred, there is no specific kernel limit on the number of POSIX semaphores.

`FreeBSD` <span class="indexterm"></span>  
The default shared memory settings are usually good enough, unless you have set `shared_memory_type` to `sysv`. System V semaphores are not used on this platform.

The default IPC settings can be changed using the `sysctl` or `loader` interfaces. The following parameters can be set using `sysctl`:

    # sysctl kern.ipc.shmall=32768
    # sysctl kern.ipc.shmmax=134217728

To make these settings persist over reboots, modify `/etc/sysctl.conf`.

If you have set `shared_memory_type` to `sysv`, you might also want to configure your kernel to lock System V shared memory into RAM and prevent it from being paged out to swap. This can be accomplished using the `sysctl` setting `kern.ipc.shm_use_phys`.

If running in a FreeBSD jail, you should set its `sysvshm` parameter to `new`, so that it has its own separate System V shared memory namespace. (Before FreeBSD 11.0, it was necessary to enable shared access to the host's IPC namespace from jails, and take measures to avoid collisions.)

`NetBSD` <span class="indexterm"></span>  
The default shared memory settings are usually good enough, unless you have set `shared_memory_type` to `sysv`. You will usually want to increase `kern.ipc.semmni` and `kern.ipc.semmns`, as `NetBSD`'s default settings for these are uncomfortably small.

IPC parameters can be adjusted using `sysctl`, for example:

    # sysctl -w kern.ipc.semmni=100

To make these settings persist over reboots, modify `/etc/sysctl.conf`.

If you have set `shared_memory_type` to `sysv`, you might also want to configure your kernel to lock System V shared memory into RAM and prevent it from being paged out to swap. This can be accomplished using the `sysctl` setting `kern.ipc.shm_use_phys`.

`OpenBSD` <span class="indexterm"></span>  
The default shared memory settings are usually good enough, unless you have set `shared_memory_type` to `sysv`. You will usually want to increase `kern.seminfo.semmni` and `kern.seminfo.semmns`, as `OpenBSD`'s default settings for these are uncomfortably small.

IPC parameters can be adjusted using `sysctl`, for example:

    # sysctl kern.seminfo.semmni=100

To make these settings persist over reboots, modify `/etc/sysctl.conf`.

`Linux` <span class="indexterm"></span>  
The default shared memory settings are usually good enough, unless you have set `shared_memory_type` to `sysv`, and even then only on older kernel versions that shipped with low defaults. System V semaphores are not used on this platform.

The shared memory size settings can be changed via the `sysctl` interface. For example, to allow 16 GB:

    $ sysctl -w kernel.shmmax=17179869184
    $ sysctl -w kernel.shmall=4194304

To make these settings persist over reboots, see `/etc/sysctl.conf`.

`macOS` <span class="indexterm"></span>  
The default shared memory and semaphore settings are usually good enough, unless you have set `shared_memory_type` to `sysv`.

The recommended method for configuring shared memory in macOS is to create a file named `/etc/sysctl.conf`, containing variable assignments such as:

    kern.sysv.shmmax=4194304
    kern.sysv.shmmin=1
    kern.sysv.shmmni=32
    kern.sysv.shmseg=8
    kern.sysv.shmall=1024

Note that in some macOS versions, *all five* shared-memory parameters must be set in `/etc/sysctl.conf`, else the values will be ignored.

`SHMMAX` can only be set to a multiple of 4096.

`SHMALL` is measured in 4 kB pages on this platform.

It is possible to change all but `SHMMNI` on the fly, using sysctl. But it's still best to set up your preferred values via `/etc/sysctl.conf`, so that the values will be kept across reboots.

`Solaris`; `illumos`  
The default shared memory and semaphore settings are usually good enough for most PostgreSQL applications. Solaris defaults to a `SHMMAX` of one-quarter of system RAM. To further adjust this setting, use a project setting associated with the `postgres` user. For example, run the following as `root`:

    projadd -c "PostgreSQL DB User" -K "project.max-shm-memory=(privileged,8GB,deny)" -U postgres -G postgres user.postgres

This command adds the `user.postgres` project and sets the shared memory maximum for the `postgres` user to 8GB, and takes effect the next time that user logs in, or when you restart PostgreSQL (not reload). The above assumes that PostgreSQL is run by the `postgres` user in the `postgres` group. No server reboot is required.

Other recommended kernel setting changes for database servers which will have a large number of connections are:

    project.max-shm-ids=(priv,32768,deny)
    project.max-sem-ids=(priv,4096,deny)
    project.max-msg-ids=(priv,4096,deny)

Additionally, if you are running PostgreSQL inside a zone, you may need to raise the zone resource usage limits as well. See "Chapter2: Projects and Tasks" in the System Administrator's Guide for more information on `projects` and `prctl`.

### systemd RemoveIPC

systemd

RemoveIPC

If systemd is in use, some care must be taken that IPC resources (including shared memory) are not prematurely removed by the operating system. This is especially of concern when installing PostgreSQL from source. Users of distribution packages of PostgreSQL are less likely to be affected, as the `postgres` user is then normally created as a system user.

The setting `RemoveIPC` in `logind.conf` controls whether IPC objects are removed when a user fully logs out. System users are exempt. This setting defaults to on in stock systemd, but some operating system distributions default it to off.

A typical observed effect when this setting is on is that shared memory objects used for parallel query execution are removed at apparently random times, leading to errors and warnings while attempting to open and remove them, like

    WARNING:  could not remove shared memory segment "/PostgreSQL.1450751626": No such file or directory

Different types of IPC objects (shared memory vs. semaphores, System V vs. POSIX) are treated slightly differently by systemd, so one might observe that some IPC resources are not removed in the same way as others. But it is not advisable to rely on these subtle differences.

A “user logging out” might happen as part of a maintenance job or manually when an administrator logs in as the `postgres` user or something similar, so it is hard to prevent in general.

What is a “system user” is determined at systemd compile time from the `SYS_UID_MAX` setting in `/etc/login.defs`.

Packaging and deployment scripts should be careful to create the `postgres` user as a system user by using `useradd -r`, `adduser --system`, or equivalent.

Alternatively, if the user account was created incorrectly or cannot be changed, it is recommended to set

    RemoveIPC=no

in `/etc/systemd/logind.conf` or another appropriate configuration file.

> [!CAUTION]
> At least one of these two things has to be ensured, or the PostgreSQL server will be very unreliable.

### Resource Limits

Unix-like operating systems enforce various kinds of resource limits that might interfere with the operation of your PostgreSQL server. Of particular importance are limits on the number of processes per user, the number of open files per process, and the amount of memory available to each process. Each of these have a “hard” and a “soft” limit. The soft limit is what actually counts but it can be changed by the user up to the hard limit. The hard limit can only be changed by the root user. The system call `setrlimit` is responsible for setting these parameters. The shell's built-in command `ulimit` (Bourne shells) or `limit` (csh) is used to control the resource limits from the command line. On BSD-derived systems the file `/etc/login.conf` controls the various resource limits set during login. See the operating system documentation for details. The relevant parameters are `maxproc`, `openfiles`, and `datasize`. For example:

    default:\
    ...
            :datasize-cur=256M:\
            :maxproc-cur=256:\
            :openfiles-cur=256:\
    ...

(`-cur` is the soft limit. Append `-max` to set the hard limit.)

Kernels can also have system-wide limits on some resources.

- On Linux the kernel parameter `fs.file-max` determines the maximum number of open files that the kernel will support. It can be changed with `sysctl -w fs.file-max=N`. To make the setting persist across reboots, add an assignment in `/etc/sysctl.conf`. The maximum limit of files per process is fixed at the time the kernel is compiled; see `/usr/src/linux/Documentation/proc.txt` for more information.

The PostgreSQL server uses one process per connection so you should provide for at least as many processes as allowed connections, in addition to what you need for the rest of your system. This is usually not a problem but if you run several servers on one machine things might get tight.

The factory default limit on open files is often set to “socially friendly” values that allow many users to coexist on a machine without using an inappropriate fraction of the system resources. If you run many servers on a machine this is perhaps what you want, but on dedicated servers you might want to raise this limit.

On the other side of the coin, some systems allow individual processes to open large numbers of files; if more than a few processes do so then the system-wide limit can easily be exceeded. If you find this happening, and you do not want to alter the system-wide limit, you can set PostgreSQL's [???](#guc-max-files-per-process) configuration parameter to limit the consumption of open files.

Another kernel limit that may be of concern when supporting large numbers of client connections is the maximum socket connection queue length. If more than that many connection requests arrive within a very short period, some may get rejected before the PostgreSQL server can service the requests, with those clients receiving unhelpful connection failure errors such as “Resource temporarily unavailable” or “Connection refused”. The default queue length limit is 128 on many platforms. To raise it, adjust the appropriate kernel parameter via sysctl, then restart the PostgreSQL server. The parameter is variously named `net.core.somaxconn` on Linux, `kern.ipc.soacceptqueue` on newer FreeBSD, and `kern.ipc.somaxconn` on macOS and other BSD variants.

### Linux Memory Overcommit

memory overcommit

OOM

overcommit

The default virtual memory behavior on Linux is not optimal for PostgreSQL. Because of the way that the kernel implements memory overcommit, the kernel might terminate the PostgreSQL postmaster (the supervisor server process) if the memory demands of either PostgreSQL or another process cause the system to run out of virtual memory.

If this happens, you will see a kernel message that looks like this (consult your system documentation and configuration on where to look for such a message):

    Out of Memory: Killed process 12345 (postgres).

This indicates that the `postgres` process has been terminated due to memory pressure. Although existing database connections will continue to function normally, no new connections will be accepted. To recover, PostgreSQL will need to be restarted.

One way to avoid this problem is to run PostgreSQL on a machine where you can be sure that other processes will not run the machine out of memory. If memory is tight, increasing the swap space of the operating system can help avoid the problem, because the out-of-memory (OOM) killer is invoked only when physical memory and swap space are exhausted.

If PostgreSQL itself is the cause of the system running out of memory, you can avoid the problem by changing your configuration. In some cases, it may help to lower memory-related configuration parameters, particularly [`shared_buffers`](#guc-shared-buffers), [`work_mem`](#guc-work-mem), and [`hash_mem_multiplier`](#guc-hash-mem-multiplier). In other cases, the problem may be caused by allowing too many connections to the database server itself. In many cases, it may be better to reduce [`max_connections`](#guc-max-connections) and instead make use of external connection-pooling software.

It is possible to modify the kernel's behavior so that it will not “overcommit” memory. Although this setting will not prevent the [OOM killer](https://lwn.net/Articles/104179/) from being invoked altogether, it will lower the chances significantly and will therefore lead to more robust system behavior. This is done by selecting strict overcommit mode via `sysctl`:

    sysctl -w vm.overcommit_memory=2

or placing an equivalent entry in `/etc/sysctl.conf`. You might also wish to modify the related setting `vm.overcommit_ratio`. For details see the kernel documentation file [](https://www.kernel.org/doc/Documentation/vm/overcommit-accounting).

Another approach, which can be used with or without altering `vm.overcommit_memory`, is to set the process-specific OOM score adjustment value for the postmaster process to `-1000`, thereby guaranteeing it will not be targeted by the OOM killer. The simplest way to do this is to execute

    echo -1000 > /proc/self/oom_score_adj

in the PostgreSQL startup script just before invoking `postgres`. Note that this action must be done as root, or it will have no effect; so a root-owned startup script is the easiest place to do it. If you do this, you should also set these environment variables in the startup script before invoking `postgres`:

    export PG_OOM_ADJUST_FILE=/proc/self/oom_score_adj
    export PG_OOM_ADJUST_VALUE=0

These settings will cause postmaster child processes to run with the normal OOM score adjustment of zero, so that the OOM killer can still target them at need. You could use some other value for `PG_OOM_ADJUST_VALUE` if you want the child processes to run with some other OOM score adjustment. (`PG_OOM_ADJUST_VALUE` can also be omitted, in which case it defaults to zero.) If you do not set `PG_OOM_ADJUST_FILE`, the child processes will run with the same OOM score adjustment as the postmaster, which is unwise since the whole point is to ensure that the postmaster has a preferential setting.

### Linux Huge Pages

Using huge pages reduces overhead when using large contiguous chunks of memory, as PostgreSQL does, particularly when using large values of [???](#guc-shared-buffers). To use this feature in PostgreSQL you need a kernel with `CONFIG_HUGETLBFS=y` and `CONFIG_HUGETLB_PAGE=y`. You will also have to configure the operating system to provide enough huge pages of the desired size. The runtime-computed parameter [???](#guc-shared-memory-size-in-huge-pages) reports the number of huge pages required. This parameter can be viewed before starting the server with a `postgres` command like:

    $ postgres -D $PGDATA -C shared_memory_size_in_huge_pages
    3170
    $ grep ^Hugepagesize /proc/meminfo
    Hugepagesize:       2048 kB
    $ ls /sys/kernel/mm/hugepages
    hugepages-1048576kB  hugepages-2048kB

In this example the default is 2MB, but you can also explicitly request either 2MB or 1GB with [???](#guc-huge-page-size) to adapt the number of pages calculated by `shared_memory_size_in_huge_pages`. While we need at least `3170` huge pages in this example, a larger setting would be appropriate if other programs on the machine also need huge pages. We can set this with:

    # sysctl -w vm.nr_hugepages=3170

Don't forget to add this setting to `/etc/sysctl.conf` so that it is reapplied after reboots. For non-default huge page sizes, we can instead use:

    # echo 3170 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

It is also possible to provide these settings at boot time using kernel parameters such as `hugepagesz=2M hugepages=3170`.

Sometimes the kernel is not able to allocate the desired number of huge pages immediately due to fragmentation, so it might be necessary to repeat the command or to reboot. (Immediately after a reboot, most of the machine's memory should be available to convert into huge pages.) To verify the huge page allocation situation for a given size, use:

    $ cat /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

It may also be necessary to give the database server's operating system user permission to use huge pages by setting `vm.hugetlb_shm_group` via sysctl, and/or give permission to lock memory with `ulimit -l`.

The default behavior for huge pages in PostgreSQL is to use them when possible, with the system's default huge page size, and to fall back to normal pages on failure. To enforce the use of huge pages, you can set [???](#guc-huge-pages) to `on` in `postgresql.conf`. Note that with this setting PostgreSQL will fail to start if not enough huge pages are available.

For a detailed description of the Linux huge pages feature have a look at [](https://www.kernel.org/doc/Documentation/vm/hugetlbpage.txt).

## Shutting Down the Server

shutdown

There are several ways to shut down the database server. Under the hood, they all reduce to sending a signal to the supervisor `postgres` process.

If you are using a pre-packaged version of PostgreSQL, and you used its provisions for starting the server, then you should also use its provisions for stopping the server. Consult the package-level documentation for details.

When managing the server directly, you can control the type of shutdown by sending different signals to the `postgres` process:

`SIGTERM`<span class="indexterm"></span>  
This is the Smart Shutdown mode. After receiving `SIGTERM`, the server disallows new connections, but lets existing sessions end their work normally. It shuts down only after all of the sessions terminate. If the server is in recovery when a smart shutdown is requested, recovery and streaming replication will be stopped only after all regular sessions have terminated.

`SIGINT`<span class="indexterm"></span>  
This is the Fast Shutdown mode. The server disallows new connections and sends all existing server processes `SIGTERM`, which will cause them to abort their current transactions and exit promptly. It then waits for all server processes to exit and finally shuts down.

`SIGQUIT`<span class="indexterm"></span>  
This is the Immediate Shutdown mode. The server will send `SIGQUIT` to all child processes and wait for them to terminate. If any do not terminate within 5 seconds, they will be sent `SIGKILL`. The supervisor server process exits as soon as all child processes have exited, without doing normal database shutdown processing. This will lead to recovery (by replaying the WAL log) upon next start-up. This is recommended only in emergencies.

The [???](#app-pg-ctl) program provides a convenient interface for sending these signals to shut down the server. Alternatively, you can send the signal directly using `kill` on non-Windows systems. The PID of the `postgres` process can be found using the `ps` program, or from the file `postmaster.pid` in the data directory. For example, to do a fast shutdown:

    $ kill -INT `head -1 /usr/local/pgsql/data/postmaster.pid`

> [!IMPORTANT]
> It is best not to use `SIGKILL` to shut down the server. Doing so will prevent the server from releasing shared memory and semaphores. Furthermore, `SIGKILL` kills the `postgres` process without letting it relay the signal to its subprocesses, so it might be necessary to kill the individual subprocesses by hand as well.

To terminate an individual session while allowing other sessions to continue, use `pg_terminate_backend()` (see [???](#functions-admin-signal-table)) or send a `SIGTERM` signal to the child process associated with the session.

## Upgrading a PostgreSQL Cluster

upgrading

version

compatibility

This section discusses how to upgrade your database data from one PostgreSQL release to a newer one.

Current PostgreSQL version numbers consist of a major and a minor version number. For example, in the version number 10.1, the 10 is the major version number and the 1 is the minor version number, meaning this would be the first minor release of the major release 10. For releases before PostgreSQL version 10.0, version numbers consist of three numbers, for example, 9.5.3. In those cases, the major version consists of the first two digit groups of the version number, e.g., 9.5, and the minor version is the third number, e.g., 3, meaning this would be the third minor release of the major release 9.5.

Minor releases never change the internal storage format and are always compatible with earlier and later minor releases of the same major version number. For example, version 10.1 is compatible with version 10.0 and version 10.6. Similarly, for example, 9.5.3 is compatible with 9.5.0, 9.5.1, and 9.5.6. To update between compatible versions, you simply replace the executables while the server is down and restart the server. The data directory remains unchanged minor upgrades are that simple.

For *major* releases of PostgreSQL, the internal data storage format is subject to change, thus complicating upgrades. The traditional method for moving data to a new major version is to dump and restore the database, though this can be slow. A faster method is [???](#pgupgrade). Replication methods are also available, as discussed below. (If you are using a pre-packaged version of PostgreSQL, it may provide scripts to assist with major version upgrades. Consult the package-level documentation for details.)

New major versions also typically introduce some user-visible incompatibilities, so application programming changes might be required. All user-visible changes are listed in the release notes ([???](#release)); pay particular attention to the section labeled "Migration". Though you can upgrade from one major version to another without upgrading to intervening versions, you should read the major release notes of all intervening versions.

Cautious users will want to test their client applications on the new version before switching over fully; therefore, it's often a good idea to set up concurrent installations of old and new versions. When testing a PostgreSQL major upgrade, consider the following categories of possible changes:

Administration  
The capabilities available for administrators to monitor and control the server often change and improve in each major release.

SQL  
Typically this includes new SQL command capabilities and not changes in behavior, unless specifically mentioned in the release notes.

Library API  
Typically libraries like libpq only add new functionality, again unless mentioned in the release notes.

System Catalogs  
System catalog changes usually only affect database management tools.

Server C-language API  
This involves changes in the backend function API, which is written in the C programming language. Such changes affect code that references backend functions deep inside the server.

### Upgrading Data via pg_dumpall

One upgrade method is to dump data from one major version of PostgreSQL and restore it in another to do this, you must use a *logical* backup tool like pg_dumpall; file system level backup methods will not work. (There are checks in place that prevent you from using a data directory with an incompatible version of PostgreSQL, so no great harm can be done by trying to start the wrong server version on a data directory.)

It is recommended that you use the pg_dump and pg_dumpall programs from the *newer* version of PostgreSQL, to take advantage of enhancements that might have been made in these programs. Current releases of the dump programs can read data from any server version back to 9.2.

These instructions assume that your existing installation is under the `/usr/local/pgsql` directory, and that the data area is in `/usr/local/pgsql/data`. Substitute your paths appropriately.

1.  If making a backup, make sure that your database is not being updated. This does not affect the integrity of the backup, but the changed data would of course not be included. If necessary, edit the permissions in the file `/usr/local/pgsql/data/pg_hba.conf` (or equivalent) to disallow access from everyone except you. See [???](#client-authentication) for additional information on access control.

    <span class="indexterm"></span> To back up your database installation, type:

        pg_dumpall > outputfile

    To make the backup, you can use the pg_dumpall command from the version you are currently running; see [???](#backup-dump-all) for more details. For best results, however, try to use the pg_dumpall command from PostgreSQL , since this version contains bug fixes and improvements over older versions. While this advice might seem idiosyncratic since you haven't installed the new version yet, it is advisable to follow it if you plan to install the new version in parallel with the old version. In that case you can complete the installation normally and transfer the data later. This will also decrease the downtime.

2.  Shut down the old server:

        pg_ctl stop

    On systems that have PostgreSQL started at boot time, there is probably a start-up file that will accomplish the same thing. For example, on a `Red Hat Linux` system one might find that this works:

        /etc/rc.d/init.d/postgresql stop

    See [Server Setup and Operation](#runtime) for details about starting and stopping the server.

3.  If restoring from backup, rename or delete the old installation directory if it is not version-specific. It is a good idea to rename the directory, rather than delete it, in case you have trouble and need to revert to it. Keep in mind the directory might consume significant disk space. To rename the directory, use a command like this:

        mv /usr/local/pgsql /usr/local/pgsql.old

    (Be sure to move the directory as a single unit so relative paths remain unchanged.)

4.  Install the new version of PostgreSQL as outlined in [???](#installation).

5.  Create a new database cluster if needed. Remember that you must execute these commands while logged in to the special database user account (which you already have if you are upgrading).

        /usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data

6.  Restore your previous `pg_hba.conf` and any `postgresql.conf` modifications.

7.  Start the database server, again using the special database user account:

        /usr/local/pgsql/bin/postgres -D /usr/local/pgsql/data

8.  Finally, restore your data from backup with:

        /usr/local/pgsql/bin/psql -d postgres -f outputfile

    using the *new* psql.

The least downtime can be achieved by installing the new server in a different directory and running both the old and the new servers in parallel, on different ports. Then you can use something like:

    pg_dumpall -p 5432 | psql -d postgres -p 5433

to transfer your data.

### Upgrading Data via pg_upgrade

The [???](#pgupgrade) module allows an installation to be migrated in-place from one major PostgreSQL version to another. Upgrades can be performed in minutes, particularly with `--link` mode. It requires steps similar to pg_dumpall above, e.g., starting/stopping the server, running initdb. The pg_upgrade [documentation](#pgupgrade) outlines the necessary steps.

### Upgrading Data via Replication

It is also possible to use logical replication methods to create a standby server with the updated version of PostgreSQL. This is possible because logical replication supports replication between different major versions of PostgreSQL. The standby can be on the same computer or a different computer. Once it has synced up with the primary server (running the older version of PostgreSQL), you can switch primaries and make the standby the primary and shut down the older database instance. Such a switch-over results in only several seconds of downtime for an upgrade.

This method of upgrading can be performed using the built-in logical replication facilities as well as using external logical replication systems such as pglogical, Slony, Londiste, and Bucardo.

## Preventing Server Spoofing

server spoofing

While the server is running, it is not possible for a malicious user to take the place of the normal database server. However, when the server is down, it is possible for a local user to spoof the normal server by starting their own server. The spoof server could read passwords and queries sent by clients, but could not return any data because the `PGDATA` directory would still be secure because of directory permissions. Spoofing is possible because any user can start a database server; a client cannot identify an invalid server unless it is specially configured.

One way to prevent spoofing of `local` connections is to use a Unix domain socket directory ([???](#guc-unix-socket-directories)) that has write permission only for a trusted local user. This prevents a malicious user from creating their own socket file in that directory. If you are concerned that some applications might still reference `/tmp` for the socket file and hence be vulnerable to spoofing, during operating system startup create a symbolic link `/tmp/.s.PGSQL.5432` that points to the relocated socket file. You also might need to modify your `/tmp` cleanup script to prevent removal of the symbolic link.

Another option for `local` connections is for clients to use [`requirepeer`](#libpq-connect-requirepeer) to specify the required owner of the server process connected to the socket.

To prevent spoofing on TCP connections, either use SSL certificates and make sure that clients check the server's certificate, or use GSSAPI encryption (or both, if they're on separate connections).

To prevent spoofing with SSL, the server must be configured to accept only `hostssl` connections ([???](#auth-pg-hba-conf)) and have SSL key and certificate files ([Secure TCP/IP Connections with SSL](#ssl-tcp)). The TCP client must connect using `sslmode=verify-ca` or `verify-full` and have the appropriate root certificate file installed ([???](#libq-ssl-certificates)). Alternatively the [system CA pool](#libpq-connect-sslrootcert), as defined by the SSL implementation, can be used using `sslrootcert=system`; in this case, `sslmode=verify-full` is forced for safety, since it is generally trivial to obtain certificates which are signed by a public CA.

To prevent server spoofing from occurring when using [scram-sha-256](#auth-password) password authentication over a network, you should ensure that you connect to the server using SSL and with one of the anti-spoofing methods described in the previous paragraph. Additionally, the SCRAM implementation in libpq cannot protect the entire authentication exchange, but using the `channel_binding=require` connection parameter provides a mitigation against server spoofing. An attacker that uses a rogue server to intercept a SCRAM exchange can use offline analysis to potentially determine the hashed password from the client.

To prevent spoofing with GSSAPI, the server must be configured to accept only `hostgssenc` connections ([???](#auth-pg-hba-conf)) and use `gss` authentication with them. The TCP client must connect using `gssencmode=require`.

## Encryption Options

encryption

PostgreSQL offers encryption at several levels, and provides flexibility in protecting data from disclosure due to database server theft, unscrupulous administrators, and insecure networks. Encryption might also be required to secure sensitive data such as medical records or financial transactions.

Password Encryption  
Database user passwords are stored as hashes (determined by the setting [???](#guc-password-encryption)), so the administrator cannot determine the actual password assigned to the user. If SCRAM or MD5 encryption is used for client authentication, the unencrypted password is never even temporarily present on the server because the client encrypts it before being sent across the network. SCRAM is preferred, because it is an Internet standard and is more secure than the PostgreSQL-specific MD5 authentication protocol.

Encryption For Specific Columns  
The [???](#pgcrypto) module allows certain fields to be stored encrypted. This is useful if only some of the data is sensitive. The client supplies the decryption key and the data is decrypted on the server and then sent to the client.

The decrypted data and the decryption key are present on the server for a brief time while it is being decrypted and communicated between the client and server. This presents a brief moment where the data and keys can be intercepted by someone with complete access to the database server, such as the system administrator.

Data Partition Encryption  
Storage encryption can be performed at the file system level or the block level. Linux file system encryption options include eCryptfs and EncFS, while FreeBSD uses PEFS. Block level or full disk encryption options include dm-crypt + LUKS on Linux and GEOM modules geli and gbde on FreeBSD. Many other operating systems support this functionality, including Windows.

This mechanism prevents unencrypted data from being read from the drives if the drives or the entire computer is stolen. This does not protect against attacks while the file system is mounted, because when mounted, the operating system provides an unencrypted view of the data. However, to mount the file system, you need some way for the encryption key to be passed to the operating system, and sometimes the key is stored somewhere on the host that mounts the disk.

Encrypting Data Across A Network  
SSL connections encrypt all data sent across the network: the password, the queries, and the data returned. The `pg_hba.conf` file allows administrators to specify which hosts can use non-encrypted connections (`host`) and which require SSL-encrypted connections (`hostssl`). Also, clients can specify that they connect to servers only via SSL.

GSSAPI-encrypted connections encrypt all data sent across the network, including queries and data returned. (No password is sent across the network.) The `pg_hba.conf` file allows administrators to specify which hosts can use non-encrypted connections (`host`) and which require GSSAPI-encrypted connections (`hostgssenc`). Also, clients can specify that they connect to servers only on GSSAPI-encrypted connections (`gssencmode=require`).

Stunnel or SSH can also be used to encrypt transmissions.

SSL Host Authentication  
It is possible for both the client and server to provide SSL certificates to each other. It takes some extra configuration on each side, but this provides stronger verification of identity than the mere use of passwords. It prevents a computer from pretending to be the server just long enough to read the password sent by the client. It also helps prevent “man in the middle” attacks where a computer between the client and server pretends to be the server and reads and passes all data between the client and server.

Client-Side Encryption  
If the system administrator for the server's machine cannot be trusted, it is necessary for the client to encrypt the data; this way, unencrypted data never appears on the database server. Data is encrypted on the client before being sent to the server, and database results have to be decrypted on the client before being used.

## Secure TCP/IP Connections with SSL

SSL

TLS

PostgreSQL has native support for using SSL connections to encrypt client/server communications for increased security. This requires that OpenSSL is installed on both client and server systems and that support in PostgreSQL is enabled at build time (see [???](#installation)).

The terms SSL and TLS are often used interchangeably to mean a secure encrypted connection using a TLS protocol. SSL protocols are the precursors to TLS protocols, and the term SSL is still used for encrypted connections even though SSL protocols are no longer supported. SSL is used interchangeably with TLS in PostgreSQL.

### Basic Setup

With SSL support compiled in, the PostgreSQL server can be started with support for encrypted connections using TLS protocols enabled by setting the parameter [???](#guc-ssl) to `on` in `postgresql.conf`. The server will listen for both normal and SSL connections on the same TCP port, and will negotiate with any connecting client on whether to use SSL. By default, this is at the client's option; see [???](#auth-pg-hba-conf) about how to set up the server to require use of SSL for some or all connections.

To start in SSL mode, files containing the server certificate and private key must exist. By default, these files are expected to be named `server.crt` and `server.key`, respectively, in the server's data directory, but other names and locations can be specified using the configuration parameters [???](#guc-ssl-cert-file) and [???](#guc-ssl-key-file).

On Unix systems, the permissions on `server.key` must disallow any access to world or group; achieve this by the command `chmod 0600 server.key`. Alternatively, the file can be owned by root and have group read access (that is, `0640` permissions). That setup is intended for installations where certificate and key files are managed by the operating system. The user under which the PostgreSQL server runs should then be made a member of the group that has access to those certificate and key files.

If the data directory allows group read access then certificate files may need to be located outside of the data directory in order to conform to the security requirements outlined above. Generally, group access is enabled to allow an unprivileged user to backup the database, and in that case the backup software will not be able to read the certificate files and will likely error.

If the private key is protected with a passphrase, the server will prompt for the passphrase and will not start until it has been entered. Using a passphrase by default disables the ability to change the server's SSL configuration without a server restart, but see [???](#guc-ssl-passphrase-command-supports-reload). Furthermore, passphrase-protected private keys cannot be used at all on Windows.

The first certificate in `server.crt` must be the server's certificate because it must match the server's private key. The certificates of “intermediate” certificate authorities can also be appended to the file. Doing this avoids the necessity of storing intermediate certificates on clients, assuming the root and intermediate certificates were created with `v3_ca` extensions. (This sets the certificate's basic constraint of `CA` to `true`.) This allows easier expiration of intermediate certificates.

It is not necessary to add the root certificate to `server.crt`. Instead, clients must have the root certificate of the server's certificate chain.

### OpenSSL Configuration

PostgreSQL reads the system-wide OpenSSL configuration file. By default, this file is named `openssl.cnf` and is located in the directory reported by `openssl version -d`. This default can be overridden by setting environment variable `OPENSSL_CONF` to the name of the desired configuration file.

OpenSSL supports a wide range of ciphers and authentication algorithms, of varying strength. While a list of ciphers can be specified in the OpenSSL configuration file, you can specify ciphers specifically for use by the database server by modifying [???](#guc-ssl-ciphers) in `postgresql.conf`.

> [!NOTE]
> It is possible to have authentication without encryption overhead by using `NULL-SHA` or `NULL-MD5` ciphers. However, a man-in-the-middle could read and pass communications between client and server. Also, encryption overhead is minimal compared to the overhead of authentication. For these reasons NULL ciphers are not recommended.

### Using Client Certificates

To require the client to supply a trusted certificate, place certificates of the root certificate authorities (CAs) you trust in a file in the data directory, set the parameter [???](#guc-ssl-ca-file) in `postgresql.conf` to the new file name, and add the authentication option `clientcert=verify-ca` or `clientcert=verify-full` to the appropriate `hostssl` line(s) in `pg_hba.conf`. A certificate will then be requested from the client during SSL connection startup. (See [???](#libpq-ssl) for a description of how to set up certificates on the client.)

For a `hostssl` entry with `clientcert=verify-ca`, the server will verify that the client's certificate is signed by one of the trusted certificate authorities. If `clientcert=verify-full` is specified, the server will not only verify the certificate chain, but it will also check whether the username or its mapping matches the `cn` (Common Name) of the provided certificate. Note that certificate chain validation is always ensured when the `cert` authentication method is used (see [???](#auth-cert)).

Intermediate certificates that chain up to existing root certificates can also appear in the [???](#guc-ssl-ca-file) file if you wish to avoid storing them on clients (assuming the root and intermediate certificates were created with `v3_ca` extensions). Certificate Revocation List (CRL) entries are also checked if the parameter [???](#guc-ssl-crl-file) or [???](#guc-ssl-crl-dir) is set.

The `clientcert` authentication option is available for all authentication methods, but only in `pg_hba.conf` lines specified as `hostssl`. When `clientcert` is not specified, the server verifies the client certificate against its CA file only if a client certificate is presented and the CA is configured.

There are two approaches to enforce that users provide a certificate during login.

The first approach makes use of the `cert` authentication method for `hostssl` entries in `pg_hba.conf`, such that the certificate itself is used for authentication while also providing ssl connection security. See [???](#auth-cert) for details. (It is not necessary to specify any `clientcert` options explicitly when using the `cert` authentication method.) In this case, the `cn` (Common Name) provided in the certificate is checked against the user name or an applicable mapping.

The second approach combines any authentication method for `hostssl` entries with the verification of client certificates by setting the `clientcert` authentication option to `verify-ca` or `verify-full`. The former option only enforces that the certificate is valid, while the latter also ensures that the `cn` (Common Name) in the certificate matches the user name or an applicable mapping.

### SSL Server File Usage

[SSL Server File Usage](#ssl-file-usage) summarizes the files that are relevant to the SSL setup on the server. (The shown file names are default names. The locally configured names could be different.)

| File | Contents | Effect |
|----|----|----|
| [???](#guc-ssl-cert-file) (`$PGDATA/server.crt`) | server certificate | sent to client to indicate server's identity |
| [???](#guc-ssl-key-file) (`$PGDATA/server.key`) | server private key | proves server certificate was sent by the owner; does not indicate certificate owner is trustworthy |
| [???](#guc-ssl-ca-file) | trusted certificate authorities | checks that client certificate is signed by a trusted certificate authority |
| [???](#guc-ssl-crl-file) | certificates revoked by certificate authorities | client certificate must not be on this list |

SSL Server File Usage {#ssl-file-usage}

The server reads these files at server start and whenever the server configuration is reloaded. On `Windows` systems, they are also re-read whenever a new backend process is spawned for a new client connection.

If an error in these files is detected at server start, the server will refuse to start. But if an error is detected during a configuration reload, the files are ignored and the old SSL configuration continues to be used. On `Windows` systems, if an error in these files is detected at backend start, that backend will be unable to establish an SSL connection. In all these cases, the error condition is reported in the server log.

### Creating Certificates

To create a simple self-signed certificate for the server, valid for 365 days, use the following OpenSSL command, replacing \<dbhost.yourdomain.com\> with the server's host name:

    openssl req -new -x509 -days 365 -nodes -text -out server.crt \
      -keyout server.key -subj "/CN=dbhost.yourdomain.com"

Then do:

    chmod og-rwx server.key

because the server will reject the file if its permissions are more liberal than this. For more details on how to create your server private key and certificate, refer to the OpenSSL documentation.

While a self-signed certificate can be used for testing, a certificate signed by a certificate authority (CA) (usually an enterprise-wide root CA) should be used in production.

To create a server certificate whose identity can be validated by clients, first create a certificate signing request (CSR) and a public/private key file:

    openssl req -new -nodes -text -out root.csr \
      -keyout root.key -subj "/CN=root.yourdomain.com"
    chmod og-rwx root.key

Then, sign the request with the key to create a root certificate authority (using the default OpenSSL configuration file location on Linux):

    openssl x509 -req -in root.csr -text -days 3650 \
      -extfile /etc/ssl/openssl.cnf -extensions v3_ca \
      -signkey root.key -out root.crt

Finally, create a server certificate signed by the new root certificate authority:

    openssl req -new -nodes -text -out server.csr \
      -keyout server.key -subj "/CN=dbhost.yourdomain.com"
    chmod og-rwx server.key

    openssl x509 -req -in server.csr -text -days 365 \
      -CA root.crt -CAkey root.key -CAcreateserial \
      -out server.crt

`server.crt` and `server.key` should be stored on the server, and `root.crt` should be stored on the client so the client can verify that the server's leaf certificate was signed by its trusted root certificate. `root.key` should be stored offline for use in creating future certificates.

It is also possible to create a chain of trust that includes intermediate certificates:

    # root
    openssl req -new -nodes -text -out root.csr \
      -keyout root.key -subj "/CN=root.yourdomain.com"
    chmod og-rwx root.key
    openssl x509 -req -in root.csr -text -days 3650 \
      -extfile /etc/ssl/openssl.cnf -extensions v3_ca \
      -signkey root.key -out root.crt

    # intermediate
    openssl req -new -nodes -text -out intermediate.csr \
      -keyout intermediate.key -subj "/CN=intermediate.yourdomain.com"
    chmod og-rwx intermediate.key
    openssl x509 -req -in intermediate.csr -text -days 1825 \
      -extfile /etc/ssl/openssl.cnf -extensions v3_ca \
      -CA root.crt -CAkey root.key -CAcreateserial \
      -out intermediate.crt

    # leaf
    openssl req -new -nodes -text -out server.csr \
      -keyout server.key -subj "/CN=dbhost.yourdomain.com"
    chmod og-rwx server.key
    openssl x509 -req -in server.csr -text -days 365 \
      -CA intermediate.crt -CAkey intermediate.key -CAcreateserial \
      -out server.crt

`server.crt` and `intermediate.crt` should be concatenated into a certificate file bundle and stored on the server. `server.key` should also be stored on the server. `root.crt` should be stored on the client so the client can verify that the server's leaf certificate was signed by a chain of certificates linked to its trusted root certificate. `root.key` and `intermediate.key` should be stored offline for use in creating future certificates.

## Secure TCP/IP Connections with GSSAPI Encryption

gssapi

PostgreSQL also has native support for using GSSAPI to encrypt client/server communications for increased security. Support requires that a GSSAPI implementation (such as MIT Kerberos) is installed on both client and server systems, and that support in PostgreSQL is enabled at build time (see [???](#installation)).

### Basic Setup

The PostgreSQL server will listen for both normal and GSSAPI-encrypted connections on the same TCP port, and will negotiate with any connecting client whether to use GSSAPI for encryption (and for authentication). By default, this decision is up to the client (which means it can be downgraded by an attacker); see [???](#auth-pg-hba-conf) about setting up the server to require the use of GSSAPI for some or all connections.

When using GSSAPI for encryption, it is common to use GSSAPI for authentication as well, since the underlying mechanism will determine both client and server identities (according to the GSSAPI implementation) in any case. But this is not required; another PostgreSQL authentication method can be chosen to perform additional verification.

Other than configuration of the negotiation behavior, GSSAPI encryption requires no setup beyond that which is necessary for GSSAPI authentication. (For more information on configuring that, see [???](#gssapi-auth).)

## Secure TCP/IP Connections with SSH Tunnels

ssh

It is possible to use SSH to encrypt the network connection between clients and a PostgreSQL server. Done properly, this provides an adequately secure network connection, even for non-SSL-capable clients.

First make sure that an SSH server is running properly on the same machine as the PostgreSQL server and that you can log in using `ssh` as some user; you then can establish a secure tunnel to the remote server. A secure tunnel listens on a local port and forwards all traffic to a port on the remote machine. Traffic sent to the remote port can arrive on its `localhost` address, or different bind address if desired; it does not appear as coming from your local machine. This command creates a secure tunnel from the client machine to the remote machine `foo.com`:

    ssh -L 63333:localhost:5432 joe@foo.com

The first number in the `-L` argument, 63333, is the local port number of the tunnel; it can be any unused port. (IANA reserves ports 49152 through 65535 for private use.) The name or IP address after this is the remote bind address you are connecting to, i.e., `localhost`, which is the default. The second number, 5432, is the remote end of the tunnel, e.g., the port number your database server is using. In order to connect to the database server using this tunnel, you connect to port 63333 on the local machine:

    psql -h localhost -p 63333 postgres

To the database server it will then look as though you are user `joe` on host `foo.com` connecting to the `localhost` bind address, and it will use whatever authentication procedure was configured for connections by that user to that bind address. Note that the server will not think the connection is SSL-encrypted, since in fact it is not encrypted between the SSH server and the PostgreSQL server. This should not pose any extra security risk because they are on the same machine.

In order for the tunnel setup to succeed you must be allowed to connect via `ssh` as `joe@foo.com`, just as if you had attempted to use `ssh` to create a terminal session.

You could also have set up port forwarding as

    ssh -L 63333:foo.com:5432 joe@foo.com

but then the database server will see the connection as coming in on its `foo.com` bind address, which is not opened by the default setting `listen_addresses = 'localhost'`. This is usually not what you want.

If you have to “hop” to the database server via some login host, one possible setup could look like this:

    ssh -L 63333:db.foo.com:5432 joe@shell.foo.com

Note that this way the connection from `shell.foo.com` to `db.foo.com` will not be encrypted by the SSH tunnel. SSH offers quite a few configuration possibilities when the network is restricted in various ways. Please refer to the SSH documentation for details.

> [!TIP]
> Several other applications exist that can provide secure tunnels using a procedure similar in concept to the one just described.

## Registering Event Log on `Windows`

event log

event log

To register a `Windows` event log library with the operating system, issue this command:

    regsvr32 pgsql_library_directory/pgevent.dll

This creates registry entries used by the event viewer, under the default event source named `PostgreSQL`.

To specify a different event source name (see [???](#guc-event-source)), use the `/n` and `/i` options:

    regsvr32 /n /i:event_source_name pgsql_library_directory/pgevent.dll

To unregister the event log library from the operating system, issue this command:

    regsvr32 /u [/i:event_source_name] pgsql_library_directory/pgevent.dll

> [!NOTE]
> To enable event logging in the database server, modify [???](#guc-log-destination) to include `eventlog` in `postgresql.conf`.
