---
title: break-inside
description: Utilities for controlling how a column or page should break within an
  element.
source_url: https://tailwindcss.com/docs/break-inside
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: break-inside.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 410
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `break-inside-auto` | `break-inside: auto;` |
| `break-inside-avoid` | `break-inside: avoid;` |
| `break-inside-avoid-page` | `break-inside: avoid-page;` |
| `break-inside-avoid-column` | `break-inside: avoid-column;` |

## Examples

### Basic example

Use utilities like `break-inside-column` and `break-inside-avoid-page` to control how a column or page break should behave within an element:

```html
<!-- [!code classes:break-inside-avoid-column] -->
<div class="columns-2">
  <p>Well, let me tell you something, ...</p>
  <p class="break-inside-avoid-column">Sure, go ahead, laugh...</p>
  <p>Maybe we can live without...</p>
  <p>Look. If you think this is...</p>
</div>
```

### Responsive design
