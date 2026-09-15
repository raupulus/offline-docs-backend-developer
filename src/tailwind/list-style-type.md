---
title: list-style-type
description: Utilities for controlling the marker style of a list.
source_url: https://tailwindcss.com/docs/list-style-type
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: list-style-type.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1060
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `list-disc` | `list-style-type: disc;` |
| `list-decimal` | `list-style-type: decimal;` |
| `list-none` | `list-style-type: none;` |
| `list-(<custom-property>)` | `list-style-type: var(<custom-property>);` |
| `list-[<value>]` | `list-style-type: <value>;` |

## Examples

### Basic example

Use utilities like `list-disc` and `list-decimal` to control the style of the markers in a list:

  {
    <div className="flex flex-col gap-8">
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">list-disc</span>
        <ul className="list-inside list-disc text-gray-900 dark:text-gray-200">
          <li>Now this is a story all about how, my life got flipped-turned upside down</li>
          <li>And I'd like to take a minute just sit right there</li>
          <li>I'll tell you how I became the prince of a town called Bel-Air</li>
        </ul>
      </div>
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">list-decimal</span>
        <ul className="list-inside list-decimal text-gray-900 dark:text-gray-200">
          <li>Now this is a story all about how, my life got flipped-turned upside down</li>
          <li>And I'd like to take a minute just sit right there</li>
          <li>I'll tell you how I became the prince of a town called Bel-Air</li>
        </ul>
      </div>
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">list-none</span>
        <ul className="list-inside list-none text-gray-900 dark:text-gray-200">
          <li>Now this is a story all about how, my life got flipped-turned upside down</li>
          <li>And I'd like to take a minute just sit right there</li>
          <li>I'll tell you how I became the prince of a town called Bel-Air</li>
        </ul>
      </div>
    </div>
  }

```html
<!-- [!code classes:list-disc] -->
<ul class="list-disc">
  <li>Now this is a story all about how, my life got flipped-turned upside down</li>
  <!-- ... -->
</ul>

<!-- [!code classes:list-decimal] -->
<ol class="list-decimal">
  <li>Now this is a story all about how, my life got flipped-turned upside down</li>
  <!-- ... -->
</ol>

<!-- [!code classes:list-none] -->
<ul class="list-none">
  <li>Now this is a story all about how, my life got flipped-turned upside down</li>
  <!-- ... -->
</ul>
```

### Using a custom value

### Responsive design
