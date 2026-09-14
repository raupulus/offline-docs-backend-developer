---
title: String.prototype.toLowerCase()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/string/tolowercase/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 8410
---

The **`toLowerCase()`** method of {{jsxref("String")}} values returns this string converted to lower case.

{{InteractiveExample("JavaScript Demo: String.prototype.toLowerCase()", "shorter")}}

```js interactive-example
const sentence = "The quick brown fox jumps over the lazy dog.";

console.log(sentence.toLowerCase());
// Expected output: "the quick brown fox jumps over the lazy dog."
```

## Syntax

```js-nolint
toLowerCase()
```

### Parameters

None.

### Return value

A new string representing the calling string converted to lower case.

## Description

The `toLowerCase()` method returns the value of the string converted to
lower case. `toLowerCase()` does not affect the value of the string
`str` itself.

## Examples

### Using `toLowerCase()`

```js
console.log("ALPHABET".toLowerCase()); // 'alphabet'
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("String.prototype.toLocaleLowerCase()")}}
- {{jsxref("String.prototype.toLocaleUpperCase()")}}
- {{jsxref("String.prototype.toUpperCase()")}}
