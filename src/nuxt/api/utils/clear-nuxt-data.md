---
title: clearNuxtData
description: Delete cached data, error status and pending promises of useAsyncData
  and useFetch.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/3.utils/clear-nuxt-data.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 1460
---

::note
This method is useful if you want to invalidate the data fetching for another page.
::

## Type

```ts [Signature]
export function clearNuxtData (keys?: string | string[] | ((key: string) => boolean)): void
```

## Parameters

* `keys`: One or an array of keys that are used in [`useAsyncData`](/docs/4.x/api/composables/use-async-data) to delete their cached data. If no keys are provided, **all data** will be invalidated.
