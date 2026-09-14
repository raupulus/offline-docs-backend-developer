---
title: nuxt module
description: Search and add modules to your Nuxt application with the command line.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/4.commands/module.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1800
---

Nuxt provides a few utilities to work with [Nuxt modules](/modules) seamlessly.

## `nuxt module add`

<!--module-add-cmd-->
```bash [Terminal]
npx nuxt module add <MODULENAME> [--cwd=<directory>] [--logLevel=<silent|info|verbose>] [--skipInstall] [--skipConfig] [--dev]
```
<!--/module-add-cmd-->

<!--module-add-args-->
| Argument     | Description                                                         |
|--------------|---------------------------------------------------------------------|
| `MODULENAME` | Specify one or more modules to install by name, separated by spaces |
<!--/module-add-args-->

<!--module-add-opts-->
| Option                               | Default | Description                         |
|--------------------------------------|---------|-------------------------------------|
| `--cwd=<directory>`                  | `.`     | Specify the working directory       |
| `--logLevel=<silent\|info\|verbose>` |         | Specify build-time log level        |
| `--skipInstall`                      |         | Skip npm install                    |
| `--skipConfig`                       |         | Skip nuxt.config.ts update          |
| `--dev`                              |         | Install modules as dev dependencies |
<!--/module-add-opts-->

The command lets you install [Nuxt modules](/modules) in your application with no manual work.

When running the command, it will:

- install the module as a dependency using your package manager
- add it to your [package.json](/docs/4.x/directory-structure/package) file
- update your [`nuxt.config`](/docs/4.x/directory-structure/nuxt-config) file

**Example:**

Installing the [`Pinia`](/modules/pinia) module

```bash [Terminal]
npx nuxt module add pinia
```

## `nuxt module search`

<!--module-search-cmd-->
```bash [Terminal]
npx nuxt module search <QUERY> [--cwd=<directory>] [--nuxtVersion=<2|3>]
```
<!--/module-search-cmd-->

### Arguments

<!--module-search-args-->
| Argument | Description            |
|----------|------------------------|
| `QUERY`  | keywords to search for |
<!--/module-search-args-->

### Options

<!--module-search-opts-->
| Option                 | Default | Description                                                                        |
|------------------------|---------|------------------------------------------------------------------------------------|
| `--cwd=<directory>`    | `.`     | Specify the working directory                                                      |
| `--nuxtVersion=<2\|3>` |         | Filter by Nuxt version and list compatible modules only (auto detected by default) |
<!--/module-search-opts-->

The command searches for Nuxt modules matching your query that are compatible with your Nuxt version.

**Example:**

```bash [Terminal]
npx nuxt module search pinia
```
