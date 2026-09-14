---
title: Number.prototype.valueOf()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/number/valueof/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 6480
---

The **`valueOf()`** method of {{jsxref("Number")}} values returns the value of this number.

{{InteractiveExample("JavaScript Demo: Number.prototype.valueOf()")}}

```js interactive-example
const numObj = new Number(42);
console.log(typeof numObj);
// Expected output: "object"

const num = numObj.valueOf();
console.log(num);
// Expected output: 42

console.log(typeof num);
// Expected output: "number"
```

## Syntax

```js-nolint
valueOf()
```

### Parameters

None.

### Return value

A number representing the primitive value of the specified {{jsxref("Number")}} object.

## Description

This method is usually called internally by JavaScript and not explicitly in web code.

## Examples

### Using valueOf

```js
const numObj = new Number(10);
console.log(typeof numObj); // object

const num = numObj.valueOf();
console.log(num); // 10
console.log(typeof num); // number
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Object.prototype.valueOf()")}}
