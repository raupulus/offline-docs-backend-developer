---
title: Bash History Builtins
source_url: https://www.gnu.org/software/bash/manual
source_path: 050-bash-history-builtins.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 500
---

## Bash History Builtins

history builtins

Bash provides two builtin commands which manipulate the history list and history file.

`fc`  

fc

    fc [-e ename] [-lnr] [first] [last]
    fc -s [pat=rep] [command]

The first form selects a range of commands from \<first\> to \<last\> from the history list and displays or edits and re-executes them. Both \<first\> and \<last\> may be specified as a string (to locate the most recent command beginning with that string) or as a number (an index into the history list, where a negative number is used as an offset from the current command number).

When listing, a \<first\> or \<last\> of 0 is equivalent to -1 and -0 is equivalent to the current command (usually the `fc` command); otherwise 0 is equivalent to -1 and -0 is invalid.

If \<last\> is not specified, it is set to the current command for listing and to \<first\> otherwise. If \<first\> is not specified, it is set to the previous command for editing and −16 for listing.

If the `-l` flag is supplied, the commands are listed on standard output. The `-n` flag suppresses the command numbers when listing. The `-r` flag reverses the order of the listing.

Otherwise, `fc` invokes the editor named by \<ename\> on a file containing those commands. If \<ename\> is not supplied, `fc` uses the value of the following variable expansion: `${FCEDIT:-${EDITOR:-vi}}`. This says to use the value of the `FCEDIT` variable if set, or the value of the `EDITOR` variable if that is set, or `vi` if neither is set. When editing is complete, `fc` reads the file of edited commands and echoes and executes them.

In the second form, `fc` re-executes \<command\> after replacing each instance of \<pat\> in the selected command with \<rep\>. \<command\> is interpreted the same as \<first\> above.

A useful alias to use with the `fc` command is `r='fc -s'`, so that typing ‘`r cc`’ runs the last command beginning with `cc` and typing ‘`r`’ re-executes the last command (see [Aliases](#Aliases)).

If the first form is used, the return value is zero unless an invalid option is encountered or \<first\> or \<last\> specify history lines out of range. When editing and re-executing a file of commands, the return value is the value of the last command executed or failure if an error occurs with the temporary file. If the second form is used, the return status is that of the re-executed command, unless \<command\> does not specify a valid history entry, in which case `fc` returns a non-zero status.

`history`  

history

    history [n]
    history -c
    history -d offset
    history -d start-end
    history [-anrw] [filename]
    history -ps arg

With no options, display the history list with numbers. Entries prefixed with a ‘`*`’ have been modified. An argument of \<n\> lists only the last \<n\> entries. If the shell variable `HISTTIMEFORMAT` is set and not null, it is used as a format string for `strftime`(3) to display the time stamp associated with each displayed history entry. If `history` uses `HISTTIMEFORMAT`, it does not print an intervening space between the formatted time stamp and the history entry.

Options, if supplied, have the following meanings:

`-c`  
Clear the history list. This may be combined with the other options to replace the history list.

`-d offset`  
Delete the history entry at position \<offset\>. If \<offset\> is positive, it should be specified as it appears when the history is displayed. If \<offset\> is negative, it is interpreted as relative to one greater than the last history position, so negative indices count back from the end of the history, and an index of ‘`-1`’ refers to the current `history -d` command.

`-d start-end`  
Delete the range of history entries between positions \<start\> and \<end\>, inclusive. Positive and negative values for \<start\> and \<end\> are interpreted as described above.

`-a`  
Append the "new" history lines to the history file. These are history lines entered since the beginning of the current Bash session, but not already appended to the history file.

`-n`  
Read the history lines not already read from the history file and add them to the current history list. These are lines appended to the history file since the beginning of the current Bash session.

`-r`  
Read the history file and append its contents to the history list.

`-w`  
Write the current history list to the history file, overwriting the history file.

`-p`  
Perform history substitution on the \<arg\>s and display the result on the standard output, without storing the results in the history list.

`-s`  
Add the \<arg\>s to the end of the history list as a single entry. The last command in the history list is removed before adding the \<arg\>s.

If a \<filename\> argument is supplied with any of the `-w`, `-r`, `-a`, or `-n` options, Bash uses \<filename\> as the history file. If not, it uses the value of the `HISTFILE` variable. If `HISTFILE` is unset or null, these options have no effect.

If the `HISTTIMEFORMAT` variable is set, `history` writes the time stamp information associated with each history entry to the history file, marked with the history comment character as described above. When the history file is read, lines beginning with the history comment character followed immediately by a digit are interpreted as timestamps for the following history entry.

The return value is 0 unless an invalid option is encountered, an error occurs while reading or writing the history file, an invalid \<offset\> or range is supplied as an argument to `-d`, or the history expansion supplied as an argument to `-p` fails.
