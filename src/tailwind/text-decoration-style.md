---
title: text-decoration-style
description: Utilities for controlling the style of text decorations.
source_url: https://tailwindcss.com/docs/text-decoration-style
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: text-decoration-style.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1680
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `decoration-solid` | `text-decoration-style: solid;` |
| `decoration-double` | `text-decoration-style: double;` |
| `decoration-dotted` | `text-decoration-style: dotted;` |
| `decoration-dashed` | `text-decoration-style: dashed;` |
| `decoration-wavy` | `text-decoration-style: wavy;` |

## Examples

### Basic example

Use utilities like `decoration-dotted` and `decoration-dashed` to change the [text decoration](/docs/text-decoration-line) style of an element:

  {
    <div className="flex flex-col gap-8 text-gray-900 dark:text-gray-200">
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">decoration-solid</div>
        <p className="text-lg font-medium underline decoration-solid">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">decoration-double</div>
        <p
          className="text-lg font-medium underline decoration-double"
          children="The quick brown fox jumps over the lazy dog."
        />
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">decoration-dotted</div>
        <p className="text-lg font-medium underline decoration-dotted">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">decoration-dashed</div>
        <p className="text-lg font-medium underline decoration-dashed">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">decoration-wavy</div>
        <p className="text-lg font-medium underline decoration-wavy">The quick brown fox jumps over the lazy dog.</p>
      </div>
    </div>
  }

```html
<!-- [!code classes:decoration-solid,decoration-double,decoration-dotted,decoration-dashed,decoration-wavy] -->
<p class="underline decoration-solid">The quick brown fox...</p>
<p class="underline decoration-double">The quick brown fox...</p>
<p class="underline decoration-dotted">The quick brown fox...</p>
<p class="underline decoration-dashed">The quick brown fox...</p>
<p class="underline decoration-wavy">The quick brown fox...</p>
```

### Responsive design
