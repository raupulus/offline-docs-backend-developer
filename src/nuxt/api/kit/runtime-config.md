---
title: Runtime Config
description: Nuxt Kit provides a set of utilities to help you access and modify Nuxt
  runtime configuration.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/5.kit/10.runtime-config.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 10
---

## `useRuntimeConfig`

At build-time, it is possible to access the resolved Nuxt [runtime config](/docs/4.x/guide/going-further/runtime-config).

### Type

```ts
function useRuntimeConfig (): Record<string, unknown>
```

## `updateRuntimeConfig`

It is also possible to update runtime configuration. This will be merged with the existing runtime configuration, and if Nitro has already been initialized it will trigger an HMR event to reload the Nitro runtime config.

### Type

```ts
function updateRuntimeConfig (config: Record<string, unknown>): void | Promise<void>
```
