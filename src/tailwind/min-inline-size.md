---
title: min-inline-size
description: Utilities for setting the minimum inline size of an element.
source_url: https://tailwindcss.com/docs/min-inline-size
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: min-inline-size.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1230
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `min-inline-<number>` | `min-inline-size: calc(var(--spacing) * <number>);` |
| `min-inline-<fraction>` | `min-inline-size: calc(<fraction> * 100%);` |
| `min-inline-3xs` | `min-inline-size: var(--container-3xs); /* 16rem (256px) */` |
| `min-inline-2xs` | `min-inline-size: var(--container-2xs); /* 18rem (288px) */` |
| `min-inline-xs` | `min-inline-size: var(--container-xs); /* 20rem (320px) */` |
| `min-inline-sm` | `min-inline-size: var(--container-sm); /* 24rem (384px) */` |
| `min-inline-md` | `min-inline-size: var(--container-md); /* 28rem (448px) */` |
| `min-inline-lg` | `min-inline-size: var(--container-lg); /* 32rem (512px) */` |
| `min-inline-xl` | `min-inline-size: var(--container-xl); /* 36rem (576px) */` |
| `min-inline-2xl` | `min-inline-size: var(--container-2xl); /* 42rem (672px) */` |
| `min-inline-3xl` | `min-inline-size: var(--container-3xl); /* 48rem (768px) */` |
| `min-inline-4xl` | `min-inline-size: var(--container-4xl); /* 56rem (896px) */` |
| `min-inline-5xl` | `min-inline-size: var(--container-5xl); /* 64rem (1024px) */` |
| `min-inline-6xl` | `min-inline-size: var(--container-6xl); /* 72rem (1152px) */` |
| `min-inline-7xl` | `min-inline-size: var(--container-7xl); /* 80rem (1280px) */` |
| `min-inline-auto` | `min-inline-size: auto;` |
| `min-inline-px` | `min-inline-size: 1px;` |
| `min-inline-full` | `min-inline-size: 100%;` |
| `min-inline-screen` | `min-inline-size: 100vw;` |
| `min-inline-dvw` | `min-inline-size: 100dvw;` |
| `min-inline-dvh` | `min-inline-size: 100dvh;` |
| `min-inline-lvw` | `min-inline-size: 100lvw;` |
| `min-inline-lvh` | `min-inline-size: 100lvh;` |
| `min-inline-svw` | `min-inline-size: 100svw;` |
| `min-inline-svh` | `min-inline-size: 100svh;` |
| `min-inline-min` | `min-inline-size: min-content;` |
| `min-inline-max` | `min-inline-size: max-content;` |
| `min-inline-fit` | `min-inline-size: fit-content;` |
| `min-inline-(<custom-property>)` | `min-inline-size: var(<custom-property>);` |
| `min-inline-[<value>]` | `min-inline-size: <value>;` |

## Examples

### Basic example

Use `min-inline-<number>` utilities like `min-inline-24` and `min-inline-64` to set an element to a fixed minimum inline size based on the spacing scale:

  {
    <div className="relative mx-auto grid w-60 justify-items-start gap-y-4 text-center font-mono text-xs font-bold text-white">
      
      <div className="relative rounded-lg bg-sky-500 px-4 py-2 min-inline-80">min-inline-80</div>
      <div className="relative rounded-lg bg-sky-500 px-4 py-2 min-inline-64">min-inline-64</div>
      <div className="relative rounded-lg bg-sky-500 px-4 py-2 min-inline-48">min-inline-48</div>
      <div className="relative rounded-lg bg-sky-500 px-4 py-2 min-inline-40">min-inline-40</div>
      <div className="relative rounded-lg bg-sky-500 px-4 py-2 min-inline-32">min-inline-32</div>
      <div className="relative rounded-lg bg-sky-500 px-4 py-2 min-inline-24">min-inline-24</div>
    </div>
  }

```html
<!-- [!code classes:min-inline-80,min-inline-64,min-inline-48,min-inline-40,min-inline-32,min-inline-24] -->
<div class="inline-20 ...">
  <div class="min-inline-80 ...">min-inline-80</div>
  <div class="min-inline-64 ...">min-inline-64</div>
  <div class="min-inline-48 ...">min-inline-48</div>
  <div class="min-inline-40 ...">min-inline-40</div>
  <div class="min-inline-32 ...">min-inline-32</div>
  <div class="min-inline-24 ...">min-inline-24</div>
</div>
```

### Using a percentage

Use `min-inline-full` or `min-inline-<fraction>` utilities like `min-inline-1/2` and `min-inline-2/5` to give an element a percentage-based minimum inline size:

  {
    <div className="relative mx-auto my-6 flex w-full justify-items-start gap-3 text-center font-mono text-xs font-bold text-white">
      
      <div className="relative rounded-lg bg-indigo-500 px-4 py-2 min-inline-2/3">min-inline-3/4</div>
      <div className="relative rounded-lg bg-indigo-300 px-4 py-2 inline-full dark:bg-indigo-800 dark:text-indigo-400">
        inline-full
      </div>
    </div>
  }

```html
<!-- [!code classes:min-inline-3/4] -->
<div class="flex ...">
  <div class="min-inline-3/4 ...">min-inline-3/4</div>
  <div class="inline-full ...">inline-full</div>
</div>
```

### Using the container scale

Use utilities like `min-inline-sm` and `min-inline-xl` to set an element to a fixed minimum inline size based on the container scale:

  {
    <div className="relative grid justify-items-start gap-y-4 text-center font-mono text-xs font-bold text-white">
      
      <div className="relative hidden rounded-lg bg-blue-500 px-4 py-2 min-inline-lg sm:block">min-inline-lg</div>
      <div className="relative hidden rounded-lg bg-blue-500 px-4 py-2 min-inline-md sm:block">min-inline-md</div>
      <div className="relative hidden rounded-lg bg-blue-500 px-4 py-2 min-inline-sm sm:block">min-inline-sm</div>
      <div className="relative rounded-lg bg-blue-500 px-4 py-2 min-inline-xs">min-inline-xs</div>
      <div className="relative rounded-lg bg-blue-500 px-4 py-2 min-inline-2xs">min-inline-2xs</div>
      <div className="relative rounded-lg bg-blue-500 px-4 py-2 min-inline-3xs">min-inline-3xs</div>
    </div>
  }

```html
<!-- [!code classes:min-inline-lg,min-inline-md,min-inline-sm,min-inline-xs,min-inline-2xs,min-inline-3xs] -->
<div class="inline-40 ...">
  <div class="min-inline-lg ...">min-inline-lg</div>
  <div class="min-inline-md ...">min-inline-md</div>
  <div class="min-inline-sm ...">min-inline-sm</div>
  <div class="min-inline-xs ...">min-inline-xs</div>
  <div class="min-inline-2xs ...">min-inline-2xs</div>
  <div class="min-inline-3xs ...">min-inline-3xs</div>
</div>
```

### Using a custom value

### Responsive design

## Customizing your theme
