---
title: text-overflow
description: Utilities for controlling how the text of an element overflows.
source_url: https://tailwindcss.com/docs/text-overflow
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: text-overflow.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1710
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `truncate` | `overflow: hidden;         text-overflow: ellipsis;         white-space: nowrap;` |
| `text-ellipsis` | `text-overflow: ellipsis;` |
| `text-clip` | `text-overflow: clip;` |

## Examples

### Truncating text

Use the `truncate` utility to prevent text from wrapping and truncate overflowing text with an ellipsis (…) if needed:

  {
    <p className="mx-auto max-w-xs truncate border-x border-x-pink-400/30 py-8 text-gray-900 dark:text-gray-200">
      The longest word in any of the major English language dictionaries is{" "}
      <span className="font-bold">pneumonoultramicroscopicsilicovolcanoconiosis,</span> a word that refers to a lung
      disease contracted from the inhalation of very fine silica particles, specifically from a volcano; medically, it
      is the same as silicosis.
    </p>
  }

```html
<!-- [!code classes:truncate] -->
<p class="truncate">The longest word in any of the major...</p>
```

### Adding an ellipsis

Use the `text-ellipsis` utility to truncate overflowing text with an ellipsis (…) if needed:

  {
    <p className="mx-auto max-w-xs overflow-hidden border-x border-x-pink-400/30 py-8 text-ellipsis text-gray-900 dark:text-gray-200">
      The longest word in any of the major English language dictionaries is{" "}
      <span className="font-bold">pneumonoultramicroscopicsilicovolcanoconiosis,</span> a word that refers to a lung
      disease contracted from the inhalation of very fine silica particles, specifically from a volcano; medically, it
      is the same as silicosis.
    </p>
  }

```html
<!-- [!code classes:text-ellipsis] -->
<p class="overflow-hidden text-ellipsis">The longest word in any of the major...</p>
```

### Clipping text

Use the `text-clip` utility to truncate the text at the limit of the content area:

  {
    <p className="mx-auto max-w-xs overflow-hidden border-x border-x-pink-400/30 py-8 text-clip text-gray-900 dark:text-gray-200">
      The longest word in any of the major English language dictionaries is{" "}
      <span className="font-bold">pneumonoultramicroscopicsilicovolcanoconiosis,</span> a word that refers to a lung
      disease contracted from the inhalation of very fine silica particles, specifically from a volcano; medically, it
      is the same as silicosis.
    </p>
  }

```html
<!-- [!code classes:text-clip] -->
<p class="overflow-hidden text-clip">The longest word in any of the major...</p>
```

This is the default browser behavior.

### Responsive design
