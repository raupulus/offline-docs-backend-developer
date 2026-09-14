---
title: Bash Conditional Expressions
source_url: https://www.gnu.org/software/bash/manual
source_path: 026-bash-conditional-expressions.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 260
---

## Bash Conditional Expressions

expressions, conditional

Conditional expressions are used by the `[[` compound command (see [Conditional Constructs](#Conditional-Constructs)) and the `test` and `[` builtin commands (see [Bourne Shell Builtins](#Bourne-Shell-Builtins)). The `test` and `[` commands determine their behavior based on the number of arguments; see the descriptions of those commands for any other command-specific actions.

Expressions may be unary or binary, and are formed from the primaries listed below. Unary expressions are often used to examine the status of a file or shell variable. Binary operators are used for string, numeric, and file attribute comparisons.

Bash handles several filenames specially when they are used in expressions. If the operating system on which Bash is running provides these special files, Bash uses them; otherwise it emulates them internally with this behavior: If the \<file\> argument to one of the primaries is of the form `/dev/fd/N`, then Bash checks file descriptor \<N\>. If the \<file\> argument to one of the primaries is one of `/dev/stdin`, `/dev/stdout`, or `/dev/stderr`, Bash checks file descriptor 0, 1, or 2, respectively.

When used with `[[`, the ‘`<`’ and ‘`>`’ operators sort lexicographically using the current locale. The `test` command uses ASCII ordering.

Unless otherwise specified, primaries that operate on files follow symbolic links and operate on the target of the link, rather than the link itself.

`-a file`  
True if \<file\> exists.

`-b file`  
True if \<file\> exists and is a block special file.

`-c file`  
True if \<file\> exists and is a character special file.

`-d file`  
True if \<file\> exists and is a directory.

`-e file`  
True if \<file\> exists.

`-f file`  
True if \<file\> exists and is a regular file.

`-g file`  
True if \<file\> exists and its set-group-id bit is set.

`-h file`  
True if \<file\> exists and is a symbolic link.

`-k file`  
True if \<file\> exists and its "sticky" bit is set.

`-p file`  
True if \<file\> exists and is a named pipe (FIFO).

`-r file`  
True if \<file\> exists and is readable.

`-s file`  
True if \<file\> exists and has a size greater than zero.

`-t fd`  
True if file descriptor \<fd\> is open and refers to a terminal.

`-u file`  
True if \<file\> exists and its set-user-id bit is set.

`-w file`  
True if \<file\> exists and is writable.

`-x file`  
True if \<file\> exists and is executable.

`-G file`  
True if \<file\> exists and is owned by the effective group id.

`-L file`  
True if \<file\> exists and is a symbolic link.

`-N file`  
True if \<file\> exists and has been modified since it was last accessed.

`-O file`  
True if \<file\> exists and is owned by the effective user id.

`-S file`  
True if \<file\> exists and is a socket.

`file1 -ef file2`  
True if \<file1\> and \<file2\> refer to the same device and inode numbers.

`file1 -nt file2`  
True if \<file1\> is newer (according to modification date) than \<file2\>, or if \<file1\> exists and \<file2\> does not.

`file1 -ot file2`  
True if \<file1\> is older than \<file2\>, or if \<file2\> exists and \<file1\> does not.

`-o optname`  
True if the shell option \<optname\> is enabled. The list of options appears in the description of the `-o` option to the `set` builtin (see [The Set Builtin](#The-Set-Builtin)).

`-v varname`  
True if the shell variable \<varname\> is set (has been assigned a value). If \<varname\> is an indexed array variable name subscripted by ‘`@`’ or ‘`*`’, this returns true if the array has any set elements. If \<varname\> is an associative array variable name subscripted by ‘`@`’ or ‘`*`’, this returns true if an element with that key is set.

`-R varname`  
True if the shell variable \<varname\> is set and is a name reference.

`-z string`  
True if the length of \<string\> is zero.

`-n string`; `string`  
True if the length of \<string\> is non-zero.

`string1 == string2`; `string1 = string2`  
True if the strings are equal. When used with the `[[` command, this performs pattern matching as described above (see [Conditional Constructs](#Conditional-Constructs)).

‘`=`’ should be used with the `test` command for POSIX conformance.

`string1 != string2`  
True if the strings are not equal.

`string1 < string2`  
True if \<string1\> sorts before \<string2\> lexicographically.

`string1 > string2`  
True if \<string1\> sorts after \<string2\> lexicographically.

`arg1 OP arg2`  
`OP` is one of ‘`-eq`’, ‘`-ne`’, ‘`-lt`’, ‘`-le`’, ‘`-gt`’, or ‘`-ge`’. These arithmetic binary operators return true if \<arg1\> is equal to, not equal to, less than, less than or equal to, greater than, or greater than or equal to \<arg2\>, respectively. \<Arg1\> and \<arg2\> may be positive or negative integers. When used with the `[[` command, \<arg1\> and \<arg2\> are evaluated as arithmetic expressions (see [Shell Arithmetic](#Shell-Arithmetic)). Since the expansions the `[[` command performs on \<arg1\> and \<arg2\> can potentially result in empty strings, arithmetic expression evaluation treats those as expressions that evaluate to 0.
