---
title: white-space
source_url: https://tailwindcss.com/docs/white-space
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: white-space.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 1920
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `whitespace-normal` | `white-space: normal;` |
| `whitespace-nowrap` | `white-space: nowrap;` |
| `whitespace-pre` | `white-space: pre;` |
| `whitespace-pre-line` | `white-space: pre-line;` |
| `whitespace-pre-wrap` | `white-space: pre-wrap;` |
| `whitespace-break-spaces` | `white-space: break-spaces;` |

## Examples

### Normal

Use the `whitespace-normal` utility to cause text to wrap normally within an element. Newlines and spaces will be collapsed:

  {
    <div className="mx-auto max-w-sm border-x border-x-pink-400/30 py-8 text-gray-900 dark:text-gray-200">
      <p
        className="whitespace-normal"
        children={
          "Hey everyone!\n\nIt’s almost 2022       and we still don’t know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.\n\nYou will never know."
        }
      />
    </div>
  }

```html
<!-- [!code classes:whitespace-normal] -->
<!-- prettier-ignore -->
<p class="whitespace-normal">Hey everyone!

It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.

You will never know.</p>
```

### No Wrap

Use the `whitespace-nowrap` utility to prevent text from wrapping within an element. Newlines and spaces will be collapsed:

  {
    <div className="mx-auto max-w-sm border-x border-x-pink-400/30 py-8 text-gray-900 dark:text-gray-200">
      <p
        className="whitespace-nowrap"
        children={
          "Hey everyone!\n\nIt’s almost 2022       and we still don’t know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.\n\nYou will never know."
        }
      />
    </div>
  }

```html
<!-- [!code classes:whitespace-nowrap] -->
<!-- prettier-ignore -->
<p class="overflow-auto whitespace-nowrap">Hey everyone!

It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.

You will never know.</p>
```

### Pre

Use the `whitespace-pre` utility to preserve newlines and spaces within an element. Text will not be wrapped:

  {
    <div className="mx-auto max-w-sm border-x border-x-pink-400/30 py-8 text-gray-900 dark:text-gray-200">
      <p
        className="whitespace-pre"
        children={
          "Hey everyone!\n\nIt’s almost 2022       and we still don’t know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.\n\nYou will never know."
        }
      />
    </div>
  }

```html
<!-- [!code classes:whitespace-pre] -->
<!-- prettier-ignore -->
<p class="overflow-auto whitespace-pre">Hey everyone!

It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.

You will never know.</p>
```

### Pre Line

Use the `whitespace-pre-line` utility to preserve newlines but not spaces within an element. Text will be wrapped normally:

  {
    <div className="mx-auto max-w-sm border-x border-x-pink-400/30 py-8 text-gray-900 dark:text-gray-200">
      <p
        className="whitespace-pre-line"
        children={
          "Hey everyone!\n\nIt’s almost 2022       and we still don’t know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.\n\nYou will never know."
        }
      />
    </div>
  }

```html
<!-- [!code classes:whitespace-pre-line] -->
<!-- prettier-ignore -->
<p class="whitespace-pre-line">Hey everyone!

It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.

You will never know.</p>
```

### Pre Wrap

Use the `whitespace-pre-wrap` utility to preserve newlines and spaces within an element. Text will be wrapped normally:

  {
    <div className="mx-auto max-w-sm border-x border-x-pink-400/30 py-8 text-gray-900 dark:text-gray-200">
      <p
        className="whitespace-pre-wrap"
        children={
          "Hey everyone!\n\nIt’s almost 2022       and we still don’t know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.\n\nYou will never know."
        }
      />
    </div>
  }

{/* prettier-ignore */}
```html
<!-- [!code classes:whitespace-pre-wrap] -->
<!-- prettier-ignore -->
<p class="whitespace-pre-wrap">Hey everyone!

It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.

You will never know.</p>
```

### Break Spaces

Use the `whitespace-break-spaces` utility to preserve newlines and spaces within an element. White space at the end of lines will not hang, but will wrap to the next line:

  {
    <div className="mx-auto max-w-sm border-x border-x-pink-400/30 py-8 text-gray-900 dark:text-gray-200">
      <p
        className="whitespace-break-spaces"
        children={
          "Hey everyone!\n\nIt’s almost 2022       and we still don’t know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.\n\nYou will never know."
        }
      />
    </div>
  }

```html
<!-- [!code classes:whitespace-break-spaces] -->
<!-- prettier-ignore -->
<p class="whitespace-break-spaces">Hey everyone!

It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.

You will never know.</p>
```

### Responsive design
