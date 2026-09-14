---
title: AsyncDisposableStack() constructor
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/asyncdisposablestack/asyncdisposablestack/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 2510
---

The **`AsyncDisposableStack()`** constructor creates {{jsxref("AsyncDisposableStack")}} objects.

## Syntax

```js-nolint
new AsyncDisposableStack()
```

> [!NOTE]
> `AsyncDisposableStack()` can only be constructed with [`new`](/en-US/docs/Web/JavaScript/Reference/Operators/new). Attempting to call it without `new` throws a {{jsxref("TypeError")}}.

### Parameters

None.

### Return value

A new `AsyncDisposableStack` object.

## Examples

### Creating an AsyncDisposableStack

```js
const disposer = new AsyncDisposableStack();
disposer.defer(() => console.log("Disposed!"));
await disposer.disposeAsync();
// Logs: Disposed!
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [JavaScript resource management](/en-US/docs/Web/JavaScript/Guide/Resource_management)
