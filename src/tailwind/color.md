---
title: color
description: Utilities for controlling the text color of an element.
source_url: https://tailwindcss.com/docs/color
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: color.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 460
---

CustomizingYourThemeColors,
  ResponsiveDesign,
  TargetingSpecificStates,
  UsingACustomValue,
} from "@/components/content.tsx";

| Clase | Propiedades CSS |
| :--- | :--- |
| `text-inherit` | `color: inherit;` |
| `text-current` | `color: currentColor;` |
| `text-transparent` | `color: transparent;` |
| `text-(<custom-property>)` | `color: var(<custom-property>);` |
| `text-[<value>]` | `color: <value>;` |
| `text-<value>` | `color: var(--color-<value>); /* <value> */` |

## Examples

### Basic example

Use utilities like `text-blue-600` and `text-sky-400` to control the text color of an element:

  {
    <div className="relative text-center text-xl leading-6 font-medium">
      <p className="text-blue-600 dark:text-sky-400">The quick brown fox jumps over the lazy dog.</p>
    </div>
  }

```html
<!-- [!code classes:text-blue-600,dark:text-sky-400] -->
<p class="text-blue-600 dark:text-sky-400">The quick brown fox...</p>
```

### Changing the opacity

Use the color opacity modifier to control the text color opacity of an element:

  {
    <div className="space-y-4 text-center text-xl leading-6 font-medium">
      <p className="text-blue-600/100 dark:text-sky-400/100">The quick brown fox jumps over the lazy dog.</p>
      <p className="text-blue-600/75 dark:text-sky-400/75">The quick brown fox jumps over the lazy dog.</p>
      <p className="text-blue-600/50 dark:text-sky-400/50">The quick brown fox jumps over the lazy dog.</p>
      <p className="text-blue-600/25 dark:text-sky-400/25">The quick brown fox jumps over the lazy dog.</p>
    </div>
  }

```html
<!-- [!code word:\/100] -->
<!-- [!code word:\/75] -->
<!-- [!code word:\/50] -->
<!-- [!code word:\/25] -->
<p class="text-blue-600/100 dark:text-sky-400/100">The quick brown fox...</p>
<p class="text-blue-600/75 dark:text-sky-400/75">The quick brown fox...</p>
<p class="text-blue-600/50 dark:text-sky-400/50">The quick brown fox...</p>
<p class="text-blue-600/25 dark:text-sky-400/25">The quick brown fox...</p>
```

### Using a custom value

### Applying on hover

  {
    <p className="text-center text-xl font-medium text-gray-900 dark:text-gray-200">
      Oh I gotta get on that{" "}
      <a
        href="https://en.wikipedia.org/wiki/Internet"
        target="_blank"
        className="underline hover:text-blue-600 dark:hover:text-blue-400"
      >
        internet
      </a>
      , I'm late on everything!
    </p>
  }

```html
<!-- [!code classes:hover:text-blue-600,dark:hover:text-blue-400] -->
<!-- prettier-ignore -->
<p class="...">
  Oh I gotta get on that
  <a class="underline hover:text-blue-600 dark:hover:text-blue-400" href="https://en.wikipedia.org/wiki/Internet">internet</a>,
  I'm late on everything!
</p>
```

### Responsive design

## Customizing your theme
