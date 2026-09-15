---
title: fill
description: Utilities for styling the fill of SVG elements.
source_url: https://tailwindcss.com/docs/fill
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: fill.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 570
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `fill-none` | `fill: none;` |
| `fill-inherit` | `fill: inherit;` |
| `fill-current` | `fill: currentColor;` |
| `fill-transparent` | `fill: transparent;` |
| `fill-(<custom-property>)` | `fill: var(<custom-property>);` |
| `fill-[<color>]` | `fill: <color>;` |
| `fill-<value>` | `fill: var(--color-<value>); /* <value> */` |

## Examples

### Basic example

Use utilities like `fill-indigo-500` and `fill-lime-600` to change the fill color of an SVG:

  {
    <div className="flex items-center justify-center">
      <svg className="h-12 fill-blue-500" viewBox="0 0 46 48">
        <path
          fillRule="evenodd"
          clipRule="evenodd"
          d="M23.0002 0C12.5068 0 4.00017 8.50659 4.00017 19V32.5335C4.00017 32.8383 3.9145 33.1371 3.75292 33.3956L0.912672 37.94C0.0801118 39.2721 1.0378 41 2.60867 41H43.3917C44.9625 41 45.9202 39.2721 45.0877 37.94L42.2474 33.3956C42.0858 33.1371 42.0002 32.8383 42.0002 32.5335V19C42.0002 8.50659 33.4936 0 23.0002 0ZM23.0002 48C20.2388 48 18.0002 45.7614 18.0002 43H28.0002C28.0002 45.7614 25.7616 48 23.0002 48Z"
        />
      </svg>
    </div>
  }

```html
<!-- [!code classes:fill-blue-500] -->
<svg class="fill-blue-500 ...">
  <!-- ... -->
</svg>
```

This can be useful for styling icon sets like [Heroicons](https://heroicons.com).

### Using the current color

Use the `fill-current` utility to set the fill color to the current text color:

  {
    <div className="flex items-center justify-center">
      <button className="inline-flex gap-2 rounded-md border border-indigo-100 bg-white px-3 py-2 text-sm font-semibold text-indigo-600 shadow-sm transition-colors duration-150 hover:border-indigo-600 hover:bg-indigo-600 hover:text-white dark:border-transparent">
        <svg viewBox="0 0 20 20" className="size-5 fill-current">
          <path
            d="M15.312 11.424a5.5 5.5 0 0 1-9.201 2.466l-.312-.311h2.433a.75.75 0 0 0 0-1.5H3.989a.75.75 0 0 0-.75.75v4.242a.75.75 0 0 0 1.5 0v-2.43l.31.31a7 7 0 0 0 11.712-3.138.75.75 0 0 0-1.449-.39Zm1.23-3.723a.75.75 0 0 0 .219-.53V2.929a.75.75 0 0 0-1.5 0V5.36l-.31-.31A7 7 0 0 0 3.239 8.188a.75.75 0 1 0 1.448.389A5.5 5.5 0 0 1 13.89 6.11l.311.31h-2.432a.75.75 0 0 0 0 1.5h4.243a.75.75 0 0 0 .53-.219Z"
            fillRule="evenodd"
            clipRule="evenodd"
          />
        </svg>
        Check for updates
      </button>
    </div>
  }

```html
<!-- [!code classes:fill-current] -->
<button class="bg-white text-indigo-600 hover:bg-indigo-600 hover:text-white ...">
  <svg class="size-5 fill-current ...">
    <!-- ... -->
  </svg>
  Check for updates
</button>
```

### Using a custom value

### Responsive design

## Customizing your theme
