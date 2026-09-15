---
title: git-repo
description: Retrieve information about the repository
source_url: https://git-scm.com/doc/git-repo
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-repo.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 1220
---

git-repo(1) ===========

NAME ---- git-repo - Retrieve information about the repository

SYNOPSIS --------

git repo info \[--format=(lines\|nul) \| -z\] \[--all \| \<key\>…\] git repo info --keys \[--format=(lines\|nul) \| -z\] git repo structure \[--format=(table\|lines\|nul) \| -z\]

DESCRIPTION ----------- Retrieve information about the repository.

THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.

COMMANDS -------- `info` `[--format=(lines|nul)` `|` `-z]` `[--all` `|` `<key>…]`:: Retrieve metadata-related information about the current repository. Only the requested data will be returned based on their keys (see "INFO KEYS" section below).\
The values are returned in the same order in which their respective keys were requested. The `--all` flag requests the values for all the available keys.\
The output format can be chosen through the flag `--format`. Two formats are supported: +

`lines`::: Output key-value pairs one per line using the `=` character as the delimiter between the key and the value. Values containing "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config](git-config.md)). This is the default.

`nul`::: Similar to `lines`, but using a newline character as the delimiter between the key and the value and using a *NUL* character after each value. This format is better suited for being parsed by another applications than `lines`. Unlike in the `lines` format, the values are never quoted.\
`-z` is an alias for `--format=nul`.

`info` `--keys` `[--format=(lines|nul)` `|` `-z]`  
List all the available keys, one per line. The output format can be chosen through the flag `--format`. The following formats are supported:

`lines`  
Output the keys one per line. This is the default.

`nul`  
Similar to `lines`, but using a *NUL* character after each value.

`structure` `[--format=(table|lines|nul)` `|` `-z]`  
Retrieve statistics about the current repository structure. The following kinds of information are reported:

- Reference counts categorized by type

- Reachable object counts categorized by type

- Total inflated size of reachable objects by type

- Total disk size of reachable objects by type

- Largest reachable objects in the repository by type

  The output format can be chosen through the flag `--format`. Three formats are supported:

`table`  
Outputs repository stats in a human-friendly table. This format may change and is not intended for machine parsing. This is the default format.

`lines`  
Each line of output contains a key-value pair for a repository stat. The ’=’ character is used to delimit between the key and the value. Values containing "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config](git-config.md)).

`nul`  
Similar to `lines`, but uses a *NUL* character to delimit between key-value pairs instead of a newline. Also uses a newline character as the delimiter between the key and value instead of ’=’. Unlike the `lines` format, values containing "unusual" characters are never quoted.

`-z` is an alias for `--format=nul`.

INFO KEYS --------- In order to obtain a set of values from `git` `repo` `info`, you should provide the keys that identify them. Here’s a list of the available keys and the values that they return:

`layout.bare`  
`true` if this is a bare repository, otherwise `false`.

`layout.shallow`  
`true` if this is a shallow repository, otherwise `false`.

`object.format`  
The object format (hash algorithm) used in the repository.

`path.commondir.absolute`  
The canonical absolute path to the Git repository’s common directory (the shared `.git` directory containing objects, refs, and global configuration).

`path.commondir.relative`  
The path to the Git repository’s common directory relative to the current working directory.

`path.gitdir.absolute`  
The canonical absolute path to the Git repository directory (the `.git` directory).

`path.gitdir.relative`  
The path to the Git repository directory relative to the current working directory.

`references.format`  
The reference storage format. The valid values are:

<div class="included" data-path="ref-storage-format.adoc">

`files`;; for loose files with packed-refs. ifndef::with-breaking-changes\[\] This is the default. endif::with-breaking-changes\[\] `reftable`;; for the reftable format. ifdef::with-breaking-changes\[\] This is the default. endif::with-breaking-changes\[\]

</div>

EXAMPLES --------

- Retrieves the reference format of the current repository:

      git repo info references.format

<!-- -->

- Retrieves whether the current repository is bare and whether it is shallow using the `nul` format:

      git repo info --format=nul layout.bare layout.shallow

SEE ALSO -------- [git-rev-parse](git-rev-parse.md)

GIT --- Part of the [git](git.md) suite
