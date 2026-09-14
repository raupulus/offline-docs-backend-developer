---
title: Publish & Share Your Module
description: Join the Nuxt module ecosystem and publish your module to npm.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 3.guide/4.modules/8.ecosystem.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: guide
order: 8
---

The [Nuxt module ecosystem](/modules) represents more than 35 million monthly NPM downloads and provides extended functionalities and integrations with all sort of tools. You can be part of this ecosystem!

::tip{icon="i-lucide-video" to="https://vueschool.io/lessons/exploring-nuxt-modules-ecosystem-and-module-types?friend=nuxt" target="_blank"}
Watch Vue School video about Nuxt module types.
::

## Understand Module Types

**Official modules** are modules prefixed (scoped) with `@nuxt/` (e.g. [`@nuxt/content`](https://content.nuxt.com)). They are made and maintained actively by the Nuxt team. Like with the framework, contributions from the community are more than welcome to help make them better!

**Community modules** are modules prefixed (scoped) with `@nuxtjs/` (e.g. [`@nuxtjs/tailwindcss`](https://tailwindcss.nuxtjs.org)). They are proven modules made and maintained by community members. Again, contributions are welcome from anyone.

**Third-party and other community modules** are modules (often) prefixed with `nuxt-`. Anyone can make them, using this prefix allows these modules to be discoverable on npm. This is the best starting point to draft and try an idea!

**Private or personal modules** are modules made for your own use case or company. They don't need to follow any naming rules to work with Nuxt and are often seen scoped under an npm organization (e.g. `@my-company/nuxt-auth`)

## List Your Module

Any community modules are welcome to be listed on [the module list](/modules). To be listed, [open an issue in the nuxt/modules](https://github.com/nuxt/modules/issues/new?template=module_request.yml) repository. The Nuxt team can help you to apply best practices before listing.

## Join `nuxt-modules`

By moving your modules to [nuxt-modules](https://github.com/nuxt-modules), there is always someone else to help, and this way, we can join forces to make one perfect solution.

If you have an already published and working module, and want to transfer it to `nuxt-modules`, [open an issue in nuxt/modules](https://github.com/nuxt/modules/issues/new).

By joining `nuxt-modules` we can rename your community module under the `@nuxtjs/` scope and provide a subdomain (e.g. `my-module.nuxtjs.org`) for its documentation.
