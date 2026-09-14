---
title: WeakRef.prototype.deref()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/weakref/deref/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 11890
---

The **`deref()`** method of {{jsxref("WeakRef")}} instances returns this `WeakRef`'s target value, or `undefined` if the target value has been garbage-collected.

## Syntax

```js-nolint
deref()
```

### Parameters

None.

### Return value

The target value of the WeakRef, which is either an object or a [non-registered symbol](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry). Returns `undefined` if the value has been garbage-collected.

## Description

See the [Notes on WeakRefs](/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#notes_on_weakrefs) section of the {{jsxref("WeakRef")}} page for some important notes.

## Examples

### Using deref()

See the [Examples](/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#examples)
section of the {{jsxref("WeakRef")}} page for the complete example.

```js
const tick = () => {
  // Get the element from the weak reference, if it still exists
  const element = this.ref.deref();
  if (element) {
    element.textContent = ++this.count;
  } else {
    // The element doesn't exist anymore
    console.log("The element is gone.");
    this.stop();
    this.ref = null;
  }
};
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("WeakRef")}}
