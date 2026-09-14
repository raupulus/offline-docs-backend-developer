---
title: 'RangeError: x can''t be converted to BigInt because it isn''t an integer'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/cant_be_converted_to_bigint_because_it_isnt_an_integer/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 660
---

The JavaScript exception "x can't be converted to BigInt because it isn't an integer" occurs when the [`BigInt()`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt) function is used on a number that isn't an integer.

## Message

```plain
RangeError: The number 1.5 cannot be converted to a BigInt because it is not an integer (V8-based & Firefox)
RangeError: Not an integer (Safari)
```

## Error type

{{jsxref("RangeError")}}.

## What went wrong?

When using the [`BigInt()`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt) function to convert a number to a BigInt, the number must be an integer (such that [`Number.isInteger`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isInteger) returns true).

## Examples

### Invalid cases

```js example-bad
const a = BigInt(1.5);
// RangeError: The number 1.5 cannot be converted to a BigInt because it is not an integer
const b = BigInt(NaN);
// RangeError: NaN cannot be converted to a BigInt because it is not an integer
```

### Valid cases

```js example-good
const a = BigInt(1);
```

## See also

- [`BigInt()` constructor](/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
- [`Number.isInteger()`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isInteger)
