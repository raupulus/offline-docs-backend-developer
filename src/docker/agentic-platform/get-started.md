---
title: Get started with Docker Agentic Platform
description: Choose an environment and start a Docker Agentic Platform sandbox.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/agentic-platform/get-started.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: agentic-platform
order: 290
---

The Docker Agentic Platform launcher collects the configuration needed to start
an isolated sandbox.

## Before you begin

You need a Docker account and access to Docker Agentic Platform. The launcher
prompts for a model provider API key when needed. You can add the key under
**Secrets** before creating the sandbox or provide it in the launcher when
prompted.

The available sandbox types are Claude Code, Codex, OpenCode, Copilot, Gemini
CLI, and Shell. The supported model provider credentials are Anthropic, OpenAI,
GitHub Copilot, Google, Groq, and xAI.

## Start a sandbox

1. Open [Docker Agentic Platform](https://agentic-platform.docker.com/) and
   select **New**.
2. Choose a sandbox type and add any requested model credential. Copilot uses
   `GITHUB_TOKEN`; add the same GitHub secret to any other sandbox type that
   needs private repository access.
3. Configure the sandbox. The initial settings are **open access**, **no tools
   added**, and **medium compute**.
4. Choose whether Docker stops or deletes the sandbox when its timer expires,
   and set the timer from 1 to 24 hours.
5. Review the configuration and select **Run**.

You cannot change the sandbox's authentication, tools, access policy, or compute
size after it starts. Docker creates the sandbox, marks it as running, and opens
its terminal.

Use the terminal to interact with the sandbox.

Return to **Sandboxes** to find the running sandbox and reopen its terminal.

## Next steps

- [Manage sandboxes](sandboxes.md)
- [Connect MCP servers](mcp.md)
- [Manage secrets](secrets.md)
- [Manage network policies](policies.md)
