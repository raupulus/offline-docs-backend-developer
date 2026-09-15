---
title: git-verify-tag
description: Check the GPG signature of tags
source_url: https://git-scm.com/doc/git-verify-tag
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-verify-tag.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1640
---

git-verify-tag(1) =================

NAME ---- git-verify-tag - Check the GPG signature of tags

SYNOPSIS --------

git verify-tag \[-v \| --verbose\] \[--format=\<format\>\] \[--raw\] \<tag\>…

DESCRIPTION ----------- Validates the gpg signature created by `git` `tag` in the tag objects listed on the command line.

OPTIONS ------- `--raw`:: Print the raw gpg status output to standard error instead of the normal human-readable output.

`-v`  

`--verbose`  
Print the contents of the tag object before validating it.

GIT --- Part of the [git](git.md) suite
