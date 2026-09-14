---
title: Temporal.PlainYearMonth.prototype.equals()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/temporal/plainyearmonth/equals/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 10480
---

The **`equals()`** method of {{jsxref("Temporal.PlainYearMonth")}} instances returns `true` if this year-month is equivalent in value to another year-month (in a form convertible by {{jsxref("Temporal/PlainYearMonth/from", "Temporal.PlainYearMonth.from()")}}), and `false` otherwise. They are compared both by their underlying ISO date values and their calendars, so two year-months from different calendars may be considered equal by {{jsxref("Temporal/PlainYearMonth/compare", "Temporal.PlainYearMonth.compare()")}} but not by `equals()`.

> [!NOTE]
> `PlainYearMonth` objects keep track of a reference ISO day, which is also used in the comparison. This day is automatically set when using the {{jsxref("Temporal/PlainYearMonth/from", "Temporal.PlainYearMonth.from()")}} method, but can be set manually using the {{jsxref("Temporal/PlainYearMonth/PlainYearMonth", "Temporal.PlainYearMonth()")}} constructor, causing two equivalent year-months to be considered different if they have different reference days. For this reason, you should avoid using the constructor directly and prefer the `from()` method.

## Syntax

```js-nolint
equals(other)
```

### Parameters

- `other`
  - : A string, an object, or a {{jsxref("Temporal.PlainYearMonth")}} instance representing the other year-month to compare. It is converted to a `Temporal.PlainYearMonth` object using the same algorithm as {{jsxref("Temporal/PlainYearMonth/from", "Temporal.PlainYearMonth.from()")}}.

### Return value

`true` if this year-month is equal to `other` both in their date value and their calendar, `false` otherwise.

## Examples

### Using equals()

```js
const ym1 = Temporal.PlainYearMonth.from("2021-08");
const ym2 = Temporal.PlainYearMonth.from({ year: 2021, month: 8 });
console.log(ym1.equals(ym2)); // true

const ym3 = Temporal.PlainYearMonth.from("2021-08-01[u-ca=japanese]");
console.log(ym1.equals(ym3)); // false

const ym4 = Temporal.PlainYearMonth.from("2021-09");
console.log(ym1.equals(ym4)); // false
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Temporal.PlainYearMonth")}}
- {{jsxref("Temporal/PlainYearMonth/compare", "Temporal.PlainYearMonth.compare()")}}
