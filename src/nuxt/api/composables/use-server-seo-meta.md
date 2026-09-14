---
title: useServerSeoMeta
description: The useServerSeoMeta composable lets you define your site's SEO meta
  tags as a flat object with full TypeScript support.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/2.composables/use-server-seo-meta.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1390
---

::warning
`useServerSeoMeta` is deprecated. Wrap [`useSeoMeta`](/docs/4.x/api/composables/use-seo-meta) in an `if (import.meta.server)` block instead. The auto-import is removed under `future.compatibilityVersion: 5`.
::

`useServerSeoMeta` lets you define your site's SEO meta tags as a flat object with full TypeScript support, exactly like [`useSeoMeta`](/docs/4.x/api/composables/use-seo-meta), but it only runs server-side and is tree-shaken from the client bundle.

:read-more{to="/docs/4.x/api/composables/use-seo-meta"}

For new code, use the server-only pattern directly:

```vue [app/app.vue]
<script setup lang="ts">
if (import.meta.server) {
  useSeoMeta({
    robots: 'index, follow',
  })
}
</script>
```

Parameters are exactly the same as with [`useSeoMeta`](/docs/4.x/api/composables/use-seo-meta).

:read-more{to="/docs/4.x/getting-started/seo-meta"}
