---
title: Invoking Bash
source_url: https://www.gnu.org/software/bash/manual
source_path: 023-invoking-bash.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 230
---

## Invoking Bash

    bash [long-opt] [-ir] [-abefhkmnptuvxdBCDHP] [-o option]
        [-O shopt_option] [argument …]
    bash [long-opt] [-abefhkmnptuvxdBCDHP] [-o option]
        [-O shopt_option] -c string [argument …]
    bash [long-opt] -s [-abefhkmnptuvxdBCDHP] [-o option]
        [-O shopt_option] [argument …]

All of the single-character options used with the `set` builtin (see [The Set Builtin](#The-Set-Builtin)) can be used as options when the shell is invoked. In addition, there are several multi-character options that you can use. These options must appear on the command line before the single-character options to be recognized.

`--debugger`  
Arrange for the debugger profile to be executed before the shell starts. Turns on extended debugging mode (see [The Shopt Builtin](#The-Shopt-Builtin) for a description of the `extdebug` option to the `shopt` builtin).

`--dump-po-strings`  
Print a list of all double-quoted strings preceded by ‘`$`’ on the standard output in the GNU `gettext` PO (portable object) file format. Equivalent to `-D` except for the output format.

`--dump-strings`  
Equivalent to `-D`.

`--help`  
Display a usage message on standard output and exit successfully.

`--init-file filename`; `--rcfile filename`  
Execute commands from \<filename\> (instead of `~/.bashrc`) in an interactive shell.

`--login`  
Equivalent to `-l`.

`--noediting`  
Do not use the GNU Readline library (see [Command Line Editing](#Command-Line-Editing)) to read command lines when the shell is interactive.

`--noprofile`  
Don’t load the system-wide startup file `/etc/profile` or any of the personal initialization files `~/.bash_profile`, `~/.bash_login`, or `~/.profile` when Bash is invoked as a login shell.

`--norc`  
Don’t read the `~/.bashrc` initialization file in an interactive shell. This is on by default if the shell is invoked as `sh`.

`--posix`  
Enable POSIX mode; change the behavior of Bash where the default operation differs from the POSIX standard to match the standard. This is intended to make Bash behave as a strict superset of that standard. See [Bash POSIX Mode](#Bash-POSIX-Mode), for a description of the Bash POSIX mode.

`--restricted`  
Equivalent to `-r`. Make the shell a restricted shell (see [The Restricted Shell](#The-Restricted-Shell)).

`--verbose`  
Equivalent to `-v`. Print shell input lines as they’re read.

`--version`  
Show version information for this instance of Bash on the standard output and exit successfully.

There are several single-character options that may be supplied at invocation which are not available with the `set` builtin.

`-c`  
Read and execute commands from the first non-option argument \<command_string\>, then exit. If there are arguments after the \<command_string\>, the first argument is assigned to `$0` and any remaining arguments are assigned to the positional parameters. The assignment to `$0` sets the name of the shell, which is used in warning and error messages.

`-i`  
Force the shell to run interactively. Interactive shells are described in [Interactive Shells](#Interactive-Shells).

`-l`  
Make this shell act as if it had been directly invoked by login. When the shell is interactive, this is equivalent to starting a login shell with ‘`exec -l bash`’. When the shell is not interactive, it will read and execute the login shell startup files. ‘`exec bash -l`’ or ‘`exec bash --login`’ will replace the current shell with a Bash login shell. See [Bash Startup Files](#Bash-Startup-Files), for a description of the special behavior of a login shell.

`-r`  
Make the shell a restricted shell (see [The Restricted Shell](#The-Restricted-Shell)).

`-s`  
If this option is present, or if no arguments remain after option processing, then Bash reads commands from the standard input. This option allows the positional parameters to be set when invoking an interactive shell or when reading input through a pipe.

`-D`  
Print a list of all double-quoted strings preceded by ‘`$`’ on the standard output. These are the strings that are subject to language translation when the current locale is not `C` or `POSIX` (see [Locale Translation](#Locale-Translation)). This implies the `-n` option; no commands will be executed.

`[-+]O [shopt_option]`  
\<shopt_option\> is one of the shell options accepted by the `shopt` builtin (see [The Shopt Builtin](#The-Shopt-Builtin)). If \<shopt_option\> is present, `-O` sets the value of that option; `+O` unsets it. If \<shopt_option\> is not supplied, Bash prints the names and values of the shell options accepted by `shopt` on the standard output. If the invocation option is `+O`, the output is displayed in a format that may be reused as input.

`--`  
A `--` signals the end of options and disables further option processing. Any arguments after the `--` are treated as a shell script filename (see [Shell Scripts](#Shell-Scripts)) and arguments passed to that script.

`-`  
Equivalent to `--`.

login shell

A login shell is one whose first character of argument zero is ‘`-`’, or one invoked with the `--login` option.

interactive shell

An interactive shell is one started without non-option arguments, unless `-s` is specified, without specifying the `-c` option, and whose standard input and standard error are both connected to terminals (as determined by *isatty(3)*), or one started with the `-i` option. See [Interactive Shells](#Interactive-Shells), for more information.

If arguments remain after option processing, and neither the `-c` nor the `-s` option has been supplied, the first argument is treated as the name of a file containing shell commands (see [Shell Scripts](#Shell-Scripts)). When Bash is invoked in this fashion, `$0` is set to the name of the file, and the positional parameters are set to the remaining arguments. Bash reads and executes commands from this file, then exits. Bash’s exit status is the exit status of the last command executed in the script. If no commands are executed, the exit status is 0. Bash first attempts to open the file in the current directory, and, if no file is found, searches the directories in `PATH` for the script.
