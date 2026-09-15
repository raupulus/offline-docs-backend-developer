---
title: Docker Engine
description: Find a comprehensive overview of Docker Engine, including how to install,
  storage details, networking, and more
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/engine/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: engine
order: 4590
---

Docker Engine is an open source containerization technology for building and
containerizing your applications. Docker Engine acts as a client-server
application with:

- A server with a long-running daemon process
  [`dockerd`](/reference/cli/dockerd).
- APIs which specify interfaces that programs can use to talk to and instruct
  the Docker daemon.
- A command line interface (CLI) client
  [`docker`](/reference/cli/docker/).

The CLI uses [Docker APIs](../reference/api/engine/index.md) to control or interact with the Docker
daemon through scripting or direct CLI commands. Many other Docker applications
use the underlying API and CLI. The daemon creates and manages Docker objects,
such as images, containers, networks, and volumes.

For more details, see
[Docker Architecture](/get-started/docker-overview.md#docker-architecture).

{{< grid >}}

## Licensing

Commercial use of Docker Engine obtained via Docker Desktop
within larger enterprises (exceeding 250 employees OR with annual revenue surpassing
$10 million USD), requires a [paid subscription](https://www.docker.com/pricing?ref=Docs&refAction=DocsEngine).
Apache License, Version 2.0. See [LICENSE](https://github.com/moby/moby/blob/master/LICENSE) for the full license.
