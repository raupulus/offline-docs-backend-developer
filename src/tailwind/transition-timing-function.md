---
title: transition-timing-function
description: Utilities for controlling the easing of CSS transitions.
source_url: https://tailwindcss.com/docs/transition-timing-function
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: transition-timing-function.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1860
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `ease-linear` | `transition-timing-function: linear;` |
| `ease-in` | `transition-timing-function: var(--ease-in); /* cubic-bezier(0.4, 0, 1, 1) */` |
| `ease-out` | `transition-timing-function: var(--ease-out); /* cubic-bezier(0, 0, 0.2, 1) */` |
| `ease-in-out` | `transition-timing-function: var(--ease-in-out); /* cubic-bezier(0.4, 0, 0.2, 1) */` |
| `ease-initial` | `transition-timing-function: initial;` |
| `ease-(<custom-property>)` | `transition-timing-function: var(<custom-property>);` |
| `ease-[<value>]` | `transition-timing-function: <value>;` |

## Examples

### Basic example

Use utilities like `ease-in` and `ease-out` to control the easing curve of an element's transition:

  {
    <div className="flex flex-col justify-around gap-8 text-sm leading-6 font-bold text-white sm:flex-row sm:gap-0">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">ease-in</p>
        <button className="rounded-md bg-sky-500 px-4 py-2 text-sm font-semibold text-white duration-300 ease-in hover:scale-125">
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">ease-out</p>
        <button className="rounded-md bg-sky-500 px-4 py-2 text-sm font-semibold text-white duration-300 ease-out hover:scale-125">
          Button B
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">ease-in-out</p>
        <button className="rounded-md bg-sky-500 px-4 py-2 text-sm font-semibold text-white duration-300 ease-in-out hover:scale-125">
          Button C
        </button>
      </div>
    </div>
  }

```html
<!-- [!code classes:ease-in,ease-out,ease-in-out] -->
<button class="duration-300 ease-in ...">Button A</button>
<button class="duration-300 ease-out ...">Button B</button>
<button class="duration-300 ease-in-out ...">Button C</button>
```

### Using a custom value

### Responsive design

## Customizing your theme
