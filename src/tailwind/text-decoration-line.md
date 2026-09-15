---
title: text-decoration-line
description: Utilities for controlling the decoration of text.
source_url: https://tailwindcss.com/docs/text-decoration-line
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: text-decoration-line.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1670
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `underline` | `text-decoration-line: underline;` |
| `overline` | `text-decoration-line: overline;` |
| `line-through` | `text-decoration-line: line-through;` |
| `no-underline` | `text-decoration-line: none;` |

## Examples

### Underling text

Use the `underline` utility to add an underline to the text of an element:

  {
    <p className="text-center text-lg font-medium text-gray-900 underline dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:underline] -->
<p class="underline">The quick brown fox...</p>
```

### Adding an overline to text

Use the `overline` utility to add an overline to the text of an element:

  {
    <p className="text-center text-lg font-medium text-gray-900 overline dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:overline] -->
<p class="overline">The quick brown fox...</p>
```

### Adding a line through text

Use the `line-through` utility to add a line through the text of an element:

  {
    <p className="text-center text-lg font-medium text-gray-900 line-through dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:line-through] -->
<p class="line-through">The quick brown fox...</p>
```

### Removing a line from text

Use the `no-underline` utility to remove a line from the text of an element:

  {
    <p className="text-center text-lg font-medium text-gray-900 no-underline dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }

```html
<!-- [!code classes:no-underline] -->
<p class="no-underline">The quick brown fox...</p>
```

### Applying on hover

  {
    <div className="text-center text-lg font-medium text-gray-900 no-underline dark:text-gray-200">
      The{" "}
      <a
        href="https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog"
        target="blank"
        className="text-sky-600 no-underline hover:underline dark:text-sky-400"
      >
        quick brown fox
      </a>{" "}
      jumps over the lazy dog.
    </div>
  }

```html
<!-- [!code classes:hover:underline] -->
<p>The <a href="..." class="no-underline hover:underline ...">quick brown fox</a> jumps over the lazy dog.</p>
```

### Responsive design
