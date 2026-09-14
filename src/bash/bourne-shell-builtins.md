---
title: Bourne Shell Builtins
source_url: https://www.gnu.org/software/bash/manual
source_path: 015-bourne-shell-builtins.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 150
---

## Bourne Shell Builtins

The following shell builtin commands are inherited from the Bourne Shell. These commands are implemented as specified by the POSIX standard.

`: (a colon)`  

:

    : [arguments]

Do nothing beyond expanding \<arguments\> and performing redirections. The return status is zero.

`. (a period)`  

.

    . [-p path] filename [arguments]

The `.` command reads and execute commands from the \<filename\> argument in the current shell context.

If \<filename\> does not contain a slash, `.` searches for it. If `-p` is supplied, `.` treats \<path\> as a colon-separated list of directories in which to find \<filename\>; otherwise, `.` uses the directories in `PATH` to find \<filename\>. \<filename\> does not need to be executable. When Bash is not in POSIX mode, it searches the current directory if \<filename\> is not found in `$PATH`, but does not search the current directory if `-p` is supplied. If the `sourcepath` option (see [The Shopt Builtin](#The-Shopt-Builtin)) is turned off, `.` does not search `PATH`.

If any \<arguments\> are supplied, they become the positional parameters when \<filename\> is executed. Otherwise the positional parameters are unchanged.

If the `-T` option is enabled, `.` inherits any trap on `DEBUG`; if it is not, any `DEBUG` trap string is saved and restored around the call to `.`, and `.` unsets the `DEBUG` trap while it executes. If `-T` is not set, and the sourced file changes the `DEBUG` trap, the new value persists after `.` completes. The return status is the exit status of the last command executed from \<filename\>, or zero if no commands are executed. If \<filename\> is not found, or cannot be read, the return status is non-zero. This builtin is equivalent to `source`.

`break`  

break

    break [n]

Exit from a `for`, `while`, `until`, or `select` loop. If \<n\> is supplied, `break` exits the \<n\>th enclosing loop. \<n\> must be greater than or equal to 1. The return status is zero unless \<n\> is not greater than or equal to 1.

`cd`  

cd

    cd [-L] [-@] [directory]
    cd -P [-e] [-@] [directory]

Change the current working directory to \<directory\>. If \<directory\> is not supplied, the value of the `HOME` shell variable is used as \<directory\>. If the shell variable `CDPATH` exists, and \<directory\> does not begin with a slash, `cd` uses it as a search path: `cd` searches each directory name in `CDPATH` for \<directory\>, with alternative directory names in `CDPATH` separated by a colon (‘`:`’). A null directory name in `CDPATH` means the same thing as the current directory.

The `-P` option means not to follow symbolic links: symbolic links are resolved while `cd` is traversing \<directory\> and before processing an instance of `..` in \<directory\>.

By default, or when the `-L` option is supplied, symbolic links in \<directory\> are resolved after `cd` processes an instance of `..` in \<directory\>.

If `..` appears in \<directory\>, `cd` processes it by removing the immediately preceding pathname component, back to a slash or the beginning of \<directory\>, and verifying that the portion of \<directory\> it has processed to that point is still a valid directory name after removing the pathname component. If it is not a valid directory name, `cd` returns a non-zero status.

If the `-e` option is supplied with `-P` and `cd` cannot successfully determine the current working directory after a successful directory change, it returns a non-zero status.

On systems that support it, the `-@` option presents the extended attributes associated with a file as a directory.

If \<directory\> is ‘`-`’, it is converted to `$OLDPWD` before attempting the directory change.

If `cd` uses a non-empty directory name from `CDPATH`, or if ‘`-`’ is the first argument, and the directory change is successful, `cd` writes the absolute pathname of the new working directory to the standard output.

If the directory change is successful, `cd` sets the value of the `PWD` environment variable to the new directory name, and sets the `OLDPWD` environment variable to the value of the current working directory before the change.

The return status is zero if the directory is successfully changed, non-zero otherwise.

`continue`  

continue

    continue [n]

`continue` resumes the next iteration of an enclosing `for`, `while`, `until`, or `select` loop. If \<n\> is supplied, Bash resumes the execution of the \<n\>th enclosing loop. \<n\> must be greater than or equal to 1. The return status is zero unless \<n\> is not greater than or equal to 1.

`eval`  

eval

    eval [arguments]

The \<arguments\> are concatenated together into a single command, separated by spaces. Bash then reads and executes this command and returns its exit status as the exit status of `eval`. If there are no arguments or only empty arguments, the return status is zero.

`exec`  

exec

    exec [-cl] [-a name] [command [arguments]]

If \<command\> is supplied, it replaces the shell without creating a new process. \<command\> cannot be a shell builtin or function. The \<arguments\> become the arguments to \<command\> If the `-l` option is supplied, the shell places a dash at the beginning of the zeroth argument passed to \<command\>. This is what the `login` program does. The `-c` option causes \<command\> to be executed with an empty environment. If `-a` is supplied, the shell passes \<name\> as the zeroth argument to \<command\>.

If \<command\> cannot be executed for some reason, a non-interactive shell exits, unless the `execfail` shell option is enabled. In that case, it returns a non-zero status. An interactive shell returns a non-zero status if the file cannot be executed. A subshell exits unconditionally if `exec` fails.

If \<command\> is not specified, redirections may be used to affect the current shell environment. If there are no redirection errors, the return status is zero; otherwise the return status is non-zero.

`exit`  

exit

    exit [n]

Exit the shell, returning a status of \<n\> to the shell’s parent. If \<n\> is omitted, the exit status is that of the last command executed. Any trap on `EXIT` is executed before the shell terminates.

`export`  

export

    export [-fn] [-p] [name[=value]]

Mark each \<name\> to be passed to subsequently executed commands in the environment. If the `-f` option is supplied, the \<name\>s refer to shell functions; otherwise the names refer to shell variables.

The `-n` option means to unexport each name: no longer mark it for export. If no \<name\>s are supplied, or if only the `-p` option is given, `export` displays a list of names of all exported variables on the standard output. Using `-p` and `-f` together displays exported functions. The `-p` option displays output in a form that may be reused as input.

`export` allows the value of a variable to be set at the same time it is exported or unexported by following the variable name with =\<value\>. This sets the value of the variable is to \<value\> while modifying the export attribute.

The return status is zero unless an invalid option is supplied, one of the names is not a valid shell variable name, or `-f` is supplied with a name that is not a shell function.

`false`  

false

    false

Does nothing; returns a non-zero status.

`getopts`  

getopts

    getopts optstring name [arg …]

`getopts` is used by shell scripts or functions to parse positional parameters and obtain options and their arguments. \<optstring\> contains the option characters to be recognized; if a character is followed by a colon, the option is expected to have an argument, which should be separated from it by whitespace. The colon (‘`:`’) and question mark (‘`?`’) may not be used as option characters.

Each time it is invoked, `getopts` places the next option in the shell variable \<name\>, initializing \<name\> if it does not exist, and the index of the next argument to be processed into the variable `OPTIND`. `OPTIND` is initialized to 1 each time the shell or a shell script is invoked. When an option requires an argument, `getopts` places that argument into the variable `OPTARG`.

The shell does not reset `OPTIND` automatically; it must be manually reset between multiple calls to `getopts` within the same shell invocation to use a new set of parameters.

When it reaches the end of options, `getopts` exits with a return value greater than zero. `OPTIND` is set to the index of the first non-option argument, and \<name\> is set to ‘`?`’.

`getopts` normally parses the positional parameters, but if more arguments are supplied as \<arg\> values, `getopts` parses those instead.

`getopts` can report errors in two ways. If the first character of \<optstring\> is a colon, `getopts` uses *silent* error reporting. In normal operation, `getopts` prints diagnostic messages when it encounters invalid options or missing option arguments. If the variable `OPTERR` is set to 0, `getopts` does not display any error messages, even if the first character of `optstring` is not a colon.

If `getopts` detects an invalid option, it places ‘`?`’ into \<name\> and, if not silent, prints an error message and unsets `OPTARG`. If `getopts` is silent, it assigns the option character found to `OPTARG` and does not print a diagnostic message.

If a required argument is not found, and `getopts` is not silent, it sets the value of \<name\> to a question mark (‘`?`’), unsets `OPTARG`, and prints a diagnostic message. If `getopts` is silent, it sets the value of \<name\> to a colon (‘`:`’), and sets `OPTARG` to the option character found.

`getopts` returns true if an option, specified or unspecified, is found. It returns false when it encounters the end of options or if an error occurs.

`hash`  

hash

    hash [-r] [-p filename] [-dt] [name]

Each time `hash` is invoked, it remembers the full filenames of the commands specified as \<name\> arguments, so they need not be searched for on subsequent invocations. The commands are found by searching through the directories listed in `$PATH`. Any previously-remembered filename associated with \<name\> is discarded. The `-p` option inhibits the path search, and `hash` uses \<filename\> as the location of \<name\>.

The `-r` option causes the shell to forget all remembered locations. Assigning to the `PATH` variable also clears all hashed filenames. The `-d` option causes the shell to forget the remembered location of each \<name\>.

If the `-t` option is supplied, `hash` prints the full pathname corresponding to each \<name\>. If multiple \<name\> arguments are supplied with `-t`, `hash` prints each \<name\> before the corresponding hashed full path. The `-l` option displays output in a format that may be reused as input.

If no arguments are given, or if only `-l` is supplied, `hash` prints information about remembered commands. The `-t`, `-d`, and `-p` options (the options that act on the \<name\> arguments) are mutually exclusive. Only one will be active. If more than one is supplied, `-t` has higher priority than `-p`, and both have higher priority than `-d`.

The return status is zero unless a \<name\> is not found or an invalid option is supplied.

`pwd`  

pwd

    pwd [-LP]

Print the absolute pathname of the current working directory. If the `-P` option is supplied, or the `-o physical` option to the `set` builtin (see [The Set Builtin](#The-Set-Builtin)) is enabled, the pathname printed will not contain symbolic links. If the `-L` option is supplied, the pathname printed may contain symbolic links. The return status is zero unless an error is encountered while determining the name of the current directory or an invalid option is supplied.

`readonly`  

readonly

    readonly [-aAf] [-p] [name[=value]] …

Mark each \<name\> as readonly. The values of these names may not be changed by subsequent assignment or unset. If the `-f` option is supplied, each \<name\> refers to a shell function. The `-a` option means each \<name\> refers to an indexed array variable; the `-A` option means each \<name\> refers to an associative array variable. If both options are supplied, `-A` takes precedence. If no \<name\> arguments are supplied, or if the `-p` option is supplied, print a list of all readonly names. The other options may be used to restrict the output to a subset of the set of readonly names. The `-p` option displays output in a format that may be reused as input.

`readonly` allows the value of a variable to be set at the same time the readonly attribute is changed by following the variable name with =\<value\>. This sets the value of the variable is to \<value\> while modifying the readonly attribute.

The return status is zero unless an invalid option is supplied, one of the \<name\> arguments is not a valid shell variable or function name, or the `-f` option is supplied with a name that is not a shell function.

`return`  

return

    return [n]

Stop executing a shell function or sourced file and return the value \<n\> to its caller. If \<n\> is not supplied, the return value is the exit status of the last command executed. If `return` is executed by a trap handler, the last command used to determine the status is the last command executed before the trap handler. If `return` is executed during a `DEBUG` trap, the last command used to determine the status is the last command executed by the trap handler before `return` was invoked.

When `return` is used to terminate execution of a script being executed with the `.` (`source`) builtin, it returns either \<n\> or the exit status of the last command executed within the script as the exit status of the script. If \<n\> is supplied, the return value is its least significant 8 bits.

Any command associated with the `RETURN` trap is executed before execution resumes after the function or script.

The return status is non-zero if `return` is supplied a non-numeric argument or is used outside a function and not during the execution of a script by `.` or `source`.

`shift`  

shift

    shift [n]

Shift the positional parameters to the left by \<n\>: the positional parameters from \<n\>+1 … `$#` are renamed to `$1` … `$#`-\<n\>. Parameters represented by the numbers `$#` down to `$#`-\<n\>+1 are unset. \<n\> must be a non-negative number less than or equal to `$#`. If \<n\> is not supplied, it is assumed to be 1. If \<n\> is zero or greater than `$#`, the positional parameters are not changed. The return status is zero unless \<n\> is greater than `$#` or less than zero, non-zero otherwise.

`test`; `[`  

test

\[

    test expr

Evaluate a conditional expression \<expr\> and return a status of 0 (true) or 1 (false). Each operator and operand must be a separate argument. Expressions are composed of the primaries described below in [Bash Conditional Expressions](#Bash-Conditional-Expressions). `test` does not accept any options, nor does it accept and ignore an argument of `--` as signifying the end of options. When using the `[` form, the last argument to the command must be a `]`.

Expressions may be combined using the following operators, listed in decreasing order of precedence. The evaluation depends on the number of arguments; see below. `test` uses operator precedence when there are five or more arguments.

`! expr`  
True if \<expr\> is false.

`( expr )`  
Returns the value of \<expr\>. This may be used to override normal operator precedence.

`expr1 -a expr2`  
True if both \<expr1\> and \<expr2\> are true.

`expr1 -o expr2`  
True if either \<expr1\> or \<expr2\> is true.

The `test` and `[` builtins evaluate conditional expressions using a set of rules based on the number of arguments.

0 arguments  
The expression is false.

1 argument  
The expression is true if, and only if, the argument is not null.

2 arguments  
If the first argument is ‘`!`’, the expression is true if and only if the second argument is null. If the first argument is one of the unary conditional operators (see [Bash Conditional Expressions](#Bash-Conditional-Expressions)), the expression is true if the unary test is true. If the first argument is not a valid unary operator, the expression is false.

3 arguments  
The following conditions are applied in the order listed.

1.  If the second argument is one of the binary conditional operators (see [Bash Conditional Expressions](#Bash-Conditional-Expressions)), the result of the expression is the result of the binary test using the first and third arguments as operands. The ‘`-a`’ and ‘`-o`’ operators are considered binary operators when there are three arguments.

2.  If the first argument is ‘`!`’, the value is the negation of the two-argument test using the second and third arguments.

3.  If the first argument is exactly ‘`(`’ and the third argument is exactly ‘`)`’, the result is the one-argument test of the second argument.

4.  Otherwise, the expression is false.

4 arguments  
The following conditions are applied in the order listed.

1.  If the first argument is ‘`!`’, the result is the negation of the three-argument expression composed of the remaining arguments.

2.  If the first argument is exactly ‘`(`’ and the fourth argument is exactly ‘`)`’, the result is the two-argument test of the second and third arguments.

3.  Otherwise, the expression is parsed and evaluated according to precedence using the rules listed above.

5 or more arguments  
The expression is parsed and evaluated according to precedence using the rules listed above.

If the shell is in POSIX mode, or if the expression is part of the `[[` command, the ‘`<`’ and ‘`>`’ operators sort using the current locale. If the shell is not in POSIX mode, the `test` and ‘`[`’ commands sort lexicographically using ASCII ordering.

The historical operator-precedence parsing with 4 or more arguments can lead to ambiguities when it encounters strings that look like primaries. The POSIX standard has deprecated the `-a` and `-o` primaries and enclosing expressions within parentheses. Scripts should no longer use them. It’s much more reliable to restrict test invocations to a single primary, and to replace uses of `-a` and `-o` with the shell’s `&&` and `||` list operators. For example, use

    test -n string1 && test -n string2

instead of

    test -n string1 -a -n string2

`times`  

times

    times

Print out the user and system times used by the shell and its children. The return status is zero.

`trap`  

trap

    trap [-lpP] [action] [sigspec …]

The \<action\> is a command that is read and executed when the shell receives any of the signals \<sigspec\>. If \<action\> is absent (and there is a single \<sigspec\>) or equal to ‘`-`’, each specified \<sigspec\>’s disposition is reset to the value it had when the shell was started. If \<action\> is the null string, then the signal specified by each \<sigspec\> is ignored by the shell and commands it invokes.

If no arguments are supplied, `trap` prints the actions associated with each trapped signal as a set of `trap` commands that can be reused as shell input to restore the current signal dispositions.

If \<action\> is not present and `-p` has been supplied, `trap` displays the trap commands associated with each \<sigspec\>, or, if no \<sigspec\>s are supplied, for all trapped signals, as a set of `trap` commands that can be reused as shell input to restore the current signal dispositions. The `-P` option behaves similarly, but displays only the actions associated with each \<sigspec\> argument. `-P` requires at least one \<sigspec\> argument. The `-P` or `-p` options may be used in a subshell environment (e.g., command substitution) and, as long as they are used before `trap` is used to change a signal’s handling, will display the state of its parent’s traps.

The `-l` option prints a list of signal names and their corresponding numbers. Each \<sigspec\> is either a signal name or a signal number. Signal names are case insensitive and the `SIG` prefix is optional. If `-l` is supplied with no \<sigspec\> arguments, it prints a list of valid signal names.

If a \<sigspec\> is `0` or `EXIT`, \<action\> is executed when the shell exits. If a \<sigspec\> is `DEBUG`, \<action\> is executed before every simple command, `for` command, `case` command, `select` command, (( arithmetic command, \[\[ conditional command, arithmetic `for` command, and before the first command executes in a shell function. Refer to the description of the `extdebug` shell option (see [The Shopt Builtin](#The-Shopt-Builtin)) for details of its effect on the `DEBUG` trap. If a \<sigspec\> is `RETURN`, \<action\> is executed each time a shell function or a script executed with the `.` or `source` builtins finishes executing.

If a \<sigspec\> is `ERR`, \<action\> is executed whenever a pipeline (which may consist of a single simple command), a list, or a compound command returns a non-zero exit status, subject to the following conditions. The `ERR` trap is not executed if the failed command is part of the command list immediately following an `until` or `while` reserved word, part of the test following the `if` or `elif` reserved words, part of a command executed in a `&&` or `||` list except the command following the final `&&` or `||`, any command in a pipeline but the last, (subject to the state of the `pipefail` shell option), or if the command’s return status is being inverted using `!`. These are the same conditions obeyed by the `errexit` (`-e`) option.

When the shell is not interactive, signals ignored upon entry to a non-interactive shell cannot be trapped or reset. Interactive shells permit trapping signals ignored on entry. Trapped signals that are not being ignored are reset to their original values in a subshell or subshell environment when one is created.

The return status is zero unless a \<sigspec\> does not specify a valid signal; non-zero otherwise.

`true`  

true

    true

Does nothing, returns a 0 status.

`umask`  

umask

    umask [-p] [-S] [mode]

Set the shell process’s file creation mask to \<mode\>. If \<mode\> begins with a digit, it is interpreted as an octal number; if not, it is interpreted as a symbolic mode mask similar to that accepted by the `chmod` command. If \<mode\> is omitted, `umask` prints the current value of the mask. If the `-S` option is supplied without a \<mode\> argument, `umask` prints the mask in a symbolic format; the default output is an octal number. If the `-p` option is supplied, and \<mode\> is omitted, the output is in a form that may be reused as input. The return status is zero if the mode is successfully changed or if no \<mode\> argument is supplied, and non-zero otherwise.

Note that when the mode is interpreted as an octal number, each number of the umask is subtracted from `7`. Thus, a umask of `022` results in permissions of `755`.

`unset`  

unset

    unset [-fnv] [name]

Remove each variable or function \<name\>. If the `-v` option is given, each \<name\> refers to a shell variable and that variable is removed. If the `-f` option is given, the \<name\>s refer to shell functions, and the function definition is removed. If the `-n` option is supplied, and \<name\> is a variable with the `nameref` attribute, \<name\> will be unset rather than the variable it references. `-n` has no effect if the `-f` option is supplied. If no options are supplied, each \<name\> refers to a variable; if there is no variable by that name, a function with that name, if any, is unset. Readonly variables and functions may not be unset. When variables or functions are removed, they are also removed from the environment passed to subsequent commands. Some shell variables may not be unset. Some shell variables lose their special behavior if they are unset; such behavior is noted in the description of the individual variables. The return status is zero unless a \<name\> is readonly or may not be unset.
