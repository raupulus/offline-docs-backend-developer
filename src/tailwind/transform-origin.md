---
title: transform-origin
source_url: https://tailwindcss.com/docs/transform-origin
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: transform-origin.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1790
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `origin-center` | `transform-origin: center;` |
| `origin-top` | `transform-origin: top;` |
| `origin-top-right` | `transform-origin: top right;` |
| `origin-right` | `transform-origin: right;` |
| `origin-bottom-right` | `transform-origin: bottom right;` |
| `origin-bottom` | `transform-origin: bottom;` |
| `origin-bottom-left` | `transform-origin: bottom left;` |
| `origin-left` | `transform-origin: left;` |
| `origin-top-left` | `transform-origin: top left;` |
| `origin-(<custom-property>)` | `transform-origin: var(<custom-property>);` |
| `origin-[<value>]` | `transform-origin: <value>;` |

## Examples

### Basic example

Use utilities like `origin-top` and `origin-bottom-left` to set an element's transform origin:

  {
    <div className="flex scroll-p-8 overflow-scroll sm:block sm:overflow-visible">
      <div className="flex shrink-0 items-center justify-around gap-12 p-8 px-12 pb-10 font-mono font-bold sm:gap-4 sm:px-8">
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            origin-center
          </p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 origin-center rotate-45">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            origin-top-left
          </p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 origin-top-left rotate-12">
              <img
                className="size-24 rounded-lg object-cover shadow-xl"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
              <div className="absolute inset-0 rounded-lg ring-1 ring-black/10 ring-inset"></div>
            </div>
          </div>
        </div>
        <div className="flex shrink-0 flex-col items-center">
          <p className="mb-9 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
            origin-bottom
          </p>
          <div className="relative">
            <div className="absolute inset-0">
              <img
                className="size-24 rounded-lg object-cover opacity-25"
                src="https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90"
              />
            </div>
            <div className="relative z-10 origin-bottom -rotate-12">
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
<!-- [!code classes:origin-center,origin-top-left,origin-bottom] -->
<img class="origin-center rotate-45 ..." src="/img/mountains.jpg" />
<img class="origin-top-left rotate-12 ..." src="/img/mountains.jpg" />
<img class="origin-bottom -rotate-12 ..." src="/img/mountains.jpg" />
```

### Using a custom value

### Responsive design
