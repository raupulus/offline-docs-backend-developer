---
title: BigInt.prototype.valueOf()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/bigint/valueof/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 2920
---

The **`valueOf()`** method of {{jsxref("BigInt")}} values returns the wrapped primitive value
of a {{jsxref("BigInt")}} object.

{{InteractiveExample("JavaScript Demo: BigInt.prototype.valueOf()", "shorter")}}

```js interactive-example
console.log(typeof Object(1n));
// Expected output: "object"

console.log(typeof Object(1n).valueOf());
// Expected output: "bigint"
```

## Syntax

```js-nolint
valueOf()
```

### Parameters

None.

### Return value

A BigInt representing the primitive value of the specified {{jsxref("BigInt")}} object.

## Examples

### Using `valueOf`

```js
typeof Object(1n); // object
typeof Object(1n).valueOf(); // bigint
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("BigInt.prototype.toString()")}}
