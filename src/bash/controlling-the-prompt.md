---
title: Controlling the Prompt
source_url: https://www.gnu.org/software/bash/manual
source_path: 031-controlling-the-prompt.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 310
---

## Controlling the Prompt

prompting

In addition, the following table describes the special characters which can appear in the prompt variables `PS0`, `PS1`, `PS2`, and `PS4`:

`\a`  
A bell character.

`\d`  
The date, in "Weekday Month Date" format (e.g., "Tue May 26").

`\D{format}`  
The \<format\> is passed to `strftime`(3) and the result is inserted into the prompt string; an empty \<format\> results in a locale-specific time representation. The braces are required.

`\e`  
An escape character.

`\h`  
The hostname, up to the first ‘`.`’.

`\H`  
The hostname.

`\j`  
The number of jobs currently managed by the shell.

`\l`  
The basename of the shell’s terminal device name (e.g., "ttys0").

`\n`  
A newline.

`\r`  
A carriage return.

`\s`  
The name of the shell: the basename of `$0` (the portion following the final slash).

`\t`  
The time, in 24-hour HH:MM:SS format.

`\T`  
The time, in 12-hour HH:MM:SS format.

`\@`  
The time, in 12-hour am/pm format.

`\A`  
The time, in 24-hour HH:MM format.

`\u`  
The username of the current user.

`\v`  
The Bash version (e.g., 2.00).

`\V`  
The Bash release, version + patchlevel (e.g., 2.00.0).

`\w`  
The value of the `PWD` shell variable (`$PWD`), with `$HOME` abbreviated with a tilde (uses the `$PROMPT_DIRTRIM` variable).

`\W`  
The basename of `$PWD`, with `$HOME` abbreviated with a tilde.

`\!`  
The history number of this command.

`\#`  
The command number of this command.

`\$`  
If the effective uid is 0, `#`, otherwise `$`.

`\nnn`  
The character whose ASCII code is the octal value \<nnn\>.

`\\`  
A backslash.

`\[`  
Begin a sequence of non-printing characters. Thiss could be used to embed a terminal control sequence into the prompt.

`\]`  
End a sequence of non-printing characters.

The command number and the history number are usually different: the history number of a command is its position in the history list, which may include commands restored from the history file (see [Bash History Facilities](#Bash-History-Facilities)), while the command number is the position in the sequence of commands executed during the current shell session.

After the string is decoded, it is expanded via parameter expansion, command substitution, arithmetic expansion, and quote removal, subject to the value of the `promptvars` shell option (see [The Shopt Builtin](#The-Shopt-Builtin)). This can have unwanted side effects if escaped portions of the string appear within command substitution or contain characters special to word expansion.
