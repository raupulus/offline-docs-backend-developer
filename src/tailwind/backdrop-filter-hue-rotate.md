---
title: 'backdrop-filter: hue-rotate()'
description: Utilities for applying backdrop hue-rotate filters to an element.
source_url: https://tailwindcss.com/docs/backdrop-filter-hue-rotate
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: backdrop-filter-hue-rotate.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 130
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `backdrop-hue-rotate-<number>` | `backdrop-filter: hue-rotate(<number>deg);` |
| `-backdrop-hue-rotate-<number>` | `backdrop-filter: hue-rotate(calc(<number>deg * -1));` |
| `backdrop-hue-rotate-(<custom-property>)` | `backdrop-filter: hue-rotate(var(<custom-property>));` |
| `backdrop-hue-rotate-[<value>]` | `backdrop-filter: hue-rotate(<value>);` |

## Examples

### Basic example

Use utilities like `backdrop-hue-rotate-90` and `backdrop-hue-rotate-180` to rotate the hue of an element's backdrop:

  {
    <div className="flex scroll-p-8 justify-start overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-6 p-8 font-mono font-bold sm:gap-4">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            backdrop-hue-rotate-90
          </p>
          <div className="relative">
            <div className="absolute inset-6 size-20 bg-white/30 backdrop-hue-rotate-90"></div>
            <img
              className="size-32 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            backdrop-hue-rotate-180
          </p>
          <div className="relative">
            <div className="absolute inset-6 size-20 bg-white/30 backdrop-hue-rotate-180"></div>
            <img
              className="size-32 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            backdrop-hue-rotate-270
          </p>
          <div className="relative">
            <div className="absolute inset-6 size-20 bg-white/30 backdrop-hue-rotate-270"></div>
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
<!-- [!code classes:backdrop-hue-rotate-90,backdrop-hue-rotate-180,backdrop-hue-rotate-270] -->
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-hue-rotate-90 ..."></div>
</div>
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-hue-rotate-180 ..."></div>
</div>
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-hue-rotate-270 ..."></div>
</div>
```

### Using negative values

Use utilities like `-backdrop-hue-rotate-90` and `-backdrop-hue-rotate-180` to set a negative backdrop hue rotation value:

  {
    <div className="flex scroll-p-8 justify-start overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-6 p-8 font-mono font-bold sm:gap-4">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            -backdrop-hue-rotate-15
          </p>
          <div className="relative">
            <div className="absolute inset-6 size-20 bg-white/30 -backdrop-hue-rotate-15"></div>
            <img
              className="size-32 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            -backdrop-hue-rotate-45
          </p>
          <div className="relative">
            <div className="absolute inset-6 size-20 bg-white/30 -backdrop-hue-rotate-45"></div>
            <img
              className="size-32 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            -backdrop-hue-rotate-90
          </p>
          <div className="relative">
            <div className="absolute inset-6 size-20 bg-white/30 -backdrop-hue-rotate-90"></div>
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
<!-- [!code classes:-backdrop-hue-rotate-15,-backdrop-hue-rotate-45,-backdrop-hue-rotate-90] -->
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 -backdrop-hue-rotate-15 ..."></div>
</div>
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 -backdrop-hue-rotate-45 ..."></div>
</div>
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 -backdrop-hue-rotate-90 ..."></div>
</div>
```

### Using a custom value

### Responsive design
