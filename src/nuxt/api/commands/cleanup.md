---
title: nuxt cleanup
description: Remove common generated Nuxt files and caches.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/4.commands/cleanup.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1740
---

<!--cleanup-cmd-->
```bash [Terminal]
npx nuxt cleanup [ROOTDIR] [--cwd=<directory>]
```
<!--/cleanup-cmd-->

The `cleanup` command removes common generated Nuxt files and caches, including:

- `.nuxt`
- `.output`
- `node_modules/.vite`
- `node_modules/.cache`

## Arguments

<!--cleanup-args-->
| Argument      | Description                                    |
|---------------|------------------------------------------------|
| `ROOTDIR="."` | Specifies the working directory (default: `.`) |
<!--/cleanup-args-->

## Options

<!--cleanup-opts-->
| Option              | Default | Description                                                                      |
|---------------------|---------|----------------------------------------------------------------------------------|
| `--cwd=<directory>` |         | Specify the working directory, this takes precedence over ROOTDIR (default: `.`) |
<!--/cleanup-opts-->
