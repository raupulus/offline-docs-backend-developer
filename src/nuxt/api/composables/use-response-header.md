---
title: useResponseHeader
description: Use useResponseHeader to set a server response header.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/2.composables/use-response-header.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1320
---

::important
This composable is available in Nuxt v3.14+.
::

You can use the built-in [`useResponseHeader`](/docs/4.x/api/composables/use-response-header) composable to set any server response header within your pages, components, and plugins.

```ts
// Set a custom response header
const header = useResponseHeader('X-My-Header')
header.value = 'my-value'
```

## Example

We can use `useResponseHeader` to easily set a response header on a per-page basis.

```vue [app/pages/test.vue]
<script setup>
// pages/test.vue
const header = useResponseHeader('X-My-Header')
header.value = 'my-value'
</script>

<template>
  <h1>Test page with custom header</h1>
  <p>The response from the server for this "/test" page will have a custom "X-My-Header" header.</p>
</template>
```

We can use `useResponseHeader` for example in Nuxt [middleware](/docs/4.x/directory-structure/app/middleware) to set a response header for all pages.

```ts [app/middleware/my-header-middleware.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const header = useResponseHeader('X-My-Always-Header')
  header.value = `I'm Always here!`
})
```
