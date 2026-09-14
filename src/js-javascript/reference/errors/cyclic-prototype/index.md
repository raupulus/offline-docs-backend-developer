---
title: 'TypeError: can''t set prototype: it would cause a prototype chain cycle'
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/errors/cyclic_prototype/index.md
technology: js-javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 780
---

The JavaScript exception "TypeError: can't set prototype: it would cause a prototype chain cycle" occurs when an object's prototype is set to an object such that the [prototype chain](/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects/Object_prototypes#the_prototype_chain) becomes circular (`a` and `b` both have each other in their prototype chains).

## Message

```plain
TypeError: Cyclic __proto__ value (V8-based)
TypeError: can't set prototype: it would cause a prototype chain cycle (Firefox)
TypeError: cyclic __proto__ value (Safari)
```

## Error type

{{jsxref("TypeError")}}

## What went wrong?

A loop, also called a cycle, was introduced in a prototype chain. That means that when walking this prototype chain, the same place would be accessed over and over again, instead of eventually reaching `null`.

This error is thrown at the time of setting the prototype. In an operation like `Object.setPrototypeOf(a, b)`, if `a` already exists in the prototype chain of `b`, this error will be thrown.

## Examples

```js example-bad
const a = {};
Object.setPrototypeOf(a, a);
// TypeError: can't set prototype: it would cause a prototype chain cycle
```

```js example-bad
const a = {};
const b = {};
const c = {};
Object.setPrototypeOf(a, b);
Object.setPrototypeOf(b, c);
Object.setPrototypeOf(c, a);
// TypeError: can't set prototype: it would cause a prototype chain cycle
```

## See also

- [Object Prototypes](/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects/Object_prototypes)
- [Inheritance and the prototype chain](/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
