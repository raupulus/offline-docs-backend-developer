---
title: scroll-behavior
description: Utilities for controlling the scroll behavior of an element.
source_url: https://tailwindcss.com/docs/scroll-behavior
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: scroll-behavior.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1500
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `scroll-auto` | `scroll-behavior: auto;` |
| `scroll-smooth` | `scroll-behavior: smooth;` |

## Examples

### Using smooth scrolling

Use the `scroll-smooth` utility to enable smooth scrolling within an element:

```html
<!-- [!code classes:scroll-smooth] -->
<html class="scroll-smooth">
  <!-- ... -->
</html>
```

Setting the `scroll-behavior` only affects scroll events that are triggered by the browser.

### Using normal scrolling

Use the `scroll-auto` utility to revert to the default browser behavior for scrolling:

```html
<!-- [!code classes:scroll-auto] -->
<html class="scroll-smooth md:scroll-auto">
  <!-- ... -->
</html>
```
