---
title: Optional Features
source_url: https://www.gnu.org/software/bash/manual
source_path: 060-optional-features.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 600
---

## Optional Features

The Bash `configure` has a number of `--enable-feature` options, where \<feature\> indicates an optional part of Bash. There are also several `--with-package` options, where \<package\> is something like ‘`bash-malloc`’ or ‘`afs`’. To turn off the default use of a package, use `--without-package`. To configure Bash without a feature that is enabled by default, use `--disable-feature`.

Here is a complete list of the `--enable-` and `--with-` options that the Bash `configure` recognizes.

`--with-afs`  
Define if you are using the Andrew File System from Transarc.

`--with-bash-malloc`  
Use the Bash version of `malloc` in the directory `lib/malloc`. This is not the same `malloc` that appears in GNU libc, but a custom version originally derived from the 4.2 BSD `malloc`. This `malloc` is very fast, but wastes some space on each allocation, though it uses several techniques to minimize the waste. This option is enabled by default. The `NOTES` file contains a list of systems for which this should be turned off, and `configure` disables this option automatically for a number of systems.

`--with-curses`  
Use the curses library instead of the termcap library. `configure` usually chooses this automatically, since most systems include the termcap functions in the curses library.

`--with-gnu-malloc`  
A synonym for `--with-bash-malloc`.

`--with-installed-readline[=PREFIX]`  
Define this to make Bash link with a locally-installed version of Readline rather than the version in `lib/readline`. This works only with Readline 5.0 and later versions. If \<PREFIX\> is `yes` or not supplied, `configure` uses the values of the make variables `includedir` and `libdir`, which are subdirectories of `prefix` by default, to find the installed version of Readline if it is not in the standard system include and library directories. If \<PREFIX\> is `no`, Bash links with the version in `lib/readline`. If \<PREFIX\> is set to any other value, `configure` treats it as a directory pathname and looks for the installed version of Readline in subdirectories of that directory (include files in \<PREFIX\>/`include` and the library in \<PREFIX\>/`lib`). The Bash default is to link with a static library built in the `lib/readline` subdirectory of the build directory.

`--with-libintl-prefix[=PREFIX]`  
Define this to make Bash link with a locally-installed version of the libintl library instead of the version in `lib/intl`.

`--with-libiconv-prefix[=PREFIX]`  
Define this to make Bash look for libiconv in \<PREFIX\> instead of the standard system locations. The Bash distribution does not include this library.

`--enable-minimal-config`  
This produces a shell with minimal features, closer to the historical Bourne shell.

There are several `--enable-` options that alter how Bash is compiled, linked, and installed, rather than changing run-time features.

`--enable-largefile`  
Enable support for [large files](http://www.unix.org/version2/whatsnew/lfs20mar.html) if the operating system requires special compiler options to build programs which can access large files. This is enabled by default, if the operating system provides large file support.

`--enable-profiling`  
This builds a Bash binary that produces profiling information to be processed by `gprof` each time it is executed.

`--enable-separate-helpfiles`  
Use external files for the documentation displayed by the `help` builtin instead of storing the text internally.

`--enable-static-link`  
This causes Bash to be linked statically, if `gcc` is being used. This could be used to build a version to use as root’s shell.

The ‘`minimal-config`’ option can be used to disable all of the following options, but it is processed first, so individual options may be enabled using ‘`enable-feature`’.

All of the following options except for ‘`alt-array-implementation`’, ‘`disabled-builtins`’, ‘`direxpand-default`’, ‘`strict-posix-default`’, and ‘`xpg-echo-default`’ are enabled by default, unless the operating system does not provide the necessary support.

`--enable-alias`  
Allow alias expansion and include the `alias` and `unalias` builtins (see [Aliases](#Aliases)).

`--enable-alt-array-implementation`  
This builds Bash using an alternate implementation of arrays (see [Arrays](#Arrays)) that provides faster access at the expense of using more memory (sometimes many times more, depending on how sparse an array is).

`--enable-arith-for-command`  
Include support for the alternate form of the `for` command that behaves like the C language `for` statement (see [Looping Constructs](#Looping-Constructs)).

`--enable-array-variables`  
Include support for one-dimensional array shell variables (see [Arrays](#Arrays)).

`--enable-bang-history`  
Include support for `csh`-like history substitution (see [History Interaction](#History-Interaction)).

`--enable-bash-source-fullpath-default`  
Set the default value of the `bash_source_fullpath` shell option described above under [The Shopt Builtin](#The-Shopt-Builtin) to be enabled. This controls how filenames are assigned to the `BASH_SOURCE` array variable.

`--enable-brace-expansion`  
Include `csh`-like brace expansion ( `b{a,b}c` ↦ `bac bbc` ). See [Brace Expansion](#Brace-Expansion), for a complete description.

`--enable-casemod-attributes`  
Include support for case-modifying attributes in the `declare` builtin and assignment statements. Variables with the `uppercase` attribute, for example, will have their values converted to uppercase upon assignment.

`--enable-casemod-expansion`  
Include support for case-modifying word expansions.

`--enable-command-timing`  
Include support for recognizing `time` as a reserved word and for displaying timing statistics for the pipeline following `time` (see [Pipelines](#Pipelines)). This allows timing pipelines, shell compound commands, shell builtins, and shell functions, which an external command cannot do easily.

`--enable-cond-command`  
Include support for the `[[` conditional command. (see [Conditional Constructs](#Conditional-Constructs)).

`--enable-cond-regexp`  
Include support for matching POSIX regular expressions using the ‘`=~`’ binary operator in the `[[` conditional command. (see [Conditional Constructs](#Conditional-Constructs)).

`--enable-coprocesses`  
Include support for coprocesses and the `coproc` reserved word (see [Pipelines](#Pipelines)).

`--enable-debugger`  
Include support for the Bash debugger (distributed separately).

`--enable-dev-fd-stat-broken`  
If calling `stat` on /dev/fd/\<N\> returns different results than calling `fstat` on file descriptor \<N\>, supply this option to enable a workaround. This has implications for conditional commands that test file attributes.

`--enable-direxpand-default`  
Cause the `direxpand` shell option (see [The Shopt Builtin](#The-Shopt-Builtin)) to be enabled by default when the shell starts. It is normally disabled by default.

`--enable-directory-stack`  
Include support for a `csh`-like directory stack and the `pushd`, `popd`, and `dirs` builtins (see [The Directory Stack](#The-Directory-Stack)).

`--enable-disabled-builtins`  
Allow builtin commands to be invoked via ‘`builtin xxx`’ even after `xxx` has been disabled using ‘`enable -n xxx`’. See [Bash Builtins](#Bash-Builtins), for details of the `builtin` and `enable` builtin commands.

`--enable-dparen-arithmetic`  
Include support for the `((…))` command (see [Conditional Constructs](#Conditional-Constructs)).

`--enable-extended-glob`  
Include support for the extended pattern matching features described above under [Pattern Matching](#Pattern-Matching).

`--enable-extended-glob-default`  
Set the default value of the `extglob` shell option described above under [The Shopt Builtin](#The-Shopt-Builtin) to be enabled.

`--enable-function-import`  
Include support for importing function definitions exported by another instance of the shell from the environment. This option is enabled by default.

`--enable-glob-asciiranges-default`  
Set the default value of the `globasciiranges` shell option described above under [The Shopt Builtin](#The-Shopt-Builtin) to be enabled. This controls the behavior of character ranges when used in pattern matching bracket expressions.

`--enable-help-builtin`  
Include the `help` builtin, which displays help on shell builtins and variables (see [Bash Builtins](#Bash-Builtins)).

`--enable-history`  
Include command history and the `fc` and `history` builtin commands (see [Bash History Facilities](#Bash-History-Facilities)).

`--enable-job-control`  
This enables the job control features (see [Job Control](#Job-Control)), if the operating system supports them.

`--enable-multibyte`  
This enables support for multibyte characters if the operating system provides the necessary support.

`--enable-net-redirections`  
This enables the special handling of filenames of the form `/dev/tcp/host/port` and `/dev/udp/host/port` when used in redirections (see [Redirections](#Redirections)).

`--enable-process-substitution`  
This enables process substitution (see [Process Substitution](#Process-Substitution)) if the operating system provides the necessary support.

`--enable-progcomp`  
Enable the programmable completion facilities (see [Programmable Completion](#Programmable-Completion)). If Readline is not enabled, this option has no effect.

`--enable-prompt-string-decoding`  
Turn on the interpretation of a number of backslash-escaped characters in the `$PS0`, `$PS1`, `$PS2`, and `$PS4` prompt strings. See [Controlling the Prompt](#Controlling-the-Prompt), for a complete list of prompt string escape sequences.

`--enable-readline`  
Include support for command-line editing and history with the Bash version of the Readline library (see [Command Line Editing](#Command-Line-Editing)).

`--enable-restricted`  
Include support for a restricted shell. If this is enabled, Bash enters a restricted mode when called as `rbash`. See [The Restricted Shell](#The-Restricted-Shell), for a description of restricted mode.

`--enable-select`  
Include the `select` compound command, which allows generation of simple menus (see [Conditional Constructs](#Conditional-Constructs)).

`--enable-single-help-strings`  
Store the text displayed by the `help` builtin as a single string for each help topic. This aids in translating the text to different languages. You may need to disable this if your compiler cannot handle very long string literals.

`--enable-strict-posix-default`  
Make Bash POSIX-conformant by default (see [Bash POSIX Mode](#Bash-POSIX-Mode)).

`--enable-translatable-strings`  
Enable support for `$"string"` translatable strings (see [Locale Translation](#Locale-Translation)).

`--enable-usg-echo-default`  
A synonym for `--enable-xpg-echo-default`.

`--enable-xpg-echo-default`  
Make the `echo` builtin expand backslash-escaped characters by default, without requiring the `-e` option. This sets the default value of the `xpg_echo` shell option to `on`, which makes the Bash `echo` behave more like the version specified in the Single Unix Specification, version 3. See [Bash Builtins](#Bash-Builtins), for a description of the escape sequences that `echo` recognizes.

The file `config-top.h` contains C Preprocessor ‘`#define`’ statements for options which are not settable from `configure`. Some of these are not meant to be changed; beware of the consequences if you do. Read the comments associated with each definition for more information about its effect.
