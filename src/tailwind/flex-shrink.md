---
title: flex-shrink
description: Utilities for controlling how flex items shrink.
source_url: https://tailwindcss.com/docs/flex-shrink
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: flex-shrink.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 710
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `shrink` | `flex-shrink: 1;` |
| `shrink-<number>` | `flex-shrink: <number>;` |
| `shrink-[<value>]` | `flex-shrink: <value>;` |
| `shrink-(<custom-property>)` | `flex-shrink: var(<custom-property>);` |

## Examples

### Allowing flex items to shrink

Use `shrink` to allow a flex item to shrink if needed:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 w-14 flex-none items-center justify-center rounded-lg bg-sky-300 p-4 dark:bg-sky-800 dark:text-sky-400">
          01
        </div>
        <div className="flex h-14 w-64 shrink items-center justify-center rounded-lg bg-sky-500 p-4">02</div>
        <div className="hidden h-14 w-14 flex-none items-center justify-center rounded-lg bg-sky-300 p-4 sm:flex dark:bg-sky-800 dark:text-sky-400">
          03
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:shrink] -->
<div class="flex ...">
  <div class="h-14 w-14 flex-none ...">01</div>
  <div class="h-14 w-64 shrink ...">02</div>
  <div class="h-14 w-14 flex-none ...">03</div>
</div>
```

### Preventing items from shrinking

Use `shrink-0` to prevent a flex item from shrinking:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex flex-1 items-center justify-center rounded-lg bg-blue-300 p-4 dark:bg-blue-800 dark:text-blue-500">
          01
        </div>
        <div className="flex w-16 shrink-0 items-center justify-center rounded-lg bg-blue-500 p-4 sm:w-64">02</div>
        <div className="hidden flex-1 items-center justify-center rounded-lg bg-blue-300 p-4 sm:flex dark:bg-blue-800 dark:text-blue-500">
          03
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:shrink-0] -->
<div class="flex ...">
  <div class="h-16 flex-1 ...">01</div>
  <div class="h-16 w-32 shrink-0 ...">02</div>
  <div class="h-16 flex-1 ...">03</div>
</div>
```

### Using a custom value

### Responsive design
