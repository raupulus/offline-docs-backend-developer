---
title: git-whatchanged
description: Show logs with differences each commit introduces
source_url: https://git-scm.com/doc/git-whatchanged
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-whatchanged.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1670
---

git-whatchanged(1) ==================

NAME ---- git-whatchanged - Show logs with differences each commit introduces

SYNOPSIS --------

git whatchanged \<option\>…

WARNING ------- `git` `whatchanged` has been deprecated and is scheduled for removal in a future version of Git, as it is merely `git` `log` with different defaults.

DESCRIPTION -----------

Shows commit logs and diff output each commit introduces.

New users are encouraged to use [git-log](git-log.md) instead. The `whatchanged` command is essentially the same as [git-log](git-log.md) but defaults to showing the raw format diff output and skipping merges:

    git log --raw --no-merges

The command is primarily kept for historical reasons; fingers of many people who learned Git long before `git` `log` was invented by reading the Linux kernel mailing list are trained to type it.

Examples -------- `git` `whatchanged` `-p` `v2.6.12..` `include/scsi` `drivers/scsi`::

    Show as patches the commits since version 'v2.6.12' that changed
    any file in the include/scsi or drivers/scsi subdirectories

`git` `whatchanged` `--since="2` `weeks` `ago" — gitk`  

<!-- -->

    Show the changes during the last two weeks to the file 'gitk'.
    The "--" is necessary to avoid confusion with the *branch* named
    'gitk'

GIT --- Part of the [git](git.md) suite
