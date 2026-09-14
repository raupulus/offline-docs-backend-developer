---
title: Redirections
source_url: https://www.gnu.org/software/bash/manual
source_path: 011-redirections.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 110
---

## Redirections

redirection

Before a command is executed, its input and output may be redirected using a special notation interpreted by the shell. Redirection allows commands’ file handles to be duplicated, opened, closed, made to refer to different files, and can change the files the command reads from and writes to. When used with the `exec` builtin, redirections modify file handles in the current shell execution environment. The following redirection operators may precede or appear anywhere within a simple command or may follow a command. Redirections are processed in the order they appear, from left to right.

Each redirection that may be preceded by a file descriptor number may instead be preceded by a word of the form {\<varname\>}. In this case, for each redirection operator except `>&-` and `<&-`, the shell allocates a file descriptor greater than or equal to 10 and assigns it to {\<varname\>}. If {\<varname\>} precedes `>&-` or `<&-`, the value of \<varname\> defines the file descriptor to close. If {\<varname\>} is supplied, the redirection persists beyond the scope of the command, which allows the shell programmer to manage the file descriptor’s lifetime manually without using the `exec` builtin. The `varredir_close` shell option manages this behavior (see [The Shopt Builtin](#The-Shopt-Builtin)).

In the following descriptions, if the file descriptor number is omitted, and the first character of the redirection operator is ‘`<`’, the redirection refers to the standard input (file descriptor 0). If the first character of the redirection operator is ‘`>`’, the redirection refers to the standard output (file descriptor 1).

The \<word\> following the redirection operator in the following descriptions, unless otherwise noted, is subjected to brace expansion, tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, quote removal, filename expansion, and word splitting. If it expands to more than one word, Bash reports an error.

The order of redirections is significant. For example, the command

    ls > dirlist 2>&1

directs both standard output (file descriptor 1) and standard error (file descriptor 2) to the file \<dirlist\>, while the command

    ls 2>&1 > dirlist

directs only the standard output to file \<dirlist\>, because the standard error was made a copy of the standard output before the standard output was redirected to \<dirlist\>.

Bash handles several filenames specially when they are used in redirections, as described in the following table. If the operating system on which Bash is running provides these special files, Bash uses them; otherwise it emulates them internally with the behavior described below.

`/dev/fd/fd`  
If \<fd\> is a valid integer, duplicate file descriptor \<fd\>.

`/dev/stdin`  
File descriptor 0 is duplicated.

`/dev/stdout`  
File descriptor 1 is duplicated.

`/dev/stderr`  
File descriptor 2 is duplicated.

`/dev/tcp/host/port`  
If \<host\> is a valid hostname or Internet address, and \<port\> is an integer port number or service name, Bash attempts to open the corresponding TCP socket.

`/dev/udp/host/port`  
If \<host\> is a valid hostname or Internet address, and \<port\> is an integer port number or service name, Bash attempts to open the corresponding UDP socket.

A failure to open or create a file causes the redirection to fail.

Redirections using file descriptors greater than 9 should be used with care, as they may conflict with file descriptors the shell uses internally.

### Redirecting Input

Redirecting input opens the file whose name results from the expansion of \<word\> for reading on file descriptor `n`, or the standard input (file descriptor 0) if `n` is not specified.

The general format for redirecting input is:

    [n]<word

### Redirecting Output

Redirecting output opens the file whose name results from the expansion of \<word\> for writing on file descriptor \<n\>, or the standard output (file descriptor 1) if \<n\> is not specified. If the file does not exist it is created; if it does exist it is truncated to zero size.

The general format for redirecting output is:

    [n]>[|]word

If the redirection operator is ‘`>`’, and the `noclobber` option to the `set` builtin command has been enabled, the redirection fails if the file whose name results from the expansion of \<word\> exists and is a regular file. If the redirection operator is ‘`>|`’, or the redirection operator is ‘`>`’ and the `noclobber` option to the `set` builtin is not enabled, Bash attempts the redirection even if the file named by \<word\> exists.

### Appending Redirected Output

Redirecting output in this fashion opens the file whose name results from the expansion of \<word\> for appending on file descriptor \<n\>, or the standard output (file descriptor 1) if \<n\> is not specified. If the file does not exist it is created.

The general format for appending output is:

    [n]>>word

### Redirecting Standard Output and Standard Error

This construct redirects both the standard output (file descriptor 1) and the standard error output (file descriptor 2) to the file whose name is the expansion of \<word\>.

There are two formats for redirecting standard output and standard error:

    &>word

and

    >&word

Of the two forms, the first is preferred. This is semantically equivalent to

    >word 2>&1

When using the second form, \<word\> may not expand to a number or ‘`-`’. If it does, other redirection operators apply (see Duplicating File Descriptors below) for compatibility reasons.

### Appending Standard Output and Standard Error

This construct appends both the standard output (file descriptor 1) and the standard error output (file descriptor 2) to the file whose name is the expansion of \<word\>.

The format for appending standard output and standard error is:

    &>>word

This is semantically equivalent to

    >>word 2>&1

(see Duplicating File Descriptors below).

### Here Documents

This type of redirection instructs the shell to read input from the current source until it reads a line containing only \<delimiter\> (with no trailing blanks). All of the lines read up to that point then become the standard input (or file descriptor \<n\> if \<n\> is specified) for a command.

The format of here-documents is:

    [n]<<[−]word
            here-document
    delimiter

The shell does not perform parameter and variable expansion, command substitution, arithmetic expansion, or filename expansion on \<word\>.

If any part of \<word\> is quoted, the \<delimiter\> is the result of quote removal on \<word\>, and the lines in the here-document are not expanded. If \<word\> is unquoted, \<delimiter\> is \<word\> itself, and the here-document text is treated similarly to a double-quoted string: all lines of the here-document are subjected to parameter expansion, command substitution, and arithmetic expansion, the character sequence `\newline` is treated literally, and ‘`\`’ must be used to quote the characters ‘`\`’, ‘`$`’, and ‘`` ` ``’; however, double quote characters have no special meaning.

If the redirection operator is ‘`<<-`’, the shell strips leading tab characters are stripped from input lines and the line containing \<delimiter\>. This allows here-documents within shell scripts to be indented in a natural fashion.

If the delimiter is not quoted, the `\<newline>` sequence is treated as a line continuation: the two lines are joined and the backslash-newline is removed. This happens while reading the here-document, before the check for the ending delimiter, so joined lines can form the end delimiter.

### Here Strings

A variant of here documents, the format is:

    [n]<<< word

The \<word\> undergoes tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, and quote removal. Filename expansion and word splitting are not performed. The result is supplied as a single string, with a newline appended, to the command on its standard input (or file descriptor \<n\> if \<n\> is specified).

### Duplicating File Descriptors

The redirection operator

    [n]<&word

is used to duplicate input file descriptors. If \<word\> expands to one or more digits, file descriptor \<n\> is made to be a copy of that file descriptor. It is a redirection error if the digits in \<word\> do not specify a file descriptor open for input. If \<word\> evaluates to ‘`-`’, file descriptor \<n\> is closed. If \<n\> is not specified, this uses the standard input (file descriptor 0).

The operator

    [n]>&word

is used similarly to duplicate output file descriptors. If \<n\> is not specified, this uses the standard output (file descriptor 1). It is a redirection error if the digits in \<word\> do not specify a file descriptor open for output. If \<word\> evaluates to ‘`-`’, file descriptor \<n\> is closed. As a special case, if \<n\> is omitted, and \<word\> does not expand to one or more digits or ‘`-`’, this redirects the standard output and standard error as described previously.

### Moving File Descriptors

The redirection operator

    [n]<&digit-

moves the file descriptor \<digit\> to file descriptor \<n\>, or the standard input (file descriptor 0) if \<n\> is not specified. \<digit\> is closed after being duplicated to \<n\>.

Similarly, the redirection operator

    [n]>&digit-

moves the file descriptor \<digit\> to file descriptor \<n\>, or the standard output (file descriptor 1) if \<n\> is not specified.

### Opening File Descriptors for Reading and Writing

The redirection operator

    [n]<>word

opens the file whose name is the expansion of \<word\> for both reading and writing on file descriptor \<n\>, or on file descriptor 0 if \<n\> is not specified. If the file does not exist, it is created.
