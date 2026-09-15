---
title: min-block-size
description: Utilities for setting the minimum block size of an element.
source_url: https://tailwindcss.com/docs/min-block-size
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: min-block-size.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1210
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `min-block-<number>` | `min-block-size: calc(var(--spacing) * <number>);` |
| `min-block-<fraction>` | `min-block-size: calc(<fraction> * 100%);` |
| `min-block-px` | `min-block-size: 1px;` |
| `min-block-full` | `min-block-size: 100%;` |
| `min-block-screen` | `min-block-size: 100vh;` |
| `min-block-dvh` | `min-block-size: 100dvh;` |
| `min-block-dvw` | `min-block-size: 100dvw;` |
| `min-block-lvh` | `min-block-size: 100lvh;` |
| `min-block-lvw` | `min-block-size: 100lvw;` |
| `min-block-svw` | `min-block-size: 100svw;` |
| `min-block-svh` | `min-block-size: 100svh;` |
| `min-block-auto` | `min-block-size: auto;` |
| `min-block-min` | `min-block-size: min-content;` |
| `min-block-max` | `min-block-size: max-content;` |
| `min-block-fit` | `min-block-size: fit-content;` |
| `min-block-lh` | `min-block-size: 1lh;` |
| `min-block-(<custom-property>)` | `min-block-size: var(<custom-property>);` |
| `min-block-[<value>]` | `min-block-size: <value>;` |

## Examples

### Basic example

Use `min-block-<number>` utilities like `min-block-24` and `min-block-64` to set an element to a fixed minimum block size based on the spacing scale:

  {
    <div className="mx-auto flex justify-center">
      <div className="relative flex items-end space-x-4 font-mono text-xs font-bold text-white">
        
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-blue-500 block-96">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-96</div>
        </div>
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-blue-500 block-80">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-80</div>
        </div>
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-blue-500 block-64">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-64</div>
        </div>
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-blue-500 block-48">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-48</div>
        </div>
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-blue-500 block-40">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-40</div>
        </div>
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-blue-500 block-32">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-32</div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:min-block-80,min-block-64,min-block-48,min-block-40,min-block-32,min-block-24] -->
<div class="block-20 ...">
  <div class="min-block-80 ...">min-block-80</div>
  <div class="min-block-64 ...">min-block-64</div>
  <div class="min-block-48 ...">min-block-48</div>
  <div class="min-block-40 ...">min-block-40</div>
  <div class="min-block-32 ...">min-block-32</div>
</div>
```

### Using a percentage

Use `min-block-full` or `min-block-<fraction>` utilities like `min-block-1/2`, and `min-block-2/5` to give an element a percentage-based minimum block size:

  {
    <div className="flex items-end justify-center space-x-4 font-mono text-xs font-bold text-white block-96">
      <div className="relative flex items-end block-full">
        
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-sky-500 min-block-full">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-full</div>
        </div>
      </div>
      <div className="relative flex items-end block-full">
        
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-sky-500 min-block-9/10">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-9/10</div>
        </div>
      </div>
      <div className="relative flex items-end block-full">
        
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-sky-500 min-block-3/4">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-3/4</div>
        </div>
      </div>
      <div className="relative flex items-end block-full">
        
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-sky-500 min-block-1/2">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-1/2</div>
        </div>
      </div>
      <div className="relative flex items-end block-full">
        
        <div className="relative flex w-8 items-end justify-center rounded-lg bg-sky-500 min-block-1/3">
          <div className="mb-1 transform-[rotate(-90deg)_translate(50%)] text-left text-nowrap">min-block-1/3</div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:min-block-9/10,min-block-3/4,min-block-1/2,min-block-1/3,min-block-full] -->
<div class="min-block-full ...">min-block-full</div>
<div class="min-block-9/10 ...">min-block-9/10</div>
<div class="min-block-3/4 ...">min-block-3/4</div>
<div class="min-block-1/2 ...">min-block-1/2</div>
<div class="min-block-1/3 ...">min-block-1/3</div>
```

### Using a custom value

### Responsive design

## Customizing your theme
