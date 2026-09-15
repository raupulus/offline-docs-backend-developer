---
title: rotate
description: Utilities for rotating elements.
source_url: https://tailwindcss.com/docs/rotate
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: rotate.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1480
---

## Examples

### Basic example

Use `rotate-<number>` utilities like `rotate-45` and `rotate-90` to rotate an element by degrees:

  {
    <div className="flex scroll-p-8 overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-12 p-8 font-mono font-bold sm:gap-4">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rotate-45</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 rotate-45">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rotate-90</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 rotate-90">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rotate-210</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 rotate-210">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
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
<!-- [!code classes:rotate-45,rotate-90,rotate-210] -->
<img class="rotate-45 ..." src="/img/mountains.jpg" />
<img class="rotate-90 ..." src="/img/mountains.jpg" />
<img class="rotate-210 ..." src="/img/mountains.jpg" />
```

### Using negative values

Use `-rotate-<number>` utilities like `-rotate-45` and `-rotate-90` to rotate an element counterclockwise by degrees:

  {
    <div className="flex scroll-p-8 overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-12 p-8 font-mono font-bold sm:gap-4">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">-rotate-45</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 -rotate-45">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">-rotate-90</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 -rotate-90">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">-rotate-210</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 -rotate-210">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
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
<!-- [!code classes:-rotate-45,-rotate-90,-rotate-210] -->
<img class="-rotate-45 ..." src="/img/mountains.jpg" />
<img class="-rotate-90 ..." src="/img/mountains.jpg" />
<img class="-rotate-210 ..." src="/img/mountains.jpg" />
```

### Rotating in 3D space

Use `rotate-x-<number>`, `rotate-y-<number>`, and `rotate-z-<number>` utilities like `rotate-x-50`, `-rotate-y-30`, and `rotate-z-45` together to rotate an element in 3D space:

  {
    <div className="flex scroll-p-8 overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-12 p-8 font-mono font-bold sm:gap-4">
        <div className="flex shrink-0 flex-col items-center">
          <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rotate-x-50</p>
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rotate-z-45</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 rotate-x-50 rotate-z-45">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rotate-x-15</p>
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            -rotate-y-30
          </p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 rotate-x-15 -rotate-y-30">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rotate-y-25</p>
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rotate-z-30</p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 rotate-y-25 rotate-z-30">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
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
<!-- [!code classes:rotate-y-25,rotate-z-30,rotate-x-15,-rotate-y-30,rotate-x-50 rotate-z-45] -->
<img class="rotate-x-50 rotate-z-45 ..." src="/img/mountains.jpg" />
<img class="rotate-x-15 -rotate-y-30 ..." src="/img/mountains.jpg" />
<img class="rotate-y-25 rotate-z-30 ..." src="/img/mountains.jpg" />
```

### Using a custom value

### Responsive design
