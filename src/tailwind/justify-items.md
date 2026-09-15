---
title: justify-items
description: Utilities for controlling how grid items are aligned along their inline
  axis.
source_url: https://tailwindcss.com/docs/justify-items
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: justify-items.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 990
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `justify-items-start` | `justify-items: start;` |
| `justify-items-end` | `justify-items: end;` |
| `justify-items-end-safe` | `justify-items: safe end;` |
| `justify-items-center` | `justify-items: center;` |
| `justify-items-center-safe` | `justify-items: safe center;` |
| `justify-items-stretch` | `justify-items: stretch;` |
| `justify-items-normal` | `justify-items: normal;` |

## Examples

### Start

Use the `justify-items-start` utility to justify grid items against the start of their inline axis:

  {
    <div className="grid grid-cols-3 gap-4 font-mono text-sm leading-6 font-bold text-white">
      <div className="grid rounded-lg">
        
        <div className="col-start-1 row-start-1 flex size-14 items-center justify-center justify-self-start rounded-lg bg-sky-500">
          01
        </div>
      </div>
      <div className="grid rounded-lg">
        
        <div className="col-start-1 row-start-1 flex size-14 items-center justify-center justify-self-start rounded-lg bg-sky-500">
          02
        </div>
      </div>
      <div className="grid rounded-lg">
        
        <div className="col-start-1 row-start-1 flex size-14 items-center justify-center justify-self-start rounded-lg bg-sky-500">
          03
        </div>
      </div>
      <div className="grid rounded-lg">
        
        <div className="col-start-1 row-start-1 flex size-14 items-center justify-center justify-self-start rounded-lg bg-sky-500">
          04
        </div>
      </div>
      <div className="grid rounded-lg">
        
        <div className="col-start-1 row-start-1 flex size-14 items-center justify-center justify-self-start rounded-lg bg-sky-500">
          05
        </div>
      </div>
      <div className="grid rounded-lg">
        
        <div className="col-start-1 row-start-1 flex size-14 items-center justify-center justify-self-start rounded-lg bg-sky-500">
          06
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:justify-items-start] -->
<div class="grid justify-items-start ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

### End

Use the `justify-items-end` or `justify-items-end-safe` utilities to justify grid items against the end of their inline axis:

  {
    <div className="grid grid-cols-1 gap-8">
      <div>
        <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">justify-items-end</p>
        <div className="mt-4 grid auto-rows-fr grid-cols-3 justify-items-stretch gap-10 text-center font-mono text-sm leading-6 font-bold text-white">
          <div className="grid grid-cols-1 justify-items-end">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-blue-500 p-4">01</div>
          </div>
          <div className="grid grid-cols-1 justify-items-end">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-blue-500 p-4">02</div>
          </div>
          <div className="grid grid-cols-1 justify-items-end">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-blue-500 p-4">03</div>
          </div>
        </div>
      </div>
      <div>
        <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          justify-items-end-safe
        </p>
        <div className="mt-4 grid auto-rows-fr grid-cols-3 justify-items-stretch gap-10 text-center font-mono text-sm leading-6 font-bold text-white">
          <div className="grid grid-cols-1 justify-items-end-safe">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-purple-500 p-4">01</div>
          </div>
          <div className="grid grid-cols-1 justify-items-end-safe">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-purple-500 p-4">02</div>
          </div>
          <div className="grid grid-cols-1 justify-items-end-safe">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-purple-500 p-4">03</div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code filename:justify-items-end] -->
<!-- [!code classes:justify-items-end] -->
<div class="grid grid-flow-col justify-items-end ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

```html
<!-- [!code filename:justify-items-end-safe] -->
<!-- [!code classes:justify-items-end-safe] -->
<div class="grid grid-flow-col justify-items-end-safe ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

</ CodeExampleStack>

When there is not enough space available, the `justify-items-end-safe` utility will align items to the start of the container instead of the end.

### Center

Use the `justify-items-center` or `justify-items-center-safe` utilities to justify grid items against the end of their inline axis:

  {
    <div className="grid grid-cols-1 gap-8">
      <div>
        <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          justify-items-center
        </p>
        <div className="mt-4 grid auto-rows-fr grid-cols-3 justify-items-stretch gap-10 text-center font-mono text-sm leading-6 font-bold text-white">
          <div className="grid grid-cols-1 justify-items-center">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-indigo-500 p-4">01</div>
          </div>
          <div className="grid grid-cols-1 justify-items-center">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-indigo-500 p-4">02</div>
          </div>
          <div className="grid grid-cols-1 justify-items-center">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-indigo-500 p-4">03</div>
          </div>
        </div>
      </div>
      <div>
        <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          justify-items-center-safe
        </p>
        <div className="mt-4 grid auto-rows-fr grid-cols-3 justify-items-stretch gap-10 text-center font-mono text-sm leading-6 font-bold text-white">
          <div className="grid grid-cols-1 justify-items-center-safe">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-fuchsia-500 p-4">01</div>
          </div>
          <div className="grid grid-cols-1 justify-items-center-safe">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-fuchsia-500 p-4">02</div>
          </div>
          <div className="grid grid-cols-1 justify-items-center-safe">
            
            <div className="col-start-1 row-start-1 size-14 rounded-lg bg-fuchsia-500 p-4">03</div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code filename:justify-items-center] -->
<!-- [!code classes:justify-items-center] -->
<div class="grid grid-flow-col justify-items-center ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

```html
<!-- [!code filename:justify-items-center-safe] -->
<!-- [!code classes:justify-items-center-safe] -->
<div class="grid grid-flow-col justify-items-center-safe ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

When there is not enough space available, the `justify-items-center-safe` utility will align items to the start of the container instead of the center.

### Stretch

Use the `justify-items-stretch` utility to stretch items along their inline axis:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid grid-cols-3 justify-items-stretch gap-4 font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 items-center justify-center rounded-lg bg-blue-500">01</div>
        <div className="flex h-14 items-center justify-center rounded-lg bg-blue-500">02</div>
        <div className="flex h-14 items-center justify-center rounded-lg bg-blue-500">03</div>
        <div className="flex h-14 items-center justify-center rounded-lg bg-blue-500">04</div>
        <div className="flex h-14 items-center justify-center rounded-lg bg-blue-500">05</div>
        <div className="flex h-14 items-center justify-center rounded-lg bg-blue-500">06</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:justify-items-stretch] -->
<div class="grid justify-items-stretch ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

### Responsive design
