---
title: mask-repeat
source_url: https://tailwindcss.com/docs/mask-repeat
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: mask-repeat.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1140
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `mask-repeat` | `mask-repeat: repeat;` |
| `mask-no-repeat` | `mask-repeat: no-repeat;` |
| `mask-repeat-x` | `mask-repeat: repeat-x;` |
| `mask-repeat-y` | `mask-repeat: repeat-y;` |
| `mask-repeat-space` | `mask-repeat: space;` |
| `mask-repeat-round` | `mask-repeat: round;` |

## Examples

### Basic example

Use the `mask-repeat` utility to repeat the mask image both vertically and horizontally:

  {
    <div className="flex flex-col py-8">
      
        <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-100% mask-radial-closest-side bg-cover bg-center mask-size-[50px_50px] mask-center mask-repeat"></div>
      
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-repeat] -->
<div class="mask-repeat mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

### Repeating horizontally

Use the `mask-repeat-x` utility to only repeat the mask image horizontally:

  {
    <div className="flex flex-col py-8">
      
        <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-100% mask-radial-closest-side bg-cover bg-center mask-size-[50px_50px] mask-center mask-repeat-x"></div>
      
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-repeat-x] -->
<div class="mask-repeat-x mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)]..."></div>
```

### Repeating vertically

Use the `mask-repeat-y` utility to only repeat the mask image vertically:

  {
    <div className="flex flex-col py-8">
      
        <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-100% mask-radial-closest-side bg-cover bg-center mask-size-[50px_50px] mask-center mask-repeat-y"></div>
      
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-repeat-y] -->
<div class="mask-repeat-y mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)]..."></div>
```

### Preventing clipping

Use the `mask-repeat-space` utility to repeat the mask image without clipping:

  {
    <div className="flex flex-col py-8">
      
        <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-100% mask-radial-closest-side bg-cover bg-center mask-size-[50px_50px] mask-repeat-space"></div>
      
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-repeat-space] -->
<div class="mask-repeat-space mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

### Preventing clipping and gaps

Use the `mask-repeat-round` utility to repeat the mask image without clipping, stretching if needed to avoid gaps:

  {
    <div className="flex flex-col py-8">
      
        <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-100% mask-radial-closest-side bg-cover bg-center mask-size-[50px_50px] mask-repeat-round"></div>
      
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-repeat-round] -->
<div class="mask-repeat-round mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

### Disabling repeating

Use the `mask-no-repeat` utility to prevent a mask image from repeating:

  {
    <div className="flex flex-col py-8">
      
        <div className="h-full rounded-lg bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] mask-radial-from-100% mask-radial-closest-side bg-cover bg-center mask-size-[50px_50px] mask-center mask-no-repeat"></div>
      
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-no-repeat] -->
<div class="mask-no-repeat mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

### Responsive design
