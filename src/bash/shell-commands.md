---
title: Shell Commands
source_url: https://www.gnu.org/software/bash/manual
source_path: 007-shell-commands.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 70
---

## Shell Commands

commands, shell

A simple shell command such as `echo a b c` consists of the command itself followed by arguments, separated by spaces.

More complex shell commands are composed of simple commands arranged together in a variety of ways: in a pipeline in which the output of one command becomes the input of a second, in a loop or conditional construct, or in some other grouping.

### Reserved Words

reserved words

Reserved words are words that have special meaning to the shell. They are used to begin and end the shell’s compound commands.

The following words are recognized as reserved when unquoted and the first word of a command (see below for exceptions):

|        |        |          |          |            |        |
|--------|--------|----------|----------|------------|--------|
| `if`   | `then` | `elif`   | `else`   | `fi`       | `time` |
| `for`  | `in`   | `until`  | `while`  | `do`       | `done` |
| `case` | `esac` | `coproc` | `select` | `function` |        |
| `{`    | `}`    | `[[`     | `]]`     | `!`        |        |

`in` is recognized as a reserved word if it is the third word of a `case` or `select` command. `in` and `do` are recognized as reserved words if they are the third word in a `for` command.

### Simple Commands

commands, simple

A simple command is the kind of command that’s executed most often. It’s just a sequence of words separated by `blank`s, terminated by one of the shell’s control operators (see [Definitions](#Definitions)). The first word generally specifies a command to be executed, with the rest of the words being that command’s arguments.

The return status (see [Exit Status](#Exit-Status)) of a simple command is its exit status as provided by the POSIX 1003.1 `waitpid` function, or 128+\<n\> if the command was terminated by signal \<n\>.

### Pipelines

pipeline

commands, pipelines

A `pipeline` is a sequence of one or more commands separated by one of the control operators ‘`|`’ or ‘`|&`’.

time

!

command timing

The format for a pipeline is

    [time [-p]] [!] command1 [ | or |& command2 ] …

The output of each command in the pipeline is connected via a pipe to the input of the next command. That is, each command reads the previous command’s output. This connection is performed before any redirections specified by \<command1\>.

If ‘`|&`’ is the pipeline operator, \<command1\>’s standard error, in addition to its standard output, is connected to \<command2\>’s standard input through the pipe; it is shorthand for `2>&1 |`. This implicit redirection of the standard error to the standard output is performed after any redirections specified by \<command1\>, consistent with that shorthand.

If the reserved word `time` precedes the pipeline, Bash prints timing statistics for the pipeline once it finishes. The statistics currently consist of elapsed (wall-clock) time and user and system time consumed by the command’s execution. The `-p` option changes the output format to that specified by POSIX. When the shell is in POSIX mode (see [Bash POSIX Mode](#Bash-POSIX-Mode)), it does not recognize `time` as a reserved word if the next token begins with a ‘`-`’. The value of the `TIMEFORMAT` variable is a format string that specifies how the timing information should be displayed. See [Bash Variables](#Bash-Variables), for a description of the available formats. Providing `time` as a reserved word permits the timing of shell builtins, shell functions, and pipelines. An external `time` command cannot time these easily.

When the shell is in POSIX mode (see [Bash POSIX Mode](#Bash-POSIX-Mode)), you can use `time` by itself as a simple command. In this case, the shell displays the total user and system time consumed by the shell and its children. The `TIMEFORMAT` variable specifies the format of the time information.

If a pipeline is not executed asynchronously (see [Lists](#Lists)), the shell waits for all commands in the pipeline to complete.

Each command in a multi-command pipeline, where pipes are created, is executed in its own subshell, which is a separate process (see [Command Execution Environment](#Command-Execution-Environment)). If the `lastpipe` option is enabled using the `shopt` builtin (see [The Shopt Builtin](#The-Shopt-Builtin)), and job control is not active, the last element of a pipeline may be run by the shell process.

The exit status of a pipeline is the exit status of the last command in the pipeline, unless the `pipefail` option is enabled (see [The Set Builtin](#The-Set-Builtin)). If `pipefail` is enabled, the pipeline’s return status is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands exit successfully. If the reserved word ‘`!`’ precedes the pipeline, the exit status is the logical negation of the exit status as described above. If a pipeline is not executed asynchronously (see [Lists](#Lists)), the shell waits for all commands in the pipeline to terminate before returning a value. The return status of an asynchronous pipeline is 0.

### Lists of Commands

commands, lists

A `list` is a sequence of one or more pipelines separated by one of the operators ‘`;`’, ‘`&`’, ‘`&&`’, or ‘`||`’, and optionally terminated by one of ‘`;`’, ‘`&`’, or a `newline`.

Of these list operators, ‘`&&`’ and ‘`||`’ have equal precedence, followed by ‘`;`’ and ‘`&`’, which have equal precedence.

A sequence of one or more newlines may appear in a `list` to delimit commands, equivalent to a semicolon.

If a command is terminated by the control operator ‘`&`’, the shell executes the command asynchronously in a subshell. This is known as executing the command in the background, and these are referred to as asynchronous commands. The shell does not wait for the command to finish, and the return status is 0 (true). When job control is not active (see [Job Control](#Job-Control)), the standard input for asynchronous commands, in the absence of any explicit redirections, is redirected from `/dev/null`.

Commands separated by a ‘`;`’ are executed sequentially; the shell waits for each command to terminate in turn. The return status is the exit status of the last command executed.

AND and OR lists are sequences of one or more pipelines separated by the control operators ‘`&&`’ and ‘`||`’, respectively. AND and OR lists are executed with left associativity.

An AND list has the form

    command1 && command2

\<command2\> is executed if, and only if, \<command1\> returns an exit status of zero (success).

An OR list has the form

    command1 || command2

\<command2\> is executed if, and only if, \<command1\> returns a non-zero exit status.

The return status of AND and OR lists is the exit status of the last command executed in the list.

### Compound Commands

commands, compound

Compound commands are the shell programming language constructs. Each construct begins with a reserved word or control operator and is terminated by a corresponding reserved word or operator. Any redirections (see [Redirections](#Redirections)) associated with a compound command apply to all commands within that compound command unless explicitly overridden.

In most cases a list of commands in a compound command’s description may be separated from the rest of the command by one or more newlines, and may be followed by a newline in place of a semicolon.

Bash provides looping constructs, conditional commands, and mechanisms to group commands and execute them as a unit.

#### Looping Constructs

commands, looping

Bash supports the following looping constructs.

Note that wherever a ‘`;`’ appears in the description of a command’s syntax, it may be replaced with one or more newlines.

`until`  

until

do

done

The syntax of the `until` command is:

    until test-commands; do consequent-commands; done

Execute \<consequent-commands\> as long as \<test-commands\> has an exit status which is not zero. The return status is the exit status of the last command executed in \<consequent-commands\>, or zero if none was executed.

`while`  

while

The syntax of the `while` command is:

    while test-commands; do consequent-commands; done

Execute \<consequent-commands\> as long as \<test-commands\> has an exit status of zero. The return status is the exit status of the last command executed in \<consequent-commands\>, or zero if none was executed.

`for`  

for

The syntax of the `for` command is:

    for name [ [in words …] ; ] do commands; done

Expand \<words\> (see [Shell Expansions](#Shell-Expansions)), and then execute \<commands\> once for each word in the resultant list, with \<name\> bound to the current word. If ‘`in words`’ is not present, the `for` command executes the \<commands\> once for each positional parameter that is set, as if ‘`in "$@"`’ had been specified (see [Special Parameters](#Special-Parameters)).

The return status is the exit status of the last command that executes. If there are no items in the expansion of \<words\>, no commands are executed, and the return status is zero.

There is an alternate form of the `for` command which is similar to the C language:

    for (( expr1 ; expr2 ; expr3 )) [;] do commands ; done

First, evaluate the arithmetic expression \<expr1\> according to the rules described below (see [Shell Arithmetic](#Shell-Arithmetic)). Then, repeatedly evaluate the arithmetic expression \<expr2\> until it evaluates to zero. Each time \<expr2\> evaluates to a non-zero value, execute \<commands\> and evaluate the arithmetic expression \<expr3\>. If any expression is omitted, it behaves as if it evaluates to 1. The return value is the exit status of the last command in \<commands\> that is executed, or non-zero if any of the expressions is invalid.

Use the `break` and `continue` builtins (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)) to control loop execution.

#### Conditional Constructs

commands, conditional

`if`  

if

then

else

elif

fi

The syntax of the `if` command is:

    if test-commands; then
      consequent-commands;
    [elif more-test-commands; then
      more-consequents;]
    [else alternate-consequents;]
    fi

The \<test-commands\> list is executed, and if its return status is zero, the \<consequent-commands\> list is executed. If \<test-commands\> returns a non-zero status, each `elif` list is executed in turn, and if its exit status is zero, the corresponding \<more-consequents\> is executed and the command completes. If ‘`else alternate-consequents`’ is present, and the final command in the final `if` or `elif` clause has a non-zero exit status, then \<alternate-consequents\> is executed. The return status is the exit status of the last command executed, or zero if no condition tested true.

`case`  

case

in

esac

The syntax of the `case` command is:

    case word in
        [ [(] pattern [| pattern]…) command-list ;;]…
    esac

`case` will selectively execute the \<command-list\> corresponding to the first \<pattern\> that matches \<word\>, proceeding from the first pattern to the last. The match is performed according to the rules described below in [Pattern Matching](#Pattern-Matching). If the `nocasematch` shell option (see the description of `shopt` in [The Shopt Builtin](#The-Shopt-Builtin)) is enabled, the match is performed without regard to the case of alphabetic characters. The ‘`|`’ is used to separate multiple patterns in a pattern list, and the ‘`)`’ operator terminates the pattern list. A pattern list and an associated \<command-list\> is known as a \<clause\>.

Each clause must be terminated with ‘`;;`’, ‘`;&`’, or ‘`;;&`’. The \<word\> undergoes tilde expansion, parameter expansion, command substitution, process substitution, arithmetic expansion, and quote removal (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)) before the shell attempts to match the pattern. Each \<pattern\> undergoes tilde expansion, parameter expansion, command substitution, arithmetic expansion, process substitution, and quote removal.

There may be an arbitrary number of `case` clauses, each terminated by a ‘`;;`’, ‘`;&`’, or ‘`;;&`’. The first pattern that matches determines the command-list that is executed. It’s a common idiom to use ‘`*`’ as the final pattern to define the default case, since that pattern will always match.

Here is an example using `case` in a script that could be used to describe one interesting feature of an animal:

    echo -n "Enter the name of an animal: "
    read ANIMAL
    echo -n "The $ANIMAL has "
    case $ANIMAL in
      horse | dog | cat) echo -n "four";;
      man | kangaroo ) echo -n "two";;
      *) echo -n "an unknown number of";;
    esac
    echo " legs."

If the ‘`;;`’ operator is used, the `case` command completes after the first pattern match. Using ‘`;&`’ in place of ‘`;;`’ causes execution to continue with the \<command-list\> associated with the next clause, if any. Using ‘`;;&`’ in place of ‘`;;`’ causes the shell to test the patterns in the next clause, if any, and execute any associated \<command-list\> if the match succeeds, continuing the case statement execution as if the pattern list had not matched.

The return status is zero if no \<pattern\> matches. Otherwise, the return status is the exit status of the last \<command-list\> executed.

`select`  

select

The `select` construct allows the easy generation of menus. It has almost the same syntax as the `for` command:

    select name [in words …]; do commands; done

First, expand the list of words following `in`, generating a list of items, and print the set of expanded words on the standard error stream, each preceded by a number. If the ‘`in words`’ is omitted, print the positional parameters, as if ‘`in "$@"`’ had been specified. `select` then displays the `PS3` prompt and reads a line from the standard input. If the line consists of a number corresponding to one of the displayed words, then `select` sets the value of \<name\> to that word. If the line is empty, `select` displays the words and prompt again. If `EOF` is read, `select` completes and returns 1. Any other value read causes \<name\> to be set to null. The line read is saved in the variable `REPLY`.

The \<commands\> are executed after each selection until a `break` command is executed, at which point the `select` command completes.

Here is an example that allows the user to pick a filename from the current directory, and displays the name and index of the file selected.

    select fname in *;
    do
        echo you picked $fname \($REPLY\)
        break;
    done

`((…))`  
    (( expression ))

The arithmetic \<expression\> is evaluated according to the rules described below (see [Shell Arithmetic](#Shell-Arithmetic)). The \<expression\> undergoes the same expansions as if it were within double quotes, but unescaped double quote characters in \<expression\> are not treated specially and are removed. Since this can potentially result in empty strings, this command treats those as expressions that evaluate to 0. If the value of the expression is non-zero, the return status is 0; otherwise the return status is 1.

`[[…]]`  

\[\[

\]\]

    [[ expression ]]

Evaluate the conditional expression \<expression\> and return a status of zero (true) or non-zero (false). Expressions are composed of the primaries described below in [Bash Conditional Expressions](#Bash-Conditional-Expressions). The words between the `[[` and `]]` do not undergo word splitting and filename expansion. The shell performs tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, process substitution, and quote removal on those words. Conditional operators such as ‘`-f`’ must be unquoted to be recognized as primaries.

When used with `[[`, the ‘`<`’ and ‘`>`’ operators sort lexicographically using the current locale.

When the ‘`==`’ and ‘`!=`’ operators are used, the string to the right of the operator is considered a pattern and matched according to the rules described below in [Pattern Matching](#Pattern-Matching), as if the `extglob` shell option were enabled. The ‘`=`’ operator is identical to ‘`==`’. If the `nocasematch` shell option (see the description of `shopt` in [The Shopt Builtin](#The-Shopt-Builtin)) is enabled, the match is performed without regard to the case of alphabetic characters. The return value is 0 if the string matches (‘`==`’) or does not match (‘`!=`’) the pattern, and 1 otherwise.

If you quote any part of the pattern, using any of the shell’s quoting mechanisms, the quoted portion is matched literally. This means every character in the quoted portion matches itself, instead of having any special pattern matching meaning.

An additional binary operator, ‘`=~`’, is available, with the same precedence as ‘`==`’ and ‘`!=`’. When you use ‘`=~`’, the string to the right of the operator is considered a POSIX extended regular expression pattern and matched accordingly (using the POSIX `regcomp` and `regexec` interfaces usually described in *regex*(3)). The return value is 0 if the string matches the pattern, and 1 if it does not. If the regular expression is syntactically incorrect, the conditional expression returns 2. If the `nocasematch` shell option (see the description of `shopt` in [The Shopt Builtin](#The-Shopt-Builtin)) is enabled, the match is performed without regard to the case of alphabetic characters.

You can quote any part of the pattern to force the quoted portion to be matched literally instead of as a regular expression (see above). If the pattern is stored in a shell variable, quoting the variable expansion forces the entire pattern to be matched literally.

The match succeeds if the pattern matches any part of the string. If you want to force the pattern to match the entire string, anchor the pattern using the ‘`^`’ and ‘`$`’ regular expression operators.

For example, the following will match a line (stored in the shell variable `line`) if there is a sequence of characters anywhere in the value consisting of any number, including zero, of characters in the `space` character class, immediately followed by zero or one instances of ‘`a`’, then a ‘`b`’:

    [[ $line =~ [[:space:]]*(a)?b ]]

That means values for `line` like ‘`aab`’, ‘`aaaaaab`’, ‘`xaby`’, and ‘`ab`’ will all match, as will a line containing a ‘`b`’ anywhere in its value.

If you want to match a character that’s special to the regular expression grammar (‘`^$|[]()\.*+?`’), it has to be quoted to remove its special meaning. This means that in the pattern ‘`xxx.txt`’, the ‘`.`’ matches any character in the string (its usual regular expression meaning), but in the pattern ‘`"xxx.txt"`’, it can only match a literal ‘`.`’.

Likewise, if you want to include a character in your pattern that has a special meaning to the regular expression grammar, you must make sure it’s not quoted. If you want to anchor a pattern at the beginning or end of the string, for instance, you cannot quote the ‘`^`’ or ‘`$`’ characters using any form of shell quoting.

If you want to match ‘`initial string`’ at the start of a line, the following will work:

    [[ $line =~ ^"initial string" ]]

but this will not:

    [[ $line =~ "^initial string" ]]

because in the second example the ‘`^`’ is quoted and doesn’t have its usual special meaning.

It is sometimes difficult to specify a regular expression properly without using quotes, or to keep track of the quoting used by regular expressions while paying attention to shell quoting and the shell’s quote removal. Storing the regular expression in a shell variable is often a useful way to avoid problems with quoting characters that are special to the shell. For example, the following is equivalent to the pattern used above:

    pattern='[[:space:]]*(a)?b'
    [[ $line =~ $pattern ]]

Shell programmers should take special care with backslashes, since backslashes are used by both the shell and regular expressions to remove the special meaning from the following character. This means that after the shell’s word expansions complete (see [Shell Expansions](#Shell-Expansions)), any backslashes remaining in parts of the pattern that were originally not quoted can remove the special meaning of pattern characters. If any part of the pattern is quoted, the shell does its best to ensure that the regular expression treats those remaining backslashes as literal, if they appeared in a quoted portion.

The following two sets of commands are *not* equivalent:

    pattern='\.'

    [[ . =~ $pattern ]]
    [[ . =~ \. ]]

    [[ . =~ "$pattern" ]]
    [[ . =~ '\.' ]]

The first two matches will succeed, but the second two will not, because in the second two the backslash will be part of the pattern to be matched. In the first two examples, the pattern passed to the regular expression parser is ‘`\.`’. The backslash removes the special meaning from ‘`.`’, so the literal ‘`.`’ matches. In the second two examples, the pattern passed to the regular expression parser has the backslash quoted (e.g., ‘`\\\.`’), which will not match the string, since it does not contain a backslash. If the string in the first examples were anything other than ‘`.`’, say ‘`a`’, the pattern would not match, because the quoted ‘`.`’ in the pattern loses its special meaning of matching any single character.

Bracket expressions in regular expressions can be sources of errors as well, since characters that are normally special in regular expressions lose their special meanings between brackets. However, you can use bracket expressions to match special pattern characters without quoting them, so they are sometimes useful for this purpose.

Though it might seem like a strange way to write it, the following pattern will match a ‘`.`’ in the string:

    [[ . =~ [.] ]]

The shell performs any word expansions before passing the pattern to the regular expression functions, so you can assume that the shell’s quoting takes precedence. As noted above, the regular expression parser will interpret any unquoted backslashes remaining in the pattern after shell expansion according to its own rules. The intention is to avoid making shell programmers quote things twice as much as possible, so shell quoting should be sufficient to quote special pattern characters where that’s necessary.

The array variable `BASH_REMATCH` records which parts of the string matched the pattern. The element of `BASH_REMATCH` with index 0 contains the portion of the string matching the entire regular expression. Substrings matched by parenthesized subexpressions within the regular expression are saved in the remaining `BASH_REMATCH` indices. The element of `BASH_REMATCH` with index \<n\> is the portion of the string matching the \<n\>th parenthesized subexpression.

Bash sets `BASH_REMATCH` in the global scope; declaring it as a local variable will lead to unexpected results.

Expressions may be combined using the following operators, listed in decreasing order of precedence:

`( expression )`  
Returns the value of \<expression\>. This may be used to override the normal precedence of operators.

`! expression`  
True if \<expression\> is false.

`expression1 && expression2`  
True if both \<expression1\> and \<expression2\> are true.

`expression1 || expression2`  
True if either \<expression1\> or \<expression2\> is true.

The `&&` and `||` operators do not evaluate \<expression2\> if the value of \<expression1\> is sufficient to determine the return value of the entire conditional expression.

#### Grouping Commands

commands, grouping

Bash provides two ways to group a list of commands to be executed as a unit. When commands are grouped, redirections may be applied to the entire command list. For example, the output of all the commands in the list may be redirected to a single stream.

`()`  
    ( list )

Placing a list of commands between parentheses forces the shell to create a subshell (see [Command Execution Environment](#Command-Execution-Environment)), and each of the commands in \<list\> is executed in that subshell environment. Since the \<list\> is executed in a subshell, variable assignments do not remain in effect after the subshell completes.

`{}`  

{

}

    { list; }

Placing a list of commands between curly braces causes the list to be executed in the current shell environment. No subshell is created. The semicolon (or newline) following \<list\> is required.

In addition to the creation of a subshell, there is a subtle difference between these two constructs due to historical reasons. The braces are reserved words, so they must be separated from the \<list\> by `blank`s or other shell metacharacters. The parentheses are operators, and are recognized as separate tokens by the shell even if they are not separated from the \<list\> by whitespace.

The exit status of both of these constructs is the exit status of \<list\>.

### Coprocesses

coprocess

A `coprocess` is a shell command preceded by the `coproc` reserved word. A coprocess is executed asynchronously in a subshell, as if the command had been terminated with the ‘`&`’ control operator, with a two-way pipe established between the executing shell and the coprocess.

The syntax for a coprocess is:

    coproc [NAME] command [redirections]

This creates a coprocess named \<NAME\>. \<command\> may be either a simple command (see [Simple Commands](#Simple-Commands)) or a compound command (see [Compound Commands](#Compound-Commands)). \<NAME\> is a shell variable name. If \<NAME\> is not supplied, the default name is `COPROC`.

The recommended form to use for a coprocess is

    coproc NAME { command; }

This form is preferred because simple commands result in the coprocess always being named `COPROC`, and it is simpler to use and more complete than the other compound commands.

There are other forms of coprocesses:

    coproc NAME compound-command
    coproc compound-command
    coproc simple-command

If \<command\> is a compound command, \<NAME\> is optional. The word following `coproc` determines whether that word is interpreted as a variable name: it is interpreted as \<NAME\> if it is not a reserved word that introduces a compound command. If \<command\> is a simple command, \<NAME\> is not allowed; this is to avoid confusion between \<NAME\> and the first word of the simple command.

When the coprocess is executed, the shell creates an array variable (see [Arrays](#Arrays)) named \<NAME\> in the context of the executing shell. The standard output of \<command\> is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to \<NAME\>\[0\]. The standard input of \<command\> is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to \<NAME\>\[1\]. This pipe is established before any redirections specified by the command (see [Redirections](#Redirections)). The file descriptors can be utilized as arguments to shell commands and redirections using standard word expansions. Other than those created to execute command and process substitutions, the file descriptors are not available in subshells.

The process ID of the shell spawned to execute the coprocess is available as the value of the variable `NAME_PID`. The `wait` builtin may be used to wait for the coprocess to terminate.

Since the coprocess is created as an asynchronous command, the `coproc` command always returns success. The return status of a coprocess is the exit status of \<command\>.

### GNU Parallel

There are ways to run commands in parallel that are not built into Bash. GNU Parallel is a tool to do just that.

GNU Parallel, as its name suggests, can be used to build and run commands in parallel. You may run the same command with different arguments, whether they are filenames, usernames, hostnames, or lines read from files. GNU Parallel provides shorthand references to many of the most common operations (input lines, various portions of the input line, different ways to specify the input source, and so on). Parallel can replace `xargs` or feed commands from its input sources to several different instances of Bash.

For a complete description, refer to the GNU Parallel documentation, which is available at <https://www.gnu.org/software/parallel/parallel_tutorial.html>.
