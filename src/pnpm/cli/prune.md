---
title: pnpm prune
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: cli/prune.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: cli
order: 560
---

Removes unnecessary packages.

## Options

### --prod

Remove the packages specified in `devDependencies`.

### --no-optional

Remove the packages specified in `optionalDependencies`.

:::warning

The prune command does not support recursive execution on a monorepo currently. To only install production-dependencies in a monorepo `node_modules` folders can be deleted and then re-installed with `pnpm install --prod`.

:::
