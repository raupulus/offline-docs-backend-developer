---
title: 'RangeError: repeat count must be non-negative'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/negative_repetition_count/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 1220
---

The JavaScript exception "repeat count must be non-negative" occurs when the
{{jsxref("String.prototype.repeat()")}} method is used with a `count`
argument that is a negative number.

## Message

```plain
RangeError: Invalid count value: -1 (V8-based)
RangeError: repeat count must be non-negative (Firefox)
RangeError: String.prototype.repeat argument must be greater than or equal to 0 and not be Infinity (Safari)
```

## Error type

{{jsxref("RangeError")}}

## What went wrong?

The {{jsxref("String.prototype.repeat()")}} method has been used. It has a
`count` parameter indicating the number of times to repeat the string. It
must be between 0 and less than positive {{jsxref("Infinity")}} and cannot be a negative
number. The range of allowed values can be described like this: \[0, +∞).

## Examples

### Invalid cases

```js example-bad
"abc".repeat(-1); // RangeError
```

### Valid cases

```js example-good
"abc".repeat(0); // ''
"abc".repeat(1); // 'abc'
"abc".repeat(2); // 'abcabc'
"abc".repeat(3.5); // 'abcabcabc' (count will be converted to integer)
```

## See also

- {{jsxref("String.prototype.repeat()")}}
