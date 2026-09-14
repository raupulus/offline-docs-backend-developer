---
title: pnpm import
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: cli/import.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: cli
order: 330
---

`pnpm import` generates a `pnpm-lock.yaml` from another package manager's lockfile. Supported source files:
* `package-lock.json`
* `npm-shrinkwrap.json`
* `yarn.lock`

Note that if you have workspaces you wish to import dependencies for, they will need to be declared in a [pnpm-workspace.yaml](../settings.md) file beforehand.
