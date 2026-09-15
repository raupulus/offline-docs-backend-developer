---
title: git-show-index
description: Show packed archive index
source_url: https://git-scm.com/doc/git-show-index
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-show-index.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1390
---

git-show-index(1) =================

NAME ---- git-show-index - Show packed archive index

SYNOPSIS --------

> ’git show-index’ \[--object-format=\<hash-algorithm\>\] \< \<pack-idx-file\>

DESCRIPTION ----------- Read the `.idx` file for a Git packfile (created with [git-pack-objects](git-pack-objects.md) or [git-index-pack](git-index-pack.md)) from the standard input, and dump its contents. The output consists of one object per line, with each line containing two or three space-separated columns:

- the first column is the offset in bytes of the object within the corresponding packfile

<!-- -->

- the second column is the object id of the object

<!-- -->

- if the index version is 2 or higher, the third column contains the CRC32 of the object data

The objects are output in the order in which they are found in the index file, which should be (in a correctly constructed file) sorted by object id.

Note that you can get more information on a packfile by calling [git-verify-pack](git-verify-pack.md). However, as this command considers only the index file itself, it’s both faster and more flexible.

OPTIONS -------

--object-format=\<hash-algorithm\>  
Specify the given object format (hash algorithm) for the index file. The valid values are ’sha1’ and (if enabled) ’sha256’. The default is the algorithm for the current repository (set by `extensions.objectFormat`), or ’sha1’ if no value is set or outside a repository..

<div class="included" data-path="object-format-disclaimer.adoc">

Note: At present, there is no interoperability between SHA-256 repositories and SHA-1 repositories.

Historically, we warned that SHA-256 repositories may later need backward incompatible changes when we introduce such interoperability features. Today, we only expect compatible changes. Furthermore, if such changes prove to be necessary, it can be expected that SHA-256 repositories created with today’s Git will be usable by future versions of Git without data loss.

</div>

GIT --- Part of the [git](git.md) suite
