---
title: gap
description: Utilities for controlling gutters between grid and flexbox items.
source_url: https://tailwindcss.com/docs/gap
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: gap.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 850
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `gap-<number>` | `gap: calc(var(--spacing) * <value>);` |
| `gap-px` | `gap: 1px;` |
| `gap-(<custom-property>)` | `gap: var(<custom-property>);` |
| `gap-[<value>]` | `gap: <value>;` |
| `gap-x-<number>` | `column-gap: calc(var(--spacing) * <value>);` |
| `gap-x-px` | `column-gap: 1px;` |
| `gap-x-(<custom-property>)` | `column-gap: var(<custom-property>);` |
| `gap-x-[<value>]` | `column-gap: <value>;` |
| `gap-y-<number>` | `row-gap: calc(var(--spacing) * <value>);` |
| `gap-y-px` | `row-gap: 1px;` |
| `gap-y-(<custom-property>)` | `row-gap: var(<custom-property>);` |
| `gap-y-[<value>]` | `row-gap: <value>;` |

## Examples

### Basic example

Use `gap-<number>` utilities like `gap-2` and `gap-4` to change the gap between both rows and columns in grid and flexbox layouts:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid grid-cols-2 gap-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-violet-500 p-4">01</div>
        <div className="rounded-lg bg-violet-500 p-4">02</div>
        <div className="rounded-lg bg-violet-500 p-4">03</div>
        <div className="rounded-lg bg-violet-500 p-4">04</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:gap-4] -->
<div class="grid grid-cols-2 gap-4">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

### Changing row and column gaps independently

Use `gap-x-<number>` or `gap-y-<number>` utilities like `gap-x-8` and `gap-y-4` to change the gap between columns and rows independently:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 grid grid-cols-3 gap-x-8 gap-y-4 rounded-lg text-center font-mono text-sm leading-6 font-bold text-white">
        <div className="rounded-lg bg-sky-500 p-4">01</div>
        <div className="rounded-lg bg-sky-500 p-4">02</div>
        <div className="rounded-lg bg-sky-500 p-4">03</div>
        <div className="rounded-lg bg-sky-500 p-4">04</div>
        <div className="rounded-lg bg-sky-500 p-4">05</div>
        <div className="rounded-lg bg-sky-500 p-4">06</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:gap-x-8,gap-y-4] -->
<div class="grid grid-cols-3 gap-x-8 gap-y-4">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

### Using a custom value

### Responsive design
