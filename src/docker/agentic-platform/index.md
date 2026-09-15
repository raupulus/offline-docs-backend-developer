---
title: Docker Agentic Platform
description: Run agents and tools in isolated, hosted sandboxes with Docker Agentic
  Platform.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/agentic-platform/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: agentic-platform
order: 270
---

> [!NOTE]
> Docker Agentic Platform is experimental. Features and behavior may change.

Docker Agentic Platform runs agents and agent-powered tools in isolated
sandboxes on Docker-managed cloud infrastructure. An active workload is not
tied to your computer remaining awake or connected. You can leave the Console
and return to the sandbox while the agent continues working.

For sandboxes that run on your development machine through the `sbx` CLI, see
[Docker Sandboxes](../ai/sandboxes/index.md).

From the web Console, choose the type of sandbox to run and configure its model
credential, network access, tools, and compute. Docker creates the sandbox and
opens a live terminal for interacting with the agent. The **Sandboxes** page
provides one place to return to and manage your running and paused workloads.

Account-level configuration can be reused across sandboxes:

- [MCP](mcp.md) connects external tools.
- [Secrets](secrets.md) provide credentials
  without placing their values inside a sandbox.
- [Network policies](policies.md) control
  outbound destinations.

To begin, open [Docker Agentic Platform](https://agentic-platform.docker.com/)
and sign in with your Docker account. Docker meters sandbox compute per second.
For account and payment information, see [Docker Billing](/subscription-billing/).

{{< grid >}}
