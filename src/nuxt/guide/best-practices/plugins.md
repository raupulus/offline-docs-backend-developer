---
title: Nuxt Plugins
description: Best practices when using Nuxt plugins.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 3.guide/2.best-practices/plugins.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: guide
order: 620
---

Plugins in Nuxt allow you to extend your application with additional functionality. However, improper use can lead to performance bottlenecks. This guide outlines best practices to optimize your Nuxt plugins.

## Avoid Costly Plugin Setup

A large number of plugins can cause performance issues, especially if they require expensive computations or take too long to initialize. Since plugins run during the hydration phase, inefficient setups can block rendering and degrade the user experience.

## Use Composition Whenever Possible

Whenever possible, favor composition over plugins. Just like in Vue, many utilities and composables can be used directly without the need for a plugin. This keeps your project lightweight and improves maintainability.

## If `async`, Enable `parallel`

By default, all plugins loads synchronously.
When defining asynchronous plugins, setting `parallel: true` allows multiple plugins to load concurrently, improving performance by preventing blocking operations.
