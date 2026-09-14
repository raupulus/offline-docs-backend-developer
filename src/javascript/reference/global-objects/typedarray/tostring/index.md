---
title: TypedArray.prototype.toString()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/typedarray/tostring/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 11580
---

The **`toString()`** method of {{jsxref("TypedArray")}} instances returns a string representing the specified typed array and its elements. This method has the same algorithm as {{jsxref("Array.prototype.toString()")}}.

{{InteractiveExample("JavaScript Demo: TypedArray.prototype.toString()", "shorter")}}

```js interactive-example
const uint8 = new Uint8Array([10, 20, 30, 40, 50]);

const uint8String = uint8.toString();

console.log(uint8String.startsWith("10"));
// Expected output: true
```

## Syntax

```js-nolint
toString()
```

### Parameters

None.

### Return value

A string representing the elements of the typed array.

## Description

See {{jsxref("Array.prototype.toString()")}} for more details. This method is not generic and can only be called on typed array instances.

## Examples

### Converting a typed array to a string

```js
const uint8 = new Uint8Array([1, 2, 3]);
// Explicit conversion
console.log(uint8.toString()); // 1,2,3
// Implicit conversion
console.log(`${uint8}`); // 1,2,3
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [JavaScript typed arrays](/en-US/docs/Web/JavaScript/Guide/Typed_arrays) guide
- {{jsxref("TypedArray")}}
- {{jsxref("TypedArray.prototype.join()")}}
- {{jsxref("TypedArray.prototype.toLocaleString()")}}
- {{jsxref("Array.prototype.toString()")}}
- {{jsxref("String.prototype.toString()")}}
