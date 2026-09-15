---
title: caret-color
description: Utilities for controlling the color of the text input cursor.
source_url: https://tailwindcss.com/docs/caret-color
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: caret-color.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 430
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `caret-inherit` | `caret-color: inherit;` |
| `caret-current` | `caret-color: currentColor;` |
| `caret-transparent` | `caret-color: transparent;` |
| `caret-<custom-property>` | `caret-color: var(<custom-property>);` |
| `caret-[<value>]` | `caret-color: <value>;` |

## Examples

### Basic example

Use utilities like `caret-rose-500` and `caret-lime-600` to change the color of the text input cursor:

  {
    <div className="flex w-full items-center justify-center">
      <textarea
        className="w-80 rounded-md p-2 text-sm caret-pink-500 ring-1 ring-gray-900/10 focus:ring-2 focus:ring-pink-500 focus:outline-none dark:bg-gray-950/25 dark:ring-1 dark:ring-white/5 dark:focus:bg-gray-950/10 dark:focus:ring-2 dark:focus:ring-pink-500"
        rows="2"
      />
    </div>
  }

```html
<!-- [!code classes:caret-pink-500] -->
<textarea class="caret-pink-500 ..."></textarea>
```

### Using a custom value

### Responsive design

## Customizing your theme
