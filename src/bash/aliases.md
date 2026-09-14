---
title: Aliases
source_url: https://www.gnu.org/software/bash/manual
source_path: 028-aliases.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 280
---

## Aliases

alias expansion

Aliases allow a string to be substituted for a word that is in a position in the input where it can be the first word of a simple command. Aliases have names and corresponding values that are set and unset using the `alias` and `unalias` builtin commands (see [Shell Builtin Commands](#Shell-Builtin-Commands)).

If the shell reads an unquoted word in the right position, it checks the word to see if it matches an alias name. If it matches, the shell replaces the word with the alias value, and reads that value as if it had been read instead of the word. The shell doesn’t look at any characters following the word before attempting alias substitution.

The characters ‘`/`’, ‘`$`’, ‘`` ` ``’, ‘`=`’ and any of the shell metacharacters or quoting characters listed above may not appear in an alias name. The replacement text may contain any valid shell input, including shell metacharacters. The first word of the replacement text is tested for aliases, but a word that is identical to an alias being expanded is not expanded a second time. This means that one may alias `ls` to `"ls -F"`, for instance, and Bash does not try to recursively expand the replacement text.

If the last character of the alias value is a `blank`, then the shell checks the next command word following the alias for alias expansion.

Aliases are created and listed with the `alias` command, and removed with the `unalias` command.

There is no mechanism for using arguments in the replacement text, as in `csh`. If arguments are needed, use a shell function (see [Shell Functions](#Shell-Functions)) instead.

Aliases are not expanded when the shell is not interactive, unless the `expand_aliases` shell option is set using `shopt` (see [The Shopt Builtin](#The-Shopt-Builtin)).

The rules concerning the definition and use of aliases are somewhat confusing. Bash always reads at least one complete line of input, and all lines that make up a compound command, before executing any of the commands on that line or the compound command. Aliases are expanded when a command is read, not when it is executed. Therefore, an alias definition appearing on the same line as another command does not take effect until the shell reads the next line of input, and an alias definition in a compound command does not take effect until the shell parses and executes the entire compound command. The commands following the alias definition on that line, or in the rest of a compound command, are not affected by the new alias. This behavior is also an issue when functions are executed. Aliases are expanded when a function definition is read, not when the function is executed, because a function definition is itself a command. As a consequence, aliases defined in a function are not available until after that function is executed. To be safe, always put alias definitions on a separate line, and do not use `alias` in compound commands.

For almost every purpose, shell functions are preferable to aliases.
