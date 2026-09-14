---
title: Command Line Editing
source_url: https://www.gnu.org/software/bash/manual
source_path: 039-command-line-editing.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 390
---

## Command Line Editing

This chapter describes the basic features of the GNU command line editing interface. Command line editing is provided by the Readline library, which is used by several different programs, including Bash. Command line editing is enabled by default when using an interactive shell, unless the `--noediting` option is supplied at shell invocation. Line editing is also used when using the `-e` option to the `read` builtin command (see [Bash Builtins](#Bash-Builtins)). By default, the line editing commands are similar to those of Emacs; a vi-style line editing interface is also available. Line editing can be enabled at any time using the `-o emacs` or `-o vi` options to the `set` builtin command (see [The Set Builtin](#The-Set-Builtin)), or disabled using the `+o emacs` or `+o vi` options to `set`.
