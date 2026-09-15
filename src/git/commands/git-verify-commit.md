---
title: git-verify-commit
description: Check the GPG signature of commits
source_url: https://git-scm.com/doc/git-verify-commit
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-verify-commit.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1620
---

git-verify-commit(1) ====================

NAME ---- git-verify-commit - Check the GPG signature of commits

SYNOPSIS --------

git verify-commit \[-v \| --verbose\] \[--raw\] \<commit\>…

DESCRIPTION ----------- Validates the GPG signature created by `git` `commit` `-S` on the commit objects given on the command line.

OPTIONS ------- `--raw`:: Print the raw gpg status output to standard error instead of the normal human-readable output.

`-v`  

`--verbose`  
Print the contents of the commit object before validating it.

GIT --- Part of the [git](git.md) suite
