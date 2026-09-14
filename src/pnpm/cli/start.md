---
title: pnpm start
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: cli/start.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: cli
order: 720
---

Aliases: `run start`

Runs an arbitrary command specified in the package's `start` property of its
`scripts` object. If no `start` property is specified on the `scripts` object,
it will attempt to run `node server.js` as a default, failing if neither are
present.

The intended usage of the property is to specify a command that starts your
program.
