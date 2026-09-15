---
title: scrollbar-width
source_url: https://tailwindcss.com/docs/scrollbar-width
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: scrollbar-width.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1580
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `scrollbar-auto` | `scrollbar-width: auto;` |
| `scrollbar-thin` | `scrollbar-width: thin;` |
| `scrollbar-none` | `scrollbar-width: none;` |

## Examples

### Using the default scrollbar width

Use the `scrollbar-auto` utility to use the browser's default scrollbar width:

```html
<!-- [!code classes:scrollbar-auto] -->
<div class="scrollbar-auto overflow-auto ...">
  <!-- ... -->
</div>
```

### Using a thin scrollbar

Use the `scrollbar-thin` utility to use a thinner scrollbar:

  {
    <div className="mx-auto h-72 max-w-sm scrollbar-thin overflow-auto rounded-xl bg-white p-6 text-sm/6 text-gray-600 shadow-lg ring-1 ring-black/5 dark:bg-gray-800 dark:text-gray-300">
      <div className="space-y-4">
        <p>
          The Cerulean Archives occupy three narrow floors above the old observatory, each lined with drawers of star
          maps, expedition notes, and brass instruments cataloged by hand.
        </p>
        <p>
          On winter mornings, the staff rolls ladders between the shelves while pale light cuts through the roof windows
          and settles on the reading tables.
        </p>
        <p>
          Visitors can request anything from the collection, but most come for the atlases that chart coastlines no
          longer found on modern maps.
        </p>
        <p>
          Every returned volume is inspected, dusted, and wrapped before being carried back into the stacks for the next
          researcher.
        </p>
      </div>
    </div>
  }

```html
<!-- [!code classes:scrollbar-thin] -->
<div class="scrollbar-thin overflow-auto ...">
  <!-- ... -->
</div>
```

### Hiding scrollbars

Use the `scrollbar-none` utility to hide scrollbars while still allowing an element to scroll:

```html
<!-- [!code classes:scrollbar-none] -->
<div class="scrollbar-none overflow-auto ...">
  <!-- ... -->
</div>
```

These utilities only support the browser keywords `auto`, `thin`, and `none`.

### Responsive design
