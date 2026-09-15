---
title: transition-duration
description: Utilities for controlling the duration of CSS transitions.
source_url: https://tailwindcss.com/docs/transition-duration
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: transition-duration.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1840
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `duration-<number>` | `transition-duration: <number>ms;` |
| `duration-initial` | `transition-duration: initial;` |
| `duration-(<custom-property>)` | `transition-duration: var(<custom-property>);` |
| `duration-[<value>]` | `transition-duration: <value>;` |

## Examples

### Basic example

Use utilities like `duration-150` and `duration-700` to set the transition duration of an element in milliseconds:

  {
    <div className="flex flex-col justify-around gap-8 text-sm leading-6 font-bold text-white sm:flex-row sm:gap-0">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">duration-150</p>
        <button className="rounded-md bg-violet-500 px-4 py-2 text-sm font-semibold text-white duration-150 ease-in-out hover:scale-125">
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">duration-300</p>
        <button className="rounded-md bg-violet-500 px-4 py-2 text-sm font-semibold text-white duration-300 ease-in-out hover:scale-125">
          Button B
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">duration-700</p>
        <button className="rounded-md bg-violet-500 px-4 py-2 text-sm font-semibold text-white duration-700 ease-in-out hover:scale-125">
          Button C
        </button>
      </div>
    </div>
  }

```html
<!-- [!code classes:duration-150,duration-300,duration-700] -->
<button class="transition duration-150 ease-in-out ...">Button A</button>
<button class="transition duration-300 ease-in-out ...">Button B</button>
<button class="transition duration-700 ease-in-out ...">Button C</button>
```

### Supporting reduced motion

For situations where the user has specified that they prefer reduced motion, you can conditionally apply animations and transitions using the `motion-safe` and `motion-reduce` variants:

```html
<!-- [!code classes:motion-reduce:duration-0] -->
<button type="button" class="duration-300 motion-reduce:duration-0 ...">
  <!-- ... -->
</button>
```

### Using a custom value

### Responsive design
