---
title: 'filter: blur()'
description: Utilities for applying blur filters to an element.
source_url: https://tailwindcss.com/docs/filter-blur
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: filter-blur.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 580
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `blur-xs` | `filter: blur(var(--blur-xs)); /* 4px */` |
| `blur-sm` | `filter: blur(var(--blur-sm)); /* 8px */` |
| `blur-md` | `filter: blur(var(--blur-md)); /* 12px */` |
| `blur-lg` | `filter: blur(var(--blur-lg)); /* 16px */` |
| `blur-xl` | `filter: blur(var(--blur-xl)); /* 24px */` |
| `blur-2xl` | `filter: blur(var(--blur-2xl)); /* 40px */` |
| `blur-3xl` | `filter: blur(var(--blur-3xl)); /* 64px */` |
| `blur-none` | `filter: ;` |
| `blur-(<custom-property>)` | `filter: blur(var(<custom-property>));` |
| `blur-[<value>]` | `filter: blur(<value>);` |

## Examples

### Basic example

Use utilities like `blur-sm` and `blur-lg` to blur an element:

  {
    <div className="flex scroll-p-8 overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-12 p-8 font-mono font-bold sm:gap-4">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">blur-none</p>
          <div className="relative blur-none">
            <img
              className="size-24 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">blur-sm</p>
          <div className="relative blur-sm">
            <img
              className="size-24 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">blur-lg</p>
          <div className="relative blur-lg">
            <img
              className="size-24 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">blur-2xl</p>
          <div className="relative blur-2xl">
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
<!-- [!code classes:blur-none,blur-sm,blur-lg,blur-2xl] -->
<img class="blur-none" src="/img/mountains.jpg" />
<img class="blur-sm" src="/img/mountains.jpg" />
<img class="blur-lg" src="/img/mountains.jpg" />
<img class="blur-2xl" src="/img/mountains.jpg" />
```

### Using a custom value

### Responsive design

## Customizing your theme
