---
title: pnpm star
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: cli/star.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
section: cli
order: 710
---

Added in: v11.0.0

Mark a package as a favorite on the registry. You must be logged in (see [`pnpm login`](login.md)).

```sh
pnpm star <pkg>
```

## pnpm unstar

Remove a package from your favorites.

```sh
pnpm unstar <pkg>
```

## pnpm stars

List the packages you (or another user) have starred.

```sh
pnpm stars [<user>]
```

When run without a username, pnpm lists the packages starred by the currently authenticated user.
