---
title: git-check-mailmap
description: Show canonical names and email addresses of contacts
source_url: https://git-scm.com/doc/git-check-mailmap
source_repo: https://github.com/git/git.git
source_ref: master
source_commit: 339ab2a8f
source_path: git-check-mailmap.adoc
technology: git
version: master
license: GPL-2.0
retrieved_at: '2026-09-15'
section: commands
order: 170
---

git-check-mailmap(1) ====================

NAME ---- git-check-mailmap - Show canonical names and email addresses of contacts

SYNOPSIS --------

> ’git check-mailmap’ \[\<options\>\] \<contact\>…

DESCRIPTION -----------

For each `Name` `$$<user@host>$$’’,`\$\$\<user@host\>\$\$’’, or \`\`\$\$user@host\$\$’’ from the command-line or standard input (when using `--stdin`), look up the person’s canonical name and email address (see "Mapping Authors" below). If found, print them; otherwise print the input as-is.

OPTIONS ------- --stdin:: Read contacts, one per line, from the standard input after exhausting contacts provided on the command-line.

--mailmap-file=\<file\>  
In addition to any configured mailmap files, read the specified mailmap file. Entries in this file take precedence over entries in either the default mailmap file or any configured mailmap file.

--mailmap-blob=\<blob\>  
Like `--mailmap-file`, but consider the value as a reference to a blob in the repository. If both `--mailmap-file` and `--mailmap-blob` are specified, entries in `--mailmap-file` will take precedence.

OUTPUT ------

For each contact, a single line is output, terminated by a newline. If the name is provided or known to the ’mailmap’, `Name` `$$<user@host>$$’’` `is` `printed;` `otherwise` `only`\$\$\<user@host\>\$\$’’ is printed.

CONFIGURATION -------------

See `mailmap.file` and `mailmap.blob` in [git-config](git-config.md) for how to specify a custom `.mailmap` target file or object.

MAPPING AUTHORS ---------------

See [gitmailmap](gitmailmap.md).

GIT --- Part of the [git](git.md) suite
