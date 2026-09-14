---
title: 'SyntaxError: Unexpected ''#'' used outside of class body'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/hash_outside_class/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 920
---

The JavaScript exception "Unexpected '#' used outside of class body" occurs when a hash
("#") is encountered in an unexpected context, most notably
[outside of a class declaration](/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements).
Hashes are valid at the beginning of a file as a [hashbang comment](/en-US/docs/Web/JavaScript/Reference/Lexical_grammar),
or inside of a class as part of a private field. You may encounter this error if you forget
the quotation marks when trying to access a DOM identifier as well.

## Message

```plain
SyntaxError: Unexpected '#' used outside of class body.
```

## Error type

{{jsxref("SyntaxError")}}

## What went wrong?

We encountered a `#` somewhere unexpected. This may be due to code moving around and no
longer being part of a class, a hashbang comment found on a line other than the first
line of a file, or accidentally forgetting the quotation marks around a DOM identifier.

## Examples

### Missing quotation marks

For each case, there might be something slightly wrong. For example

```js-nolint example-bad
document.querySelector(#some-element)
```

This can be fixed via

```js example-good
document.querySelector("#some-element");
```

### Outside of a class

```js-nolint example-bad
class ClassWithPrivateField {
  #privateField;

  constructor() {}
}

this.#privateField = 42;
```

This can be fixed by moving the private field back into the class

```js example-good
class ClassWithPrivateField {
  #privateField;

  constructor() {
    this.#privateField = 42;
  }
}
```

## See also

- {{jsxref("SyntaxError")}}
