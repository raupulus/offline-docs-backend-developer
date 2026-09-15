---
title: Overview of installing Docker Compose
description: Learn how to install Docker Compose. Compose is available natively on
  Docker Desktop, as a Docker Engine plugin, and as a standalone tool.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/compose/install/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: compose
order: 2700
---

This page summarizes the different ways you can install Docker Compose, depending on your platform and needs.

## Installation scenarios 

### Docker Desktop (Recommended)

The easiest and recommended way to get Docker Compose is to install Docker Desktop. 

Docker Desktop includes Docker Compose along with Docker Engine and Docker CLI which are Compose prerequisites. 

Docker Desktop is available for:
- [Linux](../../desktop/setup/install/linux/index.md)
- [Mac](../../desktop/setup/install/mac-install.md)
- [Windows](../../desktop/setup/install/windows-install.md)

> [!TIP]
> 
> If you have already installed Docker Desktop, you can check which version of Compose you have by selecting **About Docker Desktop** from the Docker menu {{< inline-image src="../../desktop/images/whale-x.svg" alt="whale menu" >}}.

### Plugin (Linux only)

> [!IMPORTANT]
>
> This method is only available on Linux.

If you already have Docker Engine and Docker CLI installed, you can install the Docker Compose plugin from the command line, by either:
- [Using Docker's repository](linux.md#install-using-the-repository)
- [Downloading and installing manually](linux.md#install-the-plugin-manually)

### Standalone (Legacy)

> [!WARNING]
>
> This install scenario is not recommended and is only supported for backward compatibility purposes.

You can [install the Docker Compose standalone](standalone.md) on Linux or on Windows Server.
