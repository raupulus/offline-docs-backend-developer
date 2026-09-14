---
title: ArrayBuffer.prototype.byteLength
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/arraybuffer/bytelength/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 2390
---

The **`byteLength`** accessor property of {{jsxref("ArrayBuffer")}} instances returns the length (in bytes) of this array buffer.

{{InteractiveExample("JavaScript Demo: ArrayBuffer.prototype.byteLength")}}

```js interactive-example
// Create an ArrayBuffer with a size in bytes
const buffer = new ArrayBuffer(8);

// Use byteLength to check the size
const bytes = buffer.byteLength;

console.log(bytes);
// Expected output: 8
```

## Description

The `byteLength` property is an accessor property whose set accessor function is `undefined`, meaning that you can only read this property. The value is established when the array is constructed and cannot be changed. This property returns 0 if this `ArrayBuffer` has been detached.

## Examples

### Using byteLength

```js
const buffer = new ArrayBuffer(8);
buffer.byteLength; // 8
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("ArrayBuffer")}}
