---
title: Executing Commands
source_url: https://www.gnu.org/software/bash/manual
source_path: 012-executing-commands.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 120
---

## Executing Commands

### Simple Command Expansion

command expansion

When the shell executes a simple command, it performs the following expansions, assignments, and redirections, from left to right, in the following order.

1.  The words that the parser has marked as variable assignments (those preceding the command name) and redirections are saved for later processing.

2.  The words that are not variable assignments or redirections are expanded (see [Shell Expansions](#Shell-Expansions)). If any words remain after expansion, the first word is taken to be the name of the command and the remaining words are the arguments.

3.  Redirections are performed as described above (see [Redirections](#Redirections)).

4.  The text after the ‘`=`’ in each variable assignment undergoes tilde expansion, parameter expansion, command substitution, arithmetic expansion, and quote removal before being assigned to the variable.

If no command name results, the variable assignments affect the current shell environment. In the case of such a command (one that consists only of assignment statements and redirections), assignment statements are performed before redirections. Otherwise, the variables are added to the environment of the executed command and do not affect the current shell environment. If any of the assignments attempts to assign a value to a readonly variable, an error occurs, and the command exits with a non-zero status.

If no command name results, redirections are performed, but do not affect the current shell environment. A redirection error causes the command to exit with a non-zero status.

If there is a command name left after expansion, execution proceeds as described below. Otherwise, the command exits. If one of the expansions contained a command substitution, the exit status of the command is the exit status of the last command substitution performed. If there were no command substitutions, the command exits with a zero status.

### Command Search and Execution

command execution

command search

After a command has been split into words, if it results in a simple command and an optional list of arguments, the shell performs the following actions.

1.  If the command name contains no slashes, the shell attempts to locate it. If there exists a shell function by that name, that function is invoked as described in [Shell Functions](#Shell-Functions).

2.  If the name does not match a function, the shell searches for it in the list of shell builtins. If a match is found, that builtin is invoked.

3.  If the name is neither a shell function nor a builtin, and contains no slashes, Bash searches each element of `$PATH` for a directory containing an executable file by that name. Bash uses a hash table to remember the full pathnames of executable files to avoid multiple `PATH` searches (see the description of `hash` in [Bourne Shell Builtins](#Bourne-Shell-Builtins)). Bash performs a full search of the directories in `$PATH` only if the command is not found in the hash table. If the search is unsuccessful, the shell searches for a defined shell function named `command_not_found_handle`. If that function exists, it is invoked in a separate execution environment with the original command and the original command’s arguments as its arguments, and the function’s exit status becomes the exit status of that subshell. If that function is not defined, the shell prints an error message and returns an exit status of 127.

4.  If the search is successful, or if the command name contains one or more slashes, the shell executes the named program in a separate execution environment. Argument 0 is set to the name given, and the remaining arguments to the command are set to the arguments supplied, if any.

5.  If this execution fails because the file is not in executable format, and the file is not a directory, it is assumed to be a shell script, a file containing shell commands, and the shell executes it as described in [Shell Scripts](#Shell-Scripts).

6.  If the command was not begun asynchronously, the shell waits for the command to complete and collects its exit status.

### Command Execution Environment

execution environment

The shell has an execution environment, which consists of the following:

- Open files inherited by the shell at invocation, as modified by redirections supplied to the `exec` builtin.

- The current working directory as set by `cd`, `pushd`, or `popd`, or inherited by the shell at invocation.

- The file creation mode mask as set by `umask` or inherited from the shell’s parent.

- Current traps set by `trap`.

- Shell parameters that are set by variable assignment or with `set` or inherited from the shell’s parent in the environment.

- Shell functions defined during execution or inherited from the shell’s parent in the environment.

- Options enabled at invocation (either by default or with command-line arguments) or by `set`.

- Options enabled by `shopt` (see [The Shopt Builtin](#The-Shopt-Builtin)).

- Shell aliases defined with `alias` (see [Aliases](#Aliases)).

- Various process IDs, including those of background jobs (see [Lists](#Lists)), the value of `$$`, and the value of `$PPID`.

When a simple command other than a builtin or shell function is to be executed, it is invoked in a separate execution environment that consists of the following. Unless otherwise noted, the values are inherited from the shell.

- The shell’s open files, plus any modifications and additions specified by redirections to the command.

- The current working directory.

- The file creation mode mask.

- Shell variables and functions marked for export, along with variables exported for the command, passed in the environment (see [Environment](#Environment)).

- Traps caught by the shell are reset to the values inherited from the shell’s parent, and traps ignored by the shell are ignored.

A command invoked in this separate environment cannot affect the shell’s execution environment.

A subshell is a copy of the shell process.

Command substitution, commands grouped with parentheses, and asynchronous commands are invoked in a subshell environment that is a duplicate of the shell environment, except that traps caught by the shell are reset to the values that the shell inherited from its parent at invocation. Builtin commands that are invoked as part of a pipeline, except possibly in the last element depending on the value of the `lastpipe` shell option (see [The Shopt Builtin](#The-Shopt-Builtin)), are also executed in a subshell environment. Changes made to the subshell environment cannot affect the shell’s execution environment.

When the shell is in POSIX mode, subshells spawned to execute command substitutions inherit the value of the `-e` option from the parent shell. When not in POSIX mode, Bash clears the `-e` option in such subshells See the description of the `inherit_errexit` shell option (see [Bash Builtins](#Bash-Builtins)) for how to control this behavior when not in POSIX mode.

If a command is followed by a ‘`&`’ and job control is not active, the default standard input for the command is the empty file `/dev/null`. Otherwise, the invoked command inherits the file descriptors of the calling shell as modified by redirections.

### Environment

environment

When a program is invoked it is given an array of strings called the environment. This is a list of name-value pairs, of the form `name=value`.

Bash provides several ways to manipulate the environment. On invocation, the shell scans its own environment and creates a parameter for each name found, automatically marking it for `export` to child processes. Executed commands inherit the environment. The `export`, ‘`declare -x`’, and `unset` commands modify the environment by adding and deleting parameters and functions. If the value of a parameter in the environment is modified, the new value automatically becomes part of the environment, replacing the old. The environment inherited by any executed command consists of the shell’s initial environment, whose values may be modified in the shell, less any pairs removed by the `unset` and ‘`export -n`’ commands, plus any additions via the `export` and ‘`declare -x`’ commands.

If any parameter assignment statements, as described in [Shell Parameters](#Shell-Parameters), appear before a simple command, the variable assignments are part of that command’s environment for as long as it executes. These assignment statements affect only the environment seen by that command. If these assignments precede a call to a shell function, the variables are local to the function and exported to that function’s children.

If the `-k` option is set (see [The Set Builtin](#The-Set-Builtin)), then all parameter assignments are placed in the environment for a command, not just those that precede the command name.

When Bash invokes an external command, the variable ‘`$_`’ is set to the full pathname of the command and passed to that command in its environment.

### Exit Status

exit status

The exit status of an executed command is the value returned by the `waitpid` system call or equivalent function. Exit statuses fall between 0 and 255, though, as explained below, the shell may use values above 125 specially. Exit statuses from shell builtins and compound commands are also limited to this range. Under certain circumstances, the shell will use special values to indicate specific failure modes.

For the shell’s purposes, a command which exits with a zero exit status has succeeded. So while an exit status of zero indicates success, a non-zero exit status indicates failure. This seemingly counter-intuitive scheme is used so there is one well-defined way to indicate success and a variety of ways to indicate various failure modes.

When a command terminates on a fatal signal whose number is \<N\>, Bash uses the value 128+\<N\> as the exit status.

If a command is not found, the child process created to execute it returns a status of 127. If a command is found but is not executable, the return status is 126.

If a command fails because of an error during expansion or redirection, the exit status is greater than zero.

The exit status is used by the Bash conditional commands (see [Conditional Constructs](#Conditional-Constructs)) and some of the list constructs (see [Lists](#Lists)).

All of the Bash builtins return an exit status of zero if they succeed and a non-zero status on failure, so they may be used by the conditional and list constructs. All builtins return an exit status of 2 to indicate incorrect usage, generally invalid options or missing arguments.

The exit status of the last command is available in the special parameter \$? (see [Special Parameters](#Special-Parameters)).

Bash itself returns the exit status of the last command executed, unless a syntax error occurs, in which case it exits with a non-zero value. See also the `exit` builtin command (see [Bourne Shell Builtins](#Bourne-Shell-Builtins).

### Signals

signal handling

When Bash is interactive, in the absence of any traps, it ignores `SIGTERM` (so that ‘`kill 0`’ does not kill an interactive shell), and catches and handles `SIGINT` (so that the `wait` builtin is interruptible). When Bash receives a `SIGINT`, it breaks out of any executing loops. In all cases, Bash ignores `SIGQUIT`. If job control is in effect (see [Job Control](#Job-Control)), Bash ignores `SIGTTIN`, `SIGTTOU`, and `SIGTSTP`.

The `trap` builtin modifies the shell’s signal handling, as described below (see [Bourne Shell Builtins](#Bourne-Shell-Builtins).

Non-builtin commands Bash executes have signal handlers set to the values inherited by the shell from its parent, unless `trap` sets them to be ignored, in which case the child process will ignore them as well. When job control is not in effect, asynchronous commands ignore `SIGINT` and `SIGQUIT` in addition to these inherited handlers. Commands run as a result of command substitution ignore the keyboard-generated job control signals `SIGTTIN`, `SIGTTOU`, and `SIGTSTP`.

The shell exits by default upon receipt of a `SIGHUP`. Before exiting, an interactive shell resends the `SIGHUP` to all jobs, running or stopped. The shell sends `SIGCONT` to stopped jobs to ensure that they receive the `SIGHUP` (See [Job Control](#Job-Control), for more information about running and stopped jobs). To prevent the shell from sending the `SIGHUP` signal to a particular job, remove it from the jobs table with the `disown` builtin (see [Job Control Builtins](#Job-Control-Builtins)) or mark it not to receive `SIGHUP` using `disown -h`.

If the `huponexit` shell option has been set using `shopt` (see [The Shopt Builtin](#The-Shopt-Builtin)), Bash sends a `SIGHUP` to all jobs when an interactive login shell exits.

If Bash is waiting for a command to complete and receives a signal for which a trap has been set, it will not execute the trap until the command completes. If Bash is waiting for an asynchronous command via the `wait` builtin, and it receives a signal for which a trap has been set, the `wait` builtin will return immediately with an exit status greater than 128, immediately after which the shell executes the trap.

When job control is not enabled, and Bash is waiting for a foreground command to complete, the shell receives keyboard-generated signals such as `SIGINT` (usually generated by ‘`^C`’) that users commonly intend to send to that command. This happens because the shell and the command are in the same process group as the terminal, and ‘`^C`’ sends `SIGINT` to all processes in that process group. Since Bash does not enable job control by default when the shell is not interactive, this scenario is most common in non-interactive shells.

When job control is enabled, and Bash is waiting for a foreground command to complete, the shell does not receive keyboard-generated signals, because it is not in the same process group as the terminal. This scenario is most common in interactive shells, where Bash attempts to enable job control by default. See [Job Control](#Job-Control), for a more in-depth discussion of process groups.

When job control is not enabled, and Bash receives `SIGINT` while waiting for a foreground command, it waits until that foreground command terminates and then decides what to do about the `SIGINT`:

1.  If the command terminates due to the `SIGINT`, Bash concludes that the user meant to send the `SIGINT` to the shell as well, and acts on the `SIGINT` (e.g., by running a `SIGINT` trap, exiting a non-interactive shell, or returning to the top level to read a new command).

2.  If the command does not terminate due to `SIGINT`, the program handled the `SIGINT` itself and did not treat it as a fatal signal. In that case, Bash does not treat `SIGINT` as a fatal signal, either, instead assuming that the `SIGINT` was used as part of the program’s normal operation (e.g., `emacs` uses it to abort editing commands) or deliberately discarded. However, Bash will run any trap set on `SIGINT`, as it does with any other trapped signal it receives while it is waiting for the foreground command to complete, for compatibility.

When job control is enabled, Bash does not receive keyboard-generated signals such as `SIGINT` while it is waiting for a foreground command. An interactive shell does not pay attention to the `SIGINT`, even if the foreground command terminates as a result, other than noting its exit status. If the shell is not interactive, and the foreground command terminates due to the `SIGINT`, Bash pretends it received the `SIGINT` itself (scenario 1 above), for compatibility.
