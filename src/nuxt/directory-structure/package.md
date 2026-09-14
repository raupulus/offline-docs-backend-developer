---
title: package.json
description: The package.json file contains all the dependencies and scripts for your
  application.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 2.directory-structure/3.package.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: directory-structure
order: 3
---

The minimal `package.json` of your Nuxt application should looks like:

```json [package.json]
{
  "name": "nuxt-app",
  "private": true,
  "type": "module",
  "scripts": {
    "build": "nuxt build",
    "dev": "nuxt dev",
    "generate": "nuxt generate",
    "preview": "nuxt preview",
    "postinstall": "nuxt prepare"
  },
  "dependencies": {
    "nuxt": "latest",
    "vue": "latest",
    "vue-router": "latest"
  }
}
```

::read-more{icon="i-simple-icons-npm" to="https://docs.npmjs.com/cli/configuring-npm/package-json/" target="_blank"}
Read more about the `package.json` file.
::
