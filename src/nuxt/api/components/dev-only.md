---
title: <DevOnly>
description: Render components only during development with the <DevOnly> component.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/1.components/1.dev-only.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1
---

Nuxt provides the `<DevOnly>` component to render a component only during development.

The content will not be included in production builds.

```vue [app/pages/example.vue]
<template>
  <div>
    <Sidebar />
    <DevOnly>
      <!-- this component will only be rendered during development -->
      <LazyDebugBar />

      <!-- if you ever require to have a replacement during production -->
      <!-- be sure to test these using `nuxt preview` -->
      <template #fallback>
        <div><!-- empty div for flex.justify-between --></div>
      </template>
    </DevOnly>
  </div>
</template>
```

## Slots

- `#fallback`: if you ever require to have a replacement during production.

```vue
<template>
  <div>
    <Sidebar />
    <DevOnly>
      <!-- this component will only be rendered during development -->
      <LazyDebugBar />
      <!-- be sure to test these using `nuxt preview` -->
      <template #fallback>
        <div><!-- empty div for flex.justify-between --></div>
      </template>
    </DevOnly>
  </div>
</template>
```
