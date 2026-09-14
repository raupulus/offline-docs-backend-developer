---
title: Interactive Shells
source_url: https://www.gnu.org/software/bash/manual
source_path: 025-interactive-shells.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 250
---

## Interactive Shells

interactive shell

shell, interactive

### What is an Interactive Shell?

An interactive shell is one started without non-option arguments (unless `-s` is specified) and without specifying the `-c` option, whose input and error output are both connected to terminals (as determined by `isatty(3)`), or one started with the `-i` option.

An interactive shell generally reads from and writes to a user’s terminal.

The `-s` invocation option may be used to set the positional parameters when an interactive shell starts.

### Is this Shell Interactive?

To determine within a startup script whether or not Bash is running interactively, test the value of the ‘`-`’ special parameter. It contains `i` when the shell is interactive. For example:

    case "$-" in
    *i*)    echo This shell is interactive ;;
    *)  echo This shell is not interactive ;;
    esac

Alternatively, startup scripts may examine the variable `PS1`; it is unset in non-interactive shells, and set in interactive shells. Thus:

    if [ -z "$PS1" ]; then
            echo This shell is not interactive
    else
            echo This shell is interactive
    fi

### Interactive Shell Behavior

When the shell is running interactively, it changes its behavior in several ways.

1.  Bash reads and executes startup files as described in [Bash Startup Files](#Bash-Startup-Files).

2.  Job Control (see [Job Control](#Job-Control)) is enabled by default. When job control is in effect, Bash ignores the keyboard-generated job control signals `SIGTTIN`, `SIGTTOU`, and `SIGTSTP`.

3.  Bash executes the values of the set elements of the `PROMPT_COMMAND` array variable as commands before printing the primary prompt, `$PS1` (see [Bash Variables](#Bash-Variables)).

4.  Bash expands and displays `PS1` before reading the first line of a command, and expands and displays `PS2` before reading the second and subsequent lines of a multi-line command. Bash expands and displays `PS0` after it reads a command but before executing it. See [Controlling the Prompt](#Controlling-the-Prompt), for a complete list of prompt string escape sequences.

5.  Bash uses Readline (see [Command Line Editing](#Command-Line-Editing)) to read commands from the user’s terminal.

6.  Bash inspects the value of the `ignoreeof` option to `set -o` instead of exiting immediately when it receives an `EOF` on its standard input when reading a command (see [The Set Builtin](#The-Set-Builtin)).

7.  Bash enables Command history (see [Bash History Facilities](#Bash-History-Facilities)) and history expansion (see [History Interaction](#History-Interaction)) by default. When a shell with history enabled exits, Bash saves the command history to the file named by `$HISTFILE`.

8.  Alias expansion (see [Aliases](#Aliases)) is performed by default.

9.  In the absence of any traps, Bash ignores `SIGTERM` (see [Signals](#Signals)).

10. In the absence of any traps, `SIGINT` is caught and handled (see [Signals](#Signals)). `SIGINT` will interrupt some shell builtins.

11. An interactive login shell sends a `SIGHUP` to all jobs on exit if the `huponexit` shell option has been enabled (see [Signals](#Signals)).

12. The `-n` option has no effect, whether at invocation or when using ‘`set -n`’ (see [The Set Builtin](#The-Set-Builtin)).

13. Bash will check for mail periodically, depending on the values of the `MAIL`, `MAILPATH`, and `MAILCHECK` shell variables (see [Bash Variables](#Bash-Variables)).

14. The shell will not exit on expansion errors due to references to unbound shell variables after ‘`set -u`’ has been enabled (see [The Set Builtin](#The-Set-Builtin)).

15. The shell will not exit on expansion errors caused by \<var\> being unset or null in `${var:?word}` expansions (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)).

16. Redirection errors encountered by shell builtins will not cause the shell to exit.

17. When running in POSIX mode, a special builtin returning an error status will not cause the shell to exit (see [Bash POSIX Mode](#Bash-POSIX-Mode)).

18. A failed `exec` will not cause the shell to exit (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)).

19. Parser syntax errors will not cause the shell to exit.

20. If the `cdspell` shell option is enabled, the shell will attempt simple spelling correction for directory arguments to the `cd` builtin (see the description of the `cdspell` option to the `shopt` builtin in [The Shopt Builtin](#The-Shopt-Builtin)). The `cdspell` option is only effective in interactive shells.

21. The shell will check the value of the `TMOUT` variable and exit if a command is not read within the specified number of seconds after printing `$PS1` (see [Bash Variables](#Bash-Variables)).
