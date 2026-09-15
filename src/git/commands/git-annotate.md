---
title: git-annotate
description: Annotate file lines with commit information
source_url: https://git-scm.com/doc/git-annotate
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-annotate.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 30
---

git-annotate(1) ===============

NAME ---- git-annotate - Annotate file lines with commit information

SYNOPSIS --------

> ’git annotate’ \[\<options\>\] \[\<rev-opts\>\] \[\<rev\>\] \[--\] \<file\>

DESCRIPTION ----------- Annotates each line in the given file with information from the commit which introduced the line. Optionally annotates from a given revision.

The only difference between this command and [git-blame](git-blame.md) is that they use slightly different output formats, and this command exists only for backward compatibility to support existing scripts, and provide a more familiar command name for people coming from other SCM systems.

OPTIONS ------- include::blame-options.adoc\[\]

SEE ALSO -------- [git-blame](git-blame.md)

GIT --- Part of the [git](git.md) suite
