---
title: The Directory Stack
source_url: https://www.gnu.org/software/bash/manual
source_path: 030-the-directory-stack.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 300
---

## The Directory Stack

directory stack

The directory stack is a list of recently-visited directories. The `pushd` builtin adds directories to the stack as it changes the current directory, and the `popd` builtin removes specified directories from the stack and changes the current directory to the directory removed. The `dirs` builtin displays the contents of the directory stack. The current directory is always the "top" of the directory stack.

The contents of the directory stack are also visible as the value of the `DIRSTACK` shell variable.

### Directory Stack Builtins

`dirs`  

dirs

    dirs [-clpv] [+N | -N]

Without options, display the list of currently remembered directories. Directories are added to the list with the `pushd` command; the `popd` command removes directories from the list. The current directory is always the first directory in the stack.

Options, if supplied, have the following meanings:

`-c`  
Clears the directory stack by deleting all of the elements.

`-l`  
Produces a listing using full pathnames; the default listing format uses a tilde to denote the home directory.

`-p`  
Causes `dirs` to print the directory stack with one entry per line.

`-v`  
Causes `dirs` to print the directory stack with one entry per line, prefixing each entry with its index in the stack.

`+N`  
Displays the \<N\>th directory (counting from the left of the list printed by `dirs` when invoked without options), starting with zero.

`-N`  
Displays the \<N\>th directory (counting from the right of the list printed by `dirs` when invoked without options), starting with zero.

`popd`  

popd

    popd [-n] [+N | -N]

Remove elements from the directory stack. The elements are numbered from 0 starting at the first directory listed by `dirs`; that is, `popd` is equivalent to `popd +0`.

When no arguments are given, `popd` removes the top directory from the stack and changes to the new top directory.

Arguments, if supplied, have the following meanings:

`-n`  
Suppress the normal change of directory when removing directories from the stack, only manipulate the stack.

`+N`  
Remove the \<N\>th directory (counting from the left of the list printed by `dirs`), starting with zero, from the stack.

`-N`  
Remove the \<N\>th directory (counting from the right of the list printed by `dirs`), starting with zero, from the stack.

If the top element of the directory stack is modified, and the `-n` option was not supplied, `popd` uses the `cd` builtin to change to the directory at the top of the stack. If the `cd` fails, `popd` returns a non-zero value.

Otherwise, `popd` returns an unsuccessful status if an invalid option is specified, the directory stack is empty, or \<N\> specifies a non-existent directory stack entry.

If the `popd` command is successful, Bash runs `dirs` to show the final contents of the directory stack, and the return status is 0.

`pushd`  

pushd

    pushd [-n] [+N | -N | dir]

Add a directory to the top of the directory stack, or rotate the stack, making the new top of the stack the current working directory. With no arguments, `pushd` exchanges the top two elements of the directory stack.

Arguments, if supplied, have the following meanings:

`-n`  
Suppress the normal change of directory when rotating or adding directories to the stack, only manipulate the stack.

`+N`  
Rotate the stack so that the \<N\>th directory (counting from the left of the list printed by `dirs`, starting with zero) is at the top.

`-N`  
Rotate the stack so that the \<N\>th directory (counting from the right of the list printed by `dirs`, starting with zero) is at the top.

`dir`  
Make \<dir\> be the top of the stack.

After the stack has been modified, if the `-n` option was not supplied, `pushd` uses the `cd` builtin to change to the directory at the top of the stack. If the `cd` fails, `pushd` returns a non-zero value.

Otherwise, if no arguments are supplied, `pushd` returns zero unless the directory stack is empty. When rotating the directory stack, `pushd` returns zero unless the directory stack is empty or \<N\> specifies a non-existent directory stack element.

If the `pushd` command is successful, Bash runs `dirs` to show the final contents of the directory stack.
