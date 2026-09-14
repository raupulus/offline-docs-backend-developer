---
title: Bash Builtin Commands
source_url: https://www.gnu.org/software/bash/manual
source_path: 016-bash-builtin-commands.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 160
---

## Bash Builtin Commands

This section describes builtin commands which are unique to or have been extended in Bash. Some of these commands are specified in the POSIX standard.

`alias`  

alias

    alias [-p] [name[=value] …]

Without arguments or with the `-p` option, `alias` prints the list of aliases on the standard output in a form that allows them to be reused as input. If arguments are supplied, define an alias for each \<name\> whose \<value\> is given. If no \<value\> is given, print the name and value of the alias \<name\>. A trailing space in \<value\> causes the next word to be checked for alias substitution when the alias is expanded during command parsing. `alias` returns true unless a \<name\> is given (without a corresponding =\<value\>) for which no alias has been defined. Aliases are described in [Aliases](#Aliases).

`bind`  

bind

    bind [-m keymap] [-lsvSVX]
    bind [-m keymap] [-q function] [-u function] [-r keyseq]
    bind [-m keymap] -f filename
    bind [-m keymap] -x keyseq[: ]shell-command
    bind [-m keymap] keyseq:function-name
    bind [-m keymap] keyseq:readline-command
    bind [-m keymap] -p|-P [readline-command]
    bind readline-command-line

Display current Readline (see [Command Line Editing](#Command-Line-Editing)) key and function bindings, bind a key sequence to a Readline function or macro or to a shell command, or set a Readline variable. Each non-option argument is a key binding or command as it would appear in a Readline initialization file (see [Readline Init File](#Readline-Init-File)), but each binding or command must be passed as a separate argument; e.g., ‘`"\C-x\C-r":re-read-init-file`’.

In the following descriptions, options that display output in a form available to be re-read format their output as commands that would appear in a Readline initialization file or that would be supplied as individual arguments to a `bind` command.

Options, if supplied, have the following meanings:

`-m keymap`  
Use \<keymap\> as the keymap to be affected by the subsequent bindings. Acceptable \<keymap\> names are `emacs`, `emacs-standard`, `emacs-meta`, `emacs-ctlx`, `vi`, `vi-move`, `vi-command`, and `vi-insert`. `vi` is equivalent to `vi-command` (`vi-move` is also a synonym); `emacs` is equivalent to `emacs-standard`.

`-l`  
List the names of all Readline functions.

`-p`  
Display Readline function names and bindings in such a way that they can be used as an argument to a subsequent `bind` command or in a Readline initialization file. If arguments remain after option processing, `bind` treats them as readline command names and restricts output to those names.

`-P`  
List current Readline function names and bindings. If arguments remain after option processing, `bind` treats them as readline command names and restricts output to those names.

`-s`  
Display Readline key sequences bound to macros and the strings they output in such a way that they can be used as an argument to a subsequent `bind` command or in a Readline initialization file.

`-S`  
Display Readline key sequences bound to macros and the strings they output.

`-v`  
Display Readline variable names and values in such a way that they can be used as an argument to a subsequent `bind` command or in a Readline initialization file.

`-V`  
List current Readline variable names and values.

`-f filename`  
Read key bindings from \<filename\>.

`-q function`  
Display key sequences that invoke the named Readline \<function\>.

`-u function`  
Unbind all key sequences bound to the named Readline \<function\>.

`-r keyseq`  
Remove any current binding for \<keyseq\>.

`-x keyseq:shell-command`  
Cause \<shell-command\> to be executed whenever \<keyseq\> is entered. The separator between \<keyseq\> and \<shell-command\> is either whitespace or a colon optionally followed by whitespace. If the separator is whitespace, \<shell-command\> must be enclosed in double quotes and Readline expands any of its special backslash-escapes in \<shell-command\> before saving it. If the separator is a colon, any enclosing double quotes are optional, and Readline does not expand the command string before saving it. Since the entire key binding expression must be a single argument, it should be enclosed in single quotes. When \<shell-command\> is executed, the shell sets the `READLINE_LINE` variable to the contents of the Readline line buffer and the `READLINE_POINT` and `READLINE_MARK` variables to the current location of the insertion point and the saved insertion point (the \<mark\>), respectively. The shell assigns any numeric argument the user supplied to the `READLINE_ARGUMENT` variable. If there was no argument, that variable is not set. If the executed command changes the value of any of `READLINE_LINE`, `READLINE_POINT`, or `READLINE_MARK`, those new values will be reflected in the editing state.

`-X`  
List all key sequences bound to shell commands and the associated commands in a format that can be reused as an argument to a subsequent `bind` command.

The return status is zero unless an invalid option is supplied or an error occurs.

`builtin`  

builtin

    builtin [shell-builtin [args]]

Execute the specified shell builtin \<shell-builtin\>, passing it \<args\>, and return its exit status. This is useful when defining a shell function with the same name as a shell builtin, retaining the functionality of the builtin within the function. The return status is non-zero if \<shell-builtin\> is not a shell builtin command.

`caller`  

caller

    caller [expr]

Returns the context of any active subroutine call (a shell function or a script executed with the `.` or `source` builtins).

Without \<expr\>, `caller` displays the line number and source filename of the current subroutine call. If a non-negative integer is supplied as \<expr\>, `caller` displays the line number, subroutine name, and source file corresponding to that position in the current execution call stack. This extra information may be used, for example, to print a stack trace. The current frame is frame 0.

The return value is 0 unless the shell is not executing a subroutine call or \<expr\> does not correspond to a valid position in the call stack.

`command`  

command

    command [-pVv] command [arguments …]

The `command` builtin runs \<command\> with \<arguments\> ignoring any shell function named \<command\>. Only shell builtin commands or commands found by searching the `PATH` are executed. If there is a shell function named `ls`, running ‘`command ls`’ within the function will execute the external command `ls` instead of calling the function recursively. The `-p` option means to use a default value for `PATH` that is guaranteed to find all of the standard utilities. The return status in this case is 127 if \<command\> cannot be found or an error occurred, and the exit status of \<command\> otherwise.

If either the `-V` or `-v` option is supplied, `command` prints a description of \<command\>. The `-v` option displays a single word indicating the command or file name used to invoke \<command\>; the `-V` option produces a more verbose description. In this case, the return status is zero if \<command\> is found, and non-zero if not.

`declare`  

declare

    declare [-aAfFgiIlnrtux] [-p] [name[=value] …]

Declare variables and give them attributes. If no \<name\>s are given, then display the values of variables or shell functions instead.

The `-p` option will display the attributes and values of each \<name\>. When `-p` is used with \<name\> arguments, additional options, other than `-f` and `-F`, are ignored.

When `-p` is supplied without \<name\> arguments, `declare` will display the attributes and values of all variables having the attributes specified by the additional options. If no other options are supplied with `-p`, `declare` will display the attributes and values of all shell variables. The `-f` option restricts the display to shell functions.

The `-F` option inhibits the display of function definitions; only the function name and attributes are printed. If the `extdebug` shell option is enabled using `shopt` (see [The Shopt Builtin](#The-Shopt-Builtin)), the source file name and line number where each \<name\> is defined are displayed as well. `-F` implies `-f`.

The `-g` option forces variables to be created or modified at the global scope, even when `declare` is executed in a shell function. It is ignored in when `declare` is not executed in a shell function.

The `-I` option causes local variables to inherit the attributes (except the `nameref` attribute) and value of any existing variable with the same \<name\> at a surrounding scope. If there is no existing variable, the local variable is initially unset.

The following options can be used to restrict output to variables with the specified attributes or to give variables attributes:

`-a`  
Each \<name\> is an indexed array variable (see [Arrays](#Arrays)).

`-A`  
Each \<name\> is an associative array variable (see [Arrays](#Arrays)).

`-f`  
Each \<name\> refers to a shell function.

`-i`  
The variable is to be treated as an integer; arithmetic evaluation (see [Shell Arithmetic](#Shell-Arithmetic)) is performed when the variable is assigned a value.

`-l`  
When the variable is assigned a value, all upper-case characters are converted to lower-case. The upper-case attribute is disabled.

`-n`  
Give each \<name\> the `nameref` attribute, making it a name reference to another variable. That other variable is defined by the value of \<name\>. All references, assignments, and attribute modifications to \<name\>, except for those using or changing the `-n` attribute itself, are performed on the variable referenced by \<name\>’s value. The nameref attribute cannot be applied to array variables.

`-r`  
Make \<name\>s readonly. These names cannot then be assigned values by subsequent assignment statements or unset.

`-t`  
Give each \<name\> the `trace` attribute. Traced functions inherit the `DEBUG` and `RETURN` traps from the calling shell. The trace attribute has no special meaning for variables.

`-u`  
When the variable is assigned a value, all lower-case characters are converted to upper-case. The lower-case attribute is disabled.

`-x`  
Mark each \<name\> for export to subsequent commands via the environment.

Using ‘`+`’ instead of ‘`-`’ turns off the specified attribute instead, with the exceptions that ‘`+a`’ and ‘`+A`’ may not be used to destroy array variables and ‘`+r`’ will not remove the readonly attribute.

When used in a function, `declare` makes each \<name\> local, as with the `local` command, unless the `-g` option is supplied. If a variable name is followed by =\<value\>, the value of the variable is set to \<value\>.

When using `-a` or `-A` and the compound assignment syntax to create array variables, additional attributes do not take effect until subsequent assignments.

The return status is zero unless an invalid option is encountered, an attempt is made to define a function using ‘`-f foo=bar`’, an attempt is made to assign a value to a readonly variable, an attempt is made to assign a value to an array variable without using the compound assignment syntax (see [Arrays](#Arrays)), one of the \<name\>s is not a valid shell variable name, an attempt is made to turn off readonly status for a readonly variable, an attempt is made to turn off array status for an array variable, or an attempt is made to display a non-existent function with `-f`.

`echo`  

echo

    echo [-neE] [arg …]

Output the \<arg\>s, separated by spaces, terminated with a newline. The return status is 0 unless a write error occurs. If `-n` is specified, the trailing newline is not printed.

If the `-e` option is given, `echo` interprets the following backslash-escaped characters. The `-E` option disables interpretation of these escape characters, even on systems where they are interpreted by default. The `xpg_echo` shell option determines whether or not `echo` interprets any options and expands these escape characters. `echo` does not interpret `--` to mean the end of options.

`echo` interprets the following escape sequences:

`\a`  
alert (bell)

`\b`  
backspace

`\c`  
suppress further output

`\e`; `\E`  
escape

`\f`  
form feed

`\n`  
new line

`\r`  
carriage return

`\t`  
horizontal tab

`\v`  
vertical tab

`\\`  
backslash

`\0nnn`  
The eight-bit character whose value is the octal value \<nnn\> (zero to three octal digits).

`\xHH`  
The eight-bit character whose value is the hexadecimal value \<HH\> (one or two hex digits).

`\uHHHH`  
The Unicode (ISO/IEC 10646) character whose value is the hexadecimal value \<HHHH\> (one to four hex digits).

`\UHHHHHHHH`  
The Unicode (ISO/IEC 10646) character whose value is the hexadecimal value \<HHHHHHHH\> (one to eight hex digits).

`echo` writes any unrecognized backslash-escaped characters unchanged.

`enable`  

enable

    enable [-a] [-dnps] [-f filename] [name …]

Enable and disable builtin shell commands. Disabling a builtin allows an executable file which has the same name as a shell builtin to be executed without specifying a full pathname, even though the shell normally searches for builtins before files.

If `-n` is supplied, the \<name\>s are disabled. Otherwise \<name\>s are enabled. For example, to use the `test` binary found using `$PATH` instead of the shell builtin version, type ‘`enable -n test`’.

If the `-p` option is supplied, or no \<name\> arguments are supplied, print a list of shell builtins. With no other arguments, the list consists of all enabled shell builtins. The `-n` option means to print only disabled builtins. The `-a` option means to list each builtin with an indication of whether or not it is enabled. The `-s` option means to restrict `enable` to the POSIX special builtins.

The `-f` option means to load the new builtin command \<name\> from shared object \<filename\>, on systems that support dynamic loading. If \<filename\> does not contain a slash. Bash will use the value of the `BASH_LOADABLES_PATH` variable as a colon-separated list of directories in which to search for \<filename\>. The default for `BASH_LOADABLES_PATH` is system-dependent, and may include "." to force a search of the current directory. The `-d` option will delete a builtin loaded with `-f`. If `-s` is used with `-f`, the new builtin becomes a POSIX special builtin (see [Special Builtins](#Special-Builtins)).

If no options are supplied and a \<name\> is not a shell builtin, `enable` will attempt to load \<name\> from a shared object named \<name\>, as if the command were ‘`enable -f name name`’.

The return status is zero unless a \<name\> is not a shell builtin or there is an error loading a new builtin from a shared object.

`help`  

help

    help [-dms] [pattern]

Display helpful information about builtin commands. If \<pattern\> is specified, `help` gives detailed help on all commands matching \<pattern\> as described below; otherwise it displays a list of all builtins and shell compound commands.

Options, if supplied, have the following meanings:

`-d`  
Display a short description of each \<pattern\>

`-m`  
Display the description of each \<pattern\> in a manpage-like format

`-s`  
Display only a short usage synopsis for each \<pattern\>

If \<pattern\> contains pattern matching characters (see [Pattern Matching](#Pattern-Matching)) it’s treated as a shell pattern and `help` prints the description of each help topic matching \<pattern\>.

If not, and \<pattern\> exactly matches the name of a help topic, `help` prints the description associated with that topic. Otherwise, `help` performs prefix matching and prints the descriptions of all matching help topics.

The return status is zero unless no command matches \<pattern\>.

`let`  

let

    let expression [expression …]

The `let` builtin allows arithmetic to be performed on shell variables. Each \<expression\> is evaluated as an arithmetic expression according to the rules given below in [Shell Arithmetic](#Shell-Arithmetic). If the last \<expression\> evaluates to 0, `let` returns 1; otherwise `let` returns 0.

`local`  

local

    local [option] name[=value] …

For each argument, create a local variable named \<name\>, and assign it \<value\>. The \<option\> can be any of the options accepted by `declare`. `local` can only be used within a function; it makes the variable \<name\> have a visible scope restricted to that function and its children. It is an error to use `local` when not within a function.

If \<name\> is ‘`-`’, it makes the set of shell options local to the function in which `local` is invoked: any shell options changed using the `set` builtin inside the function after the call to `local` are restored to their original values when the function returns. The restore is performed as if a series of `set` commands were executed to restore the values that were in place before the function.

With no operands, `local` writes a list of local variables to the standard output.

The return status is zero unless `local` is used outside a function, an invalid \<name\> is supplied, or \<name\> is a readonly variable.

`logout`  

logout

    logout [n]

Exit a login shell, returning a status of \<n\> to the shell’s parent.

`mapfile`  

mapfile

    mapfile [-d delim] [-n count] [-O origin] [-s count]
        [-t] [-u fd] [-C callback] [-c quantum] [array]

Read lines from the standard input, or from file descriptor \<fd\> if the `-u` option is supplied, into the indexed array variable \<array\>. The variable `MAPFILE` is the default \<array\>. Options, if supplied, have the following meanings:

`-d`  
Use the first character of \<delim\> to terminate each input line, rather than newline. If \<delim\> is the empty string, `mapfile` will terminate a line when it reads a NUL character.

`-n`  
Copy at most \<count\> lines. If \<count\> is 0, copy all lines.

`-O`  
Begin assigning to \<array\> at index \<origin\>. The default index is 0.

`-s`  
Discard the first \<count\> lines read.

`-t`  
Remove a trailing \<delim\> (default newline) from each line read.

`-u`  
Read lines from file descriptor \<fd\> instead of the standard input.

`-C`  
Evaluate \<callback\> each time \<quantum\> lines are read. The `-c` option specifies \<quantum\>.

`-c`  
Specify the number of lines read between each call to \<callback\>.

If `-C` is specified without `-c`, the default quantum is 5000. When \<callback\> is evaluated, it is supplied the index of the next array element to be assigned and the line to be assigned to that element as additional arguments. \<callback\> is evaluated after the line is read but before the array element is assigned.

If not supplied with an explicit origin, `mapfile` will clear \<array\> before assigning to it.

`mapfile` returns zero unless an invalid option or option argument is supplied, \<array\> is invalid or unassignable, or if \<array\> is not an indexed array.

`printf`  

printf

    printf [-v var] format [arguments]

Write the formatted \<arguments\> to the standard output under the control of the \<format\>. The `-v` option assigns the output to the variable \<var\> rather than printing it to the standard output.

The \<format\> is a character string which contains three types of objects: plain characters, which are simply copied to standard output, character escape sequences, which are converted and copied to the standard output, and format specifications, each of which causes printing of the next successive \<argument\>. In addition to the standard `printf(3)` format characters `cCsSndiouxXeEfFgGaA`, `printf` interprets the following additional format specifiers:

`%b`  
Causes `printf` to expand backslash escape sequences in the corresponding \<argument\> in the same way as `echo -e` (see [Bash Builtins](#Bash-Builtins)).

`%q`  
Causes `printf` to output the corresponding \<argument\> in a format that can be reused as shell input. `%q` and `%Q`P use the ANSI-C quoting style (see [ANSI-C Quoting](#ANSI_002dC-Quoting)) if any characters in the argument string require it, and backslash quoting otherwise. If the format string uses the `printf` *alternate form*, these two formats quote the argument string using single quotes.

`%Q`  
like `%q`, but applies any supplied precision to the \<argument\> before quoting it.

`%(datefmt)T`  
Causes `printf` to output the date-time string resulting from using \<datefmt\> as a format string for `strftime`(3). The corresponding \<argument\> is an integer representing the number of seconds since the epoch. This format specifier recognizes Two special argument values: -1 represents the current time, and -2 represents the time the shell was invoked. If no argument is specified, conversion behaves as if -1 had been supplied. This is an exception to the usual `printf` behavior.

The %b, %q, and %T format specifiers all use the field width and precision arguments from the format specification and write that many bytes from (or use that wide a field for) the expanded argument, which usually contains more characters than the original.

The %n format specifier accepts a corresponding argument that is treated as a shell variable name.

The %s and %c format specifiers accept an l (long) modifier, which forces them to convert the argument string to a wide-character string and apply any supplied field width and precision in terms of characters, not bytes. The %S and %C format specifiers are equivalent to %ls and %lc, respectively.

Arguments to non-string format specifiers are treated as C language constants, except that a leading plus or minus sign is allowed, and if the leading character is a single or double quote, the value is the numeric value of the following character, using the current locale.

The \<format\> is reused as necessary to consume all of the \<arguments\>. If the \<format\> requires more \<arguments\> than are supplied, the extra format specifications behave as if a zero value or null string, as appropriate, had been supplied. The return value is zero on success, non-zero if an invalid option is supplied or a write or assignment error occurs.

`read`  

read

    read [-Eers] [-a aname] [-d delim] [-i text] [-n nchars]
        [-N nchars] [-p prompt] [-t timeout] [-u fd] [name …]

Read one line from the standard input, or from the file descriptor \<fd\> supplied as an argument to the `-u` option, split it into words as described above in [Word Splitting](#Word-Splitting), and assign the first word to the first \<name\>, the second word to the second \<name\>, and so on. If there are more words than names, the remaining words and their intervening delimiters are assigned to the last \<name\>. If there are fewer words read from the input stream than names, the remaining names are assigned empty values. The characters in the value of the `IFS` variable are used to split the line into words using the same rules the shell uses for expansion (described above in [Word Splitting](#Word-Splitting)). The backslash character ‘`\`’ removes any special meaning for the next character read and is used for line continuation.

Options, if supplied, have the following meanings:

`-a aname`  
The words are assigned to sequential indices of the array variable \<aname\>, starting at 0. All elements are removed from \<aname\> before the assignment. Other \<name\> arguments are ignored.

`-d delim`  
The first character of \<delim\> terminates the input line, rather than newline. If \<delim\> is the empty string, `read` will terminate a line when it reads a NUL character.

`-e`  
If the standard input is coming from a terminal, `read` uses Readline (see [Command Line Editing](#Command-Line-Editing)) to obtain the line. Readline uses the current (or default, if line editing was not previously active) editing settings, but uses Readline’s default filename completion.

`-E`  
If the standard input is coming from a terminal, `read` uses Readline (see [Command Line Editing](#Command-Line-Editing)) to obtain the line. Readline uses the current (or default, if line editing was not previously active) editing settings, but uses Bash’s default completion, including programmable completion.

`-i text`  
If Readline is being used to read the line, `read` places \<text\> into the editing buffer before editing begins.

`-n nchars`  
`read` returns after reading \<nchars\> characters rather than waiting for a complete line of input, unless it encounters EOF or `read` times out, but honors a delimiter if it reads fewer than \<nchars\> characters before the delimiter.

`-N nchars`  
`read` returns after reading exactly \<nchars\> characters rather than waiting for a complete line of input, unless it encounters EOF or `read` times out. Delimiter characters in the input are not treated specially and do not cause `read` to return until it has read \<nchars\> characters. The result is not split on the characters in `IFS`; the intent is that the variable is assigned exactly the characters read (with the exception of backslash; see the `-r` option below).

`-p prompt`  
Display \<prompt\>, without a trailing newline, before attempting to read any input, but only if input is coming from a terminal.

`-r`  
If this option is given, backslash does not act as an escape character. The backslash is considered to be part of the line. In particular, a backslash-newline pair may not then be used as a line continuation.

`-s`  
Silent mode. If input is coming from a terminal, characters are not echoed.

`-t timeout`  
Cause `read` to time out and return failure if it does not read a complete line of input (or a specified number of characters) within \<timeout\> seconds. \<timeout\> may be a decimal number with a fractional portion following the decimal point. This option is only effective if `read` is reading input from a terminal, pipe, or other special file; it has no effect when reading from regular files. If `read` times out, it saves any partial input read into the specified variable \<name\>, and returns a status greater than 128. If \<timeout\> is 0, `read` returns immediately, without trying to read any data. In this case, the exit status is 0 if input is available on the specified file descriptor, or the read will return EOF, non-zero otherwise.

`-u fd`  
Read input from file descriptor \<fd\> instead of the standard input.

Other than the case where \<delim\> is the empty string, `read` ignores any NUL characters in the input.

If no \<name\>s are supplied, `read` assigns the line read, without the ending delimiter but otherwise unmodified, to the variable `REPLY`.

The exit status is zero, unless end-of-file is encountered, `read` times out (in which case the status is greater than 128), a variable assignment error (such as assigning to a readonly variable) occurs, or an invalid file descriptor is supplied as the argument to `-u`.

`readarray`  

readarray

    readarray [-d delim] [-n count] [-O origin] [-s count]
        [-t] [-u fd] [-C callback] [-c quantum] [array]

Read lines from the standard input into the indexed array variable \<array\>, or from file descriptor \<fd\> if the `-u` option is supplied.

A synonym for `mapfile`.

`source`  

source

    source [-p path] filename [arguments]

A synonym for `.` (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)).

`type`  

type

    type [-afptP] [name …]

Indicate how each \<name\> would be interpreted if used as a command name.

If the `-t` option is used, `type` prints a single word which is one of ‘`alias`’, ‘`keyword`’, ‘`function`’, ‘`builtin`’, or ‘`file`’, if \<name\> is an alias, shell reserved word, shell function, shell builtin, or executable file, respectively. If the \<name\> is not found, `type` prints nothing and returns a failure status.

If the `-p` option is used, `type` either returns the name of the executable file that would be found by searching `$PATH` for `name`, or nothing if `-t` would not return ‘`file`’.

The `-P` option forces a path search for each \<name\>, even if `-t` would not return ‘`file`’.

If a \<name\> is present in the table of hashed commands, options `-p` and `-P` print the hashed value, which is not necessarily the file that appears first in `$PATH`.

If the `-a` option is used, `type` returns all of the places that contain a command named \<name\>. This includes aliases, reserved words, functions, and builtins, but the path search options (`-p` and `-P`) can be supplied to restrict the output to executable files. If `-a` is supplied with `-p`, `type` does not look in the table of hashed commands, and only performs a `PATH` search for \<name\>.

If the `-f` option is used, `type` does not attempt to find shell functions, as with the `command` builtin.

The return status is zero if all of the \<name\>s are found, non-zero if any are not found.

`typeset`  

typeset

    typeset [-afFgrxilnrtux] [-p] [name[=value] …]

The `typeset` command is supplied for compatibility with the Korn shell. It is a synonym for the `declare` builtin command.

`ulimit`  

ulimit

    ulimit [-HS] -a
    ulimit [-HS] [-bcdefiklmnpqrstuvxPRT] [limit]

`ulimit` provides control over the resources available to the shell and to processes it starts, on systems that allow such control. If an option is given, it is interpreted as follows:

`-S`  
Change and report the soft limit associated with a resource.

`-H`  
Change and report the hard limit associated with a resource.

`-a`  
Report all current limits; no limits are set.

`-b`  
The maximum socket buffer size.

`-c`  
The maximum size of core files created.

`-d`  
The maximum size of a process’s data segment.

`-e`  
The maximum scheduling priority ("nice").

`-f`  
The maximum size of files written by the shell and its children.

`-i`  
The maximum number of pending signals.

`-k`  
The maximum number of kqueues that may be allocated.

`-l`  
The maximum size that may be locked into memory.

`-m`  
The maximum resident set size (many systems do not honor this limit).

`-n`  
The maximum number of open file descriptors (most systems do not allow this value to be set).

`-p`  
The pipe buffer size.

`-q`  
The maximum number of bytes in POSIX message queues.

`-r`  
The maximum real-time scheduling priority.

`-s`  
The maximum stack size.

`-t`  
The maximum amount of cpu time in seconds.

`-u`  
The maximum number of processes available to a single user.

`-v`  
The maximum amount of virtual memory available to the shell, and, on some systems, to its children.

`-x`  
The maximum number of file locks.

`-P`  
The maximum number of pseudoterminals.

`-R`  
The maximum time a real-time process can run before blocking, in microseconds.

`-T`  
The maximum number of threads.

If \<limit\> is supplied, and the `-a` option is not used, \<limit\> is the new value of the specified resource. The special \<limit\> values `hard`, `soft`, and `unlimited` stand for the current hard limit, the current soft limit, and no limit, respectively. A hard limit cannot be increased by a non-root user once it is set; a soft limit may be increased up to the value of the hard limit. Otherwise, `ulimit` prints the current value of the soft limit for the specified resource, unless the `-H` option is supplied. When more than one resource is specified, the limit name and unit, if appropriate, are printed before the value. When setting new limits, if neither `-H` nor `-S` is supplied, `ulimit` sets both the hard and soft limits. If no option is supplied, then `-f` is assumed.

Values are in 1024-byte increments, except for `-t`, which is in seconds; `-R`, which is in microseconds; `-p`, which is in units of 512-byte blocks; `-P`, `-T`, `-b`, `-k`, `-n` and `-u`, which are unscaled values; and, when in POSIX mode (see [Bash POSIX Mode](#Bash-POSIX-Mode)), `-c` and `-f`, which are in 512-byte increments.

The return status is zero unless an invalid option or argument is supplied, or an error occurs while setting a new limit.

`unalias`  

unalias

    unalias [-a] [name … ]

Remove each \<name\> from the list of aliases. If `-a` is supplied, remove all aliases. The return value is true unless a supplied \<name\> is not a defined alias. Aliases are described in [Aliases](#Aliases).
