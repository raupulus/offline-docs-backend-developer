---
title: Symbol.prototype[Symbol.toPrimitive]()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/symbol/symbol.toprimitive/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 8700
---

The **`[Symbol.toPrimitive]()`** method of {{jsxref("Symbol")}} values returns this symbol value.

## Syntax

```js-nolint
symbolValue[Symbol.toPrimitive](hint)
```

### Parameters

- `hint`
  - : A string value indicating the primitive value to return. The value is ignored.

### Return value

The primitive value of the specified {{jsxref("Symbol")}} object.

## Description

The `[Symbol.toPrimitive]()` method of {{jsxref("Symbol")}} returns the primitive
value of a Symbol object as a Symbol data type. The `hint`
argument is not used.

JavaScript calls the `[Symbol.toPrimitive]()` method to convert an object to a
primitive value. You rarely need to invoke the `[Symbol.toPrimitive]()` method
yourself; JavaScript automatically invokes it when encountering an object where a
primitive value is expected.

## Examples

### Using `[Symbol.toPrimitive]()`

```js
const sym = Symbol("example");
sym === sym[Symbol.toPrimitive](); // true
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Symbol.toPrimitive")}}
