---
title: DisposableStack.prototype.disposed
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/disposablestack/disposed/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 3860
---

The **`disposed`** accessor property of {{jsxref("DisposableStack")}} instances returns a boolean indicating whether or not this `DisposableStack` has been disposed or moved by doing any of the following:

- Calling its {{jsxref("DisposableStack/dispose", "dispose()")}} method
- Calling its {{jsxref("DisposableStack/move", "move()")}} method
- Declaring it with {{jsxref("Statements/using", "using")}} and letting the variable go out of scope, which automatically calls the [`[Symbol.dispose]()`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/Symbol.dispose) method.

## Examples

### Checking if a stack is disposed

```js
const disposer = new DisposableStack();
console.log(disposer.disposed); // false
disposer.dispose();
console.log(disposer.disposed); // true
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [JavaScript resource management](/en-US/docs/Web/JavaScript/Guide/Resource_management)
