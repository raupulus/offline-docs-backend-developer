---
title: TypedArray.prototype.with()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/typedarray/with/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 11600
---

The **`with()`** method of {{jsxref("TypedArray")}} instances is the [copying](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#copying_methods_and_mutating_methods) version of using the [bracket notation](/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#bracket_notation) to change the value of a given index. It returns a new typed array with the element at the given index replaced with the given value. This method has the same algorithm as {{jsxref("Array.prototype.with()")}}.

## Syntax

```js-nolint
arrayInstance.with(index, value)
```

### Parameters

- `index`
  - : Zero-based index at which to change the typed array, [converted to an integer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#integer_conversion).
- `value`
  - : Any value to be assigned to the given index.

### Return value

A new typed array with the element at `index` replaced with `value`.

### Exceptions

- {{jsxref("RangeError")}}
  - : Thrown if `index >= array.length` or `index < -array.length`.

## Description

See {{jsxref("Array.prototype.with()")}} for more details. This method is not generic and can only be called on typed array instances.

## Examples

### Using with()

```js
const arr = new Uint8Array([1, 2, 3, 4, 5]);
console.log(arr.with(2, 6)); // Uint8Array [1, 2, 6, 4, 5]
console.log(arr); // Uint8Array [1, 2, 3, 4, 5]
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [Polyfill of `TypedArray.prototype.with` in `core-js`](https://github.com/zloirock/core-js#change-array-by-copy)
- [JavaScript typed arrays](/en-US/docs/Web/JavaScript/Guide/Typed_arrays) guide
- {{jsxref("TypedArray.prototype.toReversed()")}}
- {{jsxref("TypedArray.prototype.toSorted()")}}
- {{jsxref("TypedArray.prototype.at()")}}
- {{jsxref("Array.prototype.with()")}}
