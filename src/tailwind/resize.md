---
title: resize
description: Utilities for controlling how an element can be resized.
source_url: https://tailwindcss.com/docs/resize
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: resize.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1460
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `resize-none` | `resize: none;` |
| `resize` | `resize: both;` |
| `resize-y` | `resize: vertical;` |
| `resize-x` | `resize: horizontal;` |

## Examples

### Resizing in all directions

Use `resize` to make an element horizontally and vertically resizable:

  {
    <textarea
      rows="2"
      className="mx-auto block w-80 resize rounded-md p-2 text-sm text-gray-950 outline-1 outline-gray-900/10 focus:outline-2 focus:outline-gray-900 dark:bg-gray-950/25 dark:text-white dark:outline-1 dark:outline-white/5 dark:focus:outline-white/20"
    ></textarea>
  }

```html
<!-- [!code classes:resize] -->
<textarea class="resize rounded-md ..."></textarea>
```

### Resizing vertically

Use `resize-y` to make an element vertically resizable:

  {
    <textarea
      rows="2"
      className="mx-auto block w-80 resize-y rounded-md p-2 text-sm text-gray-950 outline-1 outline-gray-900/10 focus:outline-2 focus:outline-gray-900 dark:bg-gray-950/25 dark:text-white dark:outline-1 dark:outline-white/5 dark:focus:outline-white/20"
    ></textarea>
  }

```html
<!-- [!code classes:resize-y] -->
<textarea class="resize-y rounded-md ..."></textarea>
```

### Resizing horizontally

Use `resize-x` to make an element horizontally resizable:

  {
    <textarea
      rows="2"
      className="mx-auto block w-80 resize-x rounded-md p-2 text-sm text-gray-950 outline-1 outline-gray-900/10 focus:outline-2 focus:outline-gray-900 dark:bg-gray-950/25 dark:text-white dark:outline-1 dark:outline-white/5 dark:focus:outline-white/20"
    ></textarea>
  }

```html
<!-- [!code classes:resize-x] -->
<textarea class="resize-x rounded-md ..."></textarea>
```

### Prevent resizing

Use `resize-none` to prevent an element from being resizable:

  {
    <textarea
      rows="2"
      className="mx-auto block w-80 resize-none rounded-md p-2 text-sm text-gray-950 outline-1 outline-gray-900/10 focus:outline-2 focus:outline-gray-900 dark:bg-gray-950/25 dark:text-white dark:outline-1 dark:outline-white/5 dark:focus:outline-white/20"
    ></textarea>
  }

```html
<!-- [!code classes:resize-none] -->
<textarea class="resize-none rounded-md"></textarea>
```

### Responsive design
