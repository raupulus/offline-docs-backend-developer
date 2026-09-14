---
title: Error.prototype.toString()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/error/tostring/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 4050
---

The **`toString()`** method of {{jsxref("Error")}} instances returns a string representing this error.

## Syntax

```js-nolint
toString()
```

### Parameters

None.

### Return value

A string representing the specified {{jsxref("Error")}} object.

## Description

The {{jsxref("Error")}} object overrides the {{jsxref("Object.prototype.toString()")}}
method inherited by all objects. Its semantics are as follows:

```js
Error.prototype.toString = function () {
  if (
    this === null ||
    (typeof this !== "object" && typeof this !== "function")
  ) {
    throw new TypeError();
  }
  let name = this.name;
  name = name === undefined ? "Error" : `${name}`;
  let msg = this.message;
  msg = msg === undefined ? "" : `${msg}`;
  if (name === "") {
    return msg;
  }
  if (msg === "") {
    return name;
  }
  return `${name}: ${msg}`;
};
```

## Examples

### Using toString()

```js
const e1 = new Error("fatal error");
console.log(e1.toString()); // "Error: fatal error"

const e2 = new Error("fatal error");
e2.name = undefined;
console.log(e2.toString()); // "Error: fatal error"

const e3 = new Error("fatal error");
e3.name = "";
console.log(e3.toString()); // "fatal error"

const e4 = new Error("fatal error");
e4.name = "";
e4.message = undefined;
console.log(e4.toString()); // ""

const e5 = new Error("fatal error");
e5.name = "hello";
e5.message = undefined;
console.log(e5.toString()); // "hello"
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [Polyfill of `Error.prototype.toString` with many bug fixes in `core-js`](https://github.com/zloirock/core-js#ecmascript-error)
