---
title: padding
source_url: https://tailwindcss.com/docs/padding
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: padding.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1370
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `p-<number>` | `padding: calc(var(--spacing) * <number>);` |
| `p-px` | `padding: 1px;` |
| `p-(<custom-property>)` | `padding: var(<custom-property>);` |
| `p-[<value>]` | `padding: <value>;` |
| `px-<number>` | `padding-inline: calc(var(--spacing) * <number>);` |
| `px-px` | `padding-inline: 1px;` |
| `px-(<custom-property>)` | `padding-inline: var(<custom-property>);` |
| `px-[<value>]` | `padding-inline: <value>;` |
| `py-<number>` | `padding-block: calc(var(--spacing) * <number>);` |
| `py-px` | `padding-block: 1px;` |
| `py-(<custom-property>)` | `padding-block: var(<custom-property>);` |
| `py-[<value>]` | `padding-block: <value>;` |
| `ps-<number>` | `padding-inline-start: calc(var(--spacing) * <number>);` |
| `ps-px` | `padding-inline-start: 1px;` |
| `ps-(<custom-property>)` | `padding-inline-start: var(<custom-property>);` |
| `ps-[<value>]` | `padding-inline-start: <value>;` |
| `pe-<number>` | `padding-inline-end: calc(var(--spacing) * <number>);` |
| `pe-px` | `padding-inline-end: 1px;` |
| `pe-(<custom-property>)` | `padding-inline-end: var(<custom-property>);` |
| `pe-[<value>]` | `padding-inline-end: <value>;` |
| `pbs-<number>` | `padding-block-start: calc(var(--spacing) * <number>);` |
| `pbs-px` | `padding-block-start: 1px;` |
| `pbs-(<custom-property>)` | `padding-block-start: var(<custom-property>);` |
| `pbs-[<value>]` | `padding-block-start: <value>;` |
| `pbe-<number>` | `padding-block-end: calc(var(--spacing) * <number>);` |
| `pbe-px` | `padding-block-end: 1px;` |
| `pbe-(<custom-property>)` | `padding-block-end: var(<custom-property>);` |
| `pbe-[<value>]` | `padding-block-end: <value>;` |
| `pt-<number>` | `padding-top: calc(var(--spacing) * <number>);` |
| `pt-px` | `padding-top: 1px;` |
| `pt-(<custom-property>)` | `padding-top: var(<custom-property>);` |
| `pt-[<value>]` | `padding-top: <value>;` |
| `pr-<number>` | `padding-right: calc(var(--spacing) * <number>);` |
| `pr-px` | `padding-right: 1px;` |
| `pr-(<custom-property>)` | `padding-right: var(<custom-property>);` |
| `pr-[<value>]` | `padding-right: <value>;` |
| `pb-<number>` | `padding-bottom: calc(var(--spacing) * <number>);` |
| `pb-px` | `padding-bottom: 1px;` |
| `pb-(<custom-property>)` | `padding-bottom: var(<custom-property>);` |
| `pb-[<value>]` | `padding-bottom: <value>;` |
| `pl-<number>` | `padding-left: calc(var(--spacing) * <number>);` |
| `pl-px` | `padding-left: 1px;` |
| `pl-(<custom-property>)` | `padding-left: var(<custom-property>);` |
| `pl-[<value>]` | `padding-left: <value>;` |

## Examples

### Basic example

Use `p-<number>` utilities like `p-4` and `p-8` to control the padding on all sides of an element:

  {
    <div className="flex justify-center font-mono text-sm leading-6 font-bold text-white">
      <div className="relative rounded-lg bg-violet-500 p-8">
        
        <div className="relative bg-violet-500 p-4">p-8</div>
      </div>
    </div>
  }

```html
<!-- [!code classes:p-8] -->
<div class="p-8 ...">p-8</div>
```

### Adding padding to one side

Use `pt-<number>`, `pr-<number>`, `pb-<number>`, and `pl-<number>` utilities like `pt-6` and `pr-4` to control the padding on one side of an element:

  {
    <div className="-mx-5 flex flex-wrap items-start justify-center font-mono text-sm leading-6 font-bold text-white">
      <div className="flex items-start">
        <div className="flex-none px-5">
          <div className="overflow-hidden rounded-lg bg-purple-500">
            
            <div className="p-4">pt-6</div>
          </div>
        </div>
        <div className="flex-none px-5 pt-6">
          <div className="flex overflow-hidden rounded-lg bg-purple-500">
            <div className="flex-none p-4">pr-4</div>
            
          </div>
        </div>
      </div>
      <div className="flex items-start">
        <div className="flex-none px-5 pt-6">
          <div className="overflow-hidden rounded-lg bg-purple-500">
            <div className="p-4">pb-8</div>
            
          </div>
        </div>
        <div className="flex-none px-5 pt-6">
          <div className="flex overflow-hidden rounded-lg bg-purple-500">
            
            <div className="flex-none p-4">pl-2</div>
          </div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:pt-6,pr-4,pb-8,pl-2] -->
<div class="pt-6 ...">pt-6</div>
<div class="pr-4 ...">pr-4</div>
<div class="pb-8 ...">pb-8</div>
<div class="pl-2 ...">pl-2</div>
```

### Adding horizontal padding

Use `px-<number>` utilities like `px-4` and `px-8` to control the horizontal padding of an element:

  {
    <div className="flex justify-center font-mono text-sm leading-6 font-bold text-white">
      <div className="flex overflow-hidden rounded-lg bg-indigo-500">
        
        <div className="p-4">px-8</div>
        
      </div>
    </div>
  }

```html
<!-- [!code classes:px-8] -->
<div class="px-8 ...">px-8</div>
```

### Adding vertical padding

Use `py-<number>` utilities like `py-4` and `py-8` to control the vertical padding of an element:

  {
    <div className="flex justify-center font-mono text-sm leading-6 font-bold text-white">
      <div className="overflow-hidden rounded-lg bg-pink-500">
        
        <div className="p-4">py-8</div>
        
      </div>
    </div>
  }

```html
<!-- [!code classes:py-8] -->
<div class="py-8 ...">py-8</div>
```

### Using logical properties

Use `ps-<number>` or `pe-<number>` utilities like `ps-4` and `pe-8` to set the `padding-inline-start` and `padding-inline-end` logical properties, which map to either the left or right side based on the text direction:

  {
    <div className="grid grid-cols-2 place-items-center gap-x-4">
      <div className="flex flex-col items-start gap-y-4">
        <p className="text-sm font-medium">Left-to-right</p>
        <div className="flex overflow-hidden rounded-lg bg-indigo-500 font-mono text-sm leading-6 font-bold text-white">
          
          <div className="p-4">ps-8</div>
        </div>
        <div className="mt-4 flex overflow-hidden rounded-lg bg-indigo-500 font-mono text-sm leading-6 font-bold text-white">
          <div className="p-4">pe-8</div>
          
        </div>
      </div>
      <div className="flex flex-col items-end gap-y-4">
        <p className="text-sm font-medium">Right-to-left</p>
        <div className="flex overflow-hidden rounded-lg bg-indigo-500 font-mono text-sm leading-6 font-bold text-white">
          <div className="p-4">ps-8</div>
          
        </div>
        <div className="mt-4 flex overflow-hidden rounded-lg bg-indigo-500 font-mono text-sm leading-6 font-bold text-white">
          
          <div className="p-4">pe-8</div>
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:ps-8,pe-8] -->
<!-- [!code word:dir="ltr"] -->
<!-- [!code word:dir="rtl"] -->
<div>
  <div dir="ltr">
    <div class="ps-8 ...">ps-8</div>
    <div class="pe-8 ...">pe-8</div>
  </div>
  <div dir="rtl">
    <div class="ps-8 ...">ps-8</div>
    <div class="pe-8 ...">pe-8</div>
  </div>
</div>
```

For more control, you can also use the [LTR and RTL modifiers](/docs/hover-focus-and-other-states#rtl-support) to conditionally apply specific styles depending on the current text direction.

Use the `pbs-<number>` and `pbe-<number>` utilities to set the `padding-block-start` and `padding-block-end` logical properties, which map to either the top or bottom side based on the writing mode:

```html
<!-- [!code classes:pbs-8] -->
<div class="pbs-8 ...">pbs-8</div>
```

### Using a custom value

### Responsive design

## Customizing your theme
