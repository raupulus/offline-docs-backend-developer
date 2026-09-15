---
title: Configure Docker Sandboxes
description: Configure credentials, project environments, GPU passthrough, registry
  mirrors, and upstream proxy settings for Docker Sandboxes.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/ai/sandboxes/configuration/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: ai
order: 810
---

Configure credentials and how Docker Sandboxes run for a project, host, or
network environment. These settings control sandbox creation, authentication,
and connectivity. To change the tools and agent configuration inside a
sandbox, see [Customize](../customize/).

- [Credentials](credentials.md) configures API keys, authentication
  credentials, and registry access for sandboxed agents.
- [Environment files](environment-files.md) declare reusable project
  configuration in `sbxenv.yaml`.
- [GPU passthrough](gpu-passthrough.md) configures a Linux host and sandbox for
  NVIDIA GPU workloads.
- [Registry mirror](registry-mirror.md) routes Docker Hub template, kit, and
  in-sandbox Docker image pulls through an organization's registry mirror.
- [Upstream proxy](upstream-proxy.md) routes sandbox and daemon traffic through
  an operating system or corporate proxy.
