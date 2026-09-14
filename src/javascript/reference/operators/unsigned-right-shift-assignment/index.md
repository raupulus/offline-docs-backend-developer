---
title: Unsigned right shift assignment (>>>=)
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/operators/unsigned_right_shift_assignment/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 12730
---

The **unsigned right shift assignment (`>>>=`)** operator performs [unsigned right shift](/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift) on the two operands and assigns the result to the left operand.

{{InteractiveExample("JavaScript Demo: Unsigned right shift assignment (>>>=) operator")}}

```js interactive-example
let a = 5; //  00000000000000000000000000000101

a >>>= 2; //  00000000000000000000000000000001
console.log(a);
// Expected output: 1

let b = -5; // -00000000000000000000000000000101

b >>>= 2; //  00111111111111111111111111111110
console.log(b);
// Expected output: 1073741822
```

## Syntax

```js-nolint
x >>>= y
```

## Description

`x >>>= y` is equivalent to `x = x >>> y`, except that the expression `x` is only evaluated once.

## Examples

### Using unsigned right shift assignment

```js
let a = 5; // (00000000000000000000000000000101)
a >>>= 2; // 1 (00000000000000000000000000000001)

let b = -5; // (-00000000000000000000000000000101)
b >>>= 2; // 1073741822 (00111111111111111111111111111110)

let c = 5n;
c >>>= 2n; // 1n
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [Assignment operators in the JS guide](/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#assignment_operators)
- [Unsigned right shift (`>>>`)](/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift)
