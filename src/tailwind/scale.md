---
title: scale
description: Utilities for scaling elements.
source_url: https://tailwindcss.com/docs/scale
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: scale.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1490
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `scale-3d` | `scale: var(--tw-scale-x) var(--tw-scale-y) var(--tw-scale-z);` |

## Examples

### Basic example

Use `scale-<number>` utilities like `scale-75` and `scale-150` to scale an element by a percentage of its original size:

  {
    <div className="flex scroll-p-8 overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-12 p-8 px-12 pb-10 font-mono font-bold sm:gap-4 sm:px-8">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scale-75</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 scale-75">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scale-100</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 scale-100">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scale-125</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 scale-125">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:scale-75,scale-100,scale-125] -->
<img class="scale-75 ..." src="/img/mountains.jpg" />
<img class="scale-100 ..." src="/img/mountains.jpg" />
<img class="scale-125 ..." src="/img/mountains.jpg" />
```

### Scaling on the x-axis

Use the `scale-x-<number>` utilities like `scale-x-75` and `-scale-x-150` to scale an element on the x-axis by a percentage of its original width:

  {
    <div className="flex scroll-p-8 overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-12 p-8 px-12 pb-10 font-mono font-bold sm:gap-4 sm:px-8">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scale-x-75</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 scale-x-75">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scale-x-100</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 scale-x-100">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scale-x-125</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 scale-x-125">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:scale-x-75,scale-x-100,scale-x-125] -->
<img class="scale-x-75 ..." src="/img/mountains.jpg" />
<img class="scale-x-100 ..." src="/img/mountains.jpg" />
<img class="scale-x-125 ..." src="/img/mountains.jpg" />
```

### Scaling on the y-axis

Use the `scale-y-<number>` utilities like `scale-y-75` and `scale-y-150` to scale an element on the y-axis by a percentage of its original height:

  {
    <div className="flex scroll-p-8 overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-12 p-8 px-12 pb-10 font-mono font-bold sm:gap-4 sm:px-8">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scale-y-75</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 scale-y-75">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scale-y-100</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 scale-y-100">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">scale-y-125</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 scale-y-125">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:scale-y-75,scale-y-100,scale-y-125] -->
<img class="scale-y-75 ..." src="/img/mountains.jpg" />
<img class="scale-y-100 ..." src="/img/mountains.jpg" />
<img class="scale-y-125 ..." src="/img/mountains.jpg" />
```

### Using negative values

Use `-scale-<number>`, `-scale-x-<number>` or `-scale-y-<number>` utilities like `-scale-x-75` and `-scale-125` to mirror and scale down an element by a percentage of its original size:

  {
    <div className="flex scroll-p-8 overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-12 p-8 px-12 pb-10 font-mono font-bold sm:gap-4 sm:px-8">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">-scale-x-75</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 -scale-x-75">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">-scale-100</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 -scale-100">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            -scale-y-125
          </p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 -scale-y-125">
              <img
                className="size-24 rounded-lg object-cover"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:-scale-x-75,-scale-100,-scale-y-125] -->
<img class="-scale-x-75 ..." src="/img/mountains.jpg" />
<img class="-scale-100 ..." src="/img/mountains.jpg" />
<img class="-scale-y-125 ..." src="/img/mountains.jpg" />
```

### Using a custom value

### Applying on hover
