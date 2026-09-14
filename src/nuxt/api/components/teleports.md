---
title: <Teleport>
description: The <Teleport> component teleports a component to a different location
  in the DOM.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/1.components/11.teleports.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 11
---

::warning
The `to` target of [`<Teleport>`](https://vuejs.org/guide/built-ins/teleport) expects a CSS selector string or an actual DOM node. Nuxt currently has SSR support for teleports to `#teleports` only, with client-side support for other targets using a `<ClientOnly>` wrapper.
::

## Body Teleport

```vue
<template>
  <button @click="open = true">
    Open Modal
  </button>
  <Teleport to="#teleports">
    <div
      v-if="open"
      class="modal"
    >
      <p>Hello from the modal!</p>
      <button @click="open = false">
        Close
      </button>
    </div>
  </Teleport>
</template>
```

## Client-side Teleport

```vue
<template>
  <ClientOnly>
    <Teleport to="#some-selector">
      <!-- content -->
    </Teleport>
  </ClientOnly>
</template>
```

:link-example{to="/docs/4.x/examples/advanced/teleport"}
