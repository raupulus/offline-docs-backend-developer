---
title: 'TypeError: WeakSet key/WeakMap value ''x'' must be an object or an unregistered
  symbol'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/key_not_weakly_held/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 1090
---

The JavaScript exception "WeakSet key (or WeakMap value) 'x' must be an object or an unregistered symbol" occurs when a value of invalid type is used as a key in a {{jsxref("WeakSet")}} or as a value in a {{jsxref("WeakMap")}}.

## Message

```plain
TypeError: Invalid value used as weak map key (V8-based)
TypeError: WeakMap key 1 must be an object or an unregistered symbol (Firefox)
TypeError: WeakMap keys must be objects or non-registered symbols (Safari)

TypeError: Invalid value used in weak set (V8-based)
TypeError: WeakSet value 1 must be an object or an unregistered symbol (Firefox)
TypeError: WeakSet values must be objects or non-registered symbols (Safari)
```

## Error type

{{jsxref("TypeError")}}

## What went wrong?

{{jsxref("WeakSet")}} and {{jsxref("WeakMap")}} require the keys to be _garbage collectable_. Only objects and non-registered symbols (that is, [symbols](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) not returned by {{jsxref("Symbol.for()")}}) are valid. For more information, see [Memory management](/en-US/docs/Web/JavaScript/Guide/Memory_management#weakmaps_and_weaksets). If you want to add keys that are strings, numbers, or other primitive values, you should store them in a regular `Set` or `Map` instead.

## Examples

### Invalid cases

```js example-bad
new WeakSet().add(1); // TypeError
new WeakMap().set(1, {}); // TypeError
new WeakSet([1]); // TypeError
new WeakMap([[1, {}]]); // TypeError
```

### Valid cases

```js example-good
new WeakSet().add({}); // OK
new WeakMap().set({}, 1); // OK

new Set([1]); // OK
new Map([[1, {}]]); // OK
```

## See also

- [Memory management](/en-US/docs/Web/JavaScript/Guide/Memory_management)
- {{jsxref("WeakSet")}}
- {{jsxref("WeakMap")}}
- {{jsxref("Set")}}
- {{jsxref("Map")}}
