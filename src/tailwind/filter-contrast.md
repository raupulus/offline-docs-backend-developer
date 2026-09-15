---
title: 'filter: contrast()'
description: Utilities for applying contrast filters to an element.
source_url: https://tailwindcss.com/docs/filter-contrast
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: filter-contrast.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 600
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `contrast-<number>` | `filter: contrast(<number>%);` |
| `contrast-(<custom-property>)` | `filter: contrast(var(<custom-property>));` |
| `contrast-[<value>]` | `filter: contrast(<value>);` |

## Examples

### Basic example

Use utilities like `contrast-50` and `contrast-100` to control an element's contrast:

  {
    <div className="flex scroll-p-8 justify-start overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-6 p-8 font-mono font-bold sm:gap-4">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">contrast-50</p>
          <div className="relative contrast-50">
            <img
              className="size-24 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            contrast-100
          </p>
          <div className="relative contrast-100">
            <img
              className="size-24 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            contrast-125
          </p>
          <div className="relative contrast-125">
            <img
              className="size-24 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            contrast-200
          </p>
          <div className="relative contrast-200">
            <img
              className="size-24 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:contrast-50,contrast-100,contrast-125,contrast-200] -->
<img class="contrast-50 ..." src="/img/mountains.jpg" />
<img class="contrast-100 ..." src="/img/mountains.jpg" />
<img class="contrast-125 ..." src="/img/mountains.jpg" />
<img class="contrast-200 ..." src="/img/mountains.jpg" />
```

### Using a custom value

### Responsive design
