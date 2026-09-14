---
title: setResponseStatus
description: setResponseStatus sets the status (and optionally the statusText) of
  the response.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/3.utils/set-response-status.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1670
---

Nuxt provides composables and utilities for first-class server-side-rendering support.

`setResponseStatus` sets the status (and optionally the statusText) of the response.

::important
`setResponseStatus` can only be called in the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context).
::

```ts
const event = useRequestEvent()

// event will be undefined in the browser
if (event) {
  // Set the status code to 404 for a custom 404 page
  setResponseStatus(event, 404)

  // Set the status message as well
  setResponseStatus(event, 404, 'Page Not Found')
}
```

::note
In the browser, `setResponseStatus` will have no effect.
::

:read-more{to="/docs/4.x/getting-started/error-handling"}
