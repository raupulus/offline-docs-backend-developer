---
title: Intl.getCanonicalLocales()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/intl/getcanonicallocales/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 4750
---

The **`Intl.getCanonicalLocales()`** static method returns an array
containing the canonical locale names. Duplicates will be omitted and elements will be
validated as structurally valid language tags.

{{InteractiveExample("JavaScript Demo: Intl.getCanonicalLocales()")}}

```js interactive-example
console.log(Intl.getCanonicalLocales("EN-US"));
// Expected output: Array ["en-US"]

console.log(Intl.getCanonicalLocales(["EN-US", "Fr"]));
// Expected output: Array ["en-US", "fr"]

try {
  Intl.getCanonicalLocales("EN_US");
} catch (err) {
  console.log(err.toString());
  // Expected output: RangeError: invalid language tag: "EN_US"
}
```

## Syntax

```js-nolint
Intl.getCanonicalLocales(locales)
```

### Parameters

- `locales`
  - : A list of {{jsxref("String")}} values for which to get the canonical locale names.

### Return value

An array containing the canonical locale names.

## Examples

### Using getCanonicalLocales

```js
Intl.getCanonicalLocales("EN-US"); // ["en-US"]
Intl.getCanonicalLocales(["EN-US", "Fr"]); // ["en-US", "fr"]

Intl.getCanonicalLocales("EN_US");
// RangeError: invalid language tag: "EN_US"
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [Polyfill of `Intl.getCanonicalLocales` in FormatJS](https://formatjs.github.io/docs/polyfills/intl-getcanonicallocales/)
- {{jsxref("Intl/NumberFormat/supportedLocalesOf", "Intl.NumberFormat.supportedLocalesOf()")}}
- {{jsxref("Intl/DateTimeFormat/supportedLocalesOf", "Intl.DateTimeFormat.supportedLocalesOf()")}}
- {{jsxref("Intl/Collator/supportedLocalesOf", "Intl.Collator.supportedLocalesOf()")}}
