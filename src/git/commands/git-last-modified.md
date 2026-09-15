---
title: git-last-modified
description: 'EXPERIMENTAL: Show when files were last modified'
source_url: https://git-scm.com/doc/git-last-modified
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-last-modified.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 780
---

git-last-modified(1) ====================

NAME ---- git-last-modified - EXPERIMENTAL: Show when files were last modified

SYNOPSIS --------

git last-modified \[--recursive\] \[--show-trees\] \[--max-depth=\<depth\>\] \[-z\] \[\<revision-range\>\] \[\[--\] \<pathspec\>…\]

DESCRIPTION -----------

Shows which commit last modified each of the relevant files and subdirectories. A commit renaming a path, or changing it’s mode is also taken into account.

THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.

OPTIONS -------

`-r`  

`--recursive`  
Recursively traverse into all subtrees. By default, the command only shows tree entries matching the `<pathspec>`. With this option, it descends into subtrees and displays all entries within them. Equivalent to `--max-depth=-1`.

`-t`  

`--show-trees`  
Show tree entries even when recursing into them.

`--max-depth=<depth>`  
For each pathspec given on the command line, traverse at most `<depth>` levels into subtrees. A negative value means no limit. The default is 0, which shows all paths matching the pathspec without descending into subtrees.

`-z`  
Terminate each line with a *NUL* character rather than a newline.

`<revision-range>`  
Only traverse commits in the specified revision range. When no `<revision-range>` is specified, it defaults to `HEAD` (i.e. the whole history leading to the current commit). For a complete list of ways to spell `<revision-range>`, see the ’Specifying Ranges’ section of [gitrevisions](gitrevisions.md).

`[--]` `<pathspec>…`  
Show the commit that last modified each path matching *\<pathspec\>*. If no *\<pathspec\>* is given, all files and subdirectories are included. See [gitglossary](gitglossary.md) for details on pathspec syntax.

OUTPUT ------

The output is in the format:

     <oid> TAB <path> LF

If a path contains any special characters, the path is C-style quoted. To avoid quoting, pass option `-z` to terminate each line with a NUL.

     <oid> TAB <path> NUL

SEE ALSO -------- [git-blame](git-blame.md), [git-log](git-log.md).

GIT --- Part of the [git](git.md) suite
