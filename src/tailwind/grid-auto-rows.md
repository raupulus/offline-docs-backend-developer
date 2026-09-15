---
title: grid-auto-rows
description: Utilities for controlling the size of implicitly-created grid rows.
source_url: https://tailwindcss.com/docs/grid-auto-rows
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: grid-auto-rows.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 880
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `auto-rows-auto` | `grid-auto-rows: auto;` |
| `auto-rows-min` | `grid-auto-rows: min-content;` |
| `auto-rows-max` | `grid-auto-rows: max-content;` |
| `auto-rows-fr` | `grid-auto-rows: minmax(0, 1fr);` |
| `auto-rows-<number>` | `grid-auto-rows: calc(var(--spacing) * <number>);` |
| `auto-rows-(<custom-property>)` | `grid-auto-rows: var(<custom-property>);` |
| `auto-rows-[<value>]` | `grid-auto-rows: <value>;` |

## Examples

### Basic example

Use utilities like `auto-rows-min` and `auto-rows-max` to control the size of implicitly-created grid rows:

```html
<!-- [!code classes:auto-rows-max] -->
<div class="grid grid-flow-row auto-rows-max">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Using a custom value

### Responsive design
