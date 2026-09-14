---
title: Logging
description: Nuxt Kit provides a set of utilities to help you work with logging. These
  functions allow you to log messages with extra features.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 4.api/5.kit/14.logging.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: api
order: 14
---

Nuxt provides a logger instance that you can use to log messages with extra features. `useLogger` allows you to get a logger instance.

## `useLogger`

Returns a logger instance. It uses [consola](https://github.com/unjs/consola) under the hood.

### Usage

```ts twoslash
import { defineNuxtModule, useLogger } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options, nuxt) {
    const logger = useLogger('my-module')

    logger.info('Hello from my module!')
  },
})
```

### Type

```ts
function useLogger (tag?: string, options?: Partial<ConsolaOptions>): ConsolaInstance
```

### Parameters

**`tag`**: A tag to suffix all log messages with, displayed on the right near the timestamp.

**`options`**: Consola configuration options.

### Example

```ts twoslash
import { defineNuxtModule, useLogger } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options, nuxt) {
    const logger = useLogger('my-module', { level: options.quiet ? 0 : 3 })

    logger.info('Hello from my module!')
  },
})
```
