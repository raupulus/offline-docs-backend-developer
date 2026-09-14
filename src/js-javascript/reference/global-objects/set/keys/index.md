---
title: Set.prototype.keys()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/set/keys/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 7780
---

The **`keys()`** method of {{jsxref("Set")}} instances is an alias for the [`values()`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values) method.

## Syntax

```js-nolint
keys()
```

### Parameters

None.

### Return value

A new [iterable iterator object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator).

## Examples

### Using keys()

The `keys()` method is exactly equivalent to the {{jsxref("Set/values", "values()")}} method.

```js
const mySet = new Set();
mySet.add("foo");
mySet.add("bar");
mySet.add("baz");

const setIter = mySet.keys();

console.log(setIter.next().value); // "foo"
console.log(setIter.next().value); // "bar"
console.log(setIter.next().value); // "baz"
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Set.prototype.entries()")}}
- {{jsxref("Set.prototype.values()")}}
