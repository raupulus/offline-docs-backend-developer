---
title: list-style-position
description: Utilities for controlling the position of bullets and numbers in lists.
source_url: https://tailwindcss.com/docs/list-style-position
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: list-style-position.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1050
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `list-inside` | `list-style-position: inside;` |
| `list-outside` | `list-style-position: outside;` |

## Examples

### Basic example

Use utilities like `list-inside` and `list-outside` to control the position of the markers and text indentation in a list:

  {
    <div className="flex flex-col gap-8 sm:flex-row">
      <div className="relative">
        <div className="absolute -top-8 -bottom-8 left-8 w-px bg-pink-400/40 dark:bg-pink-400/30"></div>
        <p className="mb-3 ml-8 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">list-inside</p>
        <ul className="list-inside list-disc rounded-xl p-4 pl-8 text-gray-900 dark:text-gray-200">
          <li>5 cups chopped Porcini mushrooms</li>
          <li>1/2 cup of olive oil</li>
          <li>3lb of celery</li>
        </ul>
      </div>
      <div className="relative">
        <div className="absolute top-0 -bottom-8 left-8 w-px bg-pink-400/40 sm:-top-8 dark:bg-pink-400/30"></div>
        <p className="mb-3 ml-8 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">list-outside</p>
        <ul className="list-outside list-disc rounded-xl p-4 pl-8 text-gray-900 dark:text-gray-200">
          <li>5 cups chopped Porcini mushrooms</li>
          <li>1/2 cup of olive oil</li>
          <li>3lb of celery</li>
        </ul>
      </div>
    </div>
  }

```html
<!-- [!code classes:list-inside] -->
<ul class="list-inside">
  <li>5 cups chopped Porcini mushrooms</li>
  <!-- ... -->
</ul>

<!-- [!code classes:list-outside] -->
<ul class="list-outside">
  <li>5 cups chopped Porcini mushrooms</li>
  <!-- ... -->
</ul>
```

### Responsive design
