---
title: git-credential-cache—​daemon
description: Temporarily store user credentials in memory
source_url: https://git-scm.com/doc/git-credential-cache--daemon
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-credential-cache--daemon.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 320
---

git-credential-cache{litdd}daemon(1) ====================================

NAME ---- git-credential-cache—​daemon - Temporarily store user credentials in memory

SYNOPSIS --------

> ’git credential-cache{litdd}daemon’ \[--debug\] \<socket-path\>

DESCRIPTION -----------

> [!NOTE]
> You probably don’t want to invoke this command yourself; it is started automatically when you use [git-credential-cache](git-credential-cache.md).

This command listens on the Unix domain socket specified by `<socket-path>` for `git-credential-cache` clients. Clients may store and retrieve credentials. Each credential is held for a timeout specified by the client; once no credentials are held, the daemon exits.

If the `--debug` option is specified, the daemon does not close its stderr stream, and may output extra diagnostics to it even after it has begun listening for clients.

GIT --- Part of the [git](git.md) suite
