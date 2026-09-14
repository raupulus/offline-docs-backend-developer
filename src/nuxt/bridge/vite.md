---
title: Vite
description: Activate Vite to your Nuxt 2 application with Nuxt Bridge.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 6.bridge/9.vite.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: bridge
order: 9
---

::warning
When using `vite`, [nitro](/docs/4.x/bridge/nitro) must have been configured.
::

## Remove Modules

- Remove `nuxt-vite`: Bridge enables same functionality

## Update Config

```ts [nuxt.config.ts]
import { defineNuxtConfig } from '@nuxt/bridge'

export default defineNuxtConfig({
  bridge: {
    vite: true,
    nitro: true,
  },
})
```

## Configuration

```ts [nuxt.config.ts]
import { defineNuxtConfig } from '@nuxt/bridge'

export default defineNuxtConfig({
  vite: {
    // Config for Vite
  },
})
```
