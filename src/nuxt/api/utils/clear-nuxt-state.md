---
title: clearNuxtState
description: Delete the cached state of useState.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/3.utils/clear-nuxt-state.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1470
---

::note
This method is useful if you want to invalidate the state of `useState`. You can also reset the state to its initial value by passing `{ reset: true }` as the second parameter.
::

## Type

```ts [Signature]
export function clearNuxtState (keys?: string | string[] | ((key: string) => boolean), opts?: ClearNuxtStateOptions): void
```

## Parameters

- `keys`: One or an array of keys that are used in [`useState`](/docs/4.x/api/composables/use-state) to delete their cached state. If no keys are provided, **all state** will be invalidated.
- `opts`: An options object to configure the clear behavior.
  - `reset` :badge[v4.4]{color="info" size="xs" class="align-middle"}: When set to `true`, resets the state to the initial value provided by the `init` function of [`useState`](/docs/4.x/api/composables/use-state) instead of setting it to `undefined`. When not specified, defaults to the value of `experimental.defaults.useState.resetOnClear` in your Nuxt config (which is `true` with `compatibilityVersion: 5`).
