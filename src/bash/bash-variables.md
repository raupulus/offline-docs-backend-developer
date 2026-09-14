---
title: Bash Variables
source_url: https://www.gnu.org/software/bash/manual
source_path: 021-bash-variables.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 210
---

## Bash Variables

These variables are set or used by Bash, but other shells do not normally treat them specially.

A few variables used by Bash are described in different chapters: variables for controlling the job control facilities (see [Job Control Variables](#Job-Control-Variables)).

<span class="indexterm vr" role="vr"></span>`_`  

\$\_

(\$\_, an underscore.) This has a number of meanings depending on context. At shell startup, \$\_ set to the pathname used to invoke the shell or shell script being executed as passed in the environment or argument list. Subsequently, it expands to the last argument to the previous simple command executed in the foreground, after expansion. It is also set to the full pathname used to invoke each command executed and placed in the environment exported to that command. When checking mail, \$\_ expands to the name of the mail file.

<span class="indexterm vr" role="vr"></span>`BASH`  
The full pathname used to execute the current instance of Bash.

<span class="indexterm vr" role="vr"></span>`BASHOPTS`  
A colon-separated list of enabled shell options. Each word in the list is a valid argument for the `-s` option to the `shopt` builtin command (see [The Shopt Builtin](#The-Shopt-Builtin)). The options appearing in `BASHOPTS` are those reported as ‘`on`’ by ‘`shopt`’. If this variable is in the environment when Bash starts up, the shell enables each option in the list before reading any startup files. If this variable is exported, child shells will enable each option in the list. This variable is readonly.

<span class="indexterm vr" role="vr"></span>`BASHPID`  
Expands to the process ID of the current Bash process. This differs from `$$` under certain circumstances, such as subshells that do not require Bash to be re-initialized. Assignments to `BASHPID` have no effect. If `BASHPID` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`BASH_ALIASES`  
An associative array variable whose members correspond to the internal list of aliases as maintained by the `alias` builtin. (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)). Elements added to this array appear in the alias list; however, unsetting array elements currently does not cause aliases to be removed from the alias list. If `BASH_ALIASES` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`BASH_ARGC`  
An array variable whose values are the number of parameters in each frame of the current Bash execution call stack. The number of parameters to the current subroutine (shell function or script executed with `.` or `source`) is at the top of the stack. When a subroutine is executed, the number of parameters passed is pushed onto `BASH_ARGC`. The shell sets `BASH_ARGC` only when in extended debugging mode (see [The Shopt Builtin](#The-Shopt-Builtin) for a description of the `extdebug` option to the `shopt` builtin). Setting `extdebug` after the shell has started to execute a subroutine, or referencing this variable when `extdebug` is not set, may result in inconsistent values. Assignments to `BASH_ARGC` have no effect, and it may not be unset.

<span class="indexterm vr" role="vr"></span>`BASH_ARGV`  
An array variable containing all of the parameters in the current Bash execution call stack. The final parameter of the last subroutine call is at the top of the stack; the first parameter of the initial call is at the bottom. When a subroutine is executed, the shell pushes the supplied parameters onto `BASH_ARGV`. The shell sets `BASH_ARGV` only when in extended debugging mode (see [The Shopt Builtin](#The-Shopt-Builtin) for a description of the `extdebug` option to the `shopt` builtin). Setting `extdebug` after the shell has started to execute a script, or referencing this variable when `extdebug` is not set, may result in inconsistent values. Assignments to `BASH_ARGV` have no effect, and it may not be unset.

<span class="indexterm vr" role="vr"></span>`BASH_ARGV0`  
When referenced, this variable expands to the name of the shell or shell script (identical to `$0`; See [Special Parameters](#Special-Parameters), for the description of special parameter 0). Assigning a value to `BASH_ARGV0` sets `$0` to the same value. If `BASH_ARGV0` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`BASH_CMDS`  
An associative array variable whose members correspond to the internal hash table of commands as maintained by the `hash` builtin (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)). Adding elements to this array makes them appear in the hash table; however, unsetting array elements currently does not remove command names from the hash table. If `BASH_CMDS` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`BASH_COMMAND`  
Expands to the command currently being executed or about to be executed, unless the shell is executing a command as the result of a trap, in which case it is the command executing at the time of the trap. If `BASH_COMMAND` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`BASH_COMPAT`  
The value is used to set the shell’s compatibility level. See [Shell Compatibility Mode](#Shell-Compatibility-Mode), for a description of the various compatibility levels and their effects. The value may be a decimal number (e.g., 4.2) or an integer (e.g., 42) corresponding to the desired compatibility level. If `BASH_COMPAT` is unset or set to the empty string, the compatibility level is set to the default for the current version. If `BASH_COMPAT` is set to a value that is not one of the valid compatibility levels, the shell prints an error message and sets the compatibility level to the default for the current version. A subset of the valid values correspond to the compatibility levels described below (see [Shell Compatibility Mode](#Shell-Compatibility-Mode)). For example, 4.2 and 42 are valid values that correspond to the `compat42` `shopt` option and set the compatibility level to 42. The current version is also a valid value.

<span class="indexterm vr" role="vr"></span>`BASH_ENV`  
If this variable is set when Bash is invoked to execute a shell script, its value is expanded and used as the name of a startup file to read before executing the script. Bash does not use `PATH` to search for the resultant filename. See [Bash Startup Files](#Bash-Startup-Files).

<span class="indexterm vr" role="vr"></span>`BASH_EXECUTION_STRING`  
The command argument to the `-c` invocation option.

<span class="indexterm vr" role="vr"></span>`BASH_LINENO`  
An array variable whose members are the line numbers in source files where each corresponding member of `FUNCNAME` was invoked. `${BASH_LINENO[$i]}` is the line number in the source file (`${BASH_SOURCE[$i+1]}`) where `${FUNCNAME[$i]}` was called (or `${BASH_LINENO[$i-1]}` if referenced within another shell function). Use `LINENO` to obtain the current line number. Assignments to `BASH_LINENO` have no effect, and it may not be unset.

<span class="indexterm vr" role="vr"></span>`BASH_LOADABLES_PATH`  
A colon-separated list of directories in which the `enable` command looks for dynamically loadable builtins.

<span class="indexterm vr" role="vr"></span>`BASH_MONOSECONDS`  
Each time this variable is referenced, it expands to the value returned by the system’s monotonic clock, if one is available. If there is no monotonic clock, this is equivalent to `EPOCHSECONDS`. If `BASH_MONOSECONDS` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`BASH_REMATCH`  
An array variable whose members are assigned by the ‘`=~`’ binary operator to the `[[` conditional command (see [Conditional Constructs](#Conditional-Constructs)). The element with index 0 is the portion of the string matching the entire regular expression. The element with index \<n\> is the portion of the string matching the \<n\>th parenthesized subexpression.

<span class="indexterm vr" role="vr"></span>`BASH_SOURCE`  
An array variable whose members are the source filenames where the corresponding shell function names in the `FUNCNAME` array variable are defined. The shell function `${FUNCNAME[$i]}` is defined in the file `${BASH_SOURCE[$i]}` and called from `${BASH_SOURCE[$i+1]}` Assignments to `BASH_SOURCE` have no effect, and it may not be unset.

<span class="indexterm vr" role="vr"></span>`BASH_SUBSHELL`  
Incremented by one within each subshell or subshell environment when the shell begins executing in that environment. The initial value is 0. If `BASH_SUBSHELL` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`BASH_TRAPSIG`  
Set to the signal number corresponding to the trap action being executed during its execution. See the description of `trap` (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)) for information about signal numbers and trap execution.

<span class="indexterm vr" role="vr"></span>`BASH_VERSINFO`  
A readonly array variable (see [Arrays](#Arrays)) whose members hold version information for this instance of Bash. The values assigned to the array members are as follows:

`BASH_VERSINFO[0]`  
The major version number (the release).

`BASH_VERSINFO[1]`  
The minor version number (the version).

`BASH_VERSINFO[2]`  
The patch level.

`BASH_VERSINFO[3]`  
The build version.

`BASH_VERSINFO[4]`  
The release status (e.g., `beta`).

`BASH_VERSINFO[5]`  
The value of `MACHTYPE`.

<span class="indexterm vr" role="vr"></span>`BASH_VERSION`  
Expands to a string describing the version of this instance of Bash (e.g., 5.2.37(3)-release).

<span class="indexterm vr" role="vr"></span>`BASH_XTRACEFD`  
If set to an integer corresponding to a valid file descriptor, Bash writes the trace output generated when ‘`set -x`’ is enabled to that file descriptor, instead of the standard error. This allows tracing output to be separated from diagnostic and error messages. The file descriptor is closed when `BASH_XTRACEFD` is unset or assigned a new value. Unsetting `BASH_XTRACEFD` or assigning it the empty string causes the trace output to be sent to the standard error. Note that setting `BASH_XTRACEFD` to 2 (the standard error file descriptor) and then unsetting it will result in the standard error being closed.

<span class="indexterm vr" role="vr"></span>`CHILD_MAX`  
Set the number of exited child status values for the shell to remember. Bash will not allow this value to be decreased below a POSIX-mandated minimum, and there is a maximum value (currently 8192) that this may not exceed. The minimum value is system-dependent.

<span class="indexterm vr" role="vr"></span>`COLUMNS`  
Used by the `select` command to determine the terminal width when printing selection lists. Automatically set if the `checkwinsize` option is enabled (see [The Shopt Builtin](#The-Shopt-Builtin)), or in an interactive shell upon receipt of a `SIGWINCH`.

<span class="indexterm vr" role="vr"></span>`COMP_CWORD`  
An index into `${COMP_WORDS}` of the word containing the current cursor position. This variable is available only in shell functions invoked by the programmable completion facilities (see [Programmable Completion](#Programmable-Completion)).

<span class="indexterm vr" role="vr"></span>`COMP_KEY`  
The key (or final key of a key sequence) used to invoke the current completion function. This variable is available only in shell functions and external commands invoked by the programmable completion facilities (see [Programmable Completion](#Programmable-Completion)).

<span class="indexterm vr" role="vr"></span>`COMP_LINE`  
The current command line. This variable is available only in shell functions and external commands invoked by the programmable completion facilities (see [Programmable Completion](#Programmable-Completion)).

<span class="indexterm vr" role="vr"></span>`COMP_POINT`  
The index of the current cursor position relative to the beginning of the current command. If the current cursor position is at the end of the current command, the value of this variable is equal to `${#COMP_LINE}`. This variable is available only in shell functions and external commands invoked by the programmable completion facilities (see [Programmable Completion](#Programmable-Completion)).

<span class="indexterm vr" role="vr"></span>`COMP_TYPE`  
Set to an integer value corresponding to the type of attempted completion that caused a completion function to be called: TAB, for normal completion, ‘`?`’, for listing completions after successive tabs, ‘`!`’, for listing alternatives on partial word completion, ‘`@`’, to list completions if the word is not unmodified, or ‘`%`’, for menu completion. This variable is available only in shell functions and external commands invoked by the programmable completion facilities (see [Programmable Completion](#Programmable-Completion)).

<span class="indexterm vr" role="vr"></span>`COMP_WORDBREAKS`  
The set of characters that the Readline library treats as word separators when performing word completion. If `COMP_WORDBREAKS` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`COMP_WORDS`  
An array variable consisting of the individual words in the current command line. The line is split into words as Readline would split it, using `COMP_WORDBREAKS` as described above. This variable is available only in shell functions invoked by the programmable completion facilities (see [Programmable Completion](#Programmable-Completion)).

<span class="indexterm vr" role="vr"></span>`COMPREPLY`  
An array variable from which Bash reads the possible completions generated by a shell function invoked by the programmable completion facility (see [Programmable Completion](#Programmable-Completion)). Each array element contains one possible completion.

<span class="indexterm vr" role="vr"></span>`COPROC`  
An array variable created to hold the file descriptors for output from and input to an unnamed coprocess (see [Coprocesses](#Coprocesses)).

<span class="indexterm vr" role="vr"></span>`DIRSTACK`  
An array variable containing the current contents of the directory stack. Directories appear in the stack in the order they are displayed by the `dirs` builtin. Assigning to members of this array variable may be used to modify directories already in the stack, but the `pushd` and `popd` builtins must be used to add and remove directories. Assigning to this variable does not change the current directory. If `DIRSTACK` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`EMACS`  
If Bash finds this variable in the environment when the shell starts, and its value is ‘`t`’, Bash assumes that the shell is running in an Emacs shell buffer and disables line editing.

<span class="indexterm vr" role="vr"></span>`ENV`  
Expanded and executed similarly to `BASH_ENV` (see [Bash Startup Files](#Bash-Startup-Files)) when an interactive shell is invoked in POSIX mode (see [Bash POSIX Mode](#Bash-POSIX-Mode)).

<span class="indexterm vr" role="vr"></span>`EPOCHREALTIME`  
Each time this parameter is referenced, it expands to the number of seconds since the Unix Epoch as a floating-point value with micro-second granularity (see the documentation for the C library function `time` for the definition of Epoch). Assignments to `EPOCHREALTIME` are ignored. If `EPOCHREALTIME` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`EPOCHSECONDS`  
Each time this parameter is referenced, it expands to the number of seconds since the Unix Epoch (see the documentation for the C library function `time` for the definition of Epoch). Assignments to `EPOCHSECONDS` are ignored. If `EPOCHSECONDS` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`EUID`  
The numeric effective user id of the current user. This variable is readonly.

<span class="indexterm vr" role="vr"></span>`EXECIGNORE`  
A colon-separated list of shell patterns (see [Pattern Matching](#Pattern-Matching)) defining the set of filenames to be ignored by command search using `PATH`. Files whose full pathnames match one of these patterns are not considered executable files for the purposes of completion and command execution via `PATH` lookup. This does not affect the behavior of the `[`, `test`, and `[[` commands. Full pathnames in the command hash table are not subject to `EXECIGNORE`. Use this variable to ignore shared library files that have the executable bit set, but are not executable files. The pattern matching honors the setting of the `extglob` shell option.

<span class="indexterm vr" role="vr"></span>`FCEDIT`  
The editor used as a default by the `fc` builtin command.

<span class="indexterm vr" role="vr"></span>`FIGNORE`  
A colon-separated list of suffixes to ignore when performing filename completion. A filename whose suffix matches one of the entries in `FIGNORE` is excluded from the list of matched filenames. A sample value is ‘`.o:~`’

<span class="indexterm vr" role="vr"></span>`FUNCNAME`  
An array variable containing the names of all shell functions currently in the execution call stack. The element with index 0 is the name of any currently-executing shell function. The bottom-most element (the one with the highest index) is `"main"`. This variable exists only when a shell function is executing. Assignments to `FUNCNAME` have no effect. If `FUNCNAME` is unset, it loses its special properties, even if it is subsequently reset.

This variable can be used with `BASH_LINENO` and `BASH_SOURCE`. Each element of `FUNCNAME` has corresponding elements in `BASH_LINENO` and `BASH_SOURCE` to describe the call stack. For instance, `${FUNCNAME[$i]}` was called from the file `${BASH_SOURCE[$i+1]}` at line number `${BASH_LINENO[$i]}`. The `caller` builtin displays the current call stack using this information.

<span class="indexterm vr" role="vr"></span>`FUNCNEST`  
A numeric value greater than 0 defines a maximum function nesting level. Function invocations that exceed this nesting level cause the current command to abort.

<span class="indexterm vr" role="vr"></span>`GLOBIGNORE`  
A colon-separated list of patterns defining the set of file names to be ignored by filename expansion. If a file name matched by a filename expansion pattern also matches one of the patterns in `GLOBIGNORE`, it is removed from the list of matches. The pattern matching honors the setting of the `extglob` shell option.

<span class="indexterm vr" role="vr"></span>`GLOBSORT`  
Controls how the results of filename expansion are sorted. The value of this variable specifies the sort criteria and sort order for the results of filename expansion. If this variable is unset or set to the null string, filename expansion uses the historical behavior of sorting by name, in ascending lexicographic order as determined by the `LC_COLLATE` shell variable.

If set, a valid value begins with an optional ‘`+`’, which is ignored, or ‘`-`’, which reverses the sort order from ascending to descending, followed by a sort specifier. The valid sort specifiers are ‘`name`’, ‘`numeric`’, ‘`size`’, ‘`mtime`’, ‘`atime`’, ‘`ctime`’, and ‘`blocks`’, which sort the files on name, names in numeric rather than lexicographic order, file size, modification time, access time, inode change time, and number of blocks, respectively. If any of the non-name keys compare as equal (e.g., if two files are the same size), sorting uses the name as a secondary sort key.

For example, a value of `-mtime` sorts the results in descending order by modification time (newest first).

The ‘`numeric`’ specifier treats names consisting solely of digits as numbers and sorts them using their numeric value (so “2” sorts before “10”, for example). When using ‘`numeric`’, names containing non-digits sort after all the all-digit names and are sorted by name using the traditional behavior.

A sort specifier of ‘`nosort`’ disables sorting completely; Bash returns the results in the order they are read from the file system, ignoring any leading ‘`-`’.

If the sort specifier is missing, it defaults to \<name\>, so a value of ‘`+`’ is equivalent to the null string, and a value of ‘`-`’ sorts by name in descending order.

Any invalid value restores the historical sorting behavior.

<span class="indexterm vr" role="vr"></span>`GROUPS`  
An array variable containing the list of groups of which the current user is a member. Assignments to `GROUPS` have no effect. If `GROUPS` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`histchars`  
The two or three characters which control history expansion, quick substitution, and tokenization (see [History Interaction](#History-Interaction)). The first character is the history expansion character, the character which begins a history expansion, normally ‘`!`’. The second character is the quick substitution character, normally ‘`^`’. When it appears as the first character on the line, history substitution repeats the previous command, replacing one string with another. The optional third character is the history comment character, normally ‘`#`’, which indicates that the remainder of the line is a comment when it appears as the first character of a word. The history comment character disables history substitution for the remaining words on the line. It does not necessarily cause the shell parser to treat the rest of the line as a comment.

<span class="indexterm vr" role="vr"></span>`HISTCMD`  
The history number, or index in the history list, of the current command. Assignments to `HISTCMD` have no effect. If `HISTCMD` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`HISTCONTROL`  
A colon-separated list of values controlling how commands are saved on the history list. If the list of values includes ‘`ignorespace`’, lines which begin with a space character are not saved in the history list. A value of ‘`ignoredups`’ causes lines which match the previous history entry not to be saved. A value of ‘`ignoreboth`’ is shorthand for ‘`ignorespace`’ and ‘`ignoredups`’. A value of ‘`erasedups`’ causes all previous lines matching the current line to be removed from the history list before that line is saved. Any value not in the above list is ignored. If `HISTCONTROL` is unset, or does not include a valid value, Bash saves all lines read by the shell parser on the history list, subject to the value of `HISTIGNORE`. If the first line of a multi-line compound command was saved, the second and subsequent lines are not tested, and are added to the history regardless of the value of `HISTCONTROL`. If the first line was not saved, the second and subsequent lines of the command are not saved either.

<span class="indexterm vr" role="vr"></span>`HISTFILE`  
The name of the file to which the command history is saved. Bash assigns a default value of `~/.bash_history`. If `HISTFILE` is unset or null, the shell does not save the command history when it exits.

<span class="indexterm vr" role="vr"></span>`HISTFILESIZE`  
The maximum number of lines contained in the history file. When this variable is assigned a value, the history file is truncated, if necessary, to contain no more than the number of history entries that total no more than that number of lines by removing the oldest entries. If the history list contains multi-line entries, the history file may contain more lines than this maximum to avoid leaving partial history entries. The history file is also truncated to this size after writing it when a shell exits or by the `history` builtin. If the value is 0, the history file is truncated to zero size. Non-numeric values and numeric values less than zero inhibit truncation. The shell sets the default value to the value of `HISTSIZE` after reading any startup files.

<span class="indexterm vr" role="vr"></span>`HISTIGNORE`  
A colon-separated list of patterns used to decide which command lines should be saved on the history list. If a command line matches one of the patterns in the value of `HISTIGNORE`, it is not saved on the history list. Each pattern is anchored at the beginning of the line and must match the complete line (Bash does not implicitly append a ‘`*`’). Each pattern is tested against the line after the checks specified by `HISTCONTROL` are applied. In addition to the normal shell pattern matching characters, ‘`&`’ matches the previous history line. A backslash escapes the ‘`&`’; the backslash is removed before attempting a match. If the first line of a multi-line compound command was saved, the second and subsequent lines are not tested, and are added to the history regardless of the value of `HISTIGNORE`. If the first line was not saved, the second and subsequent lines of the command are not saved either. The pattern matching honors the setting of the `extglob` shell option.

`HISTIGNORE` subsumes some of the function of `HISTCONTROL`. A pattern of ‘`&`’ is identical to `ignoredups`, and a pattern of ‘`[ ]*`’ is identical to `ignorespace`. Combining these two patterns, separating them with a colon, provides the functionality of `ignoreboth`.

<span class="indexterm vr" role="vr"></span>`HISTSIZE`  
The maximum number of commands to remember on the history list. If the value is 0, commands are not saved in the history list. Numeric values less than zero result in every command being saved on the history list (there is no limit). The shell sets the default value to 500 after reading any startup files.

<span class="indexterm vr" role="vr"></span>`HISTTIMEFORMAT`  
If this variable is set and not null, its value is used as a format string for `strftime`(3) to print the time stamp associated with each history entry displayed by the `history` builtin. If this variable is set, the shell writes time stamps to the history file so they may be preserved across shell sessions. This uses the history comment character to distinguish timestamps from other history lines.

<span class="indexterm vr" role="vr"></span>`HOSTFILE`  
Contains the name of a file in the same format as `/etc/hosts` that should be read when the shell needs to complete a hostname. The list of possible hostname completions may be changed while the shell is running; the next time hostname completion is attempted after the value is changed, Bash adds the contents of the new file to the existing list. If `HOSTFILE` is set, but has no value, or does not name a readable file, Bash attempts to read `/etc/hosts` to obtain the list of possible hostname completions. When `HOSTFILE` is unset, Bash clears the hostname list.

<span class="indexterm vr" role="vr"></span>`HOSTNAME`  
The name of the current host.

<span class="indexterm vr" role="vr"></span>`HOSTTYPE`  
A string describing the machine Bash is running on.

<span class="indexterm vr" role="vr"></span>`IGNOREEOF`  
Controls the action of the shell on receipt of an `EOF` character as the sole input. If set, the value is the number of consecutive `EOF` characters that can be read as the first character on an input line before Bash exits. If the variable is set but does not have a numeric value, or the value is null, then the default is 10. If the variable is unset, then `EOF` signifies the end of input to the shell. This is only in effect for interactive shells.

<span class="indexterm vr" role="vr"></span>`INPUTRC`  
The name of the Readline initialization file, overriding the default of `~/.inputrc`.

<span class="indexterm vr" role="vr"></span>`INSIDE_EMACS`  
If Bash finds this variable in the environment when the shell starts, it assumes that the shell is running in an Emacs shell buffer and may disable line editing depending on the value of `TERM`.

<span class="indexterm vr" role="vr"></span>`LANG`  
Used to determine the locale category for any category not specifically selected with a variable starting with `LC_`.

<span class="indexterm vr" role="vr"></span>`LC_ALL`  
This variable overrides the value of `LANG` and any other `LC_` variable specifying a locale category.

<span class="indexterm vr" role="vr"></span>`LC_COLLATE`  
This variable determines the collation order used when sorting the results of filename expansion, and determines the behavior of range expressions, equivalence classes, and collating sequences within filename expansion and pattern matching (see [Filename Expansion](#Filename-Expansion)).

<span class="indexterm vr" role="vr"></span>`LC_CTYPE`  
This variable determines the interpretation of characters and the behavior of character classes within filename expansion and pattern matching (see [Filename Expansion](#Filename-Expansion)).

<span class="indexterm vr" role="vr"></span>`LC_MESSAGES`  
This variable determines the locale used to translate double-quoted strings preceded by a ‘`$`’ (see [Locale Translation](#Locale-Translation)).

<span class="indexterm vr" role="vr"></span>`LC_NUMERIC`  
This variable determines the locale category used for number formatting.

<span class="indexterm vr" role="vr"></span>`LC_TIME`  
This variable determines the locale category used for data and time formatting.

<span class="indexterm vr" role="vr"></span>`LINENO`  
The line number in the script or shell function currently executing. Line numbers start with 1. When not in a script or function, the value is not guaranteed to be meaningful. If `LINENO` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`LINES`  
Used by the `select` command to determine the column length for printing selection lists. Automatically set if the `checkwinsize` option is enabled (see [The Shopt Builtin](#The-Shopt-Builtin)), or in an interactive shell upon receipt of a `SIGWINCH`.

<span class="indexterm vr" role="vr"></span>`MACHTYPE`  
A string that fully describes the system type on which Bash is executing, in the standard GNU \<cpu-company-system\> format.

<span class="indexterm vr" role="vr"></span>`MAILCHECK`  
How often (in seconds) that the shell should check for mail in the files specified in the `MAILPATH` or `MAIL` variables. The default is 60 seconds. When it is time to check for mail, the shell does so before displaying the primary prompt. If this variable is unset, or set to a value that is not a number greater than or equal to zero, the shell disables mail checking.

<span class="indexterm vr" role="vr"></span>`MAPFILE`  
An array variable created to hold the text read by the `mapfile` builtin when no variable name is supplied.

<span class="indexterm vr" role="vr"></span>`OLDPWD`  
The previous working directory as set by the `cd` builtin.

<span class="indexterm vr" role="vr"></span>`OPTERR`  
If set to the value 1, Bash displays error messages generated by the `getopts` builtin command. `OPTERR` is initialized to 1 each time the shell is invoked.

<span class="indexterm vr" role="vr"></span>`OSTYPE`  
A string describing the operating system Bash is running on.

<span class="indexterm vr" role="vr"></span>`PIPESTATUS`  
An array variable (see [Arrays](#Arrays)) containing a list of exit status values from the commands in the most-recently-executed foreground pipeline, which may consist of only a simple command (see [Shell Commands](#Shell-Commands)). Bash sets `PIPESTATUS` after executing multi-element pipelines, timed and negated pipelines, simple commands, subshells created with the ‘`(`’ operator, the `[[` and `((` compound commands, and after error conditions that result in the shell aborting command execution.

<span class="indexterm vr" role="vr"></span>`POSIXLY_CORRECT`  
If this variable is in the environment when Bash starts, the shell enters POSIX mode (see [Bash POSIX Mode](#Bash-POSIX-Mode)) before reading the startup files, as if the `--posix` invocation option had been supplied. If it is set while the shell is running, Bash enables POSIX mode, as if the command

    set -o posix

had been executed. When the shell enters POSIX mode, it sets this variable if it was not already set.

<span class="indexterm vr" role="vr"></span>`PPID`  
The process ID of the shell’s parent process. This variable is readonly.

<span class="indexterm vr" role="vr"></span>`PROMPT_COMMAND`  
If this variable is set, and is an array, the value of each set element is interpreted as a command to execute before printing the primary prompt (`$PS1`). If this is set but not an array variable, its value is used as a command to execute instead.

<span class="indexterm vr" role="vr"></span>`PROMPT_DIRTRIM`  
If set to a number greater than zero, the value is used as the number of trailing directory components to retain when expanding the `\w` and `\W` prompt string escapes (see [Controlling the Prompt](#Controlling-the-Prompt)). Characters removed are replaced with an ellipsis.

<span class="indexterm vr" role="vr"></span>`PS0`  
The value of this parameter is expanded like `PS1` and displayed by interactive shells after reading a command and before the command is executed.

<span class="indexterm vr" role="vr"></span>`PS3`  
The value of this variable is used as the prompt for the `select` command. If this variable is not set, the `select` command prompts with ‘`#?`’

<span class="indexterm vr" role="vr"></span>`PS4`  
The value of this parameter is expanded like `PS1` and the expanded value is the prompt printed before the command line is echoed when the `-x` option is set (see [The Set Builtin](#The-Set-Builtin)). The first character of the expanded value is replicated multiple times, as necessary, to indicate multiple levels of indirection. The default is ‘`+`’.

<span class="indexterm vr" role="vr"></span>`PWD`  
The current working directory as set by the `cd` builtin.

<span class="indexterm vr" role="vr"></span>`RANDOM`  
Each time this parameter is referenced, it expands to a random integer between 0 and 32767. Assigning a value to `RANDOM` initializes (seeds) the sequence of random numbers. Seeding the random number generator with the same constant value produces the same sequence of values. If `RANDOM` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`READLINE_ARGUMENT`  
Any numeric argument given to a Readline command that was defined using ‘`bind -x`’ (see [Bash Builtins](#Bash-Builtins) when it was invoked.

<span class="indexterm vr" role="vr"></span>`READLINE_LINE`  
The contents of the Readline line buffer, for use with ‘`bind -x`’ (see [Bash Builtins](#Bash-Builtins)).

<span class="indexterm vr" role="vr"></span>`READLINE_MARK`  
The position of the mark (saved insertion point) in the Readline line buffer, for use with ‘`bind -x`’ (see [Bash Builtins](#Bash-Builtins)). The characters between the insertion point and the mark are often called the region.

<span class="indexterm vr" role="vr"></span>`READLINE_POINT`  
The position of the insertion point in the Readline line buffer, for use with ‘`bind -x`’ (see [Bash Builtins](#Bash-Builtins)).

<span class="indexterm vr" role="vr"></span>`REPLY`  
The default variable for the `read` builtin; set to the line read when `read` is not supplied a variable name argument.

<span class="indexterm vr" role="vr"></span>`SECONDS`  
This variable expands to the number of seconds since the shell was started. Assignment to this variable resets the count to the value assigned, and the expanded value becomes the value assigned plus the number of seconds since the assignment. The number of seconds at shell invocation and the current time are always determined by querying the system clock at one-second resolution. If `SECONDS` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`SHELL`  
This environment variable expands to the full pathname to the shell. If it is not set when the shell starts, Bash assigns to it the full pathname of the current user’s login shell.

<span class="indexterm vr" role="vr"></span>`SHELLOPTS`  
A colon-separated list of enabled shell options. Each word in the list is a valid argument for the `-o` option to the `set` builtin command (see [The Set Builtin](#The-Set-Builtin)). The options appearing in `SHELLOPTS` are those reported as ‘`on`’ by ‘`set -o`’. If this variable is in the environment when Bash starts up, the shell enables each option in the list before reading any startup files. If this variable is exported, child shells will enable each option in the list. This variable is readonly.

<span class="indexterm vr" role="vr"></span>`SHLVL`  
Incremented by one each time a new instance of Bash is started. This is intended to be a count of how deeply your Bash shells are nested.

<span class="indexterm vr" role="vr"></span>`SRANDOM`  
This variable expands to a 32-bit pseudo-random number each time it is referenced. The random number generator is not linear on systems that support `/dev/urandom` or `arc4random`, so each returned number has no relationship to the numbers preceding it. The random number generator cannot be seeded, so assignments to this variable have no effect. If `SRANDOM` is unset, it loses its special properties, even if it is subsequently reset.

<span class="indexterm vr" role="vr"></span>`TIMEFORMAT`  
The value of this parameter is used as a format string specifying how the timing information for pipelines prefixed with the `time` reserved word should be displayed. The ‘`%`’ character introduces an escape sequence that is expanded to a time value or other information. The escape sequences and their meanings are as follows; the brackets denote optional portions.

`%%`  
A literal ‘`%`’.

`%[p][l]R`  
The elapsed time in seconds.

`%[p][l]U`  
The number of CPU seconds spent in user mode.

`%[p][l]S`  
The number of CPU seconds spent in system mode.

`%P`  
The CPU percentage, computed as (%U + %S) / %R.

The optional \<p\> is a digit specifying the precision, the number of fractional digits after a decimal point. A value of 0 causes no decimal point or fraction to be output. `time` prints at most six digits after the decimal point; values of \<p\> greater than 6 are changed to 6. If \<p\> is not specified, `time` prints three digits after the decimal point.

The optional `l` specifies a longer format, including minutes, of the form \<MM\>m\<SS\>.\<FF\>s. The value of \<p\> determines whether or not the fraction is included.

If this variable is not set, Bash acts as if it had the value

    $'\nreal\t%3lR\nuser\t%3lU\nsys\t%3lS'

If the value is null, Bash does not display any timing information. A trailing newline is added when the format string is displayed.

<span class="indexterm vr" role="vr"></span>`TMOUT`  
If set to a value greater than zero, the `read` builtin uses the value as its default timeout (see [Bash Builtins](#Bash-Builtins)). The `select` command (see [Conditional Constructs](#Conditional-Constructs)) terminates if input does not arrive after `TMOUT` seconds when input is coming from a terminal.

In an interactive shell, the value is interpreted as the number of seconds to wait for a line of input after issuing the primary prompt. Bash terminates after waiting for that number of seconds if a complete line of input does not arrive.

<span class="indexterm vr" role="vr"></span>`TMPDIR`  
If set, Bash uses its value as the name of a directory in which Bash creates temporary files for the shell’s use.

<span class="indexterm vr" role="vr"></span>`UID`  
The numeric real user id of the current user. This variable is readonly.
