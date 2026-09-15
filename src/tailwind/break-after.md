---
title: break-after
description: Utilities for controlling how a column or page should break after an
  element.
source_url: https://tailwindcss.com/docs/break-after
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: break-after.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 390
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `break-after-auto` | `break-after: auto;` |
| `break-after-avoid` | `break-after: avoid;` |
| `break-after-all` | `break-after: all;` |
| `break-after-avoid-page` | `break-after: avoid-page;` |
| `break-after-page` | `break-after: page;` |
| `break-after-left` | `break-after: left;` |
| `break-after-right` | `break-after: right;` |
| `break-after-column` | `break-after: column;` |

## Examples

### Basic example

Use utilities like `break-after-column` and `break-after-page` to control how a column or page break should behave after an element:

```html
<!-- [!code classes:break-after-column] -->
<div class="columns-2">
  <p>Well, let me tell you something, ...</p>
  <p class="break-after-column">Sure, go ahead, laugh...</p>
  <p>Maybe we can live without...</p>
  <p>Look. If you think this is...</p>
</div>
```

### Responsive design
