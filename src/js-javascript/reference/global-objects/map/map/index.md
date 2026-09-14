---
title: Map() constructor
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/map/map/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 5740
---

The **`Map()`** constructor creates {{jsxref("Map")}} objects.

## Syntax

```js-nolint
new Map()
new Map(iterable)
```

> [!NOTE]
> `Map()` can only be constructed with [`new`](/en-US/docs/Web/JavaScript/Reference/Operators/new). Attempting to call it without `new` throws a {{jsxref("TypeError")}}.

### Parameters

- `iterable` {{optional_inline}}
  - : If an [iterable object](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) (such as an array) is passed, all of its elements will be added to the new `Map`. Each element must be an object with two properties: `0` and `1`, which correspond to the key and value (for example, `[[1, "one"],[2, "two"]]`). If you don't specify this parameter, or its value is `null` or `undefined`, the new `Map` is empty.

## Examples

### Creating a new Map

```js
const myMap = new Map([
  [1, "one"],
  [2, "two"],
  [3, "three"],
]);
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [Polyfill for `Map` in `core-js`](https://github.com/zloirock/core-js#map)
- [es-shims polyfill of `Map`](https://www.npmjs.com/package/es-map)
- {{jsxref("Set")}}
- {{jsxref("WeakMap")}}
- {{jsxref("WeakSet")}}
