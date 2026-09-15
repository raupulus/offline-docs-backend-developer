---
title: git-format-rev
description: 'EXPERIMENTAL: Pretty format revisions on demand'
source_url: https://git-scm.com/doc/git-format-rev
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-format-rev.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 570
---

git-format-rev(1) =================

NAME ---- git-format-rev - EXPERIMENTAL: Pretty format revisions on demand

SYNOPSIS --------

(EXPERIMENTAL!) git format-rev --stdin-mode=\<mode\> --format=\<pretty\> \[--\[no-\]notes=\<ref\>\] \[-z\] \[--\[no-\]null-output\] \[--\[no-\]null-input\]

DESCRIPTION -----------

Pretty format revisions from standard input.

THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.

OPTIONS -------

`--stdin-mode=<mode>`  
How to interpret standard input data:

<div>

`revs`;; Each line or record (see the <a href="#io" class="cross-reference">INPUT AND OUTPUT FORMATS</a> section) is interpreted as a commit. Any kind of revision expression can be used (see [gitrevisions](gitrevisions.md)). Annotated tags are peeled (see [gitglossary](gitglossary.md)).\
The argument `rev` is also accepted.

`text`;; Formats all commit object names found in freeform text. These must be full object names, i.e. abbreviated hexadecimal object names will not be interpreted.\
Anything that is parsed as an object name but that is not found to be a commit object name is left alone (echoed).

</div>

`--format=<pretty>`  
Pretty format string.

`--notes=<ref>`  

`--no-notes`  
Custom notes ref. Notes are displayed when using the `%N` atom. See [git-notes](git-notes.md).

`-z`  

`--null`  
Use *NUL* character to terminate both input and output instead of newline. This option cannot be negated.

This is useful if both the input and output could contain newlines or if the input to this command also uses *NUL* character termination; see the <a href="#io" class="cross-reference">INPUT AND OUTPUT FORMATS</a> section below.

The mode `--stdin-mode=text` can have use for this option when it needs to process input like for example `git` `last-modified` `-z`; see the <a href="#examples" class="cross-reference">EXAMPLES</a> section below.

`--null-output`  

`--no-null-output`  
Use *NUL* character to terminate output instead of newline. The default is `--no-null-output`.

This is useful if the output could contain newlines, for example if the `%n` (newline) atom is used.

`--null-input`  

`--no-null-input`  
Use *NUL* character to terminate input instead of newline. The default is `--no-null-input`.

This is useful if the input revision expressions could contain newlines.

<div id="io" data-wrapper="1">

INPUT AND OUTPUT FORMAT -----------------------

</div>

The command uses newlines for both input and output termination by default. See the `-z`, `--null-output`, and `--null-input` options for using *NUL* character as the terminator.

The mode `--stdin-mode=revs` outputs one formatted commit followed by the terminator. This could either be called a *line* or a *record* in case "line" is too suggestive of newline termination.

Note that this means that the terminator character (newline or *NUL*) acts as a *terminator*, not a *separator*. In other words, the final line or record is also terminated by the terminator character.

The mode `--stdin-mode=text` replaces each object name with the formatted commit, i.e. the format `"%s"` would transform some commit object name to `"<subject>"` without any termination. Like this:

<div>

Did we not fix this in "\<subject\>"?

</div>

It is safe to interactively read and write from this command since each record is immediately flushed.

<div id="examples" data-wrapper="1">

EXAMPLES --------

</div>

The command [git-last-modified](git-last-modified.md) shows the commit that each file was last modified in.

    $ git last-modified -- README.md Makefile
    7798034171030be0909c56377a4e0e10e6d2df93    Makefile
    c50fbb2dd225e7e82abba4380423ae105089f4d7    README.md

We can pipe the result to this command in order to replace the object name with the commit author.

    $ git last-modified -- README.md Makefile |
        git format-rev --stdin-mode=text --format=%an
    Junio C Hamano  Makefile
    Todd Zullinger  README.md

Another example is *formatting commits in commit messages*. Given this commit message:

    Fix off-by-one error

    Fix off-by-one error introduced in
    e83c5163316f89bfbde7d9ab23ca2e25604af290.

    We thought we fixed this in 5569bf9bbedd63a00780fc5c110e0cfab3aa97b9 but
    that only covered 1/3 of the faulty cases.

We can format the commits and use par(1) to reflow the text, say in a `commit-msg` hook:

    $ git config set hook.reference-commits.event commit-msg
    $ git config set hook.reference-commits.command reference-commits
    $ cat $(which reference-commits)
    #/bin/sh

    msg="$1"
    rewritten=$(mktemp)
    git format-rev --stdin-mode=text --format=reference <"$msg" |
        par >"$rewritten"
    mv "$rewritten" "$msg"

Which will produce something like this:

    Fix off-by-one error

    Fix off-by-one error introduced in e83c5163316 (Implement better memory
    allocator, 2005-04-07).

    We thought we fixed this in 5569bf9bbed (Fix memory allocator,
    2005-06-22) but that only covered 1/3 of the faulty cases.

DISCUSSION ----------

This command lets you format any number of revisions in any order through one command invocation. Consider the [git-last-modified](git-last-modified.md) case from the <a href="#examples" class="cross-reference">EXAMPLES</a> section above:

1.  There might be hundreds of files

2.  Commits can be repeated, i.e. two or more files were last modified in the same commit

Two widely-used commands which pretty formats commits are [git-log](git-log.md) and [git-show](git-show.md). It turns out that they are not a good fit for the above use case.

- The output of [git-last-modified](git-last-modified.md) would have to be processed in stages since you need to transform the first column separately and then link the author to the filename. But this is surmountable.

- You can feed each commit to `git` `show` or `git` `log` `--no-walk` `-1`. But that means that you need to create a process for each line.

- Let’s say that you want to use one process, not one per line. So you want to feed all the commits to the command. Now you face the problem that you have to feed all the commits to the commands before you get any output (this is also the case for the `--stdin` modes). In other words, you cannot loop through each line, get the author for the commit, and output the author and the filename. You need to feed all the commits, get back all the output, and match the output with the filename.

- But the next problem is that commands will deduplicate the input and only output one commit one single time only. Thus you cannot make the output order match the input order, since a commit could have been repeated in the original input.

In short, it is straightforward to use these two commands if you use one process per line. It is much more work if you just want to use one process, but still doable. In contrast, this problem is solved with just another shell pipeline with this command.

SEE ALSO -------- [git-name-rev](git-name-rev.md), [git-log](git-log.md).

GIT --- Part of the [git](git.md) suite
