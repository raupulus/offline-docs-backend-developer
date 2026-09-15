---
title: forced-color-adjust
description: Utilities for opting in and out of forced colors.
source_url: https://tailwindcss.com/docs/forced-color-adjust
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: forced-color-adjust.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 830
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `forced-color-adjust-auto` | `forced-color-adjust: auto;` |
| `forced-color-adjust-none` | `forced-color-adjust: none;` |

## Examples

### Opting out of forced colors

Use the `forced-color-adjust-none` utility to opt an element out of the colors enforced by forced colors mode. This is useful in situations where enforcing a limited color palette will degrade usability.

  {
    <div className="mx-auto max-w-sm overflow-clip rounded-lg border border-transparent bg-white shadow dark:border-white/10 dark:bg-white/5">
      <div className="aspect-h-3 aspect-w-3 overflow-hidden">
        
      </div>
      <div className="grid grid-cols-[1fr_auto] items-center gap-4 p-4">
        <div>
          <p className="font-medium text-gray-900 dark:text-white">Basic Tee</p>
          <p className="text-sm font-medium text-gray-900 dark:text-white">$35</p>
        </div>
        <fieldset>
          <legend className="sr-only">Choose a color</legend>
          <div className="grid grid-flow-col items-center gap-3 forced-color-adjust-none">
            <label className="relative -m-0.5 flex cursor-pointer items-center justify-center rounded-full p-0.5 ring-0 focus:outline-none has-checked:ring-1 has-checked:ring-gray-400 has-checked:ring-offset-1">
              <input
                type="radio"
                name="color-choice"
                value="White"
                className="sr-only"
                aria-labelledby="color-choice-0-label"
              />
              <span id="color-choice-0-label" className="sr-only">
                White
              </span>
              <span
                aria-hidden="true"
                className="size-6 rounded-full border border-black/10 bg-white dark:border-white/10"
              ></span>
            </label>
            <label className="relative -m-0.5 flex cursor-pointer items-center justify-center rounded-full p-0.5 ring-0 focus:outline-none has-checked:ring-1 has-checked:ring-gray-400 has-checked:ring-offset-1">
              <input type="radio" defaultChecked name="color-choice" value="Gray" className="sr-only" />
              <span id="color-choice-1-label" className="sr-only">
                Gray
              </span>
              <span
                aria-hidden="true"
                className="size-6 rounded-full border border-black/10 bg-gray-200 dark:border-white/10"
              ></span>
            </label>
            <label className="relative -m-0.5 flex cursor-pointer items-center justify-center rounded-full p-0.5 ring-0 focus:outline-none has-checked:ring-1 has-checked:ring-gray-900 has-checked:ring-offset-1">
              <input
                type="radio"
                name="color-choice"
                value="Black"
                className="sr-only"
                aria-labelledby="color-choice-2-label"
              />
              <span id="color-choice-2-label" className="sr-only">
                Black
              </span>
              <span
                aria-hidden="true"
                className="size-6 rounded-full border border-black/10 bg-gray-900 dark:border-white/10"
              ></span>
            </label>
          </div>
        </fieldset>
      </div>
    </div>
  }

```html
<!-- [!code classes:forced-color-adjust-none] -->
<form>
  <img src="/img/shirt.jpg" />
  <div>
    <h3>Basic Tee</h3>
    <h3>$35</h3>
    <fieldset>
      <legend class="sr-only">Choose a color</legend>
      <div class="forced-color-adjust-none ...">
        <label>
          <input class="sr-only" type="radio" name="color-choice" value="White" />
          <span class="sr-only">White</span>
          <span class="size-6 rounded-full border border-black/10 bg-white"></span>
        </label>
        <!-- ... -->
      </div>
    </fieldset>
  </div>
</form>
```

You can also use the [forced colors variant](/docs/hover-focus-and-other-states#forced-colors) to conditionally add styles when the user has enabled a forced color mode.

### Restoring forced colors

Use the `forced-color-adjust-auto` utility to make an element adhere to colors enforced by forced colors mode:

```html
<!-- [!code classes:lg:forced-color-adjust-auto] -->
<form>
  <fieldset class="forced-color-adjust-none lg:forced-color-adjust-auto ...">
    <legend>Choose a color:</legend>
    <select class="hidden lg:block">
      <option value="White">White</option>
      <option value="Gray">Gray</option>
      <option value="Black">Black</option>
    </select>
    <div class="lg:hidden">
      <label>
        <input class="sr-only" type="radio" name="color-choice" value="White" />
        <!-- ... -->
      </label>
      <!-- ... -->
    </div>
  </fieldset>
</form>
```

This can be useful if you want to undo the `forced-color-adjust-none` utility, for example on a larger screen size.

### Responsive design
