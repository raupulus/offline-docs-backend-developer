---
title: text-decoration-thickness
description: Utilities for controlling the thickness of text decorations.
source_url: https://tailwindcss.com/docs/text-decoration-thickness
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: text-decoration-thickness.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1690
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `decoration-<number>` | `text-decoration-thickness: <number>px;` |
| `decoration-from-font` | `text-decoration-thickness: from-font;` |
| `decoration-auto` | `text-decoration-thickness: auto;` |
| `decoration-(length:<custom-property>)` | `text-decoration-thickness: var(<custom-property>);` |
| `decoration-[<value>]` | `text-decoration-thickness: <value>;` |

## Examples

### Basic example

Use `decoration-<number>` utilities like `decoration-2` and `decoration-4` to change the [text decoration](/docs/text-decoration-line) thickness of an element:

  {
    <div className="flex flex-col gap-8 text-gray-900 dark:text-gray-200">
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">decoration-1</div>
        <p className="text-lg font-medium underline decoration-1">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">decoration-2</div>
        <p className="text-lg font-medium underline decoration-2">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">decoration-4</div>
        <p className="text-lg font-medium underline decoration-4">The quick brown fox jumps over the lazy dog.</p>
      </div>
    </div>
  }

```html
<!-- [!code classes:decoration-1] -->
<p class="underline decoration-1">The quick brown fox...</p>
<!-- [!code classes:decoration-2] -->
<p class="underline decoration-2">The quick brown fox...</p>
<!-- [!code classes:decoration-4] -->
<p class="underline decoration-4">The quick brown fox...</p>
```

### Using a custom value

### Responsive design
