---
title: AsyncDisposableStack.prototype.disposed
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/asyncdisposablestack/disposed/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 2540
---

The **`disposed`** accessor property of {{jsxref("AsyncDisposableStack")}} instances returns a boolean indicating whether or not this `AsyncDisposableStack` has been disposed or moved by doing any of the following:

- Calling its {{jsxref("AsyncDisposableStack/disposeAsync", "disposeAsync()")}} method
- Calling its {{jsxref("AsyncDisposableStack/move", "move()")}} method
- Declaring it with {{jsxref("Statements/await_using", "await using")}} and letting the variable go out of scope, which automatically calls the [`[Symbol.asyncDispose]()`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncDisposableStack/Symbol.asyncDispose) method.

## Examples

### Checking if a stack is disposed

```js
const disposer = new AsyncDisposableStack();
console.log(disposer.disposed); // false
await disposer.disposeAsync();
console.log(disposer.disposed); // true
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [JavaScript resource management](/en-US/docs/Web/JavaScript/Guide/Resource_management)
