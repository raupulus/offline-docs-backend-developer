---
title: border-style
source_url: https://tailwindcss.com/docs/border-style
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: border-style.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 340
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `border-solid` | `border-style: solid;` |
| `border-dashed` | `border-style: dashed;` |
| `border-dotted` | `border-style: dotted;` |
| `border-double` | `border-style: double;` |
| `border-hidden` | `border-style: hidden;` |
| `border-none` | `border-style: none;` |
| `divide-solid` | `& > :not(:last-child) {\n  border-style: solid;\n}` |
| `divide-dashed` | `& > :not(:last-child) {\n  border-style: dashed;\n}` |
| `divide-dotted` | `& > :not(:last-child) {\n  border-style: dotted;\n}` |
| `divide-double` | `& > :not(:last-child) {\n  border-style: double;\n}` |
| `divide-hidden` | `& > :not(:last-child) {\n  border-style: hidden;\n}` |
| `divide-none` | `& > :not(:last-child) {\n  border-style: none;\n}` |

## Examples

### Basic example

Use utilities like `border-solid` and `border-dotted` to control an element's border style:

  {
    <div className="grid grid-cols-1 gap-x-4 gap-y-8 text-center text-sm leading-6 font-bold text-white sm:grid-cols-2">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">border-solid</p>
        <button className="rounded-md border-2 border-solid border-indigo-500 bg-white px-4 py-2 text-sm font-semibold text-gray-700 dark:border-sky-500 dark:bg-gray-700 dark:text-white">
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">border-dashed</p>
        <button className="rounded-md border-2 border-dashed border-indigo-500 bg-white px-4 py-2 text-sm font-semibold text-gray-700 dark:border-sky-500 dark:bg-gray-700 dark:text-white">
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">border-dotted</p>
        <button className="rounded-md border-2 border-dotted border-indigo-500 bg-white px-4 py-2 text-sm font-semibold text-gray-700 dark:border-sky-500 dark:bg-gray-700 dark:text-white">
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">border-double</p>
        <button className="rounded-md border-4 border-double border-indigo-500 bg-white px-4 py-2 text-sm font-semibold text-gray-700 dark:border-sky-500 dark:bg-gray-700 dark:text-white">
          Button A
        </button>
      </div>
    </div>
  }

```html
<!-- [!code classes:border-solid,border-dashed,border-dotted,border-double] -->
<div class="border-2 border-solid ..."></div>
<div class="border-2 border-dashed ..."></div>
<div class="border-2 border-dotted ..."></div>
<div class="border-4 border-double ..."></div>
```

### Removing a border

Use the `border-none` utility to remove an existing border from an element:

  {
    <div className="flex justify-center gap-4 text-center text-sm leading-6 font-bold text-white">
      <button className="rounded-md border-2 border-none border-indigo-500 bg-gray-100 px-4 py-2 text-sm font-semibold text-gray-700 dark:bg-gray-700 dark:text-white">
        Save Changes
      </button>
    </div>
  }

```html
<!-- [!code classes:border-none] -->
<button class="border-none ...">Save Changes</button>
```

This is most commonly used to remove a border style that was applied at a smaller breakpoint.

### Setting the divider style

Use utilities like `divide-dashed` and `divide-dotted` to control the border style between child elements:

  {
    <div className="mx-auto grid max-w-lg grid-cols-3 divide-x-3 divide-dashed divide-indigo-500 rounded-lg text-center font-mono text-sm leading-6 font-bold text-gray-400">
      <div className="p-4 outline-1 -outline-offset-1 outline-gray-900/20 outline-dashed dark:outline-white/20">01</div>
      <div className="p-4 outline-1 -outline-offset-1 outline-gray-900/20 outline-dashed dark:outline-white/20">02</div>
      <div className="p-4 outline-1 -outline-offset-1 outline-gray-900/20 outline-dashed dark:outline-white/20">03</div>
    </div>
  }

```html
<!-- [!code classes:divide-dashed] -->
<div class="grid grid-cols-3 divide-x-3 divide-dashed divide-indigo-500">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Responsive design
