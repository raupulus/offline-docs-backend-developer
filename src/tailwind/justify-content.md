---
title: justify-content
source_url: https://tailwindcss.com/docs/justify-content
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: justify-content.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 980
---

"Utilities for controlling how flex and grid items are positioned along a container's main axis.";

| Clase | Propiedades CSS |
| :--- | :--- |
| `justify-start` | `justify-content: flex-start;` |
| `justify-end` | `justify-content: flex-end;` |
| `justify-end-safe` | `justify-content: safe flex-end;` |
| `justify-center` | `justify-content: center;` |
| `justify-center-safe` | `justify-content: safe center;` |
| `justify-between` | `justify-content: space-between;` |
| `justify-around` | `justify-content: space-around;` |
| `justify-evenly` | `justify-content: space-evenly;` |
| `justify-stretch` | `justify-content: stretch;` |
| `justify-baseline` | `justify-content: baseline;` |
| `justify-normal` | `justify-content: normal;` |

## Examples

### Start

Use the `justify-start` utility to justify items against the start of the container's main axis:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex justify-start space-x-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-fuchsia-500">01</div>
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-fuchsia-500">02</div>
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-fuchsia-500">03</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:justify-start] -->
<div class="flex justify-start ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Center

Use the `justify-center` or `justify-center-safe` utilities to justify items along the center of the container's main axis:

  {
    <div className="grid grid-cols-1 gap-8">
      <div>
        <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">justify-center</p>
        <div className="mt-4 grid grid-cols-1">
          
          <div className="col-start-1 row-start-1 flex justify-center space-x-4 overflow-hidden rounded-lg font-mono text-sm leading-6 font-bold text-white">
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-blue-500">01</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-blue-500">02</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-blue-500">03</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-blue-500">04</div>
          </div>
        </div>
      </div>
      <div>
        <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          justify-center-safe
        </p>
        <div className="mt-4 grid grid-cols-1">
          
          <div className="col-start-1 row-start-1 flex justify-center-safe space-x-4 overflow-hidden rounded-lg font-mono text-sm leading-6 font-bold text-white">
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-indigo-500">01</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-indigo-500">02</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-indigo-500">03</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-indigo-500">04</div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code filename:justify-center] -->
<!-- [!code classes:justify-center] -->
<div class="flex justify-center ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

```html
<!-- [!code filename:justify-center-safe] -->
<!-- [!code classes:justify-center-safe] -->
<div class="flex justify-center-safe ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

When there is not enough space available, the `justify-center-safe` utility will align items to the start of the container instead of the center.

### End

Use the `justify-end` or `justify-end-safe` utilities to justify items against the end of the container's main axis:

  {
    <div className="grid grid-cols-1 gap-8">
      <div>
        <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">justify-end</p>
        <div className="mt-4 grid grid-cols-1">
          
          <div className="col-start-1 row-start-1 flex justify-end space-x-4 overflow-hidden rounded-lg font-mono text-sm leading-6 font-bold text-white">
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-pink-500">01</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-pink-500">02</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-pink-500">03</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-pink-500">04</div>
          </div>
        </div>
      </div>
      <div>
        <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">justify-end-safe</p>
        <div className="mt-4 grid grid-cols-1">
          
          <div className="col-start-1 row-start-1 flex justify-end-safe space-x-4 overflow-hidden rounded-lg font-mono text-sm leading-6 font-bold text-white">
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-fuchsia-500">01</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-fuchsia-500">02</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-fuchsia-500">03</div>
            <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-fuchsia-500">04</div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code filename:justify-end] -->
<!-- [!code classes:justify-end] -->
<div class="flex justify-end ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

```html
<!-- [!code filename:justify-end-safe] -->
<!-- [!code classes:justify-end-safe] -->
<div class="flex justify-end-safe ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

When there is not enough space available, the `justify-end-safe` utility will align items to the start of the container instead of the end.

### Space between

Use the `justify-between` utility to justify items along the container's main axis such that there is an equal amount of space between each item:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex justify-between space-x-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-cyan-500">01</div>
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-cyan-500">02</div>
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-cyan-500">03</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:justify-between] -->
<div class="flex justify-between ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Space around

Use the `justify-around` utility to justify items along the container's main axis such that there is an equal amount of space on each side of each item:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex justify-around space-x-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-purple-500">01</div>
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-purple-500">02</div>
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-purple-500">03</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:justify-around] -->
<div class="flex justify-around ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Space evenly

Use the `justify-evenly` utility to justify items along the container's main axis such that there is an equal amount of space around each item, but also accounting for the doubling of space you would normally see between each item when using `justify-around`:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex justify-evenly space-x-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-indigo-500">01</div>
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-indigo-500">02</div>
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-indigo-500">03</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:justify-evenly] -->
<div class="flex justify-evenly ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Stretch

Use the `justify-stretch` utility to allow auto-sized content items to fill the available space along the container's main axis:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid grid-cols-[4rem_auto_4rem] justify-stretch gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 items-center justify-center rounded-lg bg-fuchsia-500">01</div>
        <div className="flex h-14 items-center justify-center rounded-lg bg-fuchsia-500">02</div>
        <div className="flex h-14 items-center justify-center rounded-lg bg-fuchsia-500">03</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:justify-stretch] -->
<div class="grid grid-cols-[4rem_auto_4rem] justify-stretch ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Normal

Use the `justify-normal` utility to pack content items in their default position as if no `justify-content` value was set:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex justify-normal space-x-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-blue-500">01</div>
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-blue-500">02</div>
        <div className="flex size-14 shrink-0 items-center justify-center rounded-lg bg-blue-500">03</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:justify-normal] -->
<div class="flex justify-normal ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Responsive design
