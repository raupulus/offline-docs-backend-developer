---
title: mask-position
source_url: https://tailwindcss.com/docs/mask-position
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: mask-position.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1130
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `mask-top-left` | `mask-position: top left;` |
| `mask-top` | `mask-position: top;` |
| `mask-top-right` | `mask-position: top right;` |
| `mask-left` | `mask-position: left;` |
| `mask-center` | `mask-position: center;` |
| `mask-right` | `mask-position: right;` |
| `mask-bottom-left` | `mask-position: bottom left;` |
| `mask-bottom` | `mask-position: bottom;` |
| `mask-bottom-right` | `mask-position: bottom right;` |
| `mask-position-(<custom-property>)` | `mask-position: var(<custom-property>);` |
| `mask-position-[<value>]` | `mask-position: <value>;` |

## Examples

### Basic example

Use utilities like `mask-center`, `mask-right`, and `mask-left-top` to control the position of an element's mask image:

  {
    <div className="grid grid-cols-3 gap-y-8 p-8 text-center font-mono text-xs font-medium text-gray-500 max-sm:items-end max-sm:justify-between max-sm:px-2 dark:text-gray-400">
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-top-left</p>
        
          <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-70% mask-radial-to-70% bg-cover bg-center mask-size-[50%_66%] mask-top-left mask-no-repeat"></div>
        
      </div>
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-top</p>
        
          <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-70% mask-radial-to-70% bg-cover bg-center mask-size-[50%_66%] mask-top mask-no-repeat"></div>
        
      </div>
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-top-right</p>
        
          <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-70% mask-radial-to-70% bg-cover bg-center mask-size-[50%_66%] mask-top-right mask-no-repeat"></div>
        
      </div>
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-left</p>
        
          <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-70% mask-radial-to-70% bg-cover bg-center mask-size-[50%_66%] mask-left mask-no-repeat"></div>
        
      </div>
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-center</p>
        
          <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-70% mask-radial-to-70% bg-cover bg-center mask-size-[50%_66%] mask-center mask-no-repeat"></div>
        
      </div>
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-right</p>
        
          <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-70% mask-radial-to-70% bg-cover bg-center mask-size-[50%_66%] mask-right mask-no-repeat"></div>
        
      </div>
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-bottom-left</p>
        
          <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-70% mask-radial-to-70% bg-cover bg-center mask-size-[50%_66%] mask-bottom-left mask-no-repeat"></div>
        
      </div>
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-bottom</p>
        
          <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-70% mask-radial-to-70% bg-cover bg-center mask-size-[50%_66%] mask-bottom mask-no-repeat"></div>
        
      </div>
      <div className="flex flex-col items-center">
        <p className="mb-3">mask-bottom-right</p>
        
          <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-70% mask-radial-to-70% bg-cover bg-center mask-size-[50%_66%] mask-bottom-right mask-no-repeat"></div>
        
      </div>
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-top-left,mask-top,mask-top-right,mask-left,mask-center,mask-right,mask-bottom-left,mask-bottom,mask-bottom-right] -->
<div class="mask-top-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-top mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-top-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-center mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-bottom-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-bottom mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-bottom-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
```

### Using a custom value

### Responsive design
