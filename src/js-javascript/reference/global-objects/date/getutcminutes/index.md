---
title: Date.prototype.getUTCMinutes()
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/date/getutcminutes/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 3440
---

The **`getUTCMinutes()`** method of {{jsxref("Date")}} instances returns the minutes for this date according to universal time.

{{InteractiveExample("JavaScript Demo: Date.prototype.getUTCMinutes()")}}

```js interactive-example
const date1 = new Date("1 January 2000 03:15:30 GMT+07:00");
const date2 = new Date("1 January 2000 03:15:30 GMT+03:30");

console.log(date1.getUTCMinutes()); // 31 Dec 1999 20:15:30 GMT
// Expected output: 15

console.log(date2.getUTCMinutes()); // 31 Dec 1999 23:45:30 GMT
// Expected output: 45
```

## Syntax

```js-nolint
getUTCMinutes()
```

### Parameters

None.

### Return value

An integer, between 0 and 59, representing the minutes for the given date according to universal time. Returns `NaN` if the date is [invalid](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date).

## Examples

### Using getUTCMinutes()

The following example assigns the minutes portion of the current time to the variable `minutes`.

```js
const today = new Date();
const minutes = today.getUTCMinutes();
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Date.prototype.getMinutes()")}}
- {{jsxref("Date.prototype.setUTCMinutes()")}}
