---
title: git-mktree
description: Build a tree-object from ls-tree formatted text
source_url: https://git-scm.com/doc/git-mktree
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-mktree.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 950
---

git-mktree(1) =============

NAME ---- git-mktree - Build a tree-object from ls-tree formatted text

SYNOPSIS --------

> ’git mktree’ \[-z\] \[--missing\] \[--batch\]

DESCRIPTION ----------- Reads standard input in non-recursive `ls-tree` output format, and creates a tree object. The order of the tree entries is normalized by mktree so pre-sorting the input is not required. The object name of the tree object built is written to the standard output.

OPTIONS ------- -z:: Read the NUL-terminated `ls-tree` `-z` output instead.

--missing  
Allow missing objects. The default behaviour (without this option) is to verify that each tree entry’s hash identifies an existing object. This option has no effect on the treatment of gitlink entries (aka "submodules") which are always allowed to be missing.

--batch  
Allow building of more than one tree object before exiting. Each tree is separated by a single blank line. The final newline is optional. Note - if the `-z` option is used, lines are terminated with NUL.

GIT --- Part of the [git](git.md) suite
