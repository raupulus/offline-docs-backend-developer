---
title: background-color
source_url: https://tailwindcss.com/docs/background-color
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: background-color.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 230
---

CustomizingYourThemeColors,
  ResponsiveDesign,
  TargetingSpecificStates,
  UsingACustomValue,
} from "@/components/content.tsx";

| Clase | Propiedades CSS |
| :--- | :--- |
| `bg-inherit` | `background-color: inherit;` |
| `bg-current` | `background-color: currentColor;` |
| `bg-transparent` | `background-color: transparent;` |
| `bg-(<custom-property>)` | `background-color: var(<custom-property>);` |
| `bg-[<value>]` | `background-color: <value>;` |

## Examples

### Basic example

Use utilities like `bg-white`, `bg-indigo-500` and `bg-transparent` to control the background color of an element:

  {
    <div className="grid grid-cols-1 gap-4 text-sm text-white sm:grid-cols-3">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">bg-blue-500</p>
        <button
          type="button"
          tabIndex="-1"
          className="rounded-md bg-blue-500 px-4 py-2 text-sm font-semibold text-white opacity-100 focus:outline-none"
        >
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">bg-cyan-500</p>
        <button
          type="button"
          tabIndex="-1"
          className="rounded-md bg-cyan-500 px-4 py-2 text-sm font-semibold text-white opacity-100 focus:outline-none"
        >
          Button B
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">bg-pink-500</p>
        <button
          type="button"
          tabIndex="-1"
          className="rounded-md bg-pink-500 px-4 py-2 text-sm font-semibold text-white opacity-100 focus:outline-none"
        >
          Button C
        </button>
      </div>
    </div>
  }

```html
<!-- [!code classes:bg-blue-500,bg-cyan-500,bg-pink-500] -->
<button class="bg-blue-500 ...">Button A</button>
<button class="bg-cyan-500 ...">Button B</button>
<button class="bg-pink-500 ...">Button C</button>
```

### Changing the opacity

Use the color opacity modifier to control the opacity of an element's background color:

  {
    <div className="grid grid-cols-1 gap-4 text-sm text-white sm:grid-cols-3">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">
          bg-sky-500/100
        </p>
        <button
          type="button"
          tabIndex="-1"
          className="rounded-md bg-sky-500/100 px-4 py-2 text-sm font-semibold text-white opacity-100 focus:outline-none"
        >
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">bg-sky-500/75</p>
        <button
          type="button"
          tabIndex="-1"
          className="rounded-md bg-sky-500/75 px-4 py-2 text-sm font-semibold text-white opacity-100 focus:outline-none"
        >
          Button B
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">bg-sky-500/50</p>
        <button
          type="button"
          tabIndex="-1"
          className="rounded-md bg-sky-500/50 px-4 py-2 text-sm font-semibold text-white opacity-100 focus:outline-none"
        >
          Button C
        </button>
      </div>
    </div>
  }

```html
<!-- [!code word:/100] -->
<!-- [!code word:/75] -->
<!-- [!code word:/50] -->
<button class="bg-sky-500/100 ..."></button>
<button class="bg-sky-500/75 ..."></button>
<button class="bg-sky-500/50 ..."></button>
```

### Using a custom value

### Applying on hover

  {
    <button
      type="button"
      tabIndex="-1"
      className="mx-auto block rounded-md bg-indigo-500 px-3 py-2 text-sm font-semibold text-white hover:bg-fuchsia-500 focus:outline-none"
    >
      Save changes
    </button>
  }

```html
<!-- [!code classes:hover:bg-fuchsia-500] -->
<button class="bg-indigo-500 hover:bg-fuchsia-500 ...">Save changes</button>
```

### Responsive design

## Customizing your theme
