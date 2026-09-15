---
title: text-underline-offset
description: Utilities for controlling the offset of a text underline.
source_url: https://tailwindcss.com/docs/text-underline-offset
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: text-underline-offset.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1740
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `underline-offset-<number>` | `text-underline-offset: <number>px;` |
| `-underline-offset-<number>` | `text-underline-offset: calc(<number>px * -1);` |
| `underline-offset-auto` | `text-underline-offset: auto;` |
| `underline-offset-(<custom-property>)` | `text-underline-offset: var(<custom-property>);` |
| `underline-offset-[<value>]` | `text-underline-offset: <value>;` |

## Examples

### Basic example

Use `underline-offset-<number>` utilities like `underline-offset-2` and `underline-offset-4` to change the offset of a text underline:

  {
    <div className="flex flex-col gap-8 text-gray-900 dark:text-gray-200">
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">underline-offset-1</div>
        <p className="text-lg font-medium underline underline-offset-1">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">underline-offset-2</div>
        <p className="text-lg font-medium underline underline-offset-2">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">underline-offset-4</div>
        <p className="text-lg font-medium underline underline-offset-4">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">underline-offset-8</div>
        <p className="text-lg font-medium underline underline-offset-8">The quick brown fox jumps over the lazy dog.</p>
      </div>
    </div>
  }

```html
<!-- [!code classes:underline-offset-1] -->
<p class="underline underline-offset-1">The quick brown fox...</p>
<!-- [!code classes:underline-offset-2] -->
<p class="underline underline-offset-2">The quick brown fox...</p>
<!-- [!code classes:underline-offset-4] -->
<p class="underline underline-offset-4">The quick brown fox...</p>
<!-- [!code classes:underline-offset-8] -->
<p class="underline underline-offset-8">The quick brown fox...</p>
```

### Using a custom value

### Responsive design
