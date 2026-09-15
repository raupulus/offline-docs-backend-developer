---
title: object-fit
source_url: https://tailwindcss.com/docs/object-fit
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: object-fit.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1260
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `object-contain` | `object-fit: contain;` |
| `object-cover` | `object-fit: cover;` |
| `object-fill` | `object-fit: fill;` |
| `object-none` | `object-fit: none;` |
| `object-scale-down` | `object-fit: scale-down;` |

## Examples

### Resizing to cover

Use the `object-cover` utility to resize an element's content to cover its container:

  {
    <img
      className="mx-auto h-48 w-96 rounded-lg object-cover"
      src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
    />
  }

```html
<!-- [!code classes:object-cover] -->
<img class="h-48 w-96 object-cover ..." src="/img/mountains.jpg" />
```

### Containing within

Use the `object-contain` utility to resize an element's content to stay contained within its container:

  {
    <div className="relative mx-auto w-96">
      
      <img
        className="relative h-48 w-full object-contain"
        src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
      />
    </div>
  }

```html
<!-- [!code classes:object-contain] -->
<img class="h-48 w-96 object-contain ..." src="/img/mountains.jpg" />
```

### Stretching to fit

Use the `object-fill` utility to stretch an element's content to fit its container:

  {
    <img
      className="mx-auto h-48 w-96 rounded-lg object-fill"
      src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
    />
  }

```html
<!-- [!code classes:object-fill] -->
<img class="h-48 w-96 object-fill ..." src="/img/mountains.jpg" />
```

### Scaling down

Use the `object-scale-down` utility to display an element's content at its original size but scale it down to fit its container if necessary:

  {
    <div className="relative mx-auto w-96 rounded-lg">
      
      <img
        className="relative h-48 w-full object-scale-down"
        src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=128&h=160&q=80"
      />
    </div>
  }

```html
<!-- [!code classes:object-scale-down] -->
<img class="h-48 w-96 object-scale-down ..." src="/img/mountains.jpg" />
```

### Using the original size

Use the `object-none` utility to display an element's content at its original size ignoring the container size:

  {
    <img
      className="mx-auto h-48 w-96 rounded-lg object-none"
      src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
    />
  }

```html
<!-- [!code classes:object-none] -->
<img class="h-48 w-96 object-none ..." src="/img/mountains.jpg" />
```

### Responsive design

```html
<!-- [!code classes:md:object-cover] -->
<img class="object-contain md:object-cover" src="/img/mountains.jpg" />
```
