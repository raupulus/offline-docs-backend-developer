---
title: <NuxtPicture>
description: Nuxt provides a <NuxtPicture> component to handle automatic image optimization.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/1.components/10.nuxt-picture.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 10
---

`<NuxtPicture>` is a drop-in replacement for the native `<picture>` tag.

Usage of `<NuxtPicture>` is almost identical to [`<NuxtImg>`](/docs/4.x/api/components/nuxt-img) but it also allows serving modern formats like `webp` when possible.

Learn more about the [`<picture>` tag on MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture).

## Setup

In order to use `<NuxtPicture>` you should install and enable the Nuxt Image module:

```bash [Terminal]
npx nuxt module add image
```

::read-more{to="https://image.nuxt.com/usage/nuxt-picture" target="_blank"}
Read more about the `<NuxtPicture>` component.
::
