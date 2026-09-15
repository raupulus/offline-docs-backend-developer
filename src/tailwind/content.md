---
title: content
description: Utilities for controlling the content of the before and after pseudo-elements.
source_url: https://tailwindcss.com/docs/content
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: content.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 500
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `content-[<value>]` | `content: <value>;` |
| `content-(<custom-property>)` | `content: var(<custom-property>);` |
| `content-none` | `content: none;` |

## Examples

### Basic example

Use the `content-[<value>]` syntax, along with the `before` and `after` variants, to set the contents of the `::before` and `::after` pseudo-elements:

  {
    <div className="mx-auto w-full max-w-md text-gray-500 dark:text-gray-400">
      Higher resolution means more than just a better-quality image. With a Retina 6K display,{" "}
      <a
        href="https://www.apple.com/pro-display-xdr/"
        className="font-medium text-blue-600 after:text-sm after:font-bold after:content-['_↗'] dark:text-sky-400"
        target="_blank"
      >
        Pro Display XDR
      </a>{" "}
      gives you nearly 40 percent more screen real estate than a 5K display.
    </div>
  }

```html
<!-- [!code classes:after:content-['_↗']] -->
<!-- prettier-ignore -->
<p>Higher resolution means more than just a better-quality image. With a
Retina 6K display, <a class="text-blue-600 after:content-['_↗']" href="...">
Pro Display XDR</a> gives you nearly 40 percent more screen real estate than
a 5K display.</p>
```

### Referencing an attribute value

Use the `content-[attr(<name>)]` syntax to reference a value stored in an attribute using the `attr()` CSS function:

  {
    <p
      before="Hello World"
      className="text-center font-semibold text-gray-900 before:content-[attr(before)] dark:text-gray-200"
    />
  }

```html
<!-- [!code classes:before:content-[attr(before)]] -->
<p before="Hello World" class="before:content-[attr(before)] ...">
  <!-- ... -->
</p>
```

### Using spaces and underscores

Since whitespace denotes the end of a class in HTML, replace any spaces in an arbitrary value with an underscore:

  {<p className="text-center font-semibold text-gray-900 before:content-['Hello_World'] dark:text-gray-200" />}

```html
<!-- [!code classes:before:content-['Hello_World']] -->
<p class="before:content-['Hello_World'] ..."></p>
```

If you need to include an actual underscore, you can do this by escaping it with a backslash:

  {<p className="text-center font-semibold text-gray-900 before:content-['Hello\_World'] dark:text-gray-200" />}

```html
<!-- [!code classes:before:content-['Hello\_World']] -->
<p class="before:content-['Hello\_World']"></p>
```

### Using a CSS variable

Use the <code>content-{'(<custom-property>)'}</code> syntax to control the contents of the `::before` and `::after` pseudo-elements using a CSS variable:

```html
<!-- [!code classes:content-(--my-content)] -->
<p class="content-(--my-content)"></p>
```

This is just a shorthand for <code>content-{'[var(<custom-property>)]'}</code> that adds the `var()` function for you automatically.

### Responsive design

```html
<!-- [!code classes:md:before:content-['Desktop']] -->
<p class="before:content-['Mobile'] md:before:content-['Desktop'] ..."></p>
```
