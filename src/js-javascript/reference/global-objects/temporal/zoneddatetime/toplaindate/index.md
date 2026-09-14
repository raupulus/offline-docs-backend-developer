---
title: Temporal.ZonedDateTime.prototype.toPlainDate()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/temporal/zoneddatetime/toplaindate/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 11060
---

The **`toPlainDate()`** method of {{jsxref("Temporal.ZonedDateTime")}} instances returns a new {{jsxref("Temporal.PlainDate")}} object representing the date portion of this date-time.

## Syntax

```js-nolint
toPlainDate()
```

### Parameters

None.

### Return value

A new {{jsxref("Temporal.PlainDate")}} object representing the date portion of this date-time.

## Examples

### Using toPlainDate()

```js
const zdt = Temporal.ZonedDateTime.from(
  "2021-07-01T12:34:56.987654321-04:00[America/New_York]",
);
const plainDate = zdt.toPlainDate();
console.log(plainDate.toString()); // 2021-07-01
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Temporal.ZonedDateTime")}}
- {{jsxref("Temporal.PlainDate")}}
- {{jsxref("Temporal/ZonedDateTime/toPlainTime", "Temporal.ZonedDateTime.prototype.toPlainTime()")}}
- {{jsxref("Temporal/ZonedDateTime/toPlainDateTime", "Temporal.ZonedDateTime.prototype.toPlainDateTime()")}}
- {{jsxref("Temporal/ZonedDateTime/toInstant", "Temporal.ZonedDateTime.prototype.toInstant()")}}
- {{jsxref("Temporal/PlainDate/toZonedDateTime", "Temporal.PlainDate.prototype.toZonedDateTime()")}}
