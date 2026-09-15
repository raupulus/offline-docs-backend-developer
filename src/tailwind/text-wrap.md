---
title: text-wrap
description: Utilities for controlling how text wraps within an element.
source_url: https://tailwindcss.com/docs/text-wrap
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: text-wrap.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1750
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `text-wrap` | `text-wrap: wrap;` |
| `text-nowrap` | `text-wrap: nowrap;` |
| `text-balance` | `text-wrap: balance;` |
| `text-pretty` | `text-wrap: pretty;` |

## Examples

### Allowing text to wrap

Use the `text-wrap` utility to wrap overflowing text onto multiple lines at logical points in the text:

  {
    <div className="mx-auto grid max-w-xs gap-4 border-x border-x-pink-400/30 py-8 text-gray-700 dark:text-gray-400">
      <div className="text-xl font-semibold text-gray-900 dark:text-white">Beloved Manhattan soup stand closes</div>
      <p className="text-sm/6">
        New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand
        unexpectedly shutters, following a series of events that have left the community puzzled.
      </p>
    </div>
  }

```html
<!-- [!code classes:text-wrap] -->
<article class="text-wrap">
  <h3>Beloved Manhattan soup stand closes</h3>
  <p>New Yorkers are facing the winter chill...</p>
</article>
```

### Preventing text from wrapping

Use the `text-nowrap` utility to prevent text from wrapping, allowing it to overflow if necessary:

  {
    <div className="overflow-hidden">
      <div className="mx-auto grid max-w-xs gap-4 border-x border-x-pink-400/30 py-8 text-gray-700 dark:text-gray-400">
        <div className="text-xl font-semibold text-nowrap text-gray-900 dark:text-white">
          Beloved Manhattan soup stand closes
        </div>
        <p className="text-sm/6 text-nowrap">
          New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand
          unexpectedly shutters, following a series of events that have left the community puzzled.
        </p>
      </div>
    </div>
  }

```html
<!-- [!code classes:text-nowrap] -->
<article class="text-nowrap">
  <h3>Beloved Manhattan soup stand closes</h3>
  <p>New Yorkers are facing the winter chill...</p>
</article>
```

### Balanced text wrapping

Use the `text-balance` utility to distribute the text evenly across each line:

  {
    <div className="mx-auto grid max-w-xs gap-4 border-x border-x-pink-400/30 py-8 text-gray-700 dark:text-gray-400">
      <div className="text-xl font-semibold text-balance text-gray-900 dark:text-white">
        Beloved Manhattan soup stand closes
      </div>
      <p className="text-sm/6">
        New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand
        unexpectedly shutters, following a series of events that have left the community puzzled.
      </p>
    </div>
  }

```html
<!-- [!code classes:text-balance] -->
<article>
  <h3 class="text-balance">Beloved Manhattan soup stand closes</h3>
  <p>New Yorkers are facing the winter chill...</p>
</article>
```

For performance reasons browsers limit text balancing to blocks that are ~6 lines or less, making it best suited for headings.

### Pretty text wrapping

Use the `text-pretty` utility to prefer better text wrapping and layout at the expense of speed. Behavior varies across browsers but often involves approaches like preventing orphans (a single word on its own line) at the end of a text block:

  {
    <div className="mx-auto grid max-w-xs gap-4 border-x border-x-pink-400/30 py-8 text-gray-700 dark:text-gray-400">
      <div className="text-xl font-semibold text-pretty text-gray-900 dark:text-white">
        Beloved Manhattan soup stand closes
      </div>
      <p className="text-sm/6">
        New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand
        unexpectedly shutters, following a series of events that have left the community puzzled.
      </p>
    </div>
  }

```html
<!-- [!code classes:text-pretty] -->
<article>
  <h3 class="text-pretty">Beloved Manhattan soup stand closes</h3>
  <p>New Yorkers are facing the winter chill...</p>
</article>
```

### Responsive design
