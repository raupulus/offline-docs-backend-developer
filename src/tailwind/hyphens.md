---
title: hyphens
description: Utilities for controlling how words should be hyphenated.
source_url: https://tailwindcss.com/docs/hyphens
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: hyphens.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 950
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `hyphens-none` | `hyphens: none;` |
| `hyphens-manual` | `hyphens: manual;` |
| `hyphens-auto` | `hyphens: auto;` |

## Examples

### Preventing hyphenation

Use the `hyphens-none` utility to prevent words from being hyphenated even if the line break suggestion `&shy;` is used:

  {
    <p className="mx-auto max-w-xs border-x border-x-pink-400/30 py-8 break-normal hyphens-none text-gray-900 dark:text-gray-200">
      Officially recognized by the Duden dictionary as the longest word in German,{" "}
      <span className="font-bold" lang="de">
        Kraftfahrzeug&shy;haftpflichtversicherung
      </span>{" "}
      is a 36 letter word for motor vehicle liability insurance.
    </p>
  }

```html
<!-- [!code classes:hyphens-none] -->
<!-- [!code word:&shy;] -->
<!-- prettier-ignore -->
<p class="hyphens-none">
  ... Kraftfahrzeug&shy;haftpflichtversicherung is a ...
</p>
```

### Manual hyphenation

Use the `hyphens-manual` utility to only set hyphenation points where the line break suggestion `&shy;` is used:

  {
    <p className="mx-auto max-w-xs border-x border-x-pink-400/30 py-8 break-normal hyphens-manual text-gray-900 dark:text-gray-200">
      Officially recognized by the Duden dictionary as the longest word in German,{" "}
      <span className="font-bold" lang="de">
        Kraftfahrzeug&shy;haftpflichtversicherung
      </span>{" "}
      is a 36 letter word for motor vehicle liability insurance.
    </p>
  }

```html
<!-- [!code classes:hyphens-manual] -->
<!-- [!code word:&shy;] -->
<!-- prettier-ignore -->
<p class="hyphens-manual">
  ... Kraftfahrzeug&shy;haftpflichtversicherung is a ...
</p>
```

This is the default browser behavior.

### Automatic hyphenation

Use the `hyphens-auto` utility to allow the browser to automatically choose hyphenation points based on the language:

  {
    <p className="mx-auto max-w-xs border-x border-x-pink-400/30 py-8 break-normal hyphens-auto text-gray-900 dark:text-gray-200">
      Officially recognized by the Duden dictionary as the longest word in German,{" "}
      <span className="font-bold" lang="de">
        Kraftfahrzeughaftpflichtversicherung
      </span>{" "}
      is a 36 letter word for motor vehicle liability insurance.
    </p>
  }

```html
<!-- [!code classes:hyphens-auto] -->
<!-- [!code word:lang="de"] -->
<!-- prettier-ignore -->
<p class="hyphens-auto" lang="de">
  ... Kraftfahrzeughaftpflichtversicherung is a ...
</p>
```

The line break suggestion `&shy;` will be preferred over automatic hyphenation points.

### Responsive design
