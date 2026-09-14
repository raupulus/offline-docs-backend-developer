---
title: pnpm dedupe
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: cli/dedupe.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: cli
order: 210
---

Perform an install removing older dependencies in the lockfile if a newer version can be used.

## Options

### `--check`

Check if running dedupe would result in changes without installing packages or editing the lockfile. Exits with a non-zero status code if changes are possible.
