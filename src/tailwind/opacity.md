---
title: opacity
description: Utilities for controlling the opacity of an element.
source_url: https://tailwindcss.com/docs/opacity
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: opacity.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1280
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `opacity-<number>` | `opacity: <number>%;` |
| `opacity-(<custom-property>)` | `opacity: var(<custom-property>);` |
| `opacity-[<value>]` | `opacity: <value>;` |

## Examples

### Basic example

Use `opacity-<number>` utilities like `opacity-25` and `opacity-100` to set the opacity of an element:

  {
    <div className="flex flex-col items-center justify-center gap-8 text-sm leading-6 font-bold text-white sm:flex-row sm:gap-16">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">opacity-100</p>
        <button className="rounded-md bg-indigo-500 px-4 py-2 text-sm font-semibold text-white opacity-100">
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">opacity-75</p>
        <button className="rounded-md bg-indigo-500 px-4 py-2 text-sm font-semibold text-white opacity-75">
          Button B
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">opacity-50</p>
        <button className="rounded-md bg-indigo-500 px-4 py-2 text-sm font-semibold text-white opacity-50">
          Button C
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">opacity-25</p>
        <button className="rounded-md bg-indigo-500 px-4 py-2 text-sm font-semibold text-white opacity-25">
          Button D
        </button>
      </div>
    </div>
  }

```html
<!-- [!code classes:opacity-100,opacity-75,opacity-50,opacity-25] -->
<button class="bg-indigo-500 opacity-100 ..."></button>
<button class="bg-indigo-500 opacity-75 ..."></button>
<button class="bg-indigo-500 opacity-50 ..."></button>
<button class="bg-indigo-500 opacity-25 ..."></button>
```

### Applying conditionally

### Using a custom value

### Responsive design
