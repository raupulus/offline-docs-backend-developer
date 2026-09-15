---
title: user-select
description: Utilities for controlling whether the user can select text in an element.
source_url: https://tailwindcss.com/docs/user-select
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: user-select.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1890
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `select-none` | `user-select: none;` |
| `select-text` | `user-select: text;` |
| `select-all` | `user-select: all;` |
| `select-auto` | `user-select: auto;` |

## Examples

### Disabling text selection

Use the `select-none` utility to prevent selecting text in an element and its children:

  {
    <div className="flex justify-center">
      <div className="dark:highlight-white/5 inline-flex rounded-lg bg-white px-4 py-3 text-center font-sans text-sm font-semibold text-gray-900 ring-1 ring-gray-900/5 select-none dark:bg-gray-800 dark:text-gray-200 dark:ring-0">
        The quick brown fox jumps over the lazy dog.
      </div>
    </div>
  }

```html
<!-- [!code classes:select-none] -->
<div class="select-none ...">The quick brown fox jumps over the lazy dog.</div>
```

### Allowing text selection

Use the `select-text` utility to allow selecting text in an element and its children:

  {
    <div className="flex justify-center">
      <div className="dark:highlight-white/5 inline-flex rounded-lg bg-white px-4 py-3 text-center font-sans text-sm font-semibold text-gray-900 ring-1 ring-gray-900/5 select-text dark:bg-gray-800 dark:text-gray-200 dark:ring-0">
        The quick brown fox jumps over the lazy dog.
      </div>
    </div>
  }

```html
<!-- [!code classes:select-text] -->
<div class="select-text ...">The quick brown fox jumps over the lazy dog.</div>
```

### Selecting all text in one click

Use the `select-all` utility to automatically select all the text in an element when a user clicks:

  {
    <div className="flex justify-center">
      <div className="dark:highlight-white/5 inline-flex rounded-lg bg-white px-4 py-3 text-center font-sans text-sm font-semibold text-gray-900 ring-1 ring-gray-900/5 select-all dark:bg-gray-800 dark:text-gray-200 dark:ring-0">
        The quick brown fox jumps over the lazy dog.
      </div>
    </div>
  }

```html
<!-- [!code classes:select-all] -->
<div class="select-all ...">The quick brown fox jumps over the lazy dog.</div>
```

### Using auto select behavior

Use the `select-auto` utility to use the default browser behavior for selecting text:

  {
    <div className="flex justify-center">
      <div className="dark:highlight-white/5 inline-flex rounded-lg bg-white px-4 py-3 text-center font-sans text-sm font-semibold text-gray-900 ring-1 ring-gray-900/5 select-auto dark:bg-gray-800 dark:text-gray-200 dark:ring-0">
        The quick brown fox jumps over the lazy dog.
      </div>
    </div>
  }

```html
<!-- [!code classes:select-auto] -->
<div class="select-auto ...">The quick brown fox jumps over the lazy dog.</div>
```

### Responsive design
