---
title: z-index
description: Utilities for controlling the stack order of an element.
source_url: https://tailwindcss.com/docs/z-index
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: z-index.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1960
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `z-<number>` | `z-index: <number>;` |
| `z-auto` | `z-index: auto;` |
| `z-[<value>]` | `z-index: <value>;` |
| `z-(<custom-property>)` | `z-index: var(<custom-property>);` |

## Examples

### Basic example

Use the `z-<number>` utilities like `z-10` and `z-50` to control the stack order (or three-dimensional positioning) of an element, regardless of the order it has been displayed:

  {
    <div className="flex justify-center -space-x-3 font-mono text-sm leading-6 font-bold text-white">
      <div className="z-40 flex size-16 items-center justify-center rounded-full bg-pink-500 shadow-lg outline-2 outline-white dark:outline-[#11121E]">
        05
      </div>
      <div className="z-30 flex size-16 items-center justify-center rounded-full bg-pink-500 shadow-lg outline-2 outline-white dark:outline-[#11121E]">
        04
      </div>
      <div className="z-20 flex size-16 items-center justify-center rounded-full bg-pink-500 shadow-lg outline-2 outline-white dark:outline-[#11121E]">
        03
      </div>
      <div className="z-10 flex size-16 items-center justify-center rounded-full bg-pink-500 shadow-lg outline-2 outline-white dark:outline-[#11121E]">
        02
      </div>
      <div className="z-0 flex size-16 items-center justify-center rounded-full bg-pink-500 shadow-lg outline-2 outline-white dark:outline-[#11121E]">
        01
      </div>
    </div>
  }

```html
<!-- [!code classes:z-40,z-30,z-20,z-10,z-0] -->
<div class="z-40 ...">05</div>
<div class="z-30 ...">04</div>
<div class="z-20 ...">03</div>
<div class="z-10 ...">02</div>
<div class="z-0 ...">01</div>
```

### Using negative values

To use a negative z-index value, prefix the class name with a dash to convert it to a negative value:

  {
    <div className="isolate flex justify-center -space-x-3 font-mono text-sm leading-6 font-bold text-white">
      <div className="flex size-16 items-center justify-center rounded-full bg-fuchsia-500 shadow-lg outline-2 outline-white dark:outline-[#11121E]">
        01
      </div>
      <div className="flex size-16 items-center justify-center rounded-full bg-fuchsia-500 shadow-lg outline-2 outline-white dark:outline-[#11121E]">
        02
      </div>
      <div className="-z-10 flex size-16 items-center justify-center rounded-full bg-fuchsia-500 shadow-lg outline-2 outline-white dark:outline-[#11121E]">
        03
      </div>
      <div className="flex size-16 items-center justify-center rounded-full bg-fuchsia-500 shadow-lg outline-2 outline-white dark:outline-[#11121E]">
        04
      </div>
      <div className="flex size-16 items-center justify-center rounded-full bg-fuchsia-500 shadow-lg outline-2 outline-white dark:outline-[#11121E]">
        05
      </div>
    </div>
  }

```html
<!-- [!code classes:-z-10] -->
<div class="...">05</div>
<div class="...">04</div>
<div class="-z-10 ...">03</div>
<div class="...">02</div>
<div class="...">01</div>
```

### Using a custom value

### Responsive design
