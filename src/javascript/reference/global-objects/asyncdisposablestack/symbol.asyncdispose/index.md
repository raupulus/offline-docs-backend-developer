---
title: AsyncDisposableStack.prototype[Symbol.asyncDispose]()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/asyncdisposablestack/symbol.asyncdispose/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 2570
---

The **`[Symbol.asyncDispose]()`** method of {{jsxref("AsyncDisposableStack")}} instances implements the _async disposable protocol_ and allows it to be disposed when used with {{jsxref("Statements/await_using", "await using")}}. It is an alias for the {{jsxref("AsyncDisposableStack/disposeAsync", "disposeAsync()")}} method.

## Syntax

```js-nolint
asyncDisposableStack[Symbol.asyncDispose]()
```

### Parameters

None.

### Return value

None ({{jsxref("undefined")}}).

## Examples

### Declaring a stack with `await using`

The `Symbol.asyncDispose` method is intended to be automatically called in an `await using` declaration.

```js
async function doSomething() {
  await using disposer = new AsyncDisposableStack();
  const resource = disposer.use(new Resource());
  resource.doSomething();
  // disposer is disposed here immediately before the function exits
  // which causes the resource to be disposed
}
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [JavaScript resource management](/en-US/docs/Web/JavaScript/Guide/Resource_management)
- {{jsxref("AsyncDisposableStack")}}
- {{jsxref("AsyncDisposableStack.prototype.disposeAsync()")}}
