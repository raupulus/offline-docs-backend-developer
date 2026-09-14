---
title: Enableprepostscripts
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: settings/_enablePrePostScripts.mdx
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: settings
order: 1180
---

### enablePrePostScripts

* Default: **true**
* Type: **Boolean**

When `true`, pnpm will run any pre/post scripts automatically. So running `pnpm foo`
will be like running `pnpm prefoo && pnpm foo && pnpm postfoo`.
