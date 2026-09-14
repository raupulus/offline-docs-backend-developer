---
title: public
description: The public/ directory is used to serve your website's static assets.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 2.directory-structure/1.public.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: directory-structure
order: 1
---

Files contained within the `public/` directory are served at the root and are not modified by the build process. This is suitable for files that have to keep their names (e.g. `robots.txt`) _or_ likely won't change (e.g. `favicon.ico`).

```bash [Directory structure]
-| public/
---| favicon.ico
---| og-image.png
---| robots.txt
```

```vue [app/app.vue]
<script setup lang="ts">
useSeoMeta({
  ogImage: '/og-image.png',
})
</script>
```

::tip{to="https://v2.nuxt.com/docs/directory-structure/static/" target="_blank"}
This is known as the [`static/`] directory in Nuxt 2.
::
