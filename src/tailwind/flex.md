---
title: flex
description: Utilities for controlling how flex items both grow and shrink.
source_url: https://tailwindcss.com/docs/flex
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: flex.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 730
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `flex-<number>` | `flex: <number>;` |
| `flex-<fraction>` | `flex: calc(<fraction> * 100%);` |
| `flex-auto` | `flex: auto;` |
| `flex-initial` | `flex: 0 auto;` |
| `flex-none` | `flex: none;` |
| `flex-(<custom-property>)` | `flex: var(<custom-property>);` |
| `flex-[<value>]` | `flex: <value>;` |

## Examples

### Basic example

Use `flex-<number>` utilities like `flex-1` to allow a flex item to grow and shrink as needed, ignoring its initial size:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 w-14 flex-none items-center justify-center rounded-lg bg-pink-300 p-4 dark:bg-pink-800 dark:text-pink-400">
          01
        </div>
        <div className="flex w-64 flex-1 items-center justify-center rounded-lg bg-pink-500 p-4">02</div>
        <div className="flex w-32 flex-1 items-center justify-center rounded-lg bg-pink-500 p-4">03</div>
      </div>
    </div>
  }

```html
<!-- [!code word:flex-1] -->
<div class="flex">
  <div class="w-14 flex-none ...">01</div>
  <div class="w-64 flex-1 ...">02</div>
  <div class="w-32 flex-1 ...">03</div>
</div>
```

### Initial

Use `flex-initial` to allow a flex item to shrink but not grow, taking into account its initial size:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 w-14 flex-none items-center justify-center rounded-lg bg-blue-300 p-4 dark:bg-blue-800 dark:text-blue-500">
          01
        </div>
        <div className="flex w-24 flex-initial items-center justify-center rounded-lg bg-blue-500 p-4 sm:w-64">02</div>
        <div className="flex w-14 flex-initial items-center justify-center rounded-lg bg-blue-500 p-4 sm:w-32">03</div>
      </div>
    </div>
  }

```html
<!-- [!code word:flex-initial] -->
<div class="flex">
  <div class="w-14 flex-none ...">01</div>
  <div class="w-64 flex-initial ...">02</div>
  <div class="w-32 flex-initial ...">03</div>
</div>
```

### Auto

Use `flex-auto` to allow a flex item to grow and shrink, taking into account its initial size:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 w-14 flex-none items-center justify-center rounded-lg bg-violet-300 p-4 dark:bg-violet-800 dark:text-violet-400">
          01
        </div>
        <div className="flex w-64 flex-auto items-center justify-center rounded-lg bg-violet-500 p-4">02</div>
        <div className="flex w-32 flex-auto items-center justify-center rounded-lg bg-violet-500 p-4">03</div>
      </div>
    </div>
  }

```html
<!-- [!code word:flex-auto] -->
<div class="flex ...">
  <div class="w-14 flex-none ...">01</div>
  <div class="w-64 flex-auto ...">02</div>
  <div class="w-32 flex-auto ...">03</div>
</div>
```

### None

Use `flex-none` to prevent a flex item from growing or shrinking:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex-none last:pr-8 sm:last:pr-0">
          <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-indigo-500 p-4">01</div>
        </div>
        <div className="flex-none last:pr-8 sm:last:pr-0">
          <div className="flex w-32 items-center justify-center rounded-lg bg-indigo-500 p-4">02</div>
        </div>
        <div className="flex-1 last:pr-8 sm:last:pr-0">
          <div className="flex items-center justify-center rounded-lg bg-indigo-300 p-4 dark:bg-indigo-800 dark:text-indigo-400">
            03
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code word:flex-none] -->
<div class="flex ...">
  <div class="w-14 flex-none ...">01</div>
  <div class="w-32 flex-none ...">02</div>
  <div class="flex-1 ...">03</div>
</div>
```

### Using a custom value

### Responsive design
