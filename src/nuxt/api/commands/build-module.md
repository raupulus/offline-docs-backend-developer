---
title: nuxt build-module
description: Nuxt command to build your Nuxt module before publishing.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/4.commands/build-module.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1720
---

<!--build-module-cmd-->
```bash [Terminal]
npx nuxt build-module [ROOTDIR] [--cwd=<directory>] [--logLevel=<silent|info|verbose>] [--build] [--stub] [--sourcemap] [--prepare]
```
<!--/build-module-cmd-->

The `build-module` command runs `@nuxt/module-builder` to generate `dist` directory within your `rootDir` that contains the full build for your **nuxt-module**.

## Arguments

<!--build-module-args-->
| Argument      | Description                                    |
|---------------|------------------------------------------------|
| `ROOTDIR="."` | Specifies the working directory (default: `.`) |
<!--/build-module-args-->

## Options

<!--build-module-opts-->
| Option                               | Default | Description                                                                      |
|--------------------------------------|---------|----------------------------------------------------------------------------------|
| `--cwd=<directory>`                  |         | Specify the working directory, this takes precedence over ROOTDIR (default: `.`) |
| `--logLevel=<silent\|info\|verbose>` |         | Specify build-time log level                                                     |
| `--build`                            | `false` | Build module for distribution                                                    |
| `--stub`                             | `false` | Stub dist instead of actually building it for development                        |
| `--sourcemap`                        | `false` | Generate sourcemaps                                                              |
| `--prepare`                          | `false` | Prepare module for local development                                             |
<!--/build-module-opts-->

::read-more{to="https://github.com/nuxt/module-builder" icon="i-simple-icons-github" target="\_blank"}
Read more about `@nuxt/module-builder`.
::
