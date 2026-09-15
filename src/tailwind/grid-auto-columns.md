---
title: grid-auto-columns
description: Utilities for controlling the size of implicitly-created grid columns.
source_url: https://tailwindcss.com/docs/grid-auto-columns
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: grid-auto-columns.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 860
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `auto-cols-auto` | `grid-auto-columns: auto;` |
| `auto-cols-min` | `grid-auto-columns: min-content;` |
| `auto-cols-max` | `grid-auto-columns: max-content;` |
| `auto-cols-fr` | `grid-auto-columns: minmax(0, 1fr);` |
| `auto-cols-<number>` | `grid-auto-columns: calc(var(--spacing) * <number>);` |
| `auto-cols-(<custom-property>)` | `grid-auto-columns: var(<custom-property>);` |
| `auto-cols-[<value>]` | `grid-auto-columns: <value>;` |

## Examples

### Basic example

Use utilities like `auto-cols-min` and `auto-cols-max` to control the size of implicitly-created grid columns:

```html
<!-- [!code classes:auto-cols-max] -->
<div class="grid auto-cols-max grid-flow-col">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Using a custom value

### Responsive design
