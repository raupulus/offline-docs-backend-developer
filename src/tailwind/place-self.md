---
title: place-self
description: Utilities for controlling how an individual item is justified and aligned
  at the same time.
source_url: https://tailwindcss.com/docs/place-self
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: place-self.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1420
---

"Utilities for controlling how an individual item is justified and aligned at the same time.";

| Clase | Propiedades CSS |
| :--- | :--- |
| `place-self-auto` | `place-self: auto;` |
| `place-self-start` | `place-self: start;` |
| `place-self-end` | `place-self: end;` |
| `place-self-end-safe` | `place-self: safe end;` |
| `place-self-center` | `place-self: center;` |
| `place-self-center-safe` | `place-self: safe center;` |
| `place-self-stretch` | `place-self: stretch;` |

## Examples

### Auto

Use `place-self-auto` to align an item based on the value of the container's `place-items` property:

  {
    <div className="grid grid-cols-3 place-items-stretch gap-4 font-mono text-sm leading-6 font-bold text-white">
      <div className="flex items-center justify-center rounded-lg bg-indigo-300 p-8 dark:bg-indigo-800 dark:text-indigo-400">
        01
      </div>
      <div className="flex items-center justify-center place-self-auto rounded-lg bg-indigo-500 p-8">02</div>
      <div className="flex items-center justify-center rounded-lg bg-indigo-300 p-8 dark:bg-indigo-800 dark:text-indigo-400">
        03
      </div>
      <div className="flex items-center justify-center rounded-lg bg-indigo-300 p-8 dark:bg-indigo-800 dark:text-indigo-400">
        04
      </div>
      <div className="flex items-center justify-center rounded-lg bg-indigo-300 p-8 dark:bg-indigo-800 dark:text-indigo-400">
        05
      </div>
      <div className="flex items-center justify-center rounded-lg bg-indigo-300 p-8 dark:bg-indigo-800 dark:text-indigo-400">
        06
      </div>
    </div>
  }

```html
<!-- [!code classes:place-self-auto] -->
<div class="grid grid-cols-3 gap-4 ...">
  <div>01</div>
  <div class="place-self-auto ...">02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

### Start

Use `place-self-start` to align an item to the start on both axes:

  {
    <div className="grid grid-cols-3 place-items-stretch gap-4 font-mono text-sm leading-6 font-bold text-white">
      <div className="flex items-center justify-center rounded-lg bg-purple-300 p-8 dark:bg-purple-800 dark:text-purple-400">
        01
      </div>
      <div className="grid grid-cols-1">
        
        <div className="col-start-1 row-start-1 flex size-14 items-center justify-center place-self-start rounded-lg bg-purple-500">
          02
        </div>
      </div>
      <div className="flex items-center justify-center rounded-lg bg-purple-300 p-8 dark:bg-purple-800 dark:text-purple-400">
        03
      </div>
      <div className="flex items-center justify-center rounded-lg bg-purple-300 p-8 dark:bg-purple-800 dark:text-purple-400">
        04
      </div>
      <div className="flex items-center justify-center rounded-lg bg-purple-300 p-8 dark:bg-purple-800 dark:text-purple-400">
        05
      </div>
      <div className="flex items-center justify-center rounded-lg bg-purple-300 p-8 dark:bg-purple-800 dark:text-purple-400">
        06
      </div>
    </div>
  }

```html
<!-- [!code classes:place-self-start] -->
<div class="grid grid-cols-3 gap-4 ...">
  <div>01</div>
  <div class="place-self-start ...">02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

### Center

Use `place-self-center` to align an item at the center on both axes:

  {
    <div className="grid grid-cols-3 place-items-stretch gap-4 font-mono text-sm leading-6 font-bold text-white">
      <div className="flex items-center justify-center rounded-lg bg-sky-300 p-8 dark:bg-sky-800 dark:text-sky-500">
        01
      </div>
      <div className="grid grid-cols-1">
        
        <div className="col-start-1 row-start-1 flex size-14 items-center justify-center place-self-center rounded-lg bg-sky-500">
          02
        </div>
      </div>
      <div className="flex items-center justify-center rounded-lg bg-sky-300 p-8 dark:bg-sky-800 dark:text-sky-500">
        03
      </div>
      <div className="flex items-center justify-center rounded-lg bg-sky-300 p-8 dark:bg-sky-800 dark:text-sky-500">
        04
      </div>
      <div className="flex items-center justify-center rounded-lg bg-sky-300 p-8 dark:bg-sky-800 dark:text-sky-500">
        05
      </div>
      <div className="flex items-center justify-center rounded-lg bg-sky-300 p-8 dark:bg-sky-800 dark:text-sky-500">
        06
      </div>
    </div>
  }

```html
<!-- [!code classes:place-self-center] -->
<div class="grid grid-cols-3 gap-4 ...">
  <div>01</div>
  <div class="place-self-center ...">02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

### End

Use `place-self-end` to align an item to the end on both axes:

  {
    <div className="grid grid-cols-3 place-items-stretch gap-4 font-mono text-sm leading-6 font-bold text-white">
      <div className="flex items-center justify-center rounded-lg bg-pink-300 p-8 dark:bg-pink-800 dark:text-pink-400">
        01
      </div>
      <div className="grid grid-cols-1">
        
        <div className="col-start-1 row-start-1 flex size-14 items-center justify-center place-self-end rounded-lg bg-pink-500">
          02
        </div>
      </div>
      <div className="flex items-center justify-center rounded-lg bg-pink-300 p-8 dark:bg-pink-800 dark:text-pink-400">
        03
      </div>
      <div className="flex items-center justify-center rounded-lg bg-pink-300 p-8 dark:bg-pink-800 dark:text-pink-400">
        04
      </div>
      <div className="flex items-center justify-center rounded-lg bg-pink-300 p-8 dark:bg-pink-800 dark:text-pink-400">
        05
      </div>
      <div className="flex items-center justify-center rounded-lg bg-pink-300 p-8 dark:bg-pink-800 dark:text-pink-400">
        06
      </div>
    </div>
  }

```html
<!-- [!code classes:place-self-end] -->
<div class="grid grid-cols-3 gap-4 ...">
  <div>01</div>
  <div class="place-self-end ...">02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

### Stretch

Use `place-self-stretch` to stretch an item on both axes:

  {
    <div className="grid grid-cols-3 place-items-stretch gap-4 font-mono text-sm leading-6 font-bold text-white">
      <div className="flex items-center justify-center rounded-lg bg-fuchsia-300 p-8 dark:bg-fuchsia-800 dark:text-fuchsia-400">
        01
      </div>
      <div className="flex items-center justify-center place-self-stretch rounded-lg bg-fuchsia-500 p-8">02</div>
      <div className="flex items-center justify-center rounded-lg bg-fuchsia-300 p-8 dark:bg-fuchsia-800 dark:text-fuchsia-400">
        03
      </div>
      <div className="flex items-center justify-center rounded-lg bg-fuchsia-300 p-8 dark:bg-fuchsia-800 dark:text-fuchsia-400">
        04
      </div>
      <div className="flex items-center justify-center rounded-lg bg-fuchsia-300 p-8 dark:bg-fuchsia-800 dark:text-fuchsia-400">
        05
      </div>
      <div className="flex items-center justify-center rounded-lg bg-fuchsia-300 p-8 dark:bg-fuchsia-800 dark:text-fuchsia-400">
        06
      </div>
    </div>
  }

```html
<!-- [!code classes:place-self-stretch] -->
<div class="grid grid-cols-3 gap-4 ...">
  <div>01</div>
  <div class="place-self-stretch ...">02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

### Responsive design
