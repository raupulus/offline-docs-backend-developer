---
title: grid-auto-flow
description: Utilities for controlling how elements in a grid are auto-placed.
source_url: https://tailwindcss.com/docs/grid-auto-flow
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: grid-auto-flow.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 870
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `grid-flow-row` | `grid-auto-flow: row;` |
| `grid-flow-col` | `grid-auto-flow: column;` |
| `grid-flow-dense` | `grid-auto-flow: dense;` |
| `grid-flow-row-dense` | `grid-auto-flow: row dense;` |
| `grid-flow-col-dense` | `grid-auto-flow: column dense;` |

## Examples

### Basic example

Use utilities like `grid-flow-col` and `grid-flow-row-dense` to control how the auto-placement algorithm works for a grid layout:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid grid-flow-row-dense grid-cols-3 grid-rows-3 gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="col-span-2 rounded-lg bg-purple-300 p-4 dark:bg-purple-800 dark:text-purple-400">01</div>
        <div className="col-span-2 rounded-lg bg-purple-300 p-4 dark:bg-purple-800 dark:text-purple-400">02</div>
        <div className="rounded-lg bg-purple-500 p-4">03</div>
        <div className="rounded-lg bg-purple-300 p-4 dark:bg-purple-800 dark:text-purple-400">04</div>
        <div className="rounded-lg bg-purple-300 p-4 dark:bg-purple-800 dark:text-purple-400">05</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:grid-flow-row-dense] -->
<div class="grid grid-flow-row-dense grid-cols-3 grid-rows-3 ...">
  <div class="col-span-2">01</div>
  <div class="col-span-2">02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

### Responsive design
