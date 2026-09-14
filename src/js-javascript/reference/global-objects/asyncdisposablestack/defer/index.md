---
title: AsyncDisposableStack.prototype.defer()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/asyncdisposablestack/defer/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 2520
---

The **`defer()`** method of {{jsxref("AsyncDisposableStack")}} instances takes a callback function to be called and awaited when the stack is disposed.

See {{jsxref("DisposableStack.prototype.defer()")}} for general information about the `defer()` method.

## Syntax

```js-nolint
defer(onDispose)
```

### Parameters

- `onDispose`
  - : A function that will be called when the stack is disposed. The function receives no arguments and can return a promise which gets awaited.

### Return value

None ({{jsxref("undefined")}}).

### Exceptions

- {{jsxref("TypeError")}}
  - : Thrown if `onDispose` is not a function.
- {{jsxref("ReferenceError")}}
  - : Thrown if the stack is already disposed.

## Examples

### Using defer()

One use case of `defer()` is to do something unrelated to resource freeing during scope exit, such as logging a message.

```js
async function doSomething() {
  await using disposer = new AsyncDisposableStack();
  disposer.defer(async () => {
    await fs.writeFile("log.txt", "All resources freed successfully");
  });
  // Other code that claims and frees more data
}
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [JavaScript resource management](/en-US/docs/Web/JavaScript/Guide/Resource_management)
- {{jsxref("AsyncDisposableStack")}}
- {{jsxref("AsyncDisposableStack.prototype.adopt()")}}
- {{jsxref("AsyncDisposableStack.prototype.use()")}}
