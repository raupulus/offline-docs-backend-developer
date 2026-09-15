---
title: box-sizing
source_url: https://tailwindcss.com/docs/box-sizing
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: box-sizing.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 380
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `box-border` | `box-sizing: border-box;` |
| `box-content` | `box-sizing: content-box;` |

## Examples

### Including borders and padding

Use the `box-border` utility to set an element's `box-sizing` to `border-box`, telling the browser to include the element's borders and padding when you give it a height or width.

This means a 100px &times; 100px element with a 2px border and 4px of padding on all sides will be rendered as 100px &times; 100px, with an internal content area of 88px &times; 88px:

  {
    <div className="relative grid w-full grid-cols-[1fr_8rem_1fr] grid-rows-[1fr_3fr_1fr] gap-px bg-gray-700/10 font-mono text-sm leading-6 font-bold dark:bg-gray-700">
      <div className="col-start-1 row-start-1 bg-white dark:bg-gray-900"></div>
      <div className="relative col-start-2 row-start-1 bg-white dark:bg-gray-900">
        {/* w-measure indicator */}
        <div className="absolute right-0 bottom-2 left-0 flex">
          {/* Horizontal line */}
          <div className="absolute top-1/2 right-0 left-0 h-px -translate-y-px bg-sky-400"></div>
          {/* Left chip */}
          <div className="w-full">
            <div className="absolute top-1/2 left-0 h-2 w-px -translate-x-px -translate-y-1 rounded-full bg-sky-400"></div>
          </div>
          {/* Badge */}
          <div className="relative flex w-full flex-auto items-center justify-center bg-white px-1.5 font-mono text-xs leading-none font-bold text-sky-600 dark:bg-gray-900 dark:text-sky-400">
            128px
          </div>
          {/* Right chip */}
          <div className="w-full">
            <div className="absolute top-1/2 right-0 h-2 w-px translate-x-px -translate-y-1 rounded-full bg-sky-400"></div>
          </div>
        </div>
      </div>
      <div className="col-start-3 row-start-1 bg-white dark:bg-gray-900"></div>
      <div className="relative col-start-1 row-start-2 bg-white dark:bg-gray-900">
        {/* h-measure indicator */}
        <div className="absolute top-0 right-2 bottom-0 flex w-3">
          {/* Vertical line */}
          <div className="absolute top-0 bottom-0 left-1/2 w-px translate-x-[-0.5px] bg-sky-400"></div>
          {/* Top chip */}
          <div className="w-full">
            <div className="absolute top-0 left-1/2 h-px w-2 -translate-x-1 -translate-y-px rounded-full bg-sky-400"></div>
          </div>
          {/* Badge */}
          <div className="relative flex h-3 flex-auto translate-x-[-1.15rem] translate-y-14 -rotate-90 items-center justify-center bg-white px-1.5 font-mono text-xs leading-none font-bold text-sky-600 dark:bg-gray-900 dark:text-sky-400">
            128px
          </div>
          {/* Bottom chip */}
          <div className="w-full">
            <div className="absolute bottom-0 left-1/2 h-px w-2 -translate-x-1 translate-y-px rounded-full bg-sky-400"></div>
          </div>
        </div>
      </div>
      <div className="col-start-2 row-start-2 size-32 bg-white ring-1 ring-sky-300 dark:bg-gray-900 dark:ring-sky-400">
        <div className="relative box-border size-32 p-5 ring ring-sky-300 ring-inset">
          <div className="relative z-1 h-full w-full bg-sky-500 ring-1 ring-sky-500"></div>
          <div className="absolute inset-0">
            
          </div>
        </div>
      </div>
      <div className="col-start-3 row-start-2 bg-white dark:bg-gray-900"></div>
      <div className="col-start-1 row-start-3 bg-white dark:bg-gray-900"></div>
      <div className="col-start-2 row-start-3 bg-white dark:bg-gray-900"></div>
      <div className="col-start-3 row-start-3 bg-white dark:bg-gray-900"></div>
    </div>
  }

```html
<!-- [!code classes:box-border] -->
<div class="box-border size-32 border-4 p-4 ...">
  <!-- ... -->
</div>
```

Tailwind makes this the default for all elements in our [preflight base styles](/docs/preflight).

### Excluding borders and padding

Use the `box-content` utility to set an element's `box-sizing` to `content-box`, telling the browser to add borders and padding on top of the element's specified width or height.

This means a 100px &times; 100px element with a 2px border and 4px of padding on all sides will actually be rendered as 112px &times; 112px, with an internal content area of 100px &times; 100px:

  {
    <div className="relative grid grid-cols-[1fr_8rem_1fr] grid-rows-[1fr_2fr_1fr] gap-px bg-gray-700/10 font-mono text-sm leading-6 font-bold dark:bg-gray-700">
      <div className="col-start-1 row-start-1 bg-white dark:bg-gray-900"></div>
      <div className="relative col-start-2 row-start-1 bg-white dark:bg-gray-900">
        {/* w-measure indicator */}
        <div className="absolute right-0 bottom-2 left-0 flex -translate-y-5">
          {/* Horizontal line */}
          <div className="absolute top-1/2 right-0 left-0 h-px -translate-y-px bg-blue-400"></div>
          {/* Left chip */}
          <div className="w-full">
            <div className="absolute top-1/2 left-0 h-2 w-px -translate-x-px -translate-y-1 rounded-full bg-blue-400"></div>
          </div>
          {/* Badge */}
          <div className="relative flex w-full flex-auto items-center justify-center bg-white px-1.5 font-mono text-xs leading-none font-bold text-blue-600 dark:bg-gray-900 dark:text-blue-400">
            128px
          </div>
          {/* Right chip */}
          <div className="w-full">
            <div className="absolute top-1/2 right-0 h-2 w-px translate-x-px -translate-y-1 rounded-full bg-blue-400"></div>
          </div>
        </div>
      </div>
      <div className="col-start-3 row-start-1 bg-white dark:bg-gray-900"></div>
      <div className="relative col-start-1 row-start-2 bg-white dark:bg-gray-900">
        {/* h-measure indicator */}
        <div className="absolute top-0 right-2 bottom-0 flex w-3 -translate-x-5">
          {/* Vertical line */}
          <div className="absolute top-0 bottom-0 left-1/2 w-px translate-x-[-0.5px] bg-blue-400"></div>
          {/* Top chip */}
          <div className="w-full">
            <div className="absolute top-0 left-1/2 h-px w-2 -translate-x-1 -translate-y-px rounded-full bg-blue-400"></div>
          </div>
          {/* Badge */}
          <div className="relative flex h-3 flex-auto translate-x-[-1.15rem] translate-y-14 -rotate-90 items-center justify-center bg-white px-1.5 font-mono text-xs leading-none font-bold text-blue-600 dark:bg-gray-900 dark:text-blue-400">
            128px
          </div>
          {/* Bottom chip */}
          <div className="w-full">
            <div className="absolute bottom-0 left-1/2 h-px w-2 -translate-x-1 translate-y-px rounded-full bg-blue-400"></div>
          </div>
        </div>
      </div>
      <div className="col-start-2 row-start-2 size-32 bg-white">
        <div className="relative box-content size-32 -translate-x-5 -translate-y-5 p-5 ring-4 ring-blue-300 ring-inset dark:ring-blue-500">
          <div className="h-full w-full bg-blue-500 ring-1 ring-blue-500"></div>
          <div className="absolute inset-1 z-10">
            
          </div>
        </div>
      </div>
      <div className="col-start-3 row-start-2 bg-white dark:bg-gray-900"></div>
      <div className="col-start-1 row-start-3 bg-white dark:bg-gray-900"></div>
      <div className="col-start-2 row-start-3 bg-white dark:bg-gray-900"></div>
      <div className="col-start-3 row-start-3 bg-white dark:bg-gray-900"></div>
    </div>
  }

```html
<!-- [!code classes:box-content] -->
<div class="box-content size-32 border-4 p-4 ...">
  <!-- ... -->
</div>
```

### Responsive design
