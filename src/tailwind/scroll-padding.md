---
title: scroll-padding
source_url: https://tailwindcss.com/docs/scroll-padding
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: scroll-padding.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1520
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `scroll-p-<number>` | `scroll-padding: calc(var(--spacing) * <number>);` |
| `scroll-p-px` | `scroll-padding: 1px;` |
| `scroll-p-(<custom-property>)` | `scroll-padding: var(<custom-property>);` |
| `scroll-p-[<value>]` | `scroll-padding: <value>;` |
| `scroll-px-<number>` | `scroll-padding-inline: calc(var(--spacing) * <number>);` |
| `scroll-px-px` | `scroll-padding-inline: 1px;` |
| `scroll-px-(<custom-property>)` | `scroll-padding-inline: var(<custom-property>);` |
| `scroll-px-[<value>]` | `scroll-padding-inline: <value>;` |
| `scroll-py-<number>` | `scroll-padding-block: calc(var(--spacing) * <number>);` |
| `scroll-py-px` | `scroll-padding-block: 1px;` |
| `scroll-py-(<custom-property>)` | `scroll-padding-block: var(<custom-property>);` |
| `scroll-py-[<value>]` | `scroll-padding-block: <value>;` |
| `scroll-ps-<number>` | `scroll-padding-inline-start: calc(var(--spacing) * <number>);` |
| `scroll-ps-px` | `scroll-padding-inline-start: 1px;` |
| `scroll-ps-(<custom-property>)` | `scroll-padding-inline-start: var(<custom-property>);` |
| `scroll-ps-[<value>]` | `scroll-padding-inline-start: <value>;` |
| `scroll-pe-<number>` | `scroll-padding-inline-end: calc(var(--spacing) * <number>);` |
| `scroll-pe-px` | `scroll-padding-inline-end: 1px;` |
| `scroll-pe-(<custom-property>)` | `scroll-padding-inline-end: var(<custom-property>);` |
| `scroll-pe-[<value>]` | `scroll-padding-inline-end: <value>;` |
| `scroll-pbs-<number>` | `scroll-padding-block-start: calc(var(--spacing) * <number>);` |
| `scroll-pbs-px` | `scroll-padding-block-start: 1px;` |
| `scroll-pbs-(<custom-property>)` | `scroll-padding-block-start: var(<custom-property>);` |
| `scroll-pbs-[<value>]` | `scroll-padding-block-start: <value>;` |
| `scroll-pbe-<number>` | `scroll-padding-block-end: calc(var(--spacing) * <number>);` |
| `scroll-pbe-px` | `scroll-padding-block-end: 1px;` |
| `scroll-pbe-(<custom-property>)` | `scroll-padding-block-end: var(<custom-property>);` |
| `scroll-pbe-[<value>]` | `scroll-padding-block-end: <value>;` |
| `scroll-pt-<number>` | `scroll-padding-top: calc(var(--spacing) * <number>);` |
| `scroll-pt-px` | `scroll-padding-top: 1px;` |
| `scroll-pt-(<custom-property>)` | `scroll-padding-top: var(<custom-property>);` |
| `scroll-pt-[<value>]` | `scroll-padding-top: <value>;` |
| `scroll-pr-<number>` | `scroll-padding-right: calc(var(--spacing) * <number>);` |
| `scroll-pr-px` | `scroll-padding-right: 1px;` |
| `scroll-pr-(<custom-property>)` | `scroll-padding-right: var(<custom-property>);` |
| `scroll-pr-[<value>]` | `scroll-padding-right: <value>;` |
| `scroll-pb-<number>` | `scroll-padding-bottom: calc(var(--spacing) * <number>);` |
| `scroll-pb-px` | `scroll-padding-bottom: 1px;` |
| `scroll-pb-(<custom-property>)` | `scroll-padding-bottom: var(<custom-property>);` |
| `scroll-pb-[<value>]` | `scroll-padding-bottom: <value>;` |
| `scroll-pl-<number>` | `scroll-padding-left: calc(var(--spacing) * <number>);` |
| `scroll-pl-px` | `scroll-padding-left: 1px;` |
| `scroll-pl-(<custom-property>)` | `scroll-padding-left: var(<custom-property>);` |
| `scroll-pl-[<value>]` | `scroll-padding-left: <value>;` |

## Examples

### Basic example

Use the `scroll-pt-<number>`, `scroll-pr-<number>`, `scroll-pb-<number>`, and `scroll-pl-<number>` utilities like `scroll-pl-4` and `scroll-pt-6` to set the scroll offset of an element within a snap container:

  {
    <div className="relative">
      
      <div className="flex w-full snap-x scroll-pl-6 gap-8 overflow-x-auto py-14">
        <div className="shrink-0 snap-start first:pl-6 last:pr-[calc(100%-21.5rem)]">
          <img
            className="h-40 w-80 shrink-0 rounded-lg bg-white"
            src="https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
          />
        </div>
        <div className="shrink-0 snap-start first:pl-6 last:pr-[calc(100%-21.5rem)]">
          <img
            className="h-40 w-80 shrink-0 rounded-lg bg-white"
            src="https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
          />
        </div>
        <div className="shrink-0 snap-start first:pl-6 last:pr-[calc(100%-21.5rem)]">
          <img
            className="h-40 w-80 shrink-0 rounded-lg bg-white"
            src="https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
          />
        </div>
        <div className="shrink-0 snap-start first:pl-6 last:pr-[calc(100%-21.5rem)]">
          <img
            className="h-40 w-80 shrink-0 rounded-lg bg-white"
            src="https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
          />
        </div>
        <div className="shrink-0 snap-start first:pl-6 last:pr-[calc(100%-21.5rem)]">
          <img
            className="h-40 w-80 shrink-0 rounded-lg bg-white"
            src="https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
          />
        </div>
      </div>
    </div>
  }

```html
<!-- [!code classes:scroll-pl-6] -->
<div class="snap-x scroll-pl-6 ...">
  <div class="snap-start ...">
    <img src="/img/vacation-01.jpg" />
  </div>
  <div class="snap-start ...">
    <img src="/img/vacation-02.jpg" />
  </div>
  <div class="snap-start ...">
    <img src="/img/vacation-03.jpg" />
  </div>
  <div class="snap-start ...">
    <img src="/img/vacation-04.jpg" />
  </div>
  <div class="snap-start ...">
    <img src="/img/vacation-05.jpg" />
  </div>
</div>
```

### Using logical properties

Use the `scroll-ps-<number>` and `scroll-pe-<number>` utilities to set the `scroll-padding-inline-start` and `scroll-padding-inline-end` logical properties, which map to either the left or right side based on the text direction:

  {
    <>
      <p className="mb-4 pt-8 pl-6 text-sm font-medium">Left-to-right</p>
      <div className="relative" dir="ltr">
        
        <div className="flex w-full snap-x scroll-ps-6 gap-8 overflow-x-auto pb-10">
          <div className="shrink-0 snap-start first:ps-6 last:pe-[calc(100%-21.5rem)]">
            <img
              className="h-40 w-80 shrink-0 rounded-lg bg-white"
              src="https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
            />
          </div>
          <div className="shrink-0 snap-start first:ps-6 last:pe-[calc(100%-21.5rem)]">
            <img
              className="h-40 w-80 shrink-0 rounded-lg bg-white"
              src="https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
            />
          </div>
          <div className="shrink-0 snap-start first:ps-6 last:pe-[calc(100%-21.5rem)]">
            <img
              className="h-40 w-80 shrink-0 rounded-lg bg-white"
              src="https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
            />
          </div>
          <div className="shrink-0 snap-start first:ps-6 last:pe-[calc(100%-21.5rem)]">
            <img
              className="h-40 w-80 shrink-0 rounded-lg bg-white"
              src="https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
            />
          </div>
          <div className="shrink-0 snap-start first:ps-6 last:pe-[calc(100%-21.5rem)]">
            <img
              className="h-40 w-80 shrink-0 rounded-lg bg-white"
              src="https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
            />
          </div>
        </div>
      </div>
      <p className="mt-4 mb-4 pl-6 text-sm font-medium">Right-to-left</p>
      <div className="relative" dir="rtl">
        
        <div className="flex w-full snap-x scroll-ps-6 gap-8 overflow-x-auto pb-10">
          <div className="shrink-0 snap-start first:ps-6 last:pe-[calc(100%-21.5rem)]">
            <img
              className="h-40 w-80 shrink-0 rounded-lg bg-white"
              src="https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
            />
          </div>
          <div className="shrink-0 snap-start first:ps-6 last:pe-[calc(100%-21.5rem)]">
            <img
              className="h-40 w-80 shrink-0 rounded-lg bg-white"
              src="https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
            />
          </div>
          <div className="shrink-0 snap-start first:ps-6 last:pe-[calc(100%-21.5rem)]">
            <img
              className="h-40 w-80 shrink-0 rounded-lg bg-white"
              src="https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
            />
          </div>
          <div className="shrink-0 snap-start first:ps-6 last:pe-[calc(100%-21.5rem)]">
            <img
              className="h-40 w-80 shrink-0 rounded-lg bg-white"
              src="https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
            />
          </div>
          <div className="shrink-0 snap-start first:ps-6 last:pe-[calc(100%-21.5rem)]">
            <img
              className="h-40 w-80 shrink-0 rounded-lg bg-white"
              src="https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80"
            />
          </div>
        </div>
      </div>
    </>
  }

```html
<!-- [!code word:dir="ltr"] -->
<!-- [!code word:dir="rtl"] -->
<!-- [!code classes:scroll-ps-6] -->
<div dir="ltr">
  <div class="snap-x scroll-ps-6 ...">
    <!-- ... -->
  </div>
</div>

<div dir="rtl">
  <div class="snap-x scroll-ps-6 ...">
    <!-- ... -->
  </div>
</div>
```

Use the `scroll-pbs-<number>` and `scroll-pbe-<number>` utilities to set the `scroll-padding-block-start` and `scroll-padding-block-end` logical properties, which map to either the top or bottom side based on the writing mode:

```html
<!-- [!code classes:scroll-pbs-6] -->
<div class="snap-y scroll-pbs-6 ...">
  <!-- ... -->
</div>
```

### Using a custom value

### Responsive design

## Customizing your theme
