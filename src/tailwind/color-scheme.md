---
title: color-scheme
description: Utilities for controlling the color scheme of an element.
source_url: https://tailwindcss.com/docs/color-scheme
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: color-scheme.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 450
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `scheme-normal` | `color-scheme: normal;` |
| `scheme-dark` | `color-scheme: dark;` |
| `scheme-light` | `color-scheme: light;` |
| `scheme-light-dark` | `color-scheme: light dark;` |
| `scheme-only-dark` | `color-scheme: only dark;` |
| `scheme-only-light` | `color-scheme: only light;` |

## Examples

### Basic example

Use utilities like `scheme-light` and `scheme-light-dark` to control how element should be rendered:

  {
    <div className="flex justify-between gap-8 text-sm max-sm:flex-col">
      <div className="flex grow flex-col items-center gap-3 text-center scheme-light">
        <p className="font-mono font-medium text-gray-500 dark:text-gray-400">scheme-light</p>
        <input
          type="date"
          className="w-full rounded-lg border border-gray-950/10 bg-[Field] px-3 py-2 text-[FieldText] dark:border-white/10"
        />
      </div>
      <div className="flex grow flex-col items-center gap-3 text-center scheme-dark">
        <p className="font-mono font-medium text-gray-500 dark:text-gray-400">scheme-dark</p>
        <input
          type="date"
          className="w-full rounded-lg border border-gray-950/10 bg-[Field] px-3 py-2 text-[FieldText] dark:border-white/10"
        />
      </div>
      <div className="flex grow flex-col items-center gap-3 text-center scheme-light-dark">
        <p className="font-medium text-gray-500 dark:text-gray-400">scheme-light-dark</p>
        <input
          type="date"
          className="w-full rounded-lg border border-gray-950/10 bg-[Field] px-3 py-2 text-[FieldText] dark:border-white/10"
        />
      </div>
    </div>
  }

```html
<!-- [!code classes:scheme-light-dark,scheme-light,scheme-dark] -->
<div class="scheme-light ...">
  <input type="date" />
</div>

<div class="scheme-dark ...">
  <input type="date" />
</div>

<div class="scheme-light-dark ...">
  <input type="date" />
</div>
```

### Applying in dark mode
