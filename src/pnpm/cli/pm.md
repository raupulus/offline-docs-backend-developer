---
title: pnpm pm
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: cli/pm.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: cli
order: 530
---

The `pnpm pm <command>` syntax always runs the built-in pnpm command, bypassing any same-named script in `package.json`.

Some built-in commands can be overridden by scripts. For example, if your project defines a `"clean"` script in `package.json`, then `pnpm clean` runs that script instead of the built-in [`pnpm clean`](clean.md). Using `pnpm pm clean` forces the built-in command to run.

## Example

```json title="package.json"
{
  "scripts": {
    "clean": "rm -rf dist"
  }
}
```

```sh
# Runs the "clean" script from package.json
pnpm clean
# or explicitly:
pnpm run clean

# Runs the built-in pnpm clean command (removes node_modules)
pnpm pm clean
```
