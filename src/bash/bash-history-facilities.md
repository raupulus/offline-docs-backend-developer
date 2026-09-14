---
title: Bash History Facilities
source_url: https://www.gnu.org/software/bash/manual
source_path: 049-bash-history-facilities.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 490
---

## Bash History Facilities

command history

history list

When the `-o history` option to the `set` builtin is enabled (see [The Set Builtin](#The-Set-Builtin)), the shell provides access to the command history, the list of commands previously typed. The value of the `HISTSIZE` shell variable is used as the number of commands to save in a history list: the shell saves the text of the last `$HISTSIZE` commands (default 500). The shell stores each command in the history list prior to parameter and variable expansion but after history expansion is performed, subject to the values of the shell variables `HISTIGNORE` and `HISTCONTROL`.

When the shell starts up, Bash initializes the history list by reading history entries from the file named by the `HISTFILE` variable (default `~/.bash_history`). This is referred to as the history file. The history file is truncated, if necessary, to contain no more than the number of history entries specified by the value of the `HISTFILESIZE` variable. If `HISTFILESIZE` is unset, or set to null, a non-numeric value, or a numeric value less than zero, the history file is not truncated.

When the history file is read, lines beginning with the history comment character followed immediately by a digit are interpreted as timestamps for the following history entry. These timestamps are optionally displayed depending on the value of the `HISTTIMEFORMAT` variable (see [Bash Variables](#Bash-Variables)). When present, history timestamps delimit history entries, making multi-line entries possible.

When a shell with history enabled exits, Bash copies the last `$HISTSIZE` entries from the history list to the file named by `$HISTFILE`. If the `histappend` shell option is set (see [Bash Builtins](#Bash-Builtins)), Bash appends the entries to the history file, otherwise it overwrites the history file. If `HISTFILE` is unset or null, or if the history file is unwritable, the history is not saved. After saving the history, Bash truncates the history file to contain no more than `$HISTFILESIZE` lines as described above.

If the `HISTTIMEFORMAT` variable is set, the shell writes the timestamp information associated with each history entry to the history file, marked with the history comment character, so timestamps are preserved across shell sessions. When the history file is read, lines beginning with the history comment character followed immediately by a digit are interpreted as timestamps for the following history entry. As above, when using `HISTTIMEFORMAT`, the timestamps delimit multi-line history entries.

The `fc` builtin command will list or edit and re-execute a portion of the history list. The `history` builtin can display or modify the history list and manipulate the history file. When using command-line editing, search commands are available in each editing mode that provide access to the history list (see [Commands For History](#Commands-For-History)).

The shell allows control over which commands are saved on the history list. The `HISTCONTROL` and `HISTIGNORE` variables are used to save only a subset of the commands entered. If the `cmdhist` shell option is enabled, the shell attempts to save each line of a multi-line command in the same history entry, adding semicolons where necessary to preserve syntactic correctness. The `lithist` shell option modifies `cmdhist` by saving the command with embedded newlines instead of semicolons. The `shopt` builtin is used to set these options. See [The Shopt Builtin](#The-Shopt-Builtin), for a description of `shopt`.
