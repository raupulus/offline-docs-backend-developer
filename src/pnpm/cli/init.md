---
title: pnpm init
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: cli/init.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: cli
order: 340
---

Create a `package.json` file.

## Options

### --bare

Added in: v10.25.0

Creates a `package.json` with only the required fields.

### --init-type &lt;type\>

* Default: **module**
* Type: **commonjs**, **module**

Set the module system for the package.

### --init-package-manager

Pin the project to the current pnpm version.

Since v11, the pin is written as a [`devEngines.packageManager`](../package-json.md#devenginespackagemanager) entry (instead of the legacy `packageManager` field), so version ranges are supported and the resolved version is captured in `pnpm-lock.yaml`.

Inside a workspace subpackage this flag has no effect — the `devEngines.packageManager` field is only added to the workspace root's `package.json`.
