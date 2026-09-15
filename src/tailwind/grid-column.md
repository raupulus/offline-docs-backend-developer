---
title: grid-column
description: Utilities for controlling how elements are sized and placed across grid
  columns.
source_url: https://tailwindcss.com/docs/grid-column
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: grid-column.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 890
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `col-span-<number>` | `grid-column: span <number> / span <number>;` |
| `col-span-full` | `grid-column: 1 / -1;` |
| `col-span-(<custom-property>)` | `grid-column: span var(<custom-property>) / span var(<custom-property>);` |
| `col-span-[<value>]` | `grid-column: span <value> / span <value>;` |
| `col-start-<number>` | `grid-column-start: <number>;` |
| `-col-start-<number>` | `grid-column-start: calc(<number> * -1);` |
| `col-start-auto` | `grid-column-start: auto;` |
| `col-start-(<custom-property>)` | `grid-column-start: var(<custom-property>);` |
| `col-start-[<value>]` | `grid-column-start: <value>;` |
| `col-end-<number>` | `grid-column-end: <number>;` |
| `-col-end-<number>` | `grid-column-end: calc(<number> * -1);` |
| `col-end-auto` | `grid-column-end: auto;` |
| `col-end-(<custom-property>)` | `grid-column-end: var(<custom-property>);` |
| `col-end-[<value>]` | `grid-column-end: <value>;` |
| `col-auto` | `grid-column: auto;` |
| `col-<number>` | `grid-column: <number>;` |
| `-col-<number>` | `grid-column: calc(<number> * -1);` |
| `col-(<custom-property>)` | `grid-column: var(<custom-property>);` |
| `col-[<value>]` | `grid-column: <value>;` |

## Examples

### Spanning columns

Use `col-span-<number>` utilities like `col-span-2` and `col-span-4` to make an element span _n_ columns:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid grid-cols-3 gap-4 text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-indigo-300 p-4 dark:bg-indigo-800 dark:text-indigo-400">01</div>
        <div className="rounded-lg bg-indigo-300 p-4 dark:bg-indigo-800 dark:text-indigo-400">02</div>
        <div className="rounded-lg bg-indigo-300 p-4 dark:bg-indigo-800 dark:text-indigo-400">03</div>
        <div className="col-span-2 rounded-lg bg-indigo-500 p-4">04</div>
        <div className="rounded-lg bg-indigo-300 p-4 dark:bg-indigo-800 dark:text-indigo-400">05</div>
        <div className="rounded-lg bg-indigo-300 p-4 dark:bg-indigo-800 dark:text-indigo-400">06</div>
        <div className="col-span-2 rounded-lg bg-indigo-500 p-4">07</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:col-span-2] -->
<div class="grid grid-cols-3 gap-4">
  <div class="...">01</div>
  <div class="...">02</div>
  <div class="...">03</div>
  <div class="col-span-2 ...">04</div>
  <div class="...">05</div>
  <div class="...">06</div>
  <div class="col-span-2 ...">07</div>
</div>
```

### Starting and ending lines

Use `col-start-<number>` or `col-end-<number>` utilities like `col-start-2` and `col-end-3` to make an element start or end at the _nth_ grid line:

  {
    <div className="grid grid-cols-6 gap-4 text-center font-mono text-sm leading-6 font-bold text-white">
      
      <div className="col-span-4 col-start-2 rounded-lg bg-sky-500 p-4">01</div>
      
      <div className="col-start-1 col-end-3 rounded-lg bg-sky-500 p-4">02</div>
      
      
      <div className="col-span-2 col-end-7 rounded-lg bg-sky-500 p-4">03</div>
      <div className="col-start-1 col-end-7 rounded-lg bg-sky-500 p-4">04</div>
    </div>
  }

```html
<!-- [!code classes:col-start-1,col-start-2,col-end-3,col-end-7] -->
<div class="grid grid-cols-6 gap-4">
  <div class="col-span-4 col-start-2 ...">01</div>
  <div class="col-start-1 col-end-3 ...">02</div>
  <div class="col-span-2 col-end-7 ...">03</div>
  <div class="col-start-1 col-end-7 ...">04</div>
</div>
```

These can also be combined with the `col-span-<number>` utilities to span a specific number of columns.

### Using a custom value

### Responsive design
