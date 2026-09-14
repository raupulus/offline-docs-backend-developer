---
title: pnpm ci
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: cli/ci.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: cli
order: 170
---

Added in: v11.0.0

Aliases: `clean-install`, `ic`, `install-clean`

Perform a clean install. This command runs [`pnpm clean`](clean.md) followed by [`pnpm install --frozen-lockfile`](install.md).

Designed for CI/CD environments where reproducible builds are critical.

```sh
pnpm ci
```
