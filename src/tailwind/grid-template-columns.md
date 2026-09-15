---
title: grid-template-columns
description: Utilities for specifying the columns in a grid layout.
source_url: https://tailwindcss.com/docs/grid-template-columns
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: grid-template-columns.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 910
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `grid-cols-<number>` | `grid-template-columns: repeat(<number>, minmax(0, 1fr));` |
| `grid-cols-none` | `grid-template-columns: none;` |
| `grid-cols-subgrid` | `grid-template-columns: subgrid;` |
| `grid-cols-[<value>]` | `grid-template-columns: <value>;` |
| `grid-cols-(<custom-property>)` | `grid-template-columns: var(<custom-property>);` |

## Examples

### Specifying the grid columns

Use `grid-cols-<number>` utilities like `grid-cols-2` and `grid-cols-4` to create grids with _n_ equally sized columns:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid grid-cols-4 gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-fuchsia-500 p-4">01</div>
        <div className="rounded-lg bg-fuchsia-500 p-4">02</div>
        <div className="rounded-lg bg-fuchsia-500 p-4">03</div>
        <div className="rounded-lg bg-fuchsia-500 p-4">04</div>
        <div className="rounded-lg bg-fuchsia-500 p-4">05</div>
        <div className="rounded-lg bg-fuchsia-500 p-4">06</div>
        <div className="rounded-lg bg-fuchsia-500 p-4">07</div>
        <div className="rounded-lg bg-fuchsia-500 p-4">08</div>
        <div className="rounded-lg bg-fuchsia-500 p-4">09</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:grid-cols-4] -->
<div class="grid grid-cols-4 gap-4">
  <div>01</div>
  <!-- ... -->
  <div>09</div>
</div>
```

### Implementing a subgrid

Use the `grid-cols-subgrid` utility to adopt the column tracks defined by the item's parent:

  {
    <div className="grid grid-cols-4 gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
      <div className="rounded-lg bg-indigo-300 p-4 dark:bg-indigo-900">01</div>
      <div className="rounded-lg bg-indigo-300 p-4 dark:bg-indigo-900">02</div>
      <div className="rounded-lg bg-indigo-300 p-4 dark:bg-indigo-900">03</div>
      <div className="rounded-lg bg-indigo-300 p-4 dark:bg-indigo-900">04</div>
      <div className="rounded-lg bg-indigo-300 p-4 dark:bg-indigo-900">05</div>
      <div className="col-span-3 grid grid-cols-subgrid gap-4">
        
        <div className="rounded-lg bg-pink-500 p-4">06</div>
        
      </div>
    </div>
  }

```html
<!-- [!code classes:grid-cols-subgrid] -->
<div class="grid grid-cols-4 gap-4">
  <div>01</div>
  <!-- ... -->
  <div>05</div>
  <div class="col-span-3 grid grid-cols-subgrid gap-4">
    <div class="col-start-2">06</div>
  </div>
</div>
```

### Using a custom value

### Responsive design
