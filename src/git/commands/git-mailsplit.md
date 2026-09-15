---
title: git-mailsplit
description: Simple UNIX mbox splitter program
source_url: https://git-scm.com/doc/git-mailsplit
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-mailsplit.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 840
---

git-mailsplit(1) ================

NAME ---- git-mailsplit - Simple UNIX mbox splitter program

SYNOPSIS --------

> ’git mailsplit’ \[-b\] \[-f\<nn\>\] \[-d\<prec\>\] \[--keep-cr\] \[--mboxrd\]\
> -o\<directory\> \[--\] \[(\<mbox\>\|\<Maildir\>)…\]

DESCRIPTION ----------- Splits a mbox file or a Maildir into a list of files: "0001" "0002" .. in the specified directory so you can process them further from there.

> [!IMPORTANT]
> Maildir splitting relies upon filenames being sorted to output patches in the correct order.

OPTIONS ------- \<mbox\>:: Mbox file to split. If not given, the mbox is read from the standard input.

\<Maildir\>  
Root of the Maildir to split. This directory should contain the cur, tmp and new subdirectories.

-o\<directory\>  
Directory in which to place the individual messages.

-b  
If any file doesn’t begin with a From line, assume it is a single mail message instead of signaling an error.

-d\<prec\>  
Instead of the default 4 digits with leading zeros, different precision can be specified for the generated filenames.

-f\<nn\>  
Skip the first \<nn\> numbers, for example if -f3 is specified, start the numbering with 0004.

--keep-cr  
Do not remove `r` from lines ending with `rn`.

--mboxrd  
Input is of the "mboxrd" format and "^\>+From " line escaping is reversed.

GIT --- Part of the [git](git.md) suite
