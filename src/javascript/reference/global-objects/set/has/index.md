---
title: Set.prototype.has()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/set/has/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 7720
---

The **`has()`** method of {{jsxref("Set")}} instances returns a boolean indicating whether the specified value exists in this `Set` or not.

{{InteractiveExample("JavaScript Demo: Set.prototype.has()")}}

```js interactive-example
const set = new Set([1, 2, 3, 4, 5]);

console.log(set.has(1));
// Expected output: true

console.log(set.has(5));
// Expected output: true

console.log(set.has(6));
// Expected output: false
```

## Syntax

```js-nolint
has(value)
```

### Parameters

- `value`
  - : The value to test for presence in the `Set` object.

### Return value

Returns `true` if the specified value exists in the `Set` object; otherwise `false`.

## Examples

### Using has()

```js
const mySet = new Set();
mySet.add("foo");

console.log(mySet.has("foo")); // true
console.log(mySet.has("bar")); // false

const set = new Set();
const obj = { key1: 1 };
set.add(obj);

console.log(set.has(obj)); // true
console.log(set.has({ key1: 1 })); // false, because they are different object references
console.log(set.add({ key1: 1 })); // now set contains 2 entries
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Set")}}
- {{jsxref("Set.prototype.add()")}}
- {{jsxref("Set.prototype.delete()")}}
