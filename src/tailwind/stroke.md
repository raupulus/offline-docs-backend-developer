---
title: stroke
description: Utilities for styling the stroke of SVG elements.
source_url: https://tailwindcss.com/docs/stroke
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: stroke.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1610
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `stroke-none` | `stroke: none;` |
| `stroke-inherit` | `stroke: inherit;` |
| `stroke-current` | `stroke: currentColor;` |
| `stroke-transparent` | `stroke: transparent;` |
| `stroke-(<custom-property>)` | `stroke: var(<custom-property>);` |
| `stroke-[<color>]` | `stroke: <color>;` |

## Examples

### Basic example

Use utilities like `stroke-indigo-500` and `stroke-lime-600` to change the stroke color of an SVG:

  {
    <div className="flex items-center justify-center">
      <svg className="h-10 stroke-cyan-500" viewBox="0 0 48 40" fill="none">
        <path
          d="M1 13C1 10.2386 3.23858 8 6 8H13.4914C14.3844 8 15.1691 7.40805 15.4144 6.54944L16.5856 2.45056C16.8309 1.59196 17.6156 1 18.5086 1H29.4914C30.3844 1 31.1691 1.59195 31.4144 2.45056L32.5856 6.54944C32.8309 7.40804 33.6156 8 34.5086 8H42C44.7614 8 47 10.2386 47 13V34C47 36.7614 44.7614 39 42 39H6C3.23858 39 1 36.7614 1 34V13Z"
          strokeWidth="2"
        />
        <circle cx="24" cy="23" r="9" strokeWidth="2" />
      </svg>
    </div>
  }

```html
<!-- [!code classes:stroke-cyan-500] -->
<svg class="stroke-cyan-500 ...">
  <!-- ... -->
</svg>
```

This can be useful for styling icon sets like [Heroicons](https://heroicons.com).

### Using the current color

Use the `stroke-current` utility to set the stroke color to the current text color:

  {
    <div className="flex items-center justify-center">
      <button className="inline-flex gap-2 rounded-md border border-pink-100 bg-white px-3 py-2 text-sm font-semibold text-pink-600 shadow-sm transition-colors duration-150 hover:border-pink-600 hover:bg-pink-600 hover:text-white dark:border-transparent">
        <svg fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-5 stroke-current">
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3"
          />
        </svg>
        Download file
      </button>
    </div>
  }

```html
<!-- [!code classes:stroke-current] -->
<button class="bg-white text-pink-600 hover:bg-pink-600 hover:text-white ...">
  <svg class="size-5 stroke-current ..." fill="none">
    <!-- ... -->
  </svg>
  Download file
</button>
```

### Using a custom value

### Responsive design

## Customizing your theme
