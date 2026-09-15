---
title: box-decoration-break
description: Utilities for controlling how element fragments should be rendered across
  multiple lines, columns, or pages.
source_url: https://tailwindcss.com/docs/box-decoration-break
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: box-decoration-break.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 360
---

"Utilities for controlling how element fragments should be rendered across multiple lines, columns, or pages.";

| Clase | Propiedades CSS |
| :--- | :--- |
| `box-decoration-clone` | `box-decoration-break: clone;` |
| `box-decoration-slice` | `box-decoration-break: slice;` |

## Examples

### Basic example

Use the `box-decoration-slice` and `box-decoration-clone` utilities to control whether properties like background, border, border-image, box-shadow, clip-path, margin, and padding should be rendered as if the element were one continuous fragment, or distinct blocks:

  {
    <div className="grid grid-cols-1 gap-10 px-10 font-mono font-bold sm:grid-cols-2">
      <div className="flex flex-col">
        <p className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">box-decoration-slice</p>
        <div className="font-sans text-5xl leading-none font-extrabold tracking-tight">
          <span className="bg-linear-to-r from-indigo-600 to-pink-500 box-decoration-slice px-2 leading-14 text-white">
            Hello
            <br />
            World
          </span>
        </div>
      </div>
      <div className="flex flex-col">
        <p className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">box-decoration-clone</p>
        <div className="font-sans text-5xl leading-none font-extrabold tracking-tight">
          <span className="bg-linear-to-r from-indigo-600 to-pink-500 box-decoration-clone px-2 leading-14 text-white">
            Hello
            <br />
            World
          </span>
        </div>
      </div>
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:box-decoration-slice,box-decoration-clone] -->
<span class="box-decoration-slice bg-linear-to-r from-indigo-600 to-pink-500 px-2 text-white ...">
  Hello<br />World
</span>
<span class="box-decoration-clone bg-linear-to-r from-indigo-600 to-pink-500 px-2 text-white ...">
  Hello<br />World
</span>
```

### Responsive design
