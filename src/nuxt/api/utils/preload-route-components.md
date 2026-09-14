---
title: preloadRouteComponents
description: preloadRouteComponents allows you to manually preload individual pages
  in your Nuxt app.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/3.utils/preload-route-components.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1610
---

Preloading routes loads the components of a given route that the user might navigate to in future. This ensures that the components are available earlier and less likely to block the navigation, improving performance.

::tip{icon="i-lucide-rocket"}
Nuxt already automatically preloads the necessary routes if you're using the `NuxtLink` component.
::

:read-more{to="/docs/4.x/api/components/nuxt-link"}

## Example

Preload a route when using `navigateTo`.

```ts
// we don't await this async function, to avoid blocking rendering
// this component's setup function
preloadRouteComponents('/dashboard')

const submit = async () => {
  const results = await $fetch('/api/authentication')

  if (results.token) {
    await navigateTo('/dashboard')
  }
}
```

:read-more{to="/docs/4.x/api/utils/navigate-to"}

::note
On server, `preloadRouteComponents` will have no effect.
::
