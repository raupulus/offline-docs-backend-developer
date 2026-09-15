---
title: text-indent
description: Utilities for controlling the amount of empty space shown before text
  in a block.
source_url: https://tailwindcss.com/docs/text-indent
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: text-indent.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1700
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `indent-<number>` | `text-indent: calc(var(--spacing) * <number>);` |
| `-indent-<number>` | `text-indent: calc(var(--spacing) * -<number>);` |
| `indent-px` | `text-indent: 1px;` |
| `-indent-px` | `text-indent: -1px;` |
| `indent-(<custom-property>)` | `text-indent: var(<custom-property>);` |
| `indent-[<value>]` | `text-indent: <value>;` |

## Examples

### Basic example

Use `indent-<number>` utilities like `indent-2` and `indent-8` to set the amount of empty space (indentation) that's shown before text in a block:

  {
    <p className="mx-auto max-w-sm indent-8 text-gray-900 dark:text-gray-200">
      So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my
      way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of
      all living things but I tell you Jerry at that moment, I <em>was</em> a marine biologist.
    </p>
  }

```html
<!-- [!code classes:indent-8] -->
<p class="indent-8">So I started to walk into the water...</p>
```

### Using negative values

To use a negative text indent value, prefix the class name with a dash to convert it to a negative value:

  {
    <p className="mx-auto max-w-sm -indent-8 text-gray-900 dark:text-gray-200">
      So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my
      way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of
      all living things but I tell you Jerry at that moment, I <em>was</em> a marine biologist.
    </p>
  }

```html
<!-- [!code classes:-indent-8] -->
<p class="-indent-8">So I started to walk into the water...</p>
```

### Using a custom value

### Responsive design
