---
title: SharedArrayBuffer.prototype.byteLength
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/sharedarraybuffer/bytelength/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 7860
---

The **`byteLength`** accessor property of {{jsxref("SharedArrayBuffer")}} instances returns the length (in bytes) of this `SharedArrayBuffer`.

## Description

The `byteLength` property is an accessor property whose set accessor function is `undefined`, meaning that you can only read this property. The value is established when the shared array is constructed and cannot be changed.

## Examples

Note that these examples cannot be run directly from the console or an arbitrary web page, because `SharedArrayBuffer` is not defined unless its [security requirements](/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer#security_requirements) are met.

### Using byteLength

```js
const sab = new SharedArrayBuffer(1024);
sab.byteLength; // 1024
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("SharedArrayBuffer")}}
