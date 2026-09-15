---
title: mask-clip
source_url: https://tailwindcss.com/docs/mask-clip
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: mask-clip.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1080
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `mask-clip-border` | `mask-clip: border-box;` |
| `mask-clip-padding` | `mask-clip: padding-box;` |
| `mask-clip-content` | `mask-clip: content-box;` |
| `mask-clip-fill` | `mask-clip: fill-box;` |
| `mask-clip-stroke` | `mask-clip: stroke-box;` |
| `mask-clip-view` | `mask-clip: view-box;` |
| `mask-no-clip` | `mask-clip: no-clip;` |

## Examples

### Basic example

Use utilities like `mask-clip-border`, `mask-clip-padding`, and `mask-clip-content` to control the bounding box of an element's mask:

  {
    <div className="flex flex-col items-center justify-center gap-y-10 text-center font-mono text-xs font-medium text-gray-500 sm:flex-row sm:space-y-0 sm:space-x-10 dark:text-gray-400">
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-clip-border</p>
        <div className="relative size-24 rounded-lg border-3 border-dashed border-indigo-500/50 dark:border-indigo-400/75">
          <div className="absolute inset-[-3px] bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-[50%_50%] mask-radial-from-100% bg-cover bg-center mask-clip-border p-1.5"></div>
        </div>
      </div>
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-clip-padding</p>
        <div className="relative size-24 rounded-lg border-3 border-dashed border-indigo-500/50 dark:border-indigo-400/75">
          <div className="absolute inset-[-3px] rounded-lg border-3 bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-[50%_50%] mask-radial-from-100% bg-cover bg-center mask-clip-padding p-1.5"></div>
        </div>
      </div>
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-clip-content</p>
        <div className="relative size-24 rounded-lg border-3 border-dashed border-indigo-500/50 dark:border-indigo-400/75">
          <div className="absolute inset-[-3px] rounded-lg border-3 bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-[50%_50%] mask-radial-from-100% bg-cover bg-center mask-clip-content p-1.5"></div>
        </div>
      </div>
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-clip-border,mask-clip-padding,mask-clip-content] -->
<div class="mask-clip-border border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-clip-padding border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-clip-content border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

### Responsive design
