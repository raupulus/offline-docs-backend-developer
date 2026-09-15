---
title: MCP
description: Connect predefined and custom MCP servers for Docker Agentic Platform
  sandboxes.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/agentic-platform/mcp.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: agentic-platform
order: 300
---

Model Context Protocol (MCP) servers connect agents to external services and
expose operations from those services as tools. From the **MCP** page, connect a
predefined server or add a custom server by URL. Complete authorization when a
server requires it.

MCP configuration grants agents tools they can invoke. It does not restrict or
inspect ordinary network access from a sandbox. Use
[network policies](policies.md) to control outbound
destinations. MCP-specific policies are not part of the initial release.

## Connect a predefined server

1. Open **MCP** and choose a predefined server.
2. Connect the server.
3. Complete authorization if prompted.

## Add a server by URL

To connect a server that is not predefined:

1. Open **MCP**.
2. Choose the option to add a server and enter its URL.
3. Connect the server and complete authorization if prompted.
