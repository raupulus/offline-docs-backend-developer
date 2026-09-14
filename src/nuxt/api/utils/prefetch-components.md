---
title: prefetchComponents
description: Nuxt provides utilities to give you control over prefetching components.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/3.utils/prefetch-components.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1590
---

Prefetching component downloads the code in the background, this is based on the assumption that the component will likely be used for rendering, enabling the component to load instantly if and when the user requests it. The component is downloaded and cached for anticipated future use without the user making an explicit request for it.

Use `prefetchComponents` to manually prefetch individual components that have been registered globally in your Nuxt app. By default Nuxt registers these as async components. You must use the Pascal-cased version of the component name.

```ts
await prefetchComponents('MyGlobalComponent')

await prefetchComponents(['MyGlobalComponent1', 'MyGlobalComponent2'])
```

::note
Current implementation behaves exactly the same as [`preloadComponents`](/docs/4.x/api/utils/preload-components) by preloading components instead of just prefetching we are working to improve this behavior.
::

::note
On server, `prefetchComponents` will have no effect.
::
