---
title: Scriptshell
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: settings/_scriptShell.mdx
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: settings
order: 1220
---

### scriptShell

* Default: **null**
* Type: **path**

The shell to use for scripts run with the `pnpm run` command.

For instance, to force usage of Git Bash on Windows:

```
pnpm config set scriptShell "C:\\Program Files\\git\\bin\\bash.exe"
```
