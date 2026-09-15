---
title: cursor
description: Utilities for controlling the cursor style when hovering over an element.
source_url: https://tailwindcss.com/docs/cursor
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: cursor.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 510
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `cursor-auto` | `cursor: auto;` |
| `cursor-default` | `cursor: default;` |
| `cursor-pointer` | `cursor: pointer;` |
| `cursor-wait` | `cursor: wait;` |
| `cursor-text` | `cursor: text;` |
| `cursor-move` | `cursor: move;` |
| `cursor-help` | `cursor: help;` |
| `cursor-not-allowed` | `cursor: not-allowed;` |
| `cursor-none` | `cursor: none;` |
| `cursor-context-menu` | `cursor: context-menu;` |
| `cursor-progress` | `cursor: progress;` |
| `cursor-cell` | `cursor: cell;` |
| `cursor-crosshair` | `cursor: crosshair;` |
| `cursor-vertical-text` | `cursor: vertical-text;` |
| `cursor-alias` | `cursor: alias;` |
| `cursor-copy` | `cursor: copy;` |
| `cursor-no-drop` | `cursor: no-drop;` |
| `cursor-grab` | `cursor: grab;` |
| `cursor-grabbing` | `cursor: grabbing;` |
| `cursor-all-scroll` | `cursor: all-scroll;` |
| `cursor-col-resize` | `cursor: col-resize;` |
| `cursor-row-resize` | `cursor: row-resize;` |
| `cursor-n-resize` | `cursor: n-resize;` |
| `cursor-e-resize` | `cursor: e-resize;` |
| `cursor-s-resize` | `cursor: s-resize;` |
| `cursor-w-resize` | `cursor: w-resize;` |
| `cursor-ne-resize` | `cursor: ne-resize;` |
| `cursor-nw-resize` | `cursor: nw-resize;` |
| `cursor-se-resize` | `cursor: se-resize;` |
| `cursor-sw-resize` | `cursor: sw-resize;` |
| `cursor-ew-resize` | `cursor: ew-resize;` |
| `cursor-ns-resize` | `cursor: ns-resize;` |
| `cursor-nesw-resize` | `cursor: nesw-resize;` |
| `cursor-nwse-resize` | `cursor: nwse-resize;` |
| `cursor-zoom-in` | `cursor: zoom-in;` |
| `cursor-zoom-out` | `cursor: zoom-out;` |
| `cursor-(<custom-property>)` | `cursor: var(<custom-property>);` |
| `cursor-[<value>]` | `cursor: <value>;` |

## Examples

### Basic example

Use utilities like `cursor-pointer` and `cursor-grab` to control which cursor is displayed when hovering over an element:

  {
    <div className="flex flex-col items-center justify-around gap-4 sm:flex-row sm:gap-0">
      <button
        type="button"
        className="w-full cursor-pointer rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white hover:bg-indigo-700 focus:outline-none disabled:bg-indigo-300 sm:w-auto dark:disabled:bg-indigo-800 dark:disabled:text-indigo-400"
        tabIndex="-1"
      >
        Submit
      </button>
      <button
        type="button"
        className="w-full cursor-progress rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white hover:bg-indigo-700 focus:outline-none disabled:bg-indigo-300 sm:w-auto dark:disabled:bg-indigo-800 dark:disabled:text-indigo-400"
        tabIndex="-1"
      >
        Saving...
      </button>
      <button
        type="button"
        disabled
        className="w-full cursor-not-allowed rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white hover:bg-indigo-700 focus:outline-none disabled:bg-indigo-300 sm:w-auto dark:disabled:bg-indigo-800 dark:disabled:text-indigo-400"
        tabIndex="-1"
      >
        Confirm
      </button>
    </div>
  }

```html
<!-- [!code classes:cursor-pointer,cursor-progress,cursor-not-allowed] -->
<button class="cursor-pointer ...">Submit</button>
<button class="cursor-progress ...">Saving...</button>
<button class="cursor-not-allowed ..." disabled>Confirm</button>
```

### Using a custom value

### Responsive design
