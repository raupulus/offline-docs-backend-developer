---
title: WeakSet.prototype.has()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/weakset/has/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 11940
---

The **`has()`** method of {{jsxref("WeakSet")}} instances returns a boolean indicating whether the specified value exists in this `WeakSet` or not.

{{InteractiveExample("JavaScript Demo: WeakSet.prototype.has()")}}

```js interactive-example
const weakset = new WeakSet();
const object1 = {};
const object2 = {};

weakset.add(object1);

console.log(weakset.has(object1));
// Expected output: true

console.log(weakset.has(object2));
// Expected output: false
```

## Syntax

```js-nolint
has(value)
```

### Parameters

- `value`
  - : The value to test for presence in the `WeakSet` object. Objects are compared by [reference](/en-US/docs/Glossary/Object_reference), not by value.

### Return value

Returns `true` if the specified value exists in the `WeakSet` object; otherwise `false`. Always returns `false` if `value` is not an object or a [non-registered symbol](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry).

## Examples

### Using has()

```js
const ws = new WeakSet();
const obj = {};
ws.add(window);

ws.has(window); // returns true
ws.has(obj); // returns false

// Storing a non-registered symbol
const sym = Symbol("foo");
ws.add(sym);
ws.add(Symbol.iterator);
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("WeakSet")}}
- {{jsxref("WeakSet.prototype.add()")}}
- {{jsxref("WeakSet.prototype.delete()")}}
