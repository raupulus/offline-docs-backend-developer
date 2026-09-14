---
title: useError
description: useError composable returns the global Nuxt error that is being handled.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/2.composables/use-error.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1150
---

## Usage

The `useError` composable returns the global Nuxt error that is being handled and is available on both client and server. It provides a reactive, SSR-friendly error state across your app.

```ts
const error = useError()
```

You can use this composable in your components, pages, or plugins to access or react to the current Nuxt error.

## Type

```ts
interface NuxtError<DataT = unknown> {
  status: number
  statusText?: string
  message: string
  data?: DataT
  cause?: unknown
  fatal: boolean
}

export const useError: () => Ref<NuxtError | undefined>
```

## Parameters

This composable does not take any parameters.

## Return Values

Returns a `Ref` containing the current Nuxt error (or `undefined` if there is no error). The error object is reactive and will update automatically when the error state changes.

## Example

```vue
<script setup lang="ts">
const error = useError()

if (error.value) {
  console.error('Nuxt error:', error.value)
}
</script>
```

:read-more{to="/docs/4.x/getting-started/error-handling"}
