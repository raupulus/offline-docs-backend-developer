---
title: .output
description: Nuxt creates the .output/ directory when building your application for
  production.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 2.directory-structure/0.output.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: directory-structure
order: 0
---

::important
This directory should be added to your [`.gitignore`](/docs/4.x/directory-structure/gitignore) file to avoid pushing the build output to your repository.
::

Use this directory to deploy your Nuxt application to production.

:read-more{to="/docs/4.x/getting-started/deployment"}

::warning
You should not touch any files inside since the whole directory will be re-created when running [`nuxt build`](/docs/4.x/api/commands/build).
::
