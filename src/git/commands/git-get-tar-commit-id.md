---
title: git-get-tar-commit-id
description: Extract commit ID from an archive created using git-archive
source_url: https://git-scm.com/doc/git-get-tar-commit-id
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-get-tar-commit-id.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 620
---

git-get-tar-commit-id(1) ========================

NAME ---- git-get-tar-commit-id - Extract commit ID from an archive created using git-archive

SYNOPSIS --------

> ’git get-tar-commit-id’

DESCRIPTION -----------

Read a tar archive created by ’git archive’ from the standard input and extract the commit ID stored in it. It reads only the first 1024 bytes of input, thus its runtime is not influenced by the size of the tar archive very much.

If no commit ID is found, ’git get-tar-commit-id’ quietly exits with a return code of 1. This can happen if the archive had not been created using ’git archive’ or if the first parameter of ’git archive’ had been a tree ID instead of a commit ID or tag.

GIT --- Part of the [git](git.md) suite
