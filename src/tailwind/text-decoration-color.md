---
title: text-decoration-color
description: Utilities for controlling the color of text decorations.
source_url: https://tailwindcss.com/docs/text-decoration-color
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: text-decoration-color.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1660
---

CustomizingYourThemeColors,
  ResponsiveDesign,
  TargetingSpecificStates,
  UsingACustomValue,
} from "@/components/content.tsx";

| Clase | Propiedades CSS |
| :--- | :--- |
| `decoration-inherit` | `text-decoration-color: inherit;` |
| `decoration-current` | `text-decoration-color: currentColor;` |
| `decoration-transparent` | `text-decoration-color: transparent;` |
| `decoration-(<custom-property>)` | `text-decoration-color: var(<custom-property>);` |
| `decoration-[<value>]` | `text-decoration-color: <value>;` |

## Examples

### Basic example

Use utilities like `decoration-sky-500` and `decoration-pink-500` to change the [text decoration](/docs/text-decoration-line) color of an element:

  {
    <p className="mx-auto max-w-sm gap-4 p-8 text-sm/6 text-gray-900 dark:text-gray-200">
      I’m Derek, an astro-engineer based in Tattooine. I like to build X-Wings at{" "}
      <a href="#" className="font-bold underline decoration-sky-500 decoration-2 dark:text-gray-200">
        My Company, Inc
      </a>
      . Outside of work, I like to{" "}
      <a href="#" className="font-bold underline decoration-pink-500 decoration-2 dark:text-gray-200">
        watch pod-racing
      </a>{" "}
      and have{" "}
      <a href="#" className="font-bold underline decoration-indigo-500 decoration-2 dark:text-gray-200">
        light-saber
      </a>{" "}
      fights.
    </p>
  }

```html
<!-- [!code classes:decoration-sky-500,decoration-pink-500,decoration-indigo-500] -->
<!-- prettier-ignore -->
<p>
  I’m Derek, an astro-engineer based in Tattooine. I like to build X-Wings
  at <a class="underline decoration-sky-500">My Company, Inc</a>. Outside
  of work, I like to <a class="underline decoration-pink-500">watch pod-racing</a>
  and have <a class="underline decoration-indigo-500">light-saber</a> fights.
</p>
```

### Changing the opacity

Use the color opacity modifier to control the text decoration color opacity of an element:

  {
    <p className="mx-auto max-w-sm gap-4 p-8 text-sm/6 text-gray-900 dark:text-gray-200">
      I’m Derek, an astro-engineer based in Tattooine. I like to build X-Wings at{" "}
      <a href="#" className="font-bold underline decoration-sky-500/30 decoration-2 dark:text-gray-200">
        My Company, Inc
      </a>
      . Outside of work, I like to{" "}
      <a href="#" className="font-bold underline decoration-pink-500/30 decoration-2 dark:text-gray-200">
        watch pod-racing
      </a>{" "}
      and have{" "}
      <a href="#" className="font-bold underline decoration-indigo-500/30 decoration-2 dark:text-gray-200">
        light-saber
      </a>{" "}
      fights.
    </p>
  }

```html
<!-- [!code word:\/30] -->
<!-- prettier-ignore -->
<p>
  I’m Derek, an astro-engineer based in Tattooine. I like to build X-Wings
  at <a class="underline decoration-sky-500/30">My Company, Inc</a>. Outside
  of work, I like to <a class="underline decoration-pink-500/30">watch pod-racing</a>
  and have <a class="underline decoration-indigo-500/30">light-saber</a> fights.
</p>
```

### Using a custom value

### Applying on hover

  {
    <div className="text-center text-lg font-medium text-gray-900 no-underline dark:text-gray-200">
      The{" "}
      <a
        href="https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog"
        target="blank"
        className="underline hover:decoration-pink-500"
      >
        quick brown fox
      </a>{" "}
      jumps over the lazy dog.
    </div>
  }

```html
<!-- [!code classes:hover:decoration-pink-500] -->
<p>The <a href="..." class="underline hover:decoration-pink-500 ...">quick brown fox</a> jumps over the lazy dog.</p>
```

### Responsive design

## Customizing your theme
