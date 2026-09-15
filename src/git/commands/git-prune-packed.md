---
title: git-prune-packed
description: Remove extra objects that are already in pack files
source_url: https://git-scm.com/doc/git-prune-packed
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-prune-packed.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1050
---

git-prune-packed(1) ===================

NAME ---- git-prune-packed - Remove extra objects that are already in pack files

SYNOPSIS --------

> ’git prune-packed’ \[-n \| --dry-run\] \[-q \| --quiet\]

DESCRIPTION ----------- This program searches the `$GIT_OBJECT_DIRECTORY` for all objects that currently exist in a pack file as well as in the independent object directories.

All such extra objects are removed.

A pack is a collection of objects, individually compressed, with delta compression applied, stored in a single file, with an associated index file.

Packs are used to reduce the load on mirror systems, backup engines, disk storage, etc.

OPTIONS ------- -n:: --dry-run:: Don’t actually remove any objects, only show those that would have been removed.

-q  

--quiet  
Squelch the progress indicator.

SEE ALSO -------- [git-pack-objects](git-pack-objects.md) [git-repack](git-repack.md)

GIT --- Part of the [git](git.md) suite
