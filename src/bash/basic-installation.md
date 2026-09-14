---
title: Basic Installation
source_url: https://www.gnu.org/software/bash/manual
source_path: 053-basic-installation.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 530
---

## Basic Installation

installation

configuration

Bash installation

Bash configuration

These are installation instructions for Bash.

The simplest way to compile Bash is:

1.  `cd` to the directory containing the source code and type ‘`./configure`’ to configure Bash for your system. If you’re using `csh` on an old version of System V, you might need to type ‘`sh ./configure`’ instead to prevent `csh` from trying to execute `configure` itself.

    Running `configure` takes some time. While running, it prints messages telling which features it is checking for.

2.  Type ‘`make`’ to compile Bash and build the `bashbug` bug reporting script.

3.  Optionally, type ‘`make tests`’ to run the Bash test suite.

4.  Type ‘`make install`’ to install `bash` and `bashbug`. This will also install the manual pages and Info file, message translation files, some supplemental documentation, a number of example loadable builtin commands, and a set of header files for developing loadable builtins. You may need additional privileges to install `bash` to your desired destination, which may require ‘`sudo make install`’. More information about controlling the locations where `bash` and other files are installed is below (see [Installation Names](#Installation-Names)).

The `configure` shell script attempts to guess correct values for various system-dependent variables used during compilation. It uses those values to create a `Makefile` in each directory of the package (the top directory, the `builtins`, `doc`, `po`, and `support` directories, each directory under `lib`, and several others). It also creates a `config.h` file containing system-dependent definitions. Finally, it creates a shell script named `config.status` that you can run in the future to recreate the current configuration, a file `config.cache` that saves the results of its tests to speed up reconfiguring, and a file `config.log` containing compiler output (useful mainly for debugging `configure`). If at some point `config.cache` contains results you don’t want to keep, you may remove or edit it.

To find out more about the options and arguments that the `configure` script understands, type

    bash-4.2$ ./configure --help

at the Bash prompt in your Bash source directory.

If you want to build Bash in a directory separate from the source directory – to build for multiple architectures, for example – just use the full path to the configure script. The following commands will build Bash in a directory under `/usr/local/build` from the source code in `/usr/local/src/bash-4.4`:

    mkdir /usr/local/build/bash-4.4
    cd /usr/local/build/bash-4.4
    bash /usr/local/src/bash-4.4/configure
    make

See [Compiling For Multiple Architectures](#Compiling-For-Multiple-Architectures) for more information about building in a directory separate from the source.

If you need to do unusual things to compile Bash, please try to figure out how `configure` could check whether or not to do them, and mail diffs or instructions to <bash-maintainers@gnu.org> so they can be considered for the next release.

The file `configure.ac` is used to create `configure` by a program called Autoconf. You only need `configure.ac` if you want to change it or regenerate `configure` using a newer version of Autoconf. If you do this, make sure you are using Autoconf version 2.69 or newer.

You can remove the program binaries and object files from the source code directory by typing ‘`make clean`’. To also remove the files that `configure` created (so you can compile Bash for a different kind of computer), type ‘`make distclean`’.
