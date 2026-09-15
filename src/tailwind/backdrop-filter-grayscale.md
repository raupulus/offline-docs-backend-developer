---
title: 'backdrop-filter: grayscale()'
description: Utilities for applying backdrop grayscale filters to an element.
source_url: https://tailwindcss.com/docs/backdrop-filter-grayscale
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: backdrop-filter-grayscale.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 120
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `backdrop-grayscale` | `backdrop-filter: grayscale(100%);` |
| `backdrop-grayscale-<number>` | `backdrop-filter: grayscale(<number>%);` |
| `backdrop-grayscale-(<custom-property>)` | `backdrop-filter: grayscale(var(<custom-property>));` |
| `backdrop-grayscale-[<value>]` | `backdrop-filter: grayscale(<value>);` |

## Examples

### Basic example

Use utilities like `backdrop-grayscale-50` and `backdrop-grayscale` to control the grayscale effect applied to an element's backdrop:

  {
    <div className="flex scroll-p-8 justify-start overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-6 p-8 font-mono font-bold sm:gap-4">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            backdrop-grayscale-0
          </p>
          <div className="relative">
            <div className="absolute inset-6 size-20 bg-white/30 backdrop-grayscale-0"></div>
            <img
              className="size-32 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            backdrop-grayscale-50
          </p>
          <div className="relative">
            <div className="absolute inset-6 size-20 bg-white/30 backdrop-grayscale-50"></div>
            <img
              className="size-32 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            backdrop-grayscale
          </p>
          <div className="relative">
            <div className="absolute inset-6 size-20 bg-white/30 backdrop-grayscale"></div>
            <img
              className="size-32 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:backdrop-grayscale-0,backdrop-grayscale-50,backdrop-grayscale] -->
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-grayscale-0 ..."></div>
</div>
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-grayscale-50 ..."></div>
</div>
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-grayscale-200 ..."></div>
</div>
```

### Using a custom value

### Responsive design
