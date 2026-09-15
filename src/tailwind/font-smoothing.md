---
title: font-smoothing
description: Utilities for controlling the font smoothing of an element.
source_url: https://tailwindcss.com/docs/font-smoothing
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: font-smoothing.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 780
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `antialiased` | `-webkit-font-smoothing: antialiased;\n-moz-osx-font-smoothing: grayscale;` |
| `subpixel-antialiased` | `-webkit-font-smoothing: auto;\n-moz-osx-font-smoothing: auto;` |

## Examples

### Grayscale antialiasing

Use the `antialiased` utility to render text using grayscale antialiasing:

  {
    <p className="text-center text-lg font-medium text-gray-900 antialiased dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:antialiased] -->
<p class="antialiased ...">The quick brown fox ...</p>
```

### Subpixel antialiasing

Use the `subpixel-antialiased` utility to render text using subpixel antialiasing:

  {
    <p className="text-center text-lg font-medium text-gray-900 subpixel-antialiased dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:subpixel-antialiased] -->
<p class="subpixel-antialiased ...">The quick brown fox ...</p>
```

### Responsive design
