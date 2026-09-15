---
title: field-sizing
description: Utilities for controlling the sizing of form controls.
source_url: https://tailwindcss.com/docs/field-sizing
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: field-sizing.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 560
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `field-sizing-fixed` | `field-sizing: fixed;` |
| `field-sizing-content` | `field-sizing: content;` |

## Examples

### Sizing based on content

Use the `field-sizing-content` utility to allow a form control to adjust its size based on the content:

  {
    <textarea
      rows="2"
      defaultValue="Latex Salesman, Vanderlay Industries"
      className="mx-auto block field-sizing-content rounded-md p-2 text-sm text-gray-950 outline-1 outline-gray-900/10 focus:outline-2 focus:outline-gray-900 dark:bg-gray-950/25 dark:text-white dark:outline-1 dark:outline-white/5 dark:focus:outline-white/20"
    />
  }

```html
<!-- [!code classes:field-sizing-content] -->
<textarea class="field-sizing-content ..." rows="2">
  Latex Salesman, Vanderlay Industries
</textarea>
```

### Using a fixed size

Use the `field-sizing-fixed` utility to make a form control use a fixed size:

  {
    <textarea
      rows="2"
      defaultValue="Latex Salesman, Vanderlay Industries"
      className="mx-auto block field-sizing-fixed w-80 rounded-md p-2 text-sm text-gray-950 outline-1 outline-gray-900/10 focus:outline-2 focus:outline-gray-900 dark:bg-gray-950/25 dark:text-white dark:outline-1 dark:outline-white/5 dark:focus:outline-white/20"
    />
  }

```html
<!-- [!code classes:field-sizing-fixed] -->
<textarea class="field-sizing-fixed w-80 ..." rows="2">
  Latex Salesman, Vanderlay Industries
</textarea>
```

### Responsive design
