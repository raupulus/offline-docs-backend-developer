---
title: Date.prototype.toISOString()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/date/toisostring/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 3690
---

The **`toISOString()`** method of {{jsxref("Date")}} instances returns a string representing this date in the [date time string format](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format), a _simplified_ format based on [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), which is always 24 or 27 characters long (`YYYY-MM-DDTHH:mm:ss.sssZ` or `±YYYYYY-MM-DDTHH:mm:ss.sssZ`, respectively). The timezone is always UTC, as denoted by the suffix `Z`.

{{InteractiveExample("JavaScript Demo: Date.prototype.toISOString()")}}

```js interactive-example
const event = new Date("05 October 2011 14:48 UTC");
console.log(event.toString());
// Expected output: "Wed Oct 05 2011 16:48:00 GMT+0200 (CEST)"
// Note: your timezone may vary

console.log(event.toISOString());
// Expected output: "2011-10-05T14:48:00.000Z"
```

## Syntax

```js-nolint
toISOString()
```

### Parameters

None.

### Return value

A string representing the given date in the [date time string format](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format) according to universal time. It's the same format as the one required to be recognized by {{jsxref("Date.parse()")}}.

### Exceptions

- {{jsxref("RangeError")}}
  - : Thrown if the date is [invalid](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date) or if it corresponds to a year that cannot be represented in the date string format.

## Examples

### Using toISOString()

```js
const d = new Date(0);

console.log(d.toISOString()); // "1970-01-01T00:00:00.000Z"
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Date.prototype.toLocaleDateString()")}}
- {{jsxref("Date.prototype.toString()")}}
- {{jsxref("Date.prototype.toUTCString()")}}
