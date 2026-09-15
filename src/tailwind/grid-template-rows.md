---
title: grid-template-rows
description: Utilities for specifying the rows in a grid layout.
source_url: https://tailwindcss.com/docs/grid-template-rows
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: grid-template-rows.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 920
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `grid-rows-<number>` | `grid-template-rows: repeat(<number>, minmax(0, 1fr));` |
| `grid-rows-none` | `grid-template-rows: none;` |
| `grid-rows-subgrid` | `grid-template-rows: subgrid;` |
| `grid-rows-[<value>]` | `grid-template-rows: <value>;` |
| `grid-rows-(<custom-property>)` | `grid-template-rows: var(<custom-property>);` |

## Examples

### Specifying the grid rows

Use `grid-rows-<number>` utilities like `grid-rows-2` and `grid-rows-4` to create grids with _n_ equally sized rows:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid grid-flow-col grid-rows-4 gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-pink-500 p-4">01</div>
        <div className="rounded-lg bg-pink-500 p-4">02</div>
        <div className="rounded-lg bg-pink-500 p-4">03</div>
        <div className="rounded-lg bg-pink-500 p-4">04</div>
        <div className="rounded-lg bg-pink-500 p-4">05</div>
        <div className="rounded-lg bg-pink-500 p-4">06</div>
        <div className="rounded-lg bg-pink-500 p-4">07</div>
        <div className="rounded-lg bg-pink-500 p-4">08</div>
        <div className="rounded-lg bg-pink-500 p-4">09</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:grid-rows-4] -->
<div class="grid grid-flow-col grid-rows-4 gap-4">
  <div>01</div>
  <!-- ... -->
  <div>09</div>
</div>
```

### Implementing a subgrid

Use the `grid-rows-subgrid` utility to adopt the row tracks defined by the item's parent:

  {
    <div className="grid grid-flow-col grid-rows-4 gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
      <div className="grid h-14 items-center justify-center rounded-lg bg-indigo-300 dark:bg-indigo-900">01</div>
      <div className="grid h-14 items-center justify-center rounded-lg bg-indigo-300 dark:bg-indigo-900">02</div>
      <div className="grid h-14 items-center justify-center rounded-lg bg-indigo-300 dark:bg-indigo-900">03</div>
      <div className="grid h-14 items-center justify-center rounded-lg bg-indigo-300 dark:bg-indigo-900">04</div>
      <div className="grid h-14 items-center justify-center rounded-lg bg-indigo-300 dark:bg-indigo-900">05</div>
      <div className="row-span-3 grid grid-rows-subgrid gap-4">
        
        <div className="grid h-14 items-center justify-center rounded-lg bg-fuchsia-500">06</div>
        
      </div>
      <div className="grid h-14 items-center justify-center rounded-lg bg-indigo-300 dark:bg-indigo-900">07</div>
      <div className="grid h-14 items-center justify-center rounded-lg bg-indigo-300 dark:bg-indigo-900">08</div>
      <div className="grid h-14 items-center justify-center rounded-lg bg-indigo-300 dark:bg-indigo-900">09</div>
      <div className="grid h-14 items-center justify-center rounded-lg bg-indigo-300 dark:bg-indigo-900">10</div>
    </div>
  }

```html
<!-- [!code classes:grid-rows-subgrid] -->
<div class="grid grid-flow-col grid-rows-4 gap-4">
  <div>01</div>
  <!-- ... -->
  <div>05</div>
  <div class="row-span-3 grid grid-rows-subgrid gap-4">
    <div class="row-start-2">06</div>
  </div>
  <div>07</div>
  <!-- ... -->
  <div>10</div>
</div>
```

### Using a custom value

### Responsive design
