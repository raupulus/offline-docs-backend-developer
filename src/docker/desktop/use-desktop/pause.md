---
title: Pause Docker Desktop
description: understand what pausing Docker Desktop Dashboard means
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/desktop/use-desktop/pause.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: desktop
order: 3470
---

Pausing Docker Desktop temporarily suspends the Linux VM running Docker Engine. This saves the current state of all containers in memory and freezes all running processes, significantly reducing CPU and memory usage which is helpful for conserving battery on laptops.

To pause Docker Desktop, select the **Pause** icon to the left of the footer in the Docker Dashboard. To manually resume Docker Desktop, select the **Resume** option in the Docker menu, or run any Docker CLI command.

When you manually pause Docker Desktop, a paused status displays on the Docker menu and on the Docker Desktop Dashboard. You can still access the **Settings** and the **Troubleshoot** menu.

> [!TIP]
>
> The Resource Saver feature is enabled by default and provides better CPU and memory savings than the manual Pause feature. See [Resource Saver mode](resource-saver.md) for more info.
