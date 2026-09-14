---
title: pnpm search
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: cli/search.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: cli
order: 660
---

Added in: v11.0.0

Aliases: `s`, `se`, `find`

Search the registry for packages matching the given keywords.

```sh
pnpm search <keyword> [<keyword> ...]
```

## Examples

```sh
pnpm search webpack plugin
pnpm search @types/node
```

## Options

### --json

Output search results in JSON format.

### --search-limit &lt;number\>

* Default: **20**

Maximum number of results to show.
