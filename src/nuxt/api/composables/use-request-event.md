---
title: useRequestEvent
description: Access the incoming request event with the useRequestEvent composable.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/2.composables/use-request-event.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1270
---

Within the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context) you can use `useRequestEvent` to access the incoming request.

```ts
// Get underlying request event
const event = useRequestEvent()

// Get the URL
const url = event?.path
```

::tip
In the browser, `useRequestEvent` will return `undefined`.
::
