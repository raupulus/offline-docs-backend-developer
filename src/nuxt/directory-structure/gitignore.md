---
title: .gitignore
description: A .gitignore file specifies intentionally untracked files that git should
  ignore.
source_repo: nuxt/nuxt
source_ref: main
source_commit: ec5c55e26
source_path: 2.directory-structure/2.gitignore.md
technology: nuxt
version: main
license: MIT
retrieved_at: '2026-08-02'
section: directory-structure
order: 2
---

A `.gitignore` file specifies intentionally untracked files that git should ignore.

:read-more{icon="i-simple-icons-git" title="the git documentation" to="https://git-scm.com/docs/gitignore" target="_blank"}

We recommend having a `.gitignore` file that has **at least** the following entries present:

```bash [.gitignore]
# Nuxt dev/build outputs
.output
.data
.nuxt
.nitro
.cache
dist

# Node dependencies
node_modules

# Logs
logs
*.log

# Misc
.DS_Store

# Local env files
.env
.env.*
!.env.example
```
