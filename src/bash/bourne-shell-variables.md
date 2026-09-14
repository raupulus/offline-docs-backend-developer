---
title: Bourne Shell Variables
source_url: https://www.gnu.org/software/bash/manual
source_path: 020-bourne-shell-variables.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 200
---

## Bourne Shell Variables

Bash uses certain shell variables in the same way as the Bourne shell. In some cases, Bash assigns a default value to the variable.

<span class="indexterm vr" role="vr"></span>`CDPATH`  
A colon-separated list of directories used as a search path for the `cd` builtin command.

<span class="indexterm vr" role="vr"></span>`HOME`  
The current user’s home directory; the default for the `cd` builtin command. The value of this variable is also used by tilde expansion (see [Tilde Expansion](#Tilde-Expansion)).

<span class="indexterm vr" role="vr"></span>`IFS`  
A list of characters that separate fields; used when the shell splits words as part of expansion and by the `read` builtin to split lines into words. See [Word Splitting](#Word-Splitting), for a description of word splitting.

<span class="indexterm vr" role="vr"></span>`MAIL`  
If the value is set to a filename or directory name and the `MAILPATH` variable is not set, Bash informs the user of the arrival of mail in the specified file or Maildir-format directory.

<span class="indexterm vr" role="vr"></span>`MAILPATH`  
A colon-separated list of filenames which the shell periodically checks for new mail. Each list entry can specify the message that is printed when new mail arrives in the mail file by separating the filename from the message with a ‘`?`’. When used in the text of the message, `$_` expands to the name of the current mail file.

<span class="indexterm vr" role="vr"></span>`OPTARG`  
The value of the last option argument processed by the `getopts` builtin.

<span class="indexterm vr" role="vr"></span>`OPTIND`  
The index of the next argument to be processed by the `getopts` builtin.

<span class="indexterm vr" role="vr"></span>`PATH`  
A colon-separated list of directories in which the shell looks for commands. A zero-length (null) directory name in the value of `PATH` indicates the current directory. A null directory name may appear as two adjacent colons, or as an initial or trailing colon. The default path is system-dependent, and is set by the administrator who installs `bash`. A common value is "/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin".

<span class="indexterm vr" role="vr"></span>`PS1`  
The primary prompt string. The default value is ‘`\s-\v\$`’. See [Controlling the Prompt](#Controlling-the-Prompt), for the complete list of escape sequences that are expanded before `PS1` is displayed.

<span class="indexterm vr" role="vr"></span>`PS2`  
The secondary prompt string. The default value is ‘`>`’. `PS2` is expanded in the same way as `PS1` before being displayed.
