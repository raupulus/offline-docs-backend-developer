---
title: git-count-objects
description: Count unpacked number of objects and their disk consumption
source_url: https://git-scm.com/doc/git-count-objects
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-count-objects.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 310
---

git-count-objects(1) ====================

NAME ---- git-count-objects - Count unpacked number of objects and their disk consumption

SYNOPSIS --------

> ’git count-objects’ \[-v\] \[-H \| --human-readable\]

DESCRIPTION ----------- Counts the number of unpacked object files and disk space consumed by them, to help you decide when it is a good time to repack.

OPTIONS ------- -v:: --verbose:: Provide more detailed reports:\
count: the number of loose objects\
size: disk space consumed by loose objects, in KiB (unless -H is specified)\
in-pack: the number of in-pack objects\
packs: the number of pack files\
size-pack: disk space consumed by the packs, in KiB (unless -H is specified)\
prune-packable: the number of loose objects that are also present in the packs. These objects could be pruned using `git` `prune-packed`.\
garbage: the number of files in the object database that are neither valid loose objects nor valid packs\
size-garbage: disk space consumed by garbage files, in KiB (unless -H is specified)\
alternate: absolute path of alternate object databases; may appear multiple times, one line per path. Note that if the path contains non-printable characters, it may be surrounded by double-quotes and contain C-style backslashed escape sequences.

-H  

--human-readable  

Print sizes in human readable format

GIT --- Part of the [git](git.md) suite
