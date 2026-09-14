---
title: Special Builtins
source_url: https://www.gnu.org/software/bash/manual
source_path: 018-special-builtins.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 180
---

## Special Builtins

special builtin

For historical reasons, the POSIX standard has classified several builtin commands as *special*. When Bash is executing in POSIX mode, the special builtins differ from other builtin commands in three respects:

1.  Special builtins are found before shell functions during command lookup.

2.  If a special builtin returns an error status, a non-interactive shell exits.

3.  Assignment statements preceding the command stay in effect in the shell environment after the command completes.

When Bash is not executing in POSIX mode, these builtins behave no differently than the rest of the Bash builtin commands. The Bash POSIX mode is described in [Bash POSIX Mode](#Bash-POSIX-Mode).

These are the POSIX special builtins:

    break&#160;:&#160;.&#160;source&#160;continue&#160;eval&#160;exec&#160;exit&#160;export&#160;readonly&#160;return&#160;set
    shift&#160;times&#160;trap&#160;unset
