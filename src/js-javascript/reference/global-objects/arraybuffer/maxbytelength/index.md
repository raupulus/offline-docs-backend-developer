---
title: ArrayBuffer.prototype.maxByteLength
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/arraybuffer/maxbytelength/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 2430
---

The **`maxByteLength`** accessor property of {{jsxref("ArrayBuffer")}} instances returns the maximum length (in bytes) that this array buffer can be resized to.

{{InteractiveExample("JavaScript Demo: ArrayBuffer.prototype.maxByteLength")}}

```js interactive-example
const buffer = new ArrayBuffer(8, { maxByteLength: 16 });

console.log(buffer.byteLength);
// Expected output: 8

console.log(buffer.maxByteLength);
// Expected output: 16
```

## Description

The `maxByteLength` property is an accessor property whose set accessor function is `undefined`, meaning that you can only read this property. The value is established when the array is constructed, set via the `maxByteLength` option of the {{jsxref("ArrayBuffer/ArrayBuffer", "ArrayBuffer()")}} constructor, and cannot be changed.

This property returns 0 if this `ArrayBuffer` has been detached. If this `ArrayBuffer` was constructed without specifying a `maxByteLength` value, this property returns a value equal to the value of the `ArrayBuffer`'s {{jsxref("ArrayBuffer/byteLength", "byteLength")}}.

## Examples

### Using maxByteLength

In this example, we create an 8-byte buffer that is resizable to a max length of 16 bytes, then return its `maxByteLength`:

```js
const buffer = new ArrayBuffer(8, { maxByteLength: 16 });

buffer.maxByteLength; // 16
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("ArrayBuffer")}}
- {{jsxref("ArrayBuffer.prototype.byteLength")}}
- {{jsxref("ArrayBuffer.prototype.resize()")}}
