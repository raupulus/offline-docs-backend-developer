---
title: text-transform
description: Utilities for controlling the capitalization of text.
source_url: https://tailwindcss.com/docs/text-transform
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: text-transform.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1730
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `uppercase` | `text-transform: uppercase;` |
| `lowercase` | `text-transform: lowercase;` |
| `capitalize` | `text-transform: capitalize;` |
| `normal-case` | `text-transform: none;` |

## Examples

### Uppercasing text

Use the `uppercase` utility to uppercase the text of an element:

  {
    <p className="text-center text-lg font-medium text-gray-900 uppercase dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:uppercase] -->
<p class="uppercase">The quick brown fox ...</p>
```

### Lowercasing text

Use the `lowercase` utility to lowercase the text of an element:

  {
    <p className="text-center text-lg font-medium text-gray-900 lowercase dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:lowercase] -->
<p class="lowercase">The quick brown fox ...</p>
```

### Capitalizing text

Use the `capitalize` utility to capitalize text of an element:

  {
    <p className="text-center text-lg font-medium text-gray-900 capitalize dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:capitalize] -->
<p class="capitalize">The quick brown fox ...</p>
```

### Resetting text casing

Use the `normal-case` utility to preserve the original text casing of an element—typically used to reset capitalization at different breakpoints:

  {
    <p className="text-center text-lg font-medium text-gray-900 normal-case dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:normal-case] -->
<p class="normal-case">The quick brown fox ...</p>
```

### Responsive design
