---
title: Working with Git
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: git.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
order: 950
---

## Lockfiles

You should always commit the lockfile (`pnpm-lock.yaml`). This is for a
multitude of reasons, the primary of which being:
- it enables faster installation for CI and production environments, due to
being able to skip package resolution
- it enforces consistent installations and resolution between development,
testing, and production environments, meaning the packages used in testing
and production will be exactly the same as when you developed your project

### Merge conflicts

pnpm can automatically resolve merge conflicts in `pnpm-lock.yaml`.
If you have conflicts, just run `pnpm install` and commit the changes.

Be warned, however. It is advised that you review the changes prior to
staging a commit, because we cannot guarantee that pnpm will choose the correct
head - it instead builds with the most updated of lockfiles, which is ideal in
most cases.
