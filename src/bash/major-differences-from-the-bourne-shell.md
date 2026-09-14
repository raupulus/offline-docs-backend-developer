---
title: Major Differences From The Bourne Shell
source_url: https://www.gnu.org/software/bash/manual
source_path: 062-major-differences-from-the-bourne-shell.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 620
---

## Major Differences From The Bourne Shell

Bash implements essentially the same grammar, parameter and variable expansion, redirection, and quoting as the Bourne Shell. Bash uses the POSIX standard as the specification of how these features are to be implemented and how they should behave. There are some differences between the traditional Bourne shell and Bash; this section quickly details the differences of significance. A number of these differences are explained in greater depth in previous sections. This section uses the version of `sh` included in SVR4.2 (the last version of the historical Bourne shell) as the baseline reference.

- Bash is POSIX-conformant, even where the POSIX specification differs from traditional `sh` behavior (see [Bash POSIX Mode](#Bash-POSIX-Mode)).

- Bash has multi-character invocation options (see [Invoking Bash](#Invoking-Bash)).

- The Bash restricted mode is more useful (see [The Restricted Shell](#The-Restricted-Shell)); the SVR4.2 shell restricted mode is too limited.

- Bash has command-line editing (see [Command Line Editing](#Command-Line-Editing)) and the `bind` builtin.

- Bash provides a programmable word completion mechanism (see [Programmable Completion](#Programmable-Completion)), and builtin commands `complete`, `compgen`, and `compopt`, to manipulate it.

- Bash decodes a number of backslash-escape sequences in the prompt string variables (`PS0`, `PS1`, `PS2`, and `PS4`) (see [Controlling the Prompt](#Controlling-the-Prompt)).

- Bash expands and displays the `PS0` prompt string variable.

- Bash runs commands from the `PROMPT_COMMAND` array variable before issuing each primary prompt.

- Bash has command history (see [Bash History Facilities](#Bash-History-Facilities)) and the `history` and `fc` builtins to manipulate it. The Bash history list maintains timestamp information and uses the value of the `HISTTIMEFORMAT` variable to display it.

- Bash implements `csh`-like history expansion (see [History Interaction](#History-Interaction)).

- Bash supports the `$'…'` quoting syntax, which expands ANSI-C backslash-escaped characters in the text between the single quotes (see [ANSI-C Quoting](#ANSI_002dC-Quoting)).

- Bash supports the `$"…"` quoting syntax and performs locale-specific translation of the characters between the double quotes. The `-D`, `--dump-strings`, and `--dump-po-strings` invocation options list the translatable strings found in a script (see [Locale Translation](#Locale-Translation)).

- Bash includes brace expansion (see [Brace Expansion](#Brace-Expansion)) and tilde expansion (see [Tilde Expansion](#Tilde-Expansion)).

- Bash implements command aliases and the `alias` and `unalias` builtins (see [Aliases](#Aliases)).

- Bash implements the `!` reserved word to negate the return value of a pipeline (see [Pipelines](#Pipelines)). This is very useful when an `if` statement needs to act only if a test fails. The Bash ‘`-o pipefail`’ option to `set` will cause a pipeline to return a failure status if any command fails (see [The Set Builtin](#The-Set-Builtin)).

- Bash has the `time` reserved word and command timing (see [Pipelines](#Pipelines)). The display of the timing statistics may be controlled with the `TIMEFORMAT` variable.

- Bash provides coprocesses and the `coproc` reserved word (see [Coprocesses](#Coprocesses)).

- Bash implements the `for (( expr1 ; expr2 ; expr3 ))` arithmetic for command, similar to the C language (see [Looping Constructs](#Looping-Constructs)).

- Bash includes the `select` compound command, which allows the generation of simple menus (see [Conditional Constructs](#Conditional-Constructs)).

- Bash includes the `[[` compound command, which makes conditional testing part of the shell grammar (see [Conditional Constructs](#Conditional-Constructs)), including optional regular expression matching.

- Bash provides optional case-insensitive matching for the `case` and `[[` constructs (see [Conditional Constructs](#Conditional-Constructs)).

- Bash provides additional `case` statement action list terminators: ‘`;&`’ and ‘`;;&`’ (see [Conditional Constructs](#Conditional-Constructs)).

- Bash provides shell arithmetic, the `((` compound command (see [Conditional Constructs](#Conditional-Constructs)), the `let` builtin, and arithmetic expansion (see [Shell Arithmetic](#Shell-Arithmetic)).

- Bash has one-dimensional array variables (see [Arrays](#Arrays)), and the appropriate variable expansions and assignment syntax to use them. Several of the Bash builtins take options to act on arrays. Bash provides a number of built-in array variables.

- Variables present in the shell’s initial environment are automatically exported to child processes (see [Command Execution Environment](#Command-Execution-Environment)). The Bourne shell does not normally do this unless the variables are explicitly marked using the `export` command.

- Bash can expand positional parameters beyond `$9` using `${num}` (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)).

- Bash supports the ‘`+=`’ assignment operator, which appends to the value of the variable named on the left hand side (see [Shell Parameters](#Shell-Parameters)).

- Bash includes the POSIX pattern removal ‘`%`’, ‘`#`’, ‘`%%`’ and ‘`##`’ expansions to remove leading or trailing substrings from variable values (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)).

- The expansion `${#xx}`, which returns the length of `${xx}`, is supported (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)).

- The expansion `${var:`\<offset\>`[:`\<length\>`]}`, which expands to the substring of `var`’s value of length \<length\>, beginning at \<offset\>, is present (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)).

- The expansion `${var/[/]`\<pattern\>`[/`\<replacement\>`]}`, which matches \<pattern\> and replaces it with \<replacement\> in the value of \<var\>, is available (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)), with a mechanism to use the matched text in \<replacement\>.

- The expansion `${!prefix*}` expansion, which expands to the names of all shell variables whose names begin with \<prefix\>, is available (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)).

- Bash has indirect variable expansion using `${!word}` (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)) and implements the `nameref` variable attribute for automatic indirect variable expansion.

- Bash includes a set of parameter transformation word expansions of the form `${var@X}`, where ‘`X`’ specifies the transformation (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)).

- The POSIX `$()` form of command substitution is implemented (see [Command Substitution](#Command-Substitution)), and preferred to the Bourne shell’s ``` `` ``` (which is also implemented for backwards compatibility).

- Bash implements a variant of command substitution that runs the enclosed command in the current shell execution environment: `${ command;}` or `${|command;}` (see [Command Substitution](#Command-Substitution)).

- Bash has process substitution (see [Process Substitution](#Process-Substitution)).

- Bash automatically assigns variables that provide information about the current user (`UID`, `EUID`, and `GROUPS`), the current host (`HOSTTYPE`, `OSTYPE`, `MACHTYPE`, and `HOSTNAME`), and the instance of Bash that is running (`BASH`, `BASH_VERSION`, and `BASH_VERSINFO`). See [Bash Variables](#Bash-Variables), for details.

- Bash uses many variables to provide functionality and customize shell behavior that the Bourne shell does not. Examples include `RANDOM`, `SRANDOM`, `EPOCHSECONDS`, `EPOCHREALTIME`, `TIMEFORMAT`, `BASHPID`, `BASH_XTRACEFD`, `GLOBIGNORE`, `HISTIGNORE`, and `BASH_VERSION`. See [Bash Variables](#Bash-Variables), for a complete list.

- Bash uses the `GLOBSORT` shell variable to control how to sort the results of filename expansion (see [Filename Expansion](#Filename-Expansion)).

- Bash uses the `IFS` variable to split only the results of expansion, not all words (see [Word Splitting](#Word-Splitting)). This closes a longstanding shell security hole.

- The filename expansion bracket expression code uses ‘`!`’ and ‘`^`’ to negate the set of characters between the brackets (see [Filename Expansion](#Filename-Expansion)). The Bourne shell uses only ‘`!`’.

- Bash implements the full set of POSIX filename expansion operators, including character classes, equivalence classes, and collating symbols (see [Filename Expansion](#Filename-Expansion)).

- Bash implements extended pattern matching features when the `extglob` shell option is enabled (see [Pattern Matching](#Pattern-Matching)).

- The `globstar` shell option extends filename expansion to recursively scan directories and subdirectories for matching filenames (see [Pattern Matching](#Pattern-Matching)).

- It is possible to have a variable and a function with the same name; `sh` does not separate the two name spaces.

- Bash functions are permitted to have local variables using the `local` builtin, and thus users can write useful recursive functions (see [Bash Builtins](#Bash-Builtins)).

- Bash performs filename expansion on filenames specified as operands to input and output redirection operators (see [Redirections](#Redirections)).

- Bash contains the ‘`<>`’ redirection operator, allowing a file to be opened for both reading and writing, and the ‘`&>`’ redirection operator, for directing standard output and standard error to the same file (see [Redirections](#Redirections)).

- Bash includes the ‘`<<<`’ redirection operator, allowing a string to be used as the standard input to a command (see [Redirections](#Redirections)).

- Bash implements the ‘`[n]<&word`’ and ‘`[n]>&word`’ redirection operators, which move one file descriptor to another.

- Bash treats a number of filenames specially when they are used in redirection operators (see [Redirections](#Redirections)).

- Bash provides the {\<var\>}\<\<word\> capability to have the shell allocate file descriptors for redirections and assign them to \<var\> (see [Redirections](#Redirections)). This works with multiple redirection operators.

- Bash can open network connections to arbitrary machines and services with the redirection operators (see [Redirections](#Redirections)).

- The `noclobber` option is available to avoid overwriting existing files with output redirection (see [The Set Builtin](#The-Set-Builtin)). The ‘`>|`’ redirection operator may be used to override `noclobber`.

- Variable assignments preceding commands affect only that command, even builtins and functions (see [Environment](#Environment)). In `sh`, all variable assignments preceding commands are global unless the command is executed from the file system.

- Bash includes a number of features to support a separate debugger for shell scripts: variables (`BASH_ARGC`, `BASH_ARGV`, `BASH_LINENO`, `BASH_SOURCE`), the `DEBUG`, `RETURN`, and `ERR` traps, ‘`declare -F`’, and the `caller` builtin.

- Bash implements a `csh`-like directory stack, and provides the `pushd`, `popd`, and `dirs` builtins to manipulate it (see [The Directory Stack](#The-Directory-Stack)). Bash also makes the directory stack visible as the value of the `DIRSTACK` shell variable.

- Bash allows a function to override a builtin with the same name, and provides access to that builtin’s functionality within the function via the `builtin` and `command` builtins (see [Bash Builtins](#Bash-Builtins)).

- Bash includes the `caller` builtin (see [Bash Builtins](#Bash-Builtins)), which displays the context of any active subroutine call (a shell function or a script executed with the `.` or `source` builtins). This supports the Bash debugger.

- The Bash `cd` and `pwd` builtins (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)) each take `-L` and `-P` options to switch between logical and physical modes.

- The `command` builtin allows selectively skipping shell functions when performing command lookup (see [Bash Builtins](#Bash-Builtins)).

- Bash uses the `declare` builtin to modify the full set of variable and function attributes, and to assign values to variables.

- The `disown` builtin can remove a job from the internal shell job table (see [Job Control Builtins](#Job-Control-Builtins)) or suppress sending `SIGHUP` to a job when the shell exits as the result of a `SIGHUP`.

- The `enable` builtin (see [Bash Builtins](#Bash-Builtins)) can enable or disable individual builtins and implements support for dynamically loading builtin commands from shared objects.

- The Bash `exec` builtin takes additional options that allow users to control the contents of the environment passed to the executed command, and what the zeroth argument to the command is to be (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)).

- Shell functions may be exported to children via the environment using `export -f` (see [Shell Functions](#Shell-Functions)).

- The Bash `export` and `readonly` builtins (see [Bourne Shell Builtins](#Bourne-Shell-Builtins) can take a `-f` option to act on shell functions, a `-p` option to display variables with various attributes set in a format that can be used as shell input, a `-n` option to remove various variable attributes, and ‘`name=value`’ arguments to set variable attributes and values simultaneously.

- The Bash `hash` builtin allows a name to be associated with an arbitrary filename, even when that filename cannot be found by searching the `$PATH`, using ‘`hash -p`’ (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)).

- Bash includes a `help` builtin for quick reference to shell facilities (see [Bash Builtins](#Bash-Builtins)).

- Bash includes the `mapfile` builtin to quickly read the contents of a file into an indexed array variable (see [Bash Builtins](#Bash-Builtins)).

- The `printf` builtin is available to display formatted output (see [Bash Builtins](#Bash-Builtins)), and has additional custom format specifiers and an option to assign the formatted output directly to a shell variable.

- The Bash `read` builtin (see [Bash Builtins](#Bash-Builtins)) will read a line ending in ‘`\`’ with the `-r` option, and will use the `REPLY` variable as a default if no non-option arguments are supplied.

- The `read` builtin (see [Bash Builtins](#Bash-Builtins)) accepts a prompt string with the `-p` option and will use Readline to obtain the line when given the `-e` or `-E` options, with the ability to insert text into the line using the `-i` option. The `read` builtin also has additional options to control input: the `-s` option will turn off echoing of input characters as they are read, the `-t` option will allow `read` to time out if input does not arrive within a specified number of seconds, the `-n` option will allow reading only a specified number of characters rather than a full line, and the `-d` option will read until a particular character rather than newline.

- The `return` builtin may be used to abort execution of scripts executed with the `.` or `source` builtins (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)).

- Bash has much more optional behavior controllable with the `set` builtin (see [The Set Builtin](#The-Set-Builtin)).

- The `-x` (`xtrace`) option displays commands other than simple commands when performing an execution trace (see [The Set Builtin](#The-Set-Builtin)).

- Bash includes the `shopt` builtin, for finer control of shell optional capabilities (see [The Shopt Builtin](#The-Shopt-Builtin)), and allows these options to be set and unset at shell invocation (see [Invoking Bash](#Invoking-Bash)).

- The `test` builtin (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)) is slightly different, as it implements the POSIX algorithm, which specifies the behavior based on the number of arguments.

- The `trap` builtin (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)) allows a `DEBUG` pseudo-signal specification, similar to `EXIT`. Commands specified with a `DEBUG` trap are executed before every simple command, `for` command, `case` command, `select` command, every arithmetic `for` command, and before the first command executes in a shell function. The `DEBUG` trap is not inherited by shell functions unless the function has been given the `trace` attribute or the `functrace` option has been enabled using the `shopt` builtin. The `extdebug` shell option has additional effects on the `DEBUG` trap.

  The `trap` builtin (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)) allows an `ERR` pseudo-signal specification, similar to `EXIT` and `DEBUG`. Commands specified with an `ERR` trap are executed after a simple command fails, with a few exceptions. The `ERR` trap is not inherited by shell functions unless the `-o errtrace` option to the `set` builtin is enabled.

  The `trap` builtin (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)) allows a `RETURN` pseudo-signal specification, similar to `EXIT` and `DEBUG`. Commands specified with a `RETURN` trap are executed before execution resumes after a shell function or a shell script executed with `.` or `source` returns. The `RETURN` trap is not inherited by shell functions unless the function has been given the `trace` attribute or the `functrace` option has been enabled using the `shopt` builtin.

- The Bash `type` builtin is more extensive and gives more information about the names it finds (see [Bash Builtins](#Bash-Builtins)).

- The `ulimit` builtin provides control over many more per-process resources (see [Bash Builtins](#Bash-Builtins)).

- The Bash `umask` builtin uses the `-p` option to display the output in the form of a `umask` command that may be reused as input (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)).

- The Bash `wait` builtin has a `-n` option to wait for the next child to exit, possibly selecting from a list of supplied jobs, and the `-p` option to store information about a terminated child process in a shell variable.

- The SVR4.2 shell behaves differently when invoked as `jsh` (it turns on job control).

- The SVR4.2 shell has two privilege-related builtins (`mldmode` and `priv`) not present in Bash.

- Bash does not have the `stop` or `newgrp` builtins.

- Bash does not use the `SHACCT` variable or perform shell accounting.

- The SVR4.2 `sh` uses a `TIMEOUT` variable like Bash uses `TMOUT`.

More features unique to Bash may be found in [Bash Features](#Bash-Features).
