---
title: Bash Startup Files
source_url: https://www.gnu.org/software/bash/manual
source_path: 024-bash-startup-files.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 240
---

## Bash Startup Files

startup files

This section describes how Bash executes its startup files. If any of the files exist but cannot be read, Bash reports an error. Tildes are expanded in filenames as described above under Tilde Expansion (see [Tilde Expansion](#Tilde-Expansion)).

Interactive shells are described in [Interactive Shells](#Interactive-Shells).

**Invoked as an interactive login shell, or with `--login`**

When Bash is invoked as an interactive login shell, or as a non-interactive shell with the `--login` option, it first reads and executes commands from the file `/etc/profile`, if that file exists. After reading that file, it looks for `~/.bash_profile`, `~/.bash_login`, and `~/.profile`, in that order, and reads and executes commands from the first one that exists and is readable. The `--noprofile` option inhibits this behavior.

When an interactive login shell exits, or a non-interactive login shell executes the `exit` builtin command, Bash reads and executes commands from the file `~/.bash_logout`, if it exists.

**Invoked as an interactive non-login shell**

When Bash runs as an interactive shell that is not a login shell, it reads and executes commands from `~/.bashrc`, if that file exists. The `--norc` option inhibits this behavior. The `--rcfile file` option causes Bash to use \<file\> instead of `~/.bashrc`.

So, typically, your `~/.bash_profile` contains the line

    if [ -f ~/.bashrc ]; then . ~/.bashrc; fi

after (or before) any login-specific initializations.

**Invoked non-interactively**

When Bash is started non-interactively, to run a shell script, for example, it looks for the variable `BASH_ENV` in the environment, expands its value if it appears there, and uses the expanded value as the name of a file to read and execute. Bash behaves as if the following command were executed:

    if [ -n "$BASH_ENV" ]; then . "$BASH_ENV"; fi

but does not the value of the `PATH` variable to search for the filename.

As noted above, if a non-interactive shell is invoked with the `--login` option, Bash attempts to read and execute commands from the login shell startup files.

**Invoked with name `sh`**

If Bash is invoked with the name `sh`, it tries to mimic the startup behavior of historical versions of `sh` as closely as possible, while conforming to the POSIX standard as well.

When invoked as an interactive login shell, or as a non-interactive shell with the `--login` option, it first attempts to read and execute commands from `/etc/profile` and `~/.profile`, in that order. The `--noprofile` option inhibits this behavior.

When invoked as an interactive shell with the name `sh`, Bash looks for the variable `ENV`, expands its value if it is defined, and uses the expanded value as the name of a file to read and execute. Since a shell invoked as `sh` does not attempt to read and execute commands from any other startup files, the `--rcfile` option has no effect.

A non-interactive shell invoked with the name `sh` does not attempt to read any other startup files.

When invoked as `sh`, Bash enters POSIX mode after reading the startup files.

**Invoked in POSIX mode**

When Bash is started in POSIX mode, as with the `--posix` command line option, it follows the POSIX standard for startup files. In this mode, interactive shells expand the `ENV` variable and read and execute commands from the file whose name is the expanded value. No other startup files are read.

**Invoked by remote shell daemon**

Bash attempts to determine when it is being run with its standard input connected to a network connection, as when executed by the historical and rarely-seen remote shell daemon, usually `rshd`, or the secure shell daemon `sshd`. If Bash determines it is being run non-interactively in this fashion, it reads and executes commands from `~/.bashrc`, if that file exists and is readable. Bash does not read this file if invoked as `sh`. The `--norc` option inhibits this behavior, and the `--rcfile` option makes Bash use a different file instead of `~/.bashrc`, but neither `rshd` nor `sshd` generally invoke the shell with those options or allow them to be specified.

**Invoked with unequal effective and real UID/GIDs**

If Bash is started with the effective user (group) id not equal to the real user (group) id, and the `-p` option is not supplied, no startup files are read, shell functions are not inherited from the environment, the `SHELLOPTS`, `BASHOPTS`, `CDPATH`, and `GLOBIGNORE` variables, if they appear in the environment, are ignored, and the effective user id is set to the real user id. If the `-p` option is supplied at invocation, the startup behavior is the same, but the effective user id is not reset.
