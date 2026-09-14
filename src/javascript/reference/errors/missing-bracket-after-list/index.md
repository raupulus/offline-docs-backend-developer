---
title: 'SyntaxError: missing ] after element list'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/missing_bracket_after_list/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 1120
---

The JavaScript exception "missing ] after element list" occurs when there is an error
with the array initializer syntax somewhere. Likely there is a closing square bracket
(`]`) or a comma (`,`) missing.

## Message

```plain
SyntaxError: missing ] after element list (Firefox)
SyntaxError: Unexpected token ';'. Expected either a closing ']' or a ',' following an array element. (Safari)
```

## Error type

{{jsxref("SyntaxError")}}.

## What went wrong?

There is an error with the array initializer syntax somewhere. Likely there is a
closing square bracket (`]`) or a comma (`,`) missing.

## Examples

### Incomplete array initializer

```js-nolint example-bad
const list = [1, 2,

const instruments = [
  "Ukulele",
  "Guitar",
  "Piano",
};

const data = [{ foo: "bar" } { bar: "foo" }];
```

Correct would be:

```js example-good
const list = [1, 2];

const instruments = ["Ukulele", "Guitar", "Piano"];

const data = [{ foo: "bar" }, { bar: "foo" }];
```

## See also

- {{jsxref("Array")}}
