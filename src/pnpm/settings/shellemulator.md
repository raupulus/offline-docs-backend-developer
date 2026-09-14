---
title: Shellemulator
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: settings/_shellEmulator.mdx
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: settings
order: 1230
---

### shellEmulator

* Default: **false**
* Type: **Boolean**

When `true`, pnpm will use a JavaScript implementation of a [bash-like shell] to
execute scripts.

This option simplifies cross-platform scripting. For instance, by default, the
next script will fail on non-POSIX-compliant systems:

```json
"scripts": {
  "test": "NODE_ENV=test node test.js"
}
```

But if the `shellEmulator` setting is set to `true`, it will work on all
platforms.

:::note

Node.js 22 or higher supports running scripts without pnpm's assistance. For the example above, you can run the `test` script with `node --run test`. However, the `shellEmulator` option has no effect on this. Scripts that depend on POSIX features are required to be run `pnpm run` instead of `node --run` to work in non-POSIX-compliant environments.

:::

[bash-like shell]: https://www.npmjs.com/package/@yarnpkg/shell
