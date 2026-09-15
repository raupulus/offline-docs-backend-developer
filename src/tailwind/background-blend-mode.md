---
title: background-blend-mode
source_url: https://tailwindcss.com/docs/background-blend-mode
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: background-blend-mode.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 210
---

"Utilities for controlling how an element's background image should blend with its background color.";

| Clase | Propiedades CSS |
| :--- | :--- |
| `bg-blend-normal` | `background-blend-mode: normal;` |
| `bg-blend-multiply` | `background-blend-mode: multiply;` |
| `bg-blend-screen` | `background-blend-mode: screen;` |
| `bg-blend-overlay` | `background-blend-mode: overlay;` |
| `bg-blend-darken` | `background-blend-mode: darken;` |
| `bg-blend-lighten` | `background-blend-mode: lighten;` |
| `bg-blend-color-dodge` | `background-blend-mode: color-dodge;` |
| `bg-blend-color-burn` | `background-blend-mode: color-burn;` |
| `bg-blend-hard-light` | `background-blend-mode: hard-light;` |
| `bg-blend-soft-light` | `background-blend-mode: soft-light;` |
| `bg-blend-difference` | `background-blend-mode: difference;` |
| `bg-blend-exclusion` | `background-blend-mode: exclusion;` |
| `bg-blend-hue` | `background-blend-mode: hue;` |
| `bg-blend-saturation` | `background-blend-mode: saturation;` |
| `bg-blend-color` | `background-blend-mode: color;` |
| `bg-blend-luminosity` | `background-blend-mode: luminosity;` |

## Examples

### Basic example

Use utilities like `bg-blend-difference` and `bg-blend-saturation` to control how the background image and color of an element are blended:

  {
    <div className="flex flex-col items-center justify-between gap-y-6 px-1 sm:flex-row md:px-4">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          bg-blend-multiply
        </p>
        <div className="size-24 bg-blue-500 bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] bg-cover bg-center bg-no-repeat bg-blend-multiply md:size-32"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          bg-blend-soft-light
        </p>
        <div className="size-24 bg-blue-500 bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] bg-cover bg-center bg-no-repeat bg-blend-soft-light md:size-32"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          bg-blend-overlay
        </p>
        <div className="size-24 bg-blue-500 bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] bg-cover bg-center bg-no-repeat bg-blend-overlay md:size-32"></div>
      </div>
    </div>
  }

```html
<!-- [!code classes:bg-blend-multiply,bg-blend-soft-light,bg-blend-overlay] -->
<div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-multiply ..."></div>
<div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-soft-light ..."></div>
<div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-overlay ..."></div>
```

### Responsive design
