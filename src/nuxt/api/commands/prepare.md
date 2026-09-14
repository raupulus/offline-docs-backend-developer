---
title: nuxt prepare
description: The prepare command creates a .nuxt directory in your application and
  generates types.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/4.commands/prepare.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1810
---

<!--prepare-cmd-->
```bash [Terminal]
npx nuxt prepare [ROOTDIR] [--dotenv] [--cwd=<directory>] [--logLevel=<silent|info|verbose>] [--envName] [-e, --extends=<layer-name>]
```
<!--/prepare-cmd-->

The `prepare` command creates a [`.nuxt`](/docs/4.x/directory-structure/nuxt) directory in your application and generates types. This can be useful in a CI environment or as a `postinstall` command in your [`package.json`](/docs/4.x/directory-structure/package).

## Arguments

<!--prepare-args-->
| Argument      | Description                                    |
|---------------|------------------------------------------------|
| `ROOTDIR="."` | Specifies the working directory (default: `.`) |
<!--/prepare-args-->

## Options

<!--prepare-opts-->
| Option                               | Default | Description                                                                                                                                          |
|--------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--dotenv`                           |         | Path to `.env` file to load, relative to the root directory                                                                                          |
| `--cwd=<directory>`                  |         | Specify the working directory, this takes precedence over ROOTDIR (default: `.`)                                                                     |
| `--logLevel=<silent\|info\|verbose>` |         | Specify build-time log level                                                                                                                         |
| `--envName`                          |         | The environment to use when resolving configuration overrides (default is `production` when building, and `development` when running the dev server) |
| `-e, --extends=<layer-name>`         |         | Extend from a Nuxt layer                                                                                                                             |
<!--/prepare-opts-->

::note
This command sets `process.env.NODE_ENV` to `production`.
::
