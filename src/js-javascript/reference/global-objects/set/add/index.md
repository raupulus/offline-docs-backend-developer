---
title: Set.prototype.add()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/set/add/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 7660
---

The **`add()`** method of {{jsxref("Set")}} instances inserts the specified value into this set, if it is not already present.

{{InteractiveExample("JavaScript Demo: Set.prototype.add()")}}

```js interactive-example
const set = new Set();

set.add(42);
set.add(42);
set.add(13);

for (const item of set) {
  console.log(item);
  // Expected output: 42
  // Expected output: 13
}
```

## Syntax

```js-nolint
add(value)
```

### Parameters

- `value`
  - : The value to add to the `Set` object. Objects are compared by [reference](/en-US/docs/Glossary/Object_reference), not by value.

### Return value

The `Set` object.

## Examples

### Using add()

```js
const mySet = new Set();

mySet.add(1);
mySet.add(5).add("some text"); // chainable

console.log(mySet);
// Set [1, 5, "some text"]
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Set")}}
- {{jsxref("Set.prototype.delete()")}}
- {{jsxref("Set.prototype.has()")}}
