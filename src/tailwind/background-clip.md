---
title: background-clip
source_url: https://tailwindcss.com/docs/background-clip
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: background-clip.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 220
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `bg-clip-border` | `background-clip: border-box;` |
| `bg-clip-padding` | `background-clip: padding-box;` |
| `bg-clip-content` | `background-clip: content-box;` |
| `bg-clip-text` | `background-clip: text;` |

## Examples

### Basic example

Use the `bg-clip-border`, `bg-clip-padding`, and `bg-clip-content` utilities to control the bounding box of an element's background:

  {
    <div className="flex flex-col items-center justify-center space-y-10 sm:flex-row sm:space-y-0 sm:space-x-10">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          bg-clip-border
        </p>
        <div className="flex h-24 w-24 items-center justify-center rounded-lg border-3 border-dashed border-white/50 bg-indigo-500 bg-clip-border p-3 font-mono text-sm font-extrabold text-white"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          bg-clip-padding
        </p>
        <div className="flex h-24 w-24 items-center justify-center rounded-lg border-3 border-dashed border-indigo-500/50 bg-indigo-500 bg-clip-padding p-3 font-mono text-sm font-extrabold text-white"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          bg-clip-content
        </p>
        <div className="flex h-24 w-24 items-center justify-center rounded-lg border-3 border-dashed border-indigo-500/50 bg-indigo-500 bg-clip-content p-3 font-mono text-sm font-extrabold text-white"></div>
      </div>
    </div>
  }

```html
<!-- [!code classes:bg-clip-border,bg-clip-padding,bg-clip-content] -->
<div class="border-4 bg-indigo-500 bg-clip-border p-3"></div>
<div class="border-4 bg-indigo-500 bg-clip-padding p-3"></div>
<div class="border-4 bg-indigo-500 bg-clip-content p-3"></div>
```

### Cropping to text

Use the `bg-clip-text` utility to crop an element's background to match the shape of the text:

  {
    <p className="bg-linear-to-r from-pink-500 to-violet-500 bg-clip-text text-center text-4xl leading-none font-extrabold tracking-tight text-transparent sm:text-5xl">
      Hello world
    </p>
  }

```html
<!-- [!code classes:bg-clip-text] -->
<p class="bg-linear-to-r from-pink-500 to-violet-500 bg-clip-text text-5xl font-extrabold text-transparent ...">
  Hello world
</p>
```

### Responsive design
