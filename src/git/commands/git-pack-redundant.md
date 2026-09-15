---
title: git-pack-redundant
description: Find redundant pack files
source_url: https://git-scm.com/doc/git-pack-redundant
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-pack-redundant.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1020
---

git-pack-redundant(1) =====================

NAME ---- git-pack-redundant - Find redundant pack files

SYNOPSIS --------

> ’git pack-redundant’ \[--verbose\] \[--alt-odb\] (--all \| \<pack-filename\>…)

WARNING ------- `git` `pack-redundant` has been deprecated and is scheduled for removal in a future version of Git. Because it can only remove entire duplicate packs and not individual duplicate objects, it is generally not a useful tool for reducing repository size. You are better off using `git` `gc` to do so, which will put objects into a new pack, removing duplicates.

Running `pack-redundant` without the `--i-still-use-this` flag will fail in this release. If you believe you have a use case for which `pack-redundant` is better suited and oppose this removal, please contact the Git mailing list at git@vger.kernel.org. More information about the list is available at <https://git-scm.com/community>.

DESCRIPTION ----------- This program computes which packs in your repository are redundant. The output is suitable for piping to `xargs` `rm` if you are in the root of the repository.

’git pack-redundant’ accepts a list of objects on standard input. Any objects given will be ignored when checking which packs are required. This makes the following command useful when wanting to remove packs which contain unreachable objects.

git fsck --full --unreachable \| cut -d ’ ’ -f3 \| \\ git pack-redundant --all \| xargs rm

OPTIONS -------

--all  
Processes all packs. Any filenames on the command line are ignored.

--alt-odb  
Don’t require objects present in packs from alternate object database (odb) directories to be present in local packs.

--verbose  
Outputs some statistics to stderr. Has a small performance penalty.

SEE ALSO -------- [git-pack-objects](git-pack-objects.md) [git-repack](git-repack.md) [git-prune-packed](git-prune-packed.md)

GIT --- Part of the [git](git.md) suite
