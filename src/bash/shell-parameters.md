---
title: Shell Parameters
source_url: https://www.gnu.org/software/bash/manual
source_path: 009-shell-parameters.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 90
---

## Shell Parameters

parameters

variable, shell

shell variable

A parameter is an entity that stores values. It can be a `name`, a number, or one of the special characters listed below. A variable is a parameter denoted by a `name`. A variable has a `value` and zero or more `attributes`. Attributes are assigned using the `declare` builtin command (see the description of the `declare` builtin in [Bash Builtins](#Bash-Builtins)). The `export` and `readonly` builtins assign specific attributes.

A parameter is set if it has been assigned a value. The null string is a valid value. Once a variable is set, it may be unset only by using the `unset` builtin command.

A variable is assigned to using a statement of the form

    name=[value]

If \<value\> is not given, the variable is assigned the null string. All \<value\>s undergo tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, and quote removal (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)). If the variable has its `integer` attribute set, then \<value\> is evaluated as an arithmetic expression even if the `$((…))` expansion is not used (see [Arithmetic Expansion](#Arithmetic-Expansion)). Word splitting and filename expansion are not performed. Assignment statements may also appear as arguments to the `alias`, `declare`, `typeset`, `export`, `readonly`, and `local` builtin commands (declaration commands). When in POSIX mode (see [Bash POSIX Mode](#Bash-POSIX-Mode)), these builtins may appear in a command after one or more instances of the `command` builtin and retain these assignment statement properties. For example,

    command export var=value

In the context where an assignment statement is assigning a value to a shell variable or array index (see [Arrays](#Arrays)), the ‘`+=`’ operator appends to or adds to the variable’s previous value. This includes arguments to declaration commands such as `declare` that accept assignment statements. When ‘`+=`’ is applied to a variable for which the `integer` attribute has been set, the variable’s current value and \<value\> are each evaluated as arithmetic expressions, and the sum of the results is assigned as the variable’s value. The current value is usually an integer constant, but may be an expression. When ‘`+=`’ is applied to an array variable using compound assignment (see [Arrays](#Arrays)), the variable’s value is not unset (as it is when using ‘`=`’), and new values are appended to the array beginning at one greater than the array’s maximum index (for indexed arrays), or added as additional key-value pairs in an associative array. When applied to a string-valued variable, \<value\> is expanded and appended to the variable’s value.

A variable can be assigned the `nameref` attribute using the `-n` option to the `declare` or `local` builtin commands (see [Bash Builtins](#Bash-Builtins)) to create a nameref, or a reference to another variable. This allows variables to be manipulated indirectly. Whenever the nameref variable is referenced, assigned to, unset, or has its attributes modified (other than using or changing the nameref attribute itself), the operation is actually performed on the variable specified by the nameref variable’s value. A nameref is commonly used within shell functions to refer to a variable whose name is passed as an argument to the function. For instance, if a variable name is passed to a shell function as its first argument, running

    declare -n ref=$1

inside the function creates a local nameref variable `ref` whose value is the variable name passed as the first argument. References and assignments to `ref`, and changes to its attributes, are treated as references, assignments, and attribute modifications to the variable whose name was passed as `$1`.

If the control variable in a `for` loop has the nameref attribute, the list of words can be a list of shell variables, and a name reference is established for each word in the list, in turn, when the loop is executed. Array variables cannot be given the nameref attribute. However, nameref variables can reference array variables and subscripted array variables. Namerefs can be unset using the `-n` option to the `unset` builtin (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)). Otherwise, if `unset` is executed with the name of a nameref variable as an argument, the variable referenced by the nameref variable is unset.

When the shell starts, it reads its environment and creates a shell variable from each environment variable that has a valid name, as described below (see [Environment](#Environment)).

### Positional Parameters

parameters, positional

A positional parameter is a parameter denoted by one or more digits, other than the single digit `0`. Positional parameters are assigned from the shell’s arguments when it is invoked, and may be reassigned using the `set` builtin command. Positional parameter `N` may be referenced as `${N}`, or as `$N` when `N` consists of a single digit. Positional parameters may not be assigned to with assignment statements. The `set` and `shift` builtins are used to set and unset them (see [Shell Builtin Commands](#Shell-Builtin-Commands)). The positional parameters are temporarily replaced when a shell function is executed (see [Shell Functions](#Shell-Functions)).

When a positional parameter consisting of more than a single digit is expanded, it must be enclosed in braces. Without braces, a digit following ‘`$`’ can only refer to one of the first nine positional parameters (\$1\\\$9) or the special parameter \$0 (see below).

### Special Parameters

parameters, special

The shell treats several parameters specially. These parameters may only be referenced; assignment to them is not allowed. Special parameters are denoted by one of the following characters.

<span class="indexterm vr" role="vr"></span>`*`  

\$\*

(\$\*) Expands to the positional parameters, starting from one. When the expansion is not within double quotes, each positional parameter expands to a separate word. In contexts where word expansions are performed, those words are subject to further word splitting and filename expansion. When the expansion occurs within double quotes, it expands to a single word with the value of each parameter separated by the first character of the `IFS` variable. That is, `"$*"` is equivalent to `"$1c$2c…"`, where \<c\> is the first character of the value of the `IFS` variable. If `IFS` is unset, the parameters are separated by spaces. If `IFS` is null, the parameters are joined without intervening separators.

<span class="indexterm vr" role="vr"></span>`@`  

\$@

(\$@) Expands to the positional parameters, starting from one. In contexts where word splitting is performed, this expands each positional parameter to a separate word; if not within double quotes, these words are subject to word splitting. In contexts where word splitting is not performed, such as the value portion of an assignment statement, this expands to a single word with each positional parameter separated by a space. When the expansion occurs within double quotes, and word splitting is performed, each parameter expands to a separate word. That is, `"$@"` is equivalent to `"$1" "$2" …`. If the double-quoted expansion occurs within a word, the expansion of the first parameter is joined with the expansion of the beginning part of the original word, and the expansion of the last parameter is joined with the expansion of the last part of the original word. When there are no positional parameters, `"$@"` and `$@` expand to nothing (i.e., they are removed).

<span class="indexterm vr" role="vr"></span>`#`  

\$#

(\$#) Expands to the number of positional parameters in decimal.

<span class="indexterm vr" role="vr"></span>`?`  

\$?

(\$?) Expands to the exit status of the most recently executed command.

<span class="indexterm vr" role="vr"></span>`-`  

\$-

(\$-, a hyphen.) Expands to the current option flags as specified upon invocation, by the `set` builtin command, or those set by the shell itself (such as the `-i` option).

<span class="indexterm vr" role="vr"></span>`$`  

\$\$

(\$\$) Expands to the process ID of the shell. In a subshell, it expands to the process ID of the invoking shell, not the subshell.

<span class="indexterm vr" role="vr"></span>`!`  

\$!

(\$!) Expands to the process ID of the job most recently placed into the background, whether executed as an asynchronous command or using the `bg` builtin (see [Job Control Builtins](#Job-Control-Builtins)).

<span class="indexterm vr" role="vr"></span>`0`  

\$0

(\$0) Expands to the name of the shell or shell script. This is set at shell initialization. If Bash is invoked with a file of commands (see [Shell Scripts](#Shell-Scripts)), `$0` is set to the name of that file. If Bash is started with the `-c` option (see [Invoking Bash](#Invoking-Bash)), then `$0` is set to the first argument after the string to be executed, if one is present. Otherwise, it is set to the filename used to invoke Bash, as given by argument zero.
