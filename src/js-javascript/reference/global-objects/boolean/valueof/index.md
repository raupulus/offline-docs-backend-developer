---
title: Boolean.prototype.valueOf()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/boolean/valueof/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 3000
---

The **`valueOf()`** method of {{jsxref("Boolean")}} values returns the primitive value of a
{{jsxref("Boolean")}} object.

{{InteractiveExample("JavaScript Demo: Boolean.prototype.valueOf()")}}

```js interactive-example
const x = new Boolean();

console.log(x.valueOf());
// Expected output: false

const y = new Boolean("Mozilla");

console.log(y.valueOf());
// Expected output: true
```

## Syntax

```js-nolint
valueOf()
```

### Parameters

None.

### Return value

The primitive value of the given {{jsxref("Boolean")}} object.

## Description

The `valueOf()` method of {{jsxref("Boolean")}} returns the primitive value
of a `Boolean` object or literal `Boolean` as a Boolean data type.

This method is usually called internally by JavaScript and not explicitly in code.

## Examples

### Using `valueOf()`

```js
const x = new Boolean();
const myVar = x.valueOf(); // assigns false to myVar
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Object.prototype.valueOf()")}}
