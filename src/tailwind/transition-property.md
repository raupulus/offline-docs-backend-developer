---
title: transition-property
description: Utilities for controlling which CSS properties transition.
source_url: https://tailwindcss.com/docs/transition-property
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: transition-property.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1850
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `transition` | `transition-property: color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events;         transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */         transition-duration: var(--default-transition-duration); /* 150ms */` |
| `transition-all` | `transition-property: all;         transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */         transition-duration: var(--default-transition-duration); /* 150ms */` |
| `transition-colors` | `transition-property: color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to;         transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */         transition-duration: var(--default-transition-duration); /* 150ms */` |
| `transition-opacity` | `transition-property: opacity;         transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */         transition-duration: var(--default-transition-duration); /* 150ms */` |
| `transition-shadow` | `transition-property: box-shadow;         transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */         transition-duration: var(--default-transition-duration); /* 150ms */` |
| `transition-transform` | `transition-property: transform, translate, scale, rotate;         transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */         transition-duration: var(--default-transition-duration); /* 150ms */` |
| `transition-none` | `transition-property: none;` |
| `transition-(<custom-property>)` | `transition-property: var(<custom-property>);         transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */         transition-duration: var(--default-transition-duration); /* 150ms */` |
| `transition-[<value>]` | `transition-property: <value>;         transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */         transition-duration: var(--default-transition-duration); /* 150ms */` |

## Examples

### Basic example

Use utilities like `transition` and `transition-colors` to specify which properties should transition when they change:

  {
    <div className="flex justify-around text-sm leading-6 font-bold text-white">
      <button className="rounded-md bg-blue-500 px-4 py-2 text-sm font-semibold text-white delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500">
        Save Changes
      </button>
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:transition] -->
<button class="bg-blue-500 transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 ...">
  Save Changes
</button>
```

### Supporting reduced motion

For situations where the user has specified that they prefer reduced motion, you can conditionally apply animations and transitions using the `motion-safe` and `motion-reduce` variants:

```html
<!-- [!code classes:motion-reduce:transition-none,motion-reduce:hover:transform-none] -->
<!-- prettier-ignore -->
<button class="transform transition hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:transform-none ...">
  <!-- ... -->
</button>
```

### Using a custom value

### Responsive design
