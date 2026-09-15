---
title: outline-width
source_url: https://tailwindcss.com/docs/outline-width
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: outline-width.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1330
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `outline` | `outline-width: 1px;` |
| `outline-<number>` | `outline-width: <number>px;` |
| `outline-(length:<custom-property>)` | `outline-width: var(<custom-property>);` |
| `outline-[<value>]` | `outline-width: <value>;` |

## Examples

### Basic example

Use `outline` or `outline-<number>` utilities like `outline-2` and `outline-4` to set the width of an element's outline:

  {
    <div className="flex flex-col items-center justify-center gap-8 text-center text-sm font-bold text-white sm:flex-row sm:gap-16">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">outline</p>
        <button className="dark:border-gray rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-semibold text-gray-700 outline outline-offset-2 outline-blue-500 dark:border-transparent dark:bg-gray-700 dark:text-gray-200">
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">outline-2</p>
        <button className="dark:border-gray rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-semibold text-gray-700 outline-2 outline-offset-2 outline-blue-500 dark:border-transparent dark:bg-gray-700 dark:text-gray-200">
          Button B
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">outline-4</p>
        <button className="dark:border-gray rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-semibold text-gray-700 outline-4 outline-offset-2 outline-blue-500 dark:border-transparent dark:bg-gray-700 dark:text-gray-200">
          Button C
        </button>
      </div>
    </div>
  }

```html
<!-- [!code classes:outline,outline-2,outline-4] -->
<button class="outline outline-offset-2 ...">Button A</button>
<button class="outline-2 outline-offset-2 ...">Button B</button>
<button class="outline-4 outline-offset-2 ...">Button C</button>
```

### Applying on focus

  {
    <div className="mx-auto flex max-w-md justify-center gap-4 text-center text-sm leading-6 font-bold text-white">
      <button className="rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-semibold text-gray-700 outline-offset-2 outline-sky-500 focus:outline-2 dark:border-transparent dark:bg-gray-700 dark:text-gray-200">
        Save Changes
      </button>
    </div>
  }

```html
<!-- [!code classes:focus:outline-2] -->
<button class="outline-offset-2 outline-sky-500 focus:outline-2 ...">Save Changes</button>
```

### Using a custom value

### Responsive design
