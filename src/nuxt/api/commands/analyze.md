---
title: nuxt analyze
description: Analyze the production bundle or your Nuxt application.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/4.commands/analyze.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1710
---

<!--analyze-cmd-->
```bash [Terminal]
npx nuxt analyze [ROOTDIR] [--cwd=<directory>] [--logLevel=<silent|info|verbose>] [--dotenv] [-e, --extends=<layer-name>] [--name=<name>] [--no-serve]
```
<!--/analyze-cmd-->

The `analyze` command builds Nuxt and analyzes the production bundle (experimental).

## Arguments

<!--analyze-args-->
| Argument      | Description                                    |
|---------------|------------------------------------------------|
| `ROOTDIR="."` | Specifies the working directory (default: `.`) |
<!--/analyze-args-->

## Options

<!--analyze-opts-->
| Option                               | Default   | Description                                                                      |
|--------------------------------------|-----------|----------------------------------------------------------------------------------|
| `--cwd=<directory>`                  |           | Specify the working directory, this takes precedence over ROOTDIR (default: `.`) |
| `--logLevel=<silent\|info\|verbose>` |           | Specify build-time log level                                                     |
| `--dotenv`                           |           | Path to `.env` file to load, relative to the root directory                      |
| `-e, --extends=<layer-name>`         |           | Extend from a Nuxt layer                                                         |
| `--name=<name>`                      | `default` | Name of the analysis                                                             |
| `--no-serve`                         |           | Skip serving the analysis results                                                |
<!--/analyze-opts-->

::note
This command sets `process.env.NODE_ENV` to `production`.
::
