---
title: font-style
description: Utilities for controlling the style of text.
source_url: https://tailwindcss.com/docs/font-style
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: font-style.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 800
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `italic` | `font-style: italic;` |
| `not-italic` | `font-style: normal;` |

## Examples

### Italicizing text

Use the `italic` utility to make text italic:

  {
    <p className="text-center text-lg font-medium text-gray-900 italic dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:italic] -->
<p class="italic ...">The quick brown fox ...</p>
```

### Displaying text normally

Use the `not-italic` utility to display text normally:

  {
    <p className="text-center text-lg font-medium text-gray-900 not-italic dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:not-italic] -->
<p class="not-italic ...">The quick brown fox ...</p>
```

### Responsive design
