---
title: nuxt.config.ts
description: Nuxt can be easily configured with a single nuxt.config file.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 2.directory-structure/3.nuxt-config.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: directory-structure
order: 3
---

The `nuxt.config` file extension can either be `.js`, `.ts` or `.mjs`.

```ts twoslash [nuxt.config.ts]
export default defineNuxtConfig({
  // My Nuxt config
})
```

::tip
`defineNuxtConfig` helper is globally available without import.
::

You can explicitly import `defineNuxtConfig` from `nuxt/config` if you prefer:

```ts twoslash [nuxt.config.ts]
import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  // My Nuxt config
})
```

::read-more{to="/docs/4.x/api/configuration/nuxt-config"}
Discover all the available options in the **Nuxt configuration** documentation.
::

To ensure your configuration is up to date, Nuxt will make a full restart when detecting changes in the main configuration file, the [`.env`](/docs/4.x/directory-structure/env), [`.nuxtignore`](/docs/4.x/directory-structure/nuxtignore) and [`.nuxtrc`](/docs/4.x/directory-structure/nuxtrc) dotfiles.
