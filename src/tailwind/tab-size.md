---
title: tab-size
description: Utilities for controlling the size of tab characters.
source_url: https://tailwindcss.com/docs/tab-size
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: tab-size.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1630
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `tab-<number>` | `tab-size: <number>;` |
| `tab-(<custom-property>)` | `tab-size: var(<custom-property>);` |
| `tab-[<value>]` | `tab-size: <value>;` |

## Examples

### Basic example

Use `tab-<number>` utilities like `tab-2` and `tab-8` to control the size of tab characters:

  <div className="grid gap-6 sm:grid-cols-2">
    <div className="tab-2">
      <span className="mb-3 block font-mono text-xs font-medium text-gray-500 dark:text-gray-400">tab-2</span>

{/* prettier-ignore */}
```jsx
function indent() {
	return 'tabbed';
}
```

    </div>
    <div className="tab-8">
      <span className="mb-3 block font-mono text-xs font-medium text-gray-500 dark:text-gray-400">tab-8</span>

{/* prettier-ignore */}
```jsx
function indent() {
	return 'tabbed';
}
```

    </div>

  </div>

```html
<!-- [!code classes:tab-2,tab-8] -->
<pre class="tab-2 ...">function indent() {&#10;&#9;return 'tabbed'&#10;}</pre>
<pre class="tab-8 ...">function indent() {&#10;&#9;return 'tabbed'&#10;}</pre>
```

### Using a custom value

### Responsive design
