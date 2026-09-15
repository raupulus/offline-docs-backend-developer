---
title: will-change
description: Utilities for optimizing upcoming animations of elements that are expected
  to change.
source_url: https://tailwindcss.com/docs/will-change
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: will-change.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1940
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `will-change-auto` | `will-change: auto;` |
| `will-change-scroll` | `will-change: scroll-position;` |
| `will-change-contents` | `will-change: contents;` |
| `will-change-transform` | `will-change: transform;` |
| `will-change-<custom-property>` | `will-change: var(<custom-property>);` |
| `will-change-[<value>]` | `will-change: <value>;` |

## Examples

### Optimizing with will change

Use the `will-change-scroll`, `will-change-contents` and `will-change-transform` utilities to optimize an element that's expected to change in the near future by instructing the browser to prepare the necessary animation before it actually begins:

```html
<!-- [!code classes:will-change-scroll] -->
<div class="overflow-auto will-change-scroll">
  <!-- ... -->
</div>
```

It's recommended that you apply these utilities just before an element changes, and then remove it shortly after it finishes using `will-change-auto`.

The `will-change` property is intended to be used as a last resort when dealing with **known performance problems**. Avoid using these utilities too much, or simply in anticipation of performance issues, as it could actually cause the page to be less performant.

### Using a custom value

<UsingACustomValue
  utility="will-change"
  name={
    <>
      <code>will-change</code> property
    </>
  }
  value="top,left"
  variable="properties"
/>
