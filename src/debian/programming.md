---
title: Programming
source_url: https://www.debian.org/doc/manuals/debian-reference/_programming
source_repo: https://salsa.debian.org/debian/debian-reference.git
source_ref: master
source_commit: b7239e647
source_path: 12_programming.rawxml
technology: debian
version: 12 (Bookworm)
license: GPL-2.0-or-later
retrieved_at: '2026-09-15'
order: 130
---

## Programming

I provide some pointers for people to learn programming on the Debian system enough to trace the packaged source code. Here are notable packages and corresponding documentation packages for programming.

| package | popcon | size | documentation |
|:---|:---|:---|:---|
| `autoconf` | @-@popcon1@-@ | @-@psize1@-@ | "`info autoconf`" provided by `autoconf-doc` |
| `automake` | @-@popcon1@-@ | @-@psize1@-@ | "`info automake`" provided by `automake1.10-doc` |
| `bash` | @-@popcon1@-@ | @-@psize1@-@ | "`info bash`" provided by `bash-doc` |
| `bison` | @-@popcon1@-@ | @-@psize1@-@ | "`info bison`" provided by `bison-doc` |
| `cpp` | @-@popcon1@-@ | @-@psize1@-@ | "`info cpp`" provided by `cpp-doc` |
| `ddd` | @-@popcon1@-@ | @-@psize1@-@ | "`info ddd`" provided by `ddd-doc` |
| `exuberant-ctags` | @-@popcon1@-@ | @-@psize1@-@ | `exuberant-ctags(1)` |
| `flex` | @-@popcon1@-@ | @-@psize1@-@ | "`info flex`" provided by `flex-doc` |
| `gawk` | @-@popcon1@-@ | @-@psize1@-@ | "`info gawk`" provided by `gawk-doc` |
| `gcc` | @-@popcon1@-@ | @-@psize1@-@ | "`info gcc`" provided by `gcc-doc` |
| `gdb` | @-@popcon1@-@ | @-@psize1@-@ | "`info gdb`" provided by `gdb-doc` |
| `gettext` | @-@popcon1@-@ | @-@psize1@-@ | "`info gettext`" provided by `gettext-doc` |
| `gfortran` | @-@popcon1@-@ | @-@psize1@-@ | "`info gfortran`" provided by `gfortran-doc` (Fortran 95) |
| `fpc` | @-@popcon1@-@ | @-@psize1@-@ | `fpc(1)` and html by `fp-docs` (Pascal) |
| `glade` | @-@popcon1@-@ | @-@psize1@-@ | help provided via menu (UI Builder) |
| `libc6` | @-@popcon1@-@ | @-@psize1@-@ | "`info libc`" provided by `glibc-doc` and `glibc-doc-reference` |
| `make` | @-@popcon1@-@ | @-@psize1@-@ | "`info make`" provided by `make-doc` |
| `xutils-dev` | @-@popcon1@-@ | @-@psize1@-@ | `imake(1)`, `xmkmf(1)`, etc. |
| `mawk` | @-@popcon1@-@ | @-@psize1@-@ | `mawk(1)` |
| `perl` | @-@popcon1@-@ | @-@psize1@-@ | `perl(1)` and html pages provided by `perl-doc` and `perl-doc-html` |
| `python` | @-@popcon1@-@ | @-@psize1@-@ | `python(1)` and html pages provided by `python-doc` |
| `tcl` | @-@popcon1@-@ | @-@psize1@-@ | `tcl(3)` and detail manual pages provided by `tcl-doc` |
| `tk` | @-@popcon1@-@ | @-@psize1@-@ | `tk(3)` and detail manual pages provided by `tk-doc` |
| `ruby` | @-@popcon1@-@ | @-@psize1@-@ | `ruby(1)` and interactive reference provided by `ri` |
| `vim` | @-@popcon1@-@ | @-@psize1@-@ | help(F1) menu provided by `vim-doc` |
| `susv2` | @-@popcon1@-@ | @-@psize1@-@ | fetch "[The Single UNIX Specifications v2](http://www.unix.org/version2/)" |
| `susv3` | @-@popcon1@-@ | @-@psize1@-@ | fetch "[The Single UNIX Specifications v3](http://www.unix.org/version3/)" |

List of packages to help programming

Online references are available by typing "`man name`" after installing `manpages` and `manpages-dev` packages. Online references for the GNU tools are available by typing "`info program_name`" after installing the pertinent documentation packages. You may need to include the `contrib` and `non-free` archives in addition to the `main` archive since some GFDL documentations are not considered to be DFSG compliant.

> [!WARNING]
> Do not use "`test`" as the name of an executable test file. "`test`" is a shell builtin.

> [!CAUTION]
> You should install software programs directly compiled from source into "`/usr/local`" or "`/opt`" to avoid collision with system programs.

> [!TIP]
> [Code examples of creating "Song 99 Bottles of Beer"](http://www.99-bottles-of-beer.net/) should give you good ideas of practically all the programming languages.

## The shell script

The [shell script](https://en.wikipedia.org/wiki/Shell_script) is a text file with the execution bit set and contains the commands in the following format.

    #!/bin/sh
     ... command lines

The first line specifies the shell interpreter which read and execute this file contents.

Reading shell scripts is the **best** way to understand how a Unix-like system works. Here, I give some pointers and reminders for shell programming. See "Shell Mistakes" (<http://www.greenend.org.uk/rjk/2001/04/shell.html>) to learn from mistakes.

Unlike shell interactive mode (see [???](#_the_simple_shell_command) and [???](#_unix_like_text_processing)), shell scripts frequently use parameters, conditionals, and loops.

### POSIX shell compatibility

Many system scripts may be interpreted by any one of [POSIX](https://en.wikipedia.org/wiki/POSIX) shells (see [???](#list-of-shell-programs)). The default shell for the system is "`/bin/sh`" which is a symlink pointing to the actual program.

- `bash(1)` for `lenny` or older

- `dash(1)` for `squeeze` or newer

Avoid writing a shell script with **bashisms** or **zshisms** to make it portable among all POSIX shells. You can check it using `checkbashisms(1)`.

| Good: POSIX                       | Avoid: bashism                     |
|:----------------------------------|:-----------------------------------|
| `if [ "$foo" = "$bar" ] ; then …` | `if [ "$foo" == "$bar" ] ; then …` |
| `diff -u file.c.orig file.c`      | `diff -u file.c{.orig,}`           |
| `mkdir /foobar /foobaz`           | `mkdir /foo{bar,baz}`              |
| `funcname() { … }`                | `function funcname() { … }`        |
| octal format: "`\377`"            | hexadecimal format: "`\xff`"       |

List of typical bashisms

The "`echo`" command must be used with following cares since its implementation differs among shell builtin and external commands.

- Avoid using any command options except "`-n`".

- Avoid using escape sequences in the string since their handling varies.

> [!NOTE]
> Although "`-n`" option is **not** really POSIX syntax, it is generally accepted.

> [!TIP]
> Use the "`printf`" command instead of the "`echo`" command if you need to embed escape sequences in the output string.

### Shell parameters

Special shell parameters are frequently used in the shell script.

| shell parameter | value                                       |
|:----------------|:--------------------------------------------|
| `$0`            | name of the shell or shell script           |
| `$1`            | first (1st) shell argument                  |
| `$9`            | ninth (9th) shell argument                  |
| `$#`            | number of positional parameters             |
| `"$*"`          | `"$1 $2 $3 $4 … "`                          |
| `"$@"`          | `"$1" "$2" "$3" "$4" …`                     |
| `$?`            | exit status of the most recent command      |
| `$$`            | PID of this shell script                    |
| `$!`            | PID of most recently started background job |

List of shell parameters

Basic **parameter expansions** to remember are as follows.

| parameter expression form | value if `var` is set | value if `var` is not set |
|:---|:---|:---|
| `${var:-string}` | "`$var`" | "`string`" |
| `${var:+string}` | "`string`" | "`null`" |
| `${var:=string}` | "`$var`" | "`string`" (and run "`var=string`") |
| `${var:?string}` | "`$var`" | echo "`string`" to **stderr** (and exit with error) |

List of shell parameter expansions

Here, the colon "`:`" in all of these operators is actually optional.

- **with** "`:`" = operator test for **exist** and **not null**

- **without** "`:`" = operator test for **exist** only

| parameter substitution form | result                         |
|:----------------------------|:-------------------------------|
| `${var%suffix}`             | remove smallest suffix pattern |
| `${var%%suffix}`            | remove largest suffix pattern  |
| `${var#prefix}`             | remove smallest prefix pattern |
| `${var##prefix}`            | remove largest prefix pattern  |

List of key shell parameter substitutions

### Shell conditionals

Each command returns an **exit status** which can be used for conditional expressions.

- Success: 0 ("True")

- Error: non 0 ("False")

> [!NOTE]
> "0" in the shell conditional context means "True", while "0" in the C conditional context means "False".

> [!NOTE]
> "`[`" is the equivalent of the `test` command, which evaluates its arguments up to "`]`" as a conditional expression.

Basic **conditional idioms** to remember are the following.

- "`<command> && <if_success_run_this_command_too> || true`"

- "`<command> || <if_not_success_run_this_command_too> || true`"

- A multi-line script snippet as the following

<!-- -->

    if [ <conditional_expression> ]; then
     <if_success_run_this_command>
    else
     <if_not_success_run_this_command>
    fi

Here trailing "`|| true`" was needed to ensure this shell script does not exit at this line accidentally when shell is invoked with "`-e`" flag.

| equation | condition to return logical true |
|:---|:---|
| `-e <file>` | \<file\> exists |
| `-d <file>` | \<file\> exists and is a directory |
| `-f <file>` | \<file\> exists and is a regular file |
| `-w <file>` | \<file\> exists and is writable |
| `-x <file>` | \<file\> exists and is executable |
| `<file1> -nt <file2>` | \<file1\> is newer than \<file2\> (modification) |
| `<file1> -ot <file2>` | \<file1\> is older than \<file2\> (modification) |
| `<file1> -ef <file2>` | \<file1\> and \<file2\> are on the same device and the same inode number |

List of file comparison operators in the conditional expression

| equation           | condition to return logical true                  |
|:-------------------|:--------------------------------------------------|
| `-z <str>`         | the length of \<str\> is zero                     |
| `-n <str>`         | the length of \<str\> is non-zero                 |
| `<str1> = <str2>`  | \<str1\> and \<str2\> are equal                   |
| `<str1> != <str2>` | \<str1\> and \<str2\> are not equal               |
| `<str1> < <str2>`  | \<str1\> sorts before \<str2\> (locale dependent) |
| `<str1> > <str2>`  | \<str1\> sorts after \<str2\> (locale dependent)  |

List of string comparison operators in the conditional expression

**Arithmetic** integer comparison operators in the conditional expression are "`-eq`", "`-ne`", "`-lt`", "`-le`", "`-gt`", and "`-ge`".

### Shell loops

There are several loop idioms to use in POSIX shell.

- "`for x in foo1 foo2 … ; do command ; done`" loops by assigning items from the list "`foo1 foo2 …`" to variable "`x`" and executing "`command`".

- "`while condition ; do command ; done`" repeats "`command`" while "`condition`" is true.

- "`until condition ; do command ; done`" repeats "`command`" while "`condition`" is not true.

- "`break`" enables to exit from the loop.

- "`continue`" enables to resume the next iteration of the loop.

> [!TIP]
> The [C](https://en.wikipedia.org/wiki/C_(programming_language))-language like numeric iteration can be realized by using `seq(1)` as the "`foo1 foo2 …`" generator.

> [!TIP]
> See [???](#_repeating_a_command_looping_over_files).

### The shell command-line processing sequence

The shell processes a script roughly as the following sequence.

- The shell reads a line.

- The shell groups a part of the line as **one token** if it is within `"…"` or `'…'`.

- The shell splits other part of a line into **tokens** by the following.

  - Whitespaces: `<space> <tab> <newline>`

  - Metacharacters: `< > | ; & ( )`

- The shell checks the **reserved word** for each token to adjust its behavior if not within `"…"` or `'…'`.

  - **reserved word**: `if then elif else fi for in while unless do done case esac`

- The shell expands **alias** if not within `"…"` or `'…'`.

- The shell expands **tilde** if not within `"…"` or `'…'`.

  - "`~`" → current user's home directory

  - "`~<user>`" → `<user>`'s home directory

- The shell expands **parameter** to its value if not within `'…'`.

  - **parameter**: "`$PARAMETER`" or "`${PARAMETER}`"

- The shell expands **command substitution** if not within `'…'`.

  - "`$( command )`" → the output of "`command`"

  - "`` ` command ` ``" → the output of "`command`"

- The shell expands **pathname glob** to matching file names if not within `"…"` or `'…'`.

  - `*` → any characters

  - `?` → one character

  - `[…]` → any one of the characters in "`…`"

- The shell looks up **command** from the following and execute it.

  - **function** definition

  - **builtin** command

  - **executable file** in "`$PATH`"

- The shell goes to the next line and repeats this process again from the top of this sequence.

Single quotes within double quotes have no effect.

Executing "`set -x`" in the shell or invoking the shell with "`-x`" option make the shell to print all of commands executed. This is quite handy for debugging.

### Utility programs for shell script

In order to make your shell program as portable as possible across Debian systems, it is a good idea to limit utility programs to ones provided by **essential** packages.

- "`aptitude search ~E`" lists **essential** packages.

- "`dpkg -L <package_name> |grep '/man/man.*/'`" lists manpages for commands offered by `<package_name>` package.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `coreutils` | @-@popcon1@-@ | @-@psize1@-@ | GNU core utilities |
| `debianutils` | @-@popcon1@-@ | @-@psize1@-@ | miscellaneous utilities specific to Debian |
| `bsdmainutils` | @-@popcon1@-@ | @-@psize1@-@ | collection of more utilities from FreeBSD |
| `bsdutils` | @-@popcon1@-@ | @-@psize1@-@ | basic utilities from 4.4BSD-Lite |
| `moreutils` | @-@popcon1@-@ | @-@psize1@-@ | additional Unix utilities |

List of packages containing small utility programs for shell scripts

> [!TIP]
> Although `moreutils` may not exist ouside of Debian, it offers interesting small programs. Most notable one is `sponge(8)` which is quite useful when you wish to overwrite original file.

### Shell script dialog

The user interface of a simple shell program can be improved from dull interaction by `echo` and `read` commands to more interactive one by using one of the so-called dialog program etc.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `x11-utils` | @-@popcon1@-@ | @-@psize1@-@ | `xmessage(1)`: display a message or query in a window (X) |
| `whiptail` | @-@popcon1@-@ | @-@psize1@-@ | displays user-friendly dialog boxes from shell scripts (newt) |
| `dialog` | @-@popcon1@-@ | @-@psize1@-@ | displays user-friendly dialog boxes from shell scripts (ncurses) |
| `zenity` | @-@popcon1@-@ | @-@psize1@-@ | display graphical dialog boxes from shell scripts (gtk2.0) |
| `ssft` | @-@popcon1@-@ | @-@psize1@-@ | Shell Scripts Frontend Tool (wrapper for zenity, kdialog, and dialog with gettext) |
| `gettext` | @-@popcon1@-@ | @-@psize1@-@ | "`/usr/bin/gettext.sh`": translate message |

List of user interface programs

### Shell script example with zenity

Here is a simple script which creates ISO image with RS02 data supplemented by `dvdisaster(1)`.

    #!/bin/sh -e
    # gmkrs02 : Copyright (C) 2007 Osamu Aoki <osamu@debian.org>, Public Domain
    #set -x
    error_exit()
    {
      echo "$1" >&2
      exit 1
    }
    # Initialize variables
    DATA_ISO="$HOME/Desktop/iso-$$.img"
    LABEL=$(date +%Y%m%d-%H%M%S-%Z)
    if [ $# != 0 ] && [ -d "$1" ]; then
      DATA_SRC="$1"
    else
      # Select directory for creating ISO image from folder on desktop
      DATA_SRC=$(zenity --file-selection --directory  \
        --title="Select the directory tree root to create ISO image") \
        || error_exit "Exit on directory selection"
    fi
    # Check size of archive
    xterm -T "Check size $DATA_SRC" -e du -s $DATA_SRC/*
    SIZE=$(($(du -s $DATA_SRC | awk '{print $1}')/1024))
    if [ $SIZE -le 520 ] ; then
      zenity --info --title="Dvdisaster RS02" --width 640  --height 400 \
        --text="The data size is good for CD backup:\\n $SIZE MB"
    elif [ $SIZE -le 3500 ]; then
      zenity --info --title="Dvdisaster RS02" --width 640  --height 400 \
        --text="The data size is good for DVD backup :\\n $SIZE MB"
    else
      zenity --info --title="Dvdisaster RS02" --width 640  --height 400 \
        --text="The data size is too big to backup : $SIZE MB"
      error_exit "The data size is too big to backup :\\n $SIZE MB"
    fi
    # only xterm is sure to have working -e option
    # Create raw ISO image
    rm -f "$DATA_ISO" || true
    xterm -T "genisoimage $DATA_ISO" \
      -e genisoimage -r -J -V "$LABEL" -o "$DATA_ISO" "$DATA_SRC"
    # Create RS02 supplemental redundancy
    xterm -T "dvdisaster $DATA_ISO" -e  dvdisaster -i "$DATA_ISO" -mRS02 -c
    zenity --info --title="Dvdisaster RS02" --width 640  --height 400 \
      --text="ISO/RS02 data ($SIZE MB) \\n created at: $DATA_ISO"
    # EOF

You may wish to create launcher on the desktop with command set something like "`/usr/local/bin/gmkrs02 %d`".

## Make

[Make](https://en.wikipedia.org/wiki/Make_(software)) is a utility to maintain groups of programs. Upon execution of `make(1)`, `make` read the rule file, "`Makefile`", and updates a target if it depends on prerequisite files that have been modified since the target was last modified, or if the target does not exist. The execution of these updates may occur concurrently.

The rule file syntax is the following.

    target: [ prerequisites ... ]
     [TAB]  command1
     [TAB]  -command2 # ignore errors
     [TAB]  @command3 # suppress echoing

Here "`[TAB]`" is a TAB code. Each line is interpreted by the shell after make variable substitution. Use "`\`" at the end of a line to continue the script. Use "`$$`" to enter "`$`" for environment values for a shell script.

Implicit rules for the target and prerequisites can be written, for example, by the following.

    %.o: %.c header.h

Here, the target contains the character "`%`" (exactly one of them). The "`%`" can match any nonempty substring in the actual target filenames. The prerequisites likewise use "`%`" to show how their names relate to the actual target name.

| automatic variable | value                                    |
|:-------------------|:-----------------------------------------|
| `$@`               | target                                   |
| `$<`               | first prerequisite                       |
| `$?`               | all newer prerequisites                  |
| `$^`               | all prerequisites                        |
| `$*`               | "`%`" matched stem in the target pattern |

List of make automatic variables

| variable expansion | description         |
|:-------------------|:--------------------|
| `foo1 := bar`      | one-time expansion  |
| `foo2 = bar`       | recursive expansion |
| `foo3 += bar`      | append              |

List of make variable expansions

Run "`make -p -f/dev/null`" to see automatic internal rules.

## C

You can set up proper environment to compile programs written in the [C programming language](https://en.wikipedia.org/wiki/C_(programming_language)) by the following.

    # apt-get install glibc-doc manpages-dev libc6-dev gcc build-essential

The `libc6-dev` package, i.e., GNU C Library, provides [C standard library](https://en.wikipedia.org/wiki/C_standard_library) which is collection of header files and library routines used by the C programming language.

See references for C as the following.

- "`info libc`" (C library function reference)

- `gcc(1)` and "`info gcc`"

- `each_C_library_function_name(3)`

- Kernighan & Ritchie, "The C Programming Language", 2nd edition (Prentice Hall)

### Simple C program (gcc)

A simple example "`example.c`" can compiled with a library "`libm`" into an executable "`run_example`" by the following.

    $ cat > example.c << EOF
    #include <stdio.h>
    #include <math.h>
    #include <string.h>

    int main(int argc, char **argv, char **envp){
            double x;
            char y[11];
            x=sqrt(argc+7.5);
            strncpy(y, argv[0], 10); /* prevent buffer overflow */
            y[10] = '\0'; /* fill to make sure string ends with '\0' */
            printf("%5i, %5.3f, %10s, %10s\n", argc, x, y, argv[1]);
            return 0;
    }
    EOF
    $ gcc -Wall -g -o run_example example.c -lm
    $ ./run_example
            1, 2.915, ./run_exam,     (null)
    $ ./run_example 1234567890qwerty
            2, 3.082, ./run_exam, 1234567890qwerty

Here, "`-lm`" is needed to link library "`/usr/lib/libm.so`" from the `libc6` package for `sqrt(3)`. The actual library is in "`/lib/`" with filename "`libm.so.6`", which is a symlink to "`libm-2.7.so`".

Look at the last parameter in the output text. There are more than 10 characters even though "`%10s`" is specified.

The use of pointer memory operation functions without boundary checks, such as `sprintf(3)` and `strcpy(3)`, is deprecated to prevent buffer overflow exploits that leverage the above overrun effects. Instead, use `snprintf(3)` and `strncpy(3)`.

## Debug

Debug is important part of programing activities. Knowing how to debug programs makes you a good Debian user who can produce meaningful bug reports.

### Basic gdb execution

Primary [debugger](https://en.wikipedia.org/wiki/Debugger) on Debian is `gdb(1)` which enables you to inspect a program while it executes.

Let's install `gdb` and related programs by the following.

    # apt-get install gdb gdb-doc build-essential devscripts

Good tutorial of `gdb` is provided by "`info gdb`" or found [elsewhere on the web](http://www.unknownroad.com/rtfm/gdbtut/gdbtoc.html). Here is a simple example of using `gdb(1)` on a "`program`" compiled with the "`-g`" option to produce debugging information.

    $ gdb program
    (gdb) b 1                # set break point at line 1
    (gdb) run args           # run program with args
    (gdb) next               # next line
    ...
    (gdb) step               # step forward
    ...
    (gdb) p parm             # print parm
    ...
    (gdb) p parm=12          # set value to 12
    ...
    (gdb) quit

> [!TIP]
> Many `gdb(1)` commands can be abbreviated. Tab expansion works as in the shell.

### Debugging the Debian package

Since all installed binaries should be stripped on the Debian system by default, most debugging symbols are removed in the normal package. In order to debug Debian packages with `gdb(1)`, either corresponding `*-dbg` packages or `*-dbgsym` packages need to be installed (e.g. `libc6-dbg` in the case of `libc6`, `coreutils-dbgsym` in the case of `coreutils`).

Old-style packages would provide its corresponding `*-dbg` package. It is placed directly inside Debian main archive alongside of the original package itself. For newer packages, they may generate `*-dbgsym` packages automatically when built and those debug packages are placed separately in [debian-debug](http://debug.mirrors.debian.org/debian-debug) archive. Please refer to [articles on Debian Wiki](https://wiki.debian.org/DebugPackage) for more information.

If a package to be debugged does not provide either its `*-dbg` package or its `*-dbgsym` package, you need to install it after rebuilding it by the following.

    $ mkdir /path/new ; cd /path/new
    $ sudo apt-get update
    $ sudo apt-get dist-upgrade
    $ sudo apt-get install fakeroot devscripts build-essential
    $ apt-get source package_name
    $ cd package_name*
    $ sudo apt-get build-dep ./

Fix bugs if needed.

Bump package version to one which does not collide with official Debian versions, e.g. one appended with "`+debug1`" when recompiling existing package version, or one appended with "`~pre1`" when compiling unreleased package version by the following.

    $ dch -i

Compile and install packages with debug symbols by the following.

    $ export DEB_BUILD_OPTIONS="nostrip noopt"
    $ debuild
    $ cd ..
    $ sudo debi package_name*.changes

You need to check build scripts of the package and ensure to use "`CFLAGS=-g -Wall`" for compiling binaries.

### Obtaining backtrace

When you encounter program crash, reporting bug report with cut-and-pasted backtrace information is a good idea.

The backtrace can be obtained by the following steps.

- Run the program under `gdb(1)`.

- Reproduce crash.

  - It causes you to be dropped back to the `gdb` prompt.

- Type "`bt`" at the `gdb` prompt.

In case of program freeze, you can crash the program by pressing `Ctrl-C` in the terminal running `gdb` to obtain `gdb` prompt.

> [!TIP]
> Often, you see a backtrace where one or more of the top lines are in "`malloc()`" or "`g_malloc()`". When this happens, chances are your backtrace isn't very useful. The easiest way to find some useful information is to set the environment variable "`$MALLOC_CHECK_`" to a value of 2 (`malloc(3)`). You can do this while running `gdb` by doing the following.

     $ MALLOC_CHECK_=2 gdb hello

### Advanced gdb commands

| command | description for command objectives |
|:---|:---|
| `(gdb) thread apply all bt` | get a backtrace for all threads for multi-threaded program |
| `(gdb) bt full` | get parameters came on the stack of function calls |
| `(gdb) thread apply all bt full` | get a backtrace and parameters as the combination of the preceding options |
| `(gdb) thread apply all bt full 10` | get a backtrace and parameters for top 10 calls to cut off irrelevant output |
| `(gdb) set logging on` | write log of `gdb` output to a file (the default is "`gdb.txt`") |

List of advanced gdb commands

### Debugging X Errors

If a GNOME program `preview1` has received an X error, you should see a message as follows.

    The program 'preview1' received an X Window System error.

If this is the case, you can try running the program with "`--sync`", and break on the "`gdk_x_error`" function in order to obtain a backtrace.

### Check dependency on libraries

Use `ldd(1)` to find out a program's dependency on libraries by the followings.

    $ ldd /bin/ls
            librt.so.1 => /lib/librt.so.1 (0x4001e000)
            libc.so.6 => /lib/libc.so.6 (0x40030000)
            libpthread.so.0 => /lib/libpthread.so.0 (0x40153000)
            /lib/ld-linux.so.2 => /lib/ld-linux.so.2 (0x40000000)

For `ls(1)` to work in a \`chroot\`ed environment, the above libraries must be available in your \`chroot\`ed environment.

See [???](#_tracing_program_activities).

### Memory leak detection tools

There are several memory leak detection tools available in Debian.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `libc6-dev` | @-@popcon1@-@ | @-@psize1@-@ | `mtrace(1)`: malloc debugging functionality in glibc |
| `valgrind` | @-@popcon1@-@ | @-@psize1@-@ | memory debugger and profiler |
| `electric-fence` | @-@popcon1@-@ | @-@psize1@-@ | `malloc(3)` debugger |
| `leaktracer` | @-@popcon1@-@ | @-@psize1@-@ | memory-leak tracer for C++ programs |
| `libdmalloc5` | @-@popcon1@-@ | @-@psize1@-@ | debug memory allocation library |

List of memory leak detection tools

### Static code analysis tools

There are [lint](https://en.wikipedia.org/wiki/Lint_programming_tool) like tools for [static code analysis](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis).

| package | popcon | size | description |
|:---|:---|:---|:---|
| `splint` | @-@popcon1@-@ | @-@psize1@-@ | tool for statically checking C programs for bugs |
| `flawfinder` | @-@popcon1@-@ | @-@psize1@-@ | tool to examine C/C++ source code and looks for security weaknesses |
| `perl` | @-@popcon1@-@ | @-@psize1@-@ | interpreter with internal static code checker: `B::Lint(3perl)` |
| `pylint` | @-@popcon1@-@ | @-@psize1@-@ | Python code static checker |
| `weblint-perl` | @-@popcon1@-@ | @-@psize1@-@ | syntax and minimal style checker for HTML |
| `linklint` | @-@popcon1@-@ | @-@psize1@-@ | fast link checker and web site maintenance tool |
| `libxml2-utils` | @-@popcon1@-@ | @-@psize1@-@ | utilities with `xmllint(1)` to validate XML files |

List of tools for static code analysis

### Disassemble binary

You can disassemble binary code with `objdump(1)` by the following.

    $  objdump -m i386 -b binary -D /usr/lib/grub/x86_64-pc/stage1

> [!NOTE]
> `gdb(1)` may be used to disassemble code interactively.

## Flex — a better Lex

[Flex](https://en.wikipedia.org/wiki/Flex_lexical_analyser) is a [Lex](https://en.wikipedia.org/wiki/Lex_programming_tool)-compatible fast [lexical analyzer](https://en.wikipedia.org/wiki/Lexical_analysis) generator.

Tutorial for `flex(1)` can be found in "`info flex`".

You need to provide your own "`main()`" and "`yywrap()`". Otherwise, your flex program should look like this to compile without a library. This is because that "`yywrap`" is a macro and "`%option main`" turns on "`%option noyywrap`" implicitly.

    %option main
    %%
    .|\n    ECHO ;
    %%

Alternatively, you may compile with the "`-lfl`" linker option at the end of your `cc(1)` command line (like AT&T-Lex with "`-ll`"). No "`%option`" is needed in this case.

## Bison — a better Yacc

Several packages provide a [Yacc](https://en.wikipedia.org/wiki/Yacc)-compatible lookahead [LR parser](https://en.wikipedia.org/wiki/LR_parser) or [LALR parser](https://en.wikipedia.org/wiki/LALR_parser) generator in Debian.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `bison` | @-@popcon1@-@ | @-@psize1@-@ | [GNU LALR parser generator](https://en.wikipedia.org/wiki/GNU_bison) |
| `byacc` | @-@popcon1@-@ | @-@psize1@-@ | Berkeley LALR parser generator |
| `btyacc` | @-@popcon1@-@ | @-@psize1@-@ | backtracking parser generator based on `byacc` |

List of Yacc-compatible LALR parser generators

Tutorial for `bison(1)` can be found in "`info bison`".

You need to provide your own "`main()`" and "`yyerror()`". "`main()`" calls "`yyparse()`" which calls "`yylex()`", usually created with Flex.

    %%

    %%

## Autoconf

[Autoconf](https://en.wikipedia.org/wiki/Autoconf) is a tool for producing shell scripts that automatically configure software source code packages to adapt to many kinds of Unix-like systems using the entire GNU build system.

`autoconf(1)` produces the configuration script "`configure`". "`configure`" automatically creates a customized "`Makefile`" using the "`Makefile.in`" template.

### Compile and install a program

> [!WARNING]
> Do not overwrite system files with your compiled programs when installing them.

Debian does not touch files in "`/usr/local/`" or "`/opt`". So if you compile a program from source, install it into "`/usr/local/`" so it does not interfere with Debian.

    $ cd src
    $ ./configure --prefix=/usr/local
    $ make
    $ make install # this puts the files in the system

### Uninstall program

If you have the original source and if it uses `autoconf(1)`/`automake(1)` and if you can remember how you configured it, execute as follows to uninstall the program.

    $ ./configure "all-of-the-options-you-gave-it"
    # make uninstall

Alternatively, if you are absolutely sure that the install process puts files only under "`/usr/local/`" and there is nothing important there, you can erase all its contents by the following.

    # find /usr/local -type f -print0 | xargs -0 rm -f

If you are not sure where files are installed, you should consider using `checkinstall(8)` from the `checkinstall` package, which provides a clean path for the uninstall. It now supports to create a Debian package with "`-D`" option.

## Perl short script madness

Although any [AWK](https://en.wikipedia.org/wiki/AWK) scripts can be automatically rewritten in [Perl](https://en.wikipedia.org/wiki/Perl) using `a2p(1)`, one-liner AWK scripts are best converted to one-liner Perl scripts manually.

Let's think following AWK script snippet.

    awk '($2=="1957") { print $3 }' |

This is equivalent to any one of the following lines.

    perl -ne '@f=split; if ($f[1] eq "1957") { print "$f[2]\n"}' |

    perl -ne 'if ((@f=split)[1] eq "1957") { print "$f[2]\n"}' |

    perl -ne '@f=split; print $f[2] if ( $f[1]==1957 )' |

    perl -lane 'print $F[2] if $F[1] eq "1957"' |

    perl -lane 'print$F[2]if$F[1]eq+1957' |

The last one is a riddle. It took advantage of following Perl features.

- The whitespace is optional.

- The automatic conversion exists from number to the string.

See `perlrun(1)` for the command-line options. For more crazy Perl scripts, [Perl Golf](http://perlgolf.sourceforge.net) may be interesting.

## Web

Basic interactive dynamic web pages can be made as follows.

- Queries are presented to the browser user using [HTML](https://en.wikipedia.org/wiki/HTML) forms.

- Filling and clicking on the form entries sends one of the following [URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator) string with encoded parameters from the browser to the web server.

  - "`http://www.foo.dom/cgi-bin/program.pl?VAR1=VAL1&VAR2=VAL2&VAR3=VAL3`"

  - "`http://www.foo.dom/cgi-bin/program.py?VAR1=VAL1&VAR2=VAL2&VAR3=VAL3`"

  - "`http://www.foo.dom/program.php?VAR1=VAL1&VAR2=VAL2&VAR3=VAL3`"

- "`%nn`" in URL is replaced with a character with hexadecimal `nn` value.

- The environment variable is set as: "`QUERY_STRING="VAR1=VAL1 VAR2=VAL2 VAR3=VAL3"`".

- [CGI](https://en.wikipedia.org/wiki/Common_Gateway_Interface) program (any one of "`program.*`") on the web server executes itself with the environment variable "`$QUERY_STRING`".

- `stdout` of CGI program is sent to the web browser and is presented as an interactive dynamic web page.

For security reasons it is better not to hand craft new hacks for parsing CGI parameters. There are established modules for them in Perl and Python. [PHP](https://en.wikipedia.org/wiki/PHP) comes with these functionalities. When client data storage is needed, [HTTP cookies](https://en.wikipedia.org/wiki/HTTP_cookie) are used. When client side data processing is needed, [Javascript](https://en.wikipedia.org/wiki/JavaScript) is frequently used.

For more, see the [Common Gateway Interface](https://en.wikipedia.org/wiki/Common_Gateway_Interface), [The Apache Software Foundation](https://en.wikipedia.org/wiki/Apache_Software_Foundation), and [JavaScript](https://en.wikipedia.org/wiki/JavaScript).

Searching "CGI tutorial" on Google by typing encoded URL <http://www.google.com/search?hl=en&ie=UTF-8&q=CGI+tutorial> directly to the browser address is a good way to see the CGI script in action on the Google server.

## The source code translation

There are programs to convert source codes.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `perl` | @-@popcon1@-@ | @-@psize1@-@ | AWK→PERL | convert source codes from AWK to PERL: `a2p(1)` |
| `f2c` | @-@popcon1@-@ | @-@psize1@-@ | FORTRAN→C | convert source codes from FORTRAN 77 to C/C++: `f2c(1)` |
| `intel2gas` | @-@popcon1@-@ | @-@psize1@-@ | intel→gas | converter from NASM (Intel format) to the GNU Assembler (GAS) |

List of source code translation tools

## Making Debian package

If you want to make a Debian package, read followings.

- [???](#_debian_package_management) to understand the basic package system

- [???](#_porting_a_package_to_the_stable_system) to understand basic porting process

- [???](#_chroot_system) to understand basic chroot techniques

- `debuild(1)`, `pbuilder(1)` and `pdebuild(1)`

- [Debugging the Debian package](#_debugging_the_debian_package) for recompiling for debugging

- [Debian New Maintainers' Guide](https://www.debian.org/doc/manuals/maint-guide/) as tutorial (the `maint-guide` package)

- [Debian Developer's Reference](https://www.debian.org/doc/manuals/developers-reference/) (the `developers-reference` package)

- [Debian Policy Manual](https://www.debian.org/doc/debian-policy/) (the `debian-policy` package)

- [Guide for Debian Maintainers](https://www.debian.org/doc/manuals/debmake-doc/) (the `debmake-doc` package)

There are packages such as `debmake`, `dh-make`, `dh-make-perl`, etc., which help packaging.
