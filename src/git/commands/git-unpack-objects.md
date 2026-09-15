---
title: git-unpack-objects
description: Unpack objects from a packed archive
source_url: https://git-scm.com/doc/git-unpack-objects
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-unpack-objects.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1540
---

git-unpack-objects(1) =====================

NAME ---- git-unpack-objects - Unpack objects from a packed archive

SYNOPSIS --------

> ’git unpack-objects’ \[-n\] \[-q\] \[-r\] \[--strict\]

DESCRIPTION ----------- Read a packed archive (.pack) from the standard input, expanding the objects contained within and writing them into the repository in "loose" (one object per file) format.

Objects that already exist in the repository will **not** be unpacked from the packfile. Therefore, nothing will be unpacked if you use this command on a packfile that exists within the target repository.

See [git-repack](git-repack.md) for options to generate new packs and replace existing ones.

OPTIONS ------- -n:: Dry run. Check the pack file without actually unpacking the objects.

-q  
The command usually shows percentage progress. This flag suppresses it.

-r  
When unpacking a corrupt packfile, the command dies at the first corruption. This flag tells it to keep going and make the best effort to recover as many objects as possible.

--strict  
Don’t write objects with broken content or links.

--max-input-size=\<size\>  
Die, if the pack is larger than \<size\>.

GIT --- Part of the [git](git.md) suite
