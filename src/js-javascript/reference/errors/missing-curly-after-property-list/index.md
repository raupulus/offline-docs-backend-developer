---
title: 'SyntaxError: missing } after property list'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/missing_curly_after_property_list/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 1150
---

The JavaScript exception "missing } after property list" occurs when there is a mistake
in the [object initializer](/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) syntax somewhere.
Might be in fact a missing curly bracket, but could also be a missing comma.

## Message

```plain
SyntaxError: missing } after property list (Firefox)
SyntaxError: Unexpected identifier 'c'. Expected '}' to end an object literal. (Safari)
```

## Error type

{{jsxref("SyntaxError")}}

## What went wrong?

There is a mistake in the [object initializer](/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
syntax somewhere. Might be in fact a missing curly bracket, but could
also be a missing comma, for example. Also check if any closing curly braces or
parenthesis are in the correct order. Indenting or formatting the code a bit nicer might
also help you to see through the jungle.

## Examples

### Forgotten comma

Oftentimes, there is a missing comma in your object initializer code:

```js-nolint example-bad
const obj = {
  a: 1,
  b: { myProp: 2 }
  c: 3
};
```

Correct would be:

```js example-good
const obj = {
  a: 1,
  b: { myProp: 2 },
  c: 3,
};
```

## See also

- [Object initializer](/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
