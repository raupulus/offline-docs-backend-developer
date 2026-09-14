---
title: arguments.length
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/functions/arguments/length/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 1780
---

The **`arguments.length`** data property contains the number of arguments passed to the function.

## Value

A non-negative integer.

{{js_property_attributes(1, 0, 1)}}

## Description

The `arguments.length` property provides the number of arguments actually passed to a function. This can be more or less than the defined parameter's count (see {{jsxref("Function.prototype.length")}}). For example, for the function below:

```js
function func1(a, b, c) {
  console.log(arguments.length);
}
```

`func1.length` returns `3`, because `func1` declares three formal parameters. However, `func1(1, 2, 3, 4, 5)` logs `5`, because `func1` was called with five arguments. Similarly, `func1(1)` logs `1`, because `func1` was called with one argument.

## Examples

### Using arguments.length

In this example, we define a function that can add two or more numbers together.

```js
function adder(base /*, num1, …, numN */) {
  base = Number(base);
  for (let i = 1; i < arguments.length; i++) {
    base += Number(arguments[i]);
  }
  return base;
}
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [Functions](/en-US/docs/Web/JavaScript/Guide/Functions) guide
- [Functions](/en-US/docs/Web/JavaScript/Reference/Functions)
- {{jsxref("Functions/arguments", "arguments")}}
- [`Function`: `length`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)
