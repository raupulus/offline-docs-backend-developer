---
title: debugger
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/statements/debugger/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 13040
---

The **`debugger`** statement invokes any available debugging
functionality, such as setting a breakpoint. If no debugging functionality is available,
this statement has no effect.

## Syntax

```js-nolint
debugger;
```

## Examples

### Using the debugger statement

The following example shows code where a `debugger` statement has been
inserted, to invoke a debugger (if one exists) when the function is called.

```js
function potentiallyBuggyCode() {
  debugger;
  // do potentially buggy stuff to examine, step through, etc.
}
```

When the debugger is invoked, execution is paused at the `debugger`
statement. It is like a breakpoint in the script source.

![A browser with developer tools open to the debugger panel showing how execution is paused at the debugger statement to allow close inspection of variables, scopes, events, etc.](screen_shot_2014-02-07_at_9.14.35_am.png)

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- [The Firefox JavaScript Debugger¶](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html) in the Firefox source docs
