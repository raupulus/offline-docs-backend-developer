---
title: Temporal.PlainMonthDay.prototype.equals()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/temporal/plainmonthday/equals/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 10110
---

The **`equals()`** method of {{jsxref("Temporal.PlainMonthDay")}} instances returns `true` if this month-day is equivalent in value to another month-day (in a form convertible by {{jsxref("Temporal/PlainMonthDay/from", "Temporal.PlainMonthDay.from()")}}), and `false` otherwise. They are compared both by their underlying ISO date values and their calendars.

> [!NOTE]
> `PlainMonthDay` objects keep track of a reference ISO year, which is also used in the comparison. This year is automatically set when using the {{jsxref("Temporal/PlainMonthDay/from", "Temporal.PlainMonthDay.from()")}} method, but can be set manually using the {{jsxref("Temporal/PlainMonthDay/PlainMonthDay", "Temporal.PlainMonthDay()")}} constructor, causing two equivalent month-days to be considered different if they have different reference years. For this reason, you should avoid using the constructor directly and prefer the `from()` method.

## Syntax

```js-nolint
equals(other)
```

### Parameters

- `other`
  - : A string, an object, or a {{jsxref("Temporal.PlainMonthDay")}} instance representing the other month-day to compare. It is converted to a `Temporal.PlainMonthDay` object using the same algorithm as {{jsxref("Temporal/PlainMonthDay/from", "Temporal.PlainMonthDay.from()")}}.

### Return value

`true` if this month-day is equal to `other` both in their date value and their calendar, `false` otherwise.

## Examples

### Using equals()

```js
const md1 = Temporal.PlainMonthDay.from("2021-08-01");
const md2 = Temporal.PlainMonthDay.from({ year: 2020, month: 8, day: 1 }); // Year doesn't matter
console.log(md1.equals(md2)); // true

const md3 = Temporal.PlainMonthDay.from("2021-08-01[u-ca=japanese]");
console.log(md1.equals(md3)); // false

const md4 = Temporal.PlainMonthDay.from("2021-08-02");
console.log(md1.equals(md4)); // false
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Temporal.PlainMonthDay")}}
