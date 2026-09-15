---
title: Environment variables in Compose
description: Explains how to set, use, and manage environment variables in Docker
  Compose.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/compose/how-tos/environment-variables/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: compose
order: 2480
---

Environment variables and interpolation in Docker Compose help you create reusable, flexible configurations. This makes Dockerized applications easier to manage and deploy across environments.

> [!TIP]
>
> Before using environment variables, read through all of the information first to get a full picture of environment variables in Docker Compose.

This section covers:

- [How to set environment variables within your container's environment](set-environment-variables.md).
- [How environment variable precedence works within your container's environment](envvars-precedence.md).
- [Pre-defined environment variables](envvars.md).

It also covers: 
- How [interpolation](variable-interpolation.md) can be used to set variables within your Compose file and how it relates to a container's environment.
- Some [best practices](best-practices.md).
