---
title: 'SyntaxError: getter and setter for private name #x should either be both static
  or non-static'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/either_be_both_static_or_non-static/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 860
---

The JavaScript exception "mismatched placement" occurs when a private [getter](/en-US/docs/Web/JavaScript/Reference/Functions/get) and [setter](/en-US/docs/Web/JavaScript/Reference/Functions/set) are mismatched in whether or not they are {{jsxref("Classes/static", "static")}}.

## Message

```plain
SyntaxError: Identifier '#x' has already been declared (V8-based)
SyntaxError: getter and setter for private name #x should either be both static or non-static (Firefox)
SyntaxError: Cannot declare a private non-static getter if there is a static private setter with used name. (Safari)
```

## Error type

{{jsxref("SyntaxError")}}

## What went wrong?

Private [getters](/en-US/docs/Web/JavaScript/Reference/Functions/get) and [setters](/en-US/docs/Web/JavaScript/Reference/Functions/set) for the same name must either be both {{jsxref("Classes/static", "static")}}, or both non-static. This limitation does not exist for public methods.

## Examples

### Mismatched placement

```js-nolint example-bad
class Test {
  static set #foo(_) {}
  get #foo() {}
}

// SyntaxError: getter and setter for private name #foo should either be both static or non-static
```

Since `foo` is [private](/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements), the methods must be either both {{jsxref("Classes/static", "static")}}:

```js example-good
class Test {
  static set #foo(_) {}
  static get #foo() {}
}
```

or non-static:

```js example-good
class Test {
  set #foo(_) {}
  get #foo() {}
}
```

## See also

- {{jsxref("Functions/get", "get")}}
- {{jsxref("Functions/set", "set")}}
- {{jsxref("Classes/static", "static")}}
- [Private elements](/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
