---
title: useRequestHeaders
description: Use useRequestHeaders to access the incoming request headers.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/2.composables/use-request-headers.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1300
---

You can use built-in [`useRequestHeaders`](/docs/4.x/api/composables/use-request-headers) composable to access the incoming request headers within your pages, components, and plugins.

```ts
// Get all request headers
const headers = useRequestHeaders()

// Get only cookie request header
const { cookie } = useRequestHeaders(['cookie'])
```

::tip
In the browser, `useRequestHeaders` will return an empty object.
::

## Example

We can use `useRequestHeaders` to access and proxy the initial request's `authorization` header to any future internal requests during SSR.

The example below adds the `authorization` request header to an isomorphic `$fetch` call.

```vue [app/pages/some-page.vue]
<script setup lang="ts">
const { data } = await useFetch('/api/confidential', {
  headers: useRequestHeaders(['authorization']),
})
</script>
```
