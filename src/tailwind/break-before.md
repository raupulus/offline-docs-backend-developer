---
title: break-before
description: Utilities for controlling how a column or page should break before an
  element.
source_url: https://tailwindcss.com/docs/break-before
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: break-before.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 400
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `break-before-auto` | `break-before: auto;` |
| `break-before-avoid` | `break-before: avoid;` |
| `break-before-all` | `break-before: all;` |
| `break-before-avoid-page` | `break-before: avoid-page;` |
| `break-before-page` | `break-before: page;` |
| `break-before-left` | `break-before: left;` |
| `break-before-right` | `break-before: right;` |
| `break-before-column` | `break-before: column;` |

## Examples

### Basic example

Use utilities like `break-before-column` and `break-before-page` to control how a column or page break should behave before an element:

```html
<!-- [!code classes:break-before-column] -->
<div class="columns-2">
  <p>Well, let me tell you something, ...</p>
  <p class="break-before-column">Sure, go ahead, laugh...</p>
  <p>Maybe we can live without...</p>
  <p>Look. If you think this is...</p>
</div>
```

### Responsive design
