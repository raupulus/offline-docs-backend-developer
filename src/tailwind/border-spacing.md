---
title: border-spacing
description: Utilities for controlling the spacing between table borders.
source_url: https://tailwindcss.com/docs/border-spacing
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: border-spacing.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 330
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `border-spacing-<number>` | `border-spacing: calc(var(--spacing) * <number>);` |
| `border-spacing-px` | `border-spacing: 1px;` |
| `border-spacing-(<custom-property>)` | `border-spacing: var(<custom-property>);` |
| `border-spacing-[<value>]` | `border-spacing: <value>;` |
| `border-spacing-x-<number>` | `border-spacing: calc(var(--spacing) * <number>) var(--tw-border-spacing-y);` |
| `border-spacing-x-px` | `border-spacing: 1px var(--tw-border-spacing-y);` |
| `border-spacing-x-(<custom-property>)` | `border-spacing: var(<custom-property>) var(--tw-border-spacing-y);` |
| `border-spacing-x-[<value>]` | `border-spacing: <value> var(--tw-border-spacing-y);` |
| `border-spacing-y-<number>` | `border-spacing: var(--tw-border-spacing-x) calc(var(--spacing) * <number>);` |
| `border-spacing-y-px` | `border-spacing: var(--tw-border-spacing-x) 1px;` |
| `border-spacing-y-(<custom-property>)` | `border-spacing: var(--tw-border-spacing-x) var(<custom-property>);` |
| `border-spacing-y-[<value>]` | `border-spacing: var(--tw-border-spacing-x) <value>;` |

## Examples

### Basic example

Use `border-spacing-<number>` utilities like `border-spacing-2` and `border-spacing-x-3` to control the space between the borders of table cells with [separate borders](/docs/border-collapse#separating-table-borders):

  {
    <div className="px-4 py-8 sm:px-8">
      <table className="w-full border-separate border-spacing-2 border border-gray-400 bg-white text-sm dark:border-gray-500 dark:bg-gray-800">
        <thead className="bg-gray-50 dark:bg-gray-700">
          <tr>
            <th className="w-1/2 border border-gray-300 p-4 text-left font-semibold text-gray-900 dark:border-gray-600 dark:text-gray-200">
              State
            </th>
            <th className="w-1/2 border border-gray-300 p-4 text-left font-semibold text-gray-900 dark:border-gray-600 dark:text-gray-200">
              City
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className="border border-gray-300 p-4 text-gray-500 dark:border-gray-700 dark:text-gray-400">
              Indiana
            </td>
            <td className="border border-gray-300 p-4 text-gray-500 dark:border-gray-700 dark:text-gray-400">
              Indianapolis
            </td>
          </tr>
          <tr>
            <td className="border border-gray-300 p-4 text-gray-500 dark:border-gray-700 dark:text-gray-400">Ohio</td>
            <td className="border border-gray-300 p-4 text-gray-500 dark:border-gray-700 dark:text-gray-400">
              Columbus
            </td>
          </tr>
          <tr>
            <td className="border border-gray-300 p-4 text-gray-500 dark:border-gray-700 dark:text-gray-400">
              Michigan
            </td>
            <td className="border border-gray-300 p-4 text-gray-500 dark:border-gray-700 dark:text-gray-400">
              Detroit
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  }

```html
<!-- [!code classes:border-spacing-2] -->
<table class="border-separate border-spacing-2 border border-gray-400 dark:border-gray-500">
  <thead>
    <tr>
      <th class="border border-gray-300 dark:border-gray-600">State</th>
      <th class="border border-gray-300 dark:border-gray-600">City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-gray-300 dark:border-gray-700">Indiana</td>
      <td class="border border-gray-300 dark:border-gray-700">Indianapolis</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-700">Ohio</td>
      <td class="border border-gray-300 dark:border-gray-700">Columbus</td>
    </tr>
    <tr>
      <td class="border border-gray-300 dark:border-gray-700">Michigan</td>
      <td class="border border-gray-300 dark:border-gray-700">Detroit</td>
    </tr>
  </tbody>
</table>
```

### Using a custom value

### Responsive design

## Customizing your theme
