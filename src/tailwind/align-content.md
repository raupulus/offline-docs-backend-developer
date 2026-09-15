---
title: align-content
description: Utilities for controlling how rows are positioned in multi-row flex and
  grid containers.
source_url: https://tailwindcss.com/docs/align-content
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: align-content.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 30
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `content-normal` | `align-content: normal;` |
| `content-center` | `align-content: center;` |
| `content-start` | `align-content: flex-start;` |
| `content-end` | `align-content: flex-end;` |
| `content-between` | `align-content: space-between;` |
| `content-around` | `align-content: space-around;` |
| `content-evenly` | `align-content: space-evenly;` |
| `content-baseline` | `align-content: baseline;` |
| `content-stretch` | `align-content: stretch;` |

## Examples

### Start

Use `content-start` to pack rows in a container against the start of the cross axis:

  {
    <div className="grid h-56 grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid grid-cols-3 content-start gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-purple-500 p-4">01</div>
        <div className="rounded-lg bg-purple-500 p-4">02</div>
        <div className="rounded-lg bg-purple-500 p-4">03</div>
        <div className="rounded-lg bg-purple-500 p-4">04</div>
        <div className="rounded-lg bg-purple-500 p-4">05</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:content-start] -->
<div class="grid h-56 grid-cols-3 content-start gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

### Center

Use `content-center` to pack rows in a container in the center of the cross axis:

  {
    <div className="grid h-56 grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 w-full grid-cols-3 content-center gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-sky-500 p-4">01</div>
        <div className="rounded-lg bg-sky-500 p-4">02</div>
        <div className="rounded-lg bg-sky-500 p-4">03</div>
        <div className="rounded-lg bg-sky-500 p-4">04</div>
        <div className="rounded-lg bg-sky-500 p-4">05</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:content-center] -->
<div class="grid h-56 grid-cols-3 content-center gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

### End

Use `content-end` to pack rows in a container against the end of the cross axis:

  {
    <div className="grid h-56 grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 w-full grid-cols-3 content-end gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-pink-500 p-4">01</div>
        <div className="rounded-lg bg-pink-500 p-4">02</div>
        <div className="rounded-lg bg-pink-500 p-4">03</div>
        <div className="rounded-lg bg-pink-500 p-4">04</div>
        <div className="rounded-lg bg-pink-500 p-4">05</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:content-end] -->
<div class="grid h-56 grid-cols-3 content-end gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

### Space between

Use `content-between` to distribute rows in a container such that there is an equal amount of space between each line:

  {
    <div className="grid h-56 grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 w-full grid-cols-3 content-between gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-violet-500 p-4">01</div>
        <div className="rounded-lg bg-violet-500 p-4">02</div>
        <div className="rounded-lg bg-violet-500 p-4">03</div>
        <div className="rounded-lg bg-violet-500 p-4">04</div>
        <div className="rounded-lg bg-violet-500 p-4">05</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:content-between] -->
<div class="grid h-56 grid-cols-3 content-between gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

### Space around

Use `content-around` to distribute rows in a container such that there is an equal amount of space around each line:

  {
    <div className="grid h-56 grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 w-full grid-cols-3 content-around gap-x-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-blue-500 p-4">01</div>
        <div className="rounded-lg bg-blue-500 p-4">02</div>
        <div className="rounded-lg bg-blue-500 p-4">03</div>
        <div className="rounded-lg bg-blue-500 p-4">04</div>
        <div className="rounded-lg bg-blue-500 p-4">05</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:content-around] -->
<div class="grid h-56 grid-cols-3 content-around gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

### Space evenly

Use `content-evenly` to distribute rows in a container such that there is an equal amount of space around each item, but also accounting for the doubling of space you would normally see between each item when using `content-around`:

  {
    <div className="grid h-56 grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 w-full grid-cols-3 content-evenly gap-x-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-indigo-500 p-4">01</div>
        <div className="rounded-lg bg-indigo-500 p-4">02</div>
        <div className="rounded-lg bg-indigo-500 p-4">03</div>
        <div className="rounded-lg bg-indigo-500 p-4">04</div>
        <div className="rounded-lg bg-indigo-500 p-4">05</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:content-evenly] -->
<div class="grid h-56 grid-cols-3 content-evenly gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

### Stretch

Use `content-stretch` to allow content items to fill the available space along the container’s cross axis:

  {
    <div className="grid h-56 grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 w-full grid-cols-3 content-stretch gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="flex items-center justify-center rounded-lg bg-fuchsia-500 p-4">01</div>
        <div className="flex items-center justify-center rounded-lg bg-fuchsia-500 p-4">02</div>
        <div className="flex items-center justify-center rounded-lg bg-fuchsia-500 p-4">03</div>
        <div className="flex items-center justify-center rounded-lg bg-fuchsia-500 p-4">04</div>
        <div className="flex items-center justify-center rounded-lg bg-fuchsia-500 p-4">05</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:content-stretch] -->
<div class="grid h-56 grid-cols-3 content-stretch gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

### Normal

Use `content-normal` to pack content items in their default position as if no `align-content` value was set:

  {
    <div className="grid h-56 grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 w-full grid-cols-3 gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="flex items-center justify-center rounded-lg bg-indigo-500 p-4">01</div>
        <div className="flex items-center justify-center rounded-lg bg-indigo-500 p-4">02</div>
        <div className="flex items-center justify-center rounded-lg bg-indigo-500 p-4">03</div>
        <div className="flex items-center justify-center rounded-lg bg-indigo-500 p-4">04</div>
        <div className="flex items-center justify-center rounded-lg bg-indigo-500 p-4">05</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:content-normal] -->
<div class="grid h-56 grid-cols-3 content-normal gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

### Responsive design
