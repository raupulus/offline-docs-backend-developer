---
title: Copilot
description: 'Use GitHub Copilot in Docker Sandboxes with GitHub token authentication
  and

  trusted folder configuration.'
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/ai/sandboxes/agents/copilot.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: ai
order: 710
---

This guide covers authentication, configuration, and usage of GitHub Copilot
in a sandboxed environment.

Official documentation: [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli)

## Quick start

> [!NOTE]
> In Docker Sandboxes v0.42, use `sbx run docker.io/sbx/copilot-kit:latest`.
> The `copilot` shorthand is unavailable in this release.

Create a sandbox and run Copilot for a project directory:

```console
$ sbx run copilot ~/my-project
```

The workspace parameter is optional and defaults to the current directory:

```console
$ cd ~/my-project
$ sbx run copilot
```

## Authentication

Copilot requires a GitHub token with Copilot access. Store your token using
[stored secrets](../configuration/credentials.md#stored-secrets):

```console
$ sbx secret set github --command 'gh auth token'
```

## Configuration

Sandboxes don't pick up user-level configuration from your host. Only
project-level configuration in the working directory is available inside the
sandbox. See
[Why doesn't the sandbox use my user-level agent configuration?](../faq.md#why-doesnt-the-sandbox-use-my-user-level-agent-configuration)
for workarounds.

Copilot is configured to trust the workspace directory by default, so it
operates without repeated confirmations for workspace files.

### Default startup command

Without extra args, the sandbox runs:

```text
copilot --yolo
```

Arguments after `--` are added after the default flags when the first one is
itself a flag (begins with `-`), so `--yolo` is preserved:

```console
$ sbx run copilot -- -p "review this PR"   # runs copilot --yolo -p "review this PR"
```

When the first argument is a bare word — a subcommand or prompt — it replaces
the defaults instead.

## Base image

Template: `docker/sandbox-templates:copilot`

Preconfigured to trust the workspace directory.

See [Customize](../customize/) to pre-install tools or customize this
environment.
