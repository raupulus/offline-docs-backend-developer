---
title: nuxt build
description: Build your Nuxt application.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/4.commands/build.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1730
---

<!--build-cmd-->
```bash [Terminal]
npx nuxt build [ROOTDIR] [--cwd=<directory>] [--logLevel=<silent|info|verbose>] [--prerender] [--preset] [--dotenv] [--envName] [-e, --extends=<layer-name>] [--profile[=verbose]]
```
<!--/build-cmd-->

The `build` command creates a `.output` directory with all your application, server and dependencies ready for production.

## Arguments

<!--build-args-->
| Argument      | Description                                    |
|---------------|------------------------------------------------|
| `ROOTDIR="."` | Specifies the working directory (default: `.`) |
<!--/build-args-->

## Options

<!--build-opts-->
| Option                               | Default | Description                                                                                                                                          |
|--------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--cwd=<directory>`                  |         | Specify the working directory, this takes precedence over ROOTDIR (default: `.`)                                                                     |
| `--logLevel=<silent\|info\|verbose>` |         | Specify build-time log level                                                                                                                         |
| `--prerender`                        |         | Build Nuxt and prerender static routes                                                                                                               |
| `--preset=<preset>`                  |         | Specify Nitro server preset. Available presets depend on Nitro (e.g. `node-server`, `vercel`, `netlify`, `static`)                                  |
| `--dotenv`                           |         | Path to `.env` file to load, relative to the root directory                                                                                          |
| `--envName`                          |         | The environment to use when resolving configuration overrides (default is `production` when building, and `development` when running the dev server) |
| `-e, --extends=<layer-name>`         |         | Extend from a Nuxt layer                                                                                                                             |
| `--profile` :badge[v4.4]{color="info" size="xs" class="align-middle"} |         | Profile performance. Writes a V8 CPU profile and JSON report on exit. Use `--profile=verbose` for a full console report.                             |
<!--/build-opts-->

::note
This command sets `process.env.NODE_ENV` to `production`.
::

::note
`--prerender` will always set the `preset` to `static`
::
