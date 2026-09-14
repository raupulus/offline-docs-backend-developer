---
title: <NuxtImg>
description: Nuxt provides a <NuxtImg> component to handle automatic image optimization.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/1.components/9.nuxt-img.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 9
---

`<NuxtImg>` is a drop-in replacement for the native `<img>` tag.

- Uses built-in provider to optimize local and remote images
- Converts `src` to provider-optimized URLs
- Automatically resizes images based on `width` and `height`
- Generates responsive sizes when providing `sizes` option
- Supports native lazy loading as well as other `<img>` attributes

## Setup

In order to use `<NuxtImg>` you should install and enable the Nuxt Image module:

```bash [Terminal]
npx nuxt module add image
```

## Usage

`<NuxtImg>` outputs a native `img` tag directly (without any wrapper around it). Use it like you would use the `<img>` tag:

```html
<NuxtImg src="/nuxt-icon.png" />
```

Will result in:

```html
<img src="/nuxt-icon.png" />
```

::read-more{to="https://image.nuxt.com/usage/nuxt-img" target="_blank"}
Read more about the `<NuxtImg>` component.
::
