---
title: setPageLayout
description: setPageLayout allows you to dynamically change the layout of a page.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/3.utils/set-page-layout.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1660
---

::important
`setPageLayout` allows you to dynamically change the layout of a page. It relies on access to the Nuxt context and therefore can only be called within the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context).
::

```ts [app/middleware/custom-layout.ts]
export default defineNuxtRouteMiddleware((to) => {
  // Set the layout on the route you are navigating _to_
  setPageLayout('other')
})
```

## Passing Props to Layouts :badge[v4.3]{color="info" size="xs" class="align-middle"}

You can pass props to the layout by providing an object as the second argument:

```ts [app/middleware/admin-layout.ts]
export default defineNuxtRouteMiddleware((to) => {
  setPageLayout('admin', {
    sidebar: true,
    title: 'Dashboard',
  })
})
```

The layout can then receive these props:

```vue [app/layouts/admin.vue]
<script setup lang="ts">
const props = defineProps<{
  sidebar?: boolean
  title?: string
}>()
</script>

<template>
  <div>
    <aside v-if="sidebar">
      Sidebar
    </aside>
    <main>
      <h1>{{ title }}</h1>
      <slot />
    </main>
  </div>
</template>
```

::note
If you choose to set the layout dynamically on the server side, you _must_ do so before the layout is rendered by Vue (that is, within a plugin or route middleware) to avoid a hydration mismatch.
::
