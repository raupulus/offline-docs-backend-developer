---
title: Readline vi Mode
source_url: https://www.gnu.org/software/bash/manual
source_path: 044-readline-vi-mode.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 440
---

## Readline vi Mode

While the Readline library does not have a full set of `vi` editing functions, it does contain enough to allow simple editing of the line. The Readline `vi` mode behaves as specified in the `sh` description in the POSIX standard.

You can use the ‘`set -o emacs`’ and ‘`set -o vi`’ commands (see [The Set Builtin](#The-Set-Builtin)) to switch interactively between `emacs` and `vi` editing modes, The Readline default is `emacs` mode.

When you enter a line in `vi` mode, you are already placed in ‘insertion’ mode, as if you had typed an ‘`i`’. Pressing ESC switches you into ‘command’ mode, where you can edit the text of the line with the standard `vi` movement keys, move to previous history lines with ‘`k`’ and subsequent lines with ‘`j`’, and so forth.
