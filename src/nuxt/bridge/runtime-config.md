---
title: Runtime Config
description: Nuxt provides a runtime config API to expose configuration and secrets
  within your application.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 6.bridge/7.runtime-config.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: bridge
order: 7
---

::warning
When using `runtimeConfig` option, [nitro](/docs/4.x/bridge/nitro) must have been configured.
::

## Update Runtime Config

Nuxt 3 approaches runtime config differently than Nuxt 2, using a new combined `runtimeConfig` option.

First, you'll need to combine your `publicRuntimeConfig` and `privateRuntimeConfig` properties into a new one called `runtimeConfig`, with the public config within a key called `public`.

```diff
// nuxt.config.js
- privateRuntimeConfig: {
-   apiKey: process.env.NUXT_API_KEY || 'super-secret-key'
- },
- publicRuntimeConfig: {
-   websiteURL: 'https://public-data.com'
- }
+ runtimeConfig: {
+   apiKey: process.env.NUXT_API_KEY || 'super-secret-key',
+   public: {
+     websiteURL: 'https://public-data.com'
+   }
+ }
```

This also means that when you need to access public runtime config, it's behind a property called `public`. If you use public runtime config, you'll need to update your code.

```diff
// MyWidget.vue
- <div>Website: {{ $config.websiteURL }}</div>
+ <div>Website: {{ $config.public.websiteURL }}</div>
```
