---
title: 'TypeError: invalid Array.prototype.sort argument'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/array_sort_argument/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 460
---

The JavaScript exception "invalid Array.prototype.sort argument" occurs when the argument of {{jsxref("Array.prototype.sort()")}} (and its related methods: {{jsxref("Array.prototype.toSorted()")}}, {{jsxref("TypedArray.prototype.sort()")}}, {{jsxref("TypedArray.prototype.toSorted()")}}) isn't either {{jsxref("undefined")}} or a function that compares its operands.

## Message

```plain
TypeError: The comparison function must be either a function or undefined (V8-based)

TypeError: invalid Array.prototype.sort argument (Firefox)
TypeError: non-function passed to Array.prototype.toSorted (Firefox)
TypeError: invalid %TypedArray%.prototype.sort argument (Firefox)

TypeError: Array.prototype.sort requires the comparator argument to be a function or undefined (Safari)
TypeError: Array.prototype.toSorted requires the comparator argument to be a function or undefined (Safari)
TypeError: TypedArray.prototype.sort requires the comparator argument to be a function or undefined (Safari)
TypeError: TypedArray.prototype.toSorted requires the comparator argument to be a function or undefined (Safari)
```

## Error type

{{jsxref("TypeError")}}

## What went wrong?

The argument of {{jsxref("Array.prototype.sort()")}} (and its related methods: {{jsxref("Array.prototype.toSorted()")}}, {{jsxref("TypedArray.prototype.sort()")}}, {{jsxref("TypedArray.prototype.toSorted()")}}) is expected to be either {{jsxref("undefined")}} or a function which compares its operands.

## Examples

### Invalid cases

```js example-bad
[1, 3, 2].sort(5); // TypeError
students.toSorted("name"); // TypeError
```

### Valid cases

```js example-good
[1, 3, 2].sort(); // [1, 2, 3]
[1, 3, 2].sort((a, b) => a - b); // [1, 2, 3]
students.toSorted((a, b) => a.name.localeCompare(b.name));
```

## See also

- {{jsxref("Array.prototype.sort()")}}
- {{jsxref("Array.prototype.toSorted()")}}
- {{jsxref("TypedArray.prototype.sort()")}}
- {{jsxref("TypedArray.prototype.toSorted()")}}
