---
title: 'Error: fileName'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/error/filename/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 3970
---

{{Non-standard_Header}}

The **`fileName`** data property of an {{jsxref("Error")}} instance contains the path to the file that raised this error.

## Value

A string.

{{js_property_attributes(1, 0, 1)}}

## Description

This non-standard property contains the path to the file that raised this error. If called from a debugger context, the Firefox Developer Tools for example, "debugger eval code" is returned.

## Examples

### Using fileName

```js
const e = new Error("Could not parse input");
throw e;
// e.fileName could look like "file:///C:/example.html"
```

## Specifications

Not part of any standard.

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Error.prototype.stack")}}
- {{jsxref("Error.prototype.columnNumber")}}
- {{jsxref("Error.prototype.lineNumber")}}
