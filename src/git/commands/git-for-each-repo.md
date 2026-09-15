---
title: git-for-each-repo
description: Run a Git command on a list of repositories
source_url: https://git-scm.com/doc/git-for-each-repo
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-for-each-repo.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 550
---

git-for-each-repo(1) ====================

NAME ---- git-for-each-repo - Run a Git command on a list of repositories

SYNOPSIS --------

> ’git for-each-repo’ --config=\<config\> \[--\] \<arguments\>

DESCRIPTION ----------- Run a Git command on a list of repositories. The arguments after the known options or `--` indicator are used as the arguments for the Git subprocess.

THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.

For example, we could run maintenance on each of a list of repositories stored in a `maintenance.repo` config variable using

    git for-each-repo --config=maintenance.repo maintenance run

This will run `git` `-C` `<repo>` `maintenance` `run` for each value `<repo>` in the multi-valued config variable `maintenance.repo`.

OPTIONS ------- --config=\<config\>:: Use the given config variable as a multi-valued list storing absolute path names. Iterate on that list of paths to run the given arguments.\
These config values are loaded from system, global, and local Git config, as available. If `git` `for-each-repo` is run in a directory that is not a Git repository, then only the system and global config is used.

--keep-going  
Continue with the remaining repositories if the command failed on a repository. The exit code will still indicate that the overall operation was not successful.

Note that the exact exit code of the failing command is not passed through as the exit code of the `for-each-repo` command: If the command failed in any of the specified repositories, the overall exit code will be 1.

SUBPROCESS BEHAVIOR -------------------

If any `git` `-C` `<repo>` `<arguments>` subprocess returns a non-zero exit code, then the `git` `for-each-repo` process returns that exit code without running more subprocesses.

Each `git` `-C` `<repo>` `<arguments>` subprocess inherits the standard file descriptors `stdin`, `stdout`, and `stderr`.

GIT --- Part of the [git](git.md) suite
