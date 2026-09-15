---
title: background-size
source_url: https://tailwindcss.com/docs/background-size
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: background-size.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 280
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `bg-auto` | `background-size: auto;` |
| `bg-cover` | `background-size: cover;` |
| `bg-contain` | `background-size: contain;` |
| `bg-size-(<custom-property>)` | `background-size: var(<custom-property>);` |
| `bg-size-[<value>]` | `background-size: <value>;` |

## Examples

### Filling the container

Use the `bg-cover` utility to scale the background image until it fills the background layer, cropping the image if needed:

  {
    <div className="relative mx-auto flex w-56 items-center justify-center overflow-hidden rounded-lg sm:w-96">
      <div className="absolute inset-0">
        
      </div>
      <div className="relative z-10 h-48 w-full bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=512&h=640&q=80)] bg-cover bg-center bg-no-repeat"></div>
    </div>
  }

```html
<!-- [!code classes:bg-cover] -->
<div class="bg-[url(/img/mountains.jpg)] bg-cover bg-center"></div>
```

### Filling without cropping

Use the `bg-contain` utility to scale the background image to the outer edges without cropping or stretching:

  {
    <div className="relative mx-auto flex w-56 items-center justify-center overflow-hidden rounded-lg sm:w-96">
      <div className="absolute inset-0">
        
      </div>
      <div className="relative z-10 h-48 w-full bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=512&h=640&q=80)] bg-contain bg-center bg-no-repeat sm:bg-top"></div>
    </div>
  }

```html
<!-- [!code classes:bg-contain] -->
<div class="bg-[url(/img/mountains.jpg)] bg-contain bg-center"></div>
```

### Using the default size

Use the `bg-auto` utility to display the background image at its default size:

  {
    <div className="relative mx-auto flex h-48 w-56 items-center justify-center overflow-hidden rounded-lg sm:w-96">
      <div className="absolute inset-0">
        
      </div>
      <div className="relative z-10 h-full w-full bg-[url(https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=128&h=160&q=80)] bg-auto bg-center bg-no-repeat"></div>
    </div>
  }

```html
<!-- [!code classes:bg-auto] -->
<div class="bg-[url(/img/mountains.jpg)] bg-auto bg-center bg-no-repeat"></div>
```

### Using a custom value

### Responsive design
