---
title: font-feature-settings
description: Utilities for controlling advanced typographic features.
source_url: https://tailwindcss.com/docs/font-feature-settings
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: font-feature-settings.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 760
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `font-features-[<value>]` | `font-feature-settings: <value>;` |
| `font-features-(<custom-property>)` | `font-feature-settings: var(<custom-property>);` |

## Examples

### Basic example

Use the `font-features-[<value>]` utility to enable OpenType features in fonts that support them:

```html
<!-- [!code classes:font-features-["smcp"]] -->
<p class="font-features-['smcp'] ...">This text uses small caps.</p>
```

### Enabling multiple features

You can enable multiple OpenType features by separating them with commas:

```html
<!-- [!code classes:font-features-["smcp","onum"]] -->
<p class="font-features-['smcp','onum'] ...">This text uses small caps and oldstyle numbers.</p>
```

### Using CSS variables

Use the `font-features-(<custom-property>)` syntax to apply font feature settings from a CSS variable:

```html
<!-- [!code classes:font-features-(--my-features)] -->
<p class="font-features-(--my-features) ...">
  <!-- ... -->
</p>
```

### Responsive design
