---
title: border-collapse
description: Utilities for controlling whether table borders should collapse or be
  separated.
source_url: https://tailwindcss.com/docs/border-collapse
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: border-collapse.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 300
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `border-collapse` | `border-collapse: collapse;` |
| `border-separate` | `border-collapse: separate;` |

## Examples

### Collapsing table borders

Use the `border-collapse` utility to combine adjacent cell borders into a single border when possible:

  {
    <div className="px-4 py-8 sm:px-8">
      <table className="w-full border-collapse border border-gray-400 bg-white text-sm dark:border-gray-500 dark:bg-gray-800">
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
<!-- [!code classes:border-collapse] -->
<table class="border-collapse border border-gray-400 ...">
  <thead>
    <tr>
      <th class="border border-gray-300 ...">State</th>
      <th class="border border-gray-300 ...">City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-gray-300 ...">Indiana</td>
      <td class="border border-gray-300 ...">Indianapolis</td>
    </tr>
    <tr>
      <td class="border border-gray-300 ...">Ohio</td>
      <td class="border border-gray-300 ...">Columbus</td>
    </tr>
    <tr>
      <td class="border border-gray-300 ...">Michigan</td>
      <td class="border border-gray-300 ...">Detroit</td>
    </tr>
  </tbody>
</table>
```

Note that this includes collapsing borders on the top-level `<table>` tag.

### Separating table borders

Use the `border-separate` utility to force each cell to display its own separate borders:

  {
    <div className="px-4 py-8 sm:px-8">
      <table className="w-full border-separate border border-gray-400 bg-white text-sm dark:border-gray-500 dark:bg-gray-800">
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
<!-- [!code classes:border-separate] -->
<table class="border-separate border border-gray-400 ...">
  <thead>
    <tr>
      <th class="border border-gray-300 ...">State</th>
      <th class="border border-gray-300 ...">City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-gray-300 ...">Indiana</td>
      <td class="border border-gray-300 ...">Indianapolis</td>
    </tr>
    <tr>
      <td class="border border-gray-300 ...">Ohio</td>
      <td class="border border-gray-300 ...">Columbus</td>
    </tr>
    <tr>
      <td class="border border-gray-300 ...">Michigan</td>
      <td class="border border-gray-300 ...">Detroit</td>
    </tr>
  </tbody>
</table>
```

### Responsive design
