---
title: 'Error: lineNumber'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/error/linenumber/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 4000
---

{{Non-standard_Header}}

The **`lineNumber`** data property of an {{jsxref("Error")}} instance contains the line number in the file that raised this error.

## Value

A positive integer.

{{js_property_attributes(1, 0, 1)}}

## Examples

### Using lineNumber

```js
try {
  throw new Error("Could not parse input");
} catch (err) {
  console.log(err.lineNumber); // 2
}
```

### Alternative example using error event

```js
window.addEventListener("error", (e) => {
  console.log(e.lineNumber); // 5
});
const e = new Error("Could not parse input");
throw e;
```

This is not a standard feature and lacks widespread support. See the browser compatibility table below.

## Specifications

Not part of any standard.

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Error.prototype.stack")}}
- {{jsxref("Error.prototype.columnNumber")}}
- {{jsxref("Error.prototype.fileName")}}
