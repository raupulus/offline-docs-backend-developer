---
title: flex-wrap
description: Utilities for controlling how flex items wrap.
source_url: https://tailwindcss.com/docs/flex-wrap
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: flex-wrap.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 720
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `flex-nowrap` | `flex-wrap: nowrap;` |
| `flex-wrap` | `flex-wrap: wrap;` |
| `flex-wrap-reverse` | `flex-wrap: wrap-reverse;` |

## Examples

### Don't wrap

Use `flex-nowrap` to prevent flex items from wrapping, causing inflexible items to overflow the container if necessary:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex flex-nowrap gap-4 rounded-lg font-mono text-sm/6 font-bold text-white">
        <div className="w-2/5 flex-none last:pr-8">
          <div className="flex w-full items-center justify-center rounded-lg bg-sky-500 p-4">01</div>
        </div>
        <div className="w-2/5 flex-none last:pr-8">
          <div className="flex w-full items-center justify-center rounded-lg bg-sky-500 p-4">02</div>
        </div>
        <div className="w-2/5 flex-none last:pr-8">
          <div className="flex w-full items-center justify-center rounded-lg bg-sky-500 p-4">03</div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:flex-nowrap] -->
<div class="flex flex-nowrap">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Wrap normally

Use `flex-wrap` to allow flex items to wrap:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex flex-wrap gap-4 rounded-lg font-mono text-sm/6 font-bold text-white">
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-indigo-500 p-4">01</div>
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-indigo-500 p-4">02</div>
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-indigo-500 p-4">03</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:flex-wrap] -->
<div class="flex flex-wrap">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Wrap reversed

Use `flex-wrap-reverse` to wrap flex items in the reverse direction:

  {
    <div className="grid grid-cols-1">
      
      <div className="col-start-1 row-start-1 flex flex-wrap-reverse gap-4 rounded-lg font-mono text-sm/6 font-bold text-white">
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-fuchsia-500 p-4">01</div>
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-fuchsia-500 p-4">02</div>
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-fuchsia-500 p-4">03</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:flex-wrap-reverse] -->
<div class="flex flex-wrap-reverse">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Responsive design
