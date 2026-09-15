---
title: stroke-width
description: Utilities for styling the stroke width of SVG elements.
source_url: https://tailwindcss.com/docs/stroke-width
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: stroke-width.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1600
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `stroke-<number>` | `stroke-width: <number>;` |
| `stroke-(length:<custom-property>)` | `stroke-width: var(<custom-property>);` |
| `stroke-[<value>]` | `stroke-width: <value>;` |

## Examples

### Basic example

Use `stroke-<number>` utilities like `stroke-1` and `stroke-2` to set the stroke width of an SVG:

  {
    <div className="flex items-center justify-center gap-x-8">
      <svg
        className="stroke-indigo-500 stroke-1"
        width="48"
        height="48"
        viewBox="0 0 48 48"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <circle cx="24" cy="24" r="23" strokeLinejoin="round" />
        <path d="M23 1C23 1 15 10.4901 15 24C15 37.5099 23 47 23 47" strokeLinejoin="round" />
        <path d="M25 1C25 1 33 10.4901 33 24C33 37.5099 25 47 25 47" strokeLinejoin="round" />
        <path d="M1 24H47" />
      </svg>
      <svg
        className="stroke-indigo-500 stroke-2"
        width="48"
        height="48"
        viewBox="0 0 48 48"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <circle cx="24" cy="24" r="23" strokeLinejoin="round" />
        <path d="M23 1C23 1 15 10.4901 15 24C15 37.5099 23 47 23 47" strokeLinejoin="round" />
        <path d="M25 1C25 1 33 10.4901 33 24C33 37.5099 25 47 25 47" strokeLinejoin="round" />
        <path d="M1 24H47" />
      </svg>
    </div>
  }

```html
<!-- [!code classes:stroke-1,stroke-2] -->
<svg class="stroke-1 ..."></svg>
<svg class="stroke-2 ..."></svg>
```

This can be useful for styling icon sets like [Heroicons](https://heroicons.com).

### Using a custom value

### Responsive design
