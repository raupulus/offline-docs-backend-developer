---
title: .nuxtignore
description: The .nuxtignore file lets Nuxt ignore files in your project’s root directory
  during the build phase.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 2.directory-structure/2.nuxtignore.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: directory-structure
order: 2
---

The `.nuxtignore` file tells Nuxt to ignore files in your project’s root directory ([`rootDir`](/docs/4.x/api/nuxt-config#rootdir)) during the build phase.

It is subject to the same specification as [`.gitignore`](/docs/4.x/directory-structure/gitignore) and `.eslintignore` files, in which each line is a glob pattern indicating which files should be ignored.

::tip
You can also configure [`ignoreOptions`](/docs/4.x/api/nuxt-config#ignoreoptions), [`ignorePrefix`](/docs/4.x/api/nuxt-config#ignoreprefix) and [`ignore`](/docs/4.x/api/nuxt-config#ignore) in your `nuxt.config` file.
::

## Usage

```bash [.nuxtignore]
# ignore layout foo.vue
app/layouts/foo.vue
# ignore layout files whose name ends with -ignore.vue
app/layouts/*-ignore.vue

# ignore page bar.vue
app/pages/bar.vue
# ignore page inside ignore folder
app/pages/ignore/*.vue

# ignore route middleware files under foo folder except foo/bar.js
app/middleware/foo/*.js
!app/middleware/foo/bar.js
```

::read-more{icon="i-simple-icons-git" title="the git documentation" to="https://git-scm.com/docs/gitignore" target="_blank"}
More details about the spec are in the **gitignore documentation**.
::
