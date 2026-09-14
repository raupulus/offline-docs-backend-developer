---
title: Temporal.Now.instant()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/temporal/now/instant/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 9260
---

The **`Temporal.Now.instant()`** static method returns the current time as a {{jsxref("Temporal.Instant")}} object.

## Syntax

```js-nolint
Temporal.Now.instant()
```

### Parameters

None.

### Return value

A {{jsxref("Temporal.Instant")}} object representing the current time, with potentially [reduced precision](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Now#reduced_time_precision).

## Examples

### Measuring time elapsed

The following example measures two instants in time and calculates the [duration](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration) between them, and gets the total duration in milliseconds:

```js
const start = Temporal.Now.instant();
// Do something that takes time
const end = Temporal.Now.instant();
const duration = end.since(start);
console.log(duration.total("milliseconds"));
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Temporal.Now")}}
- {{jsxref("Temporal.Instant")}}
