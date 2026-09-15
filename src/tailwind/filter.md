---
title: filter
description: Utilities for applying filters to an element.
source_url: https://tailwindcss.com/docs/filter
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: filter.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 670
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `filter-none` | `filter: none;` |
| `filter-(<custom-property>)` | `filter: var(<custom-property>);` |
| `filter-[<value>]` | `filter: <value>;` |

## Examples

### Basic example

Use utilities like `blur-xs` and `grayscale` to apply filters to an element:

  {
    <div className="flex scroll-p-8 overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-12 p-8 font-mono font-bold sm:gap-4">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">blur-xs</p>
          <div className="relative blur-xs">
            <img
              className="size-24 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">grayscale</p>
          <div className="relative grayscale">
            <img
              className="size-24 rounded-lg object-cover"
              src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
            />
            <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 italic dark:text-gray-400">
            combined
          </p>
          <div className="relative blur-xs grayscale">
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
<!-- [!code classes:blur-xs,grayscale] -->
<img class="blur-xs" src="/img/mountains.jpg" />
<img class="grayscale" src="/img/mountains.jpg" />
<img class="blur-xs grayscale" src="/img/mountains.jpg" />
```

You can combine the following filter utilities: [blur](/docs/filter-blur), [brightness](/docs/filter-brightness), [contrast](/docs/filter-contrast), [drop-shadow](/docs/filter-drop-shadow), [grayscale](/docs/filter-grayscale), [hue-rotate](/docs/filter-hue-rotate), [invert](/docs/filter-invert), [saturate](/docs/filter-saturate), and [sepia](/docs/filter-sepia).

### Removing filters

Use the `filter-none` utility to remove all of the filters applied to an element:

```html
<!-- [!code classes:md:filter-none] -->
<img class="blur-md brightness-150 invert md:filter-none" src="/img/mountains.jpg" />
```

### Using a custom value

### Applying on hover

### Responsive design
