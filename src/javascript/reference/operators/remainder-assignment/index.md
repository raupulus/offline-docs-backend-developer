---
title: Remainder assignment (%=)
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/operators/remainder_assignment/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 12590
---

The **remainder assignment (`%=`)** operator performs [remainder](/en-US/docs/Web/JavaScript/Reference/Operators/Remainder) on the two operands and assigns the result to the left operand.

{{InteractiveExample("JavaScript Demo: Remainder assignment (%=) operator")}}

```js interactive-example
let a = 3;

console.log((a %= 2));
// Expected output: 1

console.log((a %= 0));
// Expected output: NaN

console.log((a %= "hello"));
// Expected output: NaN
```

## Syntax

```js-nolint
x %= y
```

## Description

`x %= y` is equivalent to `x = x % y`, except that the expression `x` is only evaluated once.

## Examples

### Using remainder assignment

```js
let bar = 5;

bar %= 2; // 1
bar %= "foo"; // NaN
bar %= 0; // NaN

let foo = 3n;
foo %= 2n; // 1n
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [Assignment operators in the JS guide](/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#assignment_operators)
- [Remainder (`%`)](/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)
