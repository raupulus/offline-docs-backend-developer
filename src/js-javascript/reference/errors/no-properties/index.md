---
title: 'TypeError: null/undefined has no properties'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/no_properties/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 1240
---

The JavaScript exception "null (or undefined) has no properties" occurs when you
attempt to access properties of [`null`](/en-US/docs/Web/JavaScript/Reference/Operators/null) and {{jsxref("undefined")}}. They
don't have any.

## Message

```plain
TypeError: Cannot read properties of undefined (reading 'x') (V8-based)
TypeError: Cannot destructure 'x' as it is undefined. (V8-based)
TypeError: Cannot destructure property 'x' of 'y' as it is undefined. (V8-based)
TypeError: null has no properties (Firefox)
TypeError: undefined has no properties (Firefox)
TypeError: undefined is not an object (evaluating 'undefined.x') (Safari)
TypeError: Right side of assignment cannot be destructured (Safari)
```

## Error type

{{jsxref("TypeError")}}.

## What went wrong?

Both [`null`](/en-US/docs/Web/JavaScript/Reference/Operators/null) and {{jsxref("undefined")}} have no properties you could access. Therefore, you cannot use [property accessors](/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors) on them, or [destructure](/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring) them.

## Examples

### null and undefined have no properties

```js example-bad
null.foo;
// TypeError: null has no properties

undefined.bar;
// TypeError: undefined has no properties
```

## See also

- [`null`](/en-US/docs/Web/JavaScript/Reference/Operators/null)
- {{jsxref("undefined")}}
