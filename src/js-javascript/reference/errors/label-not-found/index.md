---
title: 'SyntaxError: label not found'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/label_not_found/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 1100
---

The JavaScript exception "label not found" occurs when a {{jsxref("Statements/break", "break")}} or {{jsxref("Statements/continue", "continue")}} statement references a label that does not exist on any statement that contains the `break` or `continue` statement.

## Message

```plain
SyntaxError: Undefined label 'label' (V8-based)
SyntaxError: label not found (Firefox)
SyntaxError: Cannot use the undeclared label 'label'. (Safari)
```

## Error type

{{jsxref("SyntaxError")}}.

## What went wrong?

In JavaScript, [labels](/en-US/docs/Web/JavaScript/Reference/Statements/label) are very limited: you can only use them with {{jsxref("Statements/break", "break")}} and {{jsxref("Statements/continue", "continue")}} statements, and you can only jump to them from a statement contained within the labeled statement. You cannot jump to this label from anywhere in the program.

## Examples

### Unsyntactic jump

You cannot use labels as if they are `goto`.

```js-nolint example-bad
start: console.log("Hello, world!");
console.log("Do it again");
break start;
```

Instead, you can only use labels to enhance the normal semantics of `break` and `continue` statements.

```js example-good
start: {
  console.log("Hello, world!");
  if (Math.random() > 0.5) {
    break start;
  }
  console.log("Maybe I'm logged");
}
```

## See also

- [Labeled statement](/en-US/docs/Web/JavaScript/Reference/Statements/label)
