---
title: Operation Controls
source_url: https://www.gnu.org/software/bash/manual
source_path: 059-operation-controls.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 590
---

## Operation Controls

`configure` recognizes the following options to control how it operates.

`--cache-file=file`  
Use and save the results of the tests in \<file\> instead of `./config.cache`. Set \<file\> to `/dev/null` to disable caching, for debugging `configure`.

`--help`  
Print a summary of the options to `configure`, and exit.

`--quiet`; `--silent`; `-q`  
Do not print messages saying which checks are being made.

`--srcdir=dir`  
Look for the Bash source code in directory \<dir\>. Usually `configure` can determine that directory automatically.

`--version`  
Print the version of Autoconf used to generate the `configure` script, and exit.

`configure` also accepts some other, not widely used, boilerplate options. ‘`configure --help`’ prints the complete list.
