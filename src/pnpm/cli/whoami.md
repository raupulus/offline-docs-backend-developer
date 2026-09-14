---
title: pnpm whoami
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: cli/whoami.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: cli
order: 810
---

Added in: v11.0.0

Print the username associated with the current registry credentials.

```sh
pnpm whoami [--registry <url>]
```

If you are not logged in, the command exits with an error. Use [`pnpm login`](login.md) to authenticate first.

## Options

### --registry &lt;url\>

The registry to check. Defaults to the configured default registry.
