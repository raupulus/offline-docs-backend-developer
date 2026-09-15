---
title: place-content
description: Utilities for controlling how content is justified and aligned at the
  same time.
source_url: https://tailwindcss.com/docs/place-content
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: place-content.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1400
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `place-content-center` | `place-content: center;` |
| `place-content-center-safe` | `place-content: safe center;` |
| `place-content-start` | `place-content: start;` |
| `place-content-end` | `place-content: end;` |
| `place-content-end-safe` | `place-content: safe end;` |
| `place-content-between` | `place-content: space-between;` |
| `place-content-around` | `place-content: space-around;` |
| `place-content-evenly` | `place-content: space-evenly;` |
| `place-content-baseline` | `place-content: baseline;` |
| `place-content-stretch` | `place-content: stretch;` |

## Examples

### Center

Use `place-content-center` to pack items in the center of the inline and block axes:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 grid-cols-[repeat(2,56px)] place-content-center gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-sky-500 p-4">01</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-sky-500 p-4">02</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-sky-500 p-4">03</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-sky-500 p-4">04</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:place-content-center] -->
<div class="grid h-48 grid-cols-2 place-content-center gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

### Start

Use `place-content-start` to pack items against the start of the inline and block axes:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 grid-cols-[repeat(2,56px)] place-content-start gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-fuchsia-500 p-4">01</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-fuchsia-500 p-4">02</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-fuchsia-500 p-4">03</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-fuchsia-500 p-4">04</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:place-content-start] -->
<div class="grid h-48 grid-cols-2 place-content-start gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

### End

Use `place-content-end` to pack items against the end of the inline and block axes:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 grid-cols-[repeat(2,56px)] place-content-end gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-indigo-500 p-4">01</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-indigo-500 p-4">02</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-indigo-500 p-4">03</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-indigo-500 p-4">04</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:place-content-end] -->
<div class="grid h-48 grid-cols-2 place-content-end gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

### Space between

Use `place-content-between` to distribute grid items along the inline and block axes so that there is an equal amount of space between each row and column on each axis respectively:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 grid-cols-[repeat(2,56px)] place-content-between gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-purple-500 p-4">01</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-purple-500 p-4">02</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-purple-500 p-4">03</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-purple-500 p-4">04</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:place-content-between] -->
<div class="grid h-48 grid-cols-2 place-content-between gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

### Space around

Use `place-content-around` to distribute grid items along the inline and block axes so that there is an equal amount of space around each row and column on each axis respectively:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 grid-cols-[repeat(2,56px)] place-content-around gap-x-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-cyan-500 p-4">01</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-cyan-500 p-4">02</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-cyan-500 p-4">03</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-cyan-500 p-4">04</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:place-content-around] -->
<div class="grid h-48 grid-cols-2 place-content-around gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

### Space evenly

Use `place-content-evenly` to distribute grid items such that they are evenly spaced on the inline and block axes:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 grid-cols-[repeat(2,56px)] place-content-evenly rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-violet-500 p-4">01</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-violet-500 p-4">02</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-violet-500 p-4">03</div>
        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-violet-500 p-4">04</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:place-content-evenly] -->
<div class="grid h-48 grid-cols-2 place-content-evenly gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

### Stretch

Use `place-content-stretch` to stretch grid items along their grid areas on the inline and block axes:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid h-56 grid-cols-2 place-content-stretch gap-4 rounded-lg font-mono text-sm leading-6 font-bold text-white">
        <div className="flex items-center justify-center rounded-lg bg-pink-500 p-4">01</div>
        <div className="flex items-center justify-center rounded-lg bg-pink-500 p-4">02</div>
        <div className="flex items-center justify-center rounded-lg bg-pink-500 p-4">03</div>
        <div className="flex items-center justify-center rounded-lg bg-pink-500 p-4">04</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:place-content-stretch] -->
<div class="grid h-48 grid-cols-2 place-content-stretch gap-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

### Responsive design
