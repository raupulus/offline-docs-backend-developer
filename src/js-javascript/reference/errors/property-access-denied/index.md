---
title: 'Error: Permission denied to access property "x"'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/property_access_denied/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 1360
---

The JavaScript exception "Permission denied to access property" occurs when there was
an attempt to access an object for which you have no permission.

## Message

```plain
DOMException: Blocked a frame with origin "x" from accessing a cross-origin frame. (Chromium-based)
DOMException: Permission denied to access property "x" on cross-origin object (Firefox)
SecurityError: Blocked a frame with origin "x" from accessing a cross-origin frame. Protocols, domains, and ports must match. (Safari)
```

## Error type

{{domxref("DOMException")}}.

## What went wrong?

There was attempt to access an object for which you have no permission. This is likely
an {{HTMLElement("iframe")}} element loaded from a different domain for which you
violated the [same-origin policy](/en-US/docs/Web/Security/Defenses/Same-origin_policy).

## Examples

### No permission to access document

```html
<iframe id="myframe" src="http://www1.w3c-test.org/common/blank.html"></iframe>
```

```js
console.log(frames[0].document);
// Error: Permission denied to access property "document"
```

## See also

- {{HTMLElement("iframe")}}
- [Same-origin policy](/en-US/docs/Web/Security/Defenses/Same-origin_policy)
