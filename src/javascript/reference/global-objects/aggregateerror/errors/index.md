---
title: 'AggregateError: errors'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/aggregateerror/errors/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 1880
---

The **`errors`** data property of an {{jsxref("AggregateError")}} instance contains an array representing the errors that were aggregated.

## Value

An {{jsxref("Array")}} containing values in the same order as the iterable passed as the first argument of the {{jsxref("AggregateError/AggregateError", "AggregateError()")}} constructor.

{{js_property_attributes(1, 0, 1)}}

## Examples

### Using errors

```js
try {
  throw new AggregateError(
    // An iterable of errors
    new Set([new Error("some error"), new Error("another error")]),
    "Multiple errors thrown",
  );
} catch (err) {
  console.log(err.errors);
  // [
  //   Error: some error,
  //   Error: another error
  // ]
}
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [Control flow and error handling](/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling) guide
- {{jsxref("AggregateError")}}
- [`Error`: `cause`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause)
