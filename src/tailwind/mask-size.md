---
title: mask-size
source_url: https://tailwindcss.com/docs/mask-size
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: mask-size.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1150
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `mask-auto` | `mask-size: auto;` |
| `mask-cover` | `mask-size: cover;` |
| `mask-contain` | `mask-size: contain;` |
| `mask-size-(<custom-property>)` | `mask-size: var(<custom-property>);` |
| `mask-size-[<value>]` | `mask-size: <value>;` |

## Examples

### Filling the container

Use the `mask-cover` utility to scale the mask image until it fills the mask layer, cropping the image if needed:

  {
    
      <div
        className="h-full w-full bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] bg-cover bg-center bg-no-repeat mask-cover mask-center"
        style={{ maskImage: `url(${maskImg.src})` }}
      ></div>
    
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-cover] -->
<div class="mask-cover mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

### Filling without cropping

Use the `mask-contain` utility to scale the mask image to the outer edges without cropping or stretching:

  {
    
      <div
        className="h-full w-full bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] bg-cover bg-center bg-no-repeat mask-contain mask-center mask-no-repeat"
        style={{ maskImage: `url(${maskImg.src})` }}
      ></div>
    
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-contain] -->
<div class="mask-contain mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

### Using the default size

Use the `mask-auto` utility to display the mask image at its default size:

  {
    
      <div
        className="h-full w-full bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=80)] bg-cover bg-center bg-no-repeat mask-auto mask-center mask-no-repeat"
        style={{ maskImage: `url(${maskImg.src})` }}
      ></div>
    
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:mask-auto] -->
<div class="mask-auto mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

### Using a custom value

### Responsive design
