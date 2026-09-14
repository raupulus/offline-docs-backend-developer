---
title: RegExp.prototype.compile()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/regexp/compile/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 7360
---

{{Deprecated_Header}}

> [!NOTE]
> The `compile()` method is only specified for compatibility reasons. Using `compile()` causes the otherwise immutable regex source and flags to become mutable, which may break user expectations. You can use the [`RegExp()`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/RegExp) constructor to construct a new regular expression object instead.

The **`compile()`** method of {{jsxref("RegExp")}} instances is used to recompile a regular expression with new source and flags after the `RegExp` object has already been created.

## Syntax

```js-nolint
compile(pattern, flags)
```

### Parameters

- `pattern`
  - : The text of the regular expression.
- `flags`
  - : Any combination of [flag values](/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/RegExp#flags).

### Return value

None ({{jsxref("undefined")}}).

### Exceptions

- {{jsxref("TypeError")}}
  - : Thrown if the `this` value is not an instance of the current realm's `RegExp` constructor.
    This includes a subclass of `RegExp` and the `RegExp` constructor from a different realm.

## Examples

### Using compile()

The following example shows how to recompile a regular expression with a new pattern and a new flag.

```js
const regexObj = /foo/gi;
regexObj.compile("new foo", "g");
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("RegExp")}}
