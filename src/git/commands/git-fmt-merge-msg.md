---
title: git-fmt-merge-msg
description: Produce a merge commit message
source_url: https://git-scm.com/doc/git-fmt-merge-msg
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-fmt-merge-msg.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 530
---

git-fmt-merge-msg(1) ====================

NAME ---- git-fmt-merge-msg - Produce a merge commit message

SYNOPSIS --------

> ’git fmt-merge-msg’ \[-m \<message\>\] \[--into-name \<branch\>\] \[--log\[=\<n\>\] \| --no-log\]\
> ’git fmt-merge-msg’ \[-m \<message\>\] \[--log\[=\<n\>\] \| --no-log\] -F \<file\>

DESCRIPTION ----------- Takes the list of merged objects on stdin and produces a suitable commit message to be used for the merge commit, usually to be passed as the ’\<merge-message\>’ argument of ’git merge’.

This command is intended mostly for internal use by scripts automatically invoking ’git merge’.

OPTIONS -------

--log\[=\<n\>\]  
In addition to branch names, populate the log message with one-line descriptions from the actual commits that are being merged. At most \<n\> commits from each merge parent will be used (20 if \<n\> is omitted). This overrides the `merge.log` configuration variable.

--no-log  
Do not list one-line descriptions from the actual commits being merged.

--summary  

--no-summary  
Synonyms to --log and --no-log; these are deprecated and will be removed in the future.

-m \<message\>  

--message \<message\>  
Use \<message\> instead of the branch names for the first line of the log message. For use with `--log`.

--into-name \<branch\>  
Prepare the merge message as if merging to the branch `<branch>`, instead of the name of the real branch to which the merge is made.

-F \<file\>  

--file \<file\>  
Take the list of merged objects from \<file\> instead of stdin.

CONFIGURATION ------------- include::config/fmt-merge-msg.adoc\[\]

merge.summary  
Synonym to `merge.log`; this is deprecated and will be removed in the future.

EXAMPLES --------

    $ git fetch origin master
    $ git fmt-merge-msg --log <$GIT_DIR/FETCH_HEAD

Print a log message describing a merge of the "master" branch from the "origin" remote.

SEE ALSO -------- [git-merge](git-merge.md)

GIT --- Part of the [git](git.md) suite
