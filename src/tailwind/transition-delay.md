---
title: transition-delay
description: Utilities for controlling the delay of CSS transitions.
source_url: https://tailwindcss.com/docs/transition-delay
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: transition-delay.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1830
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `delay-<number>` | `transition-delay: <number>ms;` |
| `delay-(<custom-property>)` | `transition-delay: var(<custom-property>);` |
| `delay-[<value>]` | `transition-delay: <value>;` |

## Examples

### Basic example

Use utilities like `delay-150` and `delay-700` to set the transition delay of an element in milliseconds:

  {
    <div className="flex flex-col justify-around gap-8 text-sm leading-6 font-bold text-white sm:flex-row sm:gap-0">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">delay-150</p>
        <button className="rounded-md bg-blue-500 px-4 py-2 text-sm font-semibold text-white delay-150 duration-300 ease-in-out hover:scale-125">
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">delay-300</p>
        <button className="rounded-md bg-blue-500 px-4 py-2 text-sm font-semibold text-white delay-300 duration-300 ease-in-out hover:scale-125">
          Button B
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">delay-700</p>
        <button className="rounded-md bg-blue-500 px-4 py-2 text-sm font-semibold text-white delay-700 duration-300 ease-in-out hover:scale-125">
          Button C
        </button>
      </div>
    </div>
  }

```html
<!-- [!code classes:delay-150,delay-300,delay-700] -->
<button class="transition delay-150 duration-300 ease-in-out ...">Button A</button>
<button class="transition delay-300 duration-300 ease-in-out ...">Button B</button>
<button class="transition delay-700 duration-300 ease-in-out ...">Button C</button>
```

### Supporting reduced motion

For situations where the user has specified that they prefer reduced motion, you can conditionally apply animations and transitions using the `motion-safe` and `motion-reduce` variants:

```html
<!-- [!code classes:motion-reduce:delay-0] -->
<button type="button" class="delay-300 motion-reduce:delay-0 ...">
  <!-- ... -->
</button>
```

### Using a custom value

### Responsive design
