---
title: Date.prototype.getUTCHours()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/date/getutchours/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 3420
---

The **`getUTCHours()`** method of {{jsxref("Date")}} instances returns the hours for this date according to universal time.

{{InteractiveExample("JavaScript Demo: Date.prototype.getUTCHours()")}}

```js interactive-example
const date1 = new Date("December 31, 1975, 23:15:30 GMT+11:00");
const date2 = new Date("December 31, 1975, 23:15:30 GMT-11:00");

console.log(date1.getUTCHours());
// Expected output: 12

console.log(date2.getUTCHours());
// Expected output: 10
```

## Syntax

```js-nolint
getUTCHours()
```

### Parameters

None.

### Return value

An integer, between 0 and 23, representing the hours for the given date according to universal time. Returns `NaN` if the date is [invalid](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date).

## Examples

### Using getUTCHours()

The following example assigns the hours portion of the current time to the variable `hours`.

```js
const today = new Date();
const hours = today.getUTCHours();
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Date.prototype.getHours()")}}
- {{jsxref("Date.prototype.setUTCHours()")}}
