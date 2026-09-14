---
title: WeakSet.prototype.add()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/weakset/add/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 11920
---

The **`add()`** method of {{jsxref("WeakSet")}} instances inserts the specified value into this set, if it is not already present.

{{InteractiveExample("JavaScript Demo: WeakSet.prototype.add()", "taller")}}

```js interactive-example
const weakset = new WeakSet();
const object = {};

weakset.add(object);
console.log(weakset.has(object));
// Expected output: true

try {
  weakset.add(1);
} catch (error) {
  console.log(error);
  // Expected output (Chrome): TypeError: Invalid value used in weak set
  // Expected output (Firefox): TypeError: WeakSet value must be an object, got 1
  // Expected output (Safari): TypeError: Attempted to add a non-object key to a WeakSet
}
```

## Syntax

```js-nolint
add(value)
```

### Parameters

- `value`
  - : The value to add to the `WeakSet` object. Must be either an object or a [non-registered symbol](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry). Objects are compared by [reference](/en-US/docs/Glossary/Object_reference), not by value.

### Return value

The `WeakSet` object.

### Exceptions

- {{jsxref("TypeError")}}
  - : Thrown if `value` is not an object or a [non-registered symbol](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry).

## Examples

### Using add()

```js
const ws = new WeakSet();

ws.add(window); // add the window object to the WeakSet

ws.has(window); // true

// WeakSet only takes objects as arguments
ws.add(1);
// results in "TypeError: Invalid value used in weak set" in Chrome
// and "TypeError: 1 is not a non-null object" in Firefox
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("WeakSet")}}
- {{jsxref("WeakSet.prototype.delete()")}}
- {{jsxref("WeakSet.prototype.has()")}}
