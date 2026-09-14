---
title: Conditional Rendering
source_repo: vuejs/docs
source_ref: main
source_commit: b75d188ab
source_path: tutorial/src/step-6/description.md
technology: vue
version: main
license: MIT
retrieved_at: '2026-08-02'
section: tutorial
order: 1060
---

# Conditional Rendering {#conditional-rendering}

We can use the `v-if` directive to conditionally render an element:

```vue-html
<h1 v-if="awesome">Vue is awesome!</h1>
```

This `<h1>` will be rendered only if the value of `awesome` is [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy). If `awesome` changes to a [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy) value, it will be removed from the DOM.

We can also use `v-else` and `v-else-if` to denote other branches of the condition:

```vue-html
<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
```

Currently, the demo is showing both `<h1>`s at the same time, and the button does nothing. Try to add `v-if` and `v-else` directives to them, and implement the `toggle()` method so that we can use the button to toggle between them.

More details on `v-if`: <a target="_blank" href="/guide/essentials/conditional.html">Guide - Conditional Rendering</a>
