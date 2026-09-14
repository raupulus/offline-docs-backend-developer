---
title: App Config
description: Nuxt Kit provides a set of utilities to help you access and modify Nuxt
  app configuration.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/5.kit/11.app-config.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 11
---

## `updateAppConfig`

Update the app configuration that will be applied to `nuxt.options.appConfig`. This is useful for modules to set default values that can be overridden by user configuration. The update is merged with the existing configuration using [`defu`](https://github.com/unjs/defu).

### Type

```ts
function updateAppConfig (appConfig: Record<string, unknown>): void
```

### Example

```ts
import { defineNuxtModule, updateAppConfig } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    updateAppConfig({
      myModule: {
        option: 'value',
      },
    })
  },
})
```
