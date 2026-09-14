---
title: Compilers and Options
source_url: https://www.gnu.org/software/bash/manual
source_path: 054-compilers-and-options.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 540
---

## Compilers and Options

Some systems require unusual options for compilation or linking that the `configure` script does not know about. You can give `configure` initial values for variables by setting them in the environment. Using a Bourne-compatible shell, you can do that on the command line like this:

    CC=c89 CFLAGS=-O2 LIBS=-lposix ./configure

On systems that have the `env` program, you can do it like this:

    env CPPFLAGS=-I/usr/local/include LDFLAGS=-s ./configure

The configuration process uses GCC to build Bash if it is available.
