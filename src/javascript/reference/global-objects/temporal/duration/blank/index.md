---
title: Temporal.Duration.prototype.blank
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/temporal/duration/blank/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 8800
---

The **`blank`** accessor property of {{jsxref("Temporal.Duration")}} instances returns a boolean that is `true` if this duration represents a zero duration, and `false` otherwise. It is equivalent to `duration.sign === 0`.

## Examples

### Using blank

```js
const d1 = Temporal.Duration.from({ hours: 1, minutes: 30 });
const d2 = Temporal.Duration.from({ hours: -1, minutes: -30 });
const d3 = Temporal.Duration.from({ hours: 0 });

console.log(d1.blank); // false
console.log(d2.blank); // false
console.log(d3.blank); // true
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Temporal.Duration")}}
- {{jsxref("Temporal/Duration/sign", "Temporal.Duration.prototype.sign")}}
