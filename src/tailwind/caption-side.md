---
title: caption-side
description: Utilities for controlling the alignment of a caption element inside of
  a table.
source_url: https://tailwindcss.com/docs/caption-side
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: caption-side.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 420
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `caption-top` | `caption-side: top;` |
| `caption-bottom` | `caption-side: bottom;` |

## Examples

### Placing at top of table

Use the `caption-top` utility to position a caption element at the top of a table:

  {
    <div className="overflow-hidden px-4 py-8 sm:px-8">
      <table className="w-full table-auto border-collapse text-sm">
        <caption className="caption-top pb-4 text-xs text-gray-500 dark:text-gray-400">
          Table 3.1: Professional wrestlers and their signature moves.
        </caption>
        <thead>
          <tr>
            <th className="border border-gray-200 bg-gray-50 p-4 py-3 pl-8 text-left font-medium text-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-200">
              Wrestler
            </th>
            <th className="border border-gray-200 bg-gray-50 p-4 py-3 pr-8 text-left font-medium text-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-200">
              Signature Move(s)
            </th>
          </tr>
        </thead>
        <tbody className="bg-white dark:bg-gray-800">
          <tr>
            <td className="border border-gray-200 p-4 pl-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              "Stone Cold" Steve Austin
            </td>
            <td className="border border-gray-200 p-4 pr-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              Stone Cold Stunner, Lou Thesz Press
            </td>
          </tr>
          <tr>
            <td className="border border-gray-200 p-4 pl-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              Bret "The Hitman" Hart
            </td>
            <td className="border border-gray-200 p-4 pr-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              The Sharpshooter
            </td>
          </tr>
          <tr>
            <td className="border border-gray-200 p-4 pl-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              Razor Ramon
            </td>
            <td className="border border-gray-200 p-4 pr-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              Razor's Edge, Fallaway Slam
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  }

```html
<!-- [!code classes:caption-top] -->
<table>
  <caption class="caption-top">
    Table 3.1: Professional wrestlers and their signature moves.
  </caption>
  <thead>
    <tr>
      <th>Wrestler</th>
      <th>Signature Move(s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Stone Cold" Steve Austin</td>
      <td>Stone Cold Stunner, Lou Thesz Press</td>
    </tr>
    <tr>
      <td>Bret "The Hitman" Hart</td>
      <td>The Sharpshooter</td>
    </tr>
    <tr>
      <td>Razor Ramon</td>
      <td>Razor's Edge, Fallaway Slam</td>
    </tr>
  </tbody>
</table>
```

### Placing at bottom of table

Use the `caption-bottom` utility to position a caption element at the bottom of a table:

  {
    <div className="overflow-hidden px-4 py-8 sm:px-8">
      <table className="w-full table-auto border-collapse text-sm">
        <caption className="caption-bottom pt-4 text-xs text-gray-500 dark:text-gray-400">
          Table 3.1: Professional wrestlers and their signature moves.
        </caption>
        <thead>
          <tr>
            <th className="border border-gray-200 bg-gray-50 p-4 py-3 pl-8 text-left font-medium text-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-200">
              Wrestler
            </th>
            <th className="border border-gray-200 bg-gray-50 p-4 py-3 pr-8 text-left font-medium text-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-200">
              Signature Move(s)
            </th>
          </tr>
        </thead>
        <tbody className="bg-white dark:bg-gray-800">
          <tr>
            <td className="border border-gray-200 p-4 pl-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              "Stone Cold" Steve Austin
            </td>
            <td className="border border-gray-200 p-4 pr-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              Stone Cold Stunner, Lou Thesz Press
            </td>
          </tr>
          <tr>
            <td className="border border-gray-200 p-4 pl-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              Bret "The Hitman" Hart
            </td>
            <td className="border border-gray-200 p-4 pr-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              The Sharpshooter
            </td>
          </tr>
          <tr>
            <td className="border border-gray-200 p-4 pl-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              Razor Ramon
            </td>
            <td className="border border-gray-200 p-4 pr-8 text-gray-500 dark:border-gray-600 dark:text-gray-400">
              Razor's Edge, Fallaway Slam
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  }

```html
<!-- [!code word:caption-bottom] -->
<table>
  <caption class="caption-bottom">
    Table 3.1: Professional wrestlers and their signature moves.
  </caption>
  <thead>
    <tr>
      <th>Wrestler</th>
      <th>Signature Move(s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Stone Cold" Steve Austin</td>
      <td>Stone Cold Stunner, Lou Thesz Press</td>
    </tr>
    <tr>
      <td>Bret "The Hitman" Hart</td>
      <td>The Sharpshooter</td>
    </tr>
    <tr>
      <td>Razor Ramon</td>
      <td>Razor's Edge, Fallaway Slam</td>
    </tr>
  </tbody>
</table>
```

### Responsive design
