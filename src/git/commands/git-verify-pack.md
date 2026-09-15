---
title: git-verify-pack
description: Validate packed Git archive files
source_url: https://git-scm.com/doc/git-verify-pack
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-verify-pack.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1630
---

git-verify-pack(1) ==================

NAME ---- git-verify-pack - Validate packed Git archive files

SYNOPSIS --------

git verify-pack \[-v \| --verbose\] \[-s \| --stat-only\] \[--\] \<pack\>.idx…

DESCRIPTION ----------- Read each idx file for packed Git archive given on the command line, and verify the idx file and the corresponding pack file.

OPTIONS ------- `-v`:: `--verbose`:: After verifying the pack, show the list of objects contained in the pack and a histogram of delta chain length.

`-s`  

`--stat-only`  
Do not verify the pack contents; only show the histogram of delta chain length. With `--verbose`, the list of objects is also shown.

`--`  
Do not interpret any more arguments as options.

OUTPUT FORMAT ------------- When specifying the `-v` option the format used is:

    object-name type size size-in-packfile offset-in-packfile

for objects that are not deltified in the pack, and

    object-name type size size-in-packfile offset-in-packfile depth base-object-name

for objects that are deltified.

GIT --- Part of the [git](git.md) suite
