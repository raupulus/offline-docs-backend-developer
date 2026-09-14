---
title: abortNavigation
description: abortNavigation is a helper function that prevents navigation from taking
  place and throws an error if one is set as a parameter.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/3.utils/abort-navigation.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1420
---

::warning
`abortNavigation` is only usable inside a [route middleware handler](/docs/4.x/directory-structure/app/middleware).
::

## Type

```ts [Signature]
export function abortNavigation (err?: Error | string): false
```

## Parameters

### `err`

- **Type**: [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) | `string`

  Optional error to be thrown by `abortNavigation`.

## Example

The example below shows how you can use `abortNavigation` in a route middleware to prevent unauthorized route access:

```ts [app/middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const user = useState('user')

  if (!user.value.isAuthorized) {
    return abortNavigation()
  }

  if (to.path !== '/edit-post') {
    return navigateTo('/edit-post')
  }
})
```

### `err` as a String

You can pass the error as a string:

```ts [app/middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const user = useState('user')

  if (!user.value.isAuthorized) {
    return abortNavigation('Insufficient permissions.')
  }
})
```

### `err` as an Error Object

You can pass the error as an [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) object, e.g. caught by the `catch`-block:

```ts [app/middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  try {
    /* code that might throw an error */
  } catch (err) {
    return abortNavigation(err)
  }
})
```
