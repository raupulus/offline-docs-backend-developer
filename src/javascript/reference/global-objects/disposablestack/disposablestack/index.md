---
title: DisposableStack() constructor
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/disposablestack/disposablestack/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 3840
---

The **`DisposableStack()`** constructor creates {{jsxref("DisposableStack")}} objects.

## Syntax

```js-nolint
new DisposableStack()
```

> [!NOTE]
> `DisposableStack()` can only be constructed with [`new`](/en-US/docs/Web/JavaScript/Reference/Operators/new). Attempting to call it without `new` throws a {{jsxref("TypeError")}}.

### Parameters

None.

### Return value

A new `DisposableStack` object.

## Examples

### Creating a DisposableStack

```js
const disposer = new DisposableStack();
disposer.defer(() => console.log("Disposed!"));
disposer.dispose();
// Logs: Disposed!
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [JavaScript resource management](/en-US/docs/Web/JavaScript/Guide/Resource_management)
