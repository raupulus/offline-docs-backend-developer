---
title: border-radius
description: Utilities for controlling the border radius of an element.
source_url: https://tailwindcss.com/docs/border-radius
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: border-radius.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 320
---

## Examples

### Basic example

Use utilities like `rounded-sm` and `rounded-md` to apply different border radius sizes to an element:

  {
    <div className="flex flex-col items-center justify-around gap-4 text-center text-sm leading-6 font-bold text-white sm:flex-row">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-sm</p>
        <div className="size-16 rounded-sm bg-purple-500 p-4"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-md</p>
        <div className="size-16 rounded-md bg-purple-500 p-4"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-lg</p>
        <div className="size-16 rounded-lg bg-purple-500 p-4"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-xl</p>
        <div className="size-16 rounded-xl bg-purple-500 p-4"></div>
      </div>
    </div>
  }

```html
<!-- [!code classes:rounded-sm,rounded-md,rounded-lg,rounded-xl] -->
<div class="rounded-sm ..."></div>
<div class="rounded-md ..."></div>
<div class="rounded-lg ..."></div>
<div class="rounded-xl ..."></div>
```

### Rounding sides separately

Use utilities like `rounded-t-md` and `rounded-r-lg` to only round one side of an element:

  {
    <div className="flex flex-col items-center justify-around gap-4 text-center text-sm leading-6 font-bold text-white sm:flex-row">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-t-lg</p>
        <div className="size-16 rounded-t-lg bg-blue-500 p-4"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-r-lg</p>
        <div className="size-16 rounded-r-lg bg-blue-500 p-4"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-b-lg</p>
        <div className="size-16 rounded-b-lg bg-blue-500 p-4"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-l-lg</p>
        <div className="size-16 rounded-l-lg bg-blue-500 p-4"></div>
      </div>
    </div>
  }

```html
<!-- [!code classes:rounded-t-lg,rounded-r-lg,rounded-b-lg,rounded-l-lg] -->
<div class="rounded-t-lg ..."></div>
<div class="rounded-r-lg ..."></div>
<div class="rounded-b-lg ..."></div>
<div class="rounded-l-lg ..."></div>
```

### Rounding corners separately

Use utilities like `rounded-tr-md` and `rounded-tl-lg` utilities to only round one corner of an element:

  {
    <div className="flex flex-col items-center justify-around gap-4 text-center text-sm leading-6 font-bold text-white sm:flex-row">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-tl-lg</p>
        <div className="size-16 rounded-tl-lg bg-pink-500 p-4"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-tr-lg</p>
        <div className="size-16 rounded-tr-lg bg-pink-500 p-4"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-br-lg</p>
        <div className="size-16 rounded-br-lg bg-pink-500 p-4"></div>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-bl-lg</p>
        <div className="size-16 rounded-bl-lg bg-pink-500 p-4"></div>
      </div>
    </div>
  }

```html
<!-- [!code classes:rounded-tl-lg,rounded-tr-lg,rounded-br-lg,rounded-bl-lg] -->
<div class="rounded-tl-lg ..."></div>
<div class="rounded-tr-lg ..."></div>
<div class="rounded-br-lg ..."></div>
<div class="rounded-bl-lg ..."></div>
```

### Using logical properties

Use utilities like `rounded-s-md` and `rounded-se-xl` to set the border radius using [logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts), which map to the appropriate corners based on the text direction:

  {
    <div className="grid grid-cols-2 place-items-center gap-x-4">
      <div className="flex flex-col items-start gap-y-4" dir="ltr">
        <p className="text-sm font-medium">Left-to-right</p>
        <div className="size-16 rounded-s-lg bg-blue-500 p-4"></div>
      </div>
      <div className="flex flex-col items-start gap-y-4" dir="rtl">
        <p className="text-sm font-medium">Right-to-left</p>
        <div className="size-16 rounded-s-lg bg-blue-500 p-4"></div>
      </div>
    </div>
  }

```html
<!-- [!code classes:rounded-s-lg] -->
<!-- [!code word:dir="ltr"] -->
<!-- [!code word:dir="rtl"] -->
<div dir="ltr">
  <div class="rounded-s-lg ..."></div>
</div>

<div dir="rtl">
  <div class="rounded-s-lg ..."></div>
</div>
```

Here are all the available border radius logical property utilities and their physical property equivalents in both LTR and RTL modes.

{

<table>
  <thead>
    <tr>
      <th>Class</th>
      <th>Left-to-right</th>
      <th>Right-to-left</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code>rounded-s-*</code>
      </td>
      <td>
        <code>rounded-l-*</code>
      </td>
      <td>
        <code>rounded-r-*</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>rounded-e-*</code>
      </td>
      <td>
        <code>rounded-r-*</code>
      </td>
      <td>
        <code>rounded-l-*</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>rounded-ss-*</code>
      </td>
      <td>
        <code>rounded-tl-*</code>
      </td>
      <td>
        <code>rounded-tr-*</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>rounded-se-*</code>
      </td>
      <td>
        <code>rounded-tr-*</code>
      </td>
      <td>
        <code>rounded-tl-*</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>rounded-es-*</code>
      </td>
      <td>
        <code>rounded-bl-*</code>
      </td>
      <td>
        <code>rounded-br-*</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>rounded-ee-*</code>
      </td>
      <td>
        <code>rounded-br-*</code>
      </td>
      <td>
        <code>rounded-bl-*</code>
      </td>
    </tr>
  </tbody>
</table>

}

For more control, you can also use the [LTR and RTL modifiers](/docs/hover-focus-and-other-states#rtl-support) to conditionally apply specific styles depending on the current text direction.

### Creating pill buttons

Use the `rounded-full` utility to create pill buttons:

  {
    <div className="flex justify-center gap-4 text-center text-sm leading-6 font-bold text-white">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-full</p>
        <button className="rounded-full bg-cyan-500 px-4 py-2 text-sm font-semibold text-white">Save Changes</button>
      </div>
    </div>
  }

```html
<!-- [!code classes:rounded-full] -->
<button class="rounded-full ...">Save Changes</button>
```

### Removing the border radius

Use the `rounded-none` utility to remove an existing border radius from an element:

  {
    <div className="flex justify-center gap-4 text-center text-sm leading-6 font-bold text-white">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">rounded-none</p>
        <button className="rounded-none bg-sky-500 px-4 py-2 text-sm font-semibold text-white">Save Changes</button>
      </div>
    </div>
  }

```html
<!-- [!code classes:rounded-none] -->
<button class="rounded-none ...">Save Changes</button>
```

### Using a custom value

### Responsive design

## Customizing your theme
