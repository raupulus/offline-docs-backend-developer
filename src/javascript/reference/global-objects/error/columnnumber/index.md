---
title: 'Error: columnNumber'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/error/columnnumber/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 3950
---

{{Non-standard_Header}}

The **`columnNumber`** data property of an {{jsxref("Error")}} instance contains the column number in the line of the file that raised this error.

## Value

A positive integer.

{{js_property_attributes(1, 0, 1)}}

## Examples

### Using columnNumber

```js
try {
  throw new Error("Could not parse input");
} catch (err) {
  console.log(err.columnNumber); // 9
}
```

## Specifications

Not part of any standard.

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Error.prototype.stack")}}
- {{jsxref("Error.prototype.lineNumber")}}
- {{jsxref("Error.prototype.fileName")}}
