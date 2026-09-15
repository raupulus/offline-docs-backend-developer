---
title: isolation
description: Utilities for controlling whether an element should explicitly create
  a new stacking context.
source_url: https://tailwindcss.com/docs/isolation
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: isolation.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 970
---

"Utilities for controlling whether an element should explicitly create a new stacking context.";

| Clase | Propiedades CSS |
| :--- | :--- |
| `isolate` | `isolation: isolate;` |
| `isolation-auto` | `isolation: auto;` |

## Examples

### Basic example

Use the `isolate` and `isolation-auto` utilities to control whether an element should explicitly create a new stacking context:

```html
<!-- [!code classes:isolate] -->
<div class="isolate ...">
  <!-- ... -->
</div>
```

### Responsive design
