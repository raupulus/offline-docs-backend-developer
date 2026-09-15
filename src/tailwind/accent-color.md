---
title: accent-color
description: Utilities for controlling the accented color of a form control.
source_url: https://tailwindcss.com/docs/accent-color
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: accent-color.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 10
---

CustomizingYourThemeColors,
  ResponsiveDesign,
  TargetingSpecificStates,
  UsingACustomValue,
} from "@/components/content.tsx";

| Clase | Propiedades CSS |
| :--- | :--- |
| `accent-inherit` | `accent-color: inherit;` |
| `accent-current` | `accent-color: currentColor;` |
| `accent-transparent` | `accent-color: transparent;` |
| `accent-(<custom-property>)` | `accent-color: var(<custom-property>);` |
| `accent-[<value>]` | `accent-color: <value>;` |

## Examples

### Setting the accent color

Use utilities like `accent-rose-500` and `accent-lime-600` to change the accent color of an element:

  {
    <div className="flex flex-wrap justify-center gap-6">
      <label className="flex items-center space-x-2">
        <input type="checkbox" defaultChecked />
        <div className="text-sm font-semibold text-gray-900 dark:text-gray-200">Browser default</div>
      </label>
      <label className="flex items-center space-x-2">
        <input type="checkbox" className="accent-pink-500" defaultChecked />
        <div className="text-sm font-semibold text-gray-900 dark:text-gray-200">Customized</div>
      </label>
    </div>
  }

```html
<!-- [!code classes:accent-pink-500] -->
<label>
  <input type="checkbox" checked />
  Browser default
</label>
<label>
  <input class="accent-pink-500" type="checkbox" checked />
  Customized
</label>
```

This is helpful for styling elements like checkboxes and radio groups by overriding the browser's default color.

### Changing the opacity

Use the color opacity modifier to control the opacity of an element's accent color:

  {
    <div className="flex flex-wrap justify-center gap-6">
      <label className="flex items-center space-x-2">
        <input type="checkbox" defaultChecked className="accent-purple-500/25" />
        <div className="text-sm font-semibold text-gray-900 dark:text-gray-200">accent-purple-500/25</div>
      </label>
      <label className="flex items-center space-x-2">
        <input type="checkbox" className="accent-purple-500/75" defaultChecked />
        <div className="text-sm font-semibold text-gray-900 dark:text-gray-200">accent-purple-500/75</div>
      </label>
    </div>
  }

```html
<!-- [!code word:/25] -->
<!-- [!code word:/75] -->
<input class="accent-purple-500/25" type="checkbox" checked />
<input class="accent-purple-500/75" type="checkbox" checked />
```

Setting the accent color opacity has limited browser-support and only works in Firefox at this time.

### Using a custom value

### Applying on hover

  {
    <div className="flex flex-wrap justify-center gap-6">
      <label className="flex items-center space-x-2">
        <input type="checkbox" className="accent-black hover:accent-pink-500" defaultChecked />
        <div className="text-sm font-semibold text-gray-900 dark:text-gray-200">Agree to terms</div>
      </label>
    </div>
  }

```html
<!-- [!code classes:hover:accent-pink-500] -->
<input class="accent-black hover:accent-pink-500" type="checkbox" />
```

### Responsive design

## Customizing your theme
