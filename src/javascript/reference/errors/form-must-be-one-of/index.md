---
title: 'RangeError: form must be one of ''NFC'', ''NFD'', ''NFKC'', or ''NFKD'''
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/form_must_be_one_of/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 870
---

The JavaScript exception "form must be one of 'NFC', 'NFD', 'NFKC', or 'NFKD'" occurs when an unrecognized string is passed to the {{jsxref("String.prototype.normalize()")}} method.

## Message

```plain
RangeError: The normalization form should be one of NFC, NFD, NFKC, NFKD. (V8-based)
RangeError: form must be one of 'NFC', 'NFD', 'NFKC', or 'NFKD' (Firefox)
RangeError: argument does not match any normalization form (Safari)
```

## Error type

{{jsxref("RangeError")}}

## What went wrong?

The {{jsxref("String.prototype.normalize()")}} method only accepts the following four values as its `form` argument: `"NFC"`, `"NFD"`, `"NFKC"`, or `"NFKD"`. If you pass any other value, an error will be thrown. Read the reference of `normalize()` to learn about different normalization forms.

## Examples

### Invalid cases

```js example-bad
"foo".normalize("nfc"); // RangeError
"foo".normalize(" NFC "); // RangeError
```

### Valid cases

```js example-good
"foo".normalize("NFC"); // 'foo'
```

## See also

- {{jsxref("String.prototype.normalize()")}}
