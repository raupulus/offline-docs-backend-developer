---
title: Local registry with GitHub Actions
description: Create and use a local OCI registry with GitHub Actions
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/build/ci/github-actions/local-registry.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: build
order: 1960
---

For testing purposes you may need to create a [local registry](https://hub.docker.com/_/registry)
to push images into:

```yaml
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    services:
      registry:
        image: registry:3
        ports:
          - 5000:5000
    steps:
      - name: Set up QEMU
        uses: docker/setup-qemu-action@{{% param "setup_qemu_action_version" %}}
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
        with:
          driver-opts: network=host
      
      - name: Build and push to local registry
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          push: true
          tags: localhost:5000/name/app:latest
      
      - name: Inspect
        run: |
          docker buildx imagetools inspect localhost:5000/name/app:latest
```
