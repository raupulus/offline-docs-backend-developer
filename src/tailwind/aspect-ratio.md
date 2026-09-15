---
title: aspect-ratio
description: Utilities for controlling the aspect ratio of an element.
source_url: https://tailwindcss.com/docs/aspect-ratio
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: aspect-ratio.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 80
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `aspect-<ratio>` | `aspect-ratio: <ratio>;` |
| `aspect-square` | `aspect-ratio: 1 / 1;` |
| `aspect-video` | `aspect-ratio: var(--aspect-video); /* 16 / 9 */` |
| `aspect-auto` | `aspect-ratio: auto;` |
| `aspect-(<custom-property>)` | `aspect-ratio: var(<custom-property>);` |
| `aspect-[<value>]` | `aspect-ratio: <value>;` |

## Examples

### Basic example

Use <code>aspect-<var>&lt;ratio&gt;</var></code> utilities like `aspect-3/2` to give an element a specific aspect ratio:

  {
    <img
      className="mx-auto aspect-3/2 w-full max-w-sm rounded-lg object-cover"
      src="https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1200&q=80"
    />
  }

```html
<!-- [!code classes:aspect-3/2] -->
<img class="aspect-3/2 object-cover ..." src="/img/villas.jpg" />
```

### Using a video aspect ratio

Use the `aspect-video` utility to give a video element a 16 / 9 aspect ratio:

  {
    <iframe
      className="aspect-video w-full rounded-lg"
      src="https://www.youtube.com/embed/dQw4w9WgXcQ"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowFullScreen
    ></iframe>
  }

```html
<!-- [!code classes:aspect-video] -->
<iframe class="aspect-video ..." src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

### Using a custom value

### Responsive design

## Customizing your theme
