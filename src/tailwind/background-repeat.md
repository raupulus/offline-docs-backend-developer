---
title: background-repeat
source_url: https://tailwindcss.com/docs/background-repeat
source_repo: tailwindlabs/tailwindcss.com
source_ref: main
source_commit: 7f92c2213
source_path: background-repeat.mdx
technology: tailwind
version: main
license: MIT
retrieved_at: '2026-09-15'
order: 270
---

| Clase | Propiedades CSS |
| :--- | :--- |
| `bg-repeat` | `background-repeat: repeat;` |
| `bg-repeat-x` | `background-repeat: repeat-x;` |
| `bg-repeat-y` | `background-repeat: repeat-y;` |
| `bg-repeat-space` | `background-repeat: space;` |
| `bg-repeat-round` | `background-repeat: round;` |
| `bg-no-repeat` | `background-repeat: no-repeat;` |

## Examples

### Basic example

Use the `bg-repeat` utility to repeat the background image both vertically and horizontally:

  {<div className="h-64 bg-center bg-repeat" style={{ backgroundImage: `url(${cloudsImg.src})` }}></div>}

```html
<!-- [!code classes:bg-repeat] -->
<div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat ..."></div>
```

### Repeating horizontally

Use the `bg-repeat-x` utility to only repeat the background image horizontally:

  {<div className="h-64 bg-center bg-repeat-x" style={{ backgroundImage: `url(${cloudsImg.src})` }}></div>}

```html
<!-- [!code classes:bg-repeat-x] -->
<div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-x ..."></div>
```

### Repeating vertically

Use the `bg-repeat-y` utility to only repeat the background image vertically:

  {<div className="h-64 bg-center bg-repeat-y" style={{ backgroundImage: `url(${cloudsImg.src})` }}></div>}

```html
<!-- [!code classes:bg-repeat-y] -->
<div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-y ..."></div>
```

### Preventing clipping

Use the `bg-repeat-space` utility to repeat the background image without clipping:

  {<div className="h-64 bg-center bg-repeat-space" style={{ backgroundImage: `url(${cloudsImg.src})` }}></div>}

```html
<!-- [!code classes:bg-repeat-space] -->
<div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-space ..."></div>
```

### Preventing clipping and gaps

Use the `bg-repeat-round` utility to repeat the background image without clipping, stretching if needed to avoid gaps:

  {<div className="h-64 bg-center bg-repeat-round" style={{ backgroundImage: `url(${cloudsImg.src})` }}></div>}

```html
<!-- [!code classes:bg-repeat-round] -->
<div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-round ..."></div>
```

### Disabling repeating

Use the `bg-no-repeat` utility to prevent a background image from repeating:

  {<div className="h-64 bg-center bg-no-repeat" style={{ backgroundImage: `url(${cloudsImg.src})` }}></div>}

```html
<!-- [!code classes:bg-no-repeat] -->
<div class="bg-[url(/img/clouds.svg)] bg-center bg-no-repeat ..."></div>
```

### Responsive design
