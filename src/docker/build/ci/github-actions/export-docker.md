---
title: Export to Docker with GitHub Actions
description: Load the build results to the image store with GitHub Actions
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/build/ci/github-actions/export-docker.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: build
order: 1910
---

You may want your build result to be available in the Docker client through
`docker images` to be able to use it in another step of your workflow:

```yaml
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
      
      - name: Build
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          load: true
          tags: myimage:latest
      
      - name: Inspect
        run: |
          docker image inspect myimage:latest
```
