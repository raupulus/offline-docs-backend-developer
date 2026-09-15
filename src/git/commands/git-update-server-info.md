---
title: git-update-server-info
description: Update auxiliary info file to help dumb servers
source_url: https://git-scm.com/doc/git-update-server-info
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-update-server-info.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1570
---

git-update-server-info(1) =========================

NAME ---- git-update-server-info - Update auxiliary info file to help dumb servers

SYNOPSIS --------

> ’git update-server-info’ \[-f \| --force\]

DESCRIPTION ----------- A dumb server that does not do on-the-fly pack generations must have some auxiliary information files in \$GIT_DIR/info and \$GIT_OBJECT_DIRECTORY/info directories to help clients discover what references and packs the server has. This command generates such auxiliary files.

OPTIONS ------- -f:: --force:: Update the info files from scratch.

OUTPUT ------

Currently the command updates the following files. Please see [gitrepository-layout](gitrepository-layout.md) for a description of what they are for:

- objects/info/packs

<!-- -->

- info/refs

GIT --- Part of the [git](git.md) suite
