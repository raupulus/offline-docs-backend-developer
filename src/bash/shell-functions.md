---
title: Shell Functions
source_url: https://www.gnu.org/software/bash/manual
source_path: 008-shell-functions.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 80
---

## Shell Functions

shell function

functions, shell

Shell functions are a way to group commands for later execution using a single name for the group. They are executed just like a "regular" simple command. When the name of a shell function is used as a simple command name, the shell executes the list of commands associated with that function name. Shell functions are executed in the current shell context; there is no new process created to interpret them.

Functions are declared using this syntax: <span class="indexterm rw" role="rw"></span>

    fname () compound-command [ redirections ]

or

    function fname [()] compound-command [ redirections ]

This defines a shell function named \<fname\>. The reserved word `function` is optional. If the `function` reserved word is supplied, the parentheses are optional. The body of the function is the compound command \<compound-command\> (see [Compound Commands](#Compound-Commands)). That command is usually a \<list\> enclosed between { and }, but may be any compound command listed above. If the `function` reserved word is used, but the parentheses are not supplied, the braces are recommended. When the shell is in POSIX mode (see [Bash POSIX Mode](#Bash-POSIX-Mode)), \<fname\> must be a valid shell name and may not be the same as one of the special builtins (see [Special Builtins](#Special-Builtins)). When not in POSIX mode, a function name can be any unquoted shell word that does not contain ‘`$`’.

Any redirections (see [Redirections](#Redirections)) associated with the shell function are performed when the function is executed. Function definitions are deleted using the `-f` option to the `unset` builtin (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)).

The exit status of a function definition is zero unless a syntax error occurs or a readonly function with the same name already exists. When executed, the exit status of a function is the exit status of the last command executed in the body.

Note that for historical reasons, in the most common usage the curly braces that surround the body of the function must be separated from the body by `blank`s or newlines. This is because the braces are reserved words and are only recognized as such when they are separated from the command list by whitespace or another shell metacharacter. When using the braces, the \<list\> must be terminated by a semicolon, a ‘`&`’, or a newline.

\<compound-command\> is executed whenever \<fname\> is specified as the name of a simple command. Functions are executed in the context of the calling shell; there is no new process created to interpret them (contrast this with the execution of a shell script).

When a function is executed, the arguments to the function become the positional parameters during its execution (see [Positional Parameters](#Positional-Parameters)). The special parameter ‘`#`’ that expands to the number of positional parameters is updated to reflect the new set of positional parameters. Special parameter `0` is unchanged. The first element of the `FUNCNAME` variable is set to the name of the function while the function is executing.

All other aspects of the shell execution environment are identical between a function and its caller with these exceptions: the `DEBUG` and `RETURN` traps are not inherited unless the function has been given the `trace` attribute using the `declare` builtin or the `-o functrace` option has been enabled with the `set` builtin, (in which case all functions inherit the `DEBUG` and `RETURN` traps), and the `ERR` trap is not inherited unless the `-o errtrace` shell option has been enabled. See [Bourne Shell Builtins](#Bourne-Shell-Builtins), for the description of the `trap` builtin.

The `FUNCNEST` variable, if set to a numeric value greater than 0, defines a maximum function nesting level. Function invocations that exceed the limit cause the entire command to abort.

If the builtin command `return` is executed in a function, the function completes and execution resumes with the next command after the function call. Any command associated with the `RETURN` trap is executed before execution resumes. When a function completes, the values of the positional parameters and the special parameter ‘`#`’ are restored to the values they had prior to the function’s execution. If `return` is supplied a numeric argument, that is the function’s return status; otherwise the function’s return status is the exit status of the last command executed before the `return`.

Variables local to the function are declared with the `local` builtin (local variables). Ordinarily, variables and their values are shared between a function and its caller. These variables are visible only to the function and the commands it invokes. This is particularly important when a shell function calls other functions.

In the following description, the current scope is a currently- executing function. Previous scopes consist of that function’s caller and so on, back to the "global" scope, where the shell is not executing any shell function. A local variable at the current local scope is a variable declared using the `local` or `declare` builtins in the function that is currently executing.

Local variables "shadow" variables with the same name declared at previous scopes. For instance, a local variable declared in a function hides variables with the same name declared at previous scopes, including global variables: references and assignments refer to the local variable, leaving the variables at previous scopes unmodified. When the function returns, the global variable is once again visible.

The shell uses dynamic scoping to control a variable’s visibility within functions. With dynamic scoping, visible variables and their values are a result of the sequence of function calls that caused execution to reach the current function. The value of a variable that a function sees depends on its value within its caller, if any, whether that caller is the global scope or another shell function. This is also the value that a local variable declaration shadows, and the value that is restored when the function returns.

For example, if a variable `var` is declared as local in function `func1`, and `func1` calls another function `func2`, references to `var` made from within `func2` resolve to the local variable `var` from `func1`, shadowing any global variable named `var`.

The following script demonstrates this behavior. When executed, the script displays

    In func2, var = func1 local

    func1()
    {
        local var='func1 local'
        func2
    }

    func2()
    {
        echo "In func2, var = $var"
    }

    var=global
    func1

The `unset` builtin also acts using the same dynamic scope: if a variable is local to the current scope, `unset` unsets it; otherwise the unset will refer to the variable found in any calling scope as described above. If a variable at the current local scope is unset, it remains so (appearing as unset) until it is reset in that scope or until the function returns. Once the function returns, any instance of the variable at a previous scope becomes visible. If the unset acts on a variable at a previous scope, any instance of a variable with that name that had been shadowed becomes visible (see below how the `localvar_unset` shell option changes this behavior).

The `-f` option to the `declare` (`typeset`) builtin command (see [Bash Builtins](#Bash-Builtins)) lists function names and definitions. The `-F` option to `declare` or `typeset` lists the function names only (and optionally the source file and line number, if the `extdebug` shell option is enabled). Functions may be exported so that child shell processes (those created when executing a separate shell invocation) automatically have them defined with the `-f` option to the `export` builtin (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)). The `-f` option to the `unset` builtin (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)) deletes a function definition.

Functions may be recursive. The `FUNCNEST` variable may be used to limit the depth of the function call stack and restrict the number of function invocations. By default, Bash places no limit on the number of recursive calls.
