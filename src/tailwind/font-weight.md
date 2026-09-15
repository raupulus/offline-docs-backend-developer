---
title: font-weight
description: Utilities for controlling the font weight of an element.
source_url: https://tailwindcss.com/docs/font-weight
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: font-weight.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 820
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `font-thin` | `font-weight: 100;` |
| `font-extralight` | `font-weight: 200;` |
| `font-light` | `font-weight: 300;` |
| `font-normal` | `font-weight: 400;` |
| `font-medium` | `font-weight: 500;` |
| `font-semibold` | `font-weight: 600;` |
| `font-bold` | `font-weight: 700;` |
| `font-extrabold` | `font-weight: 800;` |
| `font-black` | `font-weight: 900;` |
| `font-(<custom-property>)` | `font-weight: var(<custom-property>);` |
| `font-[<value>]` | `font-weight: <value>;` |

## Examples

### Basic example

Use utilities like `font-thin` and `font-bold` to set the font weight of an element:

  {
    <div className="flex flex-col gap-8">
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">font-light</span>
        <p className="text-lg font-light text-gray-900 dark:text-gray-200">
          The quick brown fox jumps over the lazy dog.
        </p>
      </div>
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">font-normal</span>
        <p className="text-lg font-normal text-gray-900 dark:text-gray-200">
          The quick brown fox jumps over the lazy dog.
        </p>
      </div>
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">font-medium</span>
        <p className="text-lg font-medium text-gray-900 dark:text-gray-200">
          The quick brown fox jumps over the lazy dog.
        </p>
      </div>
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">font-semibold</span>
        <p className="text-lg font-semibold text-gray-900 dark:text-gray-200">
          The quick brown fox jumps over the lazy dog.
        </p>
      </div>
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">font-bold</span>
        <p className="text-lg font-bold text-gray-900 dark:text-gray-200">
          The quick brown fox jumps over the lazy dog.
        </p>
      </div>
    </div>
  }

```html
<!-- [!code classes:font-light,font-normal,font-medium,font-semibold,font-bold] -->
<p class="font-light ...">The quick brown fox ...</p>
<p class="font-normal ...">The quick brown fox ...</p>
<p class="font-medium ...">The quick brown fox ...</p>
<p class="font-semibold ...">The quick brown fox ...</p>
<p class="font-bold ...">The quick brown fox ...</p>
```

### Using a custom value

### Responsive design

## Customizing your theme
