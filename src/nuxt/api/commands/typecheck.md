---
title: nuxt typecheck
description: The typecheck command runs vue-tsc to check types throughout your app.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/4.commands/typecheck.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1840
---

<!--typecheck-cmd-->
```bash [Terminal]
npx nuxt typecheck [ROOTDIR] [--cwd=<directory>] [--logLevel=<silent|info|verbose>] [--dotenv] [-e, --extends=<layer-name>]
```
<!--/typecheck-cmd-->

The `typecheck` command runs [`vue-tsc`](https://github.com/vuejs/language-tools/tree/master/packages/tsc) to check types throughout your app.

## Arguments

<!--typecheck-args-->
| Argument      | Description                                    |
|---------------|------------------------------------------------|
| `ROOTDIR="."` | Specifies the working directory (default: `.`) |
<!--/typecheck-args-->

## Options

<!--typecheck-opts-->
| Option                               | Default | Description                                                                      |
|--------------------------------------|---------|----------------------------------------------------------------------------------|
| `--cwd=<directory>`                  |         | Specify the working directory, this takes precedence over ROOTDIR (default: `.`) |
| `--logLevel=<silent\|info\|verbose>` |         | Specify build-time log level                                                     |
| `--dotenv`                           |         | Path to `.env` file to load, relative to the root directory                      |
| `-e, --extends=<layer-name>`         |         | Extend from a Nuxt layer                                                         |
<!--/typecheck-opts-->

::note
This command sets `process.env.NODE_ENV` to `production`. To override, define `NODE_ENV` in a [`.env`](/docs/4.x/directory-structure/env) file or as a command-line argument.
::

::read-more{to="/docs/4.x/guide/concepts/typescript#type-checking"}
Read more on how to enable type-checking at build or development time.
::
