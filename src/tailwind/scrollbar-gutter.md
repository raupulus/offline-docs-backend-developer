---
title: scrollbar-gutter
source_url: https://tailwindcss.com/docs/scrollbar-gutter
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: scrollbar-gutter.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1570
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `scrollbar-gutter-auto` | `scrollbar-gutter: auto;` |
| `scrollbar-gutter-stable` | `scrollbar-gutter: stable;` |
| `scrollbar-gutter-both` | `scrollbar-gutter: stable both-edges;` |

## Examples

### Reserving space for the scrollbar

Use the `scrollbar-gutter-stable` utility to reserve space for the scrollbar even when an element isn't overflowing:

  {
    <div className="mx-auto grid max-w-xl grid-cols-1 gap-6 text-sm/6 text-gray-600 sm:grid-cols-2 dark:text-gray-300">
      <div>
        <p className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scrollbar-gutter-auto</p>
        <div className="h-40 scrollbar-gutter-auto overflow-auto rounded-lg bg-gray-50 py-4 dark:bg-white/5">
          <p className="text-justify">
            Hey everyone! It’s almost 2027 and we still don’t know if there are aliens living among us, or do we? Maybe
            the person writing this is an alien. You will never know.
          </p>
        </div>
      </div>
      <div>
        <p className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scrollbar-gutter-stable</p>
        <div className="relative h-40 scrollbar-gutter-stable rounded-lg bg-gray-50 py-4 pr-4 dark:bg-white/5">
          <p className="text-justify">
            Hey everyone! It’s almost 2027 and we still don’t know if there are aliens living among us, or do we? Maybe
            the person writing this is an alien. You will never know.
          </p>
          <div className="absolute top-0 right-0 bottom-0 w-4 rounded-r-lg border bg-[repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,transparent_0,transparent_50%)] bg-size-[8px_8px] bg-top-left text-black/10 dark:text-white/12.5"></div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:scrollbar-gutter-stable] -->
<div class="scrollbar-gutter-stable overflow-auto ...">
  <!-- ... -->
</div>
```

### Reserving space on both sides

Use the `scrollbar-gutter-both` utility to reserve matching gutter space on both sides of the element:

```html
<!-- [!code classes:scrollbar-gutter-both] -->
<div class="scrollbar-gutter-both overflow-auto ...">
  <!-- ... -->
</div>
```

### Using the default gutter

Use the `scrollbar-gutter-auto` utility to only reserve gutter space when the browser would normally show a scrollbar:

```html
<!-- [!code classes:scrollbar-gutter-auto] -->
<div class="scrollbar-gutter-auto overflow-auto ...">
  <!-- ... -->
</div>
```

### Responsive design
