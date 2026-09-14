---
title: Modifying Shell Behavior
source_url: https://www.gnu.org/software/bash/manual
source_path: 017-modifying-shell-behavior.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 170
---

## Modifying Shell Behavior

### The Set Builtin

This builtin is so complicated that it deserves its own section. `set` allows you to change the values of shell options and set the positional parameters, or to display the names and values of shell variables.

`set`  

set

    set [-abefhkmnptuvxBCEHPT] [-o option-name] [--] [-] [argument …]
    set [+abefhkmnptuvxBCEHPT] [+o option-name] [--] [-] [argument …]
    set -o
    set +o

If no options or arguments are supplied, `set` displays the names and values of all shell variables and functions, sorted according to the current locale, in a format that may be reused as input for setting or resetting the currently-set variables. Read-only variables cannot be reset. In POSIX mode, only shell variables are listed.

When options are supplied, they set or unset shell attributes. Any arguments remaining after option processing replace the positional parameters.

Options, if specified, have the following meanings:

`-a`  
Each variable or function that is created or modified is given the export attribute and marked for export to the environment of subsequent commands.

`-b`  
Cause the status of terminated background jobs to be reported immediately, rather than before printing the next primary prompt or, under some circumstances, when a foreground command exits. This is effective only when job control is enabled.

`-e`  
Exit immediately if a pipeline (see [Pipelines](#Pipelines)), which may consist of a single simple command (see [Simple Commands](#Simple-Commands)), a list (see [Lists](#Lists)), or a compound command (see [Compound Commands](#Compound-Commands)) returns a non-zero status. The shell does not exit if the command that fails is part of the command list immediately following a `while` or `until` reserved word, part of the test in an `if` statement, part of any command executed in a `&&` or `||` list except the command following the final `&&` or `||`, any command in a pipeline but the last (subject to the state of the `pipefail` shell option), or if the command’s return status is being inverted with `!`. If a compound command other than a subshell returns a non-zero status because a command failed while `-e` was being ignored, the shell does not exit. A trap on `ERR`, if set, is executed before the shell exits.

This option applies to the shell environment and each subshell environment separately (see [Command Execution Environment](#Command-Execution-Environment)), and may cause subshells to exit before executing all the commands in the subshell.

If a compound command or shell function executes in a context where `-e` is being ignored, none of the commands executed within the compound command or function body will be affected by the `-e` setting, even if `-e` is set and a command returns a failure status. If a compound command or shell function sets `-e` while executing in a context where `-e` is ignored, that setting will not have any effect until the compound command or the command containing the function call completes.

`-f`  
Disable filename expansion (globbing).

`-h`  
Locate and remember (hash) commands as they are looked up for execution. This option is enabled by default.

`-k`  
All arguments in the form of assignment statements are placed in the environment for a command, not just those that precede the command name.

`-m`  
Job control is enabled (see [Job Control](#Job-Control)). All processes run in a separate process group. When a background job completes, the shell prints a line containing its exit status.

`-n`  
Read commands but do not execute them. This may be used to check a script for syntax errors. This option is ignored by interactive shells.

`-o option-name`  
Set the option corresponding to \<option-name\>. If `-o` is supplied with no \<option-name\>, `set` prints the current shell options settings. If `+o` is supplied with no \<option-name\>, `set` prints a series of `set` commands to recreate the current option settings on the standard output. Valid option names are:

`allexport`  
Same as `-a`.

`braceexpand`  
Same as `-B`.

`emacs`  
Use an `emacs`-style line editing interface (see [Command Line Editing](#Command-Line-Editing)). This also affects the editing interface used for `read -e`.

`errexit`  
Same as `-e`.

`errtrace`  
Same as `-E`.

`functrace`  
Same as `-T`.

`hashall`  
Same as `-h`.

`histexpand`  
Same as `-H`.

`history`  
Enable command history, as described in [Bash History Facilities](#Bash-History-Facilities). This option is on by default in interactive shells.

`ignoreeof`  
An interactive shell will not exit upon reading EOF.

`keyword`  
Same as `-k`.

`monitor`  
Same as `-m`.

`noclobber`  
Same as `-C`.

`noexec`  
Same as `-n`.

`noglob`  
Same as `-f`.

`nolog`  
Currently ignored.

`notify`  
Same as `-b`.

`nounset`  
Same as `-u`.

`onecmd`  
Same as `-t`.

`physical`  
Same as `-P`.

`pipefail`  
If set, the return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands in the pipeline exit successfully. This option is disabled by default.

`posix`  
Enable POSIX mode; change the behavior of Bash where the default operation differs from the POSIX standard to match the standard (see [Bash POSIX Mode](#Bash-POSIX-Mode)). This is intended to make Bash behave as a strict superset of that standard.

`privileged`  
Same as `-p`.

`verbose`  
Same as `-v`.

`vi`  
Use a `vi`-style line editing interface. This also affects the editing interface used for `read -e`.

`xtrace`  
Same as `-x`.

`-p`  
Turn on privileged mode. In this mode, the `$BASH_ENV` and `$ENV` files are not processed, shell functions are not inherited from the environment, and the `SHELLOPTS`, `BASHOPTS`, `CDPATH` and `GLOBIGNORE` variables, if they appear in the environment, are ignored. If the shell is started with the effective user (group) id not equal to the real user (group) id, and the `-p` option is not supplied, these actions are taken and the effective user id is set to the real user id. If the `-p` option is supplied at startup, the effective user id is not reset. Turning this option off causes the effective user and group ids to be set to the real user and group ids.

`-r`  
Enable restricted shell mode (see [The Restricted Shell](#The-Restricted-Shell)). This option cannot be unset once it has been set.

`-t`  
Exit after reading and executing one command.

`-u`  
Treat unset variables and parameters other than the special parameters ‘`@`’ or ‘`*`’, or array variables subscripted with ‘`@`’ or ‘`*`’, as an error when performing parameter expansion. An error message will be written to the standard error, and a non-interactive shell will exit.

`-v`  
Print shell input lines to standard error as they are read.

`-x`  
Print a trace of simple commands, `for` commands, `case` commands, `select` commands, and arithmetic `for` commands and their arguments or associated word lists to the standard error after they are expanded and before they are executed. The shell prints the expanded value of the `PS4` variable before the command and its expanded arguments.

`-B`  
The shell will perform brace expansion (see [Brace Expansion](#Brace-Expansion)). This option is on by default.

`-C`  
Prevent output redirection using ‘`>`’, ‘`>&`’, and ‘`<>`’ from overwriting existing files. Using the redirection operator ‘`>|`’ instead of ‘`>`’ will override this and force the creation of an output file.

`-E`  
If set, any trap on `ERR` is inherited by shell functions, command substitutions, and commands executed in a subshell environment. The `ERR` trap is normally not inherited in such cases.

`-H`  
Enable ‘`!`’ style history substitution (see [History Interaction](#History-Interaction)). This option is on by default for interactive shells.

`-P`  
If set, Bash does not resolve symbolic links when executing commands such as `cd` which change the current directory. It uses the physical directory structure instead. By default, Bash follows the logical chain of directories when performing commands which change the current directory.

For example, if `/usr/sys` is a symbolic link to `/usr/local/sys` then:

    $ cd /usr/sys; echo $PWD
    /usr/sys
    $ cd ..; pwd
    /usr

If `set -P` is on, then:

    $ cd /usr/sys; echo $PWD
    /usr/local/sys
    $ cd ..; pwd
    /usr/local

`-T`  
If set, any traps on `DEBUG` and `RETURN` are inherited by shell functions, command substitutions, and commands executed in a subshell environment. The `DEBUG` and `RETURN` traps are normally not inherited in such cases.

`--`  
If no arguments follow this option, unset the positional parameters. Otherwise, the positional parameters are set to the \<arguments\>, even if some of them begin with a ‘`-`’.

`-`  
Signal the end of options, and assign all remaining \<arguments\> to the positional parameters. The `-x` and `-v` options are turned off. If there are no arguments, the positional parameters remain unchanged.

Using ‘`+`’ rather than ‘`-`’ causes these options to be turned off. The options can also be used upon invocation of the shell. The current set of options may be found in `$-`.

The remaining N \<arguments\> are positional parameters and are assigned, in order, to `$1`, `$2`, … `$N`. The special parameter `#` is set to N.

The return status is always zero unless an invalid option is supplied.

### The Shopt Builtin

This builtin allows you to change additional optional shell behavior.

`shopt`  

shopt

    shopt [-pqsu] [-o] [optname …]

Toggle the values of settings controlling optional shell behavior. The settings can be either those listed below, or, if the `-o` option is used, those available with the `-o` option to the `set` builtin command (see [The Set Builtin](#The-Set-Builtin)).

With no options, or with the `-p` option, display a list of all settable options, with an indication of whether or not each is set; if any \<optname\>s are supplied, the output is restricted to those options. The `-p` option displays output in a form that may be reused as input.

Other options have the following meanings:

`-s`  
Enable (set) each \<optname\>.

`-u`  
Disable (unset) each \<optname\>.

`-q`  
Suppresses normal output; the return status indicates whether the \<optname\> is set or unset. If multiple \<optname\> arguments are supplied with `-q`, the return status is zero if all \<optname\>s are enabled; non-zero otherwise.

`-o`  
Restricts the values of \<optname\> to be those defined for the `-o` option to the `set` builtin (see [The Set Builtin](#The-Set-Builtin)).

If either `-s` or `-u` is used with no \<optname\> arguments, `shopt` shows only those options which are set or unset, respectively.

Unless otherwise noted, the `shopt` options are disabled (off) by default.

The return status when listing options is zero if all \<optname\>s are enabled, non-zero otherwise. When setting or unsetting options, the return status is zero unless an \<optname\> is not a valid shell option.

The list of `shopt` options is:

`array_expand_once`  
If set, the shell suppresses multiple evaluation of associative and indexed array subscripts during arithmetic expression evaluation, while executing builtins that can perform variable assignments, and while executing builtins that perform array dereferencing.

`assoc_expand_once`  
Deprecated; a synonym for `array_expand_once`.

`autocd`  
If set, a command name that is the name of a directory is executed as if it were the argument to the `cd` command. This option is only used by interactive shells.

`bash_source_fullpath`  
If set, filenames added to the `BASH_SOURCE` array variable are converted to full pathnames (see [Bash Variables](#Bash-Variables)).

`cdable_vars`  
If this is set, an argument to the `cd` builtin command that is not a directory is assumed to be the name of a variable whose value is the directory to change to.

`cdspell`  
If set, the `cd` command attempts to correct minor errors in the spelling of a directory component. Minor errors include transposed characters, a missing character, and one extra character. If `cd` corrects the directory name, it prints the corrected filename, and the command proceeds. This option is only used by interactive shells.

`checkhash`  
If this is set, Bash checks that a command found in the hash table exists before trying to execute it. If a hashed command no longer exists, Bash performs a normal path search.

`checkjobs`  
If set, Bash lists the status of any stopped and running jobs before exiting an interactive shell. If any jobs are running, Bash defers the exit until a second exit is attempted without an intervening command (see [Job Control](#Job-Control)). The shell always postpones exiting if any jobs are stopped.

`checkwinsize`  
If set, Bash checks the window size after each external (non-builtin) command and, if necessary, updates the values of `LINES` and `COLUMNS`, using the file descriptor associated with stderr if it is a terminal. This option is enabled by default.

`cmdhist`  
If set, Bash attempts to save all lines of a multiple-line command in the same history entry. This allows easy re-editing of multi-line commands. This option is enabled by default, but only has an effect if command history is enabled (see [Bash History Facilities](#Bash-History-Facilities)).

`compat31`; `compat32`; `compat40`; `compat41`; `compat42`; `compat43`; `compat44`  
These control aspects of the shell’s compatibility mode (see [Shell Compatibility Mode](#Shell-Compatibility-Mode)).

`complete_fullquote`  
If set, Bash quotes all shell metacharacters in filenames and directory names when performing completion. If not set, Bash removes metacharacters such as the dollar sign from the set of characters that will be quoted in completed filenames when these metacharacters appear in shell variable references in words to be completed. This means that dollar signs in variable names that expand to directories will not be quoted; however, any dollar signs appearing in filenames will not be quoted, either. This is active only when Bash is using backslashes to quote completed filenames. This variable is set by default, which is the default Bash behavior in versions through 4.2.

`direxpand`  
If set, Bash replaces directory names with the results of word expansion when performing filename completion. This changes the contents of the Readline editing buffer. If not set, Bash attempts to preserve what the user typed.

`dirspell`  
If set, Bash attempts spelling correction on directory names during word completion if the directory name initially supplied does not exist.

`dotglob`  
If set, Bash includes filenames beginning with a ‘`.`’ in the results of filename expansion. The filenames `.` and `..` must always be matched explicitly, even if `dotglob` is set.

`execfail`  
If this is set, a non-interactive shell will not exit if it cannot execute the file specified as an argument to the `exec` builtin. An interactive shell does not exit if `exec` fails.

`expand_aliases`  
If set, aliases are expanded as described below under Aliases, [Aliases](#Aliases). This option is enabled by default for interactive shells.

`extdebug`  
If set at shell invocation, or in a shell startup file, arrange to execute the debugger profile before the shell starts, identical to the `--debugger` option. If set after invocation, behavior intended for use by debuggers is enabled:

1.  The `-F` option to the `declare` builtin (see [Bash Builtins](#Bash-Builtins)) displays the source file name and line number corresponding to each function name supplied as an argument.

2.  If the command run by the `DEBUG` trap returns a non-zero value, the next command is skipped and not executed.

3.  If the command run by the `DEBUG` trap returns a value of 2, and the shell is executing in a subroutine (a shell function or a shell script executed by the `.` or `source` builtins), the shell simulates a call to `return`.

4.  `BASH_ARGC` and `BASH_ARGV` are updated as described in their descriptions (see [Bash Variables](#Bash-Variables)).

5.  Function tracing is enabled: command substitution, shell functions, and subshells invoked with `( command )` inherit the `DEBUG` and `RETURN` traps.

6.  Error tracing is enabled: command substitution, shell functions, and subshells invoked with `( command )` inherit the `ERR` trap.

`extglob`  
If set, enable the extended pattern matching features described above (see [Pattern Matching](#Pattern-Matching)).

`extquote`  
If set, `$'string'` and `$"string"` quoting is performed within `${parameter}` expansions enclosed in double quotes. This option is enabled by default.

`failglob`  
If set, patterns which fail to match filenames during filename expansion result in an expansion error.

`force_fignore`  
If set, the suffixes specified by the `FIGNORE` shell variable cause words to be ignored when performing word completion even if the ignored words are the only possible completions. See [Bash Variables](#Bash-Variables), for a description of `FIGNORE`. This option is enabled by default.

`globasciiranges`  
If set, range expressions used in pattern matching bracket expressions (see [Pattern Matching](#Pattern-Matching)) behave as if in the traditional C locale when performing comparisons. That is, pattern matching does not take the current locale’s collating sequence into account, so ‘`b`’ will not collate between ‘`A`’ and ‘`B`’, and upper-case and lower-case ASCII characters will collate together.

`globskipdots`  
If set, filename expansion will never match the filenames `.` and `..`, even if the pattern begins with a ‘`.`’. This option is enabled by default.

`globstar`  
If set, the pattern ‘`**`’ used in a filename expansion context will match all files and zero or more directories and subdirectories. If the pattern is followed by a ‘`/`’, only directories and subdirectories match.

`gnu_errfmt`  
If set, shell error messages are written in the standard GNU error message format.

`histappend`  
If set, the history list is appended to the file named by the value of the `HISTFILE` variable when the shell exits, rather than overwriting the file.

`histreedit`  
If set, and Readline is being used, the user is given the opportunity to re-edit a failed history substitution.

`histverify`  
If set, and Readline is being used, the results of history substitution are not immediately passed to the shell parser. Instead, the resulting line is loaded into the Readline editing buffer, allowing further modification.

`hostcomplete`  
If set, and Readline is being used, Bash will attempt to perform hostname completion when a word containing a ‘`@`’ is being completed (see [Commands For Completion](#Commands-For-Completion)). This option is enabled by default.

`huponexit`  
If set, Bash will send `SIGHUP` to all jobs when an interactive login shell exits (see [Signals](#Signals)).

`inherit_errexit`  
If set, command substitution inherits the value of the `errexit` option, instead of unsetting it in the subshell environment. This option is enabled when POSIX mode is enabled.

`interactive_comments`  
In an interactive shell, a word beginning with ‘`#`’ causes that word and all remaining characters on that line to be ignored, as in a non-interactive shell. This option is enabled by default.

`lastpipe`  
If set, and job control is not active, the shell runs the last command of a pipeline not executed in the background in the current shell environment.

`lithist`  
If enabled, and the `cmdhist` option is enabled, multi-line commands are saved to the history with embedded newlines rather than using semicolon separators where possible.

`localvar_inherit`  
If set, local variables inherit the value and attributes of a variable of the same name that exists at a previous scope before any new value is assigned. The `nameref` attribute is not inherited.

`localvar_unset`  
If set, calling `unset` on local variables in previous function scopes marks them so subsequent lookups find them unset until that function returns. This is identical to the behavior of unsetting local variables at the current function scope.

`login_shell`  
The shell sets this option if it is started as a login shell (see [Invoking Bash](#Invoking-Bash)). The value may not be changed.

`mailwarn`  
If set, and a file that Bash is checking for mail has been accessed since the last time it was checked, Bash displays the message `"The mail in mailfile has been read"`.

`no_empty_cmd_completion`  
If set, and Readline is being used, Bash does not search the `PATH` for possible completions when completion is attempted on an empty line.

`nocaseglob`  
If set, Bash matches filenames in a case-insensitive fashion when performing filename expansion.

`nocasematch`  
If set, Bash matches patterns in a case-insensitive fashion when performing matching while executing `case` or `[[` conditional commands (see [Conditional Constructs](#Conditional-Constructs), when performing pattern substitution word expansions, or when filtering possible completions as part of programmable completion.

`noexpand_translation`  
If set, Bash encloses the translated results of \$"…" quoting in single quotes instead of double quotes. If the string is not translated, this has no effect.

`nullglob`  
If set, filename expansion patterns which match no files (see [Filename Expansion](#Filename-Expansion)) expand to nothing and are removed, rather than expanding to themselves.

`patsub_replacement`  
If set, Bash expands occurrences of ‘`&`’ in the replacement string of pattern substitution to the text matched by the pattern, as described above (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)). This option is enabled by default.

`progcomp`  
If set, enable the programmable completion facilities (see [Programmable Completion](#Programmable-Completion)). This option is enabled by default.

`progcomp_alias`  
If set, and programmable completion is enabled, Bash treats a command name that doesn’t have any completions as a possible alias and attempts alias expansion. If it has an alias, Bash attempts programmable completion using the command word resulting from the expanded alias.

`promptvars`  
If set, prompt strings undergo parameter expansion, command substitution, arithmetic expansion, and quote removal after being expanded as described below (see [Controlling the Prompt](#Controlling-the-Prompt)). This option is enabled by default.

`restricted_shell`  
The shell sets this option if it is started in restricted mode (see [The Restricted Shell](#The-Restricted-Shell)). The value may not be changed. This is not reset when the startup files are executed, allowing the startup files to discover whether or not a shell is restricted.

`shift_verbose`  
If this is set, the `shift` builtin prints an error message when the shift count exceeds the number of positional parameters.

`sourcepath`  
If set, the `.` (`source`) builtin uses the value of `PATH` to find the directory containing the file supplied as an argument when the `-p` option is not supplied. This option is enabled by default.

`varredir_close`  
If set, the shell automatically closes file descriptors assigned using the `{varname}` redirection syntax (see [Redirections](#Redirections)) instead of leaving them open when the command completes.

`xpg_echo`  
If set, the `echo` builtin expands backslash-escape sequences by default. If the `posix` shell option (see [The Set Builtin](#The-Set-Builtin)) is also enabled, `echo` does not interpret any options.
