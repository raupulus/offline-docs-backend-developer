---
title: nuxt test
description: The test command runs tests using @nuxt/test-utils.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/4.commands/test.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1830
---

<!--test-cmd-->
```bash [Terminal]
npx nuxt test [ROOTDIR] [--cwd=<directory>] [--logLevel=<silent|info|verbose>] [--dev] [--watch]
```
<!--/test-cmd-->

The `test` command runs tests using [`@nuxt/test-utils`](/docs/4.x/getting-started/testing). This command sets `process.env.NODE_ENV` to `test` if not already set.

## Arguments

<!--test-args-->
| Argument      | Description                                    |
|---------------|------------------------------------------------|
| `ROOTDIR="."` | Specifies the working directory (default: `.`) |
<!--/test-args-->

## Options

<!--test-opts-->
| Option                               | Default | Description                                                                      |
|--------------------------------------|---------|----------------------------------------------------------------------------------|
| `--cwd=<directory>`                  |         | Specify the working directory, this takes precedence over ROOTDIR (default: `.`) |
| `--logLevel=<silent\|info\|verbose>` |         | Specify build-time log level                                                     |
| `--dev`                              |         | Run in dev mode                                                                  |
| `--watch`                            |         | Watch mode                                                                       |
<!--/test-opts-->

::note
This command sets `process.env.NODE_ENV` to `test`.
::
