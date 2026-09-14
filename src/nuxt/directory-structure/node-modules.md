---
title: nodemodules
description: The package manager stores the dependencies of your project in the node_modules/
  directory.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 2.directory-structure/1.node_modules.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: directory-structure
order: 1
---

The package manager ([`npm`](https://docs.npmjs.com/cli/commands/npm/) or [`yarn`](https://yarnpkg.com) or [`pnpm`](https://pnpm.io/cli/install) or [`bun`](https://bun.com/package-manager) or [`deno`](https://docs.deno.com/runtime/getting_started/installation/)) creates this directory to store the dependencies of your project.

::important
This directory should be added to your [`.gitignore`](/docs/4.x/directory-structure/gitignore) file to avoid pushing the dependencies to your repository.
::
